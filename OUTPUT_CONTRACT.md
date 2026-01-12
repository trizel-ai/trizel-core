# OUTPUT_CONTRACT.md

## Repository Export Contract

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Contract Version**: 1.0.0  
**Last Updated**: 2026-01-11

---

## Export Classification

This repository exports **governance artifacts only**.

All exports are:
- Plain text (Markdown format)
- Versioned explicitly
- Immutable (changes create new versions)
- Publicly accessible
- Non-executable

---

## Exported Artifacts

### 1. Governance Documents

**Purpose**: Define epistemic rules, boundaries, and structural principles

**Artifacts**:
- `COPILOT_INSTRUCTIONS.md` — Copilot operating instructions
- `ROLE.md` — Layer assignment and repository scope
- `OUTPUT_CONTRACT.md` — This file (export contract)
- `PUBLICATION_POLICY.md` — Website publication rules
- `DEPRECATED_TERMS.md` — Forbidden terminology registry
- `docs/GOVERNANCE.md` — Operational governance specifications

**Schema**:
```yaml
type: governance_document
format: markdown
schema_version: v1.0.0
publishable: true
layer: 0
immutable: true
versioned: true
```

**Provenance Fields** (embedded in each document):
```yaml
document_version: [semantic version]
effective_date: [ISO 8601 timestamp]
repository: trizel-ai/trizel-core
layer: 0
status: [Canonical | Active | Enforced | Deprecated]
```

---

### 2. Repository Role Registry

**Purpose**: Classification of all TRIZEL repositories by layer

**Artifacts**:
- Embedded in `README.md` (Section 5: Repository Taxonomy)
- Maintained as normative reference in governance documents

**Schema**:
```yaml
type: role_registry
format: structured_text
repositories:
  - name: string
    layer: integer (0-6)
    role: string
    canonical: boolean
    status: string
```

**Update Protocol**:
- New repositories added via governance PR
- Changes require version bump
- All downstream consumers notified

---

### 3. Schema Specifications

**Purpose**: Define output formats that other layers must produce

**Artifacts**:
- Schema definitions for execution outputs
- Schema definitions for analysis summaries
- Schema definitions for evaluation results
- Schema definitions for website ingestion

**Schema** (meta-schema for other layers):
```yaml
type: schema_definition
target_layer: [1-6]
required_fields: [list]
optional_fields: [list]
validation_rules: [list]
version: [semantic version]
```

**Contract Guarantee**:
- Schema changes trigger major version bump
- All consumers receive notification before deployment
- Breaking changes require linked consumer PRs

---

### 4. Allowlist Definitions

**Purpose**: Approved sources for website ingestion

**Artifacts**:
- Allowlist specifications (structure defined, implementation in website repo)
- Publication criteria
- Source validation rules

**Schema**:
```yaml
type: allowlist_specification
approved_sources:
  - repository: string
    layer: integer
    artifact_type: string
    schema_version: string
    publishable_tag_required: true
validation_rules:
  - rule: string
    enforcement: [fail | warn | log]
```

**Fail-Closed Principle**:
- Unknown sources rejected by default
- Missing schema version = rejection
- Missing publishable tag = rejection

---

## Non-Exports

This repository does **not** export:

- Executable code or scripts
- Data files or datasets
- Analysis results or metrics
- Computational outputs
- Binary artifacts
- Automated workflows
- API endpoints
- Dynamic content

---

## Consumer Contracts

### Who Consumes This Repository's Exports

1. **Layer 1 Repositories** (Canonical algorithm definitions)
   - Consume: Role boundaries, schema specifications
   - Use for: Self-governance compliance

2. **Layer 2-5 Repositories** (Execution, analysis, data)
   - Consume: COPILOT_INSTRUCTIONS.md, output schemas
   - Use for: Ensuring layer separation, output format compliance

3. **Layer 6 Repositories** (Website, visualization)
   - Consume: PUBLICATION_POLICY.md, allowlist specifications, governance documents
   - Use for: Ingestion rules, content validation, methodology display

4. **All TRIZEL Repositories**
   - Consume: DEPRECATED_TERMS.md, ROLE.md
   - Use for: CI validation, PR template compliance

---

## Consumer Requirements

All consumers of this repository's exports must:

1. **Reference by version**: Pin to specific governance version
2. **Validate schema compatibility**: Check schema_version matches
3. **Fail on mismatch**: Do not silently degrade or ignore
4. **Update atomically**: Governance change = consumer update (linked PRs)
5. **Log provenance**: Record which governance version was used

---

## Change Notification Protocol

When this repository's exports change:

### Minor Changes (patches, clarifications)
- Update version (e.g., 1.0.0 → 1.0.1)
- Notify consumers via release notes
- No breaking changes to schemas or contracts

### Major Changes (new rules, schema changes)
- Update version (e.g., 1.0.0 → 2.0.0)
- Create linked PRs in all affected consumer repositories
- Do not merge governance change until all consumers updated
- Document migration path

### Breaking Changes
- Require explicit approval from repository owner
- Must include deprecation notice in previous version
- Provide at least one version overlap period
- Update all downstream consumers before enforcement

---

## Validation Rules

### Pre-Export Validation

Before any artifact is exported (published), it must:

1. **Pass deprecated terms check**: No forbidden terminology
2. **Pass layer boundary check**: No non-governance content
3. **Include version metadata**: Document version, date, status
4. **Include provenance**: Repository, layer, schema version
5. **Pass schema validation**: Conform to defined structure
6. **Include publishable tag**: `publishable: true` (if for website)

### Post-Export Validation

After export, consumers must:

1. **Validate schema version**: Matches expected version
2. **Validate provenance**: From approved source
3. **Validate integrity**: Content matches expectations
4. **Log usage**: Record consumption for audit trail

---

## Schema Version Policy

This repository follows **semantic versioning** for all exports:

- **Major** (X.0.0): Breaking changes, new layers, schema redesign
- **Minor** (0.X.0): New features, new documents, non-breaking additions
- **Patch** (0.0.X): Clarifications, typo fixes, metadata updates

**Current Version**: 1.0.0

---

## Interface Stability Guarantee

This repository guarantees:

- **Versioned immutability**: Published versions never change retroactively
- **Deprecation notice**: At least one minor version before removal
- **Consumer notification**: Advance notice for all breaking changes
- **Rollback support**: Previous versions remain available
- **Audit trail**: All changes logged and traceable

---

## Publication Readiness

### Artifacts Ready for Website Publication

All governance documents in this repository are publication-ready:

```yaml
publishable: true
layer: 0
type: governance
schema_version: v1.0.0
content_type:
  - methodology
  - provenance
  - structural_framework
forbidden_content:
  - interpretation
  - analysis_results
  - raw_data
  - executable_code
```

### Ingestion Method for Website

Website must use **strict allowlist ingestion**:

```yaml
source: trizel-ai/trizel-core  # Update if repository is moved or renamed
approved_artifacts:
  - COPILOT_INSTRUCTIONS.md
  - ROLE.md
  - OUTPUT_CONTRACT.md
  - PUBLICATION_POLICY.md
  - README.md
  - docs/GOVERNANCE.md
schema_version: v1.0.0
validation: fail_closed
```

---

## Error Handling

### Export Failures

If export validation fails:

1. **Block publication**: Do not merge PR
2. **Report specific failure**: Which check failed and why
3. **Require fix**: Cannot bypass validation
4. **Log incident**: Audit trail of attempted violations

### Consumer Failures

If consumer cannot process export:

1. **Fail explicitly**: Do not silently ignore or degrade
2. **Report version mismatch**: Log schema version conflict
3. **Halt ingestion**: Do not proceed with invalid data
4. **Notify governance**: Report compatibility issue

---

## Compliance Checklist

Every export from this repository must pass:

- [ ] Deprecated terms check: PASS
- [ ] Layer boundary check: PASS (governance only)
- [ ] Version metadata present: YES
- [ ] Provenance fields complete: YES
- [ ] Schema validation: PASS
- [ ] Publishable tag (if for website): YES
- [ ] Consumer impact assessment: COMPLETE
- [ ] Breaking change notification: SENT (if applicable)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-11 | Initial OUTPUT_CONTRACT.md with TRIZEL DIRECTIVE |

---

## Related Documents

- `COPILOT_INSTRUCTIONS.md` — Copilot operating rules
- `ROLE.md` — Layer assignment and scope
- `PUBLICATION_POLICY.md` — Website publication details
- `README.md` — Public repository description
