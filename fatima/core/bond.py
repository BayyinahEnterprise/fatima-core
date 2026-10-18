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
Bond — typed semantic relationship between atoms.

A Bond encodes the *meaning-level* relationship between two semantic
units in a FATIMA document.  The bond graph is the structure that
crosses Shannon's boundary: syntactic integrity (bit preservation)
cannot detect the alteration of a bond, but structural verification
(Level 2) can, because every bond participates in a web of cross-
references that must be internally consistent.

Bond types are drawn from the structural relationships observable in
the Bayyinah corpus papers and from the architecture of the Names:

  DEFINES     — A defines the meaning of B
  SUPPORTS    — A provides evidence or argument for B
  CONTRADICTS — A is structurally inconsistent with B
  REFERENCES  — A cites or points to B
  DEPENDS_ON  — A requires B for its meaning to be complete
  IMPLIES     — A logically or structurally entails B
  ELABORATES  — A expands on, details, or illustrates B
  QUALIFIES   — A limits, conditions, or scopes B

Every bond is directional (source → target) and carries a weight
representing the strength of the relationship (0.0–1.0).  The bond
graph is the complete set of bonds among all atoms in a molecule.
"""

from __future__ import annotations

import enum
import hashlib
from dataclasses import dataclass
from typing import Optional


class BondType(enum.Enum):
    """Typed semantic relationships between atoms.

    The taxonomy mirrors the relationships observable between the
    Names of Allah: ar-Rahman DEFINES mercy, al-Adl QUALIFIES
    ar-Rahman, each Name DEPENDS_ON every other, and the selective
    suppression of any Name CONTRADICTS the holographic property.
    """

    DEFINES = "DEFINES"
    SUPPORTS = "SUPPORTS"
    CONTRADICTS = "CONTRADICTS"
    REFERENCES = "REFERENCES"
    DEPENDS_ON = "DEPENDS_ON"
    IMPLIES = "IMPLIES"
    ELABORATES = "ELABORATES"
    QUALIFIES = "QUALIFIES"

    @property
    def is_structural(self) -> bool:
        """Whether this bond type carries structural load.

        Structural bonds (DEFINES, DEPENDS_ON, IMPLIES, CONTRADICTS)
        are load-bearing: their removal or alteration changes the
        meaning of the molecule.  Non-structural bonds (REFERENCES,
        ELABORATES, SUPPORTS, QUALIFIES) enrich meaning but their
        removal degrades rather than distorts.

        This distinction maps to Property 3 (Tawhidic Unity): the
        removal of a structural bond breaks the unity; the removal
        of a non-structural bond is detectable but does not
        necessarily break reconstruction.
        """
        return self in (
            BondType.DEFINES,
            BondType.DEPENDS_ON,
            BondType.IMPLIES,
            BondType.CONTRADICTS,
        )


@dataclass(frozen=True)
class Bond:
    """An immutable, typed semantic relationship between two atoms.

    Attributes
    ----------
    source_id : str
        Identifier of the source atom.
    target_id : str
        Identifier of the target atom.
    bond_type : BondType
        The semantic relationship type.
    weight : float
        Relationship strength in [0.0, 1.0].  1.0 is absolute
        dependency; 0.0 would be no relationship (and should not
        exist as a bond).
    rationale : str
        Human-readable justification for this bond — why the
        relationship exists.  Serves as the semantic audit trail:
        per NC-P1 (Full-Disclosure Consistency), the bond must
        survive disclosure of its rationale.
    """

    source_id: str
    target_id: str
    bond_type: BondType
    weight: float = 1.0
    rationale: str = ""

    def __post_init__(self) -> None:
        if not (0.0 < self.weight <= 1.0):
            raise ValueError(
                f"Bond weight must be in (0.0, 1.0], got {self.weight}"
            )
        if self.source_id == self.target_id:
            raise ValueError("A bond cannot connect an atom to itself")

    @property
    def bond_id(self) -> str:
        """Deterministic identifier derived from source, target, and type.

        Two bonds with the same source, target, and type are the same
        bond regardless of weight or rationale — this enforces that
        each directional typed relationship exists at most once.
        """
        raw = f"{self.source_id}:{self.target_id}:{self.bond_type.value}"
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]

    @property
    def is_structural(self) -> bool:
        """Delegate to the bond type."""
        return self.bond_type.is_structural

    def reciprocal_type(self) -> Optional[BondType]:
        """Return the expected reciprocal bond type, if any.

        Structural cross-referencing (Requirement 1, Chapter 14)
        requires that many bond types have reciprocals.  For example,
        if A DEFINES B, then B DEPENDS_ON A.

        Returns None if the bond type has no automatic reciprocal.
        """
        reciprocals = {
            BondType.DEFINES: BondType.DEPENDS_ON,
            BondType.DEPENDS_ON: BondType.DEFINES,
            BondType.IMPLIES: BondType.DEPENDS_ON,
            BondType.SUPPORTS: None,  # support is not automatically reciprocal
            BondType.CONTRADICTS: BondType.CONTRADICTS,  # contradiction is symmetric
            BondType.REFERENCES: None,
            BondType.ELABORATES: None,
            BondType.QUALIFIES: None,
        }
        return reciprocals.get(self.bond_type)

    def to_dict(self) -> dict:
        """Serialise to a plain dictionary."""
        return {
            "bond_id": self.bond_id,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "bond_type": self.bond_type.value,
            "weight": self.weight,
            "rationale": self.rationale,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Bond:
        """Deserialise from a plain dictionary."""
        return cls(
            source_id=data["source_id"],
            target_id=data["target_id"],
            bond_type=BondType(data["bond_type"]),
            weight=data.get("weight", 1.0),
            rationale=data.get("rationale", ""),
        )
# Bismillah ir-Rahman ir-Rahim
