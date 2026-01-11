# ROLE.md

## Repository Identification

**Repository**: `trizel-ai/trizel-core`  
**Layer**: **0 — Governance & Charter**  
**Status**: Canonical · Active · Root Authority  
**Version**: 1.0.0

---

## Single-Sentence Role

This repository is the **canonical governance and charter authority** that defines epistemic boundaries, layer separation rules, and structural principles for the entire TRIZEL ecosystem, and contains no data, execution logic, or analytical content.

---

## Epistemic Layer Assignment

**Layer 0**: Governance & Charter

This is the foundational layer that sits above all operational layers. It provides:
- Constitutional framework
- Epistemic separation rules
- Repository classification standards
- Publication policies
- Interface contract definitions

Layer 0 does not participate in the execution pipeline. It governs the pipeline itself.

---

## Explicit Scope (Allowed)

This repository is authorized to contain:

- **Governance documents**: Rules, boundaries, principles, standards
- **Role registry**: Classification of all TRIZEL repositories
- **Publication policies**: What can be published and how
- **Interface specifications**: Contracts between layers
- **Allowlist definitions**: Approved sources for downstream consumption
- **Metadata**: Versioning, provenance, citations
- **Documentation**: Non-interpretive descriptions of system structure

---

## Explicit Anti-Scope (Forbidden)

This repository must never contain:

- Scientific data or observational records
- Executable algorithms or computational code
- Analysis outputs or statistical results
- Inference models or predictions
- Interpretive claims or theoretical conclusions
- Automated workflows or scripts
- Theory definitions or validation claims
- Content belonging to other layers (1-6)

---

## Relationship to Other Layers

### Layer 0 (This Repository) → Other Layers
- **Governs**: All other layers
- **Provides**: Rules, boundaries, contracts
- **Consumes**: Nothing (no dependencies on other layers)
- **Exports**: Governance documents, schemas, allowlists

### Other Layers → Layer 0
- **Must comply with**: Governance rules defined here
- **Cannot modify**: Governance policies (one-way authority)
- **Reference**: Publication policies, role definitions, schemas

---

## Repository Dependencies

### Upstream Dependencies
**None**. This repository is the root authority and depends on no other TRIZEL repositories.

### Downstream Dependents
All TRIZEL repositories are downstream dependents:
- Layer 1: Canonical algorithm definitions
- Layer 2-3: Data and observation repositories
- Layer 4-5: Analysis and execution repositories
- Layer 6: Visualization and website repositories

---

## Export Classification

### What This Repository Exports

All exports from this repository are **governance artifacts** only:

1. **COPILOT_INSTRUCTIONS.md** — Copilot operating rules
2. **ROLE.md** (this file) — Layer assignment
3. **OUTPUT_CONTRACT.md** — Export specifications
4. **PUBLICATION_POLICY.md** — Publication rules
5. **DEPRECATED_TERMS.md** — Forbidden terminology
6. **docs/GOVERNANCE.md** — Operational governance
7. **Schema specifications** — For other layers to follow

### Export Schema Version
**v1.0.0**

### Publishable Tag
All governance documents are publishable: `publishable: true`

---

## Non-Export Declaration

This repository does **not** export:
- Data files
- Code artifacts
- Analysis results
- Computational outputs
- Interpretive content

---

## Change Protocol

Changes to this repository must:

1. **Maintain layer boundaries**: Cannot add non-governance content
2. **Version explicitly**: All changes tracked with version bumps
3. **Document rationale**: Explain why governance changed
4. **Check downstream impact**: Identify all affected repositories
5. **Follow PR template**: Use `.github/pull_request_template.md`
6. **Pass CI checks**: Deprecated terms blocker, governance validation

---

## Website Integration

### Allowed on Website
- Governance methodology (non-interpretive)
- Structural principles
- Repository role registry
- Publication policy summaries
- Provenance metadata
- Version and citation information

### Forbidden on Website
This repository contains no forbidden content for website publication. All governance artifacts are public by design.

### Ingestion Method
Website must use **allowlist-only ingestion**:
- Explicitly approved sources
- Validated schema versions
- Required `publishable: true` tag
- Fail-closed behavior (reject unknown sources)

---

## Compliance Requirements

All work in this repository must:

- [ ] Respect Layer 0 boundaries (governance only)
- [ ] Contain no deprecated terminology
- [ ] Avoid cross-layer responsibility transfer
- [ ] Maintain explicit versioning
- [ ] Document all changes
- [ ] Pass CI validation checks
- [ ] Follow minimal change principle

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-11 | Initial ROLE.md creation with TRIZEL DIRECTIVE |

---

## Related Documents

- `COPILOT_INSTRUCTIONS.md` — Operating instructions for Copilot
- `OUTPUT_CONTRACT.md` — Export contract specifications
- `PUBLICATION_POLICY.md` — Website publication rules
- `README.md` — Public-facing repository description
- `docs/GOVERNANCE.md` — Operational governance details
