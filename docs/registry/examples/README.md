# TRIZEL Registry Examples

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Document Version**: 1.0.0  
**Last Updated**: 2026-01-12

---

## Purpose

This directory contains **non-executable, static reference examples** showing how Layer 6 (website) repositories should consume the TRIZEL registry.

**IMPORTANT**: These files are **documentation only**. They contain **no executable code** and must not be run or imported.

---

## Files in This Directory

### `registry-consumption-example.yaml`

**Purpose**: Static reference example of how a Layer 6 website might structure its allowlist configuration.

**Content**:
- Allowlist configuration structure
- Validation settings
- Deprecated terms list
- Build process pseudocode (non-executable)
- Provenance tracking example

**Usage**: Read this file to understand the structure of allowlist-based validation. Do not execute or import.

**Layer Boundary**: This example belongs in Layer 0 for documentation. Actual implementation belongs in Layer 6.

---

### `registry-consumption-example.json.txt`

**Purpose**: Static reference example showing the structure of registry data after YAML-to-JSON conversion. File extension is `.json.txt` to clearly indicate this is a documentation example, not actual data.

**Content**:
- Converted registry metadata
- Repository entries in JSON format
- Example display structure
- Usage notes
- Conversion notes

**Usage**: Reference this file to understand the JSON structure after conversion. Do not use as actual data source.

**Layer Boundary**: This example belongs in Layer 0 for documentation. Actual conversion and JSON generation belong in Layer 6.

---

## How to Use These Examples

### For Layer 6 Website Developers

1. **Read** the examples to understand the structure and requirements
2. **Do not copy** these files directly into your Layer 6 repository
3. **Implement** your own allowlist configuration based on the example structure
4. **Follow** the validation rules and fail-closed behavior shown in the examples
5. **Ensure** your implementation fetches from the canonical source only

### Allowlist-Only Consumption

The examples demonstrate:
- Explicit source approval (trizel-ai/trizel-core only)
- No auto-discovery of repositories
- Fail-closed validation behavior
- Deprecated terms checking
- Multilingual support requirements
- Provenance tracking

### Non-Interpretive Display

The examples show:
- Displaying only approved metadata fields
- No analytical commentary
- No interpretive claims
- Factual presentation only

---

## What These Examples Are NOT

**NOT executable code**: These files contain pseudocode and reference structures only. They cannot and should not be executed.

**NOT actual configuration**: These are examples for reference. Your Layer 6 repository should implement its own configuration.

**NOT data sources**: Do not use these examples as data sources. Always fetch from the canonical `TRIZEL_REGISTRY.yaml`.

**NOT Layer 6 content**: These examples are Layer 0 governance documentation. Implementation belongs in Layer 6.

---

## Implementation Checklist

When implementing registry consumption in Layer 6, ensure:

- [ ] Fetch registry from approved source only: `trizel-ai/trizel-core/docs/registry/TRIZEL_REGISTRY.yaml`
- [ ] Validate schema version compatibility
- [ ] Check for deprecated terminology (see `../../DEPRECATED_TERMS.md`)
- [ ] Verify all required metadata fields present
- [ ] Ensure fail-closed validation (halt build on errors)
- [ ] Support all three languages (en, fr, ar)
- [ ] Implement RTL support for Arabic
- [ ] Display provenance metadata
- [ ] Use allowlist-only ingestion (no auto-discovery)
- [ ] Display content non-interpretively (no added commentary)

---

## Terminology Standards

### Required Algorithm Name

**Use only**: "AUTO DZ ACT" (exact spelling)

### Forbidden Terms

See `../../DEPRECATED_TERMS.md` for the complete canonical list of forbidden terminology.

---

## Layer Boundary Compliance

### These Examples (Layer 0)

**Allowed**:
- Static reference documentation
- Example structures (non-executable)
- Pseudocode for illustration
- Governance rules and requirements

**Forbidden**:
- Executable code or scripts
- Actual website implementation
- Build automation
- Analysis or interpretation

### Your Implementation (Layer 6)

**Allowed**:
- Website code (HTML, CSS, JavaScript, etc.)
- Build scripts and automation
- YAML-to-JSON conversion logic
- User interface components
- Multilingual rendering

**Forbidden**:
- Raw data ingestion or display
- Analysis or computational logic
- Interpretive commentary
- Auto-discovery of repositories
- Non-approved source consumption

---

## Questions or Issues

For questions about these examples:

1. Review `website-consumption.md` in the parent directory
2. Review `layer-boundaries.md` for Layer 0 vs Layer 6 definitions
3. Check `SCHEMA.md` for registry structure
4. Consult `../../PUBLICATION_POLICY.md` for publication rules
5. Open an issue in `trizel-ai/trizel-core` if clarification needed

**Do not**:
- Attempt to execute these examples
- Use these as actual data sources
- Implement Layer 6 code in Layer 0
- Bypass validation rules shown in examples

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-12 | Initial examples directory with YAML and JSON reference files |

---

## Related Documents

- `../website-consumption.md` — Layer 6 consumption guidelines
- `../layer-boundaries.md` — Layer 0 vs Layer 6 boundaries
- `../TRIZEL_REGISTRY.yaml` — Canonical registry (actual source)
- `../SCHEMA.md` — Registry schema definition
- `../../PUBLICATION_POLICY.md` — Publication rules
- `../../DEPRECATED_TERMS.md` — Forbidden terminology
