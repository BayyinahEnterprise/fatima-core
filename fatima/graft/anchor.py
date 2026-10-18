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
External anchor interface -- pluggable external time reference.

The prototype's anchor_ref as a free string was a placeholder, not an
interface. A real anchor requires a service that produces a verifiable
timestamp the author cannot forge.

Absent a configured anchor provider, the anchor level is UNKNOWN --
never assumed satisfied by a string.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from fatima.graft.report import GraftReport


@dataclass(frozen=True)
class AnchorProof:
    """A verifiable external timestamp proof.

    Attributes
    ----------
    provider : str
        Provider type ("rfc3161", "opentimestamps", "test-double").
    payload : bytes
        Provider-specific proof bytes.
    anchored_at : str
        ISO-8601 timestamp as claimed by provider.
    commitment_hash : str
        The hash the anchor covers.
    """

    provider: str
    payload: bytes
    anchored_at: str
    commitment_hash: str


class AnchorProvider(Protocol):
    """Interface every anchor provider must satisfy.

    A provider that cannot verify its own proofs is not a provider;
    it is a second author. The independence check at the anchor layer
    requires that the provider's verification code path is not the
    author's.
    """

    name: str

    def verify(self, proof: AnchorProof, expected_hash: str) -> bool:
        """Verify an anchor proof against an expected commitment hash."""
        ...


class NullAnchor:
    """Default provider. Returns False. Yields UNKNOWN.

    This is not a failure mode; it is the honest default. A deployment
    that has not configured an anchor does not get to claim one.
    """

    name = "null"

    def verify(self, proof: AnchorProof, expected_hash: str) -> bool:
        return False


class TestDoubleAnchor:
    """Test-only provider. Verifies if commitment_hash matches expected.

    For regression tests only. This provider does not contact an external
    service and therefore does not provide real external anchoring.
    """

    name = "test-double"

    def verify(self, proof: AnchorProof, expected_hash: str) -> bool:
        return proof.commitment_hash == expected_hash


def verify_anchor(
    proof: AnchorProof | None,
    provider: AnchorProvider,
    expected_commitment_hash: str,
) -> GraftReport:
    """Verify an external anchor proof.

    Returns
    -------
    GraftReport
        VERIFIED only if a real provider confirms the proof covers
        the expected commitment. UNKNOWN if no proof or null provider.
        VIOLATED if proof covers a different commitment or provider rejects.
    """
    if proof is None:
        return GraftReport.absent(
            "anchor", "no external anchor proof supplied"
        )
    if provider.name == "null":
        return GraftReport.absent(
            "anchor",
            "no anchor provider configured; default is null",
        )
    if proof.commitment_hash != expected_commitment_hash:
        return GraftReport.invalid(
            "anchor", "anchor covers a different commitment"
        )
    if not provider.verify(proof, expected_commitment_hash):
        return GraftReport.invalid(
            "anchor", "provider rejected its own proof"
        )
    return GraftReport.ok(
        "anchor", 1.0, f"verified by {provider.name}"
    )
# Bismillah ir-Rahman ir-Rahim
