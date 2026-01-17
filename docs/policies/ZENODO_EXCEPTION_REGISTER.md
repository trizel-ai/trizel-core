# ZENODO_EXCEPTION_REGISTER.md

## Zenodo Exception Register

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Register Version**: 1.0.0  
**Last Updated**: 2026-01-17

---

## Purpose

This register formally documents historical exceptions to the Zenodo Archiving Policy where internal governance milestones were archived on Zenodo and assigned DOIs.

These exceptions are **CLOSED** and serve as traceability records only. No future internal governance milestones may be archived on Zenodo without explicit governance approval via `governance/APPROVAL.md`.

---

## Policy Context

This register operates under the authority of:
- **ZENODO_ARCHIVING_POLICY.md** — Formal policy prohibiting Zenodo use for internal governance milestones
- **GOVERNANCE_ENFORCEMENT.md** — GATE 1 enforcement framework

**Core Principle**: Zenodo is NOT to be used for internal governance milestones (Gates, enforcement steps, CI validation). Such records are traceability-only and NOT scientific publications.

---

## Registered Exceptions

### Exception 1: Gate 1 — Governance Baseline

**DOI**: 10.5281/zenodo.18283981  
**Title**: Gate 1 — Governance Baseline (Internal Milestone)  
**Zenodo URL**: https://doi.org/10.5281/zenodo.18283981

**Classification**: Internal governance archive (traceability only)

**Scientific Status**: **NOT A SCIENTIFIC PUBLICATION**

**Citation Status**: **DO NOT CITE**

**Canonical Reference**: TRIZEL Governance v1.0.0

**Rationale for Exception**:
This DOI was created as a historical traceability record before the formal Zenodo Archiving Policy was established. It documents the completion of GATE 1 governance enforcement implementation.

**Exception Status**: **CLOSED**

This exception is formally acknowledged and closed. The record exists for historical traceability purposes only and must not be cited as a scientific publication.

**Proper Citation Alternative**:
For governance framework references, cite the canonical governance baseline:
- **TRIZEL Governance v1.0.0** (canonical reference for governance structure)

---

## Exception Criteria

For a Zenodo record to be registered as an exception in this register, it must meet ALL of the following criteria:

1. **Historical Record**: Created before Zenodo Archiving Policy was formally established
2. **Internal Governance Content**: Contains governance milestones, enforcement steps, or CI validation markers
3. **Traceability Purpose**: Serves only as a historical traceability record
4. **No Scientific Contribution**: Does NOT contain scientific theories, research frameworks, datasets, or models
5. **Governance Approval**: Registered with explicit governance authority approval

---

## Treatment of Registered Exceptions

All Zenodo records listed in this register **MUST**:

1. **Be labeled**: "NOT A SCIENTIFIC PUBLICATION" in the Zenodo metadata or description
2. **Include**: "DO NOT CITE" in the description or notes field
3. **Reference**: The canonical scientific baseline where applicable (e.g., TRIZEL Governance v1.0.0)
4. **Clarify**: The record is for traceability purposes only

**Note**: DOIs are permanent and cannot be deleted. However, Zenodo metadata can be updated to include these clarifications.

---

## Future Policy

### Prohibition on New Internal Governance Archives

**Effective immediately**, Zenodo **MUST NOT** be used for:

- Internal governance milestones (GATE-1, GATE-2, GATE-3, etc.)
- Enforcement steps or checkpoints
- CI/CD validation markers
- Development progress indicators
- Internal coordination milestones

### Approved Alternatives for Internal Milestones

For tracking internal governance milestones, use:

1. **GitHub Releases**: Version tracking and release notes
2. **Git Tags**: Version markers and milestone identifiers
3. **GitHub Milestones**: Project management and coordination
4. **GitHub Issues**: Tracking and documentation
5. **Repository Documentation**: Changelog and version history

**None of these alternatives should request Zenodo archiving or DOI minting.**

### Exception Approval Process

Any future request to archive internal governance content on Zenodo requires:

1. **Formal Request**: Issue opened in `trizel-ai/trizel-core` with title "Request Zenodo Exception: [Description]"
2. **Justification**: Detailed rationale for why exception is necessary
3. **Governance Review**: Evaluation by governance authority
4. **Documented Approval**: Explicit approval recorded in `governance/APPROVAL.md`
5. **Register Update**: Addition to this register with full documentation
6. **Metadata Requirements**: All treatment requirements applied to Zenodo record

**Default Response**: DENY (Zenodo archiving for internal governance is prohibited by policy)

---

## Enforcement Note

**This register and the associated Zenodo Archiving Policy are binding for all TRIZEL repositories.**

Any violations of this policy require explicit governance approval documented in:
- `governance/APPROVAL.md`

No repository maintainer may:
- Archive internal governance milestones on Zenodo
- Request DOI minting for internal coordination artifacts
- Create new exceptions without formal governance approval

---

## Register Maintenance

### Adding New Exceptions

To add a new exception (requires governance approval):

1. **Obtain Approval**: Documented in `governance/APPROVAL.md`
2. **Update This Register**: Add exception with all required fields
3. **Update Version**: Increment register version
4. **Update Zenodo Metadata**: Add "NOT A SCIENTIFIC PUBLICATION" and "DO NOT CITE" labels
5. **Document Canonical Reference**: Link to proper citation alternative

### Register Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-17 | Initial register with Exception 1 (DOI 10.5281/zenodo.18283981) |

---

## Audit Trail

### Exception Registration Log

| Exception # | DOI | Registration Date | Approved By | Status |
|-------------|-----|-------------------|-------------|--------|
| 1 | 10.5281/zenodo.18283981 | 2026-01-17 | Governance Authority | CLOSED |

---

## Related Documents

- `docs/policies/ZENODO_ARCHIVING_POLICY.md` — Formal Zenodo archiving policy
- `GOVERNANCE_ENFORCEMENT.md` — GATE 1 enforcement framework
- `governance/APPROVAL.md` — Governance approval log
- `PUBLICATION_POLICY.md` — Website publication rules

---

## Governance of This Register

### Register Updates

Changes to this exception register require:

1. **PR in `trizel-core`**: Update this file
2. **Version bump**: Increment register version
3. **Governance approval**: Documented in `governance/APPROVAL.md`
4. **Justification**: Clear rationale for addition or modification
5. **Audit trail update**: Log all changes in audit trail section

### Register Review Cadence

This register will be reviewed:
- Annually as part of governance review
- When new exception requests are submitted
- When Zenodo Archiving Policy is updated
- When TRIZEL governance structure changes

---

## Contact and Questions

For questions about Zenodo exceptions or to request a new exception:

1. **Review** this register and ZENODO_ARCHIVING_POLICY.md
2. **Open an issue** in `trizel-ai/trizel-core` with tag "zenodo-exception"
3. **Request governance review** with detailed justification
4. **Expect denial** unless extraordinary circumstances warrant exception

---

**Authority**: This is part of the Layer-0 governance framework.  
**Enforcement**: Manual approval required for any exception additions.  
**Compliance**: Mandatory for all TRIZEL repositories using Zenodo integration.

---

## Summary

- **Total Registered Exceptions**: 1
- **Status**: All exceptions CLOSED
- **Future Policy**: Zenodo MUST NOT be used for internal governance milestones
- **Alternative**: Use GitHub Releases for milestone tracking
- **Canonical Governance Reference**: TRIZEL Governance v1.0.0
