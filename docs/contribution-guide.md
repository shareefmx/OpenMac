# Comprehensive Contribution Guide

This guide provides an exhaustive, step-by-step walkthrough for adding projects, updating metadata, and maintaining OpenMac.

---

## 🚦 Pre-Flight Checklist

Before preparing a submission, confirm:
1. **Public Repository**: The project must have public source code (e.g. `github.com/user/repo`).
2. **License**: The repository contains an OSI-approved license file (`LICENSE`, `LICENSE.md`, or `COPYING`).
3. **Compatibility**: The app builds or runs on macOS.
4. **No Prior Entry**: The project is not already listed in `data/projects.yml`.

---

## 📝 Editing `data/projects.yml`

All project records are stored in `data/projects.yml`. Add your new project entry using the YAML structure below:

```yaml
  - id: app-name                      # Required: lowercase alphanumeric and hyphens
    name: "App Name"                  # Required: official application name
    description: "Short summary."     # Required: 20-200 characters, no marketing fluff
    github: "https://github.com/..."  # Required: primary source code repository
    website: "https://example.com"    # Required: official website or documentation
    category: productivity            # Required: must match an id in data/categories.yml
    subcategory: "Menubar Utilities"  # Optional: subcategory grouping
    license: "MIT"                    # Required: recognized open-source license
    platform: "macOS 12.0+"           # Required: minimum supported OS version
    language: "Swift"                 # Required: primary implementation language
    status: active                    # Required: active | maintenance | archived
    icon: "icons/project-icons/app-name.svg" # Required: local path to icon
    featured: false                   # Optional: boolean flag for featured list
```

---

## 🎨 Adding the Icon

Place your icon in `icons/project-icons/`:
- **Format**: SVG preferred (vector scalable); PNG accepted (min 256x256).
- **Naming**: Must strictly match the `id` field (e.g. `icons/project-icons/<id>.svg`).
- Check that the image renders with a transparent background and square aspect ratio.

---

## 🧪 Local Testing & Validation

Run the validation suite locally to catch errors before pushing:

```bash
# 1. Run schema and duplicate checks
python3 scripts/validate-projects.py

# 2. Check URL syntax
python3 scripts/check-links.py

# 3. Synchronize README tables
python3 scripts/generate-readme.py

# 4. Verify that README is in sync
python3 scripts/generate-readme.py --check
```

---

## 🚀 Submitting Your Pull Request

1. Commit your changes with a clear message:
   ```bash
   git commit -m "Add App Name to Productivity"
   ```
2. Push your branch to GitHub:
   ```bash
   git push origin add/app-name
   ```
3. Open a Pull Request against `main`.
4. Ensure CI checks pass. A maintainer will review and merge your PR.

