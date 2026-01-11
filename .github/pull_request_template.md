## TRIZEL DIRECTIVE Compliance Checklist

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter

---

### 1. Repository Role Acknowledgment

**Single-sentence role**:  
This repository is the canonical governance and charter authority that defines epistemic boundaries, layer separation rules, and structural principles for the entire TRIZEL ecosystem, and contains no data, execution logic, or analytical content.

---

### 2. Allowed/Forbidden Boundaries

**Allowed in this repository**:
- [ ] Governance policy text and procedural definitions
- [ ] Epistemic boundary specifications (layer definitions, separation rules)
- [ ] Repository classification standards and role registries
- [ ] Publication policy definitions
- [ ] Structural principles and constitutional framework
- [ ] Non-executable documentation about TRIZEL system architecture

**Forbidden in this repository**:
- [ ] Scientific data, datasets, or observational records
- [ ] Executable code, algorithms, or computational logic
- [ ] Analysis results, statistical outputs, or derived metrics
- [ ] Models, predictions, or inference artifacts
- [ ] Interpretive claims or theoretical conclusions
- [ ] Deprecated terminology (STOE, V12-V22, versioned system labels)

---

### 3. TRIZEL DIRECTIVE Compliance

- [ ] **Deprecated terms check**: PASS (no STOE, V12-V22, versioned system labels, or theoretical lineage labels)
- [ ] **Cross-layer transfer check**: PASS (no execution, analysis, or data content added)
- [ ] **Publication rule check**: PASS (if website-related, uses allowlist-only approach)
- [ ] **Algorithm name check**: PASS (only "AUTO DZ ACT" used, no variants)

---

### 4. Minimal Diff Plan

**Files to change**:
- List each file being modified, added, or removed

**Exact edits**:
- Describe the specific changes being made to each file

**Rationale**:
- Explain why these changes are necessary
- Confirm they remain within Layer 0 (Governance) scope

**Tests/checks**:
- [ ] CI checks pass (deprecated terms, governance validation)
- [ ] All markdown files valid
- [ ] No executable code introduced
- [ ] No data files introduced
- [ ] Documentation builds successfully (if applicable)

**Rollback plan**:
- Describe how to revert these changes if needed

---

### 5. Output/Schema Impact Assessment

**Does this PR change any output contracts or schemas?**
- [ ] No schema changes
- [ ] Yes — schema changes included (complete section below)

**If YES, complete this section**:

**Affected downstream consumers**:
- List all repositories that consume outputs from trizel-core
- Example: website repository, other TRIZEL repos

**Required linked PRs**:
- [ ] Website repository PR: [link]
- [ ] Other affected repos: [links]

**Schema version update**:
- Current version: `________`
- New version: `________`
- Version bump type: [ ] Major [ ] Minor [ ] Patch

**Consumer update verification**:
- [ ] All downstream consumers updated before this PR merges
- [ ] Breaking changes documented
- [ ] Migration path provided

---

### 6. Layer 0 Boundary Verification

- [ ] Changes contain **only** governance content
- [ ] No execution logic added
- [ ] No data or analysis added
- [ ] No interpretation or theoretical claims added
- [ ] Documentation is non-interpretive

---

### 7. Version and Provenance

**Version impact**:
- [ ] No version change needed (typo fix, clarification)
- [ ] Minor version bump needed (new governance document, non-breaking addition)
- [ ] Major version bump needed (breaking change to governance structure)

**Provenance metadata**:
- [ ] Document version updated (if applicable)
- [ ] Effective date updated (if applicable)
- [ ] Changelog updated (if applicable)

---

### 8. Publication Readiness

**Are any changes intended for website publication?**
- [ ] No
- [ ] Yes — complete section below

**If YES, complete this section**:

- [ ] Content is in approved artifacts list (PUBLICATION_POLICY.md)
- [ ] Content includes `publishable: true` tag
- [ ] Content includes required provenance metadata
- [ ] Content is non-interpretive (methodology/status/provenance only)
- [ ] Website repository notified of changes
- [ ] Website allowlist updated (if needed)

---

### 9. Review Checklist

**Self-review completed**:
- [ ] All files reviewed for deprecated terms
- [ ] All files reviewed for cross-layer violations
- [ ] All changes aligned with TRIZEL DIRECTIVE
- [ ] Commit messages are clear and accurate
- [ ] No temporary files or build artifacts included

**Documentation updated**:
- [ ] README.md updated (if needed)
- [ ] GOVERNANCE.md updated (if needed)
- [ ] Related governance docs updated (if needed)
- [ ] No documentation conflicts or inconsistencies

---

### 10. CI/CD Validation

- [ ] Deprecated terms check: PASSING
- [ ] Governance validation check: PASSING
- [ ] All CI workflows: PASSING
- [ ] No new workflow failures introduced

---

### 11. Stop Condition Check

**Confirm none of these stop conditions are triggered**:

- [ ] No deprecated terms introduced
- [ ] No website ingestion of raw/unvalidated material proposed
- [ ] No governance text added outside trizel-core
- [ ] No interpretation written into governance docs
- [ ] No schema changes without consumer updates
- [ ] No layer collapse or boundary violations

---

### 12. Additional Context

**Description of changes**:
<!-- Provide a clear description of what this PR does and why -->

**Related issues**:
<!-- Link any related issues or discussions -->

**Breaking changes**:
<!-- List any breaking changes and migration steps -->

**Testing performed**:
<!-- Describe how changes were tested -->

---

### 13. Reviewer Guidance

**For reviewers**:

1. Verify deprecated terms check passed
2. Verify no cross-layer violations
3. Verify changes remain within Layer 0 scope
4. Check for any interpretation or theoretical claims
5. Verify schema changes have linked consumer PRs (if applicable)
6. Confirm minimal diff principle followed
7. Review compliance with TRIZEL DIRECTIVE

**Approval criteria**:
- [ ] All checklists completed
- [ ] All CI checks passing
- [ ] No stop conditions triggered
- [ ] Changes aligned with governance role
- [ ] Documentation clear and accurate

---

## Final Confirmation

By submitting this PR, I confirm:

- [x] I have read and understood the TRIZEL DIRECTIVE
- [x] All changes comply with Layer 0 (Governance) boundaries
- [x] No deprecated terminology has been introduced
- [x] No cross-layer responsibility transfer has occurred
- [x] This PR follows the minimal change principle
- [x] All required checks have been completed

---

**PR Author**: @<!-- username -->  
**Date**: <!-- YYYY-MM-DD -->  
**TRIZEL DIRECTIVE Version**: 1.0.0
