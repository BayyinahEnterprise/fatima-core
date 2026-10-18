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
GRAFT-F03-PURITY-001 regression tests.

These tests verify that the commit/compare separation in F-03 holds:
verification observes but never writes to the object being verified.
"""

from copy import deepcopy

from fatima.core.atom import Atom
from fatima.core.bond import Bond, BondType
from fatima.core.molecule import Molecule
from fatima.properties.meaning import check_meaning_integrity
from fatima.verification.verdict import Verdict


def specimen() -> Molecule:
    m = Molecule(molecule_id="graft-f03", title="F-03 specimen")
    a1 = Atom("a1", "A proposition", "proposition")
    a2 = Atom("a2", "Supporting evidence", "evidence")
    m.add_atom(a1)
    m.add_atom(a2)
    # SUPPORTS does not require automatic reciprocal in v0.1 bond rules.
    m.add_bond(Bond(
        source_id="a2",
        target_id="a1",
        bond_type=BondType.SUPPORTS,
        weight=0.9,
        rationale="a2 supplies evidence for a1",
    ))
    m.compute_all_semantic_hashes()
    return m


def test_valid_finalised_molecule_verifies_without_mutation():
    m = specimen()
    before = deepcopy(m.to_dict())
    r = check_meaning_integrity(m)
    after = m.to_dict()
    assert r.verdict is Verdict.VERIFIED
    assert before == after


def test_bond_id_tamper_is_detected_and_not_repaired():
    m = specimen()
    stored = m.atoms["a1"].semantic_hash
    m.atoms["a1"].bond_ids.append("forged-bond-id")
    before = deepcopy(m.to_dict())

    r = check_meaning_integrity(m)

    assert r.verdict is Verdict.VIOLATED
    assert m.atoms["a1"].semantic_hash == stored
    assert m.to_dict() == before
    assert any("semantic hash mismatch" in v for v in r.violations)


def test_direct_graph_tamper_detects_stale_graph_commitment_without_rewrite():
    m = specimen()
    stored_graph_hash = m.bond_graph_hash

    forged = Bond(
        source_id="a1",
        target_id="a2",
        bond_type=BondType.REFERENCES,
        weight=0.4,
        rationale="forged direct insertion",
    )
    # Direct dict insertion deliberately bypasses add_bond() invalidation.
    m.bonds[forged.bond_id] = forged
    before = deepcopy(m.to_dict())

    r = check_meaning_integrity(m)

    assert r.verdict is Verdict.VIOLATED
    assert m.bond_graph_hash == stored_graph_hash
    assert m.to_dict() == before
    assert any("Bond graph hash mismatch" in v for v in r.violations)


def test_missing_commitments_is_unknown_not_verified():
    m = Molecule(molecule_id="unfinalised", title="Unfinalised")
    m.add_atom(Atom("a1", "Uncommitted proposition", "proposition"))
    r = check_meaning_integrity(m)
    assert r.verdict is Verdict.UNKNOWN
# Bismillah ir-Rahman ir-Rahim
