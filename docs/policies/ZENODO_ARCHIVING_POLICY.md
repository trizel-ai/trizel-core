# ZENODO_ARCHIVING_POLICY.md

## Zenodo Archiving Policy

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Policy Version**: 1.0.0  
**Last Updated**: 2026-01-17

---

## Purpose

This document defines the formal policy for archiving TRIZEL repositories on Zenodo and minting DOIs (Digital Object Identifiers).

The purpose of this policy is to:

1. **Prevent misuse** of DOI-based publication for internal governance milestones
2. **Ensure legitimacy** of archived content with permanent identifiers
3. **Maintain scientific integrity** by restricting DOI usage to substantive releases
4. **Preserve provenance** through proper archival of significant versions
5. **Prevent citation inflation** through inappropriate DOI minting

---

## Core Principle

**DOIs are permanent scholarly identifiers, not internal milestone markers.**

**Zenodo is NOT to be used for internal governance milestones.**

Internal releases (e.g., GATE-1, GATE-2, enforcement steps, CI validation) are **traceability-only** and **NOT scientific publications**.

Zenodo archiving and DOI minting are reserved **exclusively** for:
- **Scientific theories**
- **Research frameworks**
- **Datasets**
- **Models**
- **Peer-review-ready AI or astrophysics artifacts**

DOIs must **never** be used for:
- Internal governance milestones (Gates, GATE-1, GATE-2, etc.)
- Enforcement steps or CI validation markers
- Internal development milestones
- Draft or work-in-progress content
- Temporary governance states
- CI/CD pipeline triggers
- Version control housekeeping
- Internal tracking or coordination

---

## Scope of Zenodo Archiving

### What Qualifies for DOI Minting

The following types of content are **eligible** for Zenodo archiving and DOI assignment:

#### 1. Major Governance Releases
- **Description**: Finalized, stable versions of Layer-0 governance framework
- **Minimum Requirements**:
  - Complete governance documentation
  - Passed all GATE 1 enforcement checks
  - Reviewed and approved by governance authority
  - Tagged as a semantic version release (e.g., v1.0.0, v2.0.0)
  - Includes comprehensive metadata (authors, license, description)
- **Example**: `trizel-core v1.0.0` — Complete epistemic framework and governance rules

#### 2. Scientific Framework Releases
- **Description**: Stable versions of methodological frameworks suitable for citation
- **Minimum Requirements**:
  - Complete methodology documentation
  - Validation of framework completeness
  - Approval for public scholarly reference
  - Semantic version tag
  - Full metadata and citation information
- **Example**: TRIZEL Epistemic Pipeline v1.0.0 with formal specification

#### 3. Reproducible Research Artifacts
- **Description**: Published datasets, analysis code, or inference models with scholarly value
- **Minimum Requirements**:
  - Complete documentation and reproducibility instructions
  - Validation and testing completed
  - Approved for public scholarly use
  - Includes data/code availability statements
  - Full provenance and metadata
- **Example**: Validated analysis pipeline with documented methodology

#### 4. Public Interface Releases
- **Description**: Stable versions of public-facing visualization or interface tools
- **Minimum Requirements**:
  - Feature-complete and validated
  - Public documentation available
  - Approved for scholarly reference
  - Semantic version tag
  - Usage and citation guidance
- **Example**: `trizel-visual v1.0.0` with complete visualization framework

### What Does NOT Qualify for DOI Minting

The following are **explicitly excluded** from Zenodo archiving:

#### 1. Internal Governance Milestones
- ❌ GATE checkpoints (GATE 1, GATE 2, etc.)
- ❌ Internal approval states
- ❌ Workflow completion markers
- ❌ Development phase transitions
- ❌ CI/CD success indicators

**Rationale**: These are internal coordination mechanisms, not substantive scholarly artifacts.

#### 2. Draft or Incomplete Content
- ❌ Work-in-progress documents
- ❌ Draft governance policies
- ❌ Partial implementations
- ❌ Pre-review content
- ❌ Temporary documentation

**Rationale**: DOIs represent permanent records; drafts are inherently transient.

#### 3. Patch and Minor Releases
- ❌ Bug fixes (v1.0.1, v1.0.2)
- ❌ Documentation corrections
- ❌ Minor updates without substantive changes
- ❌ Formatting or style changes
- ❌ Dependency updates only

**Rationale**: Reserve DOIs for significant intellectual contributions, not maintenance.

#### 4. Development Infrastructure
- ❌ CI/CD workflow definitions
- ❌ Build scripts or automation
- ❌ Testing infrastructure
- ❌ Development tools
- ❌ Repository metadata files

**Rationale**: Infrastructure is supportive, not primary scholarly content.

#### 5. Derivative or Redundant Content
- ❌ Content duplicated from other archived versions
- ❌ Reformatted existing content without new substance
- ❌ Aggregations of already-archived materials
- ❌ Mirror repositories

**Rationale**: Avoid DOI proliferation for the same intellectual content.

---

## Approval Process for Zenodo Archiving

### Pre-Archiving Requirements

Before requesting Zenodo archiving and DOI minting, the following must be satisfied:

1. **Content Completion**
   - All planned content finalized
   - All documentation complete
   - All validation checks passed

2. **Governance Approval**
   - Reviewed by governance authority
   - Approval recorded in `governance/APPROVAL.md`
   - Breaking changes documented
   - Version number assigned per semantic versioning

3. **Metadata Completeness**
   - Authors and contributors identified
   - License specified
   - Description and keywords provided
   - Repository and provenance information complete
   - Related identifiers listed (if applicable)

4. **Quality Validation**
   - All GATE enforcement checks passed
   - No deprecated terms detected
   - Schema validation successful
   - Immutable references verified
   - Build and test validation complete (if applicable)

5. **Public Readiness**
   - Content suitable for public scholarly reference
   - No sensitive or confidential information
   - Complies with publication policies
   - Citation guidance provided

### Archiving Request Protocol

To request Zenodo archiving:

1. **Create Issue**: Open issue in repository with title "Request Zenodo Archiving: [Repository] [Version]"

2. **Provide Justification**:
   - Explain why this version warrants DOI assignment
   - Document substantive changes from previous archived version
   - Confirm all pre-archiving requirements met
   - Provide proposed metadata (authors, description, keywords)

3. **Governance Review**:
   - Governance authority reviews request
   - Validates eligibility against this policy
   - Approves or rejects with documented rationale
   - Records decision in governance log

4. **Execute Archiving**:
   - Create Git release tag (e.g., v1.0.0)
   - Zenodo webhook automatically creates deposit
   - Zenodo mints DOI
   - Update repository metadata with DOI
   - Close archiving request issue

5. **Post-Archiving**:
   - Verify DOI resolves correctly
   - Update citation files (CITATION.cff)
   - Document DOI in README or relevant location
   - Announce release with DOI reference

---

## Version Control and DOI Assignment

### Semantic Versioning Rules for DOI

DOI minting is governed by semantic versioning principles:

- **Major Releases (X.0.0)**: Always eligible for DOI if substantive
- **Minor Releases (X.Y.0)**: Eligible for DOI if significant additions
- **Patch Releases (X.Y.Z)**: Generally not eligible for DOI

### Examples of DOI-Eligible Versions

✅ **v1.0.0**: Initial release of governance framework  
✅ **v2.0.0**: Major revision with breaking changes  
✅ **v1.5.0**: Significant methodological additions  
✅ **v1.0.0-beta**: Pre-release for substantive testing (with clear pre-release status)

### Examples of DOI-Ineligible Versions

❌ **v1.0.1**: Bug fix only  
❌ **v1.0.2**: Documentation typo corrections  
❌ **v1.0.0-dev**: Development snapshot  
❌ **v0.1.0**: Pre-release governance draft  
❌ **GATE1-complete**: Internal milestone marker

---

## Zenodo Metadata Requirements

All Zenodo deposits must include complete metadata:

### Required Fields

```json
{
  "title": "Full title of repository and version",
  "creators": [
    {
      "name": "Author Name",
      "affiliation": "Institution",
      "orcid": "0000-0000-0000-0000"
    }
  ],
  "description": "Comprehensive description of content and purpose",
  "license": "License identifier (e.g., MIT, CC-BY-4.0)",
  "upload_type": "software | dataset | publication | other",
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "version": "Semantic version number",
  "related_identifiers": [
    {
      "identifier": "https://github.com/trizel-ai/trizel-core",
      "relation": "isSupplementTo"
    }
  ],
  "language": "eng"
}
```

### Metadata Validation

Before Zenodo deposit:
- Verify all required fields populated
- Validate ORCID identifiers
- Confirm license compatibility
- Check description adequacy
- Ensure keywords are appropriate
- Validate version string format

---

## Decision Matrix

The following table defines which artifact types qualify for GitHub releases, Zenodo archiving, DOI minting, and citation:

| Artifact Type | GitHub Release | Zenodo | DOI | Citable |
|--------------|----------------|--------|-----|---------|
| **Scientific Theory** | Yes | Yes | Yes | Yes |
| **Research Framework** | Yes | Yes | Yes | Yes |
| **Dataset (validated)** | Yes | Yes | Yes | Yes |
| **Model (validated)** | Yes | Yes | Yes | Yes |
| **Peer-review-ready AI artifact** | Yes | Yes | Yes | Yes |
| **Peer-review-ready astrophysics artifact** | Yes | Yes | Yes | Yes |
| **Major Governance Release (v1.0.0+)** | Yes | No* | No* | No* |
| **Internal Governance Milestone (GATE-1, GATE-2)** | No | **NO** | **NO** | **NO** |
| **Enforcement Step** | No | **NO** | **NO** | **NO** |
| **CI Validation Marker** | No | **NO** | **NO** | **NO** |
| **Bug Fix (patch release)** | Yes | No | No | No |
| **Documentation Update** | Yes | No | No | No |
| **Development Infrastructure** | No | No | No | No |

**Note**: *Governance releases may receive GitHub releases for version tracking but are **not** scientific publications and should **not** be archived on Zenodo or assigned DOIs unless they constitute a formal research framework eligible under the scientific criteria.

**Canonical governance reference**: TRIZEL Governance v1.0.0

---

## Treatment of Existing Internal Governance Archives

Any internal governance record that has already been archived on Zenodo **MUST**:

1. **Be labeled**: "NOT A SCIENTIFIC PUBLICATION"
2. **Include**: "DO NOT CITE" in the description
3. **Reference**: The canonical scientific baseline where applicable
4. **Clarify**: The record is for traceability purposes only

The **canonical governance reference** remains:
- **TRIZEL Governance v1.0.0**

All future references to governance should cite the canonical version, not intermediate internal milestones.

---

## Prohibited Uses of Zenodo DOI

The following uses of Zenodo archiving are **explicitly prohibited**:

### ❌ Internal Milestone Tracking
**Example**: Archiving "GATE 1 Complete" as a DOI-bearing release  
**Why Prohibited**: Internal governance milestones are not substantive scholarly artifacts  
**Alternative**: Use Git tags, GitHub milestones, or project boards

### ❌ CI/CD Pipeline Integration
**Example**: Automatic DOI minting on every commit or PR merge  
**Why Prohibited**: Creates DOI proliferation without scholarly value  
**Alternative**: Use standard CI/CD status badges and release notes

### ❌ Development Progress Markers
**Example**: "Feature X implemented" or "Refactoring complete" with DOI  
**Why Prohibited**: Development progress is not equivalent to scholarly publication  
**Alternative**: Use Git tags, commit messages, and issue tracking

### ❌ Redundant Versioning
**Example**: Archiving v1.0.1, v1.0.2, v1.0.3 individually when changes are trivial  
**Why Prohibited**: Unnecessary DOI proliferation dilutes scholarly record  
**Alternative**: Consolidate patches; archive only when substantive changes accumulated

### ❌ Personal Credit Accumulation
**Example**: Creating multiple minor releases to increase publication count  
**Why Prohibited**: Violates scholarly integrity and citation ethics  
**Alternative**: Focus on substantive contributions worthy of citation

---

## Enforcement Note

**This policy is binding for all TRIZEL repositories.**

Any violations of this Zenodo Archiving Policy require explicit governance approval documented in:
- `governance/APPROVAL.md`

No repository maintainer may authorize Zenodo archiving or DOI minting that conflicts with this policy without formal governance review and documented exception approval.

---

## Enforcement and Compliance

### Automated Prevention

Technical measures to prevent policy violations:

1. **Zenodo Integration Control**:
   - Webhook disabled by default
   - Manual approval required for each archiving
   - No automatic DOI minting on Git tags

2. **Release Tag Protection**:
   - Semantic version tags (v*.*.*) protected
   - Require governance approval before creation
   - Tags must pass all GATE checks

3. **Metadata Validation**:
   - Pre-deposit validation of .zenodo.json
   - Required fields enforcement
   - Description minimum length check
   - Version string format validation

### Manual Review

All Zenodo archiving requests subject to:

1. **Governance Authority Review**:
   - Validates eligibility against this policy
   - Confirms substantive nature of release
   - Approves or rejects with rationale
   - Records decision in governance log

2. **Pre-Archiving Checklist**:
   - [ ] Content complete and validated
   - [ ] Governance approval obtained
   - [ ] Metadata complete and accurate
   - [ ] Not an internal milestone
   - [ ] Not a patch or trivial update
   - [ ] Not redundant with existing DOI
   - [ ] Public scholarly value confirmed

### Violation Remediation

If inappropriate DOI minting occurs:

1. **Immediate Response**:
   - Document violation in governance log
   - Create incident report
   - Notify Zenodo administrators if necessary

2. **Corrective Action**:
   - Update deposit metadata if possible (add warning)
   - Document proper use in subsequent releases
   - Strengthen approval process to prevent recurrence

3. **Policy Update**:
   - Review policy for gaps
   - Update enforcement mechanisms
   - Communicate policy clarifications

**Note**: DOIs are permanent and cannot be deleted, only marked as deprecated or superseded.

---

## Related Policies

This Zenodo Archiving Policy must be read in conjunction with:

- **PUBLICATION_POLICY.md** — Website publication rules
- **OUTPUT_CONTRACT.md** — Export contract specifications
- **GOVERNANCE_ENFORCEMENT.md** — GATE 1 enforcement framework
- **docs/metadata/README.md** — Metadata placement and management
- **ROLE.md** — Layer 0 scope and boundaries

---

## Governance of This Policy

### Policy Updates

Changes to this Zenodo Archiving Policy require:

1. **PR in `trizel-core`**: Update this file
2. **Version bump**: Increment policy version
3. **Governance approval**: Documented in `governance/APPROVAL.md`
4. **Communication**: Notify all repository maintainers
5. **Implementation**: Update Zenodo integration configuration

### Policy Review Cadence

This policy will be reviewed:
- Annually as part of governance review
- After any DOI minting incident or issue
- When Zenodo platform changes affect integration
- When TRIZEL repository structure changes

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-17 | Initial Zenodo Archiving Policy to prevent DOI misuse for internal governance milestones |

---

## Contact and Questions

For questions about Zenodo archiving or DOI minting:

1. **Review this policy** thoroughly
2. **Check related policies** listed above
3. **Open an issue** in `trizel-ai/trizel-core` with tag "zenodo-policy"
4. **Request governance review** for archiving approval

---

**Authority**: This is part of the Layer-0 governance framework.  
**Enforcement**: Manual approval required for all Zenodo archiving.  
**Compliance**: Mandatory for all TRIZEL repositories using Zenodo integration.
