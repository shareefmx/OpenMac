#!/usr/bin/env python3
"""
Fetches the authentic, original app icons and logos directly from each
open-source project's GitHub repository or official assets.
Saves high-resolution, optimized 256x256 PNGs or clean SVGs into icons/project-icons/.
"""

import io
import os
import re
import sys
import yaml
import urllib.request
import urllib.error
from PIL import Image

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OpenMac-IconFetcher"
}

# Explicit curated original icon URLs for known macOS repositories
KNOWN_ICON_URLS = {
    "rectangle": "https://raw.githubusercontent.com/rxhanson/Rectangle/main/Rectangle/Assets.xcassets/AppIcon.appiconset/mac512pts2x.png",
    "iina": "https://raw.githubusercontent.com/iina/iina/master/iina/Assets.xcassets/AppIcon.appiconset/icon_512x512.png",
    "maccy": "https://maccy.app/img/maccy/Logo.png",
    "stats": "https://raw.githubusercontent.com/exelban/stats/master/Stats/Supporting%20Files/Assets.xcassets/AppIcon.appiconset/icon_256x256.png",
    "aerospace": "https://raw.githubusercontent.com/nikitabobko/AeroSpace/main/resources/Assets.xcassets/AppIcon.appiconset/icon.png",
    "ice": "https://raw.githubusercontent.com/jordanbaird/Ice/main/Ice/Assets.xcassets/AppIcon.appiconset/icon_256x256.png",
    "alt-tab-macos": "https://raw.githubusercontent.com/lwouis/alt-tab-macos/master/docs/readme/main.svg",
    "pearcleaner": "https://raw.githubusercontent.com/alienator88/Pearcleaner/main/Pearcleaner/Assets.xcassets/AppIcon.appiconset/AppIcon.png",
    "ghostty": "https://ghostty.org/favicon.ico",
    "zed": "https://raw.githubusercontent.com/zed-industries/zed/main/docs/src/images/zed-logo.png",
    "vscodium": "https://raw.githubusercontent.com/VSCodium/vscodium/master/icons/stable/icon.png",
    "coteditor": "https://raw.githubusercontent.com/coteditor/CotEditor/main/CotEditor/Assets.xcassets/AppIcon.appiconset/appicon_512x512@2x.png",
    "bruno": "https://raw.githubusercontent.com/usebruno/bruno/main/assets/images/bruno.png",
    "colima": "https://raw.githubusercontent.com/abiosoft/colima/master/docs/logo.png",
    "podman-desktop": "https://raw.githubusercontent.com/containers/podman-desktop/main/packages/main/resources/icons/512x512.png",
    "iterm2": "https://iterm2.com/img/iterm2-icon.png",
    "alacritty": "https://raw.githubusercontent.com/alacritty/alacritty/master/extra/logo/compat/alacritty-term.png",
    "kitty": "https://raw.githubusercontent.com/kovidgoyal/kitty/master/logo/kitty.png",
    "wezterm": "https://raw.githubusercontent.com/wez/wezterm/main/assets/icon/terminal.png",
    "starship": "https://raw.githubusercontent.com/starship/starship/master/media/icon.png",
    "zellij": "https://raw.githubusercontent.com/zellij-org/zellij/main/assets/logo.png",
    "sol": "https://raw.githubusercontent.com/ospfranco/sol/main/assets/logo.png",
    "linearmouse": "https://raw.githubusercontent.com/linearmouse/linearmouse/main/LinearMouse/Assets.xcassets/AppIcon.appiconset/icon_512x512@2x.png",
    "kap": "https://raw.githubusercontent.com/wulkano/kap/main/media/icon.png",
    "flameshot": "https://raw.githubusercontent.com/flameshot-org/flameshot/master/data/img/app/flameshot.png",
    "monitorcontrol": "https://raw.githubusercontent.com/MonitorControl/MonitorControl/master/MonitorControl/Assets.xcassets/AppIcon.appiconset/icon_512x512@2x.png",
    "latest": "https://raw.githubusercontent.com/mangerlahn/Latest/master/Latest/Assets.xcassets/AppIcon.appiconset/icon_512x512@2x.png",
    "keka": "https://www.keka.io/img/keka-icon.png",
    "homebrew": "https://raw.githubusercontent.com/Homebrew/brew/master/docs/assets/img/homebrew.png",
    "ollama": "https://ollama.com/public/ollama.png",
    "jan": "https://raw.githubusercontent.com/janhq/jan/dev/assets/jan.png",
    "chatbox": "https://raw.githubusercontent.com/Bin-Huang/chatbox/main/resources/icon.png",
    "vlc": "https://images.videolan.org/images/icons-VLC/vlc-xmas.png",
    "handbrake": "https://handbrake.fr/img/logo.png",
    "audacity": "https://raw.githubusercontent.com/audacity/audacity/master/presets/audacity.png",
    "losslesscut": "https://raw.githubusercontent.com/mifi/lossless-cut/master/src/icon.png",
    "obs-studio": "https://obsproject.com/assets/images/obs_studio_community.png",
    "bitwarden": "https://raw.githubusercontent.com/bitwarden/clients/main/apps/desktop/resources/icons/512x512.png",
    "keepassxc": "https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/share/icons/application/512x512/apps/keepassxc.png",
    "cryptomator": "https://raw.githubusercontent.com/cryptomator/cryptomator/develop/dist/mac/AppIcon.iconset/icon_512x512@2x.png",
    "logseq": "https://raw.githubusercontent.com/logseq/logseq/master/resources/icon.png",
    "joplin": "https://joplinapp.org/images/Icon.png",
    "appflowy": "https://raw.githubusercontent.com/AppFlowy-IO/AppFlowy/main/frontend/resources/icon.png",
    "zettlr": "https://raw.githubusercontent.com/Zettlr/Zettlr/develop/resources/icons/png/512x512.png",
    "marktext": "https://raw.githubusercontent.com/marktext/marktext/develop/resources/icons/512x512.png",
    "localsend": "https://raw.githubusercontent.com/localsend/localsend/main/assets/img/logo-512.png",
    "cyberduck": "https://cyberduck.io/img/cyberduck-icon-512.png",
    "transmission": "https://transmissionbt.com/images/transmission-app-icon.png",
    "syncthing-macos": "https://raw.githubusercontent.com/syncthing/syncthing-macos/master/syncthing/Assets.xcassets/AppIcon.appiconset/AppIcon_512x512@2x.png",
    "blender": "https://www.blender.org/wp-content/themes/bthree/assets/images/blender-logo-icon.png",
    "inkscape": "https://inkscape.org/static/images/inkscape-logo.svg",
    "gimp": "https://www.gimp.org/images/frontpage/wilber-big.png",
    "krita": "https://krita.org/wp-content/themes/krita-org-theme/images/krita-logo.svg",
    "karabiner-elements": "https://karabiner-elements.pqrs.org/images/apple-touch-icon.png",
    "sensible-side-buttons": "https://sensible-side-buttons.archagon.net/favicon.png",
    "macvim": "https://raw.githubusercontent.com/macvim-dev/macvim/master/src/MacVim/icons/macvim.png",
    "hidden-bar": "https://raw.githubusercontent.com/dwarvesf/hidden/master/Hidden/Assets.xcassets/AppIcon.appiconset/icon_512x512@2x.png",
    "amethyst": "https://raw.githubusercontent.com/ianyh/Amethyst/master/Amethyst/Assets.xcassets/AppIcon.appiconset/icon_512x512@2x.png",
    "gitup": "https://raw.githubusercontent.com/git-up/GitUp/master/GitUp/Images.xcassets/AppIcon.appiconset/icon_512x512@2x.png",
    "beekeeper-studio": "https://raw.githubusercontent.com/beekeeper-studio/beekeeper-studio/master/static/icon.png",
    "lulu": "https://objective-see.org/images/products/lulu.png",
    "knockknock": "https://objective-see.org/images/products/knockknock.png",
    "tor-browser": "https://www.torproject.org/static/images/tor-browser-icon.png"
}

def extract_repo_images(gh_url: str) -> list:
    """Scrapes README images from repository page HTML."""
    try:
        req = urllib.request.Request(gh_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=6) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            # Find images inside markdown body or article
            imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', html)
            clean = []
            for img in imgs:
                if any(bad in img for bad in ["shields.io", "badge", "workflow", "action", "star", "fork", "sponsor"]):
                    continue
                if img.startswith("/"):
                    img = "https://github.com" + img
                clean.append(img)
            return clean
    except Exception:
        return []

def download_image(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=8) as resp:
        return resp.read()

def process_and_save_icon(data: bytes, project_id: str, is_svg=False) -> str:
    out_dir = "icons/project-icons"
    os.makedirs(out_dir, exist_ok=True)

    if is_svg or data.startswith(b"<svg") or b"<svg" in data[:100]:
        dest = os.path.join(out_dir, f"{project_id}.svg")
        with open(dest, "wb") as f:
            f.write(data)
        return dest

    # Raster image: open with Pillow
    img = Image.open(io.BytesIO(data))
    img = img.convert("RGBA")
    # Resize to high quality 256x256
    img = img.resize((256, 256), Image.Resampling.LANCZOS)
    dest = os.path.join(out_dir, f"{project_id}.png")
    img.save(dest, "PNG", optimize=True)
    return dest

def main():
    proj_path = os.path.join("data", "projects.yml")
    with open(proj_path, "r", encoding="utf-8") as f:
        proj_data = yaml.safe_load(f)
    projects = proj_data.get("projects", [])

    print(f"Fetching official authentic icons for {len(projects)} projects...\n")
    success_count = 0

    for idx, p in enumerate(projects, start=1):
        pid = p["id"]
        name = p["name"]
        gh = p["github"]
        owner = gh.split("github.com/")[-1].split("/")[0]
        repo = gh.split("github.com/")[-1].split("/")[1]

        candidates = []
        if pid in KNOWN_ICON_URLS:
            candidates.append(KNOWN_ICON_URLS[pid])

        # Try README images
        readme_imgs = extract_repo_images(gh)
        for img_url in readme_imgs:
            if any(term in img_url.lower() for term in ["icon", "logo", "appicon", "app"]):
                candidates.append(img_url)

        # Fallback to org/user avatar (official logo on GitHub)
        candidates.append(f"https://github.com/{owner}.png?size=256")

        saved = False
        for url in candidates:
            try:
                data = download_image(url)
                if len(data) < 500:
                    continue
                is_svg = url.endswith(".svg") or b"<svg" in data[:100]
                dest_path = process_and_save_icon(data, pid, is_svg=is_svg)
                p["icon"] = dest_path
                print(f"[{idx:2d}/{len(projects)}] ✓ {name} ({pid}) -> {dest_path} (from {url[:60]}...)")
                saved = True
                success_count += 1
                break
            except Exception as e:
                continue

        if not saved:
            print(f"[{idx:2d}/{len(projects)}] ⚠️  Could not fetch live icon for {name}, keeping existing.")

    # Save updated projects.yml
    with open(proj_path, "w", encoding="utf-8") as f:
        yaml.dump(proj_data, f, sort_keys=False, allow_unicode=True)

    print(f"\nCompleted! Successfully fetched {success_count}/{len(projects)} authentic project icons.")

if __name__ == "__main__":
    main()

