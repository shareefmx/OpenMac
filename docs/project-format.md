# Project Metadata Schema Reference

This document defines the schema rules for `data/projects.yml`.

---

## 📋 Schema Definition

```yaml
projects:
  - id: string               # Required
    name: string             # Required
    description: string      # Required
    github: string (URL)     # Required
    website: string (URL)    # Required
    category: string         # Required
    subcategory: string      # Optional
    license: string          # Required
    platform: string         # Required
    language: string         # Required
    status: enum             # Required
    icon: string (Path)      # Required
    featured: boolean        # Optional (defaults to false)
```

---

## 🔍 Detailed Field Descriptions

### `id` *(required)*
- **Type**: `string`
- **Pattern**: `^[a-z0-9-]+$`
- **Description**: Unique identifier used for URL slugs and icon matching. Must be lowercase alphanumeric with hyphens only.
- **Example**: `iina`, `alt-tab-macos`

### `name` *(required)*
- **Type**: `string`
- **Description**: The official display name of the software as published by its authors.
- **Example**: `IINA`, `AltTab`

### `description` *(required)*
- **Type**: `string`
- **Length**: 20 to 240 characters.
- **Description**: An objective summary describing the core functionality of the project. Avoid marketing hyperbole (e.g. "The best ever!", "Revolutionary").
- **Example**: `"The modern media player for macOS powered by mpv."`

### `github` *(required)*
- **Type**: `string` (URL)
- **Description**: Canonical public repository URL (GitHub, GitLab, Codeberg).
- **Example**: `https://github.com/iina/iina`

### `website` *(required)*
- **Type**: `string` (URL)
- **Description**: Official homepage or documentation site. Can match `github` if no standalone domain exists.
- **Example**: `https://iina.io`

### `category` *(required)*
- **Type**: `string`
- **Description**: Must match a registered category `id` from `data/categories.yml`.
- **Allowed values**: `development`, `terminal`, `window-management`, `productivity`, `system`, `ai-ml`, `media`, `security`, `notes`, `file-management`, `design`, `customization`.

### `subcategory` *(optional)*
- **Type**: `string`
- **Description**: Fine-grained functional grouping within the category.
- **Example**: `"Video Players"`, `"Tiling Window Managers"`

### `license` *(required)*
- **Type**: `string`
- **Description**: SPDX identifier of an approved OSI/FSF open-source license. Dual licenses should be separated by slashes (e.g. `GPL-2.0 / GPL-3.0`).
- **Allowed values**: `MIT`, `Apache-2.0`, `GPL-2.0`, `GPL-3.0`, `AGPL-3.0`, `LGPL-2.1`, `LGPL-3.0`, `BSD-2-Clause`, `BSD-3-Clause`, `MPL-2.0`, `ISC`, `EPL-2.0`, `Unlicense`, `CC0-1.0`, `Vim`.

### `platform` *(required)*
- **Type**: `string`
- **Description**: Minimum supported version of macOS or architecture specification.
- **Example**: `macOS 12.0+`, `macOS 10.15+ (Apple Silicon & Intel)`

### `language` *(required)*
- **Type**: `string`
- **Description**: Primary programming language or framework used.
- **Example**: `Swift`, `Rust`, `TypeScript`, `C++`, `Objective-C`

### `status` *(required)*
- **Type**: `enum`
- **Allowed values**:
  - `active`: Regularly maintained with recent commits/releases.
  - `maintenance`: Stable, infrequent updates primarily for OS compatibility.
  - `archived`: Upstream repository is in read-only / archived state.

### `icon` *(required)*
- **Type**: `string` (Relative path)
- **Description**: Relative path to the icon file on disk.
- **Example**: `icons/project-icons/iina.svg`

### `featured` *(optional)*
- **Type**: `boolean`
- **Default**: `false`
- **Description**: Set to `true` to display the project in the Featured showcase section at the top of the directory.

