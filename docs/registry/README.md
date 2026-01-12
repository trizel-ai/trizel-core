# TRIZEL Registry — Website Integration Guide

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Document Version**: 1.0.0  
**Last Updated**: 2026-01-12

---

## Purpose

This document describes how the TRIZEL website (and other consumers) should consume `TRIZEL_REGISTRY.yaml` to display repository information, enforce allowlist-only publication rules, and maintain epistemic boundaries.

---

## Overview

`TRIZEL_REGISTRY.yaml` is the **canonical source of truth** for all TRIZEL repositories. It provides:

- Repository inventory with layer assignments
- Multilingual metadata for website display (English, French, Arabic)
- Operational status and canonical designation
- Optional branch tracking information

The website must consume this registry using **strict allowlist-only validation** with **fail-closed behavior**.

---

## Core Principles

### 1. Allowlist-Only Ingestion

The website must **only** ingest repositories explicitly listed in this registry.

**Forbidden behaviors**:
- Automatic repository discovery
- Dynamic GitHub API scanning
- Inferring repositories from organization membership
- Guessing or assuming repository inclusion

**Required behavior**:
- Check registry explicitly
- Reject unlisted repositories
- Fail build if unknown source detected

### 2. Fail-Closed Validation

When encountering issues, the website must **fail the build** rather than degrade gracefully.

**Fail conditions**:
- Repository not in registry
- Invalid schema version
- Missing required metadata
- Missing or incomplete i18n translations
- Deprecated terminology detected
- Schema validation failure

**Never**:
- Silently skip invalid entries
- Display partial or incomplete data
- Guess missing values
- Proceed with warnings

### 3. Non-Interpretive Display

All displayed content must be **factual and descriptive only**.

**Allowed**:
- Repository titles and descriptions from registry
- Layer assignments and roles
- Operational status
- Provenance metadata (version, date, source)

**Forbidden**:
- Adding interpretive commentary
- Comparing or ranking repositories
- Making analytical claims
- Displaying non-approved metadata

---

## Integration Workflow

### Step 1: Fetch Registry

```yaml
# Website build process pseudocode

1. Fetch TRIZEL_REGISTRY.yaml from trizel-ai/trizel-core
2. Validate schema version compatibility
3. Parse YAML structure
4. Validate against schema (see SCHEMA.md)
```

**Source location**: `https://github.com/trizel-ai/trizel-core/blob/main/docs/registry/TRIZEL_REGISTRY.yaml`

**Version pinning**: The website should reference a specific registry version or commit SHA for stability.

### Step 2: Validate Schema

```yaml
Required validations:
  - YAML syntax: valid
  - Schema version: matches website compatibility
  - Registry metadata: all required fields present
  - Repositories array: not empty
  - Each repository entry: conforms to schema (see SCHEMA.md)
```

**If validation fails**: Halt build, log specific error, require fix before deployment.

### Step 3: Check for Deprecated Terms

Before using any registry content:

```yaml
Scan entire registry for:
  - "STOE" → REJECT
  - "V12" through "V22" → REJECT
  - Theoretical lineage terms → REJECT
  - Other deprecated terms (see ../../DEPRECATED_TERMS.md) → REJECT
```

**If deprecated terms found**: Fail build immediately, report location, require removal.

### Step 4: Extract Repository Data

For each repository in the registry:

```yaml
Extract:
  - repository: Full GitHub path (owner/name)
  - layer: Integer 0-6
  - status: active | archived | draft | deprecated
  - canonical: boolean
  - role: String from role vocabulary
  - i18n: Object with en, fr, ar translations
  - pending_branches: Optional array
```

**Validation per entry**:
- All required fields present
- Types match schema
- Values within constraints
- i18n complete (all 3 languages)

### Step 5: Filter by Status

Determine which repositories to display:

```yaml
Default filter:
  - status: "active" → Display on website
  - status: "archived" → Optional (archive section only)
  - status: "draft" → Do not display publicly
  - status: "deprecated" → Do not display publicly

Canonical filter:
  - canonical: true → Highlight or mark as official
  - canonical: false → Display normally or label as experimental
```

### Step 6: Generate Multilingual Views

For each supported language (en, fr, ar):

```yaml
Display:
  - i18n.<lang>.title → Repository heading
  - i18n.<lang>.description → One-line description
  - layer → Layer designation
  - role → Functional role
  - repository → GitHub link
  - status → Operational status indicator
```

**Language selection**: Based on user preference or browser locale.

**Fallback**: If user language not supported, default to English (`en`).

---

## Display Guidelines

### Repository Listing

**Recommended display structure**:

```
Layer 0: Governance & Charter
  ├─ TRIZEL Core Governance (trizel-ai/trizel-core)
  │  Canonical governance and charter repository defining epistemic boundaries...
  │  [canonical] [active]

Layer 1: Algorithm Definition
  ├─ AUTO DZ ACT Algorithm (trizel-ai/Auto-dz-act)
  │  Canonical algorithm definition repository
  │  [canonical] [active]

Layer 2: Data & Observation
  ├─ 3I ATLAS Daily Data (abdelkader-omran/AUTO-DZ-ACT-3I-ATLAS-DAILY)
  │  Daily observational data repository for 3I ATLAS
  │  [active]
  ├─ TRIZEL Monitor (abdelkader-omran/trizel-monitor)
  │  Repository for monitoring and observational data collection
  │  [active]

... (continue for all layers)
```

**Visual hierarchy**:
- Group by layer
- List repositories within each layer
- Indicate canonical status visually
- Show operational status (active, archived, etc.)
- Provide GitHub links

**Sorting**:
- Primary: By layer (0-6)
- Secondary: Canonical first, then alphabetical

### Multilingual Support

**Language switching**:
- Provide language selector (English / Français / العربية)
- Preserve all other page state when switching languages
- Store language preference in browser

**RTL support**:
- Arabic (ar) requires right-to-left text direction
- Adjust layout accordingly for Arabic view
- Test thoroughly with Arabic text

### Metadata Display

**For each repository, optionally display**:

```yaml
Repository metadata:
  - GitHub link → repository field
  - Layer designation → layer field
  - Role → role field (can be human-readable, e.g., "Governance & Charter")
  - Status → status field (with visual indicator)
  - Canonical flag → canonical field (badge or icon)
```

**Provenance** (from registry_metadata):
```yaml
Registry information:
  - Registry version → registry_metadata.version
  - Last updated → registry_metadata.effective_date
  - Source → registry_metadata.repository
```

---

## Optional: Branch Information

If a repository includes `pending_branches` in the registry:

**Display guidelines**:
- Show branch information in collapsed/expandable section
- Only display for repositories with pending_branches defined
- Clearly label as "Pending Work" or "Development Branches"

**Example display**:

```
TRIZEL Core Governance (trizel-ai/trizel-core)
[canonical] [active]

  Pending Branches:
    ├─ copilot/add-trizel-registry-yaml [ready]
    │  Purpose: Add canonical project registry in YAML format
    ├─ feature/new-governance [draft]
    │  Purpose: Update governance policy for Layer 3
```

**Constraints**:
- Only show if `pending_branches` array is present and non-empty
- Display branch_name, purpose, and status
- Use status for visual indicator (draft = gray, ready = green, blocked = red)

---

## Validation and Error Handling

### Pre-Build Validation

Before deploying the website:

```yaml
Validation checklist:
  - [ ] Registry fetched successfully
  - [ ] Schema version compatible with website
  - [ ] YAML syntax valid
  - [ ] All required metadata present
  - [ ] No deprecated terms detected
  - [ ] All repositories have complete i18n (en, fr, ar)
  - [ ] Character limits respected (title ≤100, description ≤200)
  - [ ] No duplicate repositories
```

**If any check fails**: Halt build, log error, notify maintainers.

### Runtime Behavior

**The website must never**:
- Display repositories not in the registry
- Show partial or incomplete metadata
- Proceed with invalid registry data
- Silently skip validation errors
- Mix registry versions

**The website must always**:
- Validate registry before use
- Log registry version being used
- Fail explicitly on errors
- Provide clear error messages
- Maintain audit trail of ingestion

---

## Allowlist Enforcement

### Source Validation

```yaml
Approved source:
  repository: "trizel-ai/trizel-core"
  path: "docs/registry/TRIZEL_REGISTRY.yaml"
  schema_version: "1.0.0"
  publishable: true

Validation rules:
  - Source must be from trizel-ai/trizel-core
  - File path must be docs/registry/TRIZEL_REGISTRY.yaml
  - Schema version must match website compatibility
  - registry_metadata.publishable must be true
```

**Reject if**:
- Source is from different repository
- File path is different
- Schema version incompatible
- Publishable flag is false or missing

### Version Compatibility

**Current compatibility**:
- Website supports: `schema_version: "1.0.0"`
- Reject: Any other schema version (until website updated)

**For future versions**:
- Minor updates (1.1.0): Optional fields added, backwards compatible
- Major updates (2.0.0): Breaking changes, requires website update

**Handling version changes**:
1. Registry governance bumps schema version
2. Website must be updated before new version is merged
3. Linked PRs in both repositories
4. Test compatibility thoroughly
5. Deploy website first, then merge registry update

---

## Update Protocol

### When Registry Changes

**The website must**:
1. Detect registry update (via commit SHA or version change)
2. Fetch new registry version
3. Validate against schema
4. Re-run all validation checks
5. Rebuild website with new data
6. Deploy updated version

**Automated vs Manual**:
- Registry changes can trigger automated rebuild (CI/CD)
- Manual review recommended for major changes
- Test deployment in staging environment first

### Handling Removed Repositories

If a repository is removed from the registry:

```yaml
Process:
  1. Repository status changed to "deprecated" (one registry version)
  2. Website displays with "deprecated" indicator
  3. Repository removed from registry (next registry version)
  4. Website removes from display automatically
  5. Archive links preserved if applicable
```

**Do not**:
- Display removed repositories
- Cache old registry data indefinitely
- Assume repository still exists

---

## Security and Privacy

### Data Handling

**Registry contains only public metadata**:
- Repository names (public GitHub paths)
- Non-sensitive descriptions
- Layer assignments
- Operational status

**No sensitive data**:
- No credentials or secrets
- No personal information
- No internal documentation
- No private repository references

### Validation Security

**Protect against**:
- YAML injection attacks → Use safe YAML parser
- Path traversal → Validate file path explicitly
- Untrusted sources → Strict allowlist enforcement
- Schema poisoning → Pin schema version

---

## Compliance Requirements

### For Website Implementation

The website must:

- [ ] Implement allowlist-only validation
- [ ] Use fail-closed error handling
- [ ] Support all three languages (en, fr, ar)
- [ ] Respect character limits (title, description)
- [ ] Check for deprecated terminology
- [ ] Validate schema version compatibility
- [ ] Group repositories by layer
- [ ] Indicate canonical status visually
- [ ] Provide GitHub links for each repository
- [ ] Log registry version in use
- [ ] Maintain audit trail of ingestion
- [ ] Handle RTL text for Arabic
- [ ] Test thoroughly before deployment

### CI/CD Integration

**Recommended CI checks**:

```yaml
# .github/workflows/registry-validation.yml (in website repo)

steps:
  - Fetch TRIZEL_REGISTRY.yaml
  - Validate YAML syntax
  - Validate schema version
  - Check for deprecated terms
  - Verify i18n completeness
  - Lint character limits
  - Test multilingual rendering
  - Build website
  - Deploy to staging
  - Manual review
  - Deploy to production
```

---

## Troubleshooting

### Common Issues

**Issue**: Registry not found  
**Solution**: Check repository URL, file path, and branch reference

**Issue**: Schema validation failure  
**Solution**: Verify registry conforms to SCHEMA.md, check required fields

**Issue**: Deprecated terms detected  
**Solution**: Scan registry for forbidden terminology, remove immediately

**Issue**: Missing i18n translations  
**Solution**: Ensure all repositories have en, fr, ar entries

**Issue**: Character limit exceeded  
**Solution**: Trim title (≤100 chars) or description (≤200 chars)

**Issue**: Duplicate repositories  
**Solution**: Check for duplicate entries, remove duplicates

---

## Examples

### Example: Fetching and Parsing

```python
# Pseudocode for website integration

import yaml
import requests

# 1. Fetch registry
registry_url = "https://raw.githubusercontent.com/trizel-ai/trizel-core/main/docs/registry/TRIZEL_REGISTRY.yaml"
response = requests.get(registry_url)

if response.status_code != 200:
    raise Exception("Failed to fetch registry")

# 2. Parse YAML
registry = yaml.safe_load(response.text)

# 3. Validate schema version
if registry['registry_metadata']['schema_version'] != "1.0.0":
    raise Exception("Incompatible schema version")

# 4. Check publishable flag
if not registry['registry_metadata']['publishable']:
    raise Exception("Registry not marked as publishable")

# 5. Process repositories
for repo in registry['repositories']:
    if repo['status'] == 'active':
        # Extract multilingual data
        en_title = repo['i18n']['en']['title']
        en_desc = repo['i18n']['en']['description']
        
        # Display on website
        # ... (implementation-specific)
```

### Example: Multilingual Display

```html
<!-- Example HTML structure -->

<section class="layer-section" data-layer="0">
  <h2>Layer 0: Governance & Charter</h2>
  
  <article class="repository" data-canonical="true" data-status="active">
    <h3>
      <span class="title" lang="en">TRIZEL Core Governance</span>
      <span class="badges">
        <span class="badge canonical">Canonical</span>
        <span class="badge active">Active</span>
      </span>
    </h3>
    
    <p class="description" lang="en">
      Canonical governance and charter repository defining epistemic boundaries and structural principles
    </p>
    
    <a href="https://github.com/trizel-ai/trizel-core" class="repo-link">
      trizel-ai/trizel-core ↗
    </a>
  </article>
</section>
```

---

## Related Documents

- `TRIZEL_REGISTRY.yaml` — The canonical registry
- `SCHEMA.md` — Schema definition and constraints (in this directory)
- `../../PUBLICATION_POLICY.md` — Overall publication policy
- `../../ROLE.md` — Layer 0 repository role
- `../../DEPRECATED_TERMS.md` — Forbidden terminology

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-12 | Initial README for website integration |

---

## Questions or Issues

For questions about registry consumption or integration:

1. Review this document and SCHEMA.md
2. Check PUBLICATION_POLICY.md for overall guidelines
3. Open an issue in trizel-ai/trizel-core
4. Reference Layer 0 governance in issue description

**Do not**:
- Modify registry without governance approval
- Bypass validation rules
- Ingest from non-approved sources
- Proceed with invalid data
