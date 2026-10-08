"""
Graft protocol -- disciplined mechanism replacement on the fatima-core substrate.

A graft is a declared replacement of one mechanism with another. It carries
its own evidence status and begins at UNKNOWN. It rises to VERIFIED only
when an independent reviewer -- whose key is not the author's -- has signed
an attestation bound to the exact graft bytes.

Submodules
----------
manifest    -- GraftStatus, Graft, GraftManifest, GraftReport
independence -- EvidenceParty, IndependenceRecord, check_independence
anchor      -- AnchorProof, AnchorProvider, NullAnchor, verify_anchor
composite   -- CompositeGraftReport, verify_composite_grafts
adversarial -- fixture pairs for paraphrase/negation plumbing tests
"""
