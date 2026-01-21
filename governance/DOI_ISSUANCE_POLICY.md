# DOI ISSUANCE POLICY

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance  
**Policy Version**: 1.0.0  
**Effective Date**: 2026-01-21  
**Status**: Active

---

## Purpose

This document establishes the formal, auditable, fail-closed governance framework for Digital Object Identifier (DOI) issuance within the TRIZEL scientific ecosystem.

**Core Principle**: DOI issuance is a governed publication act, not a technical by-product.

---

## Scope

This policy governs:

1. **DOI issuance** for all TRIZEL scientific outputs
2. **Review and approval** processes for DOI requests
3. **Relationship with external archives** (Zenodo, etc.)
4. **Metadata requirements** for DOI-eligible artifacts
5. **Rejection criteria** for DOI requests

This policy does **not** govern:

- Scientific methodology (Layer-1)
- Presentation or display (Layer-2)
- Internal research documentation
- Non-scientific artifacts

---

## Fundamental Principles

### 1. DOI ≠ Result

A DOI is a **governance act** that certifies:
- Immutability of the artifact
- Completion of review
- Authorization for public citation
- Compliance with TRIZEL standards

A DOI is **not**:
- A validation of scientific correctness
- An endorsement of theoretical claims
- A certification of interpretive authority
- An automatic consequence of completing analysis

### 2. No Automatic DOI Issuance

**Prohibition**: No system, workflow, or automation may mint DOIs without explicit governance approval.

Every DOI requires:
- Human review
- Governance authorization
- Documented approval record
- Compliance verification

### 3. Freeze-First Rule

Only immutable, hash-verified snapshots may be considered for DOI issuance.

**Requirement**: Before DOI review begins, the artifact must be:
- Frozen (no further modifications permitted)
- Hash-verified (SHA-256 or stronger)
- Timestamped (ISO 8601 format)
- Manifested (complete file inventory)

### 4. Layer Separation

DOI issuance respects TRIZEL layer boundaries:

- **Layer-1**: Produces scientific outputs (observation, analysis)
- **Layer-0**: Authorizes publication (governance, review, DOI issuance)
- **Layer-2**: Displays references only (no DOI minting authority)

---

## Publishable Scientific Snapshot — Qualification Criteria

### What Qualifies

A scientific snapshot is eligible for DOI consideration if it meets **all** of the following:

#### 1. Immutability
- Artifact is frozen and locked against modification
- All files are hash-verified (SHA-256 minimum)
- Timestamp is permanently recorded
- No post-freeze edits permitted

#### 2. Completeness
- All required metadata fields are present
- All referenced methods are documented
- All dependencies are declared
- All provenance information is traceable

#### 3. Compliance
- No deprecated terminology
- No prohibited content types
- No Layer-0 boundary violations
- No governance rule violations

#### 4. Scientific Validity
- Methodology is documented
- Data provenance is clear
- Scope is explicitly defined
- Limitations are stated

#### 5. Authorization
- Scientific authorization has been granted (see `governance/FREEZE.md`)
- Publication is not prohibited by governance freeze
- Approval authority has been designated
- Review process has been completed

### What Does Not Qualify

The following are **explicitly disqualified** from DOI issuance:

- **Work-in-progress** artifacts
- **Preliminary** or draft results
- **Unreviewed** outputs
- **Modified** snapshots (post-freeze edits)
- **Incomplete** metadata
- **Deprecated** terminology usage
- **Unapproved** method references
- **Layer-2** presentation content
- **Interpretive** claims without evidence
- **Automated** pipeline outputs (without review)

---

## Mandatory Metadata Requirements

### Required Fields

All DOI-eligible artifacts must include the following metadata:

#### Core Identification
```yaml
title: [Full descriptive title]
version: [Semantic version or identifier]
date: [ISO 8601 timestamp]
doi: [Reserved — assigned after approval]
```

#### Authorship
```yaml
authors:
  - name: [Full name]
    affiliation: [Optional]
    orcid: [Optional]
  # Additional authors as needed
```

#### Scientific Context
```yaml
method_reference: [Canonical method identifier]
method_version: [Method version used]
scope: [Explicit scope statement]
limitations: [Known limitations]
```

#### Provenance
```yaml
repository: [Source repository]
branch: [Source branch]
commit: [Git commit SHA]
snapshot_hash: [SHA-256 of complete snapshot]
snapshot_date: [ISO 8601 timestamp]
```

#### Governance
```yaml
layer: [Layer-1 or Layer-0]
approved_by: [Governance authority]
approval_date: [ISO 8601 timestamp]
approval_reference: [PR number or governance record]
```

### Optional Fields

The following fields are recommended but not required:

- `keywords`: List of descriptive keywords
- `abstract`: Brief summary (if applicable)
- `license`: License identifier (default: as per repository)
- `funding`: Funding sources (if applicable)
- `related_dois`: Related publications

### Metadata Validation

Before DOI issuance:
1. **Schema check**: Verify all required fields present
2. **Format check**: Verify ISO 8601 dates, valid SHAs, etc.
3. **Completeness check**: Verify no placeholders (TBD, TODO, etc.)
4. **Consistency check**: Verify metadata matches snapshot content

---

## Explicit Prohibitions

### Prohibited: Automatic DOI Issuance

**No system may**:
- Mint DOIs upon completion of analysis
- Trigger DOI requests from workflow events
- Generate DOI metadata automatically
- Bypass human review requirements
- Override governance approval process

**Enforcement**: All DOI issuance must be:
- Initiated by explicit governance action
- Reviewed by designated authority
- Approved through documented process
- Logged in governance records

### Prohibited: Post-Freeze Modification

Once a snapshot is submitted for DOI review:

**No modifications permitted** to:
- Artifact files
- Metadata content
- Hash manifests
- Timestamps
- Provenance records

**Exception**: Only governance metadata (approval status, DOI assignment) may be updated.

**Violation consequence**: DOI request is rejected; new snapshot required.

### Prohibited: Retroactive DOI Assignment

**No DOIs may be assigned** to:
- Historical artifacts not meeting current standards
- Previously published content without proper review
- Artifacts predating this governance policy (unless explicitly re-reviewed)

### Prohibited: DOI for Non-Scientific Content

**No DOIs may be issued** for:
- Governance documents (this repository)
- Presentation materials (Layer-2)
- Software tools (unless scientifically validated)
- Documentation (unless part of scientific record)

---

## Review Authority and Approval Process

### Designated Authority

DOI issuance approval authority is vested in:

**Primary Authority**: TRIZEL Governance Committee (if established)  
**Interim Authority**: Repository maintainers with Layer-0 governance role

### Approval Requirements

To approve a DOI request, the authority must verify:

1. **Snapshot immutability**: Hash verification passed
2. **Metadata completeness**: All required fields present
3. **Governance compliance**: No policy violations
4. **Scientific validity**: Methodology documented, scope clear
5. **Authorization status**: Scientific publication authorized
6. **Review completion**: All checks passed

### Approval Documentation

Approved DOI requests must be recorded in:

**Location**: `governance/APPROVAL.md`

**Entry format**:
```markdown
## DOI Approval: [Snapshot Identifier]

- **Date**: [ISO 8601 timestamp]
- **Authority**: [Approver name/role]
- **Snapshot**: [Snapshot identifier]
- **DOI**: [Assigned DOI]
- **PR Reference**: [If applicable]
- **Verification**: [Hash, metadata checks passed]
```

---

## Rejection Conditions

A DOI request **must be rejected** if any of the following apply:

### Automatic Rejections

1. **Missing required metadata**: Any required field absent or incomplete
2. **Hash verification failure**: Snapshot integrity compromised
3. **Post-freeze modification**: Artifact changed after submission
4. **Governance violation**: Deprecated terms, prohibited content, etc.
5. **Scientific authorization absent**: Publication not authorized
6. **Incomplete review**: Review process not completed

### Discretionary Rejections

The approval authority may reject if:

1. **Scope unclear**: Purpose or boundaries not well-defined
2. **Methodology inadequate**: Method documentation insufficient
3. **Limitations not stated**: Known issues not disclosed
4. **Duplicate submission**: Same content already has DOI
5. **Quality concerns**: Scientific rigor concerns

### Rejection Process

Rejected requests must be documented:

**Location**: `governance/APPROVAL.md` (rejection section)

**Entry format**:
```markdown
## DOI Rejection: [Snapshot Identifier]

- **Date**: [ISO 8601 timestamp]
- **Authority**: [Reviewer name/role]
- **Snapshot**: [Snapshot identifier]
- **Reason**: [Specific rejection reason]
- **Remediation**: [Required actions for resubmission]
```

**Resubmission**: After rejection, a corrected snapshot may be resubmitted (as new request).

---

## Relationship with Zenodo

### Manual, Curated Releases Only

TRIZEL's relationship with Zenodo (or similar archives) is governed by:

**Principle**: Zenodo is a **publication destination**, not an automation target.

### Zenodo Usage Rules

1. **Manual submission only**: No automated API usage
2. **Governance approval required**: Every upload approved first
3. **Immutable snapshots only**: Only frozen, hash-verified artifacts
4. **Metadata compliance**: Zenodo metadata matches TRIZEL metadata
5. **Curated releases**: Each upload is deliberate and documented

### Zenodo Workflow

**Approved workflow**:
```
1. Snapshot created and frozen (Layer-1)
2. DOI request submitted (to Layer-0)
3. Governance review completed
4. Approval granted and documented
5. Manual Zenodo upload (by authorized person)
6. DOI assigned by Zenodo
7. DOI recorded in TRIZEL governance
8. Reference may appear in Layer-2 (static only)
```

**Any step skipped = DOI not issued**

### Prohibited Zenodo Patterns

**Never**:
- Use Zenodo GitHub integration for automatic releases
- Trigger Zenodo uploads from CI/CD workflows
- Generate Zenodo metadata programmatically
- Bypass governance review via direct Zenodo submission
- Upload non-approved snapshots

---

## Fail-Closed Enforcement

### Default State: DOI Issuance Forbidden

**Unless all requirements are met, DOI issuance is prohibited.**

This policy operates in **fail-closed mode**:

- **Incomplete metadata**: NO DOI
- **Missing approval**: NO DOI
- **Failed hash verification**: NO DOI
- **Governance violation**: NO DOI
- **Unclear authority**: NO DOI
- **Ambiguous rules**: NO DOI

### No Exceptions

There are **no exceptions** to the fail-closed rule.

- No emergency DOI issuance
- No provisional DOI assignment
- No "pending review" DOIs
- No grandfather clauses

### Enforcement Mechanism

This policy is enforced by:

1. **Human review**: No automated bypass
2. **Documented approval**: All decisions logged
3. **Governance audit**: Regular compliance checks
4. **Rejection by default**: Unless explicitly approved

---

## Policy Governance

### Policy Updates

Changes to this DOI issuance policy require:

1. **PR to `trizel-core`**: Modify this document
2. **Governance review**: Same approval process as DOI requests
3. **Version increment**: Update policy version number
4. **Documentation**: Record change rationale
5. **Approval entry**: Log in `governance/APPROVAL.md`

### Breaking Changes

If policy changes fundamentally alter DOI issuance rules:

1. **Deprecation notice**: Warn of upcoming changes
2. **Transition period**: Allow adaptation time
3. **Clear documentation**: Explain new requirements
4. **Migration path**: Guide for pending requests

---

## Compliance Checklist

Before DOI issuance, verify:

- [ ] Snapshot is immutable and hash-verified
- [ ] All required metadata fields present and valid
- [ ] No post-freeze modifications
- [ ] Governance compliance verified (no deprecated terms, etc.)
- [ ] Scientific authorization granted
- [ ] Review process completed
- [ ] Approval authority designated
- [ ] Approval documented in governance records
- [ ] Zenodo submission manual and curated
- [ ] DOI recorded in TRIZEL governance

**All checks must pass. No exceptions.**

---

## Related Policies

- `governance/FREEZE.md` — Scientific authorization status
- `governance/SNAPSHOT_CONTRACT.md` — Snapshot immutability requirements
- `governance/METHOD_REFERENCE_RULES.md` — Method citation rules
- `PUBLICATION_POLICY.md` — Website publication rules
- `governance/APPROVAL.md` — Governance approval log

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-21 | Initial DOI Issuance Policy (Phase-F) |

---

**Effective Immediately**  
**Authority**: TRIZEL Layer-0 Governance  
**Status**: Active
