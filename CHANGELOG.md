# Changelog

All notable changes to the **OpenMac** repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-09-13

### Added
- **Initial Directory Release**: Curated catalog of 68 verified, 100% open-source macOS apps, developer utilities, and CLI tools.
- **Taxonomy Framework**: Established 12 distinct categories covering Development, Terminal & Shell, Window Management, Productivity, System & Hardware, AI & Machine Learning, Media & Audio, Security & Privacy, Notes & Writing, File Management, Design, and Customization.
- **Automated Validation Engine**: Created `scripts/validate-projects.py` with URL normalization, duplicate repository detection, license verification, and filesystem icon verification.
- **Dynamic README Generator**: Implemented `scripts/generate-readme.py` to auto-compile Markdown tables, statistics, and tables of contents from `data/projects.yml`.
- **Integrated Icon Suite**: Generated 68 custom vector SVG project icons located in `icons/project-icons/`.
- **CI/CD Automation**: Added GitHub Actions workflow (`.github/workflows/validate-projects.yml`) to enforce data integrity on all commits and pull requests.
- **Community Governance Suite**: Added `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1), `SECURITY.md`, `SUPPORT.md`, and comprehensive documentation in `docs/`.
- **GitHub Issue Forms**: Added modern YAML issue templates for proposing new projects, reporting inaccuracies, and requesting categories.

