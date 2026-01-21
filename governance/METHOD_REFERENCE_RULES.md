# METHOD REFERENCE RULES

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance  
**Policy Version**: 1.0.0  
**Effective Date**: 2026-01-21  
**Status**: Active

---

## Purpose

This document establishes the formal rules for referencing AUTO-DZ-ACT and other scientific methods within TRIZEL outputs, publications, and citations.

**Core Principle**: Methods are tools, not theories. Citations must strictly separate methodological usage from interpretive claims.

---

## Scope

This policy governs:

1. **Method references** in scientific snapshots
2. **Method citations** in publications and DOI metadata
3. **Separation of method vs. result** in all documentation
4. **Prohibition of theory endorsement** through method citation
5. **Interpretive authority** boundaries

This policy applies to:
- All DOI-eligible snapshots
- All scientific publications
- All Layer-2 presentation content
- All external citations of TRIZEL work

---

## Core Principles

### 1. Method vs. Theory Separation

**Method**: A reproducible procedure for observation, analysis, or computation

**Theory**: An interpretive framework, explanatory model, or predictive claim

**Rule**: Method references must never imply theory endorsement.

### 2. AUTO-DZ-ACT is a Method, Not a Theory

AUTO-DZ-ACT is:
- A computational procedure
- A data processing algorithm
- A methodological tool

AUTO-DZ-ACT is **not**:
- A physical theory
- An explanatory framework
- A source of interpretive authority
- A validation of any specific interpretation

### 3. Citation Transparency

All citations must clearly distinguish:
- **What was done** (method)
- **What was observed** (result)
- **What is claimed** (interpretation, if any)

**No conflation permitted**

---

## AUTO-DZ-ACT Reference Rules

### Rule 1: Method-Only Reference

AUTO-DZ-ACT may be referenced **only** as a method.

**Acceptable reference**:
> "Data were processed using AUTO-DZ-ACT (version 1.0) as the computational method."

**Not acceptable**:
> "Results support AUTO-DZ-ACT theory."  
> *(AUTO-DZ-ACT is not a theory)*

> "AUTO-DZ-ACT explains the observed phenomenon."  
> *(AUTO-DZ-ACT does not explain; it processes)*

> "Findings validate the AUTO-DZ-ACT framework."  
> *(AUTO-DZ-ACT is a method, not a framework requiring validation)*

### Rule 2: Version-Specific Citation

All AUTO-DZ-ACT references must include:

1. **Name**: AUTO-DZ-ACT (exact spelling, hyphenation)
2. **Version**: Semantic version (e.g., 1.0.0)
3. **Role**: Explicitly stated as "method" or "computational procedure"

**Required format**:
```
Method: AUTO-DZ-ACT version X.Y.Z
Role: [Data processing | Computational analysis | Observation method]
Reference: [DOI or repository reference, if available]
```

**Example**:
```
Method: AUTO-DZ-ACT version 1.0.0
Role: Data processing method
Reference: https://github.com/trizel-ai/trizel-AI
```

### Rule 3: No Theory Endorsement

References to AUTO-DZ-ACT must **never**:

- Claim it as a physical theory
- Assert explanatory power beyond computational procedure
- Suggest validation of specific interpretations
- Imply endorsement of any theoretical framework
- Use language suggesting AUTO-DZ-ACT "proves" or "disproves" anything

**Prohibited language**:
- "AUTO-DZ-ACT theory"
- "AUTO-DZ-ACT framework"
- "AUTO-DZ-ACT model"
- "AUTO-DZ-ACT prediction"
- "AUTO-DZ-ACT explanation"

**Acceptable language**:
- "AUTO-DZ-ACT method"
- "AUTO-DZ-ACT procedure"
- "AUTO-DZ-ACT algorithm"
- "AUTO-DZ-ACT computation"
- "AUTO-DZ-ACT processing"

### Rule 4: No Interpretive Authority

AUTO-DZ-ACT does **not** have interpretive authority.

**What this means**:
- AUTO-DZ-ACT produces outputs
- Outputs require interpretation
- Interpretation is separate from method
- Method citation ≠ interpretation endorsement

**Example of correct separation**:
> "Data were processed using AUTO-DZ-ACT version 1.0.0. The output values were interpreted as [specific claim]. This interpretation is the responsibility of the authors and is not endorsed by the AUTO-DZ-ACT method itself."

---

## Mandatory Citation Separation

### Three-Part Citation Structure

All scientific outputs must separate:

#### 1. Method Citation

**What was used**:
- Name and version of method
- Role of method in analysis
- Reference to method documentation

**Example**:
```
Method: AUTO-DZ-ACT version 1.0.0
Purpose: Computational data processing
Reference: github.com/trizel-ai/trizel-AI
```

#### 2. Result Statement

**What was observed**:
- Raw outputs
- Computed values
- Observed patterns

**Example**:
```
Results: Processing yielded numerical outputs in the range [0.1, 0.9].
Observation: Pattern X was detected in dataset Y.
```

#### 3. Interpretation (if any)

**What is claimed**:
- Interpretation of results
- Theoretical framework applied
- Author's conclusions

**Example**:
```
Interpretation: Authors interpret these values as consistent with hypothesis Z.
Authority: This interpretation is the responsibility of the authors.
Caveat: Alternative interpretations may be equally valid.
```

### Separation Enforcement

**Requirement**: These three parts must be **explicitly separated** in:

- Published papers
- DOI metadata
- Snapshot documentation
- Website presentations
- External citations

**Violation**: Conflating method, result, and interpretation is a governance violation.

---

## Method Reference in DOI Metadata

### Required Metadata Fields

When submitting a snapshot for DOI issuance, the following method-related fields are **required**:

```yaml
method_reference: "AUTO-DZ-ACT"
method_version: "1.0.0"
method_role: "Data processing method"
method_citation: "[DOI or repository URL]"
```

### Prohibited Metadata

The following fields are **not allowed**:

```yaml
theory: "AUTO-DZ-ACT"  # ❌ AUTO-DZ-ACT is not a theory
model: "AUTO-DZ-ACT"   # ❌ AUTO-DZ-ACT is not a model
framework: "AUTO-DZ-ACT"  # ❌ AUTO-DZ-ACT is not a framework
```

### Method Description Guidelines

In DOI metadata or abstracts, method descriptions must:

**Do**:
- Describe computational procedure
- State what the method does
- Specify version and parameters
- Acknowledge limitations

**Don't**:
- Claim theoretical significance
- Assert explanatory power
- Imply validation of interpretations
- Use ambiguous language

**Example of compliant description**:
> "AUTO-DZ-ACT version 1.0.0 was used as a computational method for processing observational data. The method applies algorithm X to inputs Y, producing outputs Z. The method itself makes no theoretical claims; interpretation of outputs is the responsibility of the authors."

---

## Method Reference in Publications

### Citation Format

When citing AUTO-DZ-ACT in a publication:

**Option 1: Software citation**
```
[Software] AUTO-DZ-ACT (version 1.0.0). Available at: https://github.com/trizel-ai/trizel-AI
```

**Option 2: Method reference**
```
Data were processed using the AUTO-DZ-ACT computational method (version 1.0.0) [1].

[1] AUTO-DZ-ACT: [method description or DOI if available]
```

**Option 3: In-text reference**
```
Following the AUTO-DZ-ACT procedure (v1.0.0), we computed...
```

### Citation Context

AUTO-DZ-ACT must be cited in the **Methods** section, not:
- Introduction (as a theory)
- Results (as an explanation)
- Discussion (as interpretive authority)

**Correct placement**:
> **Methods**  
> Data processing was performed using AUTO-DZ-ACT version 1.0.0, a computational algorithm for [specific purpose]. The method is described in [reference].

**Incorrect placement**:
> **Introduction**  
> AUTO-DZ-ACT theory predicts...  
> *(Incorrect: AUTO-DZ-ACT is not a theory)*

> **Discussion**  
> These results validate AUTO-DZ-ACT.  
> *(Incorrect: Method is not validated by results)*

### Acknowledgment of Method Limitations

When citing AUTO-DZ-ACT, authors should acknowledge:

1. **Scope**: What the method does and does not do
2. **Limitations**: Known constraints or assumptions
3. **Interpretation independence**: Results require interpretation
4. **Alternative methods**: Other approaches exist

**Example acknowledgment**:
> "AUTO-DZ-ACT version 1.0.0 was used for data processing. This method performs [specific function] but does not provide theoretical interpretation. Alternative processing methods may yield different results. Interpretation of outputs is the sole responsibility of the authors."

---

## Prohibition of Theory Endorsement

### What is Prohibited

The following are **explicitly forbidden**:

#### 1. Theoretical Claims via Method Citation

**Prohibited**:
> "AUTO-DZ-ACT predicts phenomenon X."

**Why**: Methods don't predict; they compute.

**Correct**:
> "Using AUTO-DZ-ACT to process data Y, we observed output Z, which we interpret as consistent with phenomenon X."

#### 2. Explanatory Authority via Method

**Prohibited**:
> "AUTO-DZ-ACT explains the observed pattern."

**Why**: Methods don't explain; they process data.

**Correct**:
> "Data processed by AUTO-DZ-ACT revealed pattern P. We propose explanation E for this pattern."

#### 3. Validation Claims via Method

**Prohibited**:
> "Results validate AUTO-DZ-ACT theory."

**Why**: AUTO-DZ-ACT is not a theory; it's a method. Methods are tools, not hypotheses.

**Correct**:
> "Results from AUTO-DZ-ACT processing are consistent with our hypothesis H."

#### 4. Interpretive Bundling

**Prohibited**:
> "AUTO-DZ-ACT shows that..."

**Why**: Methods show outputs, not interpretations.

**Correct**:
> "AUTO-DZ-ACT processing yielded output O. We interpret this as indicating..."

---

## Prohibition of Interpretive Authority

### AUTO-DZ-ACT Has No Interpretive Authority

**Principle**: AUTO-DZ-ACT is a computational method. It has **no authority** to:

- Validate theories
- Endorse interpretations
- Determine correctness of claims
- Adjudicate between competing explanations

### Interpretation is the Author's Responsibility

**Rule**: All interpretation of AUTO-DZ-ACT outputs is the **sole responsibility** of the authors using the method.

**Required statement** (in publications):
> "Interpretation of AUTO-DZ-ACT outputs is the responsibility of the authors. The method itself makes no claims regarding the correctness or validity of any interpretation."

### Multiple Interpretations are Acceptable

**Principle**: The same AUTO-DZ-ACT output may admit multiple valid interpretations.

**Consequence**: Authors must acknowledge interpretive uncertainty.

**Example**:
> "AUTO-DZ-ACT processing yielded values in range R. We interpret this as consistent with hypothesis H1. However, alternative interpretations (H2, H3) may be equally valid. The method does not adjudicate between these interpretations."

---

## Layer-2 Presentation Rules

### Method References in Website/Presentations

When displaying method references on the TRIZEL website or other Layer-2 presentations:

#### Required Elements

1. **Method name**: AUTO-DZ-ACT
2. **Explicit role**: "Computational method" or "Data processing method"
3. **Version**: If applicable
4. **No theoretical claims**: No language suggesting explanatory power

#### Example Display

**Acceptable**:
```markdown
### Method

**AUTO-DZ-ACT** (version 1.0.0)  
*Role*: Computational data processing method  
*Reference*: [github.com/trizel-ai/trizel-AI]

This method processes observational data according to a defined algorithm.
It does not provide theoretical interpretation of results.
```

**Not acceptable**:
```markdown
### Theory

**AUTO-DZ-ACT Framework**  
Explains observed phenomena through [...]
*(Incorrect: AUTO-DZ-ACT is not a theory or framework)*
```

### Citation Display on Website

If citing a publication that used AUTO-DZ-ACT:

**Acceptable**:
```
[Publication Title]
Authors: [...]
Method: AUTO-DZ-ACT version X.Y.Z
DOI: [...]
```

**Not acceptable**:
```
[Publication Title]
Theory: AUTO-DZ-ACT
Validates: [theoretical claim]
*(Incorrect: conflates method with theory)*
```

---

## Compliance and Enforcement

### Pre-Publication Checklist

Before publishing any scientific output referencing AUTO-DZ-ACT:

- [ ] AUTO-DZ-ACT cited as method, not theory
- [ ] Version number included
- [ ] Role explicitly stated ("method", "procedure", "algorithm")
- [ ] No theoretical claims attributed to method
- [ ] Method, result, and interpretation separated
- [ ] Interpretation acknowledged as author's responsibility
- [ ] No interpretive authority claimed for method
- [ ] Limitations acknowledged
- [ ] Alternative interpretations acknowledged
- [ ] Compliant language used (no "AUTO-DZ-ACT theory", etc.)

### Governance Review

During DOI approval review, governance will verify:

1. **Method citation compliance**: Correct format and language
2. **Separation enforced**: Method vs. result vs. interpretation
3. **No theory claims**: No prohibited language or claims
4. **Interpretive transparency**: Author responsibility stated

**Violation = DOI request rejected**

### Violation Examples

The following would trigger DOI rejection:

**Example 1: Theory claim**
> "This research validates AUTO-DZ-ACT theory."

**Reason**: AUTO-DZ-ACT is not a theory

**Example 2: Interpretive authority**
> "AUTO-DZ-ACT proves that phenomenon X exists."

**Reason**: Method cannot prove; it processes data

**Example 3: Conflation**
> "AUTO-DZ-ACT results show..."

**Reason**: Conflates method with interpretation

**Example 4: Missing separation**
> [No distinction between method, result, and interpretation]

**Reason**: Mandatory separation not enforced

---

## Special Cases

### Case 1: Method Development Papers

If publishing a paper **about** AUTO-DZ-ACT itself (method development):

**Allowed**:
- Describe algorithm and implementation
- Evaluate computational performance
- Compare with other methods
- Discuss methodological limitations

**Not allowed**:
- Claim theoretical significance
- Assert explanatory power
- Make interpretive claims about what outputs "mean"

### Case 2: Method Comparison

If comparing AUTO-DZ-ACT with other methods:

**Allowed**:
- Compare computational efficiency
- Compare output characteristics
- Discuss methodological tradeoffs

**Not allowed**:
- Claim one method is "theoretically superior"
- Assert one method "validates" a theory while another doesn't

### Case 3: Historical References

If referring to deprecated terminology (e.g., "STOE"):

**Required**:
- Use only as historical non-operational reference
- Do not cite as current method
- Clearly mark as deprecated
- Refer to current AUTO-DZ-ACT method

**Example**:
> "Historically, this procedure was referred to as 'STOE' (deprecated). Current versions use the AUTO-DZ-ACT designation. This document refers exclusively to AUTO-DZ-ACT as a computational method."

---

## Related Documents

- `governance/DOI_ISSUANCE_POLICY.md` — DOI governance framework
- `governance/SNAPSHOT_CONTRACT.md` — Snapshot immutability requirements
- `governance/LAYER1_GOVERNANCE_DECLARATION.md` — AUTO-DZ-ACT status
- `DEPRECATED_TERMS.md` — Forbidden terminology
- `PUBLICATION_POLICY.md` — Website publication rules

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-21 | Initial Method Reference Rules (Phase-F) |

---

**Effective Immediately**  
**Authority**: TRIZEL Layer-0 Governance  
**Status**: Active
