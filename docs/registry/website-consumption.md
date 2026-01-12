# Website Consumption Guidelines for TRIZEL Registry

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Document Version**: 1.0.0  
**Last Updated**: 2026-01-12

---

## Purpose / Objectif / الغرض

**EN**: This document defines how Layer 6 (website) repositories may consume allowlisted artifacts from the TRIZEL governance repository, including allowlist rules, provenance requirements, and non-interpretive display constraints.

**FR**: Ce document définit comment les référentiels de la couche 6 (site Web) peuvent consommer des artefacts de la liste blanche du référentiel de gouvernance TRIZEL, y compris les règles de liste blanche, les exigences de provenance et les contraintes d'affichage non interprétatives.

**AR**: تحدد هذه الوثيقة كيف يمكن لمستودعات الطبقة 6 (موقع الويب) استهلاك القطع الأثرية من القائمة البيضاء من مستودع حوكمة TRIZEL، بما في ذلك قواعد القائمة البيضاء ومتطلبات المصدر وقيود العرض غير التفسيري.

---

## Core Principle / Principe fondamental / المبدأ الأساسي

### EN: Allowlist-Only, Fail-Closed, Non-Interpretive

The website must operate under three mandatory principles:

1. **Allowlist-Only Ingestion**: Only consume content from explicitly approved sources
2. **Fail-Closed Validation**: Halt build immediately if any validation fails
3. **Non-Interpretive Display**: Present factual metadata only, no analysis or interpretation

### FR: Liste blanche uniquement, échec fermé, non interprétatif

Le site Web doit fonctionner selon trois principes obligatoires :

1. **Ingestion de liste blanche uniquement** : Consommer uniquement du contenu provenant de sources explicitement approuvées
2. **Validation à échec fermé** : Arrêter immédiatement la construction si une validation échoue
3. **Affichage non interprétatif** : Présenter uniquement des métadonnées factuelles, sans analyse ni interprétation

### AR: القائمة البيضاء فقط، فشل مغلق، غير تفسيري

يجب أن يعمل الموقع وفقًا لثلاثة مبادئ إلزامية:

1. **استيعاب القائمة البيضاء فقط**: استهلاك المحتوى من مصادر معتمدة صراحة فقط
2. **التحقق من الفشل المغلق**: إيقاف البناء فورًا في حالة فشل أي تحقق
3. **العرض غير التفسيري**: عرض البيانات الوصفية الواقعية فقط، بدون تحليل أو تفسير

---

## Approved Source / Source approuvée / المصدر المعتمد

### EN: Canonical Registry Location

**Approved source**:
- Repository: `trizel-ai/trizel-core`
- File path: `docs/registry/TRIZEL_REGISTRY.yaml`
- Schema version: `1.0.0`
- Publishable flag: `true` (verified in registry metadata)

**Fetching method**:
```
https://raw.githubusercontent.com/trizel-ai/trizel-core/main/docs/registry/TRIZEL_REGISTRY.yaml
```

**Version pinning** (recommended):
```
https://raw.githubusercontent.com/trizel-ai/trizel-core/<commit-sha>/docs/registry/TRIZEL_REGISTRY.yaml
```

### FR: Emplacement du registre canonique

**Source approuvée** :
- Référentiel : `trizel-ai/trizel-core`
- Chemin du fichier : `docs/registry/TRIZEL_REGISTRY.yaml`
- Version du schéma : `1.0.0`
- Indicateur publiable : `true` (vérifié dans les métadonnées du registre)

**Méthode de récupération** :
```
https://raw.githubusercontent.com/trizel-ai/trizel-core/main/docs/registry/TRIZEL_REGISTRY.yaml
```

**Épinglage de version** (recommandé) :
```
https://raw.githubusercontent.com/trizel-ai/trizel-core/<commit-sha>/docs/registry/TRIZEL_REGISTRY.yaml
```

### AR: موقع السجل القانوني

**المصدر المعتمد**:
- المستودع: `trizel-ai/trizel-core`
- مسار الملف: `docs/registry/TRIZEL_REGISTRY.yaml`
- إصدار المخطط: `1.0.0`
- علامة قابلة للنشر: `true` (تم التحقق منها في بيانات السجل الوصفية)

**طريقة الجلب**:
```
https://raw.githubusercontent.com/trizel-ai/trizel-core/main/docs/registry/TRIZEL_REGISTRY.yaml
```

**تثبيت الإصدار** (موصى به):
```
https://raw.githubusercontent.com/trizel-ai/trizel-core/<commit-sha>/docs/registry/TRIZEL_REGISTRY.yaml
```

---

## Allowlist Rules / Règles de liste blanche / قواعد القائمة البيضاء

### EN: Strict Source Validation

**MUST validate**:
1. Source repository is `trizel-ai/trizel-core`
2. File path is exactly `docs/registry/TRIZEL_REGISTRY.yaml`
3. Schema version matches website compatibility (currently `1.0.0`)
4. `registry_metadata.publishable` field is `true`

**MUST reject if**:
- Source is from any other repository
- File path is different
- Schema version is incompatible
- Publishable flag is missing or `false`
- YAML syntax is invalid
- Required metadata fields are missing

**Behavior on rejection**: Halt build immediately, log specific error, require manual fix before deployment.

### FR: Validation stricte de la source

**DOIT valider** :
1. Le référentiel source est `trizel-ai/trizel-core`
2. Le chemin du fichier est exactement `docs/registry/TRIZEL_REGISTRY.yaml`
3. La version du schéma correspond à la compatibilité du site Web (actuellement `1.0.0`)
4. Le champ `registry_metadata.publishable` est `true`

**DOIT rejeter si** :
- La source provient d'un autre référentiel
- Le chemin du fichier est différent
- La version du schéma est incompatible
- L'indicateur publiable est manquant ou `false`
- La syntaxe YAML n'est pas valide
- Les champs de métadonnées requis sont manquants

**Comportement en cas de rejet** : Arrêter immédiatement la construction, enregistrer l'erreur spécifique, exiger une correction manuelle avant le déploiement.

### AR: التحقق الصارم من المصدر

**يجب التحقق من**:
1. المستودع المصدر هو `trizel-ai/trizel-core`
2. مسار الملف هو بالضبط `docs/registry/TRIZEL_REGISTRY.yaml`
3. إصدار المخطط يطابق توافق الموقع (حاليًا `1.0.0`)
4. حقل `registry_metadata.publishable` هو `true`

**يجب الرفض إذا**:
- المصدر من أي مستودع آخر
- مسار الملف مختلف
- إصدار المخطط غير متوافق
- علامة النشر مفقودة أو `false`
- بناء جملة YAML غير صالح
- حقول البيانات الوصفية المطلوبة مفقودة

**السلوك عند الرفض**: إيقاف البناء فورًا، تسجيل خطأ محدد، مطلوب إصلاح يدوي قبل النشر.

---

## Provenance Requirements / Exigences de provenance / متطلبات المصدر

### EN: Mandatory Metadata Display

For all displayed content, the website **must** show:

1. **Registry version**: `registry_metadata.version`
2. **Effective date**: `registry_metadata.effective_date`
3. **Source repository**: `registry_metadata.repository`
4. **Schema version**: `registry_metadata.schema_version`
5. **Last updated**: Timestamp of registry fetch

**Display format** (example):
```
Registry Version: 1.0.0
Last Updated: 2026-01-12T11:49:00Z
Source: trizel-ai/trizel-core
Schema: 1.0.0
```

### FR: Affichage obligatoire des métadonnées

Pour tout le contenu affiché, le site Web **doit** afficher :

1. **Version du registre** : `registry_metadata.version`
2. **Date d'effet** : `registry_metadata.effective_date`
3. **Référentiel source** : `registry_metadata.repository`
4. **Version du schéma** : `registry_metadata.schema_version`
5. **Dernière mise à jour** : Horodatage de la récupération du registre

**Format d'affichage** (exemple) :
```
Version du registre : 1.0.0
Dernière mise à jour : 2026-01-12T11:49:00Z
Source : trizel-ai/trizel-core
Schéma : 1.0.0
```

### AR: عرض البيانات الوصفية الإلزامية

لجميع المحتوى المعروض، **يجب** على الموقع إظهار:

1. **إصدار السجل**: `registry_metadata.version`
2. **تاريخ السريان**: `registry_metadata.effective_date`
3. **مستودع المصدر**: `registry_metadata.repository`
4. **إصدار المخطط**: `registry_metadata.schema_version`
5. **آخر تحديث**: الطابع الزمني لجلب السجل

**تنسيق العرض** (مثال):
```
إصدار السجل: 1.0.0
آخر تحديث: 2026-01-12T11:49:00Z
المصدر: trizel-ai/trizel-core
المخطط: 1.0.0
```

---

## Non-Interpretive Display / Affichage non interprétatif / العرض غير التفسيري

### EN: Factual Presentation Only

**Allowed display content**:
- Repository names from `i18n.<lang>.title`
- Repository descriptions from `i18n.<lang>.description`
- Layer assignments (`layer` field)
- Operational status (`status` field)
- Canonical designation (`canonical` field)
- GitHub repository links (`repository` field)
- Role designations (`role` field)

**Forbidden display content**:
- Interpretive commentary added by website
- Analytical conclusions or comparisons
- Performance metrics or rankings
- Theoretical claims or scientific assertions
- Modified or paraphrased governance text
- Content from non-approved sources

### FR: Présentation factuelle uniquement

**Contenu d'affichage autorisé** :
- Noms de référentiels depuis `i18n.<lang>.title`
- Descriptions de référentiels depuis `i18n.<lang>.description`
- Attributions de couche (champ `layer`)
- État opérationnel (champ `status`)
- Désignation canonique (champ `canonical`)
- Liens de référentiel GitHub (champ `repository`)
- Désignations de rôle (champ `role`)

**Contenu d'affichage interdit** :
- Commentaires interprétatifs ajoutés par le site Web
- Conclusions analytiques ou comparaisons
- Métriques de performance ou classements
- Revendications théoriques ou assertions scientifiques
- Texte de gouvernance modifié ou paraphrasé
- Contenu provenant de sources non approuvées

### AR: عرض واقعي فقط

**محتوى العرض المسموح به**:
- أسماء المستودعات من `i18n.<lang>.title`
- أوصاف المستودعات من `i18n.<lang>.description`
- تعيينات الطبقة (حقل `layer`)
- الحالة التشغيلية (حقل `status`)
- التعيين القانوني (حقل `canonical`)
- روابط مستودع GitHub (حقل `repository`)
- تعيينات الدور (حقل `role`)

**محتوى العرض المحظور**:
- التعليقات التفسيرية المضافة من قبل الموقع
- الاستنتاجات التحليلية أو المقارنات
- مقاييس الأداء أو التصنيفات
- الادعاءات النظرية أو التأكيدات العلمية
- نص الحوكمة المعدل أو المعاد صياغته
- المحتوى من مصادر غير معتمدة

---

## Multilingual Support / Support multilingue / الدعم متعدد اللغات

### EN: Required Language Support

The website **must** support all three languages defined in the registry:

1. **English (en)**: Default language
2. **French (fr)**: Full translation required
3. **Arabic (ar)**: Full translation required with RTL support

**Language switching**:
- Provide visible language selector
- Preserve page state when switching languages
- Store language preference in browser
- Default to English if preference not set

**RTL (Right-to-Left) support**:
- Arabic text requires RTL text direction
- Adjust layout and alignment for Arabic
- Test thoroughly with Arabic content
- Ensure navigation and UI elements adapt to RTL

### FR: Support linguistique requis

Le site Web **doit** prendre en charge les trois langues définies dans le registre :

1. **Anglais (en)** : Langue par défaut
2. **Français (fr)** : Traduction complète requise
3. **Arabe (ar)** : Traduction complète requise avec support RTL

**Changement de langue** :
- Fournir un sélecteur de langue visible
- Préserver l'état de la page lors du changement de langue
- Stocker la préférence de langue dans le navigateur
- Par défaut en anglais si la préférence n'est pas définie

**Support RTL (droite à gauche)** :
- Le texte arabe nécessite une direction de texte RTL
- Ajuster la mise en page et l'alignement pour l'arabe
- Tester minutieusement avec le contenu arabe
- Assurer que les éléments de navigation et d'interface utilisateur s'adaptent au RTL

### AR: دعم اللغة المطلوب

**يجب** على الموقع دعم جميع اللغات الثلاث المحددة في السجل:

1. **الإنجليزية (en)**: اللغة الافتراضية
2. **الفرنسية (fr)**: مطلوب ترجمة كاملة
3. **العربية (ar)**: مطلوب ترجمة كاملة مع دعم RTL

**تبديل اللغة**:
- توفير محدد لغة مرئي
- الحفاظ على حالة الصفحة عند تبديل اللغات
- تخزين تفضيل اللغة في المتصفح
- الافتراضي للإنجليزية إذا لم يتم تعيين التفضيل

**دعم RTL (من اليمين إلى اليسار)**:
- يتطلب النص العربي اتجاه نص RTL
- ضبط التخطيط والمحاذاة للعربية
- الاختبار الشامل مع المحتوى العربي
- التأكد من أن عناصر التنقل وواجهة المستخدم تتكيف مع RTL

---

## Validation Workflow / Flux de validation / سير عمل التحقق

### EN: Build-Time Validation Steps

**Step 1: Fetch Registry**
```
1. Request TRIZEL_REGISTRY.yaml from approved source
2. Verify HTTP 200 response
3. Store raw YAML content
```

**Step 2: Parse and Validate**
```
1. Parse YAML using safe parser (no code execution)
2. Validate schema version matches website compatibility
3. Verify all required metadata fields present
4. Check publishable flag is true
```

**Step 3: Check Deprecated Terms**
```
1. Scan entire registry content for forbidden terms
2. Reject if "STOE" found
3. Reject if "V12" through "V22" found
4. Reject if versioned system labels found
```

**Step 4: Validate Repository Entries**
```
1. Verify each repository has all required fields
2. Check i18n completeness (en, fr, ar)
3. Validate character limits (title ≤100, description ≤200)
4. Ensure layer values are 0-6
5. Ensure status values are valid
```

**Step 5: Build Website**
```
1. Extract multilingual content
2. Generate static pages
3. Render navigation and UI
4. Apply language-specific formatting (RTL for Arabic)
```

**Failure behavior**: If any step fails, halt build immediately, log specific error, do not deploy.

### FR: Étapes de validation au moment de la construction

**Étape 1 : Récupérer le registre**
```
1. Demander TRIZEL_REGISTRY.yaml à la source approuvée
2. Vérifier la réponse HTTP 200
3. Stocker le contenu YAML brut
```

**Étape 2 : Analyser et valider**
```
1. Analyser YAML avec un analyseur sûr (pas d'exécution de code)
2. Valider que la version du schéma correspond à la compatibilité du site Web
3. Vérifier que tous les champs de métadonnées requis sont présents
4. Vérifier que l'indicateur publiable est true
```

**Étape 3 : Vérifier les termes obsolètes**
```
1. Scanner tout le contenu du registre pour les termes interdits
2. Rejeter si "STOE" trouvé
3. Rejeter si "V12" à "V22" trouvé
4. Rejeter si des étiquettes de système versionnées trouvées
```

**Étape 4 : Valider les entrées de référentiel**
```
1. Vérifier que chaque référentiel a tous les champs requis
2. Vérifier l'exhaustivité de i18n (en, fr, ar)
3. Valider les limites de caractères (titre ≤100, description ≤200)
4. Assurer que les valeurs de couche sont 0-6
5. Assurer que les valeurs de statut sont valides
```

**Étape 5 : Construire le site Web**
```
1. Extraire le contenu multilingue
2. Générer des pages statiques
3. Rendre la navigation et l'interface utilisateur
4. Appliquer le formatage spécifique à la langue (RTL pour l'arabe)
```

**Comportement en cas d'échec** : Si une étape échoue, arrêter immédiatement la construction, enregistrer l'erreur spécifique, ne pas déployer.

### AR: خطوات التحقق في وقت البناء

**الخطوة 1: جلب السجل**
```
1. طلب TRIZEL_REGISTRY.yaml من المصدر المعتمد
2. التحقق من استجابة HTTP 200
3. تخزين محتوى YAML الخام
```

**الخطوة 2: التحليل والتحقق**
```
1. تحليل YAML باستخدام محلل آمن (لا يوجد تنفيذ للكود)
2. التحقق من أن إصدار المخطط يطابق توافق الموقع
3. التحقق من وجود جميع حقول البيانات الوصفية المطلوبة
4. التحقق من أن علامة النشر هي true
```

**الخطوة 3: التحقق من المصطلحات المهملة**
```
1. مسح كامل محتوى السجل للمصطلحات المحظورة
2. الرفض إذا تم العثور على "STOE"
3. الرفض إذا تم العثور على "V12" إلى "V22"
4. الرفض إذا تم العثور على تسميات نظام الإصدار
```

**الخطوة 4: التحقق من إدخالات المستودع**
```
1. التحقق من أن كل مستودع لديه جميع الحقول المطلوبة
2. التحقق من اكتمال i18n (en, fr, ar)
3. التحقق من حدود الأحرف (العنوان ≤100، الوصف ≤200)
4. التأكد من أن قيم الطبقة هي 0-6
5. التأكد من أن قيم الحالة صالحة
```

**الخطوة 5: بناء الموقع**
```
1. استخراج المحتوى متعدد اللغات
2. إنشاء صفحات ثابتة
3. عرض التنقل وواجهة المستخدم
4. تطبيق التنسيق الخاص باللغة (RTL للعربية)
```

**سلوك الفشل**: إذا فشلت أي خطوة، إيقاف البناء فورًا، تسجيل خطأ محدد، عدم النشر.

---

## Compliance Checklist / Liste de conformité / قائمة الامتثال

### EN: Required Validations

Before deploying the website, verify:

- [ ] Registry fetched from approved source only
- [ ] Schema version compatible with website
- [ ] All required metadata fields present
- [ ] Publishable flag is `true`
- [ ] No deprecated terminology detected
- [ ] All repositories have complete i18n (en, fr, ar)
- [ ] Character limits respected
- [ ] Layer values valid (0-6)
- [ ] Status values valid
- [ ] Build succeeds without errors
- [ ] Multilingual UI functional
- [ ] RTL support working for Arabic
- [ ] Provenance metadata displayed
- [ ] No interpretive content added

### FR: Validations requises

Avant de déployer le site Web, vérifier :

- [ ] Registre récupéré uniquement à partir de la source approuvée
- [ ] Version du schéma compatible avec le site Web
- [ ] Tous les champs de métadonnées requis présents
- [ ] L'indicateur publiable est `true`
- [ ] Aucune terminologie obsolète détectée
- [ ] Tous les référentiels ont un i18n complet (en, fr, ar)
- [ ] Limites de caractères respectées
- [ ] Valeurs de couche valides (0-6)
- [ ] Valeurs de statut valides
- [ ] Construction réussie sans erreurs
- [ ] Interface utilisateur multilingue fonctionnelle
- [ ] Support RTL fonctionnel pour l'arabe
- [ ] Métadonnées de provenance affichées
- [ ] Aucun contenu interprétatif ajouté

### AR: التحققات المطلوبة

قبل نشر الموقع، تحقق من:

- [ ] تم جلب السجل من المصدر المعتمد فقط
- [ ] إصدار المخطط متوافق مع الموقع
- [ ] جميع حقول البيانات الوصفية المطلوبة موجودة
- [ ] علامة النشر هي `true`
- [ ] لم يتم الكشف عن مصطلحات مهملة
- [ ] جميع المستودعات لديها i18n كامل (en, fr, ar)
- [ ] احترام حدود الأحرف
- [ ] قيم الطبقة صالحة (0-6)
- [ ] قيم الحالة صالحة
- [ ] نجح البناء بدون أخطاء
- [ ] واجهة المستخدم متعددة اللغات وظيفية
- [ ] دعم RTL يعمل للعربية
- [ ] عرض بيانات المصدر الوصفية
- [ ] لم تتم إضافة محتوى تفسيري

---

## Version History / Historique des versions / سجل الإصدار

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-12 | Initial website consumption guidelines with multilingual support |

---

## Related Documents / Documents connexes / الوثائق ذات الصلة

- `TRIZEL_REGISTRY.yaml` — Canonical registry
- `SCHEMA.md` — Registry schema definition
- `layer-boundaries.md` — Layer 0 vs Layer 6 boundaries
- `examples/` — Non-executable examples
- `../../PUBLICATION_POLICY.md` — Publication rules
- `../../DEPRECATED_TERMS.md` — Forbidden terminology
