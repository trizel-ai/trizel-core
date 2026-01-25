# Gate Authorization Documents

This directory contains formal governance authorization documents for the TRIZEL framework.

## Gate 3A — Lab Execution Authorization

Gate 3A authorizes controlled execution of analytical workflows within Layer-3 (Laboratory/Analysis) to produce DERIVED artifacts from SNAPSHOT inputs under strict non-interpretive constraints.

**Status:** PENDING APPROVAL  
**Authorization ID:** GATE-3A-LAB-EXEC-001  
**Effective Date:** 2026-01-25

### Documents

1. **[GATE_3A_LAB_EXECUTION_AUTHORIZATION.md](GATE_3A_LAB_EXECUTION_AUTHORIZATION.md)**
   - Primary authorization document
   - Authority statement and scope
   - Input/output contracts
   - Audit requirements
   - Evidence chain model

2. **[GATE_3A_ALLOWED_FORBIDDEN_MATRIX.md](GATE_3A_ALLOWED_FORBIDDEN_MATRIX.md)**
   - Binary reference for permitted/prohibited activities
   - Layer-3 (Laboratory) constraints
   - Layer-2 (Presentation) constraints
   - Compliance quick reference

3. **[GATE_3A_ACCEPTANCE_SIGNOFF_FORM.md](GATE_3A_ACCEPTANCE_SIGNOFF_FORM.md)**
   - Formal acceptance form for human governance approval
   - Precondition verification checklist
   - Scope lock verification
   - Content verification
   - Sign-off block

4. **[GATE_3A_OUTPUT_SCHEMA.md](GATE_3A_OUTPUT_SCHEMA.md)**
   - Definition-only schema examples (NOT executable)
   - derived-manifest.json schema
   - derived-status.json schema (VALID/INVALID/INCONCLUSIVE/PENDING)
   - ro-crate-metadata.json minimal requirements

### Prerequisites

- **Gate 2I-B:** CLOSED (real-data flow established without analysis)
- **Layer-2 Baseline:** layer-2-baseline-v1 (immutable presentation baseline)

### Key Constraints

**Definition-Only:**
- This authorization is documentation-only
- No executable code, workflows, or scripts authorized
- No CI/CD or automation changes
- Implementation requires separate authorization

**Layer Separation:**
- Layer-3 (Lab): Execution, transformation, validation, packaging
- Layer-2 (Presentation): Declarative status only (requires separate Gate 4)

**Non-Interpretive:**
- No interpretation, conclusions, or scientific claims
- No predictions or narrative analysis
- Validation status only: VALID, INVALID, INCONCLUSIVE, PENDING

**Audit Requirements:**
- Complete provenance metadata (source → transformation → output)
- SHA-256 integrity checksums for all artifacts
- Immutable timestamps (ISO 8601 UTC)
- Reproducibility documentation

### External References

- TRIZEL Layer-0 Governance Framework
- RO-Crate Metadata Specification 1.1: https://www.researchobject.org/ro-crate/

---

**Repository:** trizel-ai/trizel-core  
**Document Type:** Governance Authorization Index  
**Last Updated:** 2026-01-25
