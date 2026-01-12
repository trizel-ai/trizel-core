# TRIZEL_REGISTRY.yaml Schema Definition

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Schema Version**: 1.0.0  
**Last Updated**: 2026-01-12

---

## Purpose

This document defines the canonical schema for `TRIZEL_REGISTRY.yaml`, including all fields, their constraints, validation rules, and semantic meanings.

---

## Top-Level Structure

```yaml
registry_metadata:
  # Metadata about the registry itself

repositories:
  # Array of repository entries
```

---

## Registry Metadata Fields

### `registry_metadata`

**Type**: Object  
**Required**: Yes  
**Purpose**: Provenance and version information about the registry itself

#### Fields:

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `version` | string | Yes | Semantic version (e.g., "1.0.0") | Registry document version |
| `schema_version` | string | Yes | Semantic version (e.g., "1.0.0") | Schema format version |
| `repository` | string | Yes | Valid GitHub repository path | Source repository for this registry |
| `layer` | integer | Yes | Must be 0 | Layer assignment (always 0 for governance) |
| `effective_date` | string | Yes | ISO 8601 timestamp | When this registry version became effective |
| `status` | string | Yes | One of: `canonical`, `draft`, `deprecated` | Registry status |
| `publishable` | boolean | Yes | Must be `true` | Website publication flag |

---

## Repository Entry Fields

### `repositories[]`

**Type**: Array of Objects  
**Required**: Yes  
**Purpose**: List of all TRIZEL repositories with their metadata

#### Entry Structure:

Each repository entry must contain the following fields:

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `repository` | string | Yes | Valid GitHub repository path (owner/name) | Full repository identifier |
| `layer` | integer | Yes | 0-6 inclusive | Epistemic layer assignment |
| `status` | string | Yes | One of: `active`, `archived`, `draft`, `deprecated` | Repository operational status |
| `canonical` | boolean | Yes | `true` or `false` | Whether repository has canonical authority |
| `role` | string | Yes | See role vocabulary below | Repository's functional role |
| `i18n` | object | Yes | See i18n structure below | Multilingual metadata |
| `pending_branches` | array | No | See pending branches structure below | Optional branch tracking |

---

## Layer Assignment Definitions

### Valid Layer Values

| Layer | Name | Purpose | Examples |
|-------|------|---------|----------|
| 0 | Governance & Charter | Rules, boundaries, structural principles | trizel-core |
| 1 | Algorithm Definition | Canonical algorithm specifications | Auto-dz-act |
| 2 | Data & Observation | Raw data, monitoring, data collection | trizel-monitor |
| 3 | Analysis & Inference | Computational analysis, statistical inference | analysis repositories |
| 4 | Evaluation & Gateway | Probabilistic evaluation, TCRL boundary | trizel-phase4-gateway |
| 5 | Reserved | Future use | — |
| 6 | Visualization & Publication | Website, orchestration, public interface | trizel-AI |

### Layer Constraints

- **Required**: Every repository must have exactly one layer assignment
- **Immutable**: Layer assignments should not change without governance review
- **Non-mixing**: Repositories cannot span multiple layers
- **Separation**: Layer boundaries must be respected (no cross-layer content)

---

## Status Values

### Valid Status Values

| Status | Meaning | Usage |
|--------|---------|-------|
| `active` | Currently operational and maintained | Production repositories |
| `archived` | No longer active but preserved | Historical repositories |
| `draft` | Under development, not yet operational | Pre-release repositories |
| `deprecated` | Scheduled for removal or replacement | Legacy repositories |

### Status Constraints

- **Required**: All repositories must have a status
- **Transitions**: Status changes should be documented in registry version history
- **Website**: Only `active` repositories are typically displayed on the website

---

## Canonical Flag

### Definition

- **`canonical: true`**: Repository has official authority within its layer
- **`canonical: false`**: Repository is experimental, exploratory, or alternative

### Rules

- Layer 0 repositories should always be canonical
- Only one canonical repository per functional role per layer (when applicable)
- Canonical status does not imply correctness, only structural authority
- Non-canonical repositories may explore alternatives or experimental approaches

---

## Role Vocabulary

### Valid Role Values

Roles are constrained to a predefined vocabulary to maintain consistency:

| Role | Layer | Description |
|------|-------|-------------|
| `governance_charter` | 0 | Governance and constitutional framework |
| `algorithm_definition` | 1 | Canonical algorithm specifications |
| `data_observation` | 2 | Data collection and observational records |
| `monitoring_observation` | 2 | Continuous monitoring and data acquisition |
| `analysis_inference` | 3 | Statistical analysis and computational inference |
| `evaluation_gateway` | 4 | Probabilistic evaluation and boundary interface |
| `website_orchestration` | 6 | Website, visualization, and public interface |

### Role Constraints

- Roles must match their layer assignment
- Roles are non-interpretive and descriptive only
- New roles require governance approval and schema update

---

## Multilingual Metadata (i18n)

### Structure

```yaml
i18n:
  en:
    title: "English Title"
    description: "English one-line description"
  fr:
    title: "Titre français"
    description: "Description française en une ligne"
  ar:
    title: "العنوان العربي"
    description: "وصف عربي من سطر واحد"
```

### Required Languages

The registry must support the following languages:

- **`en`**: English (required)
- **`fr`**: French (required)
- **`ar`**: Arabic (required)

### Field Constraints

#### `i18n.<lang>.title`

- **Type**: string
- **Required**: Yes (for each language)
- **Max length**: 100 characters
- **Content**: Non-interpretive repository name or designation
- **Prohibited**: Deprecated terminology, interpretive claims, theoretical labels

#### `i18n.<lang>.description`

- **Type**: string
- **Required**: Yes (for each language)
- **Max length**: 200 characters
- **Content**: Factual, one-line description of repository purpose
- **Prohibited**: Analytical conclusions, interpretive claims, deprecated terminology

### i18n Validation Rules

1. All three languages must be present for every repository
2. Titles must be concise and non-interpretive
3. Descriptions must be factual, not analytical
4. No deprecated terms allowed (see `../../DEPRECATED_TERMS.md`)
5. Translations should be semantically equivalent across languages
6. Text must be suitable for public website display

---

## Optional: Pending Branches

### Structure

```yaml
pending_branches:
  - branch_name: "feature/new-feature"
    purpose: "Non-interpretive description of branch purpose"
    status: "draft"
  - branch_name: "fix/bug-fix"
    purpose: "Bug fix for specific issue"
    status: "ready"
```

### Fields

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `branch_name` | string | Yes | Valid git branch name | Name of the pending branch |
| `purpose` | string | Yes | Max 200 chars, non-interpretive | Factual description of branch intent |
| `status` | string | Yes | One of: `draft`, `ready`, `blocked` | Branch readiness status |

### Status Values

- **`draft`**: Work in progress, not ready for review
- **`ready`**: Ready for review or merge
- **`blocked`**: Blocked by dependencies or issues

### Constraints

- This field is **optional** — repositories may omit it entirely
- If present, must be an array (even if empty: `[]`)
- Branch information is **not** automatically discovered
- Must be manually maintained by repository owners
- Purpose descriptions must be non-interpretive and factual

---

## Validation Rules

### Automated Validation

The registry must pass the following automated checks:

1. **YAML Syntax**: Valid YAML 1.2 format
2. **Schema Compliance**: All required fields present
3. **Type Validation**: All fields match expected types
4. **Constraint Validation**: All constraints satisfied (e.g., layer 0-6, valid status)
5. **Deprecated Terms Check**: No forbidden terminology present
6. **Uniqueness**: No duplicate repository entries
7. **i18n Completeness**: All three languages present for all repositories
8. **Character Limits**: Title ≤100 chars, description ≤200 chars

### Manual Review

The following aspects require manual governance review:

1. **Accuracy**: Repository metadata correctly represents actual repositories
2. **Completeness**: All TRIZEL repositories are included
3. **Layer Assignment**: Layer values are appropriate and justified
4. **Role Assignment**: Roles accurately describe repository function
5. **Translation Quality**: i18n translations are semantically correct
6. **Non-Interpretive**: All text is factual, not analytical or interpretive

---

## Prohibited Content

### Absolutely Forbidden

The registry must **never** contain:

1. **Deprecated terminology**: See `../../DEPRECATED_TERMS.md`
   - "STOE"
   - "V12-V22" version labels
   - Versioned system labels
   - Theoretical lineage references

2. **Interpretive content**:
   - Analytical conclusions
   - Theoretical claims
   - Performance comparisons
   - Scientific interpretations

3. **Executable content**:
   - Code snippets
   - Scripts
   - Automation logic
   - Dynamic discovery mechanisms

4. **Cross-layer content**:
   - Data values
   - Analysis results
   - Computational outputs
   - Non-governance material

---

## Schema Versioning

### Current Version: 1.0.0

### Version Change Policy

- **Patch** (1.0.x): Clarifications, typos, metadata updates
- **Minor** (1.x.0): New optional fields, new languages, backwards-compatible additions
- **Major** (x.0.0): Breaking changes, required field changes, structural redesign

### Backwards Compatibility

- Website must support at least the current and previous minor versions
- Major version changes require coordinated website updates
- Deprecation notice required before removing fields

---

## Update Protocol

### Adding New Repositories

1. Create PR in `trizel-core`
2. Add repository entry to `TRIZEL_REGISTRY.yaml`
3. Ensure all required fields present
4. Provide all three i18n languages
5. Validate against this schema
6. Pass deprecated terms check
7. Document reason for addition
8. Increment registry version (minor bump)

### Modifying Existing Entries

1. Create PR in `trizel-core`
2. Update relevant fields
3. Document reason for change
4. Validate against schema
5. Pass all CI checks
6. Increment registry version (patch or minor bump)
7. Notify website maintainers if breaking changes

### Removing Repositories

1. Change `status` to `deprecated` first (one version)
2. Remove entry in subsequent version
3. Document reason for removal
4. Increment registry version (major bump if canonical repository)
5. Update website to handle removal gracefully

---

## Compliance Checklist

For every registry update:

- [ ] Valid YAML syntax: PASS
- [ ] All required fields present: YES
- [ ] Layer assignments valid (0-6): YES
- [ ] Status values valid: YES
- [ ] Role vocabulary matches: YES
- [ ] All i18n languages present (en, fr, ar): YES
- [ ] Character limits respected: YES
- [ ] No deprecated terminology: YES
- [ ] No interpretive content: YES
- [ ] No executable content: YES
- [ ] Uniqueness validated: YES
- [ ] Manual review completed: YES

---

## Related Documents

- `TRIZEL_REGISTRY.yaml` — The registry itself
- `README.md` — Website consumption guidelines (in this directory)
- `../../ROLE.md` — Layer 0 repository role definition
- `../../DEPRECATED_TERMS.md` — Forbidden terminology
- `../../PUBLICATION_POLICY.md` — Website publication rules

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-12 | Initial schema definition for TRIZEL registry |
