# COPILOT_INSTRUCTIONS.md

## Repository Role

This repository is **Layer 0 — Governance & Charter**, and is non-authoritative outside that scope.

`trizel-core` defines the epistemic constitution, boundaries, and structural principles of the TRIZEL ecosystem. It is the root authority for governance decisions only.

---

## Allowed in This Repository

- Governance policy text and procedural definitions
- Epistemic boundary specifications (layer definitions, separation rules)
- Repository classification standards and role registries
- Publication policy definitions
- Structural principles and constitutional framework
- Metadata about governance versions, provenance, and citations
- Non-executable documentation about the TRIZEL system architecture
- Interface contracts that other repositories must follow
- Allowlist specifications for downstream consumption

---

## Forbidden in This Repository

- Scientific data, datasets, or observational records
- Executable code, algorithms, or computational logic
- Analysis results, statistical outputs, or derived metrics
- Models, predictions, or inference artifacts
- Interpretive claims or theoretical conclusions
- Automated workflows that perform scientific operations
- Direct theory definitions or "tested theory" listings
- Any content that belongs in execution, analysis, or visualization layers
- Deprecated terminology (see DEPRECATED_TERMS.md)
- Cross-layer responsibility transfer
- Dynamic ingestion or "discovery" mechanisms

---

## Interfaces

### Input Contracts
This repository does not consume outputs from other repositories.

### Output Contracts
- **Governance documents**: VERSION, ROLE.md, PUBLICATION_POLICY.md
- **Schema definitions**: Output contract specifications for other layers
- **Allowlists**: Approved source registries for website consumption
- All outputs are versioned, immutable text documents

### Schema References
- Governance schema version: `v1.0.0`
- All documents follow markdown format with explicit versioning headers
- Changes require explicit version bumps and historical traceability

---

## Publication Policy

### Publishable Artifacts
- Governance policy documents (methodology, boundaries, roles)
- Provenance metadata (version, timestamp, citation information)
- Structural framework descriptions (non-interpretive)
- Repository role registry
- Publication allowlist specifications

### Non-Publishable Artifacts
This repository contains no non-publishable artifacts. All governance content is public by design.

### Publication Tag Requirement
Documents intended for website consumption must include:
```yaml
publishable: true
layer: 0
type: governance
schema_version: v1.0.0
```

---

## Stop Conditions

Copilot MUST stop immediately and request clarification if any of the following occur:

1. **Deprecated term detected**: Any legacy terminology appears in proposed changes
2. **Cross-layer violation**: Proposed change introduces execution, analysis, or data content
3. **Layer collapse**: Attempt to merge governance with non-governance responsibilities
4. **Unauthorized export**: Proposal to create outputs not defined in OUTPUT_CONTRACT.md
5. **Schema change without consumer update**: Output format change without linked PRs for all consumers
6. **Interpretation creep**: Addition of theoretical, analytical, or interpretive content
7. **Unauthorized ingestion**: Proposal to consume artifacts from other repositories
8. **Dynamic discovery**: Implementation of automatic repository detection or crawling
9. **Governance leak**: Governance-like content proposed for non-governance repositories

---

## Pre-Flight Checklist (Required Before Any Change)

Before proposing any modification, Copilot must:

1. **Restate repository role**: Confirm this is Layer 0 — Governance only
2. **Verify allowed/forbidden boundaries**: Check proposed change against explicit lists above
3. **Deprecated terms check**: Scan all changes for forbidden terminology
4. **Cross-layer check**: Confirm no execution/analysis/data content introduced
5. **Minimal diff principle**: Propose only surgical, necessary changes
6. **Output contract compliance**: If schemas change, identify all downstream consumers
7. **Publication rule check**: Verify any website-related changes follow allowlist-only approach

---

## Minimal Change Principle

All changes must be:
- **Surgical**: Modify only what is necessary
- **Reversible**: Include explicit rollback plan
- **Testable**: Specify validation approach
- **Traceable**: Document rationale and version impact
- **Bounded**: Remain within Layer 0 scope

---

## Interaction Protocol

When receiving a task, Copilot must respond with:

```
TRIZEL DIRECTIVE acknowledged.

Repository: trizel-core
Layer: 0 — Governance & Charter
Branch: [CURRENT_BRANCH]

Task: [RESTATE_TASK]

ALLOWED: Governance policy, boundaries, role definitions, publication rules
FORBIDDEN: Data, execution, analysis, interpretation, deprecated terms

Deprecated terms check: [PASS/FAIL]
Cross-layer transfer check: [PASS/FAIL]
Publication rule check: [PASS/FAIL]

Minimal diff plan:
- Files to change: [LIST]
- Exact edits: [DESCRIPTION]
- Rationale: [EXPLANATION]
- Tests/checks: [VALIDATION_APPROACH]
- Rollback: [UNDO_PLAN]

Downstream consumers affected: [LIST or NONE]
Required linked PRs: [LIST or NONE]

Proceed? [YES/NO + reasoning]
```

---

## Version

**Document Version**: 1.0.0  
**Effective Date**: 2026-01-11  
**Governance Schema**: v1.0.0  
**Status**: Canonical · Active · Enforced

---

## Related Documents

- `ROLE.md` — Layer assignment and scope
- `OUTPUT_CONTRACT.md` — Export specifications
- `PUBLICATION_POLICY.md` — Website ingestion rules
- `DEPRECATED_TERMS.md` — Forbidden terminology
- `.github/pull_request_template.md` — PR compliance checklist
