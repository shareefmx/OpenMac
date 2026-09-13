# Contributing to OpenMac

Thank you for your interest in contributing to **OpenMac**! This directory exists to make the world's best open-source macOS software discoverable, verifiable, and transparent.

Whether you are adding a new application, updating an existing listing, improving documentation, or refining automated scripts, your contributions make a tangible impact on the Mac open-source community.

---

## 🧭 Core Principles & Inclusion Rules

Before submitting a project, please ensure it strictly satisfies our **Four Pillars**:

1. **100% Genuine Open Source**: The software must have its complete source code publicly accessible in a Git repository (GitHub, GitLab, Codeberg). Closed-source freeware (such as Alfred, Raycast, Obsidian, Shottr, or AppCleaner) is strictly excluded.
2. **Recognized License**: The project must be licensed under an official [OSI-approved](https://opensource.org/licenses) or FSF-compliant license (MIT, Apache-2.0, GPL-2.0/3.0, BSD, MPL, etc.).
3. **macOS Native or Desktop Experience**: The software must run on macOS (Apple Silicon or Intel) as a desktop GUI app, menu bar utility, system extension, or powerful CLI workflow.
4. **No Deceptive Paywalls**: Applications that gate their primary functionality behind proprietary paid licenses without allowing users to compile or run the full software from source are ineligible.

---

## 🛠️ Contribution Workflow (Step-by-Step)

### Step 1: Fork and Clone the Repository
Visit [github.com/shareefmx/OpenMac](https://github.com/shareefmx/OpenMac) and click the **Fork** button in the top right corner. Then clone your fork locally:

```bash
git clone https://github.com/YOUR_USERNAME/OpenMac.git
cd OpenMac
```

### Step 2: Create a Dedicated Feature Branch
Keep your branch focused on the specific project or fix you are making:

```bash
git checkout -b add/project-name
```

### Step 3: Add the Project Icon
Place the icon into `icons/project-icons/` using a normalized, lowercase-hyphenated filename:

```bash
# Example: Adding an icon for 'my-app'
cp /path/to/icon.svg icons/project-icons/my-app.svg
```

**Icon Requirements:**
- Format: **SVG** (strongly preferred) or **PNG**.
- Geometry: Strict **1:1 square** aspect ratio.
- Filename: Exactly matching the project `id` in `data/projects.yml`.
- Refer to [`icons/README.md`](./icons/README.md) for full specs.

### Step 4: Add Metadata to `data/projects.yml`
Open `data/projects.yml` and add a new entry under the appropriate category. Follow this exact schema:

```yaml
  - id: my-app
    name: My App
    description: "Concise, descriptive summary of what the app does (20 to 200 characters)."
    github: "https://github.com/organization/my-app"
    website: "https://myapp.org"
    category: productivity
    subcategory: "Launchers & Quick Navigation"
    license: "MIT"
    platform: "macOS 12.0+"
    language: "Swift"
    status: active
    icon: "icons/project-icons/my-app.svg"
    featured: false
```

### Step 5: Run Automated Validation
Test your changes locally before committing:

```bash
python3 scripts/validate-projects.py
```

The script verifies:
- All required metadata fields are populated.
- No duplicate GitHub repository URLs or IDs exist.
- The specified license is recognized as open source.
- The referenced icon exists on disk.
- URL formats are structurally valid.

### Step 6: Regenerate the README
OpenMac tables are automatically generated from `data/projects.yml`:

```bash
python3 scripts/generate-readme.py
```

This updates all category tables, table of contents counts, and featured highlights in `README.md`.

### Step 7: Commit and Push

```bash
git add data/projects.yml icons/project-icons/ README.md
git commit -m "Add My App to Productivity"
git push origin add/project-name
```

### Step 8: Open a Pull Request
Go to your fork on GitHub and click **Compare & pull request**. Complete the PR checklist and submit for review. Our automated CI will run checks on your PR immediately!

---

## 📁 Repository Structure Overview

```
OpenMac/
├── README.md                 # Primary directory presentation (partially auto-generated)
├── CONTRIBUTING.md           # Contribution documentation
├── data/
│   ├── categories.yml        # Category definitions & ordering (Source of Truth)
│   └── projects.yml          # Project records & metadata (Source of Truth)
├── icons/
│   ├── README.md             # Icon specifications & legal guide
│   ├── default.svg           # Fallback icon
│   └── project-icons/        # Individual project icons (<id>.svg or <id>.png)
├── scripts/
│   ├── validate-projects.py  # Integrity and schema validator
│   ├── generate-readme.py    # Auto-generates markdown tables in README.md
│   └── check-links.py        # URL format and network health checker
└── docs/                     # Extended documentation and guides
```

---

## 💡 Submitting Without Git

If you are not familiar with Git or command-line workflows, you can still contribute! Simply open an issue using our [**Project Submission Issue Template**](https://github.com/shareefmx/OpenMac/issues/new?template=add-project.yml). Our maintainers will review the submission, prepare the icon, and merge it for you.

