# Metadata Directory

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Directory Purpose**: Canonical storage for author and publication metadata templates

---

## Purpose

This directory contains **canonical metadata templates** that define author, publication, and citation information for the TRIZEL ecosystem.

All metadata files in this directory are:
- **Governance artifacts**: Subject to Layer 0 validation and versioning rules
- **Canonical sources**: Single source of truth for metadata schemas
- **Version-controlled**: All changes tracked via Git with full audit trail
- **Read-only references**: Other repositories reference these files, never duplicate them

---

## Directory Structure

```
docs/metadata/
├── README.md                              ← This file (directory documentation)
├── CANONICAL_METADATA_TEMPLATE.yml        ← Primary canonical metadata template (future)
└── WEBSITE_METADATA.yml                   ← Website-approved metadata subset (future)
```

**Note**: As of version 1.0.0, this directory is prepared for future metadata template placement. Actual YAML template files will be added following the placement plan documented in `METADATA_PLACEMENT_PLAN.md`.

---

## File Descriptions

### CANONICAL_METADATA_TEMPLATE.yml (Future)

**Purpose**: Single source of truth for author and publication metadata schema

**Contents** (planned):
- Author information (names, affiliations, ORCID IDs)
- Publication metadata (title, abstract, keywords)
- License information
- Version and provenance fields
- Schema version specification
- Citation guidance

**Usage**: All other metadata files (CITATION.cff, .zenodo.json, local metadata) derive from this canonical template.

### WEBSITE_METADATA.yml (Future)

**Purpose**: Filtered subset of canonical metadata approved for website publication

**Contents** (planned):
- Website-approved fields only (per PUBLICATION_POLICY.md)
- Marked with `publishable: true`
- Excludes internal/development metadata
- Subject to fail-closed website validation

**Usage**: Website ingestion system consumes this file, not the canonical template directly.

---

## Placement Plan Reference

For complete details on metadata placement strategy, rationale, and workflows, see:

**📄 [METADATA_PLACEMENT_PLAN.md](../METADATA_PLACEMENT_PLAN.md)**

This placement plan document provides:
- Recommended file paths for all metadata placements
- Rationale for each location (canonical, citation, Zenodo, website)
- Read-only usage rules for other repositories
- Version synchronization protocols
- Governance enforcement procedures
- Migration path from current state

---

## Usage Guidelines

### For This Repository (trizel-core)

When adding or updating metadata in this directory:

1. **Follow placement plan**: Reference `METADATA_PLACEMENT_PLAN.md` for file naming and structure
2. **Version explicitly**: Bump schema version for all schema-affecting changes
3. **Synchronize derived artifacts**: Update CITATION.cff and .zenodo.json when canonical template changes
4. **Validate governance compliance**: Run deprecated terms check, schema validation
5. **Document changes**: Update version history in metadata files

### For Other TRIZEL Repositories

Other repositories must **reference, not duplicate** metadata from this directory:

**Approved**: Referencing by URL or Git SHA
```yaml
canonical_schema:
  repository: trizel-ai/trizel-core
  version: v1.0.0
  path: docs/metadata/CANONICAL_METADATA_TEMPLATE.yml
```

**Forbidden**: Copying metadata files into other repositories (creates version skew)

---

## Related Files (Repository Root)

Metadata-related files in repository root (derived from canonical template):

- `/CITATION.cff` — GitHub citation file (derived, auto-detected by GitHub)
- `/.zenodo.json` — Zenodo integration metadata (derived, used for DOI minting)

These root-level files are **derived artifacts** generated from the canonical template in this directory. They should be kept synchronized with the canonical source.

---

## Schema Versioning

All metadata files in this directory must include:

```yaml
schema_version: v1.0.0
repository: trizel-ai/trizel-core
layer: 0
type: metadata_template
effective_date: [ISO 8601 timestamp]
```

**Current schema version**: v1.0.0 (initial, to be set upon first template placement)

---

## Governance Compliance

All metadata files in this directory are subject to:

- ✅ Layer 0 boundary enforcement (governance only, no operational content)
- ✅ Deprecated terms validation (no forbidden terminology)
- ✅ Schema validation (required fields present)
- ✅ Provenance validation (repository, layer, version metadata)
- ✅ Version tracking (Git tags for all releases)
- ✅ CI validation (automated checks on all commits)

---

## Website Integration

For website to consume metadata from this directory:

1. **Use WEBSITE_METADATA.yml**: Not the canonical template directly
2. **Allowlist validation**: Verify file is in approved sources list (per PUBLICATION_POLICY.md)
3. **Schema version check**: Confirm compatibility with website ingestion system
4. **Publishable tag check**: Ensure `publishable: true` is present
5. **Fail-closed behavior**: Reject if any validation fails (no silent degradation)

---

## Zenodo Integration

For Zenodo DOI minting:

1. **Canonical template** provides source data
2. **Root-level .zenodo.json** is derived artifact in Zenodo-specific JSON format
3. **Git release tags** trigger automatic Zenodo deposits
4. **DOI is minted** by Zenodo upon release creation
5. **Update canonical template** with DOI after minting

---

## Citation Workflow

For GitHub citation feature:

1. **Canonical template** provides source data
2. **Root-level CITATION.cff** is derived artifact in Citation File Format
3. **GitHub auto-detects** CITATION.cff and displays "Cite this repository" button
4. **Keep synchronized** with canonical template on all updates
5. **Validate format** using CFF validator before commit

---

## Directory Maintenance

### Adding New Metadata Files

1. Create file in this directory following naming convention
2. Include all required metadata fields (schema_version, provenance, etc.)
3. Update this README.md with file description
4. Update `METADATA_PLACEMENT_PLAN.md` if placement strategy changes
5. Create PR with clear rationale for addition

### Updating Existing Metadata Files

1. Determine if change is major (breaking), minor (additive), or patch (clarification)
2. Bump schema version appropriately
3. Update version history in metadata file
4. Synchronize derived artifacts (CITATION.cff, .zenodo.json)
5. Notify consuming repositories if breaking change

### Deprecating Metadata Files

1. Add deprecation notice in file header
2. Document migration path to replacement
3. Maintain file for at least one version overlap period
4. Update documentation to point to new canonical source
5. Remove only after all consumers migrated

---

## Quick Reference

| Need | Action | File |
|------|--------|------|
| Define metadata schema | Edit canonical template | `CANONICAL_METADATA_TEMPLATE.yml` |
| Update website metadata | Edit website subset | `WEBSITE_METADATA.yml` |
| Add DOI to repository | Update Zenodo file | `/.zenodo.json` (root) |
| Enable GitHub citations | Update CFF file | `/CITATION.cff` (root) |
| Understand placement strategy | Read placement plan | `../METADATA_PLACEMENT_PLAN.md` |
| Reference from other repos | Use Git SHA pinning | (See METADATA_PLACEMENT_PLAN.md) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-12 | Initial directory setup and documentation |

---

## Contact

For questions about metadata placement or usage:

- **Issues**: Open an issue in `trizel-ai/trizel-core`
- **Documentation**: See `METADATA_PLACEMENT_PLAN.md` for comprehensive guidance
- **Governance**: See `PUBLICATION_POLICY.md` for website publication rules
