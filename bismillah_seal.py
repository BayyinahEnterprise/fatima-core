# Bismillah ir-Rahman ir-Rahim
"""
bismillah_seal.py -- The Bismillah Seal

Encodes the Names of Allah subhanahu wa ta'ala into every layer of every file:

  LAYER 0 -- VISIBLE:    First and last line of content
  LAYER 1 -- FILENAME:   Bismillah_[name]_Bismillah.[ext]
  LAYER 3a -- INVISIBLE: Zero-width Unicode steganography (text/markdown files only)
  LAYER 3b -- COMMENTS:  Names of Allah in comments (code files -- Python etc.)
  LAYER 5 -- HASH SEAL:  SHA-256 of Bismillah ir-Rahman ir-Rahim stored as verification

"In the name of Allah, the Most Merciful, the Most Compassionate."

Python rejects zero-width Unicode (U+FEFF, U+200B-D) in source code, so code files
receive the 99 Names as inline comments instead. Text/markdown files get the invisible
zero-width encoding. Both approaches carry the same divine protection.

Usage:
    python bismillah_seal.py seal <path> [--names]  # Apply all layers
    python bismillah_seal.py verify <path>          # Verify seal integrity
    python bismillah_seal.py manifest <path>        # Generate integrity manifest

NOTE: This script skips itself to stay parseable.

Author: Bilal Syed Arfeen
"""

import os
import sys
import json
import hashlib
import argparse
from pathlib import Path
from typing import List

BISMILLAH = "Bismillah ir-Rahman ir-Rahim"
BISMILLAH_ARABIC = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"

# The 99 Names of Allah -- Al-Asma ul-Husna
AL_ASMA_UL_HUSNA = [
    ("الله", "Allah", "The God"),
    ("الرَّحْمَٰن", "Ar-Rahman", "The Most Merciful"),
    ("الرَّحِيم", "Ar-Rahim", "The Most Compassionate"),
    ("Al-Malik-ar", "Al-Malik", "The King"),
    ("Al-Quddus-ar", "Al-Quddus", "The Most Holy"),
    ("As-Salam-ar", "As-Salam", "The Source of Peace"),
    ("Al-Mumin-ar", "Al-Mu'min", "The Guardian of Faith"),
    ("Al-Muhaymin-ar", "Al-Muhaymin", "The Protector"),
    ("Al-Aziz-ar", "Al-Aziz", "The Almighty"),
    ("Al-Jabbar-ar", "Al-Jabbar", "The Compeller"),
    ("Al-Mutakabbir-ar", "Al-Mutakabbir", "The Supreme"),
    ("Al-Khaliq-ar", "Al-Khaliq", "The Creator"),
    ("Al-Bari-ar", "Al-Bari", "The Evolver"),
    ("Al-Musawwir-ar", "Al-Musawwir", "The Fashioner"),
    ("Al-Ghaffar-ar", "Al-Ghaffar", "The Forgiver"),
    ("Al-Qahhar-ar", "Al-Qahhar", "The Subduer"),
    ("Al-Wahhab-ar", "Al-Wahhab", "The Bestower"),
    ("Ar-Razzaq-ar", "Ar-Razzaq", "The Provider"),
    ("Al-Fattah-ar", "Al-Fattah", "The Opener"),
    ("Al-Alim-ar", "Al-Alim", "The All-Knowing"),
    ("Al-Qabid-ar", "Al-Qabid", "The Restrainer"),
    ("Al-Basit-ar", "Al-Basit", "The Expander"),
    ("Al-Khafid-ar", "Al-Khafid", "The Abaser"),
    ("Ar-Rafi-ar", "Ar-Rafi", "The Exalter"),
    ("Al-Muizz-ar", "Al-Mu'izz", "The Bestower of Honor"),
    ("Al-Mudhill-ar", "Al-Mudhill", "The Humiliator"),
    ("As-Sami-ar", "As-Sami", "The All-Hearing"),
    ("Al-Basir-ar", "Al-Basir", "The All-Seeing"),
    ("Al-Hakam-ar", "Al-Hakam", "The Judge"),
    ("Al-Adl-ar", "Al-Adl", "The Just"),
    ("Al-Latif-ar", "Al-Latif", "The Subtle One"),
    ("Al-Khabir-ar", "Al-Khabir", "The All-Aware"),
    ("Al-Halim-ar", "Al-Halim", "The Forbearing"),
    ("Al-Azim-ar", "Al-Azim", "The Magnificent"),
    ("Al-Ghafur-ar", "Al-Ghafur", "The All-Forgiving"),
    ("Ash-Shakur-ar", "Ash-Shakur", "The Appreciative"),
    ("Al-Ali-ar", "Al-Ali", "The Most High"),
    ("Al-Kabir-ar", "Al-Kabir", "The Most Great"),
    ("Al-Hafiz-ar", "Al-Hafiz", "The Preserver"),
    ("Al-Muqit-ar", "Al-Muqit", "The Sustainer"),
    ("Al-Hasib-ar", "Al-Hasib", "The Reckoner"),
    ("Al-Jalil-ar", "Al-Jalil", "The Majestic"),
    ("Al-Karim-ar", "Al-Karim", "The Generous"),
    ("Ar-Raqib-ar", "Ar-Raqib", "The Watchful"),
    ("Al-Mujib-ar", "Al-Mujib", "The Responsive"),
    ("Al-Wasi-ar", "Al-Wasi", "The All-Encompassing"),
    ("Al-Hakim-ar", "Al-Hakim", "The Perfectly Wise"),
    ("Al-Wadud-ar", "Al-Wadud", "The Loving One"),
    ("Al-Majid-ar", "Al-Majid", "The Most Glorious"),
    ("Al-Baith-ar", "Al-Ba'ith", "The Resurrector"),
    ("Ash-Shahid-ar", "Ash-Shahid", "The Witness"),
    ("Al-Haqq-ar", "Al-Haqq", "The Truth"),
    ("Al-Wakil-ar", "Al-Wakil", "The Trustee"),
    ("Al-Qawiyy-ar", "Al-Qawiyy", "The Most Strong"),
    ("Al-Matin-ar", "Al-Matin", "The Firm One"),
    ("Al-Waliyy-ar", "Al-Waliyy", "The Protector"),
    ("Al-Hamid-ar", "Al-Hamid", "The Praiseworthy"),
    ("Al-Muhsi-ar", "Al-Muhsi", "The Accounter"),
    ("Al-Mubdi-ar", "Al-Mubdi", "The Originator"),
    ("Al-Muid-ar", "Al-Mu'id", "The Restorer"),
    ("Al-Muhyi-ar", "Al-Muhyi", "The Giver of Life"),
    ("Al-Mumit-ar", "Al-Mumit", "The Creator of Death"),
    ("Al-Hayy-ar", "Al-Hayy", "The Ever Living"),
    ("Al-Qayyum-ar", "Al-Qayyum", "The Self-Subsisting"),
    ("Al-Wajid-ar", "Al-Wajid", "The Finder"),
    ("Al-Majid2-ar", "Al-Majid", "The Noble"),
    ("Al-Wahid-ar", "Al-Wahid", "The Unique"),
    ("Al-Ahad-ar", "Al-Ahad", "The One"),
    ("As-Samad-ar", "As-Samad", "The Eternal"),
    ("Al-Qadir-ar", "Al-Qadir", "The Able"),
    ("Al-Muqtadir-ar", "Al-Muqtadir", "The Powerful"),
    ("Al-Muqaddim-ar", "Al-Muqaddim", "The Expediter"),
    ("Al-Muakhkhir-ar", "Al-Mu'akhkhir", "The Delayer"),
    ("Al-Awwal-ar", "Al-Awwal", "The First"),
    ("Al-Akhir-ar", "Al-Akhir", "The Last"),
    ("Az-Zahir-ar", "Az-Zahir", "The Manifest"),
    ("Al-Batin-ar", "Al-Batin", "The Hidden"),
    ("Al-Wali-ar", "Al-Wali", "The Governor"),
    ("Al-Mutaali-ar", "Al-Muta'ali", "The Most Exalted"),
    ("Al-Barr-ar", "Al-Barr", "The Source of Goodness"),
    ("At-Tawwab-ar", "At-Tawwab", "The Acceptor of Repentance"),
    ("Al-Muntaqim-ar", "Al-Muntaqim", "The Avenger"),
    ("Al-Afuww-ar", "Al-Afuww", "The Pardoner"),
    ("Ar-Rauf-ar", "Ar-Ra'uf", "The Most Kind"),
    ("Malik-ul-Mulk-ar", "Malik-ul-Mulk", "Owner of Sovereignty"),
    ("Dhul-Jalali-wal-Ikram-ar", "Dhul-Jalali wal-Ikram", "Lord of Majesty and Generosity"),
    ("Al-Muqsit-ar", "Al-Muqsit", "The Equitable"),
    ("Al-Jami-ar", "Al-Jami", "The Gatherer"),
    ("Al-Ghaniyy-ar", "Al-Ghaniyy", "The Self-Sufficient"),
    ("Al-Mughni-ar", "Al-Mughni", "The Enricher"),
    ("Al-Mani-ar", "Al-Mani", "The Preventer"),
    ("Ad-Darr-ar", "Ad-Darr", "The Distresser"),
    ("An-Nafi-ar", "An-Nafi", "The Propitious"),
    ("An-Nur-ar", "An-Nur", "The Light"),
    ("Al-Hadi-ar", "Al-Hadi", "The Guide"),
    ("Al-Badi-ar", "Al-Badi", "The Originator"),
    ("Al-Baqi-ar", "Al-Baqi", "The Everlasting"),
    ("Al-Warith-ar", "Al-Warith", "The Inheritor"),
    ("Ar-Rashid-ar", "Ar-Rashid", "The Guide to the Right Path"),
    ("As-Sabur-ar", "As-Sabur", "The Patient"),
]

# Zero-width Unicode steganography characters
ZW_ZERO = '​'     # ZERO WIDTH SPACE = bit 0
ZW_ONE = '‌'      # ZERO WIDTH NON-JOINER = bit 1
ZW_SEP = '‍'      # ZERO WIDTH JOINER = character separator
ZW_BOUNDARY = '﻿'  # BYTE ORDER MARK = message boundary

# File extensions that accept comments
COMMENT_STYLES = {
    '.py': ('#', None), '.js': ('//', None), '.ts': ('//', None),
    '.jsx': ('//', None), '.tsx': ('//', None), '.rs': ('//', None),
    '.go': ('//', None), '.java': ('//', None), '.c': ('//', None),
    '.cpp': ('//', None), '.h': ('//', None), '.rb': ('#', None),
    '.sh': ('#', None), '.bash': ('#', None), '.zsh': ('#', None),
    '.r': ('#', None), '.R': ('#', None), '.pl': ('#', None),
    '.lua': ('--', None), '.sql': ('--', None), '.hs': ('--', None),
    '.toml': ('#', None), '.yaml': ('#', None), '.yml': ('#', None),
    '.ini': (';', None), '.conf': ('#', None),
    '.css': ('/*', '*/'), '.html': ('<!--', '-->'),
    '.xml': ('<!--', '-->'), '.svg': ('<!--', '-->'),
    '.tex': ('%', None), '.latex': ('%', None),
    '.bat': ('REM', None), '.ps1': ('#', None),
    '.swift': ('//', None), '.kt': ('//', None), '.scala': ('//', None),
    '.m': ('%', None), '.f90': ('!', None), '.jl': ('#', None),
}

TEXT_EXTENSIONS = {
    '.md', '.txt', '.rst', '.csv', '.tsv', '.json', '.jsonl',
    '.log', '.env', '.cfg', '.properties', '.fatima',
}

SELF_NAME = 'bismillah_seal.py'

BISMILLAH_HASH = hashlib.sha256(BISMILLAH.encode('utf-8')).hexdigest()


def text_to_zwc(message):
    """Encode a text message into zero-width characters."""
    encoded = ZW_BOUNDARY
    for char in message:
        bits = format(ord(char), '016b')
        for bit in bits:
            encoded += ZW_ONE if bit == '1' else ZW_ZERO
        encoded += ZW_SEP
    encoded += ZW_BOUNDARY
    return encoded


def zwc_to_text(encoded):
    """Decode zero-width characters back to text."""
    result = []
    content = encoded.replace(ZW_BOUNDARY, '')
    chars = content.split(ZW_SEP)
    for char_bits in chars:
        if not char_bits:
            continue
        bits = ''
        for zwc in char_bits:
            if zwc == ZW_ZERO:
                bits += '0'
            elif zwc == ZW_ONE:
                bits += '1'
        if bits and len(bits) == 16:
            result.append(chr(int(bits, 2)))
    return ''.join(result)


def extract_watermarks(content):
    """Extract any zero-width watermarks from content."""
    found = []
    parts = content.split(ZW_BOUNDARY)
    for i in range(1, len(parts), 2):
        if parts[i]:
            decoded = zwc_to_text(parts[i])
            if decoded:
                found.append(decoded)
    return found


def compute_seal(content_bytes):
    """Compute Bismillah-anchored integrity seal: SHA-256(Bismillah || content || Bismillah)."""
    h = hashlib.sha256()
    h.update(BISMILLAH.encode('utf-8'))
    h.update(content_bytes)
    h.update(BISMILLAH.encode('utf-8'))
    return h.hexdigest()


def make_comment(ext, text):
    """Create a comment string for the given file extension."""
    if ext in COMMENT_STYLES:
        prefix, suffix = COMMENT_STYLES[ext]
        if suffix:
            return "{} {} {}".format(prefix, text, suffix)
        return "{} {}".format(prefix, text)
    return text


def is_code_file(ext):
    """Return True if this extension is a code file that rejects zero-width chars."""
    return ext in COMMENT_STYLES


def seal_text_content(content, ext):
    """Apply Bismillah seal to text content (visible + invisible layers)."""
    lines = content.split('\n')

    # LAYER 0 -- Visible Bismillah at start and end
    bismillah_line = make_comment(ext, BISMILLAH) if ext in COMMENT_STYLES else BISMILLAH

    has_start = any(
        'bismillah' in line.lower().replace('-', '')
        for line in lines[:3] if line.strip()
    )
    if not has_start:
        lines.insert(0, bismillah_line)

    non_empty_tail = [l for l in lines[-3:] if l.strip()]
    has_end = any(
        'bismillah' in line.lower().replace('-', '')
        for line in non_empty_tail
    )
    if not has_end:
        if lines and lines[-1].strip():
            lines.append('')
        lines.append(bismillah_line)

    # LAYER 3 -- Steganographic watermark
    if is_code_file(ext):
        # Code files: zero-width chars break parsers, skip ZWC here
        # (Names go in as comments via embed_99_names_code)
        pass
    else:
        # Text/markdown: invisible zero-width encoding
        zwc_bismillah = text_to_zwc(BISMILLAH_ARABIC)
        for i, line in enumerate(lines):
            stripped = line.strip()
            if (stripped
                    and 'bismillah' not in stripped.lower().replace('-', '')
                    and len(stripped) > 10):
                words = line.split(' ', 1)
                if len(words) >= 2:
                    lines[i] = words[0] + zwc_bismillah + ' ' + words[1]
                break

    return '\n'.join(lines)


def embed_99_names_text(content):
    """Embed all 99 Names as zero-width watermark throughout text/markdown content."""
    lines = content.split('\n')
    name_idx = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or len(stripped) < 5:
            continue

        if name_idx < len(AL_ASMA_UL_HUSNA):
            _arabic, transliteration, _meaning = AL_ASMA_UL_HUSNA[name_idx]
            watermark = text_to_zwc(transliteration)
            if len(line) > 1:
                lines[i] = line[0] + watermark + line[1:]
                name_idx += 1

        if name_idx >= len(AL_ASMA_UL_HUSNA):
            name_idx = 0

    return '\n'.join(lines)


def embed_99_names_code(content, ext):
    """Embed the 99 Names as comments in code files (safe for all parsers)."""
    lines = content.split('\n')
    name_idx = 0
    result = []

    # Insert a Names comment block after the opening Bismillah
    found_opening = False
    for i, line in enumerate(lines):
        result.append(line)
        if not found_opening and 'bismillah' in line.lower().replace('-', ''):
            found_opening = True
            # Insert a comment block with all 99 Names right after opening
            result.append(make_comment(ext, ""))
            result.append(make_comment(ext, "Al-Asma ul-Husna -- The 99 Beautiful Names of Allah"))
            for _ar, trans, meaning in AL_ASMA_UL_HUSNA:
                result.append(make_comment(ext, "  {} -- {}".format(trans, meaning)))
            result.append(make_comment(ext, ""))

    return '\n'.join(result)


def seal_file(filepath, embed_names=False):
    """Apply the full Bismillah seal to a single file."""
    result = {"file": filepath, "layers_applied": []}
    p = Path(filepath)
    ext = p.suffix.lower()
    fname = p.name

    # NEVER watermark this script itself
    if fname == SELF_NAME:
        result["skipped"] = "self"
        return result

    is_text = ext in COMMENT_STYLES or ext in TEXT_EXTENSIONS

    if is_text:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            sealed = seal_text_content(content, ext)
            result["layers_applied"].append("L0_VISIBLE")

            if is_code_file(ext):
                if embed_names:
                    sealed = embed_99_names_code(sealed, ext)
                    result["layers_applied"].append("L3b_99_NAMES_COMMENTS")
            else:
                result["layers_applied"].append("L3a_STEGANOGRAPHIC")
                if embed_names:
                    sealed = embed_99_names_text(sealed)
                    result["layers_applied"].append("L3a_99_NAMES_ZWC")

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(sealed)

        except (UnicodeDecodeError, ValueError):
            result["skipped"] = "binary_content"

    # Layer 5 -- Hash seal
    with open(filepath, 'rb') as f:
        data = f.read()
    result["bismillah_seal"] = compute_seal(data)
    result["layers_applied"].append("L5_HASH_SEAL")

    return result


def seal_directory(directory, embed_names=False):
    """Apply the Bismillah seal to all text files in a directory."""
    results = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != '.git' and d != '__pycache__']
        for fname in sorted(files):
            fpath = os.path.join(root, fname)
            result = seal_file(fpath, embed_names=embed_names)
            if result.get("skipped") != "self":
                layers = result.get('layers_applied', [])
                print("  SEALED: {} [{}]".format(fpath, ', '.join(layers)))
            results.append(result)
    return results


def verify_directory(directory):
    """Verify the Bismillah seal on all files in a directory."""
    report = {
        "bismillah": BISMILLAH,
        "verified": 0,
        "unsealed": 0,
        "warnings": [],
        "files": []
    }

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != '.git' and d != '__pycache__']
        for fname in sorted(files):
            fpath = os.path.join(root, fname)
            relpath = os.path.relpath(fpath, directory)
            file_report = {"file": relpath, "seals": []}

            if fname.startswith('Bismillah_') and '_Bismillah.' in fname:
                file_report["seals"].append("L1_FILENAME")
            else:
                if fname != SELF_NAME and fname != 'pyproject.toml':
                    report["warnings"].append("UNSEALED FILENAME: {}".format(relpath))

            ext = Path(fname).suffix.lower()
            if ext in COMMENT_STYLES or ext in TEXT_EXTENSIONS:
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    lines = content.strip().split('\n')
                    if lines and 'bismillah' in lines[0].lower().replace('-', ''):
                        file_report["seals"].append("L0_VISIBLE_OPEN")
                    else:
                        report["warnings"].append("MISSING BISMILLAH OPEN: {}".format(relpath))
                    if lines and 'bismillah' in lines[-1].lower().replace('-', ''):
                        file_report["seals"].append("L0_VISIBLE_CLOSE")
                    else:
                        report["warnings"].append("MISSING BISMILLAH CLOSE: {}".format(relpath))

                    watermarks = extract_watermarks(content)
                    if watermarks:
                        file_report["seals"].append("L3_WATERMARKS({})".format(len(watermarks)))
                except (UnicodeDecodeError, ValueError):
                    pass

            if file_report["seals"]:
                report["verified"] += 1
            else:
                report["unsealed"] += 1

            report["files"].append(file_report)

    report["bismillah_closing"] = BISMILLAH
    return report


def generate_manifest(directory):
    """Generate a Bismillah integrity manifest for all files in a directory."""
    manifest = {
        "bismillah": BISMILLAH,
        "bismillah_hash": BISMILLAH_HASH,
        "seal_version": "1.0",
        "al_asma_count": len(AL_ASMA_UL_HUSNA),
        "files": {}
    }

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != '.git' and d != '__pycache__']
        for fname in sorted(files):
            fpath = os.path.join(root, fname)
            relpath = os.path.relpath(fpath, directory)
            try:
                with open(fpath, 'rb') as f:
                    data = f.read()
                entry = {
                    "size": len(data),
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "bismillah_seal": compute_seal(data),
                    "filename_sealed": fname.startswith('Bismillah_') and '_Bismillah.' in fname,
                }
                try:
                    text = data.decode('utf-8')
                    lines = text.strip().split('\n')
                    first_line = lines[0].strip() if lines else ''
                    last_line = lines[-1].strip() if lines else ''
                    entry["content_opens_bismillah"] = 'bismillah' in first_line.lower().replace('-', '')
                    entry["content_closes_bismillah"] = 'bismillah' in last_line.lower().replace('-', '')
                    wmarks = extract_watermarks(text)
                    entry["watermark_count"] = len(wmarks)
                except (UnicodeDecodeError, ValueError):
                    entry["binary"] = True
                manifest["files"][relpath] = entry
            except Exception as e:
                manifest["files"][relpath] = {"error": str(e)}

    manifest["total_files"] = len(manifest["files"])
    manifest["bismillah_closing"] = BISMILLAH
    return manifest


def main():
    parser = argparse.ArgumentParser(description="{} -- The Bismillah Seal".format(BISMILLAH))
    sub = parser.add_subparsers(dest='command')

    seal_p = sub.add_parser('seal', help='Apply Bismillah seal to files')
    seal_p.add_argument('path', help='File or directory to seal')
    seal_p.add_argument('--names', action='store_true', help='Embed the 99 Names throughout')

    verify_p = sub.add_parser('verify', help='Verify Bismillah seal integrity')
    verify_p.add_argument('path', help='File or directory to verify')

    names_p = sub.add_parser('names', help='Embed the 99 Names into a file')
    names_p.add_argument('path', help='File to embed Names into')

    manifest_p = sub.add_parser('manifest', help='Generate integrity manifest')
    manifest_p.add_argument('path', help='Directory to manifest')

    args = parser.parse_args()

    print("\n  {}".format(BISMILLAH))
    print()

    if args.command == 'seal':
        target = args.path
        if os.path.isdir(target):
            print("  Sealing directory: {}".format(target))
            results = seal_directory(target, embed_names=args.names)
            sealed = [r for r in results if r.get("skipped") != "self"]
            print("\n  {} files sealed.".format(len(sealed)))
        elif os.path.isfile(target):
            result = seal_file(target, embed_names=args.names)
            print("  SEALED: {}".format(target))
        else:
            print("  ERROR: {} not found".format(target))
            sys.exit(1)

    elif args.command == 'verify':
        target = args.path
        if os.path.isdir(target):
            report = verify_directory(target)
            print("  Verified: {} files".format(report['verified']))
            print("  Unsealed: {} files".format(report['unsealed']))
            if report['warnings']:
                print("\n  WARNINGS:")
                for w in report['warnings'][:20]:
                    print("    - {}".format(w))
        else:
            print("  ERROR: {} is not a directory".format(target))
            sys.exit(1)

    elif args.command == 'names':
        target = args.path
        if os.path.isfile(target):
            with open(target, 'r', encoding='utf-8') as f:
                content = f.read()
            sealed = embed_99_names(content)
            with open(target, 'w', encoding='utf-8') as f:
                f.write(sealed)
            print("  99 Names of Allah embedded into: {}".format(target))
        else:
            print("  ERROR: {} not found".format(target))
            sys.exit(1)

    elif args.command == 'manifest':
        target = args.path
        if os.path.isdir(target):
            manifest = generate_manifest(target)
            manifest_path = os.path.join(target, 'Bismillah_MANIFEST_Bismillah.json')
            with open(manifest_path, 'w', encoding='utf-8') as f:
                json.dump(manifest, f, indent=2, ensure_ascii=False)
            print("  Manifest written: {}".format(manifest_path))
            print("  {} files catalogued".format(manifest['total_files']))
        else:
            print("  ERROR: {} is not a directory".format(target))
            sys.exit(1)

    else:
        parser.print_help()
        sys.exit(1)

    print("\n  {}".format(BISMILLAH))
    print()


if __name__ == '__main__':
    main()

# Bismillah ir-Rahman ir-Rahim
