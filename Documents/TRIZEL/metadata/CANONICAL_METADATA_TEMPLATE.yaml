# CANONICAL_METADATA_TEMPLATE.yaml
# TRIZEL Canonical Metadata Template — Source of Truth
#
# Repository: trizel-ai/trizel-core
# Layer: 0 — Governance & Charter
# Template Version: 1.0.0
# Last Updated: 2026-01-12
# Status: Canonical, Non-Executable, Archival
#
# Purpose:
# This template provides the canonical structure for TRIZEL metadata across
# all repositories. It defines the authoritative schema for governance,
# provenance, multilingual content, and epistemic layer assignments.
#
# Usage:
# - Read-only reference for metadata structure
# - Source of truth for schema definition
# - Non-executable: contains no logic, only structure
# - Immutable: changes require governance approval and versioning
#
# Compliance:
# - No deprecated terminology (see ../../DEPRECATED_TERMS.md)
# - No executable logic or scripts
# - No sensitive data or credentials
# - Governance metadata only

# Metadata Schema Version
schema_version: "1.0.0"

# Governance Metadata
governance:
  template_status: "canonical"
  layer: 0
  repository: "trizel-ai/trizel-core"
  effective_date: "2026-01-12T13:00:00Z"
  immutable: true
  non_executable: true
  archival_ready: true

# Repository Metadata Structure
repository_metadata:
  # Basic repository identification
  repository: "owner/repository-name"
  layer: 0  # Integer 0-6
  status: "active"  # active | archived | draft | deprecated
  canonical: true  # true | false
  role: "governance_charter"  # See role vocabulary below
  
  # Version and provenance
  metadata_version: "1.0.0"
  last_updated: "2026-01-12T13:00:00Z"
  source_commit: "abc123def456"  # Git commit SHA
  
  # Publication control
  publishable: true  # true | false
  public_visibility: true  # true | false
  
  # Multilingual metadata (i18n)
  i18n:
    en:
      title: "Repository Title in English"
      description: "One-line description in English (max 200 chars)"
      keywords:
        - "keyword1"
        - "keyword2"
        - "keyword3"
    
    fr:
      title: "Titre du référentiel en français"
      description: "Description d'une ligne en français (max 200 caractères)"
      keywords:
        - "mot-clé1"
        - "mot-clé2"
        - "mot-clé3"
    
    ar:
      title: "عنوان المستودع بالعربية"
      description: "وصف من سطر واحد بالعربية (الحد الأقصى 200 حرف)"
      keywords:
        - "كلمة_مفتاحية1"
        - "كلمة_مفتاحية2"
        - "كلمة_مفتاحية3"
    
    zh:
      title: "中文存储库标题"
      description: "中文单行描述（最多200个字符）"
      keywords:
        - "关键词1"
        - "关键词2"
        - "关键词3"

# Role Vocabulary (Layer-specific)
role_vocabulary:
  layer_0:
    - "governance_charter"
    - "policy_definition"
    - "epistemic_control"
  
  layer_1:
    - "algorithm_definition"
    - "method_specification"
  
  layer_2:
    - "data_observation"
    - "monitoring_observation"
    - "sensor_data"
  
  layer_3:
    - "analysis_inference"
    - "model_development"
    - "statistical_analysis"
  
  layer_4:
    - "evaluation_gateway"
    - "validation_checkpoint"
    - "tcrl_boundary"
  
  layer_5:
    - "interpretation_synthesis"
    - "knowledge_integration"
  
  layer_6:
    - "website_orchestration"
    - "visualization_publication"
    - "public_interface"

# Status Vocabulary
status_vocabulary:
  - "active"       # Currently maintained and operational
  - "archived"     # No longer active but preserved
  - "draft"        # Under development, not public
  - "deprecated"   # Superseded or no longer recommended

# Character Limits
character_limits:
  title_max: 100
  description_max: 200
  keyword_max: 50
  role_max: 50

# Required Fields
required_fields:
  - "repository"
  - "layer"
  - "status"
  - "canonical"
  - "role"
  - "i18n.en.title"
  - "i18n.en.description"
  - "i18n.fr.title"
  - "i18n.fr.description"
  - "i18n.ar.title"
  - "i18n.ar.description"

# Optional Fields
optional_fields:
  - "i18n.zh"  # Chinese support is planned
  - "metadata_version"
  - "source_commit"
  - "keywords"
  - "pending_branches"
  - "external_references"

# Provenance Tracking
provenance:
  source_repository: "trizel-ai/trizel-core"
  source_file: "Documents/TRIZEL/metadata/CANONICAL_METADATA_TEMPLATE.yaml"
  template_version: "1.0.0"
  schema_authority: "TRIZEL Layer 0 Governance"
  
# Validation Rules
validation_rules:
  layer:
    type: "integer"
    minimum: 0
    maximum: 6
  
  status:
    type: "enum"
    allowed_values:
      - "active"
      - "archived"
      - "draft"
      - "deprecated"
  
  canonical:
    type: "boolean"
  
  title:
    type: "string"
    max_length: 100
    required: true
  
  description:
    type: "string"
    max_length: 200
    required: true
  
  repository:
    type: "string"
    pattern: "^[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+$"
    required: true

# Deprecated Terms (Absolute Prohibition)
deprecated_terms:
  forbidden:
    - "STOE"
    - "V12"
    - "V13"
    - "V14"
    - "V15"
    - "V16"
    - "V17"
    - "V18"
    - "V19"
    - "V20"
    - "V21"
    - "V22"
  
  enforcement: "fail_build"
  scope: "all_fields"
  action: "reject_immediately"

# Immutability and Versioning
versioning:
  template_version: "1.0.0"
  change_policy: "governance_approval_required"
  breaking_changes: "major_version_increment"
  additive_changes: "minor_version_increment"
  
# Archive and Long-term Preservation
archival:
  format: "YAML 1.2"
  encoding: "UTF-8"
  preservation_level: "archival"
  digital_signature: false  # Reserved for future use
  checksum_algorithm: "SHA-256"  # Reserved for future use
  
# License and Usage
license:
  type: "MIT"
  scope: "template_structure_only"
  applies_to: "schema_definition"
  does_not_apply_to: "content_interpretations"

# Contact and Governance
governance_contact:
  repository: "trizel-ai/trizel-core"
  issues_url: "https://github.com/trizel-ai/trizel-core/issues"
  governance_layer: 0
  authority: "TRIZEL Epistemic Constitution"

---
# END OF CANONICAL METADATA TEMPLATE
# Version: 1.0.0
# Status: Canonical, Non-Executable, Archival-Ready
# Last Updated: 2026-01-12
