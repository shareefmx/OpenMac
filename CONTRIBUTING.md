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

## � Easy Ways to Add a Project

Adding a new open-source Mac app to OpenMac is fast and seamless. Pick the method that works best for you:

### 🌟 Method 1: 1-Click Submission (No Git Required)
The easiest way to contribute! If you don't want to use the command line or Git:
1. Open the [**Add Project Issue Form**](https://github.com/shareefmx/OpenMac/issues/new?template=add-project.yml).
2. Paste the GitHub link, app name, description, and license.
3. Submit the issue. Our automated checks and maintainers will verify the project, prepare the icon, and merge it!

---

### ⚡ Method 2: The Interactive CLI Wizard (Fastest for Developers)
We built an automated terminal wizard that asks for your project's details, copies or generates the icon, validates data, and regenerates `README.md` automatically:

```bash
# 1. Clone your fork
git clone https://github.com/YOUR_USERNAME/OpenMac.git
cd OpenMac

# 2. Run the interactive wizard
python3 scripts/add-project.py
```

The wizard handles everything:
- Prompts for project name, repository link, category, description, and stack.
- Auto-generates or imports the vector SVG icon to `icons/project-icons/`.
- Validates that no duplicates exist.
- Automatically compiles the markdown tables in `README.md`.
- Prints out the exact `git` commands ready to commit and push!

---

### 🛠️ Method 3: Standard Manual Git Workflow

If you prefer to edit files manually:

#### Step 1: Fork and Branch
```bash
git clone https://github.com/YOUR_USERNAME/OpenMac.git
cd OpenMac
git checkout -b add/project-slug
```

#### Step 2: Add the Project Icon
Place your 1:1 square vector SVG (or 256×256 PNG) in `icons/project-icons/<project-slug>.svg`:
```bash
cp /path/to/icon.svg icons/project-icons/project-slug.svg
```
*(Refer to [`icons/README.md`](./icons/README.md) for complete icon guidelines).*

#### Step 3: Add Metadata to `data/projects.yml`
Append your project record to [`data/projects.yml`](./data/projects.yml):

```yaml
  - id: project-slug
    name: Project Name
    description: "Concise description of the app's features (20 to 200 characters)."
    github: "https://github.com/organization/repo"
    website: "https://example.com"
    category: productivity
    subcategory: "Launchers & Quick Navigation"
    license: "MIT"
    platform: "macOS 12.0+"
    language: "Swift"
    status: active
    icon: "icons/project-icons/project-slug.svg"
    featured: false
```

#### Step 4: Validate and Compile
Run our built-in test suite and generator:

```bash
# Verify schema, licenses, and icon existence
python3 scripts/validate-projects.py

# Recompile the README tables
python3 scripts/generate-readme.py
```

#### Step 5: Commit, Push, and Open PR
```bash
git add data/projects.yml icons/project-icons/ README.md
git commit -m "Add Project Name to Productivity"
git push origin add/project-slug
```
Visit your fork on GitHub and click **Compare & pull request**!

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
│   ├── add-project.py        # Interactive CLI wizard to add projects
│   ├── validate-projects.py  # Integrity and schema validator
│   ├── generate-readme.py    # Auto-generates markdown tables in README.md
│   └── check-links.py        # URL format and network health checker
└── docs/                     # Extended documentation and guides
```

---

## 💬 Questions or Suggestions?

Have questions or need help with a submission? Join us in [**GitHub Discussions**](https://github.com/shareefmx/OpenMac/discussions) or open a [**Support Request**](./SUPPORT.md).
