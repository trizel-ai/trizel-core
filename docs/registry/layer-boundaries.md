# Layer 0 vs Layer 6 Boundary Definition

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Document Version**: 1.0.0  
**Last Updated**: 2026-01-12

---

## Purpose

This document defines the explicit boundary between Layer 0 (Governance & Charter) and Layer 6 (Publication & Website), specifying what each layer is allowed and forbidden to do.

---

## Layer 0: Governance & Charter

**Repository Example**: `trizel-ai/trizel-core`

### Single-Sentence Role

Layer 0 is the canonical governance and charter authority that defines epistemic boundaries, layer separation rules, and structural principles for the entire TRIZEL ecosystem, containing no data, execution logic, or analytical content.

### Allowed in Layer 0

Layer 0 repositories are authorized to contain:

- **Governance documents**: Rules, boundaries, principles, standards
- **Role registry**: Classification of all TRIZEL repositories (e.g., `TRIZEL_REGISTRY.yaml`)
- **Publication policies**: What can be published and how
- **Interface specifications**: Contracts between layers
- **Allowlist definitions**: Approved sources for downstream consumption
- **Metadata schemas**: Version, provenance, citation structures
- **Documentation**: Non-interpretive descriptions of system structure

### Forbidden in Layer 0

Layer 0 repositories must **never** contain:

- Scientific data or observational records
- Executable algorithms or computational code
- Analysis outputs or statistical results
- Inference models or predictions
- Interpretive claims or theoretical conclusions
- Automated workflows or build scripts
- Theory definitions or validation claims
- Content belonging to other layers (1-6)
- **Deprecated terminology**: STOE, V12-V22 version labels, versioned system labels

### Algorithm Name Standard

Layer 0 documents must use **only**:
- **"AUTO DZ ACT"** (exact spelling, no variants)

**Never use**:
- "STOE"
- "AUTO DZ ACT system"
- "AUTO DZ ACT v1"
- Any versioned labels

---

## Layer 6: Publication & Website

**Repository Example**: `abdelkader-omran/trizel-AI`

### Single-Sentence Role

Layer 6 is responsible for non-interpretive publication and visualization of allowlisted TRIZEL governance and metadata through a website or public interface, displaying only approved content with strict fail-closed validation.

### Allowed in Layer 6

Layer 6 repositories are authorized to contain:

- **Website code**: HTML, CSS, JavaScript, framework code (React, Vue, etc.)
- **Build scripts**: Tooling to fetch, validate, and render approved content
- **Allowlist-only ingestion**: Fetch and display content from explicitly approved sources
- **Non-interpretive visualization**: Display of structure, provenance, status, and metadata
- **Multilingual UI**: Interface supporting en/fr/ar languages
- **Static rendering**: Convert approved governance artifacts to web pages
- **Link generation**: Links to external governance documents and repositories
- **Provenance display**: Version, date, source information from allowlisted artifacts
- **Status indicators**: Visual display of repository state (active, archived, etc.)
- **Navigation components**: Menus, search, filters for browsing content
- **Responsive design**: Mobile-friendly layouts and interactions

### Forbidden in Layer 6

Layer 6 repositories must **never** contain:

- **Raw data ingestion**: Scientific datasets, observational records, measurement data
- **Data analysis**: Computational analysis, statistical processing, inference execution
- **Interpretive claims**: Analytical conclusions, theoretical assertions, scientific claims
- **Auto-discovery**: Automatic scanning of GitHub organizations or repositories
- **Non-approved sources**: Content from repositories not in the allowlist
- **Modified governance text**: Altered or paraphrased governance documents
- **Cross-layer content mixing**: Combining data, analysis, and visualization layers
- **Execution of scientific logic**: Running algorithms, models, or computational workflows
- **Theoretical content creation**: Generating interpretations or conclusions
- **Deprecated terminology**: STOE, V12-V22 version labels, versioned system labels

### Publication Rules for Layer 6

**MUST follow**:
1. **Allowlist-only ingestion**: Only consume content from approved sources
2. **Fail-closed validation**: Halt build if any validation fails
3. **Non-interpretive display**: Present facts only, no analysis or interpretation
4. **Schema validation**: Verify all ingested content matches expected schema
5. **Deprecated terms check**: Reject content containing forbidden terminology
6. **Provenance tracking**: Display source, version, and date for all content
7. **Multilingual support**: Provide EN/FR/AR translations for all displayed text

**MUST NOT**:
1. Silently skip invalid content
2. Display partial or unvalidated data
3. Guess or infer missing information
4. Mix content from different schema versions
5. Add interpretive commentary to governance text
6. Embed governance documents with modifications
7. Proceed with build when validation errors occur

---

## Boundary Enforcement

### Layer 0 → Layer 6 Interface

**What Layer 0 provides to Layer 6**:
- Canonical registry (`TRIZEL_REGISTRY.yaml`)
- Schema definitions (`SCHEMA.md`)
- Publication policies (`PUBLICATION_POLICY.md`)
- Consumption guidelines (`README.md`, `website-consumption.md`)
- Allowlist specifications
- Version and provenance metadata

**What Layer 6 must do**:
- Fetch registry from approved Layer 0 source
- Validate schema version compatibility
- Check for deprecated terminology
- Display content non-interpretively
- Maintain audit trail of ingestion
- Fail build if validation errors occur

### No Reverse Dependencies

**Critical rule**: Layer 0 must **never** depend on Layer 6.

- Layer 0 cannot import website code
- Layer 0 cannot execute website build processes
- Layer 0 cannot validate website output
- Layer 0 only defines **rules** that Layer 6 must follow

---

## Validation Checklist

### For Layer 0 Content

Before merging changes to Layer 0:

- [ ] Contains only governance, documentation, or metadata
- [ ] No executable code, scripts, or workflows
- [ ] No data, analysis results, or scientific content
- [ ] No deprecated terminology (STOE, V12-V22, etc.)
- [ ] Algorithm name is "AUTO DZ ACT" only (if mentioned)
- [ ] Documentation is non-interpretive
- [ ] All schemas are versioned
- [ ] Provenance metadata is complete

### For Layer 6 Content

Before deploying Layer 6 website:

- [ ] All sources are in approved allowlist
- [ ] Schema version matches Layer 0 compatibility
- [ ] No deprecated terms in displayed content
- [ ] All validations pass (fail-closed behavior)
- [ ] Multilingual support complete (en/fr/ar)
- [ ] Provenance displayed for all content
- [ ] No interpretive text added
- [ ] No raw data or analysis results displayed
- [ ] Build fails explicitly on errors
- [ ] Audit trail logged

---

## Common Boundary Violations (FORBIDDEN)

### Examples of What NOT to Do

**❌ Layer 0 violation**: Adding a build script to fetch external data
- **Why forbidden**: Layer 0 cannot contain executable automation

**❌ Layer 0 violation**: Embedding website HTML in governance docs
- **Why forbidden**: Layer 0 cannot contain Layer 6 content

**❌ Layer 6 violation**: Auto-discovering repositories from GitHub API
- **Why forbidden**: Layer 6 must use allowlist only, no auto-discovery

**❌ Layer 6 violation**: Adding interpretive commentary to governance text
- **Why forbidden**: Layer 6 must display content non-interpretively

**❌ Layer 6 violation**: Displaying raw scientific data
- **Why forbidden**: Layer 6 cannot ingest or display Layer 2-3 content

**❌ Cross-layer violation**: Layer 6 fetching data from Layer 2 directly
- **Why forbidden**: Layers must not skip intermediate boundaries

---

## Terminology Standards

### Required Terminology

**Algorithm name**: "AUTO DZ ACT" (exact spelling)

**Layer names**:
- Layer 0: Governance & Charter
- Layer 1: Algorithm Definition
- Layer 2: Data & Observation
- Layer 3: Analysis & Inference
- Layer 4: Evaluation & Gateway
- Layer 5: Reserved
- Layer 6: Publication & Website

### Forbidden Terminology

**Never use**:
- "STOE"
- "V12" through "V22" (any versioned system labels)
- "based on theory X"
- "evolved from Y"
- "supersedes Z"
- Theoretical lineage references
- Interpretive or analytical claims

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-12 | Initial layer boundary definition |

---

## Related Documents

- `TRIZEL_REGISTRY.yaml` — Canonical repository registry
- `SCHEMA.md` — Registry schema definition
- `website-consumption.md` — Layer 6 consumption guidelines
- `../../ROLE.md` — Layer 0 repository role
- `../../PUBLICATION_POLICY.md` — Publication rules
- `../../DEPRECATED_TERMS.md` — Forbidden terminology
