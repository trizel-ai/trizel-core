# METADATA_PLACEMENT_PLAN.md

## Canonical Author & Publication Metadata YAML Template — Placement Plan

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Document Version**: 1.0.0  
**Last Updated**: 2026-01-12

---

## Purpose

This document provides a **manual placement plan** for the canonical author and publication metadata YAML template within the TRIZEL ecosystem. It specifies **where** to place the YAML template, **why** each location is recommended, and **how** each placement serves governance, citation, and publication objectives.

This is a **documentation and planning resource only**. It does not generate YAML content or automate placement.

---

## Scope

This plan addresses:
- **Canonical storage location** (governance-safe, version-controlled)
- **Optional secondary placements** (Zenodo ingestion, citation files, website consumption)
- **Read-only usage rules** (how other repositories should reference the template)

---

## Core Principles

All placement recommendations follow these governance principles:

1. **Canonical governance separation**: Metadata templates belong in Layer 0 (governance), not in data/analysis layers
2. **Fail-closed validation**: Unknown or unapproved sources must be rejected
3. **Immutability**: Published metadata templates are versioned and never retroactively modified
4. **Traceability**: All placements include provenance and version metadata
5. **Read-only consumption**: Other repositories reference, not duplicate, the canonical template

---

## Placement Recommendations

### 1. Canonical Storage Location (PRIMARY)

**File Path**:  
```
trizel-ai/trizel-core/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml
```

**Directory Structure**:
```
trizel-core/
├── docs/
│   ├── GOVERNANCE.md
│   └── metadata/
│       ├── CANONICAL_METADATA_TEMPLATE.yml  ← PRIMARY CANONICAL SOURCE
│       └── README.md                         ← Placement documentation
```

**Rationale**:
- **Governance-safe**: Located in the Layer 0 governance repository, ensuring epistemic separation from operational layers
- **Version-controlled**: All changes tracked via Git, with full commit history and auditability
- **Single source of truth**: No ambiguity about which version is authoritative
- **Structured storage**: Dedicated `metadata/` subdirectory under `docs/` keeps governance documents organized
- **Discoverability**: Clear path structure (`docs/metadata/`) makes it easy for consumers to locate
- **CI-validated**: Subject to same governance validation checks as all Layer 0 documents (deprecated terms, schema compliance)

**Usage Rules**:
- **Read-only reference**: Other repositories should reference this file by URL or Git ref, never copy
- **Version pinning**: Consumers must pin to specific Git commit SHA or release tag
- **Schema version**: Must include `schema_version` field for compatibility tracking

---

### 2. Root-Level Reference (OPTIONAL SECONDARY)

**File Path**:  
```
trizel-ai/trizel-core/CITATION.cff
```

**Rationale**:
- **GitHub integration**: GitHub automatically recognizes `CITATION.cff` files and displays citation information
- **Standard location**: Root-level placement follows community convention (e.g., GitHub's "Cite this repository" feature)
- **Citation File Format (CFF)**: Industry-standard format for software/repository citation metadata
- **Automatic ingestion**: Tools like Zenodo, Zotero, and citation managers can auto-discover CFF files
- **User-facing**: Visible to external researchers and citation tools without navigating subdirectories

**Relationship to Canonical Template**:
- This is a **derived artifact** generated from the canonical YAML template
- Should include reference to canonical source: `references: docs/metadata/CANONICAL_METADATA_TEMPLATE.yml`
- Not the authoritative source, but the **public interface** for citations

**Contents**:
- Author metadata (names, affiliations, ORCID IDs)
- Repository metadata (title, version, DOI)
- License information
- Publication date
- Keywords and abstract
- References to canonical template

---

### 3. Zenodo Integration Metadata (OPTIONAL SECONDARY)

**File Path**:  
```
trizel-ai/trizel-core/.zenodo.json
```

**Rationale**:
- **Zenodo integration**: Zenodo uses `.zenodo.json` to automatically populate metadata when creating DOI records
- **DOI generation**: Enables automatic DOI minting for repository releases via GitHub-Zenodo integration
- **Archival compliance**: Ensures proper archival metadata when repository snapshots are preserved
- **Hidden file convention**: `.zenodo.json` (dot-prefixed) follows standard practice for repository metadata
- **Release automation**: Triggers automatic Zenodo deposit when GitHub releases are created

**Relationship to Canonical Template**:
- Another **derived artifact** from the canonical YAML template
- Transformed into Zenodo's JSON schema format
- Must maintain version synchronization with canonical source
- Should include provenance field: `"related_identifiers": [{"identifier": "https://github.com/trizel-ai/trizel-core/blob/main/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml", "relation": "isDocumentedBy"}]`

**Contents**:
- Zenodo-specific metadata fields (creators, title, description, keywords)
- Related identifiers (links to canonical template, publication URLs)
- License metadata
- Version information

---

### 4. Website Ingestion Source (OPTIONAL SECONDARY)

**File Path**:  
```
trizel-ai/trizel-core/docs/metadata/WEBSITE_METADATA.yml
```

**Rationale**:
- **Website-specific subset**: Contains only the metadata fields approved for website publication (per PUBLICATION_POLICY.md)
- **Allowlist compliance**: Explicitly marked as `publishable: true` for website ingestion validation
- **Separation of concerns**: Website consumes a curated subset, not the full canonical template
- **Transformation layer**: Acts as an adapter between canonical storage and website schema requirements
- **Governance enforcement**: Subject to fail-closed validation rules defined in PUBLICATION_POLICY.md

**Relationship to Canonical Template**:
- **Filtered subset** of canonical template
- Includes only fields approved for website publication:
  - Methodology description
  - Provenance information (version, repository, layer)
  - Citation information (DOI pointers, license)
  - Status metadata (canonical designation, effective date)
- Excludes: Internal metadata, development notes, non-public identifiers

**Contents**:
```yaml
publishable: true
layer: 0
type: metadata
schema_version: v1.0.0
repository: trizel-ai/trizel-core
canonical_source: docs/metadata/CANONICAL_METADATA_TEMPLATE.yml
website_approved_fields:
  - title
  - description
  - authors
  - license
  - doi
  - version
  - effective_date
  - repository_url
```

---

### 5. Repository-Specific Metadata (FUTURE EXPANSION)

**File Path Pattern** (for other TRIZEL repositories):  
```
trizel-ai/<repository-name>/docs/metadata/LOCAL_METADATA.yml
```

**Examples**:
```
trizel-ai/trizel-visual/docs/metadata/LOCAL_METADATA.yml
trizel-ai/trizel-data-primary/docs/metadata/LOCAL_METADATA.yml
trizel-ai/trizel-analysis-core/docs/metadata/LOCAL_METADATA.yml
```

**Rationale**:
- **Decentralized storage**: Each repository maintains its own local metadata
- **Canonical reference**: All local metadata files reference `trizel-core/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml` as schema
- **Layer-specific fields**: Allows repositories to extend canonical template with layer-specific metadata
- **Governance validation**: Each local metadata file validated against canonical schema during CI
- **Consistency**: All repositories use same directory structure pattern (`docs/metadata/`)

**Relationship to Canonical Template**:
- **Extends** canonical template with repository-specific fields
- **Inherits** schema version and validation rules from canonical source
- Must include reference field: `canonical_schema: trizel-ai/trizel-core@v1.0.0/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml`

**Contents**:
- Repository-specific author contributions
- Layer-specific metadata (e.g., dataset DOI for data repositories, algorithm citation for analysis repositories)
- Local provenance (repository version, last update, maintainer)
- Extension fields (layer-appropriate additions beyond canonical template)

---

## Placement Summary Table

| Location | File Path | Type | Purpose | Governance Status |
|----------|-----------|------|---------|-------------------|
| **Canonical** | `trizel-core/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml` | YAML | Single source of truth | PRIMARY |
| **Citation** | `trizel-core/CITATION.cff` | CFF | GitHub citation integration | DERIVED |
| **Zenodo** | `trizel-core/.zenodo.json` | JSON | DOI generation, archival | DERIVED |
| **Website** | `trizel-core/docs/metadata/WEBSITE_METADATA.yml` | YAML | Website ingestion subset | FILTERED |
| **Local** | `<repo>/docs/metadata/LOCAL_METADATA.yml` | YAML | Repository-specific extensions | EXTENDED |

---

## Directory Structure Recommendation

**Canonical governance repository** (`trizel-core`):
```
trizel-core/
├── .zenodo.json                          ← Zenodo integration (derived)
├── CITATION.cff                          ← GitHub citation (derived)
├── docs/
│   ├── GOVERNANCE.md
│   └── metadata/
│       ├── README.md                     ← Placement documentation (this plan)
│       ├── CANONICAL_METADATA_TEMPLATE.yml   ← PRIMARY CANONICAL SOURCE
│       └── WEBSITE_METADATA.yml          ← Website ingestion subset (filtered)
```

**Other TRIZEL repositories** (example: `trizel-visual`):
```
trizel-visual/
├── .zenodo.json                          ← Local Zenodo metadata (optional)
├── CITATION.cff                          ← Local citation file (optional)
├── docs/
│   └── metadata/
│       ├── LOCAL_METADATA.yml            ← Repository-specific metadata
│       └── README.md                     ← Local usage documentation
```

---

## Read-Only Usage Rules

### For Other TRIZEL Repositories

Other repositories must **reference, not duplicate** the canonical template:

**Approved Methods**:

1. **Git submodule reference** (not recommended for governance files):
   - Not recommended due to submodule complexity
   
2. **Direct URL reference** (preferred for CI validation):
   ```bash
   curl -L https://raw.githubusercontent.com/trizel-ai/trizel-core/v1.0.0/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml
   ```

3. **Git SHA pinning** (recommended for reproducibility):
   ```yaml
   canonical_schema:
     repository: trizel-ai/trizel-core
     ref: e80415ec05df6f1b00cb77f2a6d54402c7ec4c32  # Git commit SHA
     path: docs/metadata/CANONICAL_METADATA_TEMPLATE.yml
   ```

4. **Release tag pinning** (recommended for stability):
   ```yaml
   canonical_schema:
     repository: trizel-ai/trizel-core
     version: v1.0.0
     path: docs/metadata/CANONICAL_METADATA_TEMPLATE.yml
   ```

**Forbidden Methods**:
- Copying canonical template into other repositories (creates version skew)
- Modifying canonical template in non-governance repositories (violates layer separation)
- Hard-coding canonical template content (prevents updates)

---

## Version Synchronization Rules

When the canonical template is updated:

### Minor Updates (Schema-Compatible)
- Example: `v1.0.0` → `v1.1.0`
- **Action**: Derived artifacts (CITATION.cff, .zenodo.json) updated in same PR
- **Notification**: Other repositories notified via release notes
- **Compatibility**: Backward-compatible, consumers can update at their convenience

### Major Updates (Breaking Changes)
- Example: `v1.0.0` → `v2.0.0`
- **Action**: Requires linked PRs in all consuming repositories
- **Notification**: Advance notice required (at least one release cycle)
- **Compatibility**: Breaking changes documented, migration guide provided
- **Enforcement**: New version not enforced until all consumers updated

### Patch Updates (Non-Schema)
- Example: `v1.0.0` → `v1.0.1`
- **Action**: Documentation updates, clarifications only
- **Notification**: Release notes only
- **Compatibility**: No schema changes, no consumer updates required

---

## Governance Enforcement

### Pre-Placement Validation

Before placing any metadata YAML file, validate:

1. **Layer boundary check**: Metadata templates only in Layer 0 (trizel-core)
2. **Deprecated terms check**: No forbidden terminology in metadata content
3. **Schema version**: Includes `schema_version` field
4. **Provenance**: Includes repository, layer, effective_date fields
5. **Publishable tag**: Website-facing files marked `publishable: true`

### Post-Placement Validation

After placement, ensure:

1. **CI integration**: Metadata files included in governance validation workflows
2. **Version tracking**: Git tags created for all canonical template versions
3. **Documentation updated**: README.md in metadata/ directory reflects new files
4. **Allowlist updated**: PUBLICATION_POLICY.md updated if website ingestion affected
5. **Audit trail**: Changes logged with clear commit messages and version bumps

---

## Website Ingestion Workflow

For website to consume metadata:

1. **Allowlist check**: Verify `trizel-core/docs/metadata/WEBSITE_METADATA.yml` in approved sources
2. **Schema validation**: Confirm schema_version matches website expectations
3. **Publishable tag check**: Ensure `publishable: true` present
4. **Field filtering**: Ingest only approved fields (per PUBLICATION_POLICY.md)
5. **Fail-closed behavior**: Reject if any validation fails

**Website must NOT**:
- Ingest canonical template directly (use WEBSITE_METADATA.yml instead)
- Bypass allowlist validation
- Silently skip failed validation
- Guess or infer missing fields

---

## Zenodo Integration Workflow

For Zenodo to create DOI records:

1. **Enable GitHub-Zenodo integration**: Link repository to Zenodo account
2. **Place `.zenodo.json`**: In repository root with complete metadata
3. **Create GitHub release**: Tag version (e.g., `v1.0.0`)
4. **Automatic deposit**: Zenodo automatically creates DOI and archives release
5. **Update metadata**: Add DOI to CANONICAL_METADATA_TEMPLATE.yml after minting

**Zenodo metadata must include**:
- All author ORCID IDs (if available)
- License identifier (e.g., `MIT`)
- Related identifiers (link to canonical template)
- Version information (matches Git tag)

---

## Citation File (CFF) Integration Workflow

For GitHub citation feature:

1. **Create CITATION.cff**: In repository root with CFF-compliant metadata
2. **Validate format**: Use CFF validator (https://citation-file-format.github.io/cff-initializer-javascript/)
3. **GitHub auto-detection**: GitHub displays "Cite this repository" button
4. **Keep synchronized**: Update CITATION.cff when canonical template changes
5. **Version consistency**: CFF version matches repository release version

**CFF file must include**:
- All authors with ORCID IDs
- Repository title and abstract
- License information
- Preferred citation format
- DOI (if available from Zenodo)

---

## Migration Path (From Current State)

If metadata YAML does not currently exist:

1. **Create canonical template**: In `trizel-core/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml`
2. **Add placement documentation**: Create `docs/metadata/README.md` (reference this document)
3. **Generate derived artifacts**: Create CITATION.cff and .zenodo.json from canonical template
4. **Update PUBLICATION_POLICY.md**: Add metadata files to approved sources list
5. **Update allowlist**: If website ingestion planned, add WEBSITE_METADATA.yml to allowlist
6. **Version and release**: Tag as v1.0.0, create GitHub release
7. **Enable Zenodo**: Link repository, trigger initial DOI minting
8. **Notify consumers**: Inform other TRIZEL repositories of canonical metadata availability

---

## Compliance Checklist

Before finalizing metadata placement:

- [ ] Canonical template placed in `trizel-core/docs/metadata/`
- [ ] Schema version field included in all metadata files
- [ ] Provenance fields complete (repository, layer, effective_date)
- [ ] Layer 0 boundary respected (no metadata in non-governance repos)
- [ ] Derived artifacts synchronized with canonical source
- [ ] Website ingestion file marked `publishable: true` (if applicable)
- [ ] Deprecated terms check passed for all metadata content
- [ ] Documentation updated (README.md in metadata/ directory)
- [ ] CI validation configured for metadata files
- [ ] Version tagged and release created (if applicable)
- [ ] Zenodo integration enabled (if DOI needed)
- [ ] CITATION.cff created and validated (if GitHub citation needed)

---

## Related Documents

- `PUBLICATION_POLICY.md` — Website publication rules and allowlist specifications
- `OUTPUT_CONTRACT.md` — Export contract for governance artifacts
- `ROLE.md` — Layer 0 assignment and scope
- `docs/GOVERNANCE.md` — Operational governance rules

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-12 | Initial METADATA_PLACEMENT_PLAN.md creation |

---

## Contact & Governance

This document is maintained as part of the `trizel-core` governance repository.

**Updates**: All changes to this placement plan require:
- PR in `trizel-core`
- Version bump in this document
- Review by repository maintainers
- CI validation pass

**Questions**: Open an issue in `trizel-ai/trizel-core` for clarification or proposed changes to this placement plan.
