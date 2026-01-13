{
  "_comment": "CANONICAL_METADATA_TEMPLATE.json",
  "_description": "TRIZEL Canonical Metadata Template — Consumer Mirror (JSON)",
  "_metadata": {
    "repository": "trizel-ai/trizel-core",
    "layer": 0,
    "template_version": "1.0.0",
    "last_updated": "2026-01-12T13:00:00Z",
    "status": "canonical",
    "non_executable": true,
    "archival_ready": true,
    "source_file": "CANONICAL_METADATA_TEMPLATE.yaml",
    "purpose": "JSON mirror of canonical YAML template for consumer compatibility"
  },
  "schema_version": "1.0.0",
  "governance": {
    "template_status": "canonical",
    "layer": 0,
    "repository": "trizel-ai/trizel-core",
    "effective_date": "2026-01-12T13:00:00Z",
    "immutable": true,
    "non_executable": true,
    "archival_ready": true
  },
  "repository_metadata": {
    "repository": "owner/repository-name",
    "layer": 0,
    "status": "active",
    "canonical": true,
    "role": "governance_charter",
    "metadata_version": "1.0.0",
    "last_updated": "2026-01-12T13:00:00Z",
    "source_commit": "abc123def456",
    "publishable": true,
    "public_visibility": true,
    "i18n": {
      "en": {
        "title": "Repository Title in English",
        "description": "One-line description in English (max 200 chars)",
        "keywords": [
          "keyword1",
          "keyword2",
          "keyword3"
        ]
      },
      "fr": {
        "title": "Titre du référentiel en français",
        "description": "Description d'une ligne en français (max 200 caractères)",
        "keywords": [
          "mot-clé1",
          "mot-clé2",
          "mot-clé3"
        ]
      },
      "ar": {
        "title": "عنوان المستودع بالعربية",
        "description": "وصف من سطر واحد بالعربية (الحد الأقصى 200 حرف)",
        "keywords": [
          "كلمة_مفتاحية1",
          "كلمة_مفتاحية2",
          "كلمة_مفتاحية3"
        ]
      },
      "zh": {
        "title": "中文存储库标题",
        "description": "中文单行描述（最多200个字符）",
        "keywords": [
          "关键词1",
          "关键词2",
          "关键词3"
        ]
      }
    }
  },
  "role_vocabulary": {
    "layer_0": [
      "governance_charter",
      "policy_definition",
      "epistemic_control"
    ],
    "layer_1": [
      "algorithm_definition",
      "method_specification"
    ],
    "layer_2": [
      "data_observation",
      "monitoring_observation",
      "sensor_data"
    ],
    "layer_3": [
      "analysis_inference",
      "model_development",
      "statistical_analysis"
    ],
    "layer_4": [
      "evaluation_gateway",
      "validation_checkpoint",
      "tcrl_boundary"
    ],
    "layer_5": [
      "interpretation_synthesis",
      "knowledge_integration"
    ],
    "layer_6": [
      "website_orchestration",
      "visualization_publication",
      "public_interface"
    ]
  },
  "status_vocabulary": [
    "active",
    "archived",
    "draft",
    "deprecated"
  ],
  "character_limits": {
    "title_max": 100,
    "description_max": 200,
    "keyword_max": 50,
    "role_max": 50
  },
  "required_fields": [
    "repository",
    "layer",
    "status",
    "canonical",
    "role",
    "i18n.en.title",
    "i18n.en.description",
    "i18n.fr.title",
    "i18n.fr.description",
    "i18n.ar.title",
    "i18n.ar.description"
  ],
  "optional_fields": [
    "i18n.zh",
    "metadata_version",
    "source_commit",
    "keywords",
    "pending_branches",
    "external_references"
  ],
  "provenance": {
    "source_repository": "trizel-ai/trizel-core",
    "source_file": "Documents/TRIZEL/metadata/CANONICAL_METADATA_TEMPLATE.json",
    "template_version": "1.0.0",
    "schema_authority": "TRIZEL Layer 0 Governance"
  },
  "validation_rules": {
    "layer": {
      "type": "integer",
      "minimum": 0,
      "maximum": 6
    },
    "status": {
      "type": "enum",
      "allowed_values": [
        "active",
        "archived",
        "draft",
        "deprecated"
      ]
    },
    "canonical": {
      "type": "boolean"
    },
    "title": {
      "type": "string",
      "max_length": 100,
      "required": true
    },
    "description": {
      "type": "string",
      "max_length": 200,
      "required": true
    },
    "repository": {
      "type": "string",
      "pattern": "^[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+$",
      "required": true
    }
  },
  "deprecated_terms": {
    "forbidden": [
      "STOE",
      "V12",
      "V13",
      "V14",
      "V15",
      "V16",
      "V17",
      "V18",
      "V19",
      "V20",
      "V21",
      "V22"
    ],
    "enforcement": "fail_build",
    "scope": "all_fields",
    "action": "reject_immediately"
  },
  "versioning": {
    "template_version": "1.0.0",
    "change_policy": "governance_approval_required",
    "breaking_changes": "major_version_increment",
    "additive_changes": "minor_version_increment"
  },
  "archival": {
    "format": "JSON",
    "encoding": "UTF-8",
    "preservation_level": "archival",
    "digital_signature": false,
    "checksum_algorithm": "SHA-256"
  },
  "license": {
    "type": "MIT",
    "scope": "template_structure_only",
    "applies_to": "schema_definition",
    "does_not_apply_to": "content_interpretations"
  },
  "governance_contact": {
    "repository": "trizel-ai/trizel-core",
    "issues_url": "https://github.com/trizel-ai/trizel-core/issues",
    "governance_layer": 0,
    "authority": "TRIZEL Epistemic Constitution"
  }
}
