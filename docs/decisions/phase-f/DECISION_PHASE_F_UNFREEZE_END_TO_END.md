# Phase-F Decision Record: Unfreeze End-to-End Publication Enablement

**Repository:** trizel-ai/trizel-core  
**Document Type:** Layer-0 Governance Decision Record  
**Authority Level:** Layer-0 (Governance)  
**Status:** APPROVED  
**Version:** 1.0.0  
**Decision Date:** 2026-01-23  
**Review Cycle:** On completion of Phase-F implementation or on request

---

## I. Title / Date / Scope

### Title
**Phase-F Decision: Authorization of End-to-End Publication Enablement (Layer-1 → Layer-2)**

### Date
**Decision Effective Date:** 2026-01-23  
**Next Scheduled Review:** On Phase-F completion or governance structural changes

### Scope

This decision authorizes the **end-to-end publication pipeline** that enables:

1. **Layer-1 Execution** to generate publishable **STATIC artifacts** from canonical source data
2. **Layer-2 Publication** to consume, render, and publish those STATIC artifacts on public-facing platforms

**Scope Boundaries:**

- **IN SCOPE:** Layer-1 generation of static HTML, CSS, PDF, and metadata artifacts from canonical governance and provenance sources
- **IN SCOPE:** Layer-2 rendering and publication of pre-packaged static artifacts received from Layer-1
- **IN SCOPE:** Static navigation, styling, and layout for published artifacts
- **OUT OF SCOPE:** Layer-2 executable logic beyond UI rendering of static content
- **OUT OF SCOPE:** Live data, real-time telemetry, analytics counters, or runtime metrics
- **OUT OF SCOPE:** Backend APIs, database access, or schema modifications on Layer-2
- **OUT OF SCOPE:** AI-generated scientific claims or authoritative interpretations

**Critical Constraint:**  
This decision **UNFREEZES** the end-to-end publication pipeline while **MAINTAINING** all Phase-E security constraints. Layer-2 remains restricted to static content rendering only.

---

## II. Decision (Authorization Statement)

### A. Authorization

By Layer-0 governance authority, this decision **AUTHORIZES** the following:

1. **Layer-1 Publication Artifact Generation**
   - Layer-1 execution environments MAY generate static publication artifacts (HTML, CSS, PDF, metadata)
   - Layer-1 MAY package these artifacts for consumption by Layer-2 publication platforms
   - Layer-1 MAY emit structured metadata conforming to TRIZEL registry schemas
   - Layer-1 MUST operate only on canonical source data (governance documents, provenance records, structural definitions)

2. **Layer-2 Static Publication**
   - Layer-2 publication platforms (e.g., `trizel-site`) MAY receive pre-packaged static artifacts from Layer-1
   - Layer-2 MAY render and publish these static artifacts on public-facing websites
   - Layer-2 MAY provide static navigation, styling, and layout for published content
   - Layer-2 MUST NOT execute logic beyond UI rendering of static packaged artifacts

3. **End-to-End Pipeline Activation**
   - The complete publication flow (Layer-1 generation → Layer-2 publication) is now ACTIVE
   - Human review gates remain MANDATORY at critical transition points
   - All activities MUST comply with fail-closed governance principles

### B. Rationale

This authorization is issued because:

1. **Phase-E Foundation Complete:** Phase-E established publication constraints, allowlists, and governance frameworks
2. **Static-Only Architecture:** The end-to-end pipeline design ensures Layer-2 handles only static artifacts
3. **Security Constraints Maintained:** No live data, telemetry, or dynamic execution is authorized
4. **Governance Maturity:** Layer-0 governance has reached sufficient maturity to enable controlled publication
5. **Academic Transparency:** External publication supports reproducibility and peer review of governance methodology

### C. Effect

This decision **UNFREEZES** the end-to-end publication pipeline while maintaining strict security boundaries established in Phase-E.

---

## III. Permitted (Explicit Allow-List)

The following activities are **EXPLICITLY PERMITTED** under Phase-F:

### A. Layer-1 Activities (Artifact Generation)

#### 1. Static Artifact Creation
- ✅ **ALLOWED:** Generate static HTML files from canonical markdown sources
- ✅ **ALLOWED:** Generate CSS stylesheets for presentation and layout
- ✅ **ALLOWED:** Generate PDF artifacts from approved governance documents
- ✅ **ALLOWED:** Generate structured metadata (JSON, YAML) conforming to TRIZEL schemas
- ✅ **ALLOWED:** Package artifacts into immutable release bundles

#### 2. Source Data Processing
- ✅ **ALLOWED:** Read canonical governance documents from `docs/` directories
- ✅ **ALLOWED:** Read provenance records and structural definitions
- ✅ **ALLOWED:** Extract metadata for citation and archival purposes
- ✅ **ALLOWED:** Validate source documents against allowlists
- ✅ **ALLOWED:** Apply templates and styling to generate publication-ready artifacts

#### 3. Artifact Packaging and Transfer
- ✅ **ALLOWED:** Create versioned artifact packages (e.g., tarballs, zip files, git tags)
- ✅ **ALLOWED:** Tag artifact packages with semantic versions
- ✅ **ALLOWED:** Generate checksums and content hashes for integrity verification
- ✅ **ALLOWED:** Transfer packaged artifacts to Layer-2 via PR workflows or artifact repositories

### B. Layer-2 Activities (Static Publication)

#### 1. Static Content Rendering
- ✅ **ALLOWED:** Receive pre-packaged static artifacts from Layer-1
- ✅ **ALLOWED:** Render static HTML/CSS content in web browsers
- ✅ **ALLOWED:** Serve static PDF files for download
- ✅ **ALLOWED:** Display static metadata for citation purposes
- ✅ **ALLOWED:** Provide static navigation (table of contents, breadcrumbs, internal links)

#### 2. Presentation and Layout
- ✅ **ALLOWED:** Apply CSS for styling and responsive layout
- ✅ **ALLOWED:** Use static site generation frameworks (Jekyll, Hugo, etc.) if they produce static output only
- ✅ **ALLOWED:** Implement static search indexes (pre-built at Layer-1)
- ✅ **ALLOWED:** Provide static syntax highlighting or code formatting

#### 3. Hosting and Deployment
- ✅ **ALLOWED:** Deploy static artifacts to public-facing web servers
- ✅ **ALLOWED:** Use CDNs for static content delivery
- ✅ **ALLOWED:** Serve content over HTTPS with appropriate caching headers
- ✅ **ALLOWED:** Host on platforms like GitHub Pages, Netlify, Vercel (static mode only)

### C. Governance and Quality Assurance

#### 1. Human Review Gates
- ✅ **ALLOWED:** Human review of Layer-1 generated artifacts before Layer-2 publication
- ✅ **ALLOWED:** Human approval of PRs transferring artifacts from Layer-1 to Layer-2
- ✅ **ALLOWED:** Human validation of published content against allowlists
- ✅ **ALLOWED:** Rollback procedures requiring human authorization

#### 2. Validation and Verification
- ✅ **ALLOWED:** Automated validation of artifact structure and schema compliance
- ✅ **ALLOWED:** Link integrity checks (ensuring links point to immutable artifacts)
- ✅ **ALLOWED:** Content hash verification (ensuring artifact integrity)
- ✅ **ALLOWED:** Allowlist enforcement (ensuring only approved content is published)

#### 3. Audit and Monitoring
- ✅ **ALLOWED:** Logging of publication activities for audit trails
- ✅ **ALLOWED:** Version tracking of published artifacts
- ✅ **ALLOWED:** Git commit history as audit log
- ✅ **ALLOWED:** Immutable release tags for published versions

---

## IV. Forbidden (Explicit Deny-List)

The following activities remain **STRICTLY FORBIDDEN** under Phase-F:

### A. Layer-2 Executable Logic

#### 1. Runtime Execution
- ❌ **FORBIDDEN:** JavaScript execution beyond static UI rendering
- ❌ **FORBIDDEN:** Server-side code execution on Layer-2
- ❌ **FORBIDDEN:** WebAssembly or other runtime compilation
- ❌ **FORBIDDEN:** Client-side logic that modifies or generates content dynamically

#### 2. Live Data and Telemetry
- ❌ **FORBIDDEN:** Live data fetching from APIs or databases
- ❌ **FORBIDDEN:** Real-time analytics or usage counters
- ❌ **FORBIDDEN:** Telemetry collection (page views, user behavior, etc.)
- ❌ **FORBIDDEN:** Dynamic content generation based on user input or external data

#### 3. Backend and Infrastructure
- ❌ **FORBIDDEN:** Backend APIs or server endpoints on Layer-2
- ❌ **FORBIDDEN:** Database queries or schema modifications
- ❌ **FORBIDDEN:** Authentication or user management systems
- ❌ **FORBIDDEN:** Form submissions or interactive features requiring server processing

### B. Scientific Content and Interpretation

#### 1. Scientific Claims
- ❌ **FORBIDDEN:** AI-generated scientific claims or hypotheses
- ❌ **FORBIDDEN:** Interpretation of scientific data or results
- ❌ **FORBIDDEN:** Publication of experimental findings or analysis results
- ❌ **FORBIDDEN:** Claims of correctness, validation, or hypothesis confirmation

#### 2. Scientific Artifacts
- ❌ **FORBIDDEN:** Publication of datasets, models, or training artifacts
- ❌ **FORBIDDEN:** Publication of computational experiments or benchmarks
- ❌ **FORBIDDEN:** Publication of scientific code or analysis scripts
- ❌ **FORBIDDEN:** Endorsement or interpretation of scientific theories

### C. Automation Overrides

#### 1. Bypass of Review Gates
- ❌ **FORBIDDEN:** Auto-merge of publication PRs without human approval
- ❌ **FORBIDDEN:** Automatic deployment to production without human gate
- ❌ **FORBIDDEN:** Override of required approvals or checks
- ❌ **FORBIDDEN:** Emergency procedures that bypass governance rules

#### 2. Allowlist Violations
- ❌ **FORBIDDEN:** Publication of documents not on Phase-E allowlist
- ❌ **FORBIDDEN:** Inclusion of internal drafts or working documents
- ❌ **FORBIDDEN:** Publication of enforcement code or automation logic
- ❌ **FORBIDDEN:** Inclusion of non-canonical or unapproved sources

### D. Mutable References

#### 1. Links and Citations
- ❌ **FORBIDDEN:** Links to mutable branches (e.g., `main`, `develop`)
- ❌ **FORBIDDEN:** Links to draft or work-in-progress content
- ❌ **FORBIDDEN:** References to unpublished or internal artifacts
- ❌ **FORBIDDEN:** Citations without permanent identifiers (DOI, commit SHA, release tag)

---

## V. Governance Controls

This decision operates under strict Layer-0 governance controls:

### A. Epistemic Neutrality (EN) Semantic Authority

**Principle:**  
All published artifacts MUST maintain epistemic neutrality. TRIZEL governance does not claim scientific authority or endorse scientific theories.

**Application:**
- Published content is **descriptive of process**, not **interpretive of results**
- Published content documents **governance methodology**, not **scientific findings**
- Published content provides **epistemic infrastructure**, not **scientific claims**

**Enforcement:**
- All artifacts MUST pass EN validation before publication
- Layer-1 generation MUST enforce EN constraints in source selection
- Layer-2 publication MUST reject artifacts that violate EN principles

### B. Approval Requirements

**Layer-1 → Layer-2 Transfer:**
- All PRs transferring artifacts from Layer-1 to Layer-2 REQUIRE human approval
- Approver MUST verify artifact compliance with allowlists and governance rules
- Approver MUST confirm EN neutrality and static-only content

**Layer-2 Production Deployment:**
- All merges to Layer-2 production branches REQUIRE human approval
- Deployment MUST use staging/preview environments before production
- Rollback procedures MUST be validated and available

**Governance Exceptions:**
- Any deviation from permitted activities REQUIRES a new Layer-0 governance decision
- Emergency procedures REQUIRE post-facto governance review and documentation

### C. Auditability and Transparency

**Audit Trails:**
- All publication activities MUST be logged in git history
- All artifacts MUST be tagged with semantic versions
- All PRs MUST include rationale and compliance validation

**Transparency:**
- Decision records MUST be public and version-controlled
- Allowlists MUST be publicly documented
- Enforcement mechanisms MUST be documented and reproducible

**Review Cycles:**
- Phase-F authorization will be reviewed on completion of initial implementation
- Annual reviews or on significant governance structural changes
- Ad-hoc reviews on security incidents or compliance violations

---

## VI. Effect / Supersedence

### A. Effect

This decision **ACTIVATES** the end-to-end publication pipeline:

**What Is Enabled:**
- Layer-1 MAY now generate publication artifacts
- Layer-2 MAY now publish static artifacts received from Layer-1
- The complete Layer-1 → Layer-2 flow is operationally authorized

**What Remains Unchanged:**
- Phase-E security constraints remain in full force
- Static-only publication requirement remains mandatory
- Human review gates remain required
- Fail-closed governance principles remain active
- Scientific content publication remains forbidden

### B. Supersedence

**This Decision Extends (Does Not Replace):**
- `DECISION_PHASE_E_PUBLICATION.md` — Allowlist and publication eligibility criteria remain binding
- `DECISION_PHASE_E_TRANSITION.md` — T2/T3 governance rules remain applicable to Layer-2
- `PUBLICATION_POLICY.md` — Static-only and fail-closed principles remain in force
- `FREEZE.md` — SYSTEM FREEZE for scientific content remains active

**This Decision Does NOT Supersede:**
- Scientific authorization requirements (no scientific publication is authorized)
- Internal governance document restrictions (internal drafts remain unpublishable)
- Executable code restrictions (no code in published artifacts)
- Dynamic content restrictions (no JavaScript execution, no live data)

**Relationship to Existing Governance:**
- **Compatible with Phase-E:** This decision unfreezes the pipeline established in Phase-E
- **Compatible with SYSTEM FREEZE:** No scientific content authorization is provided
- **Extends Publication Policy:** Enables Layer-1 artifact generation previously undefined
- **Maintains Security Posture:** All Phase-E security constraints remain intact

---

## VII. Sign-Off

**Layer-0 Governance Authority**

This decision is issued under Layer-0 governance authority as documented in:
- `TRIZEL_GOVERNANCE_LEDGER.md` (Layer-0 authority model)
- `ROLE.md` (Repository classification and epistemic layer assignment)
- `GOVERNANCE_REFERENCE.md` (Governance structure and decision-making process)

**Authorization:**  
By Layer-0 authority, the end-to-end publication pipeline (Layer-1 → Layer-2) is hereby **AUTHORIZED** under the constraints, permissions, and governance controls specified in this decision.

**Effective Date:** 2026-01-23

**Binding Status:** ACTIVE and BINDING on all TRIZEL repositories involved in publication activities, specifically:
- `trizel-ai/trizel-core` (governance repository)
- Layer-1 execution environments (artifact generation)
- `trizel-ai/trizel-site` or equivalent Layer-2 publication platforms (static publication)

**Review Authority:**  
This decision may be reviewed, amended, or superseded only by subsequent Layer-0 governance decisions. Any amendments MUST maintain or strengthen security constraints.

**Accountability:**  
Violations of this decision's constraints constitute governance violations and require:
1. Immediate rollback of unauthorized activities
2. Root cause analysis and documentation
3. Governance decision update (if warranted)
4. Implementation of prevention measures

---

## Document Metadata

**Version History:**
- 1.0.0 (2026-01-23): Initial decision authorizing Phase-F end-to-end publication enablement

**Document Location:**
- `docs/decisions/phase-f/DECISION_PHASE_F_UNFREEZE_END_TO_END.md`

**Related Documents:**
- `DECISION_PHASE_E_PUBLICATION.md` (Phase-E allowlist and eligibility)
- `DECISION_PHASE_E_TRANSITION.md` (T2/T3 governance rules)
- `PUBLICATION_POLICY.md` (Static-only publication requirements)
- `FREEZE.md` (SYSTEM FREEZE status)
- `TRIZEL_GOVERNANCE_LEDGER.md` (Governance authority)

**Authority Level:** Layer-0 (Governance)  
**Classification:** Governance Decision Record  
**Binding Scope:** All TRIZEL repositories involved in publication activities  
**Next Review:** On Phase-F implementation completion or governance structural changes

---

**END OF DECISION RECORD**
