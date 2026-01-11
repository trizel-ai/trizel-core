# PUBLICATION_POLICY.md

## Website Publication Policy

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Policy Version**: 1.0.0  
**Last Updated**: 2026-01-11

---

## Purpose

This document defines what content from `trizel-core` can be published to the TRIZEL website, how it must be ingested, and what is explicitly forbidden.

---

## Core Principle

The TRIZEL website is **not** an ingestion vacuum. It is a **governed, allowlist-only, fail-closed publication interface** that displays:

1. **Methodology** (non-interpretive)
2. **Provenance** (version, source, timestamp)
3. **Status** (repository state, version metadata)
4. **Structural framework** (epistemic pipeline, layer definitions)
5. **Citation information** (DOI pointers, if applicable)

The website **never** publishes:
- Interpretation
- Analysis results
- Raw data
- Executable code
- Theoretical claims

---

## Publishable Content from `trizel-core`

### Allowed for Website Publication

The following artifacts from this repository are **approved for website publication**:

1. **README.md**
   - Purpose: Overview of TRIZEL governance
   - Content type: Methodology, structural framework
   - Sections: All except internal implementation details

2. **ROLE.md**
   - Purpose: Layer 0 definition and scope
   - Content type: Structural framework, role definition
   - Sections: All

3. **docs/GOVERNANCE.md**
   - Purpose: Operational governance rules
   - Content type: Methodology, enforcement rules
   - Sections: All

4. **Repository Role Registry**
   - Purpose: Classification of all TRIZEL repositories
   - Content type: Structural framework
   - Location: Embedded in README.md (Section 5)

5. **Epistemic Pipeline Diagram**
   - Purpose: Visual representation of layer separation
   - Content type: Structural framework (non-executable SVG)
   - Location: README.md (TRIZEL System Map)

6. **Version and Provenance Metadata**
   - Purpose: Traceability and citation
   - Content type: Provenance
   - Fields: version, date, repository, layer, status

### Metadata Requirements

All published content must include:

```yaml
publishable: true
layer: 0
type: governance
schema_version: v1.0.0
repository: trizel-ai/trizel-core
document_version: [version]
effective_date: [ISO 8601 timestamp]
status: [Canonical | Active | Enforced]
```

---

## Non-Publishable Content

The following are **explicitly forbidden** from website publication:

1. **Internal implementation files**
   - `.github/workflows/*` (CI configuration)
   - Internal scripts or automation

2. **Development artifacts**
   - Draft documents
   - Temporary files
   - Build artifacts

3. **Content not in the approved list above**
   - Any file not explicitly listed in "Allowed for Website Publication"

**Enforcement**: Website build must **fail** if non-approved sources are detected.

---

## Ingestion Rules for Website

### Allowlist-Only Ingestion

The website must implement **strict allowlist validation**:

```yaml
# website/config/allowlist.yml (example structure)

approved_sources:
  - repository: trizel-ai/trizel-core
    layer: 0
    schema_version: v1.0.0
    artifacts:
      - path: README.md
        type: governance
        publishable: true
      - path: ROLE.md
        type: governance
        publishable: true
      - path: docs/GOVERNANCE.md
        type: governance
        publishable: true
    validation_rules:
      - publishable_tag_required: true
      - schema_version_match: true
      - provenance_fields_complete: true
```

### Validation Protocol

Before ingesting any content, the website must:

1. **Check repository source**: Is it in approved_sources list?
2. **Check artifact path**: Is the specific file approved?
3. **Check schema version**: Does it match approved version?
4. **Check publishable tag**: Is `publishable: true` present?
5. **Validate provenance**: Are all required fields present?

**If any check fails**: Reject content and fail build (fail-closed behavior).

---

## Fail-Closed Enforcement

The website ingestion system must operate in **fail-closed mode**:

### What Fail-Closed Means

- **Unknown source**: REJECT (do not guess or silently skip)
- **Missing schema version**: REJECT
- **Missing publishable tag**: REJECT
- **Mismatched version**: REJECT
- **Incomplete provenance**: REJECT

### Error Behavior

When validation fails:

1. **Stop build**: Do not proceed with deployment
2. **Log specific failure**: Record which check failed
3. **Report reason**: Output clear error message
4. **Require manual fix**: Cannot bypass validation

**Never**:
- Silently skip invalid content
- Degrade gracefully
- Guess or infer intent
- Proceed with partial data

---

## Content Type Restrictions

### Allowed Content Types for Website

From `trizel-core`, only the following content types are permitted:

1. **Methodology** (non-interpretive)
   - How TRIZEL works
   - Layer separation principles
   - Governance rules

2. **Structural Framework**
   - Epistemic pipeline
   - Repository taxonomy
   - Layer definitions

3. **Provenance**
   - Version information
   - Timestamps
   - Source identifiers

4. **Status**
   - Repository state
   - Version metadata
   - Canonical/non-canonical designation

5. **Citations**
   - DOI pointers (when available)
   - Repository references
   - License information

### Forbidden Content Types

The website must **never** publish from `trizel-core`:

- Interpretation or theoretical claims
- Analysis results or statistical outputs
- Raw data or datasets
- Executable code or algorithms
- Predictive models or inferences
- Personal opinions or commentary
- Content from deprecated terminology

---

## Website Build Integration

### Pre-Build Validation

Before building the website, run:

1. **Allowlist check**: Verify all sources are approved
2. **Schema validation**: Confirm version compatibility
3. **Publishable tag check**: Ensure all content tagged correctly
4. **Deprecated terms check**: Scan for forbidden terminology
5. **Provenance validation**: Verify all metadata present

### Build Failure Triggers

Website build must **fail** if:

- Content from non-approved source detected
- Missing or mismatched schema version
- Missing `publishable: true` tag
- Incomplete provenance metadata
- Deprecated terminology detected
- Non-approved content type found

### Post-Build Verification

After successful build:

1. **Log ingestion**: Record what was published and from where
2. **Version audit**: Confirm published governance version
3. **Content inventory**: List all published artifacts
4. **Validate structure**: Ensure only allowed sections rendered

---

## Schema Version Coupling

### Current Schema Version

**Governance Schema**: v1.0.0

### Website Compatibility

The website must declare compatible schema versions:

```yaml
# website/config/compatibility.yml (example)

compatible_governance_versions:
  - v1.0.0

deprecated_versions:
  - # none yet

breaking_changes:
  - # none yet
```

### Version Mismatch Handling

If governance schema version changes:

1. **Minor version change** (e.g., 1.0.0 → 1.1.0):
   - Website may support both old and new
   - Update website within one release cycle
   - Log deprecation warning for old version

2. **Major version change** (e.g., 1.0.0 → 2.0.0):
   - Website must be updated **before** governance change merges
   - Linked PRs required (governance + website)
   - Breaking changes documented
   - Migration path provided

---

## Consumer Update Requirements

When `trizel-core` governance changes:

### For Website Repository

The website must:

1. **Update allowlist**: If new artifacts approved
2. **Update schema version**: If governance version bumps
3. **Update validation rules**: If new checks required
4. **Update content rendering**: If structure changes
5. **Test ingestion**: Verify compatibility before deployment

### Linked PR Protocol

For breaking changes:

1. **Create governance PR**: In `trizel-core`
2. **Create website PR**: In website repository
3. **Link PRs**: Reference each other in descriptions
4. **Merge atomically**: Website first, then governance
5. **Verify deployment**: Confirm website handles new version

---

## Publication Content Inventory

### What the Website Displays from `trizel-core`

The website publishes **only**:

- **Governance Overview**: From README.md
- **Epistemic Pipeline**: Visual diagram and description
- **Repository Taxonomy**: Role registry
- **Layer Definitions**: From ROLE.md
- **Publication Policies**: From this document
- **Version Metadata**: Provenance and status
- **License Information**: From LICENSE

### What the Website Never Displays

The website **never** displays:

- Internal workflow files
- Development documentation
- Draft or work-in-progress documents
- Anything not in the approved artifacts list
- Content from other repositories (unless explicitly allowlisted)

---

## Audit and Compliance

### Audit Trail Requirements

The website must maintain:

1. **Ingestion log**: What was published, when, from which version
2. **Validation log**: Which checks passed/failed
3. **Version history**: Governance versions used over time
4. **Rejection log**: Any content rejected and why

### Compliance Checklist (per deployment)

- [ ] All sources in approved allowlist: YES
- [ ] All schema versions match: YES
- [ ] All publishable tags present: YES
- [ ] All provenance fields complete: YES
- [ ] No deprecated terms detected: YES
- [ ] No forbidden content types: YES
- [ ] Build validation passed: YES
- [ ] Audit trail logged: YES

---

## Rollback and Error Recovery

### If Invalid Content Published

If non-compliant content reaches production:

1. **Immediate rollback**: Revert to previous version
2. **Incident report**: Document what was published and how
3. **Fix validation**: Update checks to prevent recurrence
4. **Re-deploy**: With validated content only

### If Ingestion Fails

If website cannot ingest governance content:

1. **Preserve previous version**: Keep current site live
2. **Diagnose mismatch**: Identify version incompatibility
3. **Update website**: Fix compatibility issue
4. **Re-attempt ingestion**: After fix validated
5. **Log recovery**: Document resolution

---

## Governance of This Policy

### Policy Updates

Changes to this publication policy require:

1. **PR in `trizel-core`**: Update PUBLICATION_POLICY.md
2. **Version bump**: Increment policy version
3. **Website notification**: Alert website maintainers
4. **Linked website PR**: Update ingestion rules
5. **Coordinated merge**: Policy + website together

### Breaking Policy Changes

If publication rules change fundamentally:

1. **Deprecation notice**: In current policy version
2. **Migration period**: At least one version overlap
3. **Website adaptation**: Implement new rules before enforcement
4. **Communication**: Document changes clearly
5. **Validation**: Test thoroughly before deployment

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-11 | Initial PUBLICATION_POLICY.md with TRIZEL DIRECTIVE |

---

## Related Documents

- `COPILOT_INSTRUCTIONS.md` — Copilot operating rules
- `ROLE.md` — Layer 0 assignment and scope
- `OUTPUT_CONTRACT.md` — Export contract specifications
- `README.md` — Governance overview
- `docs/GOVERNANCE.md` — Operational governance
