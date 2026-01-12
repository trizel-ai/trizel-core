# TRIZEL Registry Website

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance & Charter  
**Website Version**: 1.0.0  
**Last Updated**: 2026-01-12  
**Status**: Static, GitHub Pages Compatible

---

## Purpose

This directory contains the **static multilingual registry website** for the TRIZEL ecosystem. The website provides a public-facing view of the canonical project registry (`TRIZEL_REGISTRY.yaml`) with strict Layer 0 / Layer 6 separation.

---

## Contents

### Files

- `index.html` — Main registry website page (multilingual, self-contained)

### Features

1. **Multilingual Support**:
   - **EN (English)** — Full support
   - **FR (French)** — Full support
   - **AR (Arabic)** — Full support with RTL layout
   - **ZH (Chinese)** — Visible stub marked "Planned"

2. **Language Selector**: 
   - Interactive language switcher (EN / FR / AR / ZH)
   - Persists across page interactions
   - Automatic RTL layout for Arabic

3. **Registry Display**:
   - Consumes TRIZEL_REGISTRY.yaml data (embedded in page)
   - Groups repositories by layer (0-6)
   - Displays canonical status, operational status, roles
   - Provides GitHub links for each repository

4. **Provenance Information**:
   - Source repository: trizel-ai/trizel-core
   - Registry version: 1.0.0
   - Last updated date
   - Governance layer designation

5. **Compliance**:
   - Allowlist-only (no auto-discovery)
   - Strictly non-interpretive
   - No deprecated terminology
   - No cross-layer content mixing
   - Static HTML only (GitHub Pages compatible)

---

## Layer Separation

### Layer 0 (This Repository)

**Role**: Governance & Charter

This website implementation lives in the **Layer 0 governance repository** (trizel-ai/trizel-core) as:
- Reference implementation
- Schema demonstration
- Static content source

**Contents**:
- HTML template with embedded registry data
- Non-executable, static display
- Governance metadata only

### Layer 6 (Target Deployment)

**Role**: Website & Orchestration

The actual **production website** should be deployed in the **Layer 6 repository** (abdelkader-omran/trizel-AI):
- Consumes TRIZEL_REGISTRY.yaml from Layer 0
- Implements this reference design
- Hosts on GitHub Pages or equivalent
- Provides public-facing visualization

**Important**: This directory (`website/registry/`) is a **reference template**. The Layer 6 repository should:
1. Fetch TRIZEL_REGISTRY.yaml from trizel-ai/trizel-core
2. Implement website using this design as reference
3. Deploy to GitHub Pages
4. Update dynamically when registry changes

---

## Usage

### For Layer 6 Website Maintainers

**Deploying the Registry Website**:

1. **Copy Reference Template**:
   - Use `index.html` as starting point
   - Modify registry data loading to fetch from trizel-ai/trizel-core
   - Update provenance information with build metadata

2. **Fetch Registry Data**:
   ```javascript
   // Example: Fetch registry from Layer 0
   fetch('https://raw.githubusercontent.com/trizel-ai/trizel-core/main/docs/registry/TRIZEL_REGISTRY.yaml')
       .then(response => response.text())
       .then(yaml => {
           // Parse YAML and update registryData
           // Render website with fetched data
       });
   ```

3. **Deploy to GitHub Pages**:
   - Enable GitHub Pages in Layer 6 repository settings
   - Set source to main branch or docs folder
   - Configure custom domain if desired
   - Test all languages and RTL layout

4. **Update on Registry Changes**:
   - Implement automatic rebuild on registry updates
   - Verify registry version compatibility
   - Re-deploy website with new data

### For Local Testing

**Testing the Website Locally**:

1. **Open in Browser**:
   ```bash
   # From repository root
   cd website/registry
   python3 -m http.server 8000
   # Or use any other local server
   ```

2. **Navigate to**:
   - http://localhost:8000/index.html

3. **Test Features**:
   - Language switching (EN / FR / AR / ZH)
   - RTL layout for Arabic
   - Repository display and grouping
   - Links to GitHub repositories
   - Responsive design

### For Validation

**Compliance Checks**:

1. **HTML Validation**:
   ```bash
   # Use W3C HTML validator
   # https://validator.w3.org/
   ```

2. **Deprecated Terms Check**:
   ```bash
   # Scan for forbidden terms
   grep -r "STOE" website/registry/
   grep -rE "V(12|13|14|15|16|17|18|19|20|21|22)" website/registry/
   ```

3. **Browser Testing**:
   - Test in Chrome, Firefox, Safari, Edge
   - Verify RTL layout in Arabic mode
   - Check responsive design on mobile
   - Validate accessibility (screen readers)

---

## Design Principles

### Non-Interpretive Display

**Allowed**:
- Display repository titles and descriptions from registry
- Show layer assignments and roles
- Indicate canonical and operational status
- Provide GitHub links

**Forbidden**:
- Adding interpretive commentary
- Comparing or ranking repositories
- Making analytical claims
- Displaying non-registry metadata

### Allowlist-Only Ingestion

**Required Behavior**:
- Only display repositories from TRIZEL_REGISTRY.yaml
- Reject unlisted repositories
- Fail if registry data invalid
- Validate schema before rendering

**Forbidden Behavior**:
- Auto-discovering repositories via GitHub API
- Guessing repository inclusion
- Displaying partial or unvalidated data
- Silently skipping validation errors

### Fail-Closed Validation

**Failure Conditions**:
- Registry file not found
- Invalid YAML/JSON syntax
- Missing required fields
- Deprecated terminology detected
- Schema version mismatch

**On Failure**:
- Display error message
- Do not render partial data
- Log validation failure
- Require fix before deployment

---

## Multilingual Implementation

### Language Support

**Current Languages**:

1. **English (EN)** — Primary language, full support
2. **French (FR)** — Full translation, complete
3. **Arabic (AR)** — Full translation with RTL support
4. **Chinese (ZH)** — Planned, visible stub with notice

**Chinese Implementation**:
- Language selector includes ZH option
- Registry data includes ZH translations
- Page displays "Planned" notice in ZH mode
- Full support to be implemented in future

### RTL (Right-to-Left) Support

**Arabic Mode**:
- Sets `dir="rtl"` on body element
- Adjusts layout for right-to-left reading
- Reverses flex direction for badges and headers
- Moves border indicators to right side

**Testing RTL**:
- Verify text alignment
- Check badge and button positioning
- Ensure readable layout
- Test with Arabic content

---

## Technical Specifications

### Browser Compatibility

**Minimum Requirements**:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

**Features Used**:
- CSS Flexbox
- CSS Variables (Custom Properties)
- JavaScript ES6+ (const, let, arrow functions)
- Fetch API (for future dynamic loading)

### Responsive Design

**Breakpoints**:
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

**Layout Adjustments**:
- Flexible containers
- Responsive font sizes
- Stacking on small screens
- Fluid max-width containers

### Accessibility

**ARIA Support**:
- Semantic HTML elements
- Proper heading hierarchy
- Descriptive link text
- Language attributes

**Keyboard Navigation**:
- Tab-accessible language selector
- Focusable links
- Logical tab order

---

## GitHub Pages Deployment

### Configuration

**For Layer 6 Repository**:

1. **Enable GitHub Pages**:
   - Settings → Pages
   - Source: main branch / docs folder
   - Save

2. **Custom Domain** (optional):
   - Configure CNAME record
   - Add custom domain in settings
   - Enable HTTPS

3. **Build Settings**:
   - No build required (static HTML)
   - Direct deployment from repository

### File Structure

```
abdelkader-omran/trizel-AI/
├── index.html (or redirect to registry)
├── registry/
│   └── index.html (this website)
├── assets/
│   └── (optional CSS, images)
└── README.md
```

---

## Updating the Website

### When Registry Changes

**Process**:

1. **Detect Change**:
   - Monitor trizel-ai/trizel-core for commits to TRIZEL_REGISTRY.yaml
   - Set up GitHub Actions webhook (optional)

2. **Fetch Updated Registry**:
   - Pull latest TRIZEL_REGISTRY.yaml
   - Validate schema version
   - Check for deprecated terms

3. **Update Website**:
   - Re-embed registry data in HTML
   - Or implement dynamic fetch on page load
   - Test all languages

4. **Deploy**:
   - Commit changes to Layer 6 repository
   - Push to trigger GitHub Pages rebuild
   - Verify deployment

### Version Compatibility

**Schema Versions**:
- Current: 1.0.0
- Website supports: 1.0.0
- Future: Update website when schema changes

**Breaking Changes**:
- Major version bump (1.0.0 → 2.0.0)
- Requires website update before registry merge
- Coordinate changes across layers

---

## Security and Privacy

### Data Handling

**Public Data Only**:
- Repository names and metadata
- Layer assignments
- Operational status
- Multilingual descriptions

**No Sensitive Data**:
- No credentials or secrets
- No personal information
- No internal documentation
- No private repository references

### Content Security

**Static Content**:
- No user input processing
- No dynamic content generation (server-side)
- No database queries
- No external API calls (except optional registry fetch)

**XSS Prevention**:
- Sanitized text rendering
- No innerHTML with user data
- Escaped special characters

---

## Compliance Checklist

For Layer 6 deployment:

- [ ] Fetch registry from trizel-ai/trizel-core only
- [ ] Validate schema version compatibility
- [ ] Check for deprecated terminology
- [ ] Support all four languages (EN, FR, AR, ZH)
- [ ] Implement RTL layout for Arabic
- [ ] Display provenance information
- [ ] Provide GitHub links for repositories
- [ ] Group by layer (0-6)
- [ ] Show canonical and status badges
- [ ] HTML validated (W3C)
- [ ] Browser tested (Chrome, Firefox, Safari, Edge)
- [ ] Accessibility verified
- [ ] GitHub Pages deployed successfully

---

## Maintenance

### Update Frequency

**Registry Updates**: As needed (triggered by Layer 0 changes)  
**Website Design**: Stable (updates only for improvements or fixes)  
**Translations**: Update when new languages added

### Ownership

**Governance**: Layer 0 (trizel-ai/trizel-core)  
**Implementation**: Layer 6 (abdelkader-omran/trizel-AI)  
**Maintenance**: Coordinated between layers

---

## Related Documents

- `../../docs/registry/TRIZEL_REGISTRY.yaml` — Canonical registry (source data)
- `../../docs/registry/README.md` — Registry integration guide
- `../../docs/registry/SCHEMA.md` — Registry schema definition
- `../../PUBLICATION_POLICY.md` — Publication guidelines
- `../../Documents/TRIZEL/metadata/` — Metadata templates

---

## Version History

| Version | Date       | Changes                                      |
|---------|------------|----------------------------------------------|
| 1.0.0   | 2026-01-12 | Initial multilingual registry website       |

---

## Questions and Support

For questions about the registry website:

**Repository**: trizel-ai/trizel-core (Layer 0)  
**Issues**: https://github.com/trizel-ai/trizel-core/issues  
**Label**: `registry-website`, `layer-6-integration`

For Layer 6 deployment support:

**Repository**: abdelkader-omran/trizel-AI (Layer 6)  
**Issues**: (Layer 6 repository issues)

---

**TRIZEL — Technology for Research, Inference, Zonal Evaluation & Learning**  
Static Multilingual Registry Website — GitHub Pages Compatible  
Layer 0 Reference Implementation → Layer 6 Deployment
