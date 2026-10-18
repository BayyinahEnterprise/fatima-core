# Bismillah ir-Rahman ir-Rahim
# 
# Al-Asma ul-Husna -- The 99 Beautiful Names of Allah
#   Allah -- The God
#   Ar-Rahman -- The Most Merciful
#   Ar-Rahim -- The Most Compassionate
#   Al-Malik -- The King
#   Al-Quddus -- The Most Holy
#   As-Salam -- The Source of Peace
#   Al-Mu'min -- The Guardian of Faith
#   Al-Muhaymin -- The Protector
#   Al-Aziz -- The Almighty
#   Al-Jabbar -- The Compeller
#   Al-Mutakabbir -- The Supreme
#   Al-Khaliq -- The Creator
#   Al-Bari -- The Evolver
#   Al-Musawwir -- The Fashioner
#   Al-Ghaffar -- The Forgiver
#   Al-Qahhar -- The Subduer
#   Al-Wahhab -- The Bestower
#   Ar-Razzaq -- The Provider
#   Al-Fattah -- The Opener
#   Al-Alim -- The All-Knowing
#   Al-Qabid -- The Restrainer
#   Al-Basit -- The Expander
#   Al-Khafid -- The Abaser
#   Ar-Rafi -- The Exalter
#   Al-Mu'izz -- The Bestower of Honor
#   Al-Mudhill -- The Humiliator
#   As-Sami -- The All-Hearing
#   Al-Basir -- The All-Seeing
#   Al-Hakam -- The Judge
#   Al-Adl -- The Just
#   Al-Latif -- The Subtle One
#   Al-Khabir -- The All-Aware
#   Al-Halim -- The Forbearing
#   Al-Azim -- The Magnificent
#   Al-Ghafur -- The All-Forgiving
#   Ash-Shakur -- The Appreciative
#   Al-Ali -- The Most High
#   Al-Kabir -- The Most Great
#   Al-Hafiz -- The Preserver
#   Al-Muqit -- The Sustainer
#   Al-Hasib -- The Reckoner
#   Al-Jalil -- The Majestic
#   Al-Karim -- The Generous
#   Ar-Raqib -- The Watchful
#   Al-Mujib -- The Responsive
#   Al-Wasi -- The All-Encompassing
#   Al-Hakim -- The Perfectly Wise
#   Al-Wadud -- The Loving One
#   Al-Majid -- The Most Glorious
#   Al-Ba'ith -- The Resurrector
#   Ash-Shahid -- The Witness
#   Al-Haqq -- The Truth
#   Al-Wakil -- The Trustee
#   Al-Qawiyy -- The Most Strong
#   Al-Matin -- The Firm One
#   Al-Waliyy -- The Protector
#   Al-Hamid -- The Praiseworthy
#   Al-Muhsi -- The Accounter
#   Al-Mubdi -- The Originator
#   Al-Mu'id -- The Restorer
#   Al-Muhyi -- The Giver of Life
#   Al-Mumit -- The Creator of Death
#   Al-Hayy -- The Ever Living
#   Al-Qayyum -- The Self-Subsisting
#   Al-Wajid -- The Finder
#   Al-Majid -- The Noble
#   Al-Wahid -- The Unique
#   Al-Ahad -- The One
#   As-Samad -- The Eternal
#   Al-Qadir -- The Able
#   Al-Muqtadir -- The Powerful
#   Al-Muqaddim -- The Expediter
#   Al-Mu'akhkhir -- The Delayer
#   Al-Awwal -- The First
#   Al-Akhir -- The Last
#   Az-Zahir -- The Manifest
#   Al-Batin -- The Hidden
#   Al-Wali -- The Governor
#   Al-Muta'ali -- The Most Exalted
#   Al-Barr -- The Source of Goodness
#   At-Tawwab -- The Acceptor of Repentance
#   Al-Muntaqim -- The Avenger
#   Al-Afuww -- The Pardoner
#   Ar-Ra'uf -- The Most Kind
#   Malik-ul-Mulk -- Owner of Sovereignty
#   Dhul-Jalali wal-Ikram -- Lord of Majesty and Generosity
#   Al-Muqsit -- The Equitable
#   Al-Jami -- The Gatherer
#   Al-Ghaniyy -- The Self-Sufficient
#   Al-Mughni -- The Enricher
#   Al-Mani -- The Preventer
#   Ad-Darr -- The Distresser
#   An-Nafi -- The Propitious
#   An-Nur -- The Light
#   Al-Hadi -- The Guide
#   Al-Badi -- The Originator
#   Al-Baqi -- The Everlasting
#   Al-Warith -- The Inheritor
#   Ar-Rashid -- The Guide to the Right Path
#   As-Sabur -- The Patient
# 
"""
Graft manifest -- declared mechanism replacements with evidence status.

A graft is not an edit. It is a declared replacement of one mechanism
with another, carrying its own evidence status. Without a manifest, a
graft silently becomes a rewrite -- the same class of fracture as F-03.

A graft whose reviewer is the author is not a graft. It is a
self-attestation and is UNKNOWN by construction.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence

from fatima.verification.verdict import Verdict
from fatima.graft.report import GraftReport


class GraftStatus(Enum):
    """Graft lifecycle.

    UNKNOWN is a terminal state, not a waiting room. A graft is promoted
    to VERIFIED only when an independent reviewer (not the author, not the
    author's lineage) has signed an attestation that the mechanism was
    replaced and the replacement was verified against the target substrate.
    """

    PROPOSED = "PROPOSED"       # declared, not yet applied
    APPLIED = "APPLIED"         # mechanism replaced on substrate
    UNKNOWN = "UNKNOWN"         # applied but not independently reviewed
    VERIFIED = "VERIFIED"       # applied and independently attested
    REVERTED = "REVERTED"       # rolled back; recorded permanently


@dataclass(frozen=True)
class Graft:
    """A single declared mechanism replacement.

    Attributes
    ----------
    graft_id : str
        Unique identifier for this graft.
    target_path : str
        The file in fatima-core where the mechanism lives.
    old_symbol : str
        The symbol (function/class/module attr) being replaced.
    new_module : str
        The v0.2 module supplying the replacement.
    rationale : str
        Why the fracture requires replacement (Canon finding description).
    canon_ref : str
        Canon finding ID (F-01 through F-08 or other section).
    status : GraftStatus
        Current lifecycle position.
    reviewer_attestation : bytes or None
        Ed25519 signature over (graft_id, status), if reviewed.
    reviewer_key_id : str or None
        Key identifier of the reviewer who signed the attestation.
    """

    graft_id: str
    target_path: str
    old_symbol: str
    new_module: str
    rationale: str
    canon_ref: str
    status: GraftStatus = GraftStatus.PROPOSED
    reviewer_attestation: Optional[bytes] = None
    reviewer_key_id: Optional[str] = None

    def canonical_bytes(self) -> bytes:
        """Deterministic serialisation for signature binding."""
        obj = {
            "graft_id": self.graft_id,
            "target_path": self.target_path,
            "old_symbol": self.old_symbol,
            "new_module": self.new_module,
            "rationale": self.rationale,
            "canon_ref": self.canon_ref,
        }
        return json.dumps(
            obj, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")


def compute_graft_verdict(
    graft: Graft,
    author_key_id: str,
    reviewer_public_keys: dict[str, object] | None = None,
) -> GraftReport:
    """Compute a graft's report.

    Parameters
    ----------
    graft : Graft
        The graft to evaluate.
    author_key_id : str
        The author's key identifier. If the reviewer's key equals the
        author's key, the graft cannot rise above UNKNOWN. This is the
        same non-self-attestation rule as L4, applied at the graft layer.
    reviewer_public_keys : dict or None
        Mapping of key_id -> Ed25519 public key objects. If None or empty,
        no reviewer verification is possible.

    Returns
    -------
    GraftReport
        The verdict for this graft.
    """
    if graft.status is GraftStatus.PROPOSED:
        return GraftReport.absent("graft", "not yet applied to substrate")

    if graft.status is GraftStatus.REVERTED:
        return GraftReport.invalid(
            "graft", "graft was reverted; substrate state is 0.1 mechanism"
        )

    if graft.reviewer_attestation is None or graft.reviewer_key_id is None:
        return GraftReport.absent("graft", "no independent reviewer attestation")

    if graft.reviewer_key_id == author_key_id:
        return GraftReport.absent(
            "graft", "reviewer and author share key identity"
        )

    if not reviewer_public_keys or graft.reviewer_key_id not in reviewer_public_keys:
        return GraftReport.absent(
            "graft", "reviewer key not in verifier trust store"
        )

    # Signature verification requires the cryptography library.
    # If unavailable, the graft cannot be cryptographically verified.
    pub = reviewer_public_keys[graft.reviewer_key_id]
    payload = (
        graft.canonical_bytes()
        + b"|"
        + graft.status.value.encode("utf-8")
    )

    try:
        from cryptography.exceptions import InvalidSignature
        pub.verify(graft.reviewer_attestation, payload)  # type: ignore[union-attr]
    except ImportError:
        return GraftReport.absent(
            "graft", "cryptography library not available for signature verification"
        )
    except Exception:
        return GraftReport.invalid("graft", "invalid reviewer signature")

    if graft.status is not GraftStatus.VERIFIED:
        return GraftReport.absent(
            "graft",
            f"reviewer signed; status still {graft.status.value}",
        )

    return GraftReport.ok(
        "graft", 1.0, f"reviewed by {graft.reviewer_key_id}"
    )


@dataclass(frozen=True)
class GraftManifest:
    """The complete declared graft set for a candidate release.

    Final release verdict = meet of all graft verdicts.
    A release with any UNKNOWN graft cannot be VERIFIED.
    A release with any VIOLATED graft is VIOLATED.
    """

    release_id: str
    grafts: tuple[Graft, ...]

    def compute(
        self,
        author_key_id: str,
        reviewer_public_keys: dict[str, object] | None = None,
    ) -> GraftReport:
        """Compute the manifest's aggregate verdict."""
        reports = [
            compute_graft_verdict(g, author_key_id, reviewer_public_keys)
            for g in self.grafts
        ]
        if not reports:
            return GraftReport.absent("manifest", "no grafts declared")

        verdict = Verdict.VERIFIED
        confidence = 1.0
        notes: list[str] = []
        for r in reports:
            verdict = verdict & r.verdict
            confidence = min(confidence, r.confidence)
            if r.verdict is not Verdict.VERIFIED:
                notes.append(
                    f"{r.layer}: {r.notes[0] if r.notes else ''}"
                )
        return GraftReport(
            layer="manifest",
            verdict=verdict,
            confidence=confidence,
            notes=tuple(notes),
            code=verdict.value,
        )
# Bismillah ir-Rahman ir-Rahim
