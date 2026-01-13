# TRIZEL Canonical Metadata Templates

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Version**: 1.0.0  
**Last Updated**: 2026-01-12  
**Status**: Canonical, Non-Executable, Archival

---

## Purpose

This directory contains the **canonical metadata templates** for the TRIZEL ecosystem. These templates define the authoritative structure for all metadata across TRIZEL repositories, ensuring consistency, interoperability, and long-term preservation.

---

## Files in This Directory

### 1. CANONICAL_METADATA_TEMPLATE.yaml

**Source of Truth**

The YAML template is the **primary canonical source** for TRIZEL metadata schema definition.

- **Format**: YAML 1.2
- **Encoding**: UTF-8
- **Status**: Canonical, read-only reference
- **Purpose**: Define authoritative metadata structure

**Use this file when**:
- Defining metadata schema
- Validating metadata structure
- Creating new repository metadata
- Understanding governance requirements

### 2. CANONICAL_METADATA_TEMPLATE.json

**Consumer Mirror**

The JSON template is a **consumer-compatible mirror** of the YAML source for systems that prefer JSON.

- **Format**: JSON
- **Encoding**: UTF-8
- **Status**: Derived from YAML source
- **Purpose**: Enable JSON-based consumers

**Use this file when**:
- Integrating with JSON-based systems
- Building web applications
- Creating programmatic validators
- Consuming metadata in JSON format

**Important**: Both files contain the same canonical structure. The YAML file is authoritative; JSON is a convenience mirror.

---

## Governance and Immutability

### Template Status

These templates are **canonical governance documents** under Layer 0 authority.

- **Canonical**: Defines structural rules for the ecosystem
- **Immutable**: Changes require formal governance approval
- **Non-Executable**: Contains no logic, scripts, or code
- **Archival-Ready**: Designed for long-term preservation

### Change Policy

**Minor Changes** (e.g., adding optional fields):
- Increment minor version (1.0.0 → 1.1.0)
- Must maintain backward compatibility
- Require governance review and approval

**Major Changes** (e.g., changing required fields):
- Increment major version (1.0.0 → 2.0.0)
- May break backward compatibility
- Require ecosystem-wide coordination
- Must include migration guide

**Prohibited Changes**:
- Removing required fields without major version
- Adding deprecated terminology
- Making templates executable
- Compromising archival integrity

---

## Usage Guidelines

### For Repository Maintainers

**Creating Metadata for Your Repository**:

1. Copy the appropriate template (YAML or JSON)
2. Fill in your repository-specific values
3. Ensure all required fields are present
4. Validate against character limits
5. Check for deprecated terminology
6. Provide multilingual translations (EN, FR, AR minimum; ZH planned)
7. Set appropriate layer assignment (0-6)
8. Mark canonical status accurately

**Required Fields**:
- `repository`: Full GitHub path (owner/name)
- `layer`: Integer 0-6
- `status`: active | archived | draft | deprecated
- `canonical`: true | false
- `role`: From role vocabulary
- `i18n.en.title`: English title (≤100 chars)
- `i18n.en.description`: English description (≤200 chars)
- `i18n.fr.title`: French title (≤100 chars)
- `i18n.fr.description`: French description (≤200 chars)
- `i18n.ar.title`: Arabic title (≤100 chars)
- `i18n.ar.description`: Arabic description (≤200 chars)

### For Website Developers

**Consuming Metadata**:

1. Fetch metadata from canonical repository
2. Validate against template schema
3. Check for deprecated terms
4. Enforce character limits
5. Support all required languages (EN, FR, AR)
6. Display provenance information
7. Use fail-closed validation (reject invalid data)
8. Implement allowlist-only ingestion

**Example Integration** (pseudocode):

```python
import yaml

# Load template for validation
with open('CANONICAL_METADATA_TEMPLATE.yaml') as f:
    template = yaml.safe_load(f)

# Validate repository metadata
def validate_metadata(metadata):
    # Check required fields
    for field in template['required_fields']:
        if not has_field(metadata, field):
            raise ValueError(f"Missing required field: {field}")
    
    # Check deprecated terms
    for term in template['deprecated_terms']['forbidden']:
        if term in str(metadata):
            raise ValueError(f"Deprecated term found: {term}")
    
    # Validate character limits
    if len(metadata['i18n']['en']['title']) > 100:
        raise ValueError("Title exceeds 100 character limit")
    
    return True
```

### For Validators and CI/CD

**Automated Validation**:

1. Parse template to extract validation rules
2. Apply rules to repository metadata
3. Check for completeness (all required fields)
4. Verify character limits
5. Scan for deprecated terms
6. Validate i18n completeness
7. Fail build on any violation

---

## Metadata Structure

### Layer Assignment (0-6)

**Layer 0**: Governance & Charter
- Defines rules and boundaries
- Contains policy and standards
- Example: `trizel-core`

**Layer 1**: Algorithm Definition
- Canonical algorithm specifications
- Method definitions
- Example: `Auto-dz-act`

**Layer 2**: Data & Observation
- Raw data collection
- Monitoring and sensors
- Example: `trizel-monitor`

**Layer 3**: Analysis & Inference
- Data processing
- Statistical analysis
- Model development

**Layer 4**: Evaluation Gateway
- Validation checkpoints
- TCRL boundary interface
- Example: `trizel-phase4-gateway`

**Layer 5**: Interpretation & Synthesis
- Knowledge integration
- Cross-domain synthesis

**Layer 6**: Website & Orchestration
- Public visualization
- Website publication
- Example: `trizel-AI` (Layer 6 website)

### Multilingual Support (i18n)

**Required Languages**:
- **EN** (English): Full support, required
- **FR** (French): Full support, required
- **AR** (Arabic): Full support with RTL, required

**Planned Languages**:
- **ZH** (Chinese): Explicitly planned, currently optional

Each language must include:
- `title`: Repository title (≤100 chars)
- `description`: One-line description (≤200 chars)
- `keywords`: Optional list of keywords

**RTL Support**:
- Arabic text requires right-to-left rendering
- Website implementations must support RTL layout
- Test thoroughly with Arabic content

### Role Vocabulary

Roles are **layer-specific** and **non-overlapping**:

**Layer 0 Roles**:
- `governance_charter`
- `policy_definition`
- `epistemic_control`

**Layer 1 Roles**:
- `algorithm_definition`
- `method_specification`

**Layer 2 Roles**:
- `data_observation`
- `monitoring_observation`
- `sensor_data`

**Layer 3 Roles**:
- `analysis_inference`
- `model_development`
- `statistical_analysis`

**Layer 4 Roles**:
- `evaluation_gateway`
- `validation_checkpoint`
- `tcrl_boundary`

**Layer 5 Roles**:
- `interpretation_synthesis`
- `knowledge_integration`

**Layer 6 Roles**:
- `website_orchestration`
- `visualization_publication`
- `public_interface`

---

## Validation Rules

### Character Limits

- **Title**: Maximum 100 characters
- **Description**: Maximum 200 characters
- **Keywords**: Maximum 50 characters each
- **Role**: Maximum 50 characters

### Data Types

- `layer`: Integer between 0 and 6 (inclusive)
- `canonical`: Boolean (true/false)
- `publishable`: Boolean (true/false)
- `status`: Enum (active, archived, draft, deprecated)

### Pattern Validation

- `repository`: Must match pattern `owner/repository-name`
- No spaces or special characters except hyphen and underscore

---

## Deprecated Terms (Absolute Prohibition)

The following legacy placeholders are **permanently forbidden** in all metadata:

- **DEPRECATED_TERM_PLACEHOLDER**
- **VERSION_LABEL_PLACEHOLDER_RANGE**
- Any theoretical lineage references
- Any versioned system labels

**Enforcement**: Automated CI checks must scan all metadata and **fail builds** if deprecated terms are detected.

**Action**: If found, remove immediately and reject the metadata.

See `../../DEPRECATED_TERMS.md` for complete list and enforcement rules.

**Enforcement**: Automated CI checks must scan all metadata and **fail builds** if deprecated terms are detected.

**Action**: If found, remove immediately and reject the metadata.

See `../../DEPRECATED_TERMS.md` for complete list and enforcement rules.

---

## Archival and Preservation

These templates are designed for **long-term archival** and **institutional preservation**.

### Archival Properties

- **Format**: Standards-compliant YAML 1.2 and JSON
- **Encoding**: UTF-8 (universal compatibility)
- **Structure**: Human-readable and machine-parseable
- **Versioning**: Explicit version tracking
- **Provenance**: Complete source attribution

### Digital Preservation

**Reserved for Future Use**:
- Digital signatures (planned)
- Checksum verification (SHA-256)
- Cryptographic attestation
- Immutable timestamp anchoring

---

## Integration Examples

### Example 1: Python Validation

```python
import yaml
import re

def validate_trizel_metadata(metadata_file):
    """Validate repository metadata against canonical template."""
    
    # Load metadata
    with open(metadata_file) as f:
        metadata = yaml.safe_load(f)
    
    # Check required fields
    required = [
        'repository', 'layer', 'status', 'canonical', 'role',
        'i18n.en.title', 'i18n.en.description',
        'i18n.fr.title', 'i18n.fr.description',
        'i18n.ar.title', 'i18n.ar.description'
    ]
    
    for field in required:
        if not get_nested_field(metadata, field):
            raise ValueError(f"Missing required field: {field}")
    
    # Validate layer range
    if not (0 <= metadata['layer'] <= 6):
        raise ValueError("Layer must be between 0 and 6")
    
    # Check character limits
    if len(metadata['i18n']['en']['title']) > 100:
        raise ValueError("English title exceeds 100 characters")
    
    if len(metadata['i18n']['en']['description']) > 200:
        raise ValueError("English description exceeds 200 characters")
    
    # Check for deprecated terms
    forbidden = ['STOE', 'V12', 'V13', 'V14', 'V15', 'V16', 
                 'V17', 'V18', 'V19', 'V20', 'V21', 'V22']
    
    metadata_str = str(metadata)
    for term in forbidden:
        if term in metadata_str:
            raise ValueError(f"Deprecated term found: {term}")
    
    # Validate repository pattern
    if not re.match(r'^[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+$', metadata['repository']):
        raise ValueError("Invalid repository format")
    
    return True
```

### Example 2: JavaScript/TypeScript Consumer

```typescript
interface TrizelMetadata {
  repository: string;
  layer: number;
  status: 'active' | 'archived' | 'draft' | 'deprecated';
  canonical: boolean;
  role: string;
  i18n: {
    en: { title: string; description: string };
    fr: { title: string; description: string };
    ar: { title: string; description: string };
    zh?: { title: string; description: string };
  };
}

function validateMetadata(metadata: TrizelMetadata): boolean {
  // Validate required fields
  if (!metadata.repository || !metadata.layer) {
    throw new Error('Missing required fields');
  }
  
  // Validate layer range
  if (metadata.layer < 0 || metadata.layer > 6) {
    throw new Error('Layer must be between 0 and 6');
  }
  
  // Validate character limits
  if (metadata.i18n.en.title.length > 100) {
    throw new Error('Title exceeds 100 character limit');
  }
  
  // Check deprecated terms
  const forbidden = ['STOE', /V(12|13|14|15|16|17|18|19|20|21|22)/];
  const metadataStr = JSON.stringify(metadata);
  
  for (const term of forbidden) {
    if (typeof term === 'string' && metadataStr.includes(term)) {
      throw new Error(`Deprecated term found: ${term}`);
    } else if (term instanceof RegExp && term.test(metadataStr)) {
      throw new Error('Deprecated version label found');
    }
  }
  
  return true;
}
```

---

## Compliance Checklist

For all metadata implementations:

- [ ] All required fields present
- [ ] Character limits respected
- [ ] Layer assignment valid (0-6)
- [ ] Role matches layer vocabulary
- [ ] Multilingual support complete (EN, FR, AR minimum)
- [ ] No deprecated terminology
- [ ] Repository pattern valid
- [ ] Status value valid
- [ ] Canonical flag accurate
- [ ] Provenance information included

---

## Version History

| Version | Date       | Changes                                  |
|---------|------------|------------------------------------------|
| 1.0.0   | 2026-01-12 | Initial canonical metadata templates    |

---

## Related Documents

- `TRIZEL_REGISTRY.yaml` — Canonical project registry (../../docs/registry/)
- `DEPRECATED_TERMS.md` — Forbidden terminology list (../../)
- `PUBLICATION_POLICY.md` — Publication guidelines (../../)
- `ROLE.md` — Repository layer assignments (../../)

---

## Questions and Support

For questions about metadata templates:

1. Review this README and template files
2. Check TRIZEL governance documentation
3. Open an issue in `trizel-ai/trizel-core`
4. Reference Layer 0 governance authority

**Do not**:
- Modify templates without governance approval
- Add deprecated terminology
- Remove required fields
- Make templates executable
- Bypass validation rules

---

## License

These templates are provided under the MIT License (see repository LICENSE file).

The license applies to the **template structure only**, not to scientific interpretations or derived content.

---

**TRIZEL — Technology for Research, Inference, Zonal Evaluation & Learning**  
Canonical Governance & Charter Repository  
Layer 0 — Non-Executable, Archival, Governance Metadata
