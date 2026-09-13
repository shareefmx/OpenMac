# OpenMac Icon System & Guidelines

All project icons displayed in OpenMac are stored directly inside this repository under `icons/project-icons/`. This ensures all icons are version-controlled, highly performant, load reliably on GitHub without external tracking, and render consistently across dark and light modes.

---

## 📐 Icon Specifications

When contributing an icon for an open-source project, please follow these technical criteria:

| Property | Requirement |
| :--- | :--- |
| **Format** | Clean **SVG** (vector) or **PNG** (raster) |
| **Dimensions (PNG)** | Recommended `256×256` px or `512×512` px |
| **Dimensions (SVG)** | Valid `viewBox` (e.g., `0 0 128 128` or `0 0 256 256`) |
| **Aspect Ratio** | Strictly **1:1** square |
| **Background** | Transparent background (or rounded squircle matching macOS app icon design) |
| **File Size** | Under **100 KB** (optimized with SVGO for SVG or pngquant/oxipng for PNG) |
| **Naming Convention** | Strictly matching the project ID: `icons/project-icons/<project-id>.svg` (or `.png`) |

---

## 🏷️ Naming Rules

Filenames must adhere to strict normalization:
- **Lowercase alphanumeric** characters and hyphens only (`[a-z0-9-]+`).
- No uppercase letters, spaces, underscores, or special characters.
- Must exactly match the `id` field defined in `data/projects.yml`.

**Examples:**
- ✅ `icons/project-icons/iina.svg`
- ✅ `icons/project-icons/alt-tab-macos.svg`
- ❌ `icons/project-icons/AltTab.PNG`
- ❌ `icons/project-icons/iina_icon.png`

---

## ⚖️ Trademark & Brand Policy

1. **Ownership**: All project icons, logos, and trademarks belong to their respective creators and organizations.
2. **Fair Use & Attribution**: Icons in this repository are included strictly for fair-use identification and directory discovery purposes.
3. **No Endorsement**: Inclusion of a logo does not imply endorsement by the upstream project or creator.
4. **Takedowns**: Project owners who wish to update, replace, or remove their icon may open an issue or pull request, and we will promptly respect their preference.
5. **No Fabricated Logos**: Do not invent fake logos for projects that do not have one. For projects without an official app icon, use a clean stylized glyph or the fallback icon `icons/default.svg`.

