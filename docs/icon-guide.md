# OpenMac Icon Specifications & Design Guide

This document outlines the design standards, technical specifications, and legal considerations for project icons in OpenMac.

---

## 🎯 Purpose of Local Icons

Unlike third-party directories that rely on external CDNs or raw image links from external websites:
1. **Zero Tracking**: No user requests are sent to external third-party analytics trackers when viewing OpenMac.
2. **Archival Stability**: Icons never break due to remote URL changes, site redesigns, or deleted assets.
3. **Optimized Performance**: Icons render instantly via GitHub's internal repository CDN.

---

## 📐 Technical Specifications

| Dimension | Specification | Notes |
| :--- | :--- | :--- |
| **Aspect Ratio** | Strictly **1:1** (Square) | Rectangular logos will be rejected. |
| **Format** | **SVG** (Preferred) or **PNG** | SVG provides infinite scaling and minimal file weight. |
| **PNG Resolution** | `256×256` or `512×512` px | Ensures sharpness on Retina displays. |
| **SVG viewBox** | Defined `viewBox` attribute | e.g. `viewBox="0 0 128 128"` or `0 0 256 256`. |
| **File Size** | < **80 KB** | Compress PNGs with `oxipng` or `pngquant`; clean SVGs with `svgo`. |
| **Background** | Transparent or rounded squircle | Match macOS Human Interface Guidelines where possible. |

---

## 🏷️ File Naming Convention

Icon filenames must strictly mirror the project `id`:
- Pattern: `^[a-z0-9-]+.(svg|png)$`
- Directory: `icons/project-icons/`

**Correct Examples:**
- `icons/project-icons/rectangle.svg`
- `icons/project-icons/alt-tab-macos.svg`
- `icons/project-icons/stats.svg`

**Incorrect Examples:**
- ❌ `icons/project-icons/Rectangle_Icon.PNG` (uppercase and underscores)
- ❌ `icons/project-icons/stats-logo.jpeg` (JPEG format not accepted)
- ❌ `icons/project-icons/app.svg` (must match project ID)

---

## ⚖️ Legal & Brand Integrity

1. **Third-Party Trademarks**: Project icons remain the property of their respective creators. Their presence in OpenMac is for factual identification under fair use.
2. **No Invented Logos**: If an open-source project lacks an official graphic emblem, do not create a speculative or unauthorized corporate logo. Use a clean, generic typographic symbol or the fallback icon `icons/default.svg`.

