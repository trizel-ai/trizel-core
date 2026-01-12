# Canonical Metadata YAML Template — Placement Summary

**Task**: Manual placement plan for canonical author & publication metadata YAML  
**Output**: Recommended file paths and rationale (documentation only, no PRs, no code changes)  
**Date**: 2026-01-12

---

## Step-by-Step Manual Placement Plan

### PRIMARY PLACEMENT: Canonical Storage (Required)

**File Path**: `trizel-ai/trizel-core/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml`

**Rationale**:
- Single source of truth for all metadata schemas across TRIZEL ecosystem
- Located in Layer 0 governance repository, ensuring epistemic separation
- Version-controlled via Git with full audit trail
- CI-validated against deprecated terms and governance rules
- Discoverable via standardized path structure (`docs/metadata/`)
- All other metadata placements derive from this canonical source

**Usage Rule**: Read-only reference by other repositories (never copy/duplicate)

---

### SECONDARY PLACEMENT 1: GitHub Citation Integration (Optional)

**File Path**: `trizel-ai/trizel-core/CITATION.cff`

**Rationale**:
- GitHub auto-detects `CITATION.cff` in repository root
- Enables "Cite this repository" button in GitHub UI
- Standard Citation File Format (CFF) recognized by academic tools
- Auto-discovered by citation managers (Zotero, Mendeley, etc.)
- User-facing location for external researchers

**Usage Rule**: Derived artifact from canonical template (must stay synchronized)

---

### SECONDARY PLACEMENT 2: Zenodo Integration (Optional)

**File Path**: `trizel-ai/trizel-core/.zenodo.json`

**Rationale**:
- Zenodo uses `.zenodo.json` for automatic DOI minting
- Enables GitHub-Zenodo integration for release archival
- Triggers automatic DOI creation when GitHub releases are tagged
- Supports long-term preservation and academic citation
- Hidden file convention (dot-prefixed) for repository metadata

**Usage Rule**: Derived artifact in Zenodo JSON format (converted from canonical YAML)

---

### SECONDARY PLACEMENT 3: Website Ingestion (Optional)

**File Path**: `trizel-ai/trizel-core/docs/metadata/WEBSITE_METADATA.yml`

**Rationale**:
- Filtered subset containing only website-approved fields
- Enforces fail-closed validation per PUBLICATION_POLICY.md
- Marked with `publishable: true` for allowlist compliance
- Separates public-facing metadata from internal canonical template
- Enables governance-safe website consumption

**Usage Rule**: Read-only consumption by website (allowlist-validated, fail-closed)

---

### FUTURE PLACEMENT: Repository-Specific Extensions (Pattern)

**File Path Pattern**: `trizel-ai/<repository-name>/docs/metadata/LOCAL_METADATA.yml`

**Examples**:
- `trizel-ai/trizel-visual/docs/metadata/LOCAL_METADATA.yml`
- `trizel-ai/trizel-data-primary/docs/metadata/LOCAL_METADATA.yml`
- `trizel-ai/trizel-analysis-core/docs/metadata/LOCAL_METADATA.yml`

**Rationale**:
- Allows repositories to extend canonical template with layer-specific metadata
- Maintains consistency via standardized directory pattern
- Each local file references canonical template as schema authority
- CI-validated against canonical template during builds
- Enables decentralized storage while preserving governance

**Usage Rule**: Must reference canonical template and include schema version

---

## Recommended Directory Structure

### In trizel-core (Governance Repository)

```
trizel-core/
├── .zenodo.json                              ← Zenodo integration (derived)
├── CITATION.cff                              ← GitHub citation (derived)
├── docs/
│   ├── GOVERNANCE.md
│   ├── METADATA_PLACEMENT_PLAN.md            ← Full placement documentation
│   └── metadata/
│       ├── README.md                         ← Directory documentation
│       ├── CANONICAL_METADATA_TEMPLATE.yml   ← PRIMARY SOURCE
│       └── WEBSITE_METADATA.yml              ← Website subset (filtered)
```

### In Other TRIZEL Repositories (Example)

```
trizel-visual/
├── .zenodo.json                              ← Optional: local Zenodo metadata
├── CITATION.cff                              ← Optional: local citation file
├── docs/
│   └── metadata/
│       ├── LOCAL_METADATA.yml                ← Repository-specific metadata
│       └── README.md                         ← Local usage documentation
```

---

## Read-Only Usage Rules

### How Other Repositories Should Reference Canonical Template

**Approved Methods**:

- **Git SHA pinning** (recommended for reproducibility):
  - Reference specific commit: `trizel-ai/trizel-core@<commit-sha>/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml`
  - Example: `trizel-ai/trizel-core@ea48a5f/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml`

- **Release tag pinning** (recommended for stability):
  - Reference version tag: `trizel-ai/trizel-core@v1.0.0/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml`

- **Direct URL reference** (for CI validation):
  - Raw GitHub URL: `https://raw.githubusercontent.com/trizel-ai/trizel-core/v1.0.0/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml`

**Forbidden Methods**:

- ❌ Copying canonical template into other repositories (creates version skew)
- ❌ Modifying canonical template in non-governance repositories (violates layer separation)
- ❌ Hard-coding template content (prevents updates)

---

## Governance-Safe Scope

### What Can Be Placed in Metadata Files (Allowed)

- Author names, affiliations, ORCID identifiers
- Publication titles, abstracts, keywords
- License information (e.g., MIT)
- DOI references (after Zenodo minting)
- Repository provenance (URL, version, layer)
- Citation guidance and preferred formats
- Schema version and effective dates
- Contact information for maintainers

### What Cannot Be Placed (Forbidden per Layer 0 Governance)

- ❌ Scientific data or observational records
- ❌ Analysis results or statistical outputs
- ❌ Theoretical claims or interpretations
- ❌ Executable code or algorithms
- ❌ Model predictions or inferences
- ❌ Automated workflow scripts
- ❌ Content from other epistemic layers (1-6)

---

## Website Ingestion Rules (Read-Only)

### Website Must Follow

- Consume `WEBSITE_METADATA.yml` only (not canonical template directly)
- Validate against allowlist (per PUBLICATION_POLICY.md)
- Check `publishable: true` tag is present
- Verify schema version compatibility
- Use fail-closed behavior (reject if validation fails)
- Never silently skip or degrade on validation failure

### Website Must Not

- ❌ Bypass allowlist validation
- ❌ Ingest non-approved metadata fields
- ❌ Silently ignore validation failures
- ❌ Guess or infer missing metadata

---

## Zenodo Integration Workflow (Read-Only)

### To Enable DOI Minting

1. Enable GitHub-Zenodo integration (link repository to Zenodo account)
2. Place `.zenodo.json` in repository root with complete metadata
3. Create GitHub release with version tag (e.g., `v1.0.0`)
4. Zenodo automatically creates DOI and archives release
5. Update canonical template with minted DOI

### Zenodo Metadata Must Include

- All author ORCID IDs (if available)
- License identifier (e.g., `MIT`)
- Related identifiers (link to canonical template)
- Version matching Git release tag

---

## Citation File Format (CFF) Integration (Read-Only)

### To Enable GitHub Citation Button

1. Create `CITATION.cff` in repository root with CFF-compliant metadata
2. Validate format using CFF validator (https://citation-file-format.github.io/)
3. GitHub auto-detects file and displays "Cite this repository" button
4. Keep synchronized with canonical template on all updates
5. Ensure CFF version matches repository release version

### CFF File Must Include

- All authors with ORCID IDs
- Repository title and abstract
- License information
- Preferred citation format
- DOI (if available from Zenodo)

---

## Version Synchronization (Manual Process)

### When Canonical Template Updates

**Minor Updates** (schema-compatible, e.g., v1.0.0 → v1.1.0):
- Update derived artifacts (CITATION.cff, .zenodo.json) in same PR
- Notify other repositories via release notes
- Consumers can update at convenience (backward-compatible)

**Major Updates** (breaking changes, e.g., v1.0.0 → v2.0.0):
- Requires linked PRs in all consuming repositories
- Advance notice required (at least one release cycle)
- Breaking changes documented with migration guide
- New version not enforced until all consumers updated

**Patch Updates** (documentation only, e.g., v1.0.0 → v1.0.1):
- Release notes only, no consumer updates required
- No schema changes

---

## Compliance Checklist (Before Placement)

Before placing any metadata YAML file, validate:

- [ ] Located in correct directory (`docs/metadata/` for canonical, root for derived)
- [ ] Includes `schema_version` field for compatibility tracking
- [ ] Includes provenance fields (repository, layer, effective_date)
- [ ] Respects Layer 0 boundaries (no non-governance content)
- [ ] Passes deprecated terms validation (no forbidden terminology)
- [ ] Derived artifacts synchronized with canonical source (if applicable)
- [ ] Website files marked `publishable: true` (if for website ingestion)
- [ ] Documentation updated (README.md in metadata directory)
- [ ] Version tagged if creating release (e.g., v1.0.0)

---

## Key Takeaways

1. **Single Canonical Source**: `trizel-core/docs/metadata/CANONICAL_METADATA_TEMPLATE.yml` is the only authoritative template
2. **All Other Placements Are Derived**: CITATION.cff, .zenodo.json, WEBSITE_METADATA.yml derive from canonical source
3. **Read-Only References**: Other repositories reference canonical template by Git SHA/tag, never copy
4. **Governance Separation**: Metadata templates belong in Layer 0 only (no metadata in operational layers)
5. **Version Control Critical**: All changes tracked, versioned, and synchronized across derived artifacts
6. **Fail-Closed Validation**: Unknown sources, missing tags, or validation failures must halt ingestion
7. **No Automation**: This is a manual placement plan (no code generation, no automated processes)

---

## Documentation Reference

For comprehensive details, see:
- **Full Placement Plan**: `docs/METADATA_PLACEMENT_PLAN.md` (454 lines, complete workflows)
- **Metadata Directory**: `docs/metadata/README.md` (239 lines, usage guidelines)
- **Governance Policy**: `PUBLICATION_POLICY.md` (website ingestion rules)
- **Export Contract**: `OUTPUT_CONTRACT.md` (consumer requirements)

---

**Note**: This is a documentation-only deliverable. No PRs created, no repository modifications made, no YAML templates generated. This plan provides manual placement guidance only.
