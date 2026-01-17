# ZENODO_READY_CHECKLIST.md

## Zenodo Readiness Checklist

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Checklist Version**: 1.0.0  
**Last Updated**: 2026-01-17

---

## Purpose

This checklist defines **mandatory pre-publication conditions** that must be satisfied before any artifact may be archived on Zenodo and assigned a DOI.

This checklist serves as a strict governance gate to ensure that only appropriate scientific outputs receive permanent identifiers, and to prevent misuse of Zenodo for internal governance milestones or incomplete work.

---

## Core Principle

**Zenodo publication requires explicit scientific readiness and governance approval.**

**GitHub Releases alone are insufficient for scientific publication.**

Zenodo archiving is a formal scholarly act that creates a permanent, citable record. All artifacts submitted to Zenodo must meet rigorous scientific and governance standards.

---

## Hard Block Rule

**If ANY checklist item fails → Zenodo publication is PROHIBITED.**

No exceptions may be granted without explicit governance approval documented in `governance/APPROVAL.md` following the exception approval process defined in ZENODO_EXCEPTION_REGISTER.md.

---

## Mandatory Pre-Publication Checklist

Before requesting Zenodo archiving and DOI minting, **ALL** of the following conditions must be satisfied:

### 1. Scientific Output Classification

**Requirement**: The artifact must be a scientific output suitable for scholarly citation.

**Validation Criteria**:
- [ ] Artifact is one of the following types:
  - Scientific theory with formal specification
  - Research framework with documented methodology
  - Dataset with validation and metadata
  - Model with reproducibility documentation
  - Peer-review-ready AI artifact
  - Peer-review-ready astrophysics artifact

**FAIL if**:
- Artifact is an internal governance milestone (GATE-1, GATE-2, etc.)
- Artifact is an enforcement step or CI validation marker
- Artifact is development infrastructure or tooling
- Artifact is a draft or work-in-progress
- Artifact is a patch release or minor bug fix

**Approval Authority**: Governance authority must verify classification

---

### 2. Non-Governance Milestone Verification

**Requirement**: The artifact must NOT be an internal governance milestone.

**Validation Criteria**:
- [ ] Artifact is NOT labeled as GATE-1, GATE-2, GATE-3, or any numbered gate
- [ ] Artifact is NOT an enforcement checkpoint or step
- [ ] Artifact is NOT a CI/CD validation marker
- [ ] Artifact is NOT an internal coordination milestone
- [ ] Artifact is NOT a governance baseline or compliance record

**FAIL if**:
- Artifact title or description contains "Gate", "GATE", "Enforcement", "Baseline", "Milestone", "Checkpoint", or "Validation" in the context of internal governance

**Approval Authority**: Governance authority must verify non-governance status

---

### 3. Scientific Abstract

**Requirement**: A clear, formal scientific abstract must be present.

**Validation Criteria**:
- [ ] Abstract describes the scientific contribution
- [ ] Abstract states the research question or problem addressed
- [ ] Abstract summarizes the methodology employed
- [ ] Abstract indicates the key findings or capabilities
- [ ] Abstract is written in formal scientific language
- [ ] Abstract is between 100-500 words

**FAIL if**:
- No abstract provided
- Abstract is marketing or promotional language
- Abstract describes internal processes rather than scientific contribution
- Abstract is shorter than 100 words or longer than 500 words

**Approval Authority**: Scientific lead must review abstract

---

### 4. Evidence and Methodology Documentation

**Requirement**: Evidence sources, methodology, and validation must be explicitly documented.

**Validation Criteria**:
- [ ] **Evidence**: Sources of data or observations clearly identified
- [ ] **Method**: Procedures and techniques explicitly documented
- [ ] **Validation**: Quality assurance and verification procedures described
- [ ] **Reproducibility**: Sufficient detail for independent reproduction
- [ ] **Limitations**: Known constraints or boundaries acknowledged
- [ ] **ImmutableRefs**: Commit hashes or content hashes provided for traceability

**FAIL if**:
- Evidence sources not identified
- Methodology not documented
- Validation procedures absent
- Reproducibility not possible from documentation
- No immutable references provided

**Approval Authority**: Methodology review by scientific lead

---

### 5. Canonical References

**Requirement**: All canonical references and dependencies must be identified.

**Validation Criteria**:
- [ ] Related work cited appropriately
- [ ] Canonical governance reference included (if applicable): TRIZEL Governance v1.0.0
- [ ] Dependencies and prerequisites documented
- [ ] Prior versions or related artifacts linked
- [ ] Superseded work marked appropriately

**FAIL if**:
- Related work not cited
- Dependencies not documented
- Prior versions not linked
- Canonical governance reference missing (when applicable)

**Approval Authority**: Documentation review by governance authority

---

### 6. Version Frozen and Immutable

**Requirement**: The artifact version must be frozen and immutable.

**Validation Criteria**:
- [ ] Version tag created in Git (semantic version: vX.Y.Z)
- [ ] Repository state frozen at tagged commit
- [ ] No pending changes or uncommitted work
- [ ] All tests and validation checks passed
- [ ] All GATE enforcement checks passed (if applicable)
- [ ] Documentation complete and finalized

**FAIL if**:
- No version tag present
- Uncommitted changes exist
- Tests or validation checks failing
- Documentation incomplete
- Work-in-progress markers present (TODO, FIXME, etc.)

**Approval Authority**: Technical lead must verify version freeze

---

### 7. Citation Intent

**Requirement**: The intended use for citation must be explicitly stated.

**Validation Criteria**:
- [ ] Citation purpose clearly stated (e.g., "Cite when using this methodology", "Cite when referencing this dataset")
- [ ] Recommended citation format provided (BibTeX, APA, etc.)
- [ ] Authorship and contributions documented
- [ ] License clearly specified (MIT, CC-BY-4.0, etc.)
- [ ] Funding sources acknowledged (if applicable)

**FAIL if**:
- Citation intent not stated
- Citation format not provided
- Authorship unclear
- License not specified
- Required acknowledgments missing

**Approval Authority**: Publication lead must review citation information

---

### 8. Governance Approval

**Requirement**: Explicit governance approval must be recorded.

**Validation Criteria**:
- [ ] Zenodo archiving request issue opened in trizel-ai/trizel-core
- [ ] Justification for DOI minting documented
- [ ] Governance authority reviewed request
- [ ] Approval documented in `governance/APPROVAL.md`
- [ ] Approval entry includes:
  - PR number or issue number
  - Artifact identification (title, version, DOI to be minted)
  - Rationale for scientific publication
  - Approver name and date
  - Confirmation that all checklist items satisfied

**FAIL if**:
- No governance approval request submitted
- Approval not documented in governance/APPROVAL.md
- Approval entry incomplete
- Checklist items not verified by approver

**Approval Authority**: Governance authority (final gate)

---

## Checklist Execution Protocol

### Step 1: Self-Assessment
Repository maintainer completes checklist and documents evidence for each item.

### Step 2: Governance Request
Submit issue in trizel-ai/trizel-core with title: "Request Zenodo Archiving: [Artifact Title] [Version]"

Include in issue:
- Completed checklist with evidence for each item
- Link to frozen version (Git tag)
- Proposed Zenodo metadata (title, abstract, authors, keywords)
- Justification for scientific publication

### Step 3: Governance Review
Governance authority reviews checklist and supporting evidence:
- Verifies each checklist item satisfied
- Reviews scientific merit and appropriateness
- Confirms non-governance-milestone status
- Validates metadata completeness

### Step 4: Approval or Rejection

**If ALL items satisfied**:
- Approval recorded in governance/APPROVAL.md
- Proceed to Zenodo archiving
- Create Git release tag
- Zenodo webhook creates deposit
- DOI minted by Zenodo

**If ANY item fails**:
- Request REJECTED
- Detailed feedback provided
- Artifact may be resubmitted after addressing issues
- GitHub Release may be created without Zenodo archiving

### Step 5: Post-Publication
- Verify DOI resolves correctly
- Update repository metadata with DOI
- Update CITATION.cff
- Announce release with proper citation

---

## Explicit Prohibitions

### Zenodo Publication is PROHIBITED if:

1. **Artifact is internal governance milestone**
   - GATE-1, GATE-2, enforcement steps, CI markers
   - **Alternative**: Use GitHub Releases only

2. **Checklist items incomplete**
   - Missing abstract, methodology, or validation
   - **Alternative**: Complete documentation first

3. **No governance approval**
   - Approval not documented in governance/APPROVAL.md
   - **Alternative**: Submit governance request

4. **Version not frozen**
   - Uncommitted changes, work-in-progress markers
   - **Alternative**: Finalize version, create Git tag

5. **Non-scientific artifact**
   - Development tools, infrastructure, internal documentation
   - **Alternative**: Use GitHub Releases or no publication

---

## Governance Violation Consequences

**Zenodo publication without completing this checklist is a governance violation.**

If Zenodo archiving occurs without checklist completion:

1. **Immediate Response**:
   - Document violation in governance log
   - Create incident report
   - Notify governance authority

2. **Corrective Action**:
   - Update Zenodo metadata to add warning (if possible)
   - Register as exception in ZENODO_EXCEPTION_REGISTER.md
   - Mark as "NOT A SCIENTIFIC PUBLICATION" if inappropriate
   - Document proper citation alternative

3. **Policy Enforcement**:
   - Strengthen pre-publication validation
   - Review approval process
   - Update checklist if gaps identified

4. **Accountability**:
   - Review by governance authority
   - Documented in governance/APPROVAL.md
   - Prevent recurrence through process improvement

---

## Relationship to Other Policies

This checklist operates in conjunction with:

- **ZENODO_ARCHIVING_POLICY.md** — Defines eligible vs ineligible artifacts
- **ZENODO_EXCEPTION_REGISTER.md** — Documents historical exceptions
- **GOVERNANCE_ENFORCEMENT.md** — GATE 1 enforcement framework
- **PUBLICATION_POLICY.md** — Website publication rules
- **governance/APPROVAL.md** — Governance approval log

All policies must be satisfied for Zenodo publication.

---

## Checklist Template

Copy this template for each Zenodo archiving request:

```markdown
## Zenodo Readiness Checklist

**Artifact**: [Title]
**Version**: [vX.Y.Z]
**Repository**: [trizel-ai/repo-name]
**Request Date**: [YYYY-MM-DD]
**Requestor**: [GitHub username]

### 1. Scientific Output Classification
- [ ] Artifact type: [theory | framework | dataset | model | AI artifact | astrophysics artifact]
- [ ] Evidence: [Explanation]
- **Approval**: [ ] Governance authority verified

### 2. Non-Governance Milestone Verification
- [ ] NOT an internal governance milestone
- [ ] Evidence: [Confirmation of scientific nature]
- **Approval**: [ ] Governance authority verified

### 3. Scientific Abstract
- [ ] Abstract present (100-500 words)
- [ ] Abstract location: [File path or section]
- **Approval**: [ ] Scientific lead reviewed

### 4. Evidence and Methodology Documentation
- [ ] Evidence sources identified
- [ ] Methodology documented
- [ ] Validation procedures described
- [ ] Reproducibility documented
- [ ] Immutable references provided: [commit hash]
- **Approval**: [ ] Scientific lead reviewed

### 5. Canonical References
- [ ] Related work cited
- [ ] Canonical governance reference: TRIZEL Governance v1.0.0 (if applicable)
- [ ] Dependencies documented
- **Approval**: [ ] Governance authority verified

### 6. Version Frozen and Immutable
- [ ] Git tag: [vX.Y.Z]
- [ ] Commit hash: [hash]
- [ ] All tests passed: YES
- [ ] Documentation complete: YES
- **Approval**: [ ] Technical lead verified

### 7. Citation Intent
- [ ] Citation purpose stated
- [ ] Citation format provided (BibTeX, etc.)
- [ ] Authors documented
- [ ] License: [License type]
- **Approval**: [ ] Publication lead reviewed

### 8. Governance Approval
- [ ] Request issue: #[issue number]
- [ ] Approval in governance/APPROVAL.md: [link]
- [ ] All checklist items verified: YES
- **Approval**: [ ] Governance authority (FINAL)

---

**Final Decision**: [ ] APPROVED for Zenodo archiving / [ ] REJECTED

**Approver**: [Name]
**Date**: [YYYY-MM-DD]
```

---

## Maintenance and Updates

### Checklist Review Cadence

This checklist will be reviewed:
- Annually as part of governance review
- After any Zenodo publication incident
- When ZENODO_ARCHIVING_POLICY.md is updated
- When new artifact types are introduced

### Checklist Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-17 | Initial Zenodo Readiness Checklist with 8 mandatory conditions |

---

## Contact and Questions

For questions about the Zenodo Readiness Checklist:

1. **Review** this checklist and related policies
2. **Prepare** completed checklist with evidence
3. **Submit** governance request issue
4. **Await** governance authority review and approval

For checklist clarifications or policy questions:
- Open issue in trizel-ai/trizel-core with tag "zenodo-checklist"

---

**Authority**: This is part of the Layer-0 governance framework.  
**Enforcement**: REQUIRED for all Zenodo archiving requests.  
**Compliance**: Mandatory for all TRIZEL repositories using Zenodo integration.

---

## Summary

- **Purpose**: Strict gate for Zenodo publication
- **Requirement**: ALL 8 checklist items must be satisfied
- **Hard Block**: ANY failure → Zenodo publication PROHIBITED
- **Approval**: Governance authority must review and approve
- **Violation**: Zenodo publication without checklist is governance violation
- **Alternative**: GitHub Releases for artifacts not meeting scientific publication criteria
