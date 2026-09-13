<div align="center">

<img src="./icons/logo.svg" width="340" alt="OpenMac Logo">

# OpenMac

**The community-powered directory of genuinely open-source macOS apps, developer tools, and system utilities.**

<!-- STATS:START -->
[![Total Projects](https://img.shields.io/badge/Projects-722-blue.svg?style=flat-square)](#all-categories) [![Categories](https://img.shields.io/badge/Categories-50-indigo.svg?style=flat-square)](#table-of-contents) [![100% Open Source](https://img.shields.io/badge/Source-100%25%20Open%20Source-emerald.svg?style=flat-square)](#selection-criteria) [![macOS Compatible](https://img.shields.io/badge/Platform-macOS-000000.svg?logo=apple&style=flat-square)](#selection-criteria)
<!-- STATS:END -->

<p align="center">
  <a href="#table-of-contents"><b>Explore Categories</b></a> •
  <a href="#featured-projects"><b>Featured Apps</b></a> •
  <a href="#all-categories"><b>All Apps</b></a> •
  <a href="#how-to-contribute"><b>Add a Project</b></a> •
  <a href="./CONTRIBUTING.md"><b>Contribution Guide</b></a> •
  <a href="https://github.com/shareefmx/OpenMac/issues/new?template=add-project.yml"><b>1-Click Submit</b></a>
</p>

---

</div>

<a id="about"></a>
## 📖 About OpenMac

**OpenMac** is a curated, transparent, community-maintained catalog dedicated exclusively to **free and open-source software (FOSS)** built for macOS.

While directories like *awesome-mac* provide great utility, they frequently mix open-source software with closed-source freeware, proprietary trials, and commercial subscriptions. **OpenMac establishes a clear, uncompromising standard:**

> [!IMPORTANT]
> **The Golden Rule**: Every listed application in this directory must have a **publicly accessible source code repository** and operate under a recognized **OSI or FSF-approved open-source license**. No closed-source freeware. No proprietary freemium apps. No telemetry-heavy trials.

### Why Developers and Mac Users Love OpenMac
- 🛡️ **Auditability & Privacy**: Inspect the code running on your system. Know exactly what handles your clipboard, keystrokes, and network traffic.
- ⚡ **Native Performance**: Prioritizes modern Swift, SwiftUI, Rust, and Metal-accelerated tools tuned for Apple Silicon and Intel Macs.
- 🤖 **Automated & Verified**: Canonical metadata is strictly validated via automated CI to guarantee no dead links, missing icons, or license misrepresentations.
- 🤝 **Community-Governed**: Maintained by Mac developers and enthusiasts worldwide. Fork, submit, and improve.

---

<a id="table-of-contents"></a>
<a id="categories"></a>
## 🧭 Table of Contents

<!-- TOC:START -->
| Category | Focus Area | Projects |
| :--- | :--- | :---: |
| 🎵 [**Audio**](#audio) | Audio recorders, sound equalizers, routing drivers, and microphone controllers. | [`38 apps`](#audio) |
| 💾 [**Backup**](#backup) | Snapshot tools, Time Machine helpers, volume cloners, and data protection utilities. | [`6 apps`](#backup) |
| 🌐 [**Browser**](#browser) | Open-source web browsers, privacy navigation tools, and lightweight web viewing engines. | [`13 apps`](#browser) |
| 💬 [**Chat**](#chat) | Instant messaging, Matrix, IRC, Telegram, WhatsApp wrappers, and team communication. | [`20 apps`](#chat) |
| 💰 [**Cryptocurrency**](#cryptocurrency) | Cryptocurrency wallets, node runners, portfolio trackers, and blockchain tools. | [`5 apps`](#cryptocurrency) |
| 🗄️ [**Database**](#database) | Modern database GUIs, SQL query editors, Redis managers, and SQLite visualizers. | [`17 apps`](#database) |
| 👨‍💻 [**Development**](#development) | General developer utilities, SDK managers, reverse engineering suites, and debugging tools. | [`28 apps`](#development) |
| 📦 [**Git**](#git) | Native Git GUI clients, visual diff inspection tools, commit helpers, and merge assistants. | [`18 apps`](#git) |
| 📱 [**iOS / macOS**](#ios-macos) | Apple ecosystem tooling, Xcode enhancements, provisioning helpers, and simulator utilities. | [`41 apps`](#ios-macos) |
| 🔄 [**JSON Parsing**](#json-parsing) | JSON formatters, syntax highlighters, schema validators, and data tree inspectors. | [`4 apps`](#json-parsing) |
| 🔧 [**Other Development**](#other-development) | Specialized developer tools, regex visualizers, string processors, and testing utilities. | [`5 apps`](#other-development) |
| 🌍 [**Web Development**](#web-development) | Local web servers, HTTP debugging proxies, static site generators, and API inspection tools. | [`14 apps`](#web-development) |
| ⬇️ [**Downloader**](#downloader) | Media downloaders, YouTube download utilities, Homebrew cask grabbers, and batch fetchers. | [`10 apps`](#downloader) |
| 📝 [**Editors**](#editors) | General text and code editors, native macOS typing suites, and distraction-free editors. | [`6 apps`](#editors) |
| 📊 [**CSV**](#csv) | Tabular data viewers, spreadsheet inspectors, and high-speed CSV file editors. | [`1 apps`](#csv) |
| 📋 [**JSON**](#json) | Dedicated JSON documents editors, structure organizers, and tree manipulation apps. | [`2 apps`](#json) |
| 📝 [**Markdown**](#markdown) | Markdown editors, live preview tools, note renderers, and technical documentation writers. | [`9 apps`](#markdown) |
| 📐 [**TeX**](#tex) | LaTeX typesetting tools, mathematical formula editors, and academic paper generators. | [`2 apps`](#tex) |
| ✏️ [**Text**](#text) | Plain text scratchpads, notepad alternatives, and distraction-free writing environments. | [`7 apps`](#text) |
| 🧩 [**Extensions**](#extensions) | Quick Look generators, Finder context menu extensions, and share sheet utilities. | [`13 apps`](#extensions) |
| 🔍 [**Finder**](#finder) | Finder enhancements, folder bookmarkers, duplicate detectors, and advanced file browsers. | [`13 apps`](#finder) |
| 🎮 [**Games**](#games) | Open-source games, console emulators, game engines, and recreational apps for macOS. | [`13 apps`](#games) |
| 🎨 [**Graphics**](#graphics) | Vector design tools, 3D rendering packages, animation software, and diagramming apps. | [`17 apps`](#graphics) |
| 💻 [**IDE**](#ide) | Full-fledged integrated development environments supporting multiple programming stacks. | [`6 apps`](#ide) |
| 🖼️ [**Images**](#images) | Image viewing apps, screenshot annotation suites, image optimizers, and color managers. | [`12 apps`](#images) |
| ⌨️ [**Keyboard**](#keyboard) | Key remap utilities, shortcut cheatsheets, keyboard layout managers, and typing assists. | [`11 apps`](#keyboard) |
| 📧 [**Mail**](#mail) | Desktop email clients, menubar notification checkers, and inbox management tools. | [`6 apps`](#mail) |
| 🏥 [**Medical**](#medical) | DICOM viewers, medical image visualizers, and healthcare workstation applications. | [`1 apps`](#medical) |
| 📊 [**Menubar**](#menubar) | Menu bar monitors, notch managers, status bar applets, and quick-access widgets. | [`53 apps`](#menubar) |
| 🎧 [**Music**](#music) | Music players, lyrics synchronizers, audio taggers, and streaming service desktop clients. | [`10 apps`](#music) |
| 📰 [**News**](#news) | RSS and Atom feed readers, news aggregators, and headline notification monitors. | [`5 apps`](#news) |
| 📔 [**Notes**](#notes) | Note-taking applications, personal knowledge bases, digital journals, and thought planners. | [`18 apps`](#notes) |
| 📦 [**Other**](#other) | Curated collection of unique, miscellaneous, and versatile macOS tools and utilities. | [`24 apps`](#other) |
| ▶️ [**Player**](#player) | Dedicated lightweight audio and media playback applications for macOS. | [`3 apps`](#player) |
| 🎙️ [**Podcast**](#podcast) | Podcast players, chapter indexers, episode downloaders, and RSS audio subscriptions. | [`6 apps`](#podcast) |
| ⏱️ [**Productivity**](#productivity) | Application launchers, clipboard managers, pomodoro timers, and daily workflow enhancers. | [`64 apps`](#productivity) |
| 🌙 [**Screensaver**](#screensaver) | Aesthetic screensavers, clock displays, retro animations, and dynamic ambient visuals. | [`10 apps`](#screensaver) |
| 🔒 [**Security**](#security) | Password vaults, personal application firewalls, disk encryption, and network monitors. | [`13 apps`](#security) |
| 📤 [**Sharing Files**](#sharing-files) | P2P file transfer tools, AirDrop alternatives, local network sharing, and file sync apps. | [`11 apps`](#sharing-files) |
| 👥 [**Social Networking**](#social-networking) | Clients for decentralized social networks, Mastodon, Bluesky, and community platforms. | [`9 apps`](#social-networking) |
| 📡 [**Streaming**](#streaming) | Live broadcasting suites, desktop capture utilities, and livestream management apps. | [`2 apps`](#streaming) |
| ⚙️ [**System**](#system) | System diagnostics, hardware monitors, uninstallation cleaners, and maintenance apps. | [`23 apps`](#system) |
| 📺 [**Terminal**](#terminal) | Modern terminal emulators, shell accelerators, multiplexers, and prompt personalizers. | [`14 apps`](#terminal) |
| 🎚️ [**Touch Bar**](#touch-bar) | MacBook Pro Touch Bar customization utilities, widgets, and mini tactile applets. | [`6 apps`](#touch-bar) |
| 🛠️ [**Utilities**](#utilities) | Everyday Mac utilities, mouse accelerators, audio routers, and desktop tools. | [`57 apps`](#utilities) |
| 🔐 [**VPN & Proxy**](#vpn-proxy) | WireGuard, OpenVPN, Shadowsocks clients, and local network proxy toggle utilities. | [`7 apps`](#vpn-proxy) |
| 🎬 [**Video**](#video) | Video players, subtitle editors, video encoders, and multimedia conversion tools. | [`19 apps`](#video) |
| 🖥️ [**Wallpaper**](#wallpaper) | Dynamic wallpaper rotators, aerial desktop engines, and custom wallpaper creators. | [`11 apps`](#wallpaper) |
| 🪟 [**Window Management**](#window-management) | Tiling window managers, keyboard snap helpers, and window switcher enhancements. | [`14 apps`](#window-management) |
| 🤖 [**AI & Machine Learning**](#ai-ml) | Local large language model runners, desktop AI frontends, and on-device ML workflows. | [`5 apps`](#ai-ml) |
<!-- TOC:END -->

---

<a id="featured-projects"></a>
## ⭐ Featured Projects

A curated selection of standout, mature, and widely acclaimed open-source macOS software distinguished by active community maintenance, exceptional UX, and deep platform integration.

<!-- FEATURED:START -->
| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://nikitabobko.github.io/AeroSpace"><img src="./icons/project-icons/aerospace.png" width="32" height="32" alt="AeroSpace"></a> | **[AeroSpace](https://nikitabobko.github.io/AeroSpace)** | i3-like tiling window manager for macOS with tree-based workspace navigation. | `Swift` | [Website](https://nikitabobko.github.io/AeroSpace) • [Code](https://github.com/nikitabobko/AeroSpace) | `MIT` |
| <a href="https://alt-tab-macos.netlify.app"><img src="./icons/project-icons/alt-tab-macos.svg" width="32" height="32" alt="AltTab"></a> | **[AltTab](https://alt-tab-macos.netlify.app)** | Brings Windows-style alt-tab window switcher functionality with live window previews to macOS. | `Swift` | [Website](https://alt-tab-macos.netlify.app) • [Code](https://github.com/lwouis/alt-tab-macos) | `GPL-3.0` |
| <a href="https://bitwarden.com"><img src="./icons/project-icons/bitwarden.png" width="32" height="32" alt="Bitwarden"></a> | **[Bitwarden](https://bitwarden.com)** | Trusted open-source password manager with end-to-end encryption across all your devices. | `TypeScript` | [Website](https://bitwarden.com) • [Code](https://github.com/bitwarden/clients) | `GPL-3.0` |
| <a href="https://www.blender.org"><img src="./icons/project-icons/blender.png" width="32" height="32" alt="Blender"></a> | **[Blender](https://www.blender.org)** | Open-source 3D creation suite supporting modeling, rigging, animation, simulation, and rendering with Metal. | `C++` | [Website](https://www.blender.org) • [Code](https://github.com/blender/blender) | `GPL-3.0` |
| <a href="https://www.usebruno.com"><img src="./icons/project-icons/bruno.png" width="32" height="32" alt="Bruno"></a> | **[Bruno](https://www.usebruno.com)** | Fast, git-friendly open-source API client for exploring and testing REST and GraphQL APIs. | `JavaScript` | [Website](https://www.usebruno.com) • [Code](https://github.com/usebruno/bruno) | `MIT` |
| <a href="https://ghostty.org"><img src="./icons/project-icons/ghostty.png" width="32" height="32" alt="Ghostty"></a> | **[Ghostty](https://ghostty.org)** | Fast, feature-rich, and cross-platform terminal emulator leveraging native macOS UI and GPU acceleration. | `Zig` | [Website](https://ghostty.org) • [Code](https://github.com/ghostty-org/ghostty) | `MIT` |
| <a href="https://brew.sh"><img src="./icons/project-icons/homebrew.png" width="32" height="32" alt="Homebrew"></a> | **[Homebrew](https://brew.sh)** | The missing package manager for macOS and Linux, installing software packages from the CLI. | `Ruby` | [Website](https://brew.sh) • [Code](https://github.com/Homebrew/brew) | `BSD-2-Clause` |
| <a href="https://iina.io"><img src="./icons/project-icons/iina.png" width="32" height="32" alt="IINA"></a> | **[IINA](https://iina.io)** | The modern media player for macOS, built with Swift and powered by mpv with native Picture-in-Picture. | `Swift` | [Website](https://iina.io) • [Code](https://github.com/iina/iina) | `GPL-3.0` |
| <a href="https://iterm2.com"><img src="./icons/project-icons/iterm2.png" width="32" height="32" alt="iTerm2"></a> | **[iTerm2](https://iterm2.com)** | Full-featured macOS terminal emulator with split panes, search, autocomplete, and tmux integration. | `Objective-C` | [Website](https://iterm2.com) • [Code](https://github.com/gnachman/iTerm2) | `GPL-2.0` |
| <a href="https://jan.ai"><img src="./icons/project-icons/jan.png" width="32" height="32" alt="Jan"></a> | **[Jan](https://jan.ai)** | Open-source local AI conversational assistant that runs offline on your Mac with zero data tracking. | `TypeScript` | [Website](https://jan.ai) • [Code](https://github.com/janhq/jan) | `AGPL-3.0` |
| <a href="https://karabiner-elements.pqrs.org"><img src="./icons/project-icons/karabiner-elements.png" width="32" height="32" alt="Karabiner-Elements"></a> | **[Karabiner-Elements](https://karabiner-elements.pqrs.org)** | Powerful and stable keyboard customizer for macOS to remap keys and create complex modification rules. | `C++` | [Website](https://karabiner-elements.pqrs.org) • [Code](https://github.com/pqrs-org/Karabiner-Elements) | `MIT` |
| <a href="https://localsend.org"><img src="./icons/project-icons/localsend.png" width="32" height="32" alt="LocalSend"></a> | **[LocalSend](https://localsend.org)** | AirDrop alternative to share files and messages nearby across macOS, iOS, Android, and Windows. | `Dart` | [Website](https://localsend.org) • [Code](https://github.com/localsend/localsend) | `MIT` |
| <a href="https://logseq.com"><img src="./icons/project-icons/logseq.png" width="32" height="32" alt="Logseq"></a> | **[Logseq](https://logseq.com)** | Privacy-first, local-only platform for knowledge management and outliner journaling. | `Clojure` | [Website](https://logseq.com) • [Code](https://github.com/logseq/logseq) | `AGPL-3.0` |
| <a href="https://objective-see.org/products/lulu.html"><img src="./icons/project-icons/lulu.png" width="32" height="32" alt="LuLu"></a> | **[LuLu](https://objective-see.org/products/lulu.html)** | Free, open-source macOS firewall aimed at blocking unauthorized outgoing network connections. | `Objective-C` | [Website](https://objective-see.org/products/lulu.html) • [Code](https://github.com/objective-see/LuLu) | `GPL-3.0` |
| <a href="https://maccy.app"><img src="./icons/project-icons/maccy.png" width="32" height="32" alt="Maccy"></a> | **[Maccy](https://maccy.app)** | Lightweight, native clipboard manager with search history and zero telemetry. | `Swift` | [Website](https://maccy.app) • [Code](https://github.com/p0deje/Maccy) | `MIT` |
| <a href="https://ollama.com"><img src="./icons/project-icons/ollama.png" width="32" height="32" alt="Ollama"></a> | **[Ollama](https://ollama.com)** | Get up and running with large language models locally on Apple Silicon and Intel Macs. | `Go` | [Website](https://ollama.com) • [Code](https://github.com/ollama/ollama) | `MIT` |
| <a href="https://github.com/alienator88/Pearcleaner"><img src="./icons/project-icons/pearcleaner.png" width="32" height="32" alt="Pearcleaner"></a> | **[Pearcleaner](https://github.com/alienator88/Pearcleaner)** | Open-source Mac app uninstaller inspired by AppCleaner, written cleanly in native SwiftUI. | `Swift` | [Code](https://github.com/alienator88/Pearcleaner) | `GPL-3.0` |
| <a href="https://rectangleapp.com"><img src="./icons/project-icons/rectangle.png" width="32" height="32" alt="Rectangle"></a> | **[Rectangle](https://rectangleapp.com)** | Move and resize windows on macOS using keyboard shortcuts and snap areas. | `Swift` | [Website](https://rectangleapp.com) • [Code](https://github.com/rxhanson/Rectangle) | `MIT` |
| <a href="https://github.com/exelban/stats"><img src="./icons/project-icons/stats.png" width="32" height="32" alt="Stats"></a> | **[Stats](https://github.com/exelban/stats)** | Menu bar system monitor showing CPU, GPU, memory, disks, sensors, battery, and network speeds. | `Swift` | [Code](https://github.com/exelban/stats) | `MIT` |
| <a href="https://vscodium.com"><img src="./icons/project-icons/vscodium.svg" width="32" height="32" alt="VSCodium"></a> | **[VSCodium](https://vscodium.com)** | Community-driven, telemetry-free binary distribution of Microsoft's VS Code editor. | `TypeScript` | [Website](https://vscodium.com) • [Code](https://github.com/VSCodium/vscodium) | `MIT` |
| <a href="https://zed.dev"><img src="./icons/project-icons/zed.png" width="32" height="32" alt="Zed"></a> | **[Zed](https://zed.dev)** | High-performance, multiplayer code editor written in Rust with GPU-accelerated rendering. | `Rust` | [Website](https://zed.dev) • [Code](https://github.com/zed-industries/zed) | `GPL-3.0` |
<!-- FEATURED:END -->

---

<a id="all-categories"></a>
## 🗂️ All Categories

<!-- PROJECTS:START -->
<a id="audio"></a>
### 🎵 Audio

> Audio recorders, sound equalizers, routing drivers, and microphone controllers.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/CocoaHeadsBrasil/MuteUnmuteMic"><img src="./icons/project-icons/un-mutemic.png" width="32" height="32" alt="[Un]MuteMic"></a> | **[[Un]MuteMic](https://github.com/CocoaHeadsBrasil/MuteUnmuteMic)** | macOS app to mute & unmute the input volume of your microphone. Perfect for podcasters. | `Objective-C` | [Source](https://github.com/CocoaHeadsBrasil/MuteUnmuteMic) | `MIT` |
| <a href="https://www.audacityteam.org"><img src="./icons/project-icons/audacity.png" width="32" height="32" alt="Audacity"></a> | **[Audacity](https://www.audacityteam.org)** | Multi-track audio editor and recorder offering high-resolution recording and sound manipulation. | `C++` | [Website](https://www.audacityteam.org) • [Source](https://github.com/audacity/audacity) | `GPL-3.0` |
| <a href="https://github.com/vgorloff/AUHost"><img src="./icons/project-icons/auhost.png" width="32" height="32" alt="AUHost"></a> | **[AUHost](https://github.com/vgorloff/AUHost)** | Application which hosts AudioUnits v3 using AVFoundation API. | `Swift` | [Source](https://github.com/vgorloff/AUHost) | `MIT` |
| <a href="https://github.com/kartik-venugopal/aural-player"><img src="./icons/project-icons/aural-player.png" width="32" height="32" alt="Aural Player"></a> | **[Aural Player](https://github.com/kartik-venugopal/aural-player)** | Aural Player is a audio player application for the macOS platform. Inspired by the classic Winamp player for Windows, it is designed to be to-the-point and easy to use. | `Swift` | [Source](https://github.com/kartik-venugopal/aural-player) | `MIT` |
| <a href="https://yoni.ninja/automute"><img src="./icons/project-icons/automute.png" width="32" height="32" alt="AutoMute"></a> | **[AutoMute](https://yoni.ninja/automute)** | Automatically mute the sound when headphones disconnect / Mac awake from sleep. | `Objective-C` | [Website](https://yoni.ninja/automute) • [Source](https://github.com/yonilevy/automute) | `MIT` |
| <a href="https://github.com/kyleneideck/BackgroundMusic"><img src="./icons/project-icons/background-music.png" width="32" height="32" alt="Background Music"></a> | **[Background Music](https://github.com/kyleneideck/BackgroundMusic)** | Background Music, a macOS audio utility: automatically pause your music, set individual apps' volumes and record system audio. | `C++` | [Source](https://github.com/kyleneideck/BackgroundMusic) | `MIT` |
| <a href="https://existential.audio/blackhole"><img src="./icons/project-icons/blackhole.png" width="32" height="32" alt="BlackHole"></a> | **[BlackHole](https://existential.audio/blackhole)** | Virtual audio loopback driver that allows applications to pass audio to other applications. | `C` | [Website](https://existential.audio/blackhole) • [Source](https://github.com/ExistentialAudio/BlackHole) | `GPL-3.0` |
| <a href="https://github.com/hanayik/CAM"><img src="./icons/project-icons/cam.png" width="32" height="32" alt="CAM"></a> | **[CAM](https://github.com/hanayik/CAM)** | macOS camera recording using ffmpeg | `JavaScript` | [Source](https://github.com/hanayik/CAM) | `MIT` |
| <a href="https://www.clementine-player.org"><img src="./icons/project-icons/clementine.png" width="32" height="32" alt="Clementine"></a> | **[Clementine](https://www.clementine-player.org)** | Clementine is a modern music player and library organizer for Windows, Linux and macOS. | `C++` | [Website](https://www.clementine-player.org) • [Source](https://github.com/clementine-player/Clementine) | `MIT` |
| <a href="https://cogx.org"><img src="./icons/project-icons/cog.svg" width="32" height="32" alt="Cog"></a> | **[Cog](https://cogx.org)** | Cog is an open source audio player for macOS. The basic layout is a single-paned playlist interface with two retractable drawers, one for navigating the user's music folders and another for viewing audio file properties, like bitrate. | `Objective-C` | [Website](https://cogx.org) • [Source](https://bitbucket.org/losnoco/cog/src) | `MIT` |
| <a href="https://github.com/bitgapp/eqMac"><img src="./icons/project-icons/eqmac2.png" width="32" height="32" alt="eqMac2"></a> | **[eqMac2](https://github.com/bitgapp/eqMac)** | System-Wide Equalizer for the Mac. | `C++` | [Source](https://github.com/bitgapp/eqMac) | `MIT` |
| <a href="https://github.com/enzo1982/freac"><img src="./icons/project-icons/fre-ac.png" width="32" height="32" alt="fre:ac"></a> | **[fre:ac](https://github.com/enzo1982/freac)** | The fre:ac audio converter project. | `C++` | [Source](https://github.com/enzo1982/freac) | `MIT` |
| <a href="https://github.com/melissa-pereira-deel/home-rec"><img src="./icons/project-icons/homerec.png" width="32" height="32" alt="HomeRec"></a> | **[HomeRec](https://github.com/melissa-pereira-deel/home-rec)** | Lightweight native macOS app for recording system audio as high-quality WAV files using ScreenCaptureKit. | `Swift` | [Source](https://github.com/melissa-pereira-deel/home-rec) | `MIT` |
| <a href="https://github.com/alberti42/iTunes-Volume-Control"><img src="./icons/project-icons/itunes-volume-control.png" width="32" height="32" alt="iTunes-Volume-Control"></a> | **[iTunes-Volume-Control](https://github.com/alberti42/iTunes-Volume-Control)** | This app allows you to control the iTunes volume using volume up and volume down hotkeys. | `Objective-C` | [Source](https://github.com/alberti42/iTunes-Volume-Control) | `MIT` |
| <a href="https://github.com/jcm93/jmc"><img src="./icons/project-icons/jmc.png" width="32" height="32" alt="jmc"></a> | **[jmc](https://github.com/jcm93/jmc)** | jmc is new macOS media organizer. | `Swift` | [Source](https://github.com/jcm93/jmc) | `MIT` |
| <a href="https://www.karaoke-eternal.com"><img src="./icons/project-icons/karaoke-forever.png" width="32" height="32" alt="Karaoke Forever"></a> | **[Karaoke Forever](https://www.karaoke-eternal.com)** | Host awesome karaoke parties where everyone can queue songs from their phone's browser. Plays MP3+G and MP4 with WebGL visualizations. | `JavaScript` | [Website](https://www.karaoke-eternal.com) • [Source](https://github.com/bhj/KaraokeEternal) | `MIT` |
| <a href="https://github.com/dsward2/LocalRadio"><img src="./icons/project-icons/localradio.png" width="32" height="32" alt="LocalRadio"></a> | **[LocalRadio](https://github.com/dsward2/LocalRadio)** | LocalRadio is software for listening to "Software-Defined Radio" on your Mac and mobile devices. | `Objective-C` | [Source](https://github.com/dsward2/LocalRadio) | `MIT` |
| <a href="https://github.com/ateymoori/lyricglow"><img src="./icons/project-icons/lyricglow.png" width="32" height="32" alt="LyricGlow"></a> | **[LyricGlow](https://github.com/ateymoori/lyricglow)** | macOS application displaying synchronized lyrics with animated word-by-word glow effects for Spotify, Apple Music, and YouTube Music. | `JavaScript` | [Source](https://github.com/ateymoori/lyricglow) | `MIT` |
| <a href="https://github.com/lyc2345/Lyricism"><img src="./icons/project-icons/lyricism.png" width="32" height="32" alt="Lyricism"></a> | **[Lyricism](https://github.com/lyc2345/Lyricism)** | macOS app to show you lyric what currently iTunes or Spotify is playing. | `Objective-C` | [Source](https://github.com/lyc2345/Lyricism) | `MIT` |
| <a href="https://github.com/ddddxxx/LyricsX"><img src="./icons/project-icons/lyricsx.png" width="32" height="32" alt="LyricsX"></a> | **[LyricsX](https://github.com/ddddxxx/LyricsX)** | Lyrics for iTunes, Spotify and Vox. | `Swift` | [Source](https://github.com/ddddxxx/LyricsX) | `MIT` |
| <a href="https://github.com/bsdelf/mous"><img src="./icons/project-icons/mous-player.png" width="32" height="32" alt="Mous Player"></a> | **[Mous Player](https://github.com/bsdelf/mous)** | Simple yet powerful audio player for BSD/Linux/macOS. | `C++` | [Source](https://github.com/bsdelf/mous) | `MIT` |
| <a href="https://mpv.io"><img src="./icons/project-icons/mpv.png" width="32" height="32" alt="MPV"></a> | **[MPV](https://mpv.io)** | Lightweight, highly configurable media player. | `C` | [Website](https://mpv.io) • [Source](https://github.com/mpv-player/mpv) | `MIT` |
| <a href="https://github.com/insidegui/NoiseBuddy"><img src="./icons/project-icons/noisebuddy.png" width="32" height="32" alt="NoiseBuddy"></a> | **[NoiseBuddy](https://github.com/insidegui/NoiseBuddy)** | Control the listening mode on your AirPods Pro in the Touch Bar or Menu Bar. | `Swift` | [Source](https://github.com/insidegui/NoiseBuddy) | `MIT` |
| <a href="https://github.com/nbolar/PlayStatus"><img src="./icons/project-icons/playstatus.png" width="32" height="32" alt="PlayStatus"></a> | **[PlayStatus](https://github.com/nbolar/PlayStatus)** | PlayStatus is a macOS app that allows the control of Spotify and iTunes music playback from the menu bar. | `Swift` | [Source](https://github.com/nbolar/PlayStatus) | `MIT` |
| <a href="https://www.plugformac.com"><img src="./icons/project-icons/plug.png" width="32" height="32" alt="Plug"></a> | **[Plug](https://www.plugformac.com)** | Discover and listen to music from Hype Machine. | `Swift` | [Website](https://www.plugformac.com) • [Source](https://github.com/wulkano/Plug) | `MIT` |
| <a href="https://github.com/bazalp/pulp"><img src="./icons/project-icons/pulp.svg" width="32" height="32" alt="Pulp"></a> | **[Pulp](https://github.com/bazalp/pulp)** | Audio Sample manager. | `Rust` | [Source](https://github.com/bazalp/pulp) | `MIT` |
| <a href="https://billthefarmer.github.io/audiotools"><img src="./icons/project-icons/scope.png" width="32" height="32" alt="Scope"></a> | **[Scope](https://billthefarmer.github.io/audiotools)** | Audio Oscilloscope for real-time macOS audio signal visualization | `Swift` | [Website](https://billthefarmer.github.io/audiotools) • [Source](https://github.com/billthefarmer/audiotools/tree/master/Scope/swift) | `MIT` |
| <a href="https://github.com/mikebrady/shairport-sync"><img src="./icons/project-icons/shairport-sync.png" width="32" height="32" alt="shairport-sync"></a> | **[shairport-sync](https://github.com/mikebrady/shairport-sync)** | macOS/Linux/FreeBSD/OpenBSD Airplay audio receiver. | `C` | [Source](https://github.com/mikebrady/shairport-sync) | `MIT` |
| <a href="https://github.com/ShazamScrobbler/shazamscrobbler-macos"><img src="./icons/project-icons/shazamscrobbler.png" width="32" height="32" alt="ShazamScrobbler"></a> | **[ShazamScrobbler](https://github.com/ShazamScrobbler/shazamscrobbler-macos)** | Scrobble vinyl, radios, movies to Last.fm. | `Objective-C` | [Source](https://github.com/ShazamScrobbler/shazamscrobbler-macos) | `MIT` |
| <a href="https://github.com/sonoramac/Sonora"><img src="./icons/project-icons/sonora.png" width="32" height="32" alt="Sonora"></a> | **[Sonora](https://github.com/sonoramac/Sonora)** | Minimal, beautifully designed music player for macOS. | `Objective-C` | [Source](https://github.com/sonoramac/Sonora) | `MIT` |
| <a href="https://github.com/fabiusBile/Spotify4BigSur"><img src="./icons/project-icons/spotify4bigsur.png" width="32" height="32" alt="Spotify4BigSur"></a> | **[Spotify4BigSur](https://github.com/fabiusBile/Spotify4BigSur)** | Spotify widget for Notification Center. | `Swift` | [Source](https://github.com/fabiusBile/Spotify4BigSur) | `MIT` |
| <a href="https://github.com/kmikiy/SpotMenu"><img src="./icons/project-icons/spotmenu.png" width="32" height="32" alt="SpotMenu"></a> | **[SpotMenu](https://github.com/kmikiy/SpotMenu)** | Spotify and iTunes in your menu bar. | `Objective-C` | [Source](https://github.com/kmikiy/SpotMenu) | `MIT` |
| <a href="https://github.com/will-stone/SpotSpot"><img src="./icons/project-icons/spotspot.png" width="32" height="32" alt="SpotSpot"></a> | **[SpotSpot](https://github.com/will-stone/SpotSpot)** | Spotify mini-player for macOS. | `JavaScript` | [Source](https://github.com/will-stone/SpotSpot) | `MIT` |
| <a href="https://github.com/stargatedaw/stargate"><img src="./icons/project-icons/stargatedaw.png" width="32" height="32" alt="StargateDAW"></a> | **[StargateDAW](https://github.com/stargatedaw/stargate)** | An all-in-one digital audio workstation (DAW) and plugin suite | `C` | [Source](https://github.com/stargatedaw/stargate) | `MIT` |
| <a href="https://github.com/Sunnyyoung/Suohai"><img src="./icons/project-icons/suohai.png" width="32" height="32" alt="Suohai"></a> | **[Suohai](https://github.com/Sunnyyoung/Suohai)** | Audio input/output source lock for macOS. | `Swift` | [Source](https://github.com/Sunnyyoung/Suohai) | `MIT` |
| <a href="https://github.com/yingDev/Tickeys"><img src="./icons/project-icons/tickeys.png" width="32" height="32" alt="Tickeys"></a> | **[Tickeys](https://github.com/yingDev/Tickeys)** | Instant audio feedback for typing. macOS version. | `Rust` | [Source](https://github.com/yingDev/Tickeys) | `MIT` |
| <a href="https://billthefarmer.github.io/ctuner"><img src="./icons/project-icons/tuner.png" width="32" height="32" alt="Tuner"></a> | **[Tuner](https://billthefarmer.github.io/ctuner)** | Musical Instrument Tuner | `Swift` | [Website](https://billthefarmer.github.io/ctuner) • [Source](https://github.com/billthefarmer/ctuner) | `MIT` |
| <a href="https://github.com/getoffmyhack/waveSDR"><img src="./icons/project-icons/wavesdr.png" width="32" height="32" alt="waveSDR"></a> | **[waveSDR](https://github.com/getoffmyhack/waveSDR)** | macOS native desktop Software Defined Radio application using the RTL-SDR USB device. | `Swift` | [Source](https://github.com/getoffmyhack/waveSDR) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="backup"></a>
### 💾 Backup

> Snapshot tools, Time Machine helpers, volume cloners, and data protection utilities.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/vdbsh/backy"><img src="./icons/project-icons/backy.png" width="32" height="32" alt="backy"></a> | **[backy](https://github.com/vdbsh/backy)** | Tiny multiprocessing utility for file backups. | `Go` | [Source](https://github.com/vdbsh/backy) | `MIT` |
| <a href="https://www.borgbase.com"><img src="./icons/project-icons/borgbase-vorta.png" width="32" height="32" alt="BorgBase/Vorta"></a> | **[BorgBase/Vorta](https://www.borgbase.com)** | Simple and Secure Offsite Backups | `Python` | [Website](https://www.borgbase.com) • [Source](https://github.com/borgbase) | `MIT` |
| <a href="https://github.com/lra/mackup"><img src="./icons/project-icons/mackup.png" width="32" height="32" alt="Mackup"></a> | **[Mackup](https://github.com/lra/mackup)** | Keep your application settings in sync (macOS/Linux). | `Python` | [Source](https://github.com/lra/mackup) | `MIT` |
| <a href="https://github.com/alichtman/shallow-backup"><img src="./icons/project-icons/shallow-backup.png" width="32" height="32" alt="shallow-backup"></a> | **[shallow-backup](https://github.com/alichtman/shallow-backup)** | Easily create lightweight documentation of installed applications, dotfiles, and more. | `Python` | [Source](https://github.com/alichtman/shallow-backup) | `MIT` |
| <a href="https://github.com/zenangst/Syncalicious"><img src="./icons/project-icons/syncalicious.png" width="32" height="32" alt="Syncalicious"></a> | **[Syncalicious](https://github.com/zenangst/Syncalicious)** | Keeping multiple macOS preferences in sync can be painful, but it shouldn't be. | `Swift` | [Source](https://github.com/zenangst/Syncalicious) | `MIT` |
| <a href="https://github.com/uroni/urbackup_backend"><img src="./icons/project-icons/urbackup.png" width="32" height="32" alt="UrBackup"></a> | **[UrBackup](https://github.com/uroni/urbackup_backend)** | UrBackup is Client/Server network backup for Windows, macOS and Linux. | `C++` | [Source](https://github.com/uroni/urbackup_backend) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="browser"></a>
### 🌐 Browser

> Open-source web browsers, privacy navigation tools, and lightweight web viewing engines.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/beakerbrowser/beaker"><img src="./icons/project-icons/beaker-browser.png" width="32" height="32" alt="Beaker Browser"></a> | **[Beaker Browser](https://github.com/beakerbrowser/beaker)** | Beaker is an experimental peer-to-peer Web browser. | `JavaScript` | [Source](https://github.com/beakerbrowser/beaker) | `MIT` |
| <a href="https://github.com/brave/brave-browser"><img src="./icons/project-icons/brave-browser.png" width="32" height="32" alt="Brave Browser"></a> | **[Brave Browser](https://github.com/brave/brave-browser)** | Brave browser for Desktop and Laptop computers running Windows, macOS, and Linux. | `JavaScript` | [Source](https://github.com/brave/brave-browser) | `MIT` |
| <a href="https://github.com/will-stone/browserosaurus"><img src="./icons/project-icons/browserosaurus.png" width="32" height="32" alt="browserosaurus"></a> | **[browserosaurus](https://github.com/will-stone/browserosaurus)** | macOS tool that prompts you to choose a browser when opening a link. | `JavaScript` | [Source](https://github.com/will-stone/browserosaurus) | `MIT` |
| <a href="https://www.chromium.org"><img src="./icons/project-icons/chromium.svg" width="32" height="32" alt="Chromium"></a> | **[Chromium](https://www.chromium.org)** | Chromium is an open-source browser project that aims to build a safer, faster, and more stable way for all users to experience the web. | `JavaScript` | [Website](https://www.chromium.org) • [Source](https://chromium.googlesource.com/chromium/src/) | `MIT` |
| <a href="https://github.com/johnste/finicky"><img src="./icons/project-icons/finicky.png" width="32" height="32" alt="Finicky"></a> | **[Finicky](https://github.com/johnste/finicky)** | Always opens the right browser. | `Swift` | [Source](https://github.com/johnste/finicky) | `MIT` |
| <a href="https://www.mozilla.org/en-US/firefox/browsers"><img src="./icons/project-icons/firefox.svg" width="32" height="32" alt="Firefox"></a> | **[Firefox](https://www.mozilla.org/en-US/firefox/browsers)** | Fast, privacy aware browser from a non-profit. Runs on Windows, macOS and Linux. | `JavaScript` | [Website](https://www.mozilla.org/en-US/firefox/browsers) • [Source](https://hg.mozilla.org/mozilla-central/) | `MIT` |
| <a href="https://github.com/JadenGeller/Helium"><img src="./icons/project-icons/helium.png" width="32" height="32" alt="Helium"></a> | **[Helium](https://github.com/JadenGeller/Helium)** | Floating browser window for macOS. | `Objective-C` | [Source](https://github.com/JadenGeller/Helium) | `MIT` |
| <a href="https://minbrowser.org"><img src="./icons/project-icons/min-browser.png" width="32" height="32" alt="Min Browser"></a> | **[Min Browser](https://minbrowser.org)** | A fast and efficient minimal web browser. | `JavaScript` | [Website](https://minbrowser.org) • [Source](https://github.com/minbrowser/min) | `MIT` |
| <a href="https://github.com/OtterBrowser/otter-browser"><img src="./icons/project-icons/otter-browser.png" width="32" height="32" alt="otter-browser"></a> | **[otter-browser](https://github.com/OtterBrowser/otter-browser)** | Otter Browser aims to recreate the best aspects of the classic Opera (12.x) UI using Qt5. | `C++` | [Source](https://github.com/OtterBrowser/otter-browser) | `MIT` |
| <a href="https://github.com/kamranahmedse/pennywise"><img src="./icons/project-icons/pennywise.svg" width="32" height="32" alt="Pennywise"></a> | **[Pennywise](https://github.com/kamranahmedse/pennywise)** | Pennywise opens any website or media in a small floating window that remains on top of all other applications. It's a great alternative to Helium. | `JavaScript` | [Source](https://github.com/kamranahmedse/pennywise) | `MIT` |
| <a href="https://sindresorhus.com/plash"><img src="./icons/project-icons/plash.png" width="32" height="32" alt="Plash"></a> | **[Plash](https://sindresorhus.com/plash)** | Make any website your desktop wallpaper. | `Swift` | [Website](https://sindresorhus.com/plash) • [Source](https://github.com/sindresorhus/Plash) | `MIT` |
| <a href="https://github.com/smmr-software/privacy-redirect-safari"><img src="./icons/project-icons/privacy-redirect-for-safari.png" width="32" height="32" alt="Privacy Redirect for Safari"></a> | **[Privacy Redirect for Safari](https://github.com/smmr-software/privacy-redirect-safari)** | Redirect Twitter, YouTube, Reddit, Google Maps, Google Search, and Google Translate to privacy friendly alternatives. | `Swift` | [Source](https://github.com/smmr-software/privacy-redirect-safari) | `MIT` |
| <a href="https://github.com/SafeExamBrowser/seb-mac"><img src="./icons/project-icons/seb-mac.png" width="32" height="32" alt="seb-mac"></a> | **[seb-mac](https://github.com/SafeExamBrowser/seb-mac)** | Safe Exam Browser for macOS and iOS. | `C` | [Source](https://github.com/SafeExamBrowser/seb-mac) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="chat"></a>
### 💬 Chat

> Instant messaging, Matrix, IRC, Telegram, WhatsApp wrappers, and team communication.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://adium.im"><img src="./icons/project-icons/adium.png" width="32" height="32" alt="Adium"></a> | **[Adium](https://adium.im)** | Instant messaging application that can connect to XMPP (Jabber), IRC and more. | `C` | [Website](https://adium.im) • [Source](https://github.com/adium/adium) | `MIT` |
| <a href="https://beagle.im"><img src="./icons/project-icons/beagle-im.png" width="32" height="32" alt="Beagle IM"></a> | **[Beagle IM](https://beagle.im)** | Powerful XMPP client with support for file transfer, VoIP and end-to-end encryption. | `Swift` | [Website](https://beagle.im) • [Source](https://github.com/tigase/beagle-im) | `MIT` |
| <a href="https://github.com/stonesam92/ChitChat"><img src="./icons/project-icons/chitchat.png" width="32" height="32" alt="ChitChat"></a> | **[ChitChat](https://github.com/stonesam92/ChitChat)** | Native Mac app wrapper for WhatsApp Web. | `Objective-C` | [Source](https://github.com/stonesam92/ChitChat) | `MIT` |
| <a href="https://github.com/geeeeeeeeek/electronic-wechat"><img src="./icons/project-icons/electronic-wechat.png" width="32" height="32" alt="Electronic WeChat"></a> | **[Electronic WeChat](https://github.com/geeeeeeeeek/electronic-wechat)** | Better WeChat on macOS and Linux. | `JavaScript` | [Source](https://github.com/geeeeeeeeek/electronic-wechat) | `MIT` |
| <a href="https://github.com/vector-im/element-web"><img src="./icons/project-icons/element.png" width="32" height="32" alt="Element"></a> | **[Element](https://github.com/vector-im/element-web)** | Element is a collaboration app (currently Electron) for the [Matrix](https://matrix.org/) protocol. | `JavaScript` | [Source](https://github.com/vector-im/element-web) | `MIT` |
| <a href="https://github.com/meetfranz/franz"><img src="./icons/project-icons/franz.png" width="32" height="32" alt="Franz"></a> | **[Franz](https://github.com/meetfranz/franz)** | Franz is messaging application for services like WhatsApp, Slack, Messenger and many more. | `JavaScript` | [Source](https://github.com/meetfranz/franz) | `MIT` |
| <a href="https://github.com/kelyvin/Google-Allo-For-Desktop"><img src="./icons/project-icons/google-allo-for-desktop.png" width="32" height="32" alt="Google Allo for Desktop"></a> | **[Google Allo for Desktop](https://github.com/kelyvin/Google-Allo-For-Desktop)** | Native macOS & Windows desktop app for Google Allo. | `JavaScript` | [Source](https://github.com/kelyvin/Google-Allo-For-Desktop) | `MIT` |
| <a href="https://github.com/dcrousso/GroupMe"><img src="./icons/project-icons/groupme.png" width="32" height="32" alt="GroupMe"></a> | **[GroupMe](https://github.com/dcrousso/GroupMe)** | Unofficial GroupMe App. | `JavaScript` | [Source](https://github.com/dcrousso/GroupMe) | `MIT` |
| <a href="https://github.com/glaurent/MessagesHistoryBrowser"><img src="./icons/project-icons/messageshistorybrowser.png" width="32" height="32" alt="MessagesHistoryBrowser"></a> | **[MessagesHistoryBrowser](https://github.com/glaurent/MessagesHistoryBrowser)** | macOS application to comfortably browse and search through your Messages.app history. | `Swift` | [Source](https://github.com/glaurent/MessagesHistoryBrowser) | `MIT` |
| <a href="https://onionshare.org"><img src="./icons/project-icons/onionshare.png" width="32" height="32" alt="OnionShare"></a> | **[OnionShare](https://onionshare.org)** | Securely and anonymously share files, host websites, and chat with friends using the Tor network. | `Python` | [Website](https://onionshare.org) • [Source](https://github.com/onionshare/onionshare) | `MIT` |
| <a href="https://www.rocket.chat"><img src="./icons/project-icons/rocketchat.png" width="32" height="32" alt="RocketChat"></a> | **[RocketChat](https://www.rocket.chat)** | Free open source chat system for teams. An alternative to Slack that can also be self hosted. | `JavaScript` | [Website](https://www.rocket.chat) • [Source](https://github.com/RocketChat/Rocket.Chat.Electron) | `MIT` |
| <a href="https://github.com/neilalexander/seaglass"><img src="./icons/project-icons/seaglass.png" width="32" height="32" alt="Seaglass"></a> | **[Seaglass](https://github.com/neilalexander/seaglass)** | A truly native [Matrix](https://matrix.org/blog/home/) client for macOS. | `Swift` | [Source](https://github.com/neilalexander/seaglass) | `MIT` |
| <a href="https://github.com/signalapp/Signal-Desktop"><img src="./icons/project-icons/signal-desktop.png" width="32" height="32" alt="Signal Desktop"></a> | **[Signal Desktop](https://github.com/signalapp/Signal-Desktop)** | Electron app that links with your Signal Android or Signal iOS app. | `JavaScript` | [Source](https://github.com/signalapp/Signal-Desktop) | `MIT` |
| <a href="https://github.com/SwiftcordApp/Swiftcord"><img src="./icons/project-icons/swiftcord.png" width="32" height="32" alt="Swiftcord"></a> | **[Swiftcord](https://github.com/SwiftcordApp/Swiftcord)** | Native Discord client built in Swift & SwiftUI. Light on your RAM and CPU. | `Swift` | [Source](https://github.com/SwiftcordApp/Swiftcord) | `MIT` |
| <a href="https://github.com/overtake/TelegramSwift"><img src="./icons/project-icons/telegram.png" width="32" height="32" alt="Telegram"></a> | **[Telegram](https://github.com/overtake/TelegramSwift)** | Source code of Telegram for macOS on Swift. | `Swift` | [Source](https://github.com/overtake/TelegramSwift) | `MIT` |
| <a href="https://github.com/telegramdesktop/tdesktop"><img src="./icons/project-icons/telegram-desktop.png" width="32" height="32" alt="Telegram Desktop"></a> | **[Telegram Desktop](https://github.com/telegramdesktop/tdesktop)** | Telegram Desktop messaging app. | `C++` | [Source](https://github.com/telegramdesktop/tdesktop) | `MIT` |
| <a href="https://github.com/Codeux-Software/Textual"><img src="./icons/project-icons/textual.png" width="32" height="32" alt="Textual"></a> | **[Textual](https://github.com/Codeux-Software/Textual)** | Textual is an IRC client for macOS. | `Objective-C` | [Source](https://github.com/Codeux-Software/Textual) | `MIT` |
| <a href="https://github.com/javerous/TorChat-Mac"><img src="./icons/project-icons/torchat-mac.png" width="32" height="32" alt="Torchat-Mac"></a> | **[Torchat-Mac](https://github.com/javerous/TorChat-Mac)** | TorChat for Mac is a macOS native and unofficial port of torchat. | `Objective-C` | [Source](https://github.com/javerous/TorChat-Mac) | `MIT` |
| <a href="https://github.com/aldychris/WhatsAppBar"><img src="./icons/project-icons/whatsappbar.png" width="32" height="32" alt="WhatsAppBar"></a> | **[WhatsAppBar](https://github.com/aldychris/WhatsAppBar)** | Send WhatsApp message from menu bar. | `Swift` | [Source](https://github.com/aldychris/WhatsAppBar) | `MIT` |
| <a href="https://github.com/wireapp/wire-desktop"><img src="./icons/project-icons/wire-desktop.png" width="32" height="32" alt="Wire Desktop"></a> | **[Wire Desktop](https://github.com/wireapp/wire-desktop)** | Standalone Electron app for the chatapp Wire. | `JavaScript` | [Source](https://github.com/wireapp/wire-desktop) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="cryptocurrency"></a>
### 💰 Cryptocurrency

> Cryptocurrency wallets, node runners, portfolio trackers, and blockchain tools.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://bitcoincore.org"><img src="./icons/project-icons/bitcoin-core.png" width="32" height="32" alt="Bitcoin Core"></a> | **[Bitcoin Core](https://bitcoincore.org)** | Official Bitcoin Core software for running a full Bitcoin node. | `C++` | [Website](https://bitcoincore.org) • [Source](https://github.com/bitcoin/bitcoin) | `MIT` |
| <a href="https://github.com/adamwaite/CoinBar"><img src="./icons/project-icons/coinbar.png" width="32" height="32" alt="CoinBar"></a> | **[CoinBar](https://github.com/adamwaite/CoinBar)** | macOS menu bar application for tracking crypto coin prices. | `Swift` | [Source](https://github.com/adamwaite/CoinBar) | `MIT` |
| <a href="https://github.com/bitpay/copay"><img src="./icons/project-icons/copay.png" width="32" height="32" alt="Copay"></a> | **[Copay](https://github.com/bitpay/copay)** | A secure bitcoin wallet platform for both desktop and mobile devices. | `TypeScript` | [Source](https://github.com/bitpay/copay) | `MIT` |
| <a href="https://github.com/geraldoramos/crypto-bar"><img src="./icons/project-icons/crypto-bar.png" width="32" height="32" alt="Crypto Bar"></a> | **[Crypto Bar](https://github.com/geraldoramos/crypto-bar)** | macOS menu bar application built with Electron. | `JavaScript` | [Source](https://github.com/geraldoramos/crypto-bar) | `MIT` |
| <a href="https://github.com/kaunteya/FloatCoin"><img src="./icons/project-icons/float-coin.png" width="32" height="32" alt="Float coin"></a> | **[Float coin](https://github.com/kaunteya/FloatCoin)** | Native menu bar app with floating window and support for many Exchanges. | `Swift` | [Source](https://github.com/kaunteya/FloatCoin) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="database"></a>
### 🗄️ Database

> Modern database GUIs, SQL query editors, Redis managers, and SQLite visualizers.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/bdash-app/bdash"><img src="./icons/project-icons/bdash.png" width="32" height="32" alt="Bdash"></a> | **[Bdash](https://github.com/bdash-app/bdash)** | Simple SQL Client for lightweight data analysis. | `JavaScript` | [Source](https://github.com/bdash-app/bdash) | `MIT` |
| <a href="https://github.com/sqlitebrowser/sqlitebrowser"><img src="./icons/project-icons/db-browser-for-sqlite.png" width="32" height="32" alt="DB Browser for SQLite"></a> | **[DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser)** | SQLite database management GUI. | `C++` | [Source](https://github.com/sqlitebrowser/sqlitebrowser) | `MIT` |
| <a href="https://github.com/dbeaver/dbeaver"><img src="./icons/project-icons/dbeaver.png" width="32" height="32" alt="DBeaver"></a> | **[DBeaver](https://github.com/dbeaver/dbeaver)** | Universal database tool and SQL client. | `Java` | [Source](https://github.com/dbeaver/dbeaver) | `MIT` |
| <a href="https://dbgate.org"><img src="./icons/project-icons/dbgate.png" width="32" height="32" alt="DbGate"></a> | **[DbGate](https://dbgate.org)** | Database manager for MySQL, PostgreSQL, SQL Server, MongoDB, SQLite and others. Runs under Windows, Linux, Mac or as web application. | `JavaScript` | [Website](https://dbgate.org) • [Source](https://github.com/dbgate/dbgate) | `MIT` |
| <a href="https://github.com/luin/medis"><img src="./icons/project-icons/medis.png" width="32" height="32" alt="Medis"></a> | **[Medis](https://github.com/luin/medis)** | 💻 Medis is a beautiful, easy-to-use Mac database management application for Redis. | `JavaScript` | [Source](https://github.com/luin/medis) | `MIT` |
| <a href="https://github.com/gcollazo/mongodbapp"><img src="./icons/project-icons/mongodb-app.png" width="32" height="32" alt="mongoDB.app"></a> | **[mongoDB.app](https://github.com/gcollazo/mongodbapp)** | The easiest way to get started with mongoDB on the Mac. | `Swift` | [Source](https://github.com/gcollazo/mongodbapp) | `MIT` |
| <a href="https://github.com/jeromelebel/MongoHub-Mac"><img src="./icons/project-icons/mongohub.png" width="32" height="32" alt="MongoHub"></a> | **[MongoHub](https://github.com/jeromelebel/MongoHub-Mac)** | Add another lightweight Mac Native MongoDB client. | `Objective-C` | [Source](https://github.com/jeromelebel/MongoHub-Mac) | `MIT` |
| <a href="https://github.com/Paxa/postbird"><img src="./icons/project-icons/postbird.png" width="32" height="32" alt="Postbird"></a> | **[Postbird](https://github.com/Paxa/postbird)** | PostgreSQL GUI client for macOS. | `JavaScript` | [Source](https://github.com/Paxa/postbird) | `MIT` |
| <a href="https://github.com/PostgresApp/PostgresApp"><img src="./icons/project-icons/postgres-app.png" width="32" height="32" alt="Postgres.app"></a> | **[Postgres.app](https://github.com/PostgresApp/PostgresApp)** | The easiest way to get started with PostgreSQL on the Mac. | `Swift` | [Source](https://github.com/PostgresApp/PostgresApp) | `MIT` |
| <a href="https://github.com/uglide/RedisDesktopManager"><img src="./icons/project-icons/redis-desktop-manager.png" width="32" height="32" alt="Redis Desktop Manager"></a> | **[Redis Desktop Manager](https://github.com/uglide/RedisDesktopManager)** | Cross-platform open source database management tool for Redis ® | `C++` | [Source](https://github.com/uglide/RedisDesktopManager) | `MIT` |
| <a href="https://github.com/cmushroom/redis-pro"><img src="./icons/project-icons/redis-pro.png" width="32" height="32" alt="redis-pro"></a> | **[redis-pro](https://github.com/cmushroom/redis-pro)** | Redis management with SwiftUI. | `Swift` | [Source](https://github.com/cmushroom/redis-pro) | `MIT` |
| <a href="https://github.com/jpadilla/redisapp"><img src="./icons/project-icons/redis-app.png" width="32" height="32" alt="Redis.app"></a> | **[Redis.app](https://github.com/jpadilla/redisapp)** | The easiest way to get started with Redis on the Mac. | `Swift` | [Source](https://github.com/jpadilla/redisapp) | `MIT` |
| <a href="https://github.com/b3z/reventlou"><img src="./icons/project-icons/reventlou.png" width="32" height="32" alt="reventlou"></a> | **[reventlou](https://github.com/b3z/reventlou)** | Personal database as an information management system. | `TypeScript` | [Source](https://github.com/b3z/reventlou) | `MIT` |
| <a href="https://github.com/Studio3T/robomongo"><img src="./icons/project-icons/robo-3t.png" width="32" height="32" alt="Robo 3T"></a> | **[Robo 3T](https://github.com/Studio3T/robomongo)** | Robo 3T (formerly Robomongo) is the free lightweight GUI for MongoDB enthusiasts. | `C++` | [Source](https://github.com/Studio3T/robomongo) | `MIT` |
| <a href="https://sequel-ace.com"><img src="./icons/project-icons/sequel-ace.png" width="32" height="32" alt="Sequel Ace"></a> | **[Sequel Ace](https://sequel-ace.com)** | Sequel Ace is a fast, easy-to-use Mac database management application for working with MySQL & MariaDB databases. | `Objective-C` | [Website](https://sequel-ace.com) • [Source](https://github.com/Sequel-Ace/Sequel-Ace) | `MIT` |
| <a href="https://github.com/sequelpro/sequelpro"><img src="./icons/project-icons/sequel-pro.png" width="32" height="32" alt="Sequel Pro"></a> | **[Sequel Pro](https://github.com/sequelpro/sequelpro)** | MySQL/MariaDB database management for macOS. | `Objective-C` | [Source](https://github.com/sequelpro/sequelpro) | `MIT` |
| <a href="https://sqlectron.github.io"><img src="./icons/project-icons/sqlectron.png" width="32" height="32" alt="sqlectron"></a> | **[sqlectron](https://sqlectron.github.io)** | A simple and lightweight SQL client desktop/terminal with cross database and platform support. | `TypeScript` | [Website](https://sqlectron.github.io) • [Source](https://github.com/sqlectron/sqlectron-gui) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="development"></a>
### 👨‍💻 Development

> General developer utilities, SDK managers, reverse engineering suites, and debugging tools.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://netbeans.apache.org"><img src="./icons/project-icons/apache-netbeans.png" width="32" height="32" alt="Apache Netbeans"></a> | **[Apache Netbeans](https://netbeans.apache.org)** | Apache NetBeans is an IDE, Tooling Platform and Application Framework suitable for development in Java, JavaScript, PHP, HTML5, CSS, and more. | `Java` | [Website](https://netbeans.apache.org) • [Source](https://github.com/apache/netbeans) | `MIT` |
| <a href="https://www.beekeeperstudio.io"><img src="./icons/project-icons/beekeeper-studio.png" width="32" height="32" alt="Beekeeper Studio"></a> | **[Beekeeper Studio](https://www.beekeeperstudio.io)** | Modern, easy-to-use SQL editor and database management tool supporting Postgres, MySQL, and SQLite. | `TypeScript` | [Website](https://www.beekeeperstudio.io) • [Source](https://github.com/beekeeper-studio/beekeeper-studio) | `GPL-3.0` |
| <a href="https://brackets.io"><img src="./icons/project-icons/brackets.png" width="32" height="32" alt="Brackets"></a> | **[Brackets](https://brackets.io)** | Modern open-source code editor for HTML, CSS and JavaScript that's built in HTML, CSS and JavaScript. | `JavaScript` | [Website](https://brackets.io) • [Source](https://github.com/brackets-cont/brackets) | `MIT` |
| <a href="https://www.usebruno.com"><img src="./icons/project-icons/bruno.png" width="32" height="32" alt="Bruno"></a> | **[Bruno](https://www.usebruno.com)** | Fast, git-friendly open-source API client for exploring and testing REST and GraphQL APIs. | `JavaScript` | [Website](https://www.usebruno.com) • [Source](https://github.com/usebruno/bruno) | `MIT` |
| <a href="https://GetClipboard.app"><img src="./icons/project-icons/clipboard.png" width="32" height="32" alt="Clipboard"></a> | **[Clipboard](https://GetClipboard.app)** | An easy-to-use clipboard manager with time saving features that work across all terminals. | `C++` | [Website](https://GetClipboard.app) • [Source](https://github.com/Slackadays/Clipboard) | `MIT` |
| <a href="https://github.com/abiosoft/colima"><img src="./icons/project-icons/colima.png" width="32" height="32" alt="Colima"></a> | **[Colima](https://github.com/abiosoft/colima)** | Container runtimes (Docker and containerd) on macOS with minimal resource consumption. | `Go` | [Source](https://github.com/abiosoft/colima) | `MIT` |
| <a href="https://imazing.com/colorset"><img src="./icons/project-icons/colorset.png" width="32" height="32" alt="ColorSet"></a> | **[ColorSet](https://imazing.com/colorset)** | ColorSet is a macOS utility and framework allowing developers to manage custom interface colors with ease. | `Swift` | [Website](https://imazing.com/colorset) • [Source](https://github.com/DigiDNA/ColorSet) | `MIT` |
| <a href="https://coteditor.com"><img src="./icons/project-icons/coteditor.png" width="32" height="32" alt="CotEditor"></a> | **[CotEditor](https://coteditor.com)** | Lightweight, pure native plain-text editor designed exclusively for macOS. | `Swift` | [Website](https://coteditor.com) • [Source](https://github.com/coteditor/CotEditor) | `Apache-2.0` |
| <a href="https://github.com/csprasad/DevLint"><img src="./icons/project-icons/devlint.png" width="32" height="32" alt="DevLint"></a> | **[DevLint](https://github.com/csprasad/DevLint)** | A lightweight app for formatting and correcting Swift syntax. | `Swift` | [Source](https://github.com/csprasad/DevLint) | `MIT` |
| <a href="https://dorothyai.app"><img src="./icons/project-icons/dorothy.png" width="32" height="32" alt="Dorothy"></a> | **[Dorothy](https://dorothyai.app)** | Desktop app to orchestrate multiple AI CLI agents simultaneously with automations, Kanban management, and remote control via Telegram. | `TypeScript` | [Website](https://dorothyai.app) • [Source](https://github.com/Charlie85270/Dorothy) | `MIT` |
| <a href="https://www.eclipse.org"><img src="./icons/project-icons/eclipse.png" width="32" height="32" alt="Eclipse"></a> | **[Eclipse](https://www.eclipse.org)** | Eclipse is an open-source integrated development environment (IDE) used in computer programming, featuring a base workspace and an extensible plug-in system for customizing the environment. | `Java` | [Website](https://www.eclipse.org) • [Source](https://github.com/eclipse-platform/eclipse.platform) | `MIT` |
| <a href="https://gitahead.github.io/gitahead.com"><img src="./icons/project-icons/gitahead.png" width="32" height="32" alt="GitAhead"></a> | **[GitAhead](https://gitahead.github.io/gitahead.com)** | A graphical Git client designed to help you understand and manage your source code history. | `C++` | [Website](https://gitahead.github.io/gitahead.com) • [Source](https://github.com/gitahead/gitahead/) | `MIT` |
| <a href="https://gitup.co"><img src="./icons/project-icons/gitup.svg" width="32" height="32" alt="GitUp"></a> | **[GitUp](https://gitup.co)** | Direct-manipulation Git client offering a non-linear graph visualization and instant undo. | `Objective-C` | [Website](https://gitup.co) • [Source](https://github.com/git-up/GitUp) | `GPL-3.0` |
| <a href="https://gridfy.astroon.pro"><img src="./icons/project-icons/gridfy.png" width="32" height="32" alt="Gridfy"></a> | **[Gridfy](https://gridfy.astroon.pro)** | Quickly calculate column widths and get correct results for your grid. | `JavaScript` | [Website](https://gridfy.astroon.pro) • [Source](https://github.com/Slllava/gridfy) | `MIT` |
| <a href="https://kaphacius.github.io/just-tags"><img src="./icons/project-icons/justtags.png" width="32" height="32" alt="JustTags"></a> | **[JustTags](https://kaphacius.github.io/just-tags)** | JustTags in a macOS app for working with BERTLV EMV tags. | `Swift` | [Website](https://kaphacius.github.io/just-tags) • [Source](https://github.com/kaphacius/just-tags) | `MIT` |
| <a href="https://www.kicad.org"><img src="./icons/project-icons/kicad.svg" width="32" height="32" alt="KiCad"></a> | **[KiCad](https://www.kicad.org)** | A software suite for electronic design automation. | `C++` | [Website](https://www.kicad.org) • [Source](https://gitlab.com/kicad/code/kicad) | `MIT` |
| <a href="https://apps.apple.com/nl/app/layout-designer/id1507238011?l=en&mt=12"><img src="./icons/project-icons/layout-designer-for-uicollectionview.png" width="32" height="32" alt="Layout Designer for UICollectionView"></a> | **[Layout Designer for UICollectionView](https://apps.apple.com/nl/app/layout-designer/id1507238011?l=en&mt=12)** | A simple but powerful tool that helps you make complex layouts for UICollectionView. | `Swift` | [Website](https://apps.apple.com/nl/app/layout-designer/id1507238011?l=en&mt=12) • [Source](https://github.com/amirdew/CollectionViewPagingLayout) | `MIT` |
| <a href="https://schlaubischlump.github.io/LocationSimulator"><img src="./icons/project-icons/locationsimulator.png" width="32" height="32" alt="LocationSimulator"></a> | **[LocationSimulator](https://schlaubischlump.github.io/LocationSimulator)** | Application to spoof your iOS or iPhoneSimulator location. | `Swift` | [Website](https://schlaubischlump.github.io/LocationSimulator) • [Source](https://github.com/Schlaubischlump/LocationSimulator) | `MIT` |
| <a href="https://github.com/Mcourtyard/m-courtyard"><img src="./icons/project-icons/m-courtyard.png" width="32" height="32" alt="M-Courtyard"></a> | **[M-Courtyard](https://github.com/Mcourtyard/m-courtyard)** | Desktop app for fine-tuning LLMs on Apple Silicon Macs with zero code. Import documents, generate training datasets with AI, LoRA fine-tune, test, and export to Ollama — entirely offline. | `TypeScript` | [Source](https://github.com/Mcourtyard/m-courtyard) | `MIT` |
| <a href="https://macvim-dev.github.io/macvim"><img src="./icons/project-icons/macvim.png" width="32" height="32" alt="MacVim"></a> | **[MacVim](https://macvim-dev.github.io/macvim)** | Vim text editor port designed to look and behave natively on macOS with full GUI integration. | `C` | [Website](https://macvim-dev.github.io/macvim) • [Source](https://github.com/macvim-dev/macvim) | `Vim` |
| <a href="https://github.com/us/mocker"><img src="./icons/project-icons/mocker.png" width="32" height="32" alt="Mocker"></a> | **[Mocker](https://github.com/us/mocker)** | Docker-compatible container CLI for macOS, built on Apple's Containerization framework. | `Swift` | [Source](https://github.com/us/mocker) | `MIT` |
| <a href="https://sindresorhus.com/pasteboard-viewer"><img src="./icons/project-icons/pasteboard-viewer.png" width="32" height="32" alt="Pasteboard Viewer"></a> | **[Pasteboard Viewer](https://sindresorhus.com/pasteboard-viewer)** | Inspect the system pasteboards. | `Swift` | [Website](https://sindresorhus.com/pasteboard-viewer) • [Source](https://github.com/sindresorhus/Pasteboard-Viewer) | `MIT` |
| <a href="https://podman-desktop.io"><img src="./icons/project-icons/podman-desktop.png" width="32" height="32" alt="Podman Desktop"></a> | **[Podman Desktop](https://podman-desktop.io)** | Desktop environment to manage containers, Kubernetes, and local development environments. | `TypeScript` | [Website](https://podman-desktop.io) • [Source](https://github.com/containers/podman-desktop) | `Apache-2.0` |
| <a href="https://ssbun.github.io/Shark"><img src="./icons/project-icons/shark.png" width="32" height="32" alt="Shark"></a> | **[Shark](https://ssbun.github.io/Shark)** | Cursor IDE workspace manager for macOS. | `Swift` | [Website](https://ssbun.github.io/Shark) • [Source](https://github.com/SSBun/Shark) | `MIT` |
| <a href="https://github.com/mohakapt/Stringz"><img src="./icons/project-icons/stringz.svg" width="32" height="32" alt="Stringz"></a> | **[Stringz](https://github.com/mohakapt/Stringz)** | A lightweight and powerful editor for localizing iOS, macOS, tvOS, and watchOS applications. | `Swift` | [Source](https://github.com/mohakapt/Stringz) | `MIT` |
| <a href="https://mac.getutm.app"><img src="./icons/project-icons/utmapp.png" width="32" height="32" alt="utmapp"></a> | **[utmapp](https://mac.getutm.app)** | Virtualization for other operating systems. | `Swift` | [Website](https://mac.getutm.app) • [Source](https://github.com/utmapp/) | `MIT` |
| <a href="https://vscodium.com"><img src="./icons/project-icons/vscodium.svg" width="32" height="32" alt="VSCodium"></a> | **[VSCodium](https://vscodium.com)** | Community-driven, telemetry-free binary distribution of Microsoft's VS Code editor. | `TypeScript` | [Website](https://vscodium.com) • [Source](https://github.com/VSCodium/vscodium) | `MIT` |
| <a href="https://zed.dev"><img src="./icons/project-icons/zed.png" width="32" height="32" alt="Zed"></a> | **[Zed](https://zed.dev)** | High-performance, multiplayer code editor written in Rust with GPU-accelerated rendering. | `Rust` | [Website](https://zed.dev) • [Source](https://github.com/zed-industries/zed) | `GPL-3.0` |

[⬆ Back to Top](#table-of-contents)


<a id="git"></a>
### 📦 Git

> Native Git GUI clients, visual diff inspection tools, commit helpers, and merge assistants.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/dhennessy/OpenCashew"><img src="./icons/project-icons/cashew.png" width="32" height="32" alt="Cashew"></a> | **[Cashew](https://github.com/dhennessy/OpenCashew)** | Cashew macOS Github Issue Tracker. | `Objective-C` | [Source](https://github.com/dhennessy/OpenCashew) | `MIT` |
| <a href="https://gitrebasetool.mitmaro.ca"><img src="./icons/project-icons/git-interactive-rebase-tool.png" width="32" height="32" alt="Git Interactive Rebase Tool"></a> | **[Git Interactive Rebase Tool](https://gitrebasetool.mitmaro.ca)** | Full feature terminal based sequence editor for interactive rebase. | `Rust` | [Website](https://gitrebasetool.mitmaro.ca) • [Source](https://github.com/MitMaro/git-interactive-rebase-tool) | `MIT` |
| <a href="https://github.com/maoyama/GitBlamePR"><img src="./icons/project-icons/gitblamepr.png" width="32" height="32" alt="GitBlamePR"></a> | **[GitBlamePR](https://github.com/maoyama/GitBlamePR)** | Mac app that shows pull request last modified each line of a file | `Swift` | [Source](https://github.com/maoyama/GitBlamePR) | `MIT` |
| <a href="https://github.com/Nightonke/Gitee"><img src="./icons/project-icons/gitee.png" width="32" height="32" alt="Gitee"></a> | **[Gitee](https://github.com/Nightonke/Gitee)** | Gitee, macOS status bar application for Github. | `Objective-C` | [Source](https://github.com/Nightonke/Gitee) | `MIT` |
| <a href="https://github.com/remirobert/Github-contributions"><img src="./icons/project-icons/github-contributions.png" width="32" height="32" alt="Github contributions"></a> | **[Github contributions](https://github.com/remirobert/Github-contributions)** | GitHub contributions app, for iOS, WatchOS, and macOS. | `Swift` | [Source](https://github.com/remirobert/Github-contributions) | `MIT` |
| <a href="https://github.com/desktop/desktop"><img src="./icons/project-icons/github-desktop.png" width="32" height="32" alt="GitHub Desktop"></a> | **[GitHub Desktop](https://github.com/desktop/desktop)** | Simple collaboration from your desktop. | `TypeScript` | [Source](https://github.com/desktop/desktop) | `MIT` |
| <a href="https://github.com/ad/GithubListener"><img src="./icons/project-icons/githublistener.png" width="32" height="32" alt="GithubListener"></a> | **[GithubListener](https://github.com/ad/GithubListener)** | Simple app that will notify about new commits to watched repositories. | `Swift` | [Source](https://github.com/ad/GithubListener) | `MIT` |
| <a href="https://github.com/erik/github-notify"><img src="./icons/project-icons/githubnotify.png" width="32" height="32" alt="GithubNotify"></a> | **[GithubNotify](https://github.com/erik/github-notify)** | Simple macOS app to alert you when you have unread GitHub notifications. | `Swift` | [Source](https://github.com/erik/github-notify) | `MIT` |
| <a href="https://www.gitify.io"><img src="./icons/project-icons/gitify.png" width="32" height="32" alt="Gitify"></a> | **[Gitify](https://www.gitify.io)** | Your GitHub notifications on your menu bar. | `JavaScript` | [Website](https://www.gitify.io) • [Source](https://github.com/manosim/gitify) | `MIT` |
| <a href="https://github.com/eonist/GitSync"><img src="./icons/project-icons/gitsync.png" width="32" height="32" alt="GitSync"></a> | **[GitSync](https://github.com/eonist/GitSync)** | Minimalistic Git client for Mac. | `Swift` | [Source](https://github.com/eonist/GitSync) | `MIT` |
| <a href="https://github.com/gitx/gitx"><img src="./icons/project-icons/gitx.png" width="32" height="32" alt="GitX"></a> | **[GitX](https://github.com/gitx/gitx)** | Graphical client for the git version control system. | `Objective-C` | [Source](https://github.com/gitx/gitx) | `MIT` |
| <a href="https://github.com/mtgto/GPM"><img src="./icons/project-icons/gpm.png" width="32" height="32" alt="GPM"></a> | **[GPM](https://github.com/mtgto/GPM)** | macOS application for easily operating GitHub Projects. | `Swift` | [Source](https://github.com/mtgto/GPM) | `MIT` |
| <a href="https://github.com/doekman/osagitfilter"><img src="./icons/project-icons/osagitfilter.png" width="32" height="32" alt="osagitfilter"></a> | **[osagitfilter](https://github.com/doekman/osagitfilter)** | Filter to put OSA languages (AppleScript, JavaScript) into git, as if they where plain text-files. | `Shell` | [Source](https://github.com/doekman/osagitfilter) | `MIT` |
| <a href="https://github.com/jamieweavis/streaker"><img src="./icons/project-icons/streaker.png" width="32" height="32" alt="Streaker"></a> | **[Streaker](https://github.com/jamieweavis/streaker)** | GitHub contribution streak tracking menubar app. | `JavaScript` | [Source](https://github.com/jamieweavis/streaker) | `MIT` |
| <a href="https://github.com/marcinreliga/TeamStatus-for-GitHub"><img src="./icons/project-icons/teamstatus-for-github.png" width="32" height="32" alt="TeamStatus-for-GitHub"></a> | **[TeamStatus-for-GitHub](https://github.com/marcinreliga/TeamStatus-for-GitHub)** | macOS status bar application for tracking code review process within the team. | `Swift` | [Source](https://github.com/marcinreliga/TeamStatus-for-GitHub) | `MIT` |
| <a href="https://github.com/maoyama/Tempo"><img src="./icons/project-icons/tempo.png" width="32" height="32" alt="Tempo"></a> | **[Tempo](https://github.com/maoyama/Tempo)** | Replace the Git CLI with a clear UI and AI assist. | `Swift` | [Source](https://github.com/maoyama/Tempo) | `MIT` |
| <a href="https://github.com/ptsochantaris/trailer"><img src="./icons/project-icons/trailer.png" width="32" height="32" alt="Trailer"></a> | **[Trailer](https://github.com/ptsochantaris/trailer)** | Managing Pull Requests and Issues For GitHub & GitHub Enterprise. | `Swift` | [Source](https://github.com/ptsochantaris/trailer) | `MIT` |
| <a href="https://github.com/Uncommon/Xit"><img src="./icons/project-icons/xit.png" width="32" height="32" alt="Xit"></a> | **[Xit](https://github.com/Uncommon/Xit)** | Xit is a graphical tool for working with git repositories. | `Swift` | [Source](https://github.com/Uncommon/Xit) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="ios-macos"></a>
<a id="ios-/-macos"></a>
<a id="ios--macos"></a>
### 📱 iOS / macOS

> Apple ecosystem tooling, Xcode enhancements, provisioning helpers, and simulator utilities.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/getappbox/AppBox-iOSAppsWirelessInstallation"><img src="./icons/project-icons/appbox.png" width="32" height="32" alt="AppBox"></a> | **[AppBox](https://github.com/getappbox/AppBox-iOSAppsWirelessInstallation)** | Tool for iOS developers to build and deploy Development, Ad-Hoc and In-house (Enterprise) applications directly to the devices from your Dropbox account. | `Objective-C` | [Source](https://github.com/getappbox/AppBox-iOSAppsWirelessInstallation) | `MIT` |
| <a href="https://github.com/kuyawa/AppIcons"><img src="./icons/project-icons/appicons.png" width="32" height="32" alt="AppIcons"></a> | **[AppIcons](https://github.com/kuyawa/AppIcons)** | Tool for generating icons in all sizes as required by macOS and iOS apps. | `Swift` | [Source](https://github.com/kuyawa/AppIcons) | `MIT` |
| <a href="https://github.com/arbel03/AppStoreReviewTimes"><img src="./icons/project-icons/appstorereviewtimes.png" width="32" height="32" alt="AppStoreReviewTimes"></a> | **[AppStoreReviewTimes](https://github.com/arbel03/AppStoreReviewTimes)** | Gives you indication about the average iOS / macOS app stores review times. | `Swift` | [Source](https://github.com/arbel03/AppStoreReviewTimes) | `MIT` |
| <a href="https://github.com/insidegui/AssetCatalogTinkerer"><img src="./icons/project-icons/asset-catalog-tinkerer.png" width="32" height="32" alt="Asset Catalog Tinkerer"></a> | **[Asset Catalog Tinkerer](https://github.com/insidegui/AssetCatalogTinkerer)** | App that lets you open .car files and browse/extract their images. | `Objective-C` | [Source](https://github.com/insidegui/AssetCatalogTinkerer) | `MIT` |
| <a href="https://github.com/e7711bbear/Assets"><img src="./icons/project-icons/assets.png" width="32" height="32" alt="Assets"></a> | **[Assets](https://github.com/e7711bbear/Assets)** | Assets is a macOS app that manages assets for your development projects (Xcode, web, etc). | `Swift` | [Source](https://github.com/e7711bbear/Assets) | `MIT` |
| <a href="https://github.com/attaswift/Attabench"><img src="./icons/project-icons/attabench.png" width="32" height="32" alt="Attabench"></a> | **[Attabench](https://github.com/attaswift/Attabench)** | Attabench is a microbenchmarking app for macOS, designed to measure and visualize the performance of Swift code. | `Swift` | [Source](https://github.com/attaswift/Attabench) | `MIT` |
| <a href="https://github.com/angelvasa/AVXCAssets-Generator"><img src="./icons/project-icons/avxcassets-generator.png" width="32" height="32" alt="AVXCAssets Generator"></a> | **[AVXCAssets Generator](https://github.com/angelvasa/AVXCAssets-Generator)** | Takes path for your assets images and creates appiconset and imageset for you in just one click. | `Swift` | [Source](https://github.com/angelvasa/AVXCAssets-Generator) | `MIT` |
| <a href="https://github.com/JustinFincher/BoardForGitHub"><img src="./icons/project-icons/board-for-github.png" width="32" height="32" alt="Board For GitHub"></a> | **[Board For GitHub](https://github.com/JustinFincher/BoardForGitHub)** | Small application to monitor your GitHub project web page in a native macOS app ! | `Objective-C` | [Source](https://github.com/JustinFincher/BoardForGitHub) | `MIT` |
| <a href="https://github.com/br1sk/brisk"><img src="./icons/project-icons/brisk.png" width="32" height="32" alt="Brisk"></a> | **[Brisk](https://github.com/br1sk/brisk)** | macOS app for submitting radars. | `Swift` | [Source](https://github.com/br1sk/brisk) | `MIT` |
| <a href="https://github.com/xing/calabash-launcher"><img src="./icons/project-icons/calabash-launcher.png" width="32" height="32" alt="calabash-launcher"></a> | **[calabash-launcher](https://github.com/xing/calabash-launcher)** | iOS Calabash Launcher is a macOS app that helps you run and manage Calabash tests on your Mac. | `Swift` | [Source](https://github.com/xing/calabash-launcher) | `MIT` |
| <a href="https://github.com/waylybaye/XcodeCleaner"><img src="./icons/project-icons/cleaner-for-xcode.png" width="32" height="32" alt="Cleaner for Xcode"></a> | **[Cleaner for Xcode](https://github.com/waylybaye/XcodeCleaner)** | Cleaner for Xcode.app built with react-native-macOS. | `Objective-C` | [Source](https://github.com/waylybaye/XcodeCleaner) | `MIT` |
| <a href="https://apps.apple.com/us/app/clendar-a-calendar-app/id1548102041"><img src="./icons/project-icons/clendar.png" width="32" height="32" alt="Clendar"></a> | **[Clendar](https://apps.apple.com/us/app/clendar-a-calendar-app/id1548102041)** | Clendar is an universal calendar app. Written in SwiftUI. | `Swift` | [Website](https://apps.apple.com/us/app/clendar-a-calendar-app/id1548102041) • [Source](https://github.com/vinhnx/Clendar) | `MIT` |
| <a href="https://github.com/mmattozzi/cocoa-rest-client"><img src="./icons/project-icons/cocoarestclient.png" width="32" height="32" alt="CocoaRestClient"></a> | **[CocoaRestClient](https://github.com/mmattozzi/cocoa-rest-client)** | Native Apple macOS app for testing HTTP/REST endpoints. | `Objective-C` | [Source](https://github.com/mmattozzi/cocoa-rest-client) | `MIT` |
| <a href="https://coronatracker.samabox.com"><img src="./icons/project-icons/corona-tracker.png" width="32" height="32" alt="Corona Tracker"></a> | **[Corona Tracker](https://coronatracker.samabox.com)** | Coronavirus tracker app for iOS & macOS with maps & charts. | `Swift` | [Website](https://coronatracker.samabox.com) • [Source](https://github.com/MhdHejazi/CoronaTracker) | `MIT` |
| <a href="https://github.com/KrisYu/FilterShop"><img src="./icons/project-icons/filtershop.png" width="32" height="32" alt="FilterShop"></a> | **[FilterShop](https://github.com/KrisYu/FilterShop)** | macOS App to explore CoreImage Filters. | `Swift` | [Source](https://github.com/KrisYu/FilterShop) | `MIT` |
| <a href="https://github.com/onmyway133/IconGenerator"><img src="./icons/project-icons/icongenerator.png" width="32" height="32" alt="IconGenerator"></a> | **[IconGenerator](https://github.com/onmyway133/IconGenerator)** | macOS app to generate app icons. | `JavaScript` | [Source](https://github.com/onmyway133/IconGenerator) | `MIT` |
| <a href="https://github.com/raphaelhanneken/iconizer"><img src="./icons/project-icons/iconizer.png" width="32" height="32" alt="Iconizer"></a> | **[Iconizer](https://github.com/raphaelhanneken/iconizer)** | Create Xcode image catalogs (xcassets) on the fly. | `Swift` | [Source](https://github.com/raphaelhanneken/iconizer) | `MIT` |
| <a href="https://apps.apple.com/us/app/iconology/id1463452867"><img src="./icons/project-icons/iconology.png" width="32" height="32" alt="Iconology"></a> | **[Iconology](https://apps.apple.com/us/app/iconology/id1463452867)** | Edit icons and then export to Xcode, icns, ico, favicon, macOS iconset, or a custom collection. | `Swift` | [Website](https://apps.apple.com/us/app/iconology/id1463452867) • [Source](https://github.com/liamrosenfeld/Iconology) | `MIT` |
| <a href="https://github.com/SAP/macos-icon-generator"><img src="./icons/project-icons/icons-app.png" width="32" height="32" alt="Icons.app"></a> | **[Icons.app](https://github.com/SAP/macos-icon-generator)** | App for macOS which is designed to generate consistent sized icons of an existing application in various states, jiggling (shaking) etc. | `Objective-C` | [Source](https://github.com/SAP/macos-icon-generator) | `MIT` |
| <a href="https://github.com/johnno1962/InjectionIII"><img src="./icons/project-icons/injectioniii.png" width="32" height="32" alt="InjectionIII"></a> | **[InjectionIII](https://github.com/johnno1962/InjectionIII)** | overdue Swift rewrite of Injection. | `Objective-C` | [Source](https://github.com/johnno1962/InjectionIII) | `MIT` |
| <a href="https://inputsource.pro"><img src="./icons/project-icons/input-source-pro.png" width="32" height="32" alt="Input Source Pro"></a> | **[Input Source Pro](https://inputsource.pro)** | Input Source Pro is macOS utility designed for multilingual users who frequently switch input sources. | `Swift` | [Website](https://inputsource.pro) • [Source](https://github.com/runjuu/InputSourcePro/) | `MIT` |
| <a href="https://github.com/devcxm/iOS-Images-Extractor"><img src="./icons/project-icons/ios-images-extractor.png" width="32" height="32" alt="iOS Images Extractor"></a> | **[iOS Images Extractor](https://github.com/devcxm/iOS-Images-Extractor)** | iOS Images Extractor is a Mac app to normalize, decode, and extract images from iOS apps. | `Objective-C` | [Source](https://github.com/devcxm/iOS-Images-Extractor) | `MIT` |
| <a href="https://github.com/wigl/iSimulator"><img src="./icons/project-icons/isimulator.png" width="32" height="32" alt="iSimulator"></a> | **[iSimulator](https://github.com/wigl/iSimulator)** | iSimulator is a GUI utility to control the Simulator and manage the app installed on the simulator. | `Objective-C` | [Source](https://github.com/wigl/iSimulator) | `MIT` |
| <a href="https://github.com/KnuffApp/Knuff"><img src="./icons/project-icons/knuff.png" width="32" height="32" alt="Knuff"></a> | **[Knuff](https://github.com/KnuffApp/Knuff)** | The debug application for Apple Push Notification Service (APNs). | `Objective-C` | [Source](https://github.com/KnuffApp/Knuff) | `MIT` |
| <a href="https://github.com/yuhua-chen/LayerX"><img src="./icons/project-icons/layerx.png" width="32" height="32" alt="LayerX"></a> | **[LayerX](https://github.com/yuhua-chen/LayerX)** | Intuitive app to display transparent images on screen. | `Swift` | [Source](https://github.com/yuhua-chen/LayerX) | `MIT` |
| <a href="https://github.com/cristibaluta/Localizable.strings"><img src="./icons/project-icons/localizable-strings.png" width="32" height="32" alt="Localizable.strings"></a> | **[Localizable.strings](https://github.com/cristibaluta/Localizable.strings)** | Mac app to localize your iOS and macOS projects. | `Swift` | [Source](https://github.com/cristibaluta/Localizable.strings) | `MIT` |
| <a href="https://github.com/igorkulman/iOSLocalizationEditor"><img src="./icons/project-icons/localization-editor.png" width="32" height="32" alt="Localization Editor"></a> | **[Localization Editor](https://github.com/igorkulman/iOSLocalizationEditor)** | Simple macOS editor app to help you manage iOS app localizations by allowing you to edit all the translations side by side. | `Swift` | [Source](https://github.com/igorkulman/iOSLocalizationEditor) | `MIT` |
| <a href="https://github.com/e7711bbear/Localizations"><img src="./icons/project-icons/localizations.png" width="32" height="32" alt="Localizations"></a> | **[Localizations](https://github.com/e7711bbear/Localizations)** | Localizations is an macOS app that manages your Xcode project localization files (.strings). | `Swift` | [Source](https://github.com/e7711bbear/Localizations) | `MIT` |
| <a href="https://github.com/nvzqz/Menubar-Colors"><img src="./icons/project-icons/menubar-colors.png" width="32" height="32" alt="Menubar Colors"></a> | **[Menubar Colors](https://github.com/nvzqz/Menubar-Colors)** | macOS app for convenient access to the system color panel. | `Swift` | [Source](https://github.com/nvzqz/Menubar-Colors) | `MIT` |
| <a href="https://github.com/macmade/Notarize"><img src="./icons/project-icons/notarize.png" width="32" height="32" alt="Notarize"></a> | **[Notarize](https://github.com/macmade/Notarize)** | Notarization status monitoring tool for macOS, supporting multiple developer accounts | `Swift` | [Source](https://github.com/macmade/Notarize) | `MIT` |
| <a href="https://github.com/kizitonwose/PodsUpdater"><img src="./icons/project-icons/podsupdater.png" width="32" height="32" alt="PodsUpdater"></a> | **[PodsUpdater](https://github.com/kizitonwose/PodsUpdater)** | macOS app which helps you manage dependency releases in your Podfile. | `Swift` | [Source](https://github.com/kizitonwose/PodsUpdater) | `MIT` |
| <a href="https://github.com/shaojiankui/ProfilesManager"><img src="./icons/project-icons/profilesmanager.png" width="32" height="32" alt="ProfilesManager"></a> | **[ProfilesManager](https://github.com/shaojiankui/ProfilesManager)** | Apple iOS/macOS Provisioning Profiles management,.provisionprofile, .mobileprovision files manager tool for mac. | `Objective-C` | [Source](https://github.com/shaojiankui/ProfilesManager) | `MIT` |
| <a href="https://github.com/onmyway133/PushNotifications"><img src="./icons/project-icons/pushnotifications.png" width="32" height="32" alt="PushNotifications"></a> | **[PushNotifications](https://github.com/onmyway133/PushNotifications)** | macOS app to test push notifications on iOS and Android. | `JavaScript` | [Source](https://github.com/onmyway133/PushNotifications) | `MIT` |
| <a href="https://github.com/InjoyDeng/ResignTool"><img src="./icons/project-icons/resigntool.png" width="32" height="32" alt="ResignTool"></a> | **[ResignTool](https://github.com/InjoyDeng/ResignTool)** | This is an app for macOS that can (re)sign apps and bundle them into ipa files that are ready to be installed on an iOS device. | `Objective-C` | [Source](https://github.com/InjoyDeng/ResignTool) | `MIT` |
| <a href="https://github.com/onurgenes/Resizr"><img src="./icons/project-icons/resizr.png" width="32" height="32" alt="Resizr"></a> | **[Resizr](https://github.com/onurgenes/Resizr)** | MacOS application for creating AppIcon for iOS and Android apps. | `Swift` | [Source](https://github.com/onurgenes/Resizr) | `MIT` |
| <a href="https://github.com/shaojiankui/SmartPush"><img src="./icons/project-icons/smartpush.png" width="32" height="32" alt="SmartPush"></a> | **[SmartPush](https://github.com/shaojiankui/SmartPush)** | iOS Push Notification Debug App. | `Objective-C` | [Source](https://github.com/shaojiankui/SmartPush) | `MIT` |
| <a href="https://github.com/iseebi/TransporterPad"><img src="./icons/project-icons/transporterpad.png" width="32" height="32" alt="TransporterPad"></a> | **[TransporterPad](https://github.com/iseebi/TransporterPad)** | iOS/Android app deployment tool for macOS. | `Swift` | [Source](https://github.com/iseebi/TransporterPad) | `MIT` |
| <a href="https://github.com/insidegui/WWDC"><img src="./icons/project-icons/wwdc.png" width="32" height="32" alt="WWDC"></a> | **[WWDC](https://github.com/insidegui/WWDC)** | Unofficial WWDC app for macOS. | `Swift` | [Source](https://github.com/insidegui/WWDC) | `MIT` |
| <a href="https://github.com/ssamadgh/WWDCsrt"><img src="./icons/project-icons/wwdc-srt.png" width="32" height="32" alt="WWDC.srt"></a> | **[WWDC.srt](https://github.com/ssamadgh/WWDCsrt)** | Powerful app for downloading subtitle for each WWDC session video since 2013 in (srt) format. | `Swift` | [Source](https://github.com/ssamadgh/WWDCsrt) | `MIT` |
| <a href="https://github.com/RobotsAndPencils/XcodesApp"><img src="./icons/project-icons/xcodes-app.png" width="32" height="32" alt="Xcodes.app"></a> | **[Xcodes.app](https://github.com/RobotsAndPencils/XcodesApp)** | The easiest way to install and switch between multiple versions of Xcode. | `Swift` | [Source](https://github.com/RobotsAndPencils/XcodesApp) | `MIT` |
| <a href="https://github.com/novemberfiveco/xib2Storyboard"><img src="./icons/project-icons/xib2storyboard.png" width="32" height="32" alt="xib2Storyboard"></a> | **[xib2Storyboard](https://github.com/novemberfiveco/xib2Storyboard)** | Tool to convert Xcode .xib to .storyboard files. | `Objective-C` | [Source](https://github.com/novemberfiveco/xib2Storyboard) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="json-parsing"></a>
### 🔄 JSON Parsing

> JSON formatters, syntax highlighters, schema validators, and data tree inspectors.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/zadr/j2s"><img src="./icons/project-icons/j2s.png" width="32" height="32" alt="j2s"></a> | **[j2s](https://github.com/zadr/j2s)** | macOS app to convert JSON objects into Swift structs (currently targets Swift 4 and Codable). | `Swift` | [Source](https://github.com/zadr/j2s) | `MIT` |
| <a href="https://github.com/AppCraft-LLC/json-mapper"><img src="./icons/project-icons/json-mapper.png" width="32" height="32" alt="JSON Mapper"></a> | **[JSON Mapper](https://github.com/AppCraft-LLC/json-mapper)** | Simple macOS app to generate Swift Object Mapper classes from JSON. | `Swift` | [Source](https://github.com/AppCraft-LLC/json-mapper) | `MIT` |
| <a href="https://github.com/chanonly123/Json-Model-Generator"><img src="./icons/project-icons/json-to-model-class.png" width="32" height="32" alt="JSON to Model class"></a> | **[JSON to Model class](https://github.com/chanonly123/Json-Model-Generator)** | Template based highly customizable macOS app to generate classes from JSON string, supports many languages. | `Swift` | [Source](https://github.com/chanonly123/Json-Model-Generator) | `MIT` |
| <a href="https://github.com/Ahmed-Ali/JSONExport"><img src="./icons/project-icons/jsonexport.png" width="32" height="32" alt="JSONExport"></a> | **[JSONExport](https://github.com/Ahmed-Ali/JSONExport)** | Desktop application for macOS which enables you to export JSON objects as model classes with their associated constructors, utility methods, setters and getters in your favorite language. | `Swift` | [Source](https://github.com/Ahmed-Ali/JSONExport) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="other-development"></a>
### 🔧 Other Development

> Specialized developer tools, regex visualizers, string processors, and testing utilities.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://boop.okat.best"><img src="./icons/project-icons/boop.png" width="32" height="32" alt="Boop"></a> | **[Boop](https://boop.okat.best)** | A scriptable scratchpad for developers. | `Swift` | [Website](https://boop.okat.best) • [Source](https://github.com/IvanMathy/Boop) | `MIT` |
| <a href="https://github.com/Yasumoto/ChefInspector"><img src="./icons/project-icons/chefinspector.png" width="32" height="32" alt="ChefInspector"></a> | **[ChefInspector](https://github.com/Yasumoto/ChefInspector)** | Node and Attribute viewer for Chef | `Swift` | [Source](https://github.com/Yasumoto/ChefInspector) | `MIT` |
| <a href="https://github.com/dcsch/macho-browser"><img src="./icons/project-icons/macho-browser.png" width="32" height="32" alt="macho-browser"></a> | **[macho-browser](https://github.com/dcsch/macho-browser)** | Browser for macOS Mach-O binaries. | `Objective-C` | [Source](https://github.com/dcsch/macho-browser) | `MIT` |
| <a href="https://github.com/emqx/MQTTX"><img src="./icons/project-icons/mqttx.png" width="32" height="32" alt="MQTTX"></a> | **[MQTTX](https://github.com/emqx/MQTTX)** | An elegant Cross-platform MQTT 5.0 desktop client. | `JavaScript` | [Source](https://github.com/emqx/MQTTX) | `MIT` |
| <a href="https://github.com/ant4g0nist/vegvisir"><img src="./icons/project-icons/vegvisir.png" width="32" height="32" alt="vegvisir"></a> | **[vegvisir](https://github.com/ant4g0nist/vegvisir)** | Browser based GUI for LLDB Debugger. | `JavaScript` | [Source](https://github.com/ant4g0nist/vegvisir) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="web-development"></a>
### 🌍 Web Development

> Local web servers, HTTP debugging proxies, static site generators, and API inspection tools.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/RafalWilinski/s3-uploader"><img src="./icons/project-icons/aws-s3-uploader.png" width="32" height="32" alt="aws-s3-uploader"></a> | **[aws-s3-uploader](https://github.com/RafalWilinski/s3-uploader)** | Simple macOS app for uploading files to Amazon Web Services. | `JavaScript` | [Source](https://github.com/RafalWilinski/s3-uploader) | `MIT` |
| <a href="https://github.com/TheNewNormal/corectl.app"><img src="./icons/project-icons/corectl-app-for-macos.png" width="32" height="32" alt="Corectl App for macOS"></a> | **[Corectl App for macOS](https://github.com/TheNewNormal/corectl.app)** | Corectl App is a macOS Status bar App which works like a wrapper around the corectl command line tool corectld to control the server runtime process. | `Swift` | [Source](https://github.com/TheNewNormal/corectl.app) | `MIT` |
| <a href="https://github.com/TheNewNormal/coreos-osx"><img src="./icons/project-icons/coreos-vm.png" width="32" height="32" alt="CoreOS VM"></a> | **[CoreOS VM](https://github.com/TheNewNormal/coreos-osx)** | CoreOS VM is macOS status bar app which allows in an easy way to control CoreOS VM on your Mac. | `Objective-C` | [Source](https://github.com/TheNewNormal/coreos-osx) | `MIT` |
| <a href="https://httptoolkit.com"><img src="./icons/project-icons/http-toolkit.png" width="32" height="32" alt="HTTP Toolkit"></a> | **[HTTP Toolkit](https://httptoolkit.com)** | HTTP Toolkit is a cross-platform tool to intercept, debug & mock HTTP. | `TypeScript` | [Website](https://httptoolkit.com) • [Source](https://github.com/httptoolkit/httptoolkit-desktop) | `MIT` |
| <a href="https://github.com/Kong/insomnia"><img src="./icons/project-icons/insomnia.png" width="32" height="32" alt="Insomnia"></a> | **[Insomnia](https://github.com/Kong/insomnia)** | Insomnia is a cross-platform REST client, built on top of Electron. | `JavaScript` | [Source](https://github.com/Kong/insomnia) | `MIT` |
| <a href="https://github.com/trulyronak/itunesconnect"><img src="./icons/project-icons/itunesconnect.png" width="32" height="32" alt="iTunesConnect"></a> | **[iTunesConnect](https://github.com/trulyronak/itunesconnect)** | macOS app to let you access iTunesConnect. | `Swift` | [Source](https://github.com/trulyronak/itunesconnect) | `MIT` |
| <a href="https://github.com/Daniel-Sanche/KubeMonitor"><img src="./icons/project-icons/kubemonitor.png" width="32" height="32" alt="KubeMonitor"></a> | **[KubeMonitor](https://github.com/Daniel-Sanche/KubeMonitor)** | KubeMonitor is a macOS app that displays information about your active Kubernetes cluster in your menu bar. | `Swift` | [Source](https://github.com/Daniel-Sanche/KubeMonitor) | `MIT` |
| <a href="https://github.com/nsriram/KubeSwitch"><img src="./icons/project-icons/kubeswitch.png" width="32" height="32" alt="KubeSwitch"></a> | **[KubeSwitch](https://github.com/nsriram/KubeSwitch)** | KubeSwitch lists the available kubernetes cluster contexts on the mac, in Mac's Menu bar. | `Swift` | [Source](https://github.com/nsriram/KubeSwitch) | `MIT` |
| <a href="https://github.com/RoyalIcing/Lantern"><img src="./icons/project-icons/lantern.png" width="32" height="32" alt="Lantern"></a> | **[Lantern](https://github.com/RoyalIcing/Lantern)** | Dedicated Mac app for website auditing and crawling. | `Swift` | [Source](https://github.com/RoyalIcing/Lantern) | `MIT` |
| <a href="https://github.com/plan44/localSites"><img src="./icons/project-icons/localsites.png" width="32" height="32" alt="LocalSites"></a> | **[LocalSites](https://github.com/plan44/localSites)** | Simple Menu Bar (Status Bar) App for macOS listing local Bonjour websites (as Safari 11 no longer has Bonjour Bookmarks). | `Swift` | [Source](https://github.com/plan44/localSites) | `MIT` |
| <a href="https://github.com/vsaravind007/nodeScratchpad"><img src="./icons/project-icons/nodescratchpad.png" width="32" height="32" alt="nodeScratchpad"></a> | **[nodeScratchpad](https://github.com/vsaravind007/nodeScratchpad)** | Evaluate Nodejs/JS code snippets from Menubar. | `Swift` | [Source](https://github.com/vsaravind007/nodeScratchpad) | `MIT` |
| <a href="https://requestly.com"><img src="./icons/project-icons/requestly.png" width="32" height="32" alt="Requestly"></a> | **[Requestly](https://requestly.com)** | A lightweight open-source API Development, Testing & Mocking platform | `JavaScript` | [Website](https://requestly.com) • [Source](https://github.com/requestly/requestly) | `MIT` |
| <a href="https://simplelocalize.io"><img src="./icons/project-icons/simplelocalize-cli.png" width="32" height="32" alt="SimpleLocalize CLI"></a> | **[SimpleLocalize CLI](https://simplelocalize.io)** | Open source tool for managing i18n keys in software projects. | `Swift` | [Website](https://simplelocalize.io) • [Source](https://github.com/simplelocalize/simplelocalize-cli) | `MIT` |
| <a href="https://github.com/inket/stts"><img src="./icons/project-icons/stts.png" width="32" height="32" alt="stts"></a> | **[stts](https://github.com/inket/stts)** | macOS app for monitoring the status of cloud services. | `Swift` | [Source](https://github.com/inket/stts) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="downloader"></a>
### ⬇️ Downloader

> Media downloaders, YouTube download utilities, Homebrew cask grabbers, and batch fetchers.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/yep/app-downloader"><img src="./icons/project-icons/app-downloader.png" width="32" height="32" alt="App Downloader"></a> | **[App Downloader](https://github.com/yep/app-downloader)** | Easily search and download macOS apps from the huge homebrew cask app catalog. | `Swift` | [Source](https://github.com/yep/app-downloader) | `MIT` |
| <a href="https://appfair.app"><img src="./icons/project-icons/app-fair.png" width="32" height="32" alt="App Fair"></a> | **[App Fair](https://appfair.app)** | Find and install macOS apps from Homebrew Cask and Fairground App catalogs. | `Swift` | [Website](https://appfair.app) • [Source](https://github.com/App-Fair/App) | `MIT` |
| <a href="https://aerolite.dev/applite"><img src="./icons/project-icons/applite.png" width="32" height="32" alt="Applite"></a> | **[Applite](https://aerolite.dev/applite)** | User-friendly GUI app for Homebrew Casks. Install, update, and uninstall apps with a single click. | `Swift` | [Website](https://aerolite.dev/applite) • [Source](https://github.com/milanvarady/Applite) | `MIT` |
| <a href="https://subhra74.github.io/xdm"><img src="./icons/project-icons/extream-download-manager.png" width="32" height="32" alt="Extream Download Manager"></a> | **[Extream Download Manager](https://subhra74.github.io/xdm)** | a powerful tool to increase download speeds up to 500% | `Java` | [Website](https://subhra74.github.io/xdm) • [Source](https://github.com/subhra74/xdm) | `MIT` |
| <a href="https://filezilla-project.org"><img src="./icons/project-icons/filezilla.svg" width="32" height="32" alt="FileZilla"></a> | **[FileZilla](https://filezilla-project.org)** | Free open-source FTP, FTPS, and SFTP client. | `c++` | [Website](https://filezilla-project.org) • [Source](https://sourceforge.net/projects/filezilla/) | `MIT` |
| <a href="https://github.com/Kevin-De-Koninck/Get-It"><img src="./icons/project-icons/get-it.png" width="32" height="32" alt="Get It"></a> | **[Get It](https://github.com/Kevin-De-Koninck/Get-It)** | Native macOS video/audio downloader. Think of it as a youtube downloader that works on many sites. | `Swift` | [Source](https://github.com/Kevin-De-Koninck/Get-It) | `MIT` |
| <a href="https://motrix.app"><img src="./icons/project-icons/motrix.png" width="32" height="32" alt="Motrix"></a> | **[Motrix](https://motrix.app)** | A full-featured download manager. | `JavaScript` | [Website](https://motrix.app) • [Source](https://github.com/agalwood/Motrix) | `MIT` |
| <a href="https://github.com/Pjirlip/Pillager"><img src="./icons/project-icons/pillager.png" width="32" height="32" alt="Pillager"></a> | **[Pillager](https://github.com/Pjirlip/Pillager)** | macOS Video Downloader written in Swift and Objective-C. | `Objective-C` | [Source](https://github.com/Pjirlip/Pillager) | `MIT` |
| <a href="https://github.com/FaisalUmair/udemy-downloader-gui"><img src="./icons/project-icons/udemy-downloader-gui.png" width="32" height="32" alt="udemy-downloader-gui"></a> | **[udemy-downloader-gui](https://github.com/FaisalUmair/udemy-downloader-gui)** | desktop application for downloading Udemy Courses. | `JavaScript` | [Source](https://github.com/FaisalUmair/udemy-downloader-gui) | `MIT` |
| <a href="https://github.com/DenBeke/YouTube-Downloader-for-macOS"><img src="./icons/project-icons/youtube-downloader-for-macos.png" width="32" height="32" alt="YouTube Downloader for macOS"></a> | **[YouTube Downloader for macOS](https://github.com/DenBeke/YouTube-Downloader-for-macOS)** | Simple menu bar app to download YouTube movies on your Mac. I wrote this as a test project to learn more about app development on macOS. | `Swift` | [Source](https://github.com/DenBeke/YouTube-Downloader-for-macOS) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="editors"></a>
### 📝 Editors

> General text and code editors, native macOS typing suites, and distraction-free editors.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://auroraeditor.com"><img src="./icons/project-icons/auroraeditor.png" width="32" height="32" alt="AuroraEditor"></a> | **[AuroraEditor](https://auroraeditor.com)** | Lightweight Code Editor (IDE) for macOS. | `Swift` | [Website](https://auroraeditor.com) • [Source](https://github.com/AuroraEditor/AuroraEditor) | `MIT` |
| <a href="https://www.chimehq.com"><img src="./icons/project-icons/chime.png" width="32" height="32" alt="Chime"></a> | **[Chime](https://www.chimehq.com)** | An editor for macOS with native design, syntax highlighting, and LSP support | `Swift` | [Website](https://www.chimehq.com) • [Source](https://github.com/ChimeHQ/Chime) | `MIT` |
| <a href="https://www.codeedit.app"><img src="./icons/project-icons/codeedit.png" width="32" height="32" alt="CodeEdit"></a> | **[CodeEdit](https://www.codeedit.app)** | CodeEdit App for macOS – Elevate your code editing experience. Open source, free forever. | `Swift` | [Website](https://www.codeedit.app) • [Source](https://github.com/CodeEditApp/CodeEdit) | `MIT` |
| <a href="https://www.geany.org"><img src="./icons/project-icons/geany.png" width="32" height="32" alt="Geany"></a> | **[Geany](https://www.geany.org)** | Geany is a powerful, stable and lightweight programmer's text editor that provides tons of useful features without bogging down your workflow. | `C` | [Website](https://www.geany.org) • [Source](https://github.com/geany/geany) | `MIT` |
| <a href="https://github.com/maxmilian/markout"><img src="./icons/project-icons/markout.png" width="32" height="32" alt="Markout"></a> | **[Markout](https://github.com/maxmilian/markout)** | Native Markdown editor with live preview, offline KaTeX math, Mermaid diagrams, and HTML/PDF export. | `Swift` | [Source](https://github.com/maxmilian/markout) | `MIT` |
| <a href="https://github.com/maxnd/mxMarkEdit"><img src="./icons/project-icons/mxmarkedit.png" width="32" height="32" alt="mxMarkEdit"></a> | **[mxMarkEdit](https://github.com/maxnd/mxMarkEdit)** | A visual editor of Markdown document, tasks and tables. | `free-pascal` | [Source](https://github.com/maxnd/mxMarkEdit) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="csv"></a>
### 📊 CSV

> Tabular data viewers, spreadsheet inspectors, and high-speed CSV file editors.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://apps.apple.com/app/table-tool/id1122008420"><img src="./icons/project-icons/tabletool.png" width="32" height="32" alt="TableTool"></a> | **[TableTool](https://apps.apple.com/app/table-tool/id1122008420)** | A simple CSV editor for macOS. | `Objective-C` | [Website](https://apps.apple.com/app/table-tool/id1122008420) • [Source](https://github.com/jakob/TableTool) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="json"></a>
### 📋 JSON

> Dedicated JSON documents editors, structure organizers, and tree manipulation apps.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/fand/json-editor-app"><img src="./icons/project-icons/json-editor.png" width="32" height="32" alt="JSON Editor"></a> | **[JSON Editor](https://github.com/fand/json-editor-app)** | Dead simple JSON editor using josdejong/jsoneditor | `TypeScript` | [Source](https://github.com/fand/json-editor-app) | `MIT` |
| <a href="https://github.com/wellsjo/JSON-Splora"><img src="./icons/project-icons/json-splora.png" width="32" height="32" alt="JSON-Splora"></a> | **[JSON-Splora](https://github.com/wellsjo/JSON-Splora)** | GUI for editing, visualizing, and manipulating JSON data. | `JavaScript` | [Source](https://github.com/wellsjo/JSON-Splora) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="markdown"></a>
### 📝 Markdown

> Markdown editors, live preview tools, note renderers, and technical documentation writers.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/gingko/client"><img src="./icons/project-icons/gingko.png" width="32" height="32" alt="Gingko"></a> | **[Gingko](https://github.com/gingko/client)** | Tree-structured markdown editor for macOS, Windows, and Linux. | `Elm` | [Source](https://github.com/gingko/client) | `MIT` |
| <a href="https://uselinked.com"><img src="./icons/project-icons/linked.png" width="32" height="32" alt="linked"></a> | **[linked](https://uselinked.com)** | 🧾 Your daily journal app, diary or anything else to unclutter your mind. Let linked help you get focused by writing down what is in your mind on a daily basis. | `JavaScript` | [Website](https://uselinked.com) • [Source](https://github.com/lostdesign/linked) | `MIT` |
| <a href="https://github.com/MacDownApp/macdown"><img src="./icons/project-icons/macdown.png" width="32" height="32" alt="MacDown"></a> | **[MacDown](https://github.com/MacDownApp/macdown)** | Markdown editor for macOS. | `Objective-C` | [Source](https://github.com/MacDownApp/macdown) | `MIT` |
| <a href="https://github.com/ruspg/markdown-quicklook"><img src="./icons/project-icons/markdown-quicklook.png" width="32" height="32" alt="markdown-quicklook"></a> | **[markdown-quicklook](https://github.com/ruspg/markdown-quicklook)** | Rendered Markdown Quick Look preview with syntax highlighting, YAML front matter, configurable fonts/colors, and a menu bar toggle. | `Swift` | [Source](https://github.com/ruspg/markdown-quicklook) | `MIT` |
| <a href="https://markedit.app"><img src="./icons/project-icons/markedit.png" width="32" height="32" alt="MarkEdit"></a> | **[MarkEdit](https://markedit.app)** | MarkEdit is a free and open-source Markdown editor, for macOS. It's just like TextEdit on Mac but dedicated to Markdown. | `Swift` | [Website](https://markedit.app) • [Source](https://github.com/MarkEdit-app/MarkEdit) | `MIT` |
| <a href="https://notenik.app"><img src="./icons/project-icons/notenik.png" width="32" height="32" alt="Notenik"></a> | **[Notenik](https://notenik.app)** | Note-taking app with many organizational options. | `Swift` | [Website](https://notenik.app) • [Source](https://github.com/hbowie/notenik-swift) | `MIT` |
| <a href="https://obsidian.md"><img src="./icons/project-icons/obsidian-plugins-themes.png" width="32" height="32" alt="Obsidian plugins & themes"></a> | **[Obsidian plugins & themes](https://obsidian.md)** | Community plugins list, theme list, and releases of Obsidian. | `JavaScript` | [Website](https://obsidian.md) • [Source](https://github.com/obsidianmd/obsidian-releases) | `MIT` |
| <a href="https://github.com/lukakerr/Pine"><img src="./icons/project-icons/pine.png" width="32" height="32" alt="Pine"></a> | **[Pine](https://github.com/lukakerr/Pine)** | A modern MacOS markdown editor. | `Swift` | [Source](https://github.com/lukakerr/Pine) | `MIT` |
| <a href="https://www.qownnotes.org"><img src="./icons/project-icons/qownnotes.png" width="32" height="32" alt="QOwnNotes"></a> | **[QOwnNotes](https://www.qownnotes.org)** | Plain-text file notepad and todo-list manager with markdown support and ownCloud / Nextcloud integration. | `C++` | [Website](https://www.qownnotes.org) • [Source](https://github.com/pbek/QOwnNotes) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="tex"></a>
### 📐 TeX

> LaTeX typesetting tools, mathematical formula editors, and academic paper generators.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://bibdesk.sourceforge.io"><img src="./icons/project-icons/bibdesk.svg" width="32" height="32" alt="BibDesk"></a> | **[BibDesk](https://bibdesk.sourceforge.io)** | Use BibDesk to edit and manage your bibliography | `Objective-C` | [Website](https://bibdesk.sourceforge.io) • [Source](https://sourceforge.net/projects/bibdesk/) | `MIT` |
| <a href="https://github.com/qilin-editor/qilin-app"><img src="./icons/project-icons/qilin-editor.png" width="32" height="32" alt="Qilin Editor"></a> | **[Qilin Editor](https://github.com/qilin-editor/qilin-app)** | Text editor for exact sciences with built-in KaTeX/AsciiMath support. | `JavaScript` | [Source](https://github.com/qilin-editor/qilin-app) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="text"></a>
### ✏️ Text

> Plain text scratchpads, notepad alternatives, and distraction-free writing environments.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://micro-editor.github.io"><img src="./icons/project-icons/micro.png" width="32" height="32" alt="micro"></a> | **[micro](https://micro-editor.github.io)** | A terminal-based text editor that aims to be easy to use and intuitive, while also taking advantage of the capabilities of modern terminals. | `Go` | [Website](https://micro-editor.github.io) • [Source](https://github.com/zyedidia/micro) | `MIT` |
| <a href="https://notesnook.com"><img src="./icons/project-icons/notesnook.png" width="32" height="32" alt="Notesnook"></a> | **[Notesnook](https://notesnook.com)** | A fully open source and end-to-end encrypted note taking alternative to Evernote. | `JavaScript` | [Website](https://notesnook.com) • [Source](https://github.com/streetwriters/notesnook) | `MIT` |
| <a href="https://github.com/brunophilipe/noto"><img src="./icons/project-icons/noto.png" width="32" height="32" alt="Noto"></a> | **[Noto](https://github.com/brunophilipe/noto)** | Plain text editor for macOS with customizable themes. | `Swift` | [Source](https://github.com/brunophilipe/noto) | `MIT` |
| <a href="https://github.com/subethaedit/SubEthaEdit"><img src="./icons/project-icons/subethaedit.png" width="32" height="32" alt="SubEthaEdit"></a> | **[SubEthaEdit](https://github.com/subethaedit/SubEthaEdit)** | General purpose plain text editor for macOS. Widely known for its live collaboration feature. | `Objective-C` | [Source](https://github.com/subethaedit/SubEthaEdit) | `MIT` |
| <a href="https://github.com/textmate/textmate"><img src="./icons/project-icons/textmate.png" width="32" height="32" alt="TextMate"></a> | **[TextMate](https://github.com/textmate/textmate)** | TextMate is a graphical text editor for macOS. | `Objective-C` | [Source](https://github.com/textmate/textmate) | `MIT` |
| <a href="https://codingfriends.github.io/Tincta"><img src="./icons/project-icons/tincta.png" width="32" height="32" alt="Tincta"></a> | **[Tincta](https://codingfriends.github.io/Tincta)** | One-window text editor with syntax highlighting. | `Objective-C` | [Website](https://codingfriends.github.io/Tincta) • [Source](https://github.com/CodingFriends/Tincta) | `MIT` |
| <a href="https://github.com/qvacua/vimr"><img src="./icons/project-icons/vimr.png" width="32" height="32" alt="VimR"></a> | **[VimR](https://github.com/qvacua/vimr)** | Refined Neovim experience for macOS. | `Swift` | [Source](https://github.com/qvacua/vimr) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="extensions"></a>
### 🧩 Extensions

> Quick Look generators, Finder context menu extensions, and share sheet utilities.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://adguard.com/en/welcome.html"><img src="./icons/project-icons/adguard-for-safari.png" width="32" height="32" alt="AdGuard for Safari"></a> | **[AdGuard for Safari](https://adguard.com/en/welcome.html)** | The most advanced ad blocking extension for Safari | `JavaScript` | [Website](https://adguard.com/en/welcome.html) • [Source](https://github.com/adguardteam/adguardforsafari) | `MIT` |
| <a href="https://github.com/Capevace/BetterPiP"><img src="./icons/project-icons/betterpip.png" width="32" height="32" alt="BetterPiP"></a> | **[BetterPiP](https://github.com/Capevace/BetterPiP)** | Use native picture-in-picture with browsers such as Google Chrome for HTML5 videos. | `Swift` | [Source](https://github.com/Capevace/BetterPiP) | `MIT` |
| <a href="https://florian.codes/projects/is-it-private"><img src="./icons/project-icons/is-it-private.png" width="32" height="32" alt="Is It Private?"></a> | **[Is It Private?](https://florian.codes/projects/is-it-private)** | A Safari Extension providing a toolbar icon that changes its visual appearance if Private Browsing is enabled. | `Swift` | [Website](https://florian.codes/projects/is-it-private) • [Source](https://github.com/ffittschen/IsItPrivate) | `MIT` |
| <a href="https://github.com/artginzburg/MiddleClick-Ventura"><img src="./icons/project-icons/middleclick.png" width="32" height="32" alt="Middleclick"></a> | **[Middleclick](https://github.com/artginzburg/MiddleClick-Ventura)** | Emulate a scroll wheel click with three finger Click or Tap on MacBook trackpad and Magic Mouse | `C` | [Source](https://github.com/artginzburg/MiddleClick-Ventura) | `MIT` |
| <a href="https://nef.bow-swift.io"><img src="./icons/project-icons/nef.png" width="32" height="32" alt="nef"></a> | **[nef](https://nef.bow-swift.io)** | This Xcode extension enables you to make a code selection and export it to a snippets. Available on Mac AppStore. | `Swift` | [Website](https://nef.bow-swift.io) • [Source](https://github.com/bow-swift/nef-plugin) | `MIT` |
| <a href="https://github.com/fphilipe/PageExtender.app"><img src="./icons/project-icons/pageextender.png" width="32" height="32" alt="PageExtender"></a> | **[PageExtender](https://github.com/fphilipe/PageExtender.app)** | Extend pages with your own CSS and JS files. | `Swift` | [Source](https://github.com/fphilipe/PageExtender.app) | `MIT` |
| <a href="https://github.com/arnoappenzeller/PiPifier"><img src="./icons/project-icons/pipifier.png" width="32" height="32" alt="PiPifier"></a> | **[PiPifier](https://github.com/arnoappenzeller/PiPifier)** | PiPifier is a native macOS 10.12 Safari extension that lets you use every HTML5 video in Picture in Picture mode. | `Swift` | [Source](https://github.com/arnoappenzeller/PiPifier) | `MIT` |
| <a href="https://github.com/bfmatei/PiPTool"><img src="./icons/project-icons/piptool.png" width="32" height="32" alt="PiPTool"></a> | **[PiPTool](https://github.com/bfmatei/PiPTool)** | Add the Picture-in-Picture Functionality to YouTube, Netflix, Plex and other video broadcasting services in macOS. | `JavaScript` | [Source](https://github.com/bfmatei/PiPTool) | `MIT` |
| <a href="https://github.com/AlexPerathoner/Sessions"><img src="./icons/project-icons/sessions.png" width="32" height="32" alt="Sessions"></a> | **[Sessions](https://github.com/AlexPerathoner/Sessions)** | Safari extension to save your working sessions | `Swift` | [Source](https://github.com/AlexPerathoner/Sessions) | `MIT` |
| <a href="https://jintin.github.io/Swimat"><img src="./icons/project-icons/swimat.png" width="32" height="32" alt="Swimat"></a> | **[Swimat](https://jintin.github.io/Swimat)** | Swimat is an Xcode plug-in to format your Swift code. | `Swift` | [Website](https://jintin.github.io/Swimat) • [Source](https://github.com/Jintin/Swimat) | `MIT` |
| <a href="https://github.com/87kangsw/ThenGenerator"><img src="./icons/project-icons/thengenerator.png" width="32" height="32" alt="ThenGenerator"></a> | **[ThenGenerator](https://github.com/87kangsw/ThenGenerator)** | Xcode Source Editor Extension for 'Then' | `Swift` | [Source](https://github.com/87kangsw/ThenGenerator) | `MIT` |
| <a href="https://github.com/Swift-open-source/UltraTabSaver"><img src="./icons/project-icons/ultra-tabsaver.png" width="32" height="32" alt="Ultra TabSaver"></a> | **[Ultra TabSaver](https://github.com/Swift-open-source/UltraTabSaver)** | Ultra TabSaver is an open-source Tab Manager for Safari | `Swift` | [Source](https://github.com/Swift-open-source/UltraTabSaver) | `MIT` |
| <a href="https://github.com/leonspok/Yape"><img src="./icons/project-icons/yape.png" width="32" height="32" alt="Yape"></a> | **[Yape](https://github.com/leonspok/Yape)** | Yet Another PiP Extension. Finds all HTML5 videos on a webpage and allows you to play them in Picture-in-Picture mode from the Safari toolbar. | `Swift` | [Source](https://github.com/leonspok/Yape) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="finder"></a>
### 🔍 Finder

> Finder enhancements, folder bookmarkers, duplicate detectors, and advanced file browsers.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/jbtule/cdto"><img src="./icons/project-icons/cd-to.png" width="32" height="32" alt="cd to..."></a> | **[cd to...](https://github.com/jbtule/cdto)** | Finder Toolbar app to open the current directory in the Terminal | `Objective-C` | [Source](https://github.com/jbtule/cdto) | `MIT` |
| <a href="https://github.com/Clipy/Clipy"><img src="./icons/project-icons/clipy.png" width="32" height="32" alt="Clipy"></a> | **[Clipy](https://github.com/Clipy/Clipy)** | Clipy is a Clipboard extension app for macOS. | `Swift` | [Source](https://github.com/Clipy/Clipy) | `MIT` |
| <a href="https://github.com/hluk/CopyQ"><img src="./icons/project-icons/copyq.png" width="32" height="32" alt="CopyQ"></a> | **[CopyQ](https://github.com/hluk/CopyQ)** | Clipboard manager with advanced features | `C++` | [Source](https://github.com/hluk/CopyQ) | `MIT` |
| <a href="https://dupeguru.voltaicideas.net"><img src="./icons/project-icons/dupeguru.png" width="32" height="32" alt="dupeGuru"></a> | **[dupeGuru](https://dupeguru.voltaicideas.net)** | dupeGuru is a tool to find duplicate files on your computer. It can scan using file names and file contents. | `Objective-C` | [Website](https://dupeguru.voltaicideas.net) • [Source](https://github.com/arsenetar/dupeguru/) | `MIT` |
| <a href="https://github.com/powerwolf543/DuplicateFinder"><img src="./icons/project-icons/duplicate-finder.png" width="32" height="32" alt="Duplicate Finder"></a> | **[Duplicate Finder](https://github.com/powerwolf543/DuplicateFinder)** | It's a useful tool that would help you to find all duplicate files which have the same names in the specific folder. | `Swift` | [Source](https://github.com/powerwolf543/DuplicateFinder) | `MIT` |
| <a href="https://github.com/onmyway133/FinderGo"><img src="./icons/project-icons/finder-go.png" width="32" height="32" alt="Finder Go"></a> | **[Finder Go](https://github.com/onmyway133/FinderGo)** | macOS app and Finder Sync Extension to open Terminal, iTerm, Hyper from Finder. | `Swift` | [Source](https://github.com/onmyway133/FinderGo) | `MIT` |
| <a href="https://github.com/Mortennn/FiScript"><img src="./icons/project-icons/fiscript.png" width="32" height="32" alt="FiScript"></a> | **[FiScript](https://github.com/Mortennn/FiScript)** | Execute custom scripts from the MacOS context menu (CTRL+click) in Finder. | `Swift` | [Source](https://github.com/Mortennn/FiScript) | `MIT` |
| <a href="https://www.mucommander.com"><img src="./icons/project-icons/mucommander.png" width="32" height="32" alt="muCommander"></a> | **[muCommander](https://www.mucommander.com)** | A lightweight, cross-platform file manager with a dual-pane interface. | `Java` | [Website](https://www.mucommander.com) • [Source](https://github.com/mucommander/mucommander) | `MIT` |
| <a href="https://github.com/sozercan/OpenInCode"><img src="./icons/project-icons/openincode.png" width="32" height="32" alt="OpenInCode"></a> | **[OpenInCode](https://github.com/sozercan/OpenInCode)** | Finder toolbar app to open current folder in Visual Studio Code. | `Objective-C` | [Source](https://github.com/sozercan/OpenInCode) | `MIT` |
| <a href="https://github.com/Ji4n1ng/OpenInTerminal"><img src="./icons/project-icons/openinterminal.png" width="32" height="32" alt="OpenInTerminal"></a> | **[OpenInTerminal](https://github.com/Ji4n1ng/OpenInTerminal)** | Finder Toolbar app for macOS to open the current directory in Terminal, iTerm, Hyper or Alacritty. | `Swift` | [Source](https://github.com/Ji4n1ng/OpenInTerminal) | `MIT` |
| <a href="https://github.com/sindresorhus/quick-look-plugins"><img src="./icons/project-icons/quick-look-plugins.png" width="32" height="32" alt="Quick Look plugins"></a> | **[Quick Look plugins](https://github.com/sindresorhus/quick-look-plugins)** | List of useful Quick Look plugins for developers. | `Objective-C` | [Source](https://github.com/sindresorhus/quick-look-plugins) | `MIT` |
| <a href="https://saneclick.com"><img src="./icons/project-icons/saneclick.png" width="32" height="32" alt="SaneClick"></a> | **[SaneClick](https://saneclick.com)** | Finder extension with 51+ right-click actions for file management, image conversion, and developer tools. | `Swift` | [Website](https://saneclick.com) • [Source](https://github.com/sane-apps/SaneClick) | `MIT` |
| <a href="https://github.com/ajeetdsouza/zoxide"><img src="./icons/project-icons/zoxide.png" width="32" height="32" alt="zoxide"></a> | **[zoxide](https://github.com/ajeetdsouza/zoxide)** | zoxide is a smarter cd command for your terminal. | `Rust` | [Source](https://github.com/ajeetdsouza/zoxide) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="games"></a>
### 🎮 Games

> Open-source games, console emulators, game engines, and recreational apps for macOS.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://play0ad.com"><img src="./icons/project-icons/0-a-d.svg" width="32" height="32" alt="0 A.D."></a> | **[0 A.D.](https://play0ad.com)** | Real-time strategy game of ancient warfare | `C++` | [Website](https://play0ad.com) • [Source](https://svn.wildfiregames.com/public/ps/trunk/) | `MIT` |
| <a href="https://ariessciences.com/highlight?product=tic-tac-toe"><img src="./icons/project-icons/amazing-tic-tac-toe.svg" width="32" height="32" alt="Amazing Tic Tac Toe"></a> | **[Amazing Tic Tac Toe](https://ariessciences.com/highlight?product=tic-tac-toe)** | Fun Tic Tac Toe game equipped with multiplayer (local and online) and leveled single player available on the App Store. | `Swift` | [Website](https://ariessciences.com/highlight?product=tic-tac-toe) • [Source](https://github.com/Aries-Sciences-LLC/Tic-Tac-Toe) | `MIT` |
| <a href="https://github.com/wesnoth/wesnoth"><img src="./icons/project-icons/battle-for-wesnoth.png" width="32" height="32" alt="Battle for Wesnoth"></a> | **[Battle for Wesnoth](https://github.com/wesnoth/wesnoth)** | Turn-based tactical strategy game, featuring both single-player and online multiplayer combat. | `C++` | [Source](https://github.com/wesnoth/wesnoth) | `MIT` |
| <a href="https://github.com/alunbestor/Boxer"><img src="./icons/project-icons/boxer.png" width="32" height="32" alt="Boxer"></a> | **[Boxer](https://github.com/alunbestor/Boxer)** | The DOS game emulator that’s fit for your Mac. | `C++` | [Source](https://github.com/alunbestor/Boxer) | `MIT` |
| <a href="https://www.apple.com"><img src="./icons/project-icons/chess.svg" width="32" height="32" alt="Chess"></a> | **[Chess](https://www.apple.com)** | The chess app that comes with macOS. | `objective-c` | [Website](https://www.apple.com) • [Source](https://opensource.apple.com/source/Chess/Chess-410.4.1/) | `MIT` |
| <a href="https://github.com/dolphin-emu/dolphin"><img src="./icons/project-icons/dolphin.png" width="32" height="32" alt="Dolphin"></a> | **[Dolphin](https://github.com/dolphin-emu/dolphin)** | Powerful emulator for Nintendo GameCube and Wii games. | `C++` | [Source](https://github.com/dolphin-emu/dolphin) | `MIT` |
| <a href="https://apollozhu.github.io/Dynamic-Dark-Mode"><img src="./icons/project-icons/dynamic-dark-mode.png" width="32" height="32" alt="Dynamic Dark Mode"></a> | **[Dynamic Dark Mode](https://apollozhu.github.io/Dynamic-Dark-Mode)** | Dynamic Dark Mode is the app you are looking for to power up Dark Mode on macOS Mojave and beyond. | `Swift` | [Website](https://apollozhu.github.io/Dynamic-Dark-Mode) • [Source](https://github.com/ApolloZhu/Dynamic-Dark-Mode) | `MIT` |
| <a href="https://github.com/OpenEmu/OpenEmu"><img src="./icons/project-icons/openemu.png" width="32" height="32" alt="OpenEmu"></a> | **[OpenEmu](https://github.com/OpenEmu/OpenEmu)** | Retro video game emulation for macOS. | `Objective-C` | [Source](https://github.com/OpenEmu/OpenEmu) | `MIT` |
| <a href="https://github.com/OpenRCT2/OpenRCT2"><img src="./icons/project-icons/openrct2.png" width="32" height="32" alt="OpenRCT2"></a> | **[OpenRCT2](https://github.com/OpenRCT2/OpenRCT2)** | Re-implementation of RollerCoaster Tycoon 2. | `C++` | [Source](https://github.com/OpenRCT2/OpenRCT2) | `MIT` |
| <a href="http://sabaki.yichuanshen.de"><img src="./icons/project-icons/sabaki.png" width="32" height="32" alt="Sabaki"></a> | **[Sabaki](http://sabaki.yichuanshen.de)** | An elegant Go/Baduk/Weiqi board and SGF editor for a more civilized age. | `JavaScript` | [Website](http://sabaki.yichuanshen.de) • [Source](https://github.com/SabakiHQ/Sabaki) | `MIT` |
| <a href="https://github.com/AaronRandall/Screentendo"><img src="./icons/project-icons/screentendo.png" width="32" height="32" alt="Screentendo"></a> | **[Screentendo](https://github.com/AaronRandall/Screentendo)** | Turn your screen into a playable level of Mario. | `Objective-C` | [Source](https://github.com/AaronRandall/Screentendo) | `MIT` |
| <a href="https://github.com/daylen/stockfish-mac"><img src="./icons/project-icons/stockfish.png" width="32" height="32" alt="Stockfish"></a> | **[Stockfish](https://github.com/daylen/stockfish-mac)** | Beautiful, powerful chess application. | `C++` | [Source](https://github.com/daylen/stockfish-mac) | `MIT` |
| <a href="https://www.widelands.org"><img src="./icons/project-icons/widelands.png" width="32" height="32" alt="Widelands"></a> | **[Widelands](https://www.widelands.org)** | Widelands is a free, open source real-time strategy game with singleplayer campaigns and a multiplayer mode. The game was inspired by Settlers II™ (© Bluebyte) but has significantly more variety and depth to it. | `c++` | [Website](https://www.widelands.org) • [Source](https://github.com/widelands/widelands) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="graphics"></a>
### 🎨 Graphics

> Vector design tools, 3D rendering packages, animation software, and diagramming apps.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/aseprite/aseprite"><img src="./icons/project-icons/aseprite.png" width="32" height="32" alt="Aseprite"></a> | **[Aseprite](https://github.com/aseprite/aseprite)** | Animated sprite editor & pixel art tool (Windows, macOS, Linux). | `C++` | [Source](https://github.com/aseprite/aseprite) | `MIT` |
| <a href="https://www.blender.org"><img src="./icons/project-icons/blender.png" width="32" height="32" alt="Blender"></a> | **[Blender](https://www.blender.org)** | Open-source 3D creation suite supporting modeling, rigging, animation, simulation, and rendering with Metal. | `C++` | [Website](https://www.blender.org) • [Source](https://github.com/blender/blender) | `GPL-3.0` |
| <a href="https://github.com/sfragrance/CaptuocrToy"><img src="./icons/project-icons/captuocrtoy.png" width="32" height="32" alt="CaptuocrToy"></a> | **[CaptuocrToy](https://github.com/sfragrance/CaptuocrToy)** | Tool to capture screenshot and recognize text by online ocr apis. | `Swift` | [Source](https://github.com/sfragrance/CaptuocrToy) | `MIT` |
| <a href="https://www.freecad.org"><img src="./icons/project-icons/freecad.png" width="32" height="32" alt="FreeCAD"></a> | **[FreeCAD](https://www.freecad.org)** | FreeCAD is an open-source 3D parametric modeler | `c++` | [Website](https://www.freecad.org) • [Source](https://github.com/FreeCAD/FreeCAD) | `MIT` |
| <a href="https://gaphor.org"><img src="./icons/project-icons/gaphor.png" width="32" height="32" alt="Gaphor"></a> | **[Gaphor](https://gaphor.org)** | Gaphor is the simple modeling tool for UML and SysML. | `Python` | [Website](https://gaphor.org) • [Source](https://github.com/gaphor/gaphor) | `MIT` |
| <a href="https://github.com/onmyway133/GifCapture"><img src="./icons/project-icons/gifcapture.png" width="32" height="32" alt="GifCapture"></a> | **[GifCapture](https://github.com/onmyway133/GifCapture)** | Gif capture app for macOS. | `Swift` | [Source](https://github.com/onmyway133/GifCapture) | `MIT` |
| <a href="https://github.com/lettier/gifcurry"><img src="./icons/project-icons/gifcurry.png" width="32" height="32" alt="Gifcurry"></a> | **[Gifcurry](https://github.com/lettier/gifcurry)** | Video to GIF maker with a graphical interface capable of cropping, adding text, seeking, and trimming. | `Haskell` | [Source](https://github.com/lettier/gifcurry) | `MIT` |
| <a href="https://github.com/sindresorhus/Gifski"><img src="./icons/project-icons/gifski.png" width="32" height="32" alt="Gifski"></a> | **[Gifski](https://github.com/sindresorhus/Gifski)** | Convert videos to high-quality GIFs. | `Swift` | [Source](https://github.com/sindresorhus/Gifski) | `MIT` |
| <a href="https://www.gimp.org"><img src="./icons/project-icons/gimp.png" width="32" height="32" alt="GIMP"></a> | **[GIMP](https://www.gimp.org)** | Cross-platform image editor used for photo retouching, image composition, and graphic authoring. | `C` | [Website](https://www.gimp.org) • [Source](https://github.com/GNOME/gimp) | `GPL-3.0` |
| <a href="https://github.com/CleanCocoa/InfiniteCanvas"><img src="./icons/project-icons/infinitecanvas.png" width="32" height="32" alt="InfiniteCanvas"></a> | **[InfiniteCanvas](https://github.com/CleanCocoa/InfiniteCanvas)** | Proof of concept Mac drawing application. | `Swift` | [Source](https://github.com/CleanCocoa/InfiniteCanvas) | `MIT` |
| <a href="https://krita.org/en"><img src="./icons/project-icons/krita-2.svg" width="32" height="32" alt="Krita"></a> | **[Krita](https://krita.org/en)** | Krita is a cross-platform application for creating digital art files from scratch like illustrations, concept art, matte painting, textures, comics and animations. | `C++` | [Website](https://krita.org/en) • [Source](https://invent.kde.org/graphics/krita) | `MIT` |
| <a href="https://librecad.org"><img src="./icons/project-icons/librecad.png" width="32" height="32" alt="LibreCAD"></a> | **[LibreCAD](https://librecad.org)** | LibreCAD is a free Open Source CAD application for Windows, Apple and Linux. Support and documentation are free from our large, dedicated community of users, contributors and developers. | `c++` | [Website](https://librecad.org) • [Source](https://github.com/LibreCAD/LibreCAD) | `MIT` |
| <a href="https://github.com/dsward2/macSVG"><img src="./icons/project-icons/macsvg.png" width="32" height="32" alt="macSVG"></a> | **[macSVG](https://github.com/dsward2/macSVG)** | macOS application for designing HTML5 SVG (Scalable Vector Graphics) art and animation with a WebKit web view. | `Objective-C` | [Source](https://github.com/dsward2/macSVG) | `MIT` |
| <a href="https://github.com/BafS/Material-Colors-native"><img src="./icons/project-icons/material-colors-native.png" width="32" height="32" alt="Material Colors Native"></a> | **[Material Colors Native](https://github.com/BafS/Material-Colors-native)** | Choose your Material colours and copy the hex code. | `Objective-C` | [Source](https://github.com/BafS/Material-Colors-native) | `MIT` |
| <a href="https://github.com/cartesiancs/nugget-app"><img src="./icons/project-icons/nugget.png" width="32" height="32" alt="Nugget"></a> | **[Nugget](https://github.com/cartesiancs/nugget-app)** | Video editing software designed for motion effects and versatility. | `TypeScript` | [Source](https://github.com/cartesiancs/nugget-app) | `MIT` |
| <a href="https://github.com/pencil2d/pencil"><img src="./icons/project-icons/pencil2d-animation.png" width="32" height="32" alt="Pencil2D Animation"></a> | **[Pencil2D Animation](https://github.com/pencil2d/pencil)** | Pencil2D is an animation/drawing software for macOS, Windows, and Linux. It lets you create traditional hand-drawn animation (cartoon) using both bitmap and vector graphics. | `C++` | [Source](https://github.com/pencil2d/pencil) | `MIT` |
| <a href="https://github.com/duyquoc/ScreenToLayers"><img src="./icons/project-icons/screentolayers-for-macos.png" width="32" height="32" alt="ScreenToLayers for macOS"></a> | **[ScreenToLayers for macOS](https://github.com/duyquoc/ScreenToLayers)** | ScreenToLayers is a macOS application to easily capture your screen as a layered PSD file. | `Objective-C` | [Source](https://github.com/duyquoc/ScreenToLayers) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="ide"></a>
### 💻 IDE

> Full-fledged integrated development environments supporting multiple programming stacks.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://www.jetbrains.com/idea"><img src="./icons/project-icons/intellij-idea-community-edition.png" width="32" height="32" alt="IntelliJ IDEA Community Edition"></a> | **[IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea)** | IntelliJ IDEA is an integrated development environment written in Java for developing computer software | `Java` | [Website](https://www.jetbrains.com/idea) • [Source](https://github.com/JetBrains/intellij-community) | `MIT` |
| <a href="https://livecode.org"><img src="./icons/project-icons/livecode.png" width="32" height="32" alt="LiveCode"></a> | **[LiveCode](https://livecode.org)** | Cross-platform development IDE. | `C` | [Website](https://livecode.org) • [Source](https://github.com/livecode/livecode) | `MIT` |
| <a href="https://github.com/onivim/oni"><img src="./icons/project-icons/oni.png" width="32" height="32" alt="Oni"></a> | **[Oni](https://github.com/onivim/oni)** | Oni is a modern take on modal editing code editor focused on developer productivity. | `JavaScript` | [Source](https://github.com/onivim/oni) | `MIT` |
| <a href="https://www.vim.org"><img src="./icons/project-icons/vim.png" width="32" height="32" alt="Vim"></a> | **[Vim](https://www.vim.org)** | ubiquitous text editor | `C` | [Website](https://www.vim.org) • [Source](https://github.com/vim/vim) | `MIT` |
| <a href="https://github.com/Microsoft/vscode"><img src="./icons/project-icons/visual-studio-code.png" width="32" height="32" alt="Visual Studio Code"></a> | **[Visual Studio Code](https://github.com/Microsoft/vscode)** | Code editor developed by Microsoft. | `TypeScript` | [Source](https://github.com/Microsoft/vscode) | `MIT` |
| <a href="https://github.com/pkulchenko/ZeroBraneStudio"><img src="./icons/project-icons/zerobranestudio.png" width="32" height="32" alt="ZeroBraneStudio"></a> | **[ZeroBraneStudio](https://github.com/pkulchenko/ZeroBraneStudio)** | ZeroBrane Studio is a lightweight cross-platform Lua IDE with code completion, syntax highlighting, remote debugger, code analyzer, live coding, and debugging support for various Lua engines. | `Lua` | [Source](https://github.com/pkulchenko/ZeroBraneStudio) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="images"></a>
### 🖼️ Images

> Image viewing apps, screenshot annotation suites, image optimizers, and color managers.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/shgodoroja/APNGb"><img src="./icons/project-icons/apngb.png" width="32" height="32" alt="APNGb"></a> | **[APNGb](https://github.com/shgodoroja/APNGb)** | macOS app which assembles and disassembles animated png files. | `Swift` | [Source](https://github.com/shgodoroja/APNGb) | `MIT` |
| <a href="https://github.com/chrissimpkins/Crunch"><img src="./icons/project-icons/crunch.png" width="32" height="32" alt="Crunch"></a> | **[Crunch](https://github.com/chrissimpkins/Crunch)** | Insane(ly slow but wicked good) PNG image optimization. | `Python` | [Source](https://github.com/chrissimpkins/Crunch) | `MIT` |
| <a href="https://exifcleaner.com"><img src="./icons/project-icons/exifcleaner.png" width="32" height="32" alt="ExifCleaner"></a> | **[ExifCleaner](https://exifcleaner.com)** | Remove image metadata with drag and drop, multi-core batch processing, and dark mode. | `JavaScript` | [Website](https://exifcleaner.com) • [Source](https://github.com/szTheory/exifcleaner) | `MIT` |
| <a href="https://github.com/wddwycc/Freehand"><img src="./icons/project-icons/freehand.png" width="32" height="32" alt="Freehand"></a> | **[Freehand](https://github.com/wddwycc/Freehand)** | macOS Status Bar App for quick sketch. | `Swift` | [Source](https://github.com/wddwycc/Freehand) | `MIT` |
| <a href="https://github.com/kornelski/ImageAlpha"><img src="./icons/project-icons/imagealpha.png" width="32" height="32" alt="ImageAlpha"></a> | **[ImageAlpha](https://github.com/kornelski/ImageAlpha)** | Mac GUI for pngquant, pngnq and posterizer. | `Objective-C` | [Source](https://github.com/kornelski/ImageAlpha) | `MIT` |
| <a href="https://github.com/meowtec/Imagine"><img src="./icons/project-icons/imagine.png" width="32" height="32" alt="Imagine"></a> | **[Imagine](https://github.com/meowtec/Imagine)** | Imagine is a desktop app for compression of PNG and JPEG, with a modern and friendly UI. | `TypeScript` | [Source](https://github.com/meowtec/Imagine) | `MIT` |
| <a href="https://inkscape.org"><img src="./icons/project-icons/inkscape-2.svg" width="32" height="32" alt="Inkscape"></a> | **[Inkscape](https://inkscape.org)** | Inkscape is a Free and open source vector graphics editor. | `c++` | [Website](https://inkscape.org) • [Source](https://gitlab.com/inkscape/inkscape) | `MIT` |
| <a href="https://github.com/bluegill/katana"><img src="./icons/project-icons/katana.png" width="32" height="32" alt="Katana"></a> | **[Katana](https://github.com/bluegill/katana)** | Katana is a simple screenshot utility for macOS that lives in your menubar. | `JavaScript` | [Source](https://github.com/bluegill/katana) | `MIT` |
| <a href="https://github.com/gergelysanta/photominer"><img src="./icons/project-icons/photominer.png" width="32" height="32" alt="PhotoMiner"></a> | **[PhotoMiner](https://github.com/gergelysanta/photominer)** | macOS app for finding and lost forgotten photos on your disks. | `Swift` | [Source](https://github.com/gergelysanta/photominer) | `MIT` |
| <a href="https://github.com/crilleengvall/Screenbar"><img src="./icons/project-icons/screenbar.png" width="32" height="32" alt="Screenbar"></a> | **[Screenbar](https://github.com/crilleengvall/Screenbar)** | macOS menubar app for automating screenshots. | `Swift` | [Source](https://github.com/crilleengvall/Screenbar) | `MIT` |
| <a href="https://github.com/robaho/seashore"><img src="./icons/project-icons/seashore.png" width="32" height="32" alt="Seashore"></a> | **[Seashore](https://github.com/robaho/seashore)** | Easy to use macOS image editing application for the rest of us. | `Objective-C` | [Source](https://github.com/robaho/seashore) | `MIT` |
| <a href="https://github.com/1000ch/WebPonize"><img src="./icons/project-icons/webponize.png" width="32" height="32" alt="WebPonize"></a> | **[WebPonize](https://github.com/1000ch/WebPonize)** | WebPonize is a macOS App for converting PNG, JPEG, animated (or not) GIF images into WebP. | `Swift` | [Source](https://github.com/1000ch/WebPonize) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="keyboard"></a>
### ⌨️ Keyboard

> Key remap utilities, shortcut cheatsheets, keyboard layout managers, and typing assists.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/msvisser/AnnePro-mac"><img src="./icons/project-icons/annepro-mac.png" width="32" height="32" alt="AnnePro-mac"></a> | **[AnnePro-mac](https://github.com/msvisser/AnnePro-mac)** | macOS application for controlling AnnePro keyboard over bluetooth. | `Swift` | [Source](https://github.com/msvisser/AnnePro-mac) | `MIT` |
| <a href="https://github.com/Pyroh/Fluor"><img src="./icons/project-icons/fluor.png" width="32" height="32" alt="Fluor"></a> | **[Fluor](https://github.com/Pyroh/Fluor)** | Handy tool for macOS allowing you to switch Fn keys' mode based on active application. | `Swift` | [Source](https://github.com/Pyroh/Fluor) | `MIT` |
| <a href="https://github.com/yqrashawn/GokuRakuJoudo"><img src="./icons/project-icons/gokurakujoudo.png" width="32" height="32" alt="GokuRakuJoudo"></a> | **[GokuRakuJoudo](https://github.com/yqrashawn/GokuRakuJoudo)** | Karabiner-Elements configuration manager, rescue to bloated karabiner.json | `Clojure` | [Source](https://github.com/yqrashawn/GokuRakuJoudo) | `MIT` |
| <a href="https://github.com/tekezo/Karabiner"><img src="./icons/project-icons/karabiner.png" width="32" height="32" alt="Karabiner"></a> | **[Karabiner](https://github.com/tekezo/Karabiner)** | Karabiner (KeyRemap4MacBook) is a powerful utility for keyboard customization. | `C++` | [Source](https://github.com/tekezo/Karabiner) | `MIT` |
| <a href="https://karabiner-elements.pqrs.org"><img src="./icons/project-icons/karabiner-elements.png" width="32" height="32" alt="Karabiner-Elements"></a> | **[Karabiner-Elements](https://karabiner-elements.pqrs.org)** | Powerful and stable keyboard customizer for macOS to remap keys and create complex modification rules. | `C++` | [Website](https://karabiner-elements.pqrs.org) • [Source](https://github.com/pqrs-org/Karabiner-Elements) | `MIT` |
| <a href="https://github.com/hatashiro/kawa"><img src="./icons/project-icons/kawa.png" width="32" height="32" alt="Kawa"></a> | **[Kawa](https://github.com/hatashiro/kawa)** | Better input source switcher for macOS. | `Swift` | [Source](https://github.com/hatashiro/kawa) | `MIT` |
| <a href="https://github.com/keycastr/keycastr"><img src="./icons/project-icons/keycastr.png" width="32" height="32" alt="Keycastr"></a> | **[Keycastr](https://github.com/keycastr/keycastr)** | Keystroke visualizer. | `Objective-C` | [Source](https://github.com/keycastr/keycastr) | `MIT` |
| <a href="https://reg2005.github.io/langSwitcher"><img src="./icons/project-icons/langswitcher.png" width="32" height="32" alt="LangSwitcher"></a> | **[LangSwitcher](https://reg2005.github.io/langSwitcher)** | Open-source keyboard layout text converter for macOS. | `Swift` | [Website](https://reg2005.github.io/langSwitcher) • [Source](https://github.com/reg2005/langSwitcher) | `MIT` |
| <a href="https://sensible-side-buttons.archagon.net"><img src="./icons/project-icons/sensible-side-buttons.png" width="32" height="32" alt="SensibleSideButtons"></a> | **[SensibleSideButtons](https://sensible-side-buttons.archagon.net)** | App that lets third-party mice with side buttons navigate back and forth properly across macOS. | `Objective-C` | [Website](https://sensible-side-buttons.archagon.net) • [Source](https://github.com/archagon/sensible-side-buttons) | `GPL-3.0` |
| <a href="https://github.com/gbammc/Thor"><img src="./icons/project-icons/thor.png" width="32" height="32" alt="Thor"></a> | **[Thor](https://github.com/gbammc/Thor)** | Switch the right application ASAP. | `Swift` | [Source](https://github.com/gbammc/Thor) | `MIT` |
| <a href="https://unshaky.nestederror.com"><img src="./icons/project-icons/unshaky.png" width="32" height="32" alt="Unshaky"></a> | **[Unshaky](https://unshaky.nestederror.com)** | A software attempt to address the "double key press" issue on Apple's butterfly keyboard | `Swift` | [Website](https://unshaky.nestederror.com) • [Source](https://github.com/aahung/Unshaky) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="mail"></a>
### 📧 Mail

> Desktop email clients, menubar notification checkers, and inbox management tools.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/amitmerchant1990/correo"><img src="./icons/project-icons/correo.png" width="32" height="32" alt="Correo"></a> | **[Correo](https://github.com/amitmerchant1990/correo)** | Menubar/taskbar Gmail App for Windows and macOS. | `JavaScript` | [Source](https://github.com/amitmerchant1990/correo) | `MIT` |
| <a href="https://github.com/dinhvh/dejalu"><img src="./icons/project-icons/dejalu.png" width="32" height="32" alt="dejalu"></a> | **[dejalu](https://github.com/dinhvh/dejalu)** | Fast and Simple Email Client. | `C++` | [Source](https://github.com/dinhvh/dejalu) | `MIT` |
| <a href="https://github.com/vladimiry/ElectronMail"><img src="./icons/project-icons/electronmail.png" width="32" height="32" alt="ElectronMail"></a> | **[ElectronMail](https://github.com/vladimiry/ElectronMail)** | Unofficial desktop app for ProtonMail and Tutanota end-to-end encrypted email providers. | `TypeScript` | [Source](https://github.com/vladimiry/ElectronMail) | `MIT` |
| <a href="https://getmailspring.com"><img src="./icons/project-icons/mailspring.png" width="32" height="32" alt="Mailspring"></a> | **[Mailspring](https://getmailspring.com)** | 💌 A beautiful, fast and maintained fork of @nylas Mail by one of the original authors | `JavaScript` | [Website](https://getmailspring.com) • [Source](https://github.com/Foundry376/Mailspring) | `MIT` |
| <a href="https://github.com/ramboxapp/community-edition"><img src="./icons/project-icons/rambox.png" width="32" height="32" alt="Rambox"></a> | **[Rambox](https://github.com/ramboxapp/community-edition)** | Cross Platform messaging and emailing app that combines common web applications into one. | `JavaScript` | [Source](https://github.com/ramboxapp/community-edition) | `MIT` |
| <a href="https://github.com/simple-login/mac-app"><img src="./icons/project-icons/simplelogin.png" width="32" height="32" alt="SimpleLogin"></a> | **[SimpleLogin](https://github.com/simple-login/mac-app)** | Email Alias solution: protect your real email address. | `Swift` | [Source](https://github.com/simple-login/mac-app) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="medical"></a>
### 🏥 Medical

> DICOM viewers, medical image visualizers, and healthcare workstation applications.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/invesalius/invesalius3/"><img src="./icons/project-icons/invesalius.png" width="32" height="32" alt="InVesalius"></a> | **[InVesalius](https://github.com/invesalius/invesalius3/)** | 3D medical imaging reconstruction software | `Python` | [Source](https://github.com/invesalius/invesalius3/) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="menubar"></a>
### 📊 Menubar

> Menu bar monitors, notch managers, status bar applets, and quick-access widgets.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://yagcioglutoprak.github.io/AIQuotaBar"><img src="./icons/project-icons/aiquotabar.png" width="32" height="32" alt="AIQuotaBar"></a> | **[AIQuotaBar](https://yagcioglutoprak.github.io/AIQuotaBar)** | See your Claude.ai and ChatGPT usage limits live in your macOS menu bar. | `Python` | [Website](https://yagcioglutoprak.github.io/AIQuotaBar) • [Source](https://github.com/yagcioglutoprak/AIQuotaBar) | `MIT` |
| <a href="https://github.com/alvesjtiago/airpass"><img src="./icons/project-icons/airpass.png" width="32" height="32" alt="Airpass"></a> | **[Airpass](https://github.com/alvesjtiago/airpass)** | Status bar Mac application to overcome time constrained WiFi networks. | `JavaScript` | [Source](https://github.com/alvesjtiago/airpass) | `MIT` |
| <a href="https://github.com/jariz/Akku"><img src="./icons/project-icons/akku.png" width="32" height="32" alt="Akku"></a> | **[Akku](https://github.com/jariz/Akku)** | The missing macOS bluetooth headset battery indicator app. | `Swift` | [Source](https://github.com/jariz/Akku) | `MIT` |
| <a href="https://github.com/tonsky/AnyBar"><img src="./icons/project-icons/anybar.png" width="32" height="32" alt="AnyBar"></a> | **[AnyBar](https://github.com/tonsky/AnyBar)** | macOS menubar status indicator. | `Objective-C` | [Source](https://github.com/tonsky/AnyBar) | `MIT` |
| <a href="https://github.com/barseghyanartur/app-menu"><img src="./icons/project-icons/app-menu.png" width="32" height="32" alt="app-menu"></a> | **[app-menu](https://github.com/barseghyanartur/app-menu)** | The missing Applications Menu for macOS. | `Swift` | [Source](https://github.com/barseghyanartur/app-menu) | `MIT` |
| <a href="https://github.com/relikd/barss"><img src="./icons/project-icons/barss-menu-bar-rss-reader.png" width="32" height="32" alt="baRSS – Menu Bar RSS Reader"></a> | **[baRSS – Menu Bar RSS Reader](https://github.com/relikd/barss)** | RSS & Atom feed reader that lives in the system status bar. | `Objective-C` | [Source](https://github.com/relikd/barss) | `MIT` |
| <a href="https://thijmendam.github.io/BarTranslate"><img src="./icons/project-icons/bartranslate.png" width="32" height="32" alt="BarTranslate"></a> | **[BarTranslate](https://thijmendam.github.io/BarTranslate)** | A handy (native) menu bar translator app that supports Google Translate. | `Swift` | [Website](https://thijmendam.github.io/BarTranslate) • [Source](https://github.com/ThijmenDam/BarTranslate) | `MIT` |
| <a href="https://github.com/a692570/bolo"><img src="./icons/project-icons/bolo.png" width="32" height="32" alt="Bolo"></a> | **[Bolo](https://github.com/a692570/bolo)** | Voice dictation menubar app using Telnyx STT and LLM APIs. | `Python` | [Source](https://github.com/a692570/bolo) | `MIT` |
| <a href="https://github.com/designsbymuzeer/Bye-Mac-App"><img src="./icons/project-icons/bye-appquit.png" width="32" height="32" alt="Bye-AppQuit"></a> | **[Bye-AppQuit](https://github.com/designsbymuzeer/Bye-Mac-App)** | A minimal native macOS app to quickly view and Bulk kill running processes. | `Swift` | [Source](https://github.com/designsbymuzeer/Bye-Mac-App) | `MIT` |
| <a href="https://github.com/theDanButuc/Claude-Usage-Monitor"><img src="./icons/project-icons/claude-usage-monitor.png" width="32" height="32" alt="Claude Usage Monitor"></a> | **[Claude Usage Monitor](https://github.com/theDanButuc/Claude-Usage-Monitor)** | Native macOS menu bar app that tracks Claude.ai usage with colour-coded icons and reset timers. | `Swift` | [Source](https://github.com/theDanButuc/Claude-Usage-Monitor) | `MIT` |
| <a href="https://yagcioglutoprak.github.io/AIQuotaBar"><img src="./icons/project-icons/claudeusagebar.png" width="32" height="32" alt="ClaudeUsageBar"></a> | **[ClaudeUsageBar](https://yagcioglutoprak.github.io/AIQuotaBar)** | See your Claude.ai and ChatGPT usage limits live in your macOS menu bar. | `Python` | [Website](https://yagcioglutoprak.github.io/AIQuotaBar) • [Source](https://github.com/yagcioglutoprak/ClaudeUsageBar) | `MIT` |
| <a href="https://bysiber.github.io/cleardisk"><img src="./icons/project-icons/cleardisk.png" width="32" height="32" alt="ClearDisk"></a> | **[ClearDisk](https://bysiber.github.io/cleardisk)** | Visualize and clean developer caches to reclaim disk space on macOS. | `Swift` | [Website](https://bysiber.github.io/cleardisk) • [Source](https://github.com/bysiber/cleardisk) | `MIT` |
| <a href="https://github.com/praneeth552/clipflow"><img src="./icons/project-icons/clipflow.png" width="32" height="32" alt="ClipFlow"></a> | **[ClipFlow](https://github.com/praneeth552/clipflow)** | Clipboard history manager for macOS with terminal-style navigation, image previews, and cursor-following popup. | `Swift` | [Source](https://github.com/praneeth552/clipflow) | `MIT` |
| <a href="https://github.com/josh-/CloudyTabs"><img src="./icons/project-icons/cloudytabs.png" width="32" height="32" alt="CloudyTabs"></a> | **[CloudyTabs](https://github.com/josh-/CloudyTabs)** | Simple menu bar macOS application for displaying lists of your iCloud Tabs and Reading List. | `Objective-C` | [Source](https://github.com/josh-/CloudyTabs) | `MIT` |
| <a href="https://github.com/inderdhir/DatWeatherDoe"><img src="./icons/project-icons/datweatherdoe.png" width="32" height="32" alt="DatWeatherDoe"></a> | **[DatWeatherDoe](https://github.com/inderdhir/DatWeatherDoe)** | Simple menu bar weather app for macOS written in Swift. | `Swift` | [Source](https://github.com/inderdhir/DatWeatherDoe) | `MIT` |
| <a href="https://github.com/Kwpolska/DisplayMenu"><img src="./icons/project-icons/displaymenu.png" width="32" height="32" alt="DisplayMenu"></a> | **[DisplayMenu](https://github.com/Kwpolska/DisplayMenu)** | Simple (bare-bones) macOS menubar extra to apply display presets. | `Swift` | [Source](https://github.com/Kwpolska/DisplayMenu) | `MIT` |
| <a href="https://github.com/Mortennn/Dozer"><img src="./icons/project-icons/dozer.png" width="32" height="32" alt="Dozer"></a> | **[Dozer](https://github.com/Mortennn/Dozer)** | Hide MacOS menubar items. | `Swift` | [Source](https://github.com/Mortennn/Dozer) | `MIT` |
| <a href="https://github.com/gao-sun/eul"><img src="./icons/project-icons/eul.png" width="32" height="32" alt="eul"></a> | **[eul](https://github.com/gao-sun/eul)** | macOS status monitoring app written in SwiftUI. | `Swift` | [Source](https://github.com/gao-sun/eul) | `MIT` |
| <a href="https://github.com/rkbhochalya/grayscale-mode"><img src="./icons/project-icons/grayscale-mode.png" width="32" height="32" alt="Grayscale Mode"></a> | **[Grayscale Mode](https://github.com/rkbhochalya/grayscale-mode)** | Manage grayscale mode from menu bar. | `Swift` | [Source](https://github.com/rkbhochalya/grayscale-mode) | `MIT` |
| <a href="https://github.com/CodySchrank/gSwitch"><img src="./icons/project-icons/gswitch.png" width="32" height="32" alt="gSwitch"></a> | **[gSwitch](https://github.com/CodySchrank/gSwitch)** | macOS status bar app that allows control over the gpu on dual gpu macbooks. | `Swift` | [Source](https://github.com/CodySchrank/gSwitch) | `MIT` |
| <a href="https://github.com/iglance/iGlance"><img src="./icons/project-icons/iglance.png" width="32" height="32" alt="iGlance"></a> | **[iGlance](https://github.com/iglance/iGlance)** | macOS System Monitor (cpu, memory, network, fan and battery) for the Status Bar. | `Swift` | [Source](https://github.com/iglance/iGlance) | `MIT` |
| <a href="https://www.mowglii.com/itsycal"><img src="./icons/project-icons/itsycal.png" width="32" height="32" alt="Itsycal"></a> | **[Itsycal](https://www.mowglii.com/itsycal)** | A tiny calendar for that lives in the Mac menu bar. | `Objective-C` | [Website](https://www.mowglii.com/itsycal) • [Source](https://github.com/sfsam/Itsycal) | `MIT` |
| <a href="https://github.com/turkenh/KubeContext"><img src="./icons/project-icons/kubecontext.png" width="32" height="32" alt="KubeContext"></a> | **[KubeContext](https://github.com/turkenh/KubeContext)** | import, manage and switch between your Kubernetes contexts on Mac. | `Swift` | [Source](https://github.com/turkenh/KubeContext) | `MIT` |
| <a href="https://halo.github.io/LinkLiar"><img src="./icons/project-icons/linkliar.png" width="32" height="32" alt="LinkLiar"></a> | **[LinkLiar](https://halo.github.io/LinkLiar)** | Keep your MAC address random for privacy (intuitive GUI for ifconfig) | `Swift` | [Website](https://halo.github.io/LinkLiar) • [Source](https://github.com/halo/LinkLiar) | `MIT` |
| <a href="https://github.com/CorvidLabs/MacNTop"><img src="./icons/project-icons/macntop.png" width="32" height="32" alt="MacNTop"></a> | **[MacNTop](https://github.com/CorvidLabs/MacNTop)** | macOS menu bar system monitor with retro CRT aesthetics. | `Swift` | [Source](https://github.com/CorvidLabs/MacNTop) | `MIT` |
| <a href="https://github.com/mnndnl/market-bar"><img src="./icons/project-icons/market-bar.png" width="32" height="32" alt="Market Bar"></a> | **[Market Bar](https://github.com/mnndnl/market-bar)** | Tiny stocks watcher for the menu bar. | `Swift` | [Source](https://github.com/mnndnl/market-bar) | `MIT` |
| <a href="https://github.com/leits/MeetingBar"><img src="./icons/project-icons/meetingbar.png" width="32" height="32" alt="MeetingBar"></a> | **[MeetingBar](https://github.com/leits/MeetingBar)** | Menu bar app for your calendar meetings | `Swift` | [Source](https://github.com/leits/MeetingBar) | `MIT` |
| <a href="https://github.com/lucasbento/menubar-brightness"><img src="./icons/project-icons/menubar-brightness.png" width="32" height="32" alt="Menubar Brightness"></a> | **[Menubar Brightness](https://github.com/lucasbento/menubar-brightness)** | macOS app to change the screen brightness on the menubar. | `JavaScript` | [Source](https://github.com/lucasbento/menubar-brightness) | `MIT` |
| <a href="https://github.com/yujitach/MenuMeters"><img src="./icons/project-icons/menumeters.png" width="32" height="32" alt="MenuMeters"></a> | **[MenuMeters](https://github.com/yujitach/MenuMeters)** | CPU, memory, disk, and network monitoring tools for macOS. | `Objective-C` | [Source](https://github.com/yujitach/MenuMeters) | `MIT` |
| <a href="https://www.minisim.app"><img src="./icons/project-icons/minisim.png" width="32" height="32" alt="MiniSim"></a> | **[MiniSim](https://www.minisim.app)** | MacOS menu bar app for launching iOS  and Android 🤖 emulators. | `Swift` | [Website](https://www.minisim.app) • [Source](https://github.com/okwasniewski/MiniSim) | `MIT` |
| <a href="https://github.com/tidiemme/monitorbar"><img src="./icons/project-icons/monitor-bar.png" width="32" height="32" alt="Monitor Bar"></a> | **[Monitor Bar](https://github.com/tidiemme/monitorbar)** | Monitor Bar app supports three modes, compact, normal, extra. It monitors battery, Disk, Memory, CPU, Network bandwidth, Wi-Fi. | `Swift` | [Source](https://github.com/tidiemme/monitorbar) | `MIT` |
| <a href="https://github.com/isaiasmatewos/night-shift-control"><img src="./icons/project-icons/night-shift-control.png" width="32" height="32" alt="Night Shift Control"></a> | **[Night Shift Control](https://github.com/isaiasmatewos/night-shift-control)** | Night Shift Control is a simple macOS menubar app for controlling Night Shift. It's aim is to bring features from f.lux which are missing from Night Shift such as disabling Night Shift for certain apps. | `Swift` | [Source](https://github.com/isaiasmatewos/night-shift-control) | `MIT` |
| <a href="https://github.com/joshjon/nocturnal"><img src="./icons/project-icons/nocturnal.png" width="32" height="32" alt="Nocturnal"></a> | **[Nocturnal](https://github.com/joshjon/nocturnal)** | Menu bar app featuring darker than dark dimming, Night Shift fine tuning, and the ability to turn off TouchBar on MacBook Pro. | `Swift` | [Source](https://github.com/joshjon/nocturnal) | `MIT` |
| <a href="https://github.com/deepshal99/notch-so-good"><img src="./icons/project-icons/notch-so-good.png" width="32" height="32" alt="Notch So Good"></a> | **[Notch So Good](https://github.com/deepshal99/notch-so-good)** | A pixel-art crab lives in your MacBook notch and monitors Claude Code sessions with 13 animations, smart notifications, and multi-session support. | `Swift` | [Source](https://github.com/deepshal99/notch-so-good) | `MIT` |
| <a href="https://www.jacklandrin.com/2021/12/01/onlyswitch"><img src="./icons/project-icons/onlyswitch.png" width="32" height="32" alt="OnlySwitch"></a> | **[OnlySwitch](https://www.jacklandrin.com/2021/12/01/onlyswitch)** | All-in-One status bar button, hide MacBook Pro's notch, dark mode, AirPods, Shortcuts | `Swift` | [Website](https://www.jacklandrin.com/2021/12/01/onlyswitch) • [Source](https://github.com/jacklandrin/OnlySwitch) | `MIT` |
| <a href="https://paretosecurity.com"><img src="./icons/project-icons/pareto-security.png" width="32" height="32" alt="Pareto Security"></a> | **[Pareto Security](https://paretosecurity.com)** | A MenuBar app to automatically audit your Mac for basic security hygiene. | `Swift` | [Website](https://paretosecurity.com) • [Source](https://github.com/paretoSecurity/pareto-mac/) | `MIT` |
| <a href="https://github.com/Bunn/PiStats"><img src="./icons/project-icons/pi-stats.png" width="32" height="32" alt="Pi Stats"></a> | **[Pi Stats](https://github.com/Bunn/PiStats)** | macOS app to visualize Pi-hole information. | `Swift` | [Source](https://github.com/Bunn/PiStats) | `MIT` |
| <a href="https://superhighfives.com/pika"><img src="./icons/project-icons/pika.png" width="32" height="32" alt="Pika"></a> | **[Pika](https://superhighfives.com/pika)** | Is an easy to use, open-source, native colour picker for macOS. | `Swift` | [Website](https://superhighfives.com/pika) • [Source](https://github.com/superhighfives/pika) | `MIT` |
| <a href="https://github.com/nikhilsh/PSIBar"><img src="./icons/project-icons/psibar.png" width="32" height="32" alt="PSIBar"></a> | **[PSIBar](https://github.com/nikhilsh/PSIBar)** | Quickly hacked up PSI macOS status bar app. | `Swift` | [Source](https://github.com/nikhilsh/PSIBar) | `MIT` |
| <a href="https://ariessciences.com/highlight?product=quick-weather"><img src="./icons/project-icons/quick-weather.svg" width="32" height="32" alt="Quick Weather"></a> | **[Quick Weather](https://ariessciences.com/highlight?product=quick-weather)** | Simple and elegant menubar weather app on the App Store. | `Swift` | [Website](https://ariessciences.com/highlight?product=quick-weather) • [Source](https://github.com/Aries-Sciences-LLC/Quick-Weather) | `MIT` |
| <a href="https://github.com/alexrosenfeld10/Quickeys"><img src="./icons/project-icons/quickeys.png" width="32" height="32" alt="Quickeys"></a> | **[Quickeys](https://github.com/alexrosenfeld10/Quickeys)** | A mac menu bar app that provides note taking functionality though a quick dropdown menu. | `Swift` | [Source](https://github.com/alexrosenfeld10/Quickeys) | `MIT` |
| <a href="https://r2drop.com"><img src="./icons/project-icons/r2drop.png" width="32" height="32" alt="R2Drop"></a> | **[R2Drop](https://r2drop.com)** | Native macOS menu bar application for uploading files to Cloudflare R2 storage. | `Swift` | [Website](https://r2drop.com) • [Source](https://github.com/superhumancorp/r2drop) | `MIT` |
| <a href="https://rustcast.umangsurana.com"><img src="./icons/project-icons/rustcast.png" width="32" height="32" alt="RustCast"></a> | **[RustCast](https://rustcast.umangsurana.com)** | Blazingly fast, customisable multi tool, application launcher | `Rust` | [Website](https://rustcast.umangsurana.com) • [Source](https://github.com/unsecretised/rustcast) | `MIT` |
| <a href="https://sanebar.com"><img src="./icons/project-icons/sanebar.png" width="32" height="32" alt="SaneBar"></a> | **[SaneBar](https://sanebar.com)** | Privacy-first menu bar manager with Touch ID lock, Always-Hidden Zone, and automation triggers. | `Swift` | [Website](https://sanebar.com) • [Source](https://github.com/sane-apps/SaneBar) | `MIT` |
| <a href="https://screenhint.com"><img src="./icons/project-icons/screenhint.png" width="32" height="32" alt="ScreenHint"></a> | **[ScreenHint](https://screenhint.com)** | A simple screenshotting utility for thinking clearly. | `Swift` | [Website](https://screenhint.com) • [Source](https://github.com/salemhilal/ScreenHint) | `MIT` |
| <a href="https://github.com/thompsonate/Shifty"><img src="./icons/project-icons/shifty.png" width="32" height="32" alt="Shifty"></a> | **[Shifty](https://github.com/thompsonate/Shifty)** | macOS menu bar app that gives you more control over Night Shift. | `Swift` | [Source](https://github.com/thompsonate/Shifty) | `MIT` |
| <a href="https://felixkratz.github.io/SketchyBar"><img src="./icons/project-icons/sketchybar.png" width="32" height="32" alt="SketchyBar"></a> | **[SketchyBar](https://felixkratz.github.io/SketchyBar)** | Highly customizable macOS status bar replacement with event-driven shell scripts. | `C` | [Website](https://felixkratz.github.io/SketchyBar) • [Source](https://github.com/FelixKratz/SketchyBar) | `GPL-3.0` |
| <a href="https://github.com/AlexPerathoner/SlimHUD"><img src="./icons/project-icons/slimhud-cyanocitta.png" width="32" height="32" alt="SlimHUD - Cyanocitta"></a> | **[SlimHUD - Cyanocitta](https://github.com/AlexPerathoner/SlimHUD)** | Replacement for MacOS' volume, brightness and keyboard backlight HUDs. | `Swift` | [Source](https://github.com/AlexPerathoner/SlimHUD) | `MIT` |
| <a href="https://swiftbar.app"><img src="./icons/project-icons/swiftbar.png" width="32" height="32" alt="SwiftBar"></a> | **[SwiftBar](https://swiftbar.app)** | Powerful macOS menu bar customization tool. | `Swift` | [Website](https://swiftbar.app) • [Source](https://github.com/swiftbar/SwiftBar) | `MIT` |
| <a href="https://timescribe.app"><img src="./icons/project-icons/timescribe.png" width="32" height="32" alt="TimeScribe"></a> | **[TimeScribe](https://timescribe.app)** | Simple and free working time recording. | `CSS` | [Website](https://timescribe.app) • [Source](https://github.com/WINBIGFOX/timescribe) | `MIT` |
| <a href="https://vercel-deployment-menu-bar.vercel.app"><img src="./icons/project-icons/vercel-deployment-menu-bar.png" width="32" height="32" alt="Vercel Deployment Menu Bar"></a> | **[Vercel Deployment Menu Bar](https://vercel-deployment-menu-bar.vercel.app)** | Open-source macOS menu bar app to monitor Vercel deployment status in real time. | `Swift` | [Website](https://vercel-deployment-menu-bar.vercel.app) • [Source](https://github.com/andrewk17/vercel-deployment-menu-bar) | `MIT` |
| <a href="https://github.com/GeiserX/VPN-Bypass"><img src="./icons/project-icons/vpn-bypass.png" width="32" height="32" alt="VPN Bypass"></a> | **[VPN Bypass](https://github.com/GeiserX/VPN-Bypass)** | Route specific domains and services around your corporate VPN while keeping the rest of your traffic protected. | `Swift` | [Source](https://github.com/GeiserX/VPN-Bypass) | `MIT` |
| <a href="https://github.com/matryer/xbar"><img src="./icons/project-icons/xbar.png" width="32" height="32" alt="xbar"></a> | **[xbar](https://github.com/matryer/xbar)** | Put the output from any script or program into your macOS Menu Bar. | `Objective-C` | [Source](https://github.com/matryer/xbar) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="music"></a>
### 🎧 Music

> Music players, lyrics synchronizers, audio taggers, and streaming service desktop clients.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/AnaghSharma/Carol"><img src="./icons/project-icons/carol.png" width="32" height="32" alt="Carol"></a> | **[Carol](https://github.com/AnaghSharma/Carol)** | A minimal and beautiful lyrics app that stays in the menu bar of macOS. | `C#` | [Source](https://github.com/AnaghSharma/Carol) | `MIT` |
| <a href="https://github.com/cemolcay/ChordDetector"><img src="./icons/project-icons/chorddetector.png" width="32" height="32" alt="ChordDetector"></a> | **[ChordDetector](https://github.com/cemolcay/ChordDetector)** | Tiny menu bar app that listens iTunes and Spotify to detect chords of songs! | `Swift` | [Source](https://github.com/cemolcay/ChordDetector) | `MIT` |
| <a href="https://github.com/imanel/deezplayer"><img src="./icons/project-icons/deezplayer.png" width="32" height="32" alt="DeezPlayer"></a> | **[DeezPlayer](https://github.com/imanel/deezplayer)** | Deezer Desktop app for Windows, Linux and macOS. | `CoffeeScript` | [Source](https://github.com/imanel/deezplayer) | `MIT` |
| <a href="https://github.com/Zac-Garby/iTunes-Graphs"><img src="./icons/project-icons/itunes-graphs.png" width="32" height="32" alt="iTunes Graphs"></a> | **[iTunes Graphs](https://github.com/Zac-Garby/iTunes-Graphs)** | macOS app to visualise your iTunes library as graphs. | `Swift` | [Source](https://github.com/Zac-Garby/iTunes-Graphs) | `MIT` |
| <a href="https://github.com/doches/lilypond-ui"><img src="./icons/project-icons/lilypond-ui.png" width="32" height="32" alt="Lilypond UI"></a> | **[Lilypond UI](https://github.com/doches/lilypond-ui)** | Create beautiful musical scores with LilyPond. | `JavaScript` | [Source](https://github.com/doches/lilypond-ui) | `MIT` |
| <a href="https://github.com/mamal72/lyricsify-mac"><img src="./icons/project-icons/lyricsify.png" width="32" height="32" alt="lyricsify"></a> | **[lyricsify](https://github.com/mamal72/lyricsify-mac)** | Simple Spotify lyrics viewer menu bar app for macOS in Swift. | `Swift` | [Source](https://github.com/mamal72/lyricsify-mac) | `MIT` |
| <a href="https://github.com/salomvary/soundcleod"><img src="./icons/project-icons/soundcleod.png" width="32" height="32" alt="SoundCleod"></a> | **[SoundCleod](https://github.com/salomvary/soundcleod)** | SoundCloud for macOS and Windows. | `JavaScript` | [Source](https://github.com/salomvary/soundcleod) | `MIT` |
| <a href="https://spicetify.app"><img src="./icons/project-icons/spicetify-cli.png" width="32" height="32" alt="spicetify-cli"></a> | **[spicetify-cli](https://spicetify.app)** | Command-line tool to customize the official Spotify client. Supports Windows, MacOS and Linux. | `JavaScript` | [Website](https://spicetify.app) • [Source](https://github.com/spicetify/spicetify-cli) | `MIT` |
| <a href="https://github.com/ersel/spotify-cli-mac"><img src="./icons/project-icons/spotify-cli-mac.png" width="32" height="32" alt="Spotify-Cli-Mac"></a> | **[Spotify-Cli-Mac](https://github.com/ersel/spotify-cli-mac)** | Control Spotify without leaving your terminal. 🎶 | `JavaScript` | [Source](https://github.com/ersel/spotify-cli-mac) | `MIT` |
| <a href="https://github.com/steve228uk/YouTube-Music"><img src="./icons/project-icons/youtube-music.png" width="32" height="32" alt="YouTube-Music"></a> | **[YouTube-Music](https://github.com/steve228uk/YouTube-Music)** | macOS wrapper for music.youtube.com. | `Swift` | [Source](https://github.com/steve228uk/YouTube-Music) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="news"></a>
### 📰 News

> RSS and Atom feed readers, news aggregators, and headline notification monitors.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/ngquerol/Diurna"><img src="./icons/project-icons/diurna.png" width="32" height="32" alt="Diurna"></a> | **[Diurna](https://github.com/ngquerol/Diurna)** | Basic/Classic Hacker News app, used as a Cocoa & Swift learning platform. | `Swift` | [Source](https://github.com/ngquerol/Diurna) | `MIT` |
| <a href="https://github.com/owenthereal/hacker-menu"><img src="./icons/project-icons/hacker-menu.png" width="32" height="32" alt="hacker-menu"></a> | **[hacker-menu](https://github.com/owenthereal/hacker-menu)** | Hacker News Delivered to Desktop. | `JavaScript` | [Source](https://github.com/owenthereal/hacker-menu) | `MIT` |
| <a href="https://github.com/Ranchero-Software/NetNewsWire"><img src="./icons/project-icons/netnewswire.png" width="32" height="32" alt="NetNewsWire"></a> | **[NetNewsWire](https://github.com/Ranchero-Software/NetNewsWire)** | Feed reader for macOS. | `Swift` | [Source](https://github.com/Ranchero-Software/NetNewsWire) | `MIT` |
| <a href="https://github.com/ViennaRSS/vienna-rss"><img src="./icons/project-icons/vienna.png" width="32" height="32" alt="Vienna"></a> | **[Vienna](https://github.com/ViennaRSS/vienna-rss)** | Vienna is a RSS/Atom newsreader for macOS. | `Objective-C` | [Source](https://github.com/ViennaRSS/vienna-rss) | `MIT` |
| <a href="https://getstream.io/winds"><img src="./icons/project-icons/winds.png" width="32" height="32" alt="Winds"></a> | **[Winds](https://getstream.io/winds)** | A Beautiful Open Source RSS & Podcast App Powered by Getstream.io | `JavaScript` | [Website](https://getstream.io/winds) • [Source](https://github.com/GetStream/Winds) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="notes"></a>
### 📔 Notes

> Note-taking applications, personal knowledge bases, digital journals, and thought planners.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://appflowy.io"><img src="./icons/project-icons/appflowy.png" width="32" height="32" alt="AppFlowy"></a> | **[AppFlowy](https://appflowy.io)** | Open-source alternative to Notion, built with Flutter and Rust for offline-first privacy. | `Dart` | [Website](https://appflowy.io) • [Source](https://github.com/AppFlowy-IO/AppFlowy) | `AGPL-3.0` |
| <a href="https://github.com/BoostIO/BoostNote-Legacy"><img src="./icons/project-icons/boostnote.png" width="32" height="32" alt="Boostnote"></a> | **[Boostnote](https://github.com/BoostIO/BoostNote-Legacy)** | Note-taking application made for programmers just like you. | `JavaScript` | [Source](https://github.com/BoostIO/BoostNote-Legacy) | `MIT` |
| <a href="https://www.getdnote.com"><img src="./icons/project-icons/dnote.png" width="32" height="32" alt="Dnote"></a> | **[Dnote](https://www.getdnote.com)** | A simple command line notebook with multi-device sync and web interface. | `Go` | [Website](https://www.getdnote.com) • [Source](https://github.com/dnote/dnote) | `MIT` |
| <a href="https://github.com/Kilian/fromscratch"><img src="./icons/project-icons/fromscratch.png" width="32" height="32" alt="FromScratch"></a> | **[FromScratch](https://github.com/Kilian/fromscratch)** | Little app that you can use as a quick note taking or todo app. | `JavaScript` | [Source](https://github.com/Kilian/fromscratch) | `MIT` |
| <a href="https://github.com/glushchenko/fsnotes"><img src="./icons/project-icons/fsnotes.png" width="32" height="32" alt="FSNotes"></a> | **[FSNotes](https://github.com/glushchenko/fsnotes)** | Notes manager for macOS/iOS: modern notational velocity (nvALT) on steroids. | `Swift` | [Source](https://github.com/glushchenko/fsnotes) | `MIT` |
| <a href="https://joplinapp.org"><img src="./icons/project-icons/joplin.png" width="32" height="32" alt="Joplin"></a> | **[Joplin](https://joplinapp.org)** | Secure, open-source note-taking app with end-to-end encryption and multi-device synchronization. | `TypeScript` | [Website](https://joplinapp.org) • [Source](https://github.com/laurent22/joplin) | `AGPL-3.0` |
| <a href="https://github.com/tuxu/nbviewer-app"><img src="./icons/project-icons/jupyter-notebook-viewer.png" width="32" height="32" alt="Jupyter Notebook Viewer"></a> | **[Jupyter Notebook Viewer](https://github.com/tuxu/nbviewer-app)** | Notebook viewer for macOS. | `Swift` | [Source](https://github.com/tuxu/nbviewer-app) | `MIT` |
| <a href="https://logseq.com"><img src="./icons/project-icons/logseq.png" width="32" height="32" alt="Logseq"></a> | **[Logseq](https://logseq.com)** | Privacy-first, local-only platform for knowledge management and outliner journaling. | `Clojure` | [Website](https://logseq.com) • [Source](https://github.com/logseq/logseq) | `AGPL-3.0` |
| <a href="https://github.com/marktext/marktext"><img src="./icons/project-icons/marktext.png" width="32" height="32" alt="MarkText"></a> | **[MarkText](https://github.com/marktext/marktext)** | Simple and elegant open-source markdown editor focused on speed and real-time live preview. | `JavaScript` | [Source](https://github.com/marktext/marktext) | `MIT` |
| <a href="https://github.com/jmcfarlane/notable"><img src="./icons/project-icons/notable.png" width="32" height="32" alt="notable"></a> | **[notable](https://github.com/jmcfarlane/notable)** | Simple note taking application. | `JavaScript` | [Source](https://github.com/jmcfarlane/notable) | `MIT` |
| <a href="https://github.com/SauvageP/Notes"><img src="./icons/project-icons/notes.png" width="32" height="32" alt="Notes"></a> | **[Notes](https://github.com/SauvageP/Notes)** | Notes is a macOS application built to create notes, using text amongst other formats: images, videos, contacts, and etc. | `Swift` | [Source](https://github.com/SauvageP/Notes) | `MIT` |
| <a href="https://github.com/insidegui/NoteTaker"><img src="./icons/project-icons/notetaker.png" width="32" height="32" alt="NoteTaker"></a> | **[NoteTaker](https://github.com/insidegui/NoteTaker)** | Simple note taking app for macOS and iOS which uses Realm and CloudKit for syncing. | `Swift` | [Source](https://github.com/insidegui/NoteTaker) | `MIT` |
| <a href="https://github.com/Automattic/simplenote-macos"><img src="./icons/project-icons/simplenote.png" width="32" height="32" alt="Simplenote"></a> | **[Simplenote](https://github.com/Automattic/simplenote-macos)** | Simplest way to keep notes. | `Objective-C` | [Source](https://github.com/Automattic/simplenote-macos) | `MIT` |
| <a href="https://github.com/standardnotes/app"><img src="./icons/project-icons/standard-notes.png" width="32" height="32" alt="Standard Notes"></a> | **[Standard Notes](https://github.com/standardnotes/app)** | Safe place for your notes, thoughts, and life's work. | `JavaScript` | [Source](https://github.com/standardnotes/app) | `MIT` |
| <a href="https://stik.ink"><img src="./icons/project-icons/stik.png" width="32" height="32" alt="Stik"></a> | **[Stik](https://stik.ink)** | Instant thought capture for macOS. Global hotkey summons a post-it note, type and close. Notes stored as plain markdown files. | `Rust` | [Website](https://stik.ink) • [Source](https://github.com/0xMassi/stik_app) | `MIT` |
| <a href="https://github.com/buddax2/tmpNote"><img src="./icons/project-icons/tmpnote.png" width="32" height="32" alt="tmpNote"></a> | **[tmpNote](https://github.com/buddax2/tmpNote)** | Very simple macOS app to make temporary notes. | `Swift` | [Source](https://github.com/buddax2/tmpNote) | `MIT` |
| <a href="https://github.com/klaudiosinani/tusk"><img src="./icons/project-icons/tusk.png" width="32" height="32" alt="Tusk"></a> | **[Tusk](https://github.com/klaudiosinani/tusk)** | Unofficial, third-party, community driven Evernote app with a handful of useful features. | `JavaScript` | [Source](https://github.com/klaudiosinani/tusk) | `MIT` |
| <a href="https://zettlr.com"><img src="./icons/project-icons/zettlr.png" width="32" height="32" alt="Zettlr"></a> | **[Zettlr](https://zettlr.com)** | Supercharged markdown editor tailored for academic researchers, journalists, and writers. | `TypeScript` | [Website](https://zettlr.com) • [Source](https://github.com/Zettlr/Zettlr) | `GPL-3.0` |

[⬆ Back to Top](#table-of-contents)


<a id="other"></a>
### 📦 Other

> Curated collection of unique, miscellaneous, and versatile macOS tools and utilities.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://betaflight.com"><img src="./icons/project-icons/betaflight-configurator.png" width="32" height="32" alt="Betaflight Configurator"></a> | **[Betaflight Configurator](https://betaflight.com)** | Cross platform configuration tool for the Betaflight firmware. | `JavaScript` | [Website](https://betaflight.com) • [Source](https://github.com/betaflight/betaflight-configurator) | `MIT` |
| <a href="https://github.com/brunophilipe/Cakebrew"><img src="./icons/project-icons/cakebrew.png" width="32" height="32" alt="Cakebrew"></a> | **[Cakebrew](https://github.com/brunophilipe/Cakebrew)** | Manage your Homebrew formulas with style using Cakebrew. | `Objective-C` | [Source](https://github.com/brunophilipe/Cakebrew) | `MIT` |
| <a href="https://github.com/esrlabs/chipmunk"><img src="./icons/project-icons/chipmunk.png" width="32" height="32" alt="ChipMunk"></a> | **[ChipMunk](https://github.com/esrlabs/chipmunk)** | High-performance log analysis and visual log inspection tool for macOS | `TypeScript` | [Source](https://github.com/esrlabs/chipmunk) | `MIT` |
| <a href="https://github.com/dteoh/devdocs-macos"><img src="./icons/project-icons/devdocs-for-macos.png" width="32" height="32" alt="DevDocs for macOS"></a> | **[DevDocs for macOS](https://github.com/dteoh/devdocs-macos)** | An unofficial DevDocs API documentation viewer. | `Swift` | [Source](https://github.com/dteoh/devdocs-macos) | `MIT` |
| <a href="https://github.com/2ndalpha/gasmask"><img src="./icons/project-icons/gas-mask.png" width="32" height="32" alt="Gas Mask"></a> | **[Gas Mask](https://github.com/2ndalpha/gasmask)** | Hosts file manager for macOS. | `Objective-C` | [Source](https://github.com/2ndalpha/gasmask) | `MIT` |
| <a href="https://gramps-project.org"><img src="./icons/project-icons/gramps.png" width="32" height="32" alt="Gramps"></a> | **[Gramps](https://gramps-project.org)** | A genealogy program that is both intuitive for hobbyists and feature-complete for professional genealogists. | `Python` | [Website](https://gramps-project.org) • [Source](https://github.com/gramps-project/gramps) | `MIT` |
| <a href="https://github.com/specialunderwear/Hosts.prefpane"><img src="./icons/project-icons/hosts.png" width="32" height="32" alt="Hosts"></a> | **[Hosts](https://github.com/specialunderwear/Hosts.prefpane)** | Cocoa GUI for /etc/hosts. | `Objective-C` | [Source](https://github.com/specialunderwear/Hosts.prefpane) | `MIT` |
| <a href="https://github.com/ImageOptim/ImageOptim"><img src="./icons/project-icons/imageoptim.png" width="32" height="32" alt="ImageOptim"></a> | **[ImageOptim](https://github.com/ImageOptim/ImageOptim)** | GUI image optimizer for Mac. | `Objective-C` | [Source](https://github.com/ImageOptim/ImageOptim) | `MIT` |
| <a href="https://github.com/insidegui/KeyframesPlayer"><img src="./icons/project-icons/keyframes-player.png" width="32" height="32" alt="Keyframes Player"></a> | **[Keyframes Player](https://github.com/insidegui/KeyframesPlayer)** | Simple macOS app to preview animations created with Facebook's keyframes framework. | `Swift` | [Source](https://github.com/insidegui/KeyframesPlayer) | `MIT` |
| <a href="https://github.com/hackjutsu/Lepton"><img src="./icons/project-icons/lepton.png" width="32" height="32" alt="Lepton"></a> | **[Lepton](https://github.com/hackjutsu/Lepton)** | Democratizing Code Snippets Management (macOS/Win/Linux). | `JavaScript` | [Source](https://github.com/hackjutsu/Lepton) | `MIT` |
| <a href="https://github.com/klaaspieter/letters"><img src="./icons/project-icons/letters.png" width="32" height="32" alt="Letters"></a> | **[Letters](https://github.com/klaaspieter/letters)** | Teach your kids the alphabet and how to type. | `Swift` | [Source](https://github.com/klaaspieter/letters) | `MIT` |
| <a href="https://github.com/Bunn/macGist"><img src="./icons/project-icons/macgist.png" width="32" height="32" alt="macGist"></a> | **[macGist](https://github.com/Bunn/macGist)** | Simple app to send pasteboard items to GitHub's Gist. | `Swift` | [Source](https://github.com/Bunn/macGist) | `MIT` |
| <a href="https://numi.app"><img src="./icons/project-icons/numi.png" width="32" height="32" alt="Numi"></a> | **[Numi](https://numi.app)** | Beautiful calculator app for macOS | `JavaScript` | [Website](https://numi.app) • [Source](https://github.com/nikolaeu/numi) | `MIT` |
| <a href="https://github.com/sveinbjornt/Platypus"><img src="./icons/project-icons/platypus.png" width="32" height="32" alt="Platypus"></a> | **[Platypus](https://github.com/sveinbjornt/Platypus)** | Mac developer tool that creates application bundles from command line scripts. | `Objective-C` | [Source](https://github.com/sveinbjornt/Platypus) | `MIT` |
| <a href="https://github.com/Esqarrouth/QorumLogs"><img src="./icons/project-icons/qorumlogs.svg" width="32" height="32" alt="QorumLogs"></a> | **[QorumLogs](https://github.com/Esqarrouth/QorumLogs)** | Swift Logging Utility for Xcode & Google Docs. | `Swift` | [Source](https://github.com/Esqarrouth/QorumLogs) | `MIT` |
| <a href="https://github.com/jhen0409/react-native-debugger"><img src="./icons/project-icons/react-native-debugger.png" width="32" height="32" alt="React Native Debugger"></a> | **[React Native Debugger](https://github.com/jhen0409/react-native-debugger)** | Desktop app for inspecting your React Native projects. macOS, Linux, and Windows. | `JavaScript` | [Source](https://github.com/jhen0409/react-native-debugger) | `MIT` |
| <a href="https://github.com/infinitered/reactotron"><img src="./icons/project-icons/reactotron.png" width="32" height="32" alt="Reactotron"></a> | **[Reactotron](https://github.com/infinitered/reactotron)** | Desktop app for inspecting your React JS and React Native projects. macOS, Linux, and Windows. | `JavaScript` | [Source](https://github.com/infinitered/reactotron) | `MIT` |
| <a href="https://github.com/woofwoofinc/rktmachine"><img src="./icons/project-icons/rktmachine.png" width="32" height="32" alt="RktMachine"></a> | **[RktMachine](https://github.com/woofwoofinc/rktmachine)** | Menu bar macOS app for running rkt in a macOS hypervisor CoreOS VM. | `Swift` | [Source](https://github.com/woofwoofinc/rktmachine) | `MIT` |
| <a href="https://github.com/gosu/ruby-app"><img src="./icons/project-icons/ruby-app.png" width="32" height="32" alt="Ruby.app"></a> | **[Ruby.app](https://github.com/gosu/ruby-app)** | macOS app that contains a full Ruby installation (for use with Ruby/Gosu). | `Ruby` | [Source](https://github.com/gosu/ruby-app) | `MIT` |
| <a href="https://github.com/fitztrev/shuttle"><img src="./icons/project-icons/shuttle.png" width="32" height="32" alt="Shuttle"></a> | **[Shuttle](https://github.com/fitztrev/shuttle)** | Simple SSH shortcut menu for macOS. | `Objective-C` | [Source](https://github.com/fitztrev/shuttle) | `MIT` |
| <a href="https://github.com/SwiftyBeaver/SwiftyBeaver"><img src="./icons/project-icons/swiftybeaver.png" width="32" height="32" alt="SwiftyBeaver"></a> | **[SwiftyBeaver](https://github.com/SwiftyBeaver/SwiftyBeaver)** | Convenient logging during development & release in Swift. | `Swift` | [Source](https://github.com/SwiftyBeaver/SwiftyBeaver) | `MIT` |
| <a href="https://github.com/s00d/switchshuttle"><img src="./icons/project-icons/switchshuttle.png" width="32" height="32" alt="SwitchShuttle"></a> | **[SwitchShuttle](https://github.com/s00d/switchshuttle)** | Simple commands shortcut menu for macOS. | `Rust` | [Source](https://github.com/s00d/switchshuttle) | `MIT` |
| <a href="https://github.com/jeffhodnett/Unused"><img src="./icons/project-icons/unused.png" width="32" height="32" alt="Unused"></a> | **[Unused](https://github.com/jeffhodnett/Unused)** | Mac app for checking Xcode projects for unused resources. | `Objective-C` | [Source](https://github.com/jeffhodnett/Unused) | `MIT` |
| <a href="https://github.com/lanayotech/vagrant-manager"><img src="./icons/project-icons/vagrant-manager.png" width="32" height="32" alt="Vagrant Manager"></a> | **[Vagrant Manager](https://github.com/lanayotech/vagrant-manager)** | Manage your vagrant machines in one place with Vagrant Manager for macOS. | `Objective-C` | [Source](https://github.com/lanayotech/vagrant-manager) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="player"></a>
### ▶️ Player

> Dedicated lightweight audio and media playback applications for macOS.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/emoRaivis/MacMorpheus"><img src="./icons/project-icons/macmorpheus.png" width="32" height="32" alt="MacMorpheus"></a> | **[MacMorpheus](https://github.com/emoRaivis/MacMorpheus)** | 3D 180/360 video player for macOS for PSVR with head tracking. | `Objective-C` | [Source](https://github.com/emoRaivis/MacMorpheus) | `MIT` |
| <a href="https://github.com/lettier/movie-monad"><img src="./icons/project-icons/movie-monad.png" width="32" height="32" alt="Movie Monad"></a> | **[Movie Monad](https://github.com/lettier/movie-monad)** | Desktop video player built with Haskell that uses GStreamer and GTK+. | `Haskell` | [Source](https://github.com/lettier/movie-monad) | `MIT` |
| <a href="https://github.com/niltsh/MPlayerX"><img src="./icons/project-icons/mplayerx.png" width="32" height="32" alt="MPlayerX"></a> | **[MPlayerX](https://github.com/niltsh/MPlayerX)** | Media player on macOS. | `Objective-C` | [Source](https://github.com/niltsh/MPlayerX) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="podcast"></a>
### 🎙️ Podcast

> Podcast players, chapter indexers, episode downloaders, and RSS audio subscriptions.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/z-------------/CPod"><img src="./icons/project-icons/cumulonimbus.png" width="32" height="32" alt="Cumulonimbus"></a> | **[Cumulonimbus](https://github.com/z-------------/CPod)** | Simple, beautiful podcast app. | `JavaScript` | [Source](https://github.com/z-------------/CPod) | `MIT` |
| <a href="https://github.com/dyerc/Doughnut"><img src="./icons/project-icons/doughnut.png" width="32" height="32" alt="Doughnut"></a> | **[Doughnut](https://github.com/dyerc/Doughnut)** | Podcast player and library for mac | `Swift` | [Source](https://github.com/dyerc/Doughnut) | `MIT` |
| <a href="https://gpodder.github.io"><img src="./icons/project-icons/gpodder.png" width="32" height="32" alt="gPodder"></a> | **[gPodder](https://gpodder.github.io)** | gPodder is a simple, open source podcast client. | `Python` | [Website](https://gpodder.github.io) • [Source](https://github.com/gpodder/gpodder) | `MIT` |
| <a href="https://github.com/muammar/mkchromecast"><img src="./icons/project-icons/mkchromecast.png" width="32" height="32" alt="mkchromecast"></a> | **[mkchromecast](https://github.com/muammar/mkchromecast)** | Cast macOS and Linux Audio/Video to your Google Cast and Sonos Devices. | `Python` | [Source](https://github.com/muammar/mkchromecast) | `MIT` |
| <a href="https://github.com/insidegui/PodcastMenu"><img src="./icons/project-icons/podcastmenu.png" width="32" height="32" alt="PodcastMenu"></a> | **[PodcastMenu](https://github.com/insidegui/PodcastMenu)** | PodcastMenu is a simple app which puts [Overcast](https://overcast.fm/) on your Mac's menu bar so you can listen to your favorite podcasts while you work. | `Swift` | [Source](https://github.com/insidegui/PodcastMenu) | `MIT` |
| <a href="https://github.com/Podlive/podlive-macos"><img src="./icons/project-icons/podlive-for-macos.png" width="32" height="32" alt="Podlive for macOS"></a> | **[Podlive for macOS](https://github.com/Podlive/podlive-macos)** | macOS client to listen to live streaming podcasts (only). It currently supports all livestreams broadcasting via Ultraschall with [Studio Link On Air](https://studio-link.de/). | `Objective-C` | [Source](https://github.com/Podlive/podlive-macos) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="productivity"></a>
### ⏱️ Productivity

> Application launchers, clipboard managers, pomodoro timers, and daily workflow enhancers.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://activitywatch.net"><img src="./icons/project-icons/activitywatch.png" width="32" height="32" alt="ActivityWatch"></a> | **[ActivityWatch](https://activitywatch.net)** | Open-source automated time tracker that tracks how you spend time on your devices. | `Python` | [Website](https://activitywatch.net) • [Source](https://github.com/ActivityWatch/activitywatch) | `MIT` |
| <a href="https://alt-tab-macos.netlify.app"><img src="./icons/project-icons/alt-tab-macos.svg" width="32" height="32" alt="AltTab"></a> | **[AltTab](https://alt-tab-macos.netlify.app)** | Brings Windows-style alt-tab window switcher functionality with live window previews to macOS. | `Swift` | [Website](https://alt-tab-macos.netlify.app) • [Source](https://github.com/lwouis/alt-tab-macos) | `GPL-3.0` |
| <a href="https://github.com/klaudiosinani/ao"><img src="./icons/project-icons/ao.png" width="32" height="32" alt="Ao"></a> | **[Ao](https://github.com/klaudiosinani/ao)** | Elegant Microsoft To-Do desktop app. | `JavaScript` | [Source](https://github.com/klaudiosinani/ao) | `MIT` |
| <a href="https://blinkeye.vercel.app"><img src="./icons/project-icons/blink-eye.png" width="32" height="32" alt="Blink Eye"></a> | **[Blink Eye](https://blinkeye.vercel.app)** | An Open-Source minimalist Eye Care reminder & Break Timer app for Windows, macOS, and Linux. | `TypeScript` | [Website](https://blinkeye.vercel.app) • [Source](https://github.com/nomandhoni-cs/blink-eye) | `MIT` |
| <a href="https://github.com/varol/Calculeta"><img src="./icons/project-icons/calculeta.png" width="32" height="32" alt="Calculeta"></a> | **[Calculeta](https://github.com/varol/Calculeta)** | Calculator for macOS which working on statusbar. | `Swift` | [Source](https://github.com/varol/Calculeta) | `MIT` |
| <a href="https://github.com/cerebroapp/cerebro"><img src="./icons/project-icons/cerebro.png" width="32" height="32" alt="Cerebro"></a> | **[Cerebro](https://github.com/cerebroapp/cerebro)** | Cross-platform launcher app. | `JavaScript` | [Source](https://github.com/cerebroapp/cerebro) | `MIT` |
| <a href="https://github.com/naotaka/ClipMenu"><img src="./icons/project-icons/clipmenu.png" width="32" height="32" alt="ClipMenu"></a> | **[ClipMenu](https://github.com/naotaka/ClipMenu)** | Clipboard manager for macOS. | `Objective-C` | [Source](https://github.com/naotaka/ClipMenu) | `MIT` |
| <a href="https://github.com/n0shake/Clocker"><img src="./icons/project-icons/clocker.png" width="32" height="32" alt="Clocker"></a> | **[Clocker](https://github.com/n0shake/Clocker)** | macOS app to plan and organize through timezones. | `Objective-C` | [Source](https://github.com/n0shake/Clocker) | `MIT` |
| <a href="https://www.condution.com"><img src="./icons/project-icons/condution.png" width="32" height="32" alt="Condution"></a> | **[Condution](https://www.condution.com)** | Create tasks, manage due dates, and filter with powerful perspectives. | `JavaScript` | [Website](https://www.condution.com) • [Source](https://github.com/Shabang-Systems/Condution) | `MIT` |
| <a href="https://github.com/dustinrue/ControlPlane"><img src="./icons/project-icons/controlplane.png" width="32" height="32" alt="ControlPlane"></a> | **[ControlPlane](https://github.com/dustinrue/ControlPlane)** | Automate running tasks based on where you are or what you do. | `Objective-C` | [Source](https://github.com/dustinrue/ControlPlane) | `MIT` |
| <a href="https://devutils.com"><img src="./icons/project-icons/devutils-app.png" width="32" height="32" alt="DevUtils.app"></a> | **[DevUtils.app](https://devutils.com)** | Developer Utilities for macOS, helps you with your tiny daily tasks with just a single click! i.e., JSON Formatter, UUID Generator... | `Swift` | [Website](https://devutils.com) • [Source](https://github.com/DevUtilsApp/DevUtils-app) | `MIT` |
| <a href="https://dockit-docs.pages.dev/?s=open-sourse-mac-os-apps"><img src="./icons/project-icons/dockit.png" width="32" height="32" alt="Dockit"></a> | **[Dockit](https://dockit-docs.pages.dev/?s=open-sourse-mac-os-apps)** | An application that can dock any window to the edge of the screen. | `Swift` | [Website](https://dockit-docs.pages.dev/?s=open-sourse-mac-os-apps) • [Source](https://github.com/xicheng148/Dockit) | `MIT` |
| <a href="https://github.com/GameGodS3/DropPoint"><img src="./icons/project-icons/droppoint.png" width="32" height="32" alt="DropPoint"></a> | **[DropPoint](https://github.com/GameGodS3/DropPoint)** | Make drag-and-drop easier using DropPoint. Helps to drag content without having to open side-by-side windows. | `JavaScript` | [Source](https://github.com/GameGodS3/DropPoint) | `MIT` |
| <a href="https://espanso.org"><img src="./icons/project-icons/espanso.png" width="32" height="32" alt="espanso"></a> | **[espanso](https://espanso.org)** | Cross-platform Text Expander, a powerful replacement for Alfred Snippets | `Rust` | [Website](https://espanso.org) • [Source](https://github.com/espanso/espanso) | `MIT` |
| <a href="https://github.com/elfmz/far2l"><img src="./icons/project-icons/far2l.png" width="32" height="32" alt="far2l"></a> | **[far2l](https://github.com/elfmz/far2l)** | Linux/Mac fork of FAR Manager v2 | `C` | [Source](https://github.com/elfmz/far2l) | `MIT` |
| <a href="https://fazm.ai"><img src="./icons/project-icons/fazm.png" width="32" height="32" alt="Fazm"></a> | **[Fazm](https://fazm.ai)** | The fastest AI computer agent for macOS. Takes voice commands and controls your entire desktop. | `Swift` | [Website](https://fazm.ai) • [Source](https://github.com/m13v/fazm) | `MIT` |
| <a href="https://filearchitect.com"><img src="./icons/project-icons/file-architect.png" width="32" height="32" alt="File Architect"></a> | **[File Architect](https://filearchitect.com)** | Create file and folder structures from plain text descriptions. | `TypeScript` | [Website](https://filearchitect.com) • [Source](https://github.com/filearchitect/app) | `MIT` |
| <a href="https://flameshot.org"><img src="./icons/project-icons/flameshot.png" width="32" height="32" alt="Flameshot"></a> | **[Flameshot](https://flameshot.org)** | Powerful yet simple to use screenshot software with in-place annotation and editing. | `C++` | [Website](https://flameshot.org) • [Source](https://github.com/flameshot-org/flameshot) | `GPL-3.0` |
| <a href="https://github.com/TermiT/flycut"><img src="./icons/project-icons/flycut.png" width="32" height="32" alt="Flycut"></a> | **[Flycut](https://github.com/TermiT/flycut)** | Clean and simple clipboard manager for developers. | `Objective-C` | [Source](https://github.com/TermiT/flycut) | `MIT` |
| <a href="https://freeter.io"><img src="./icons/project-icons/freeter.png" width="32" height="32" alt="Freeter"></a> | **[Freeter](https://freeter.io)** | App that allows you to gather everything you need for work in one place, organized by projects and workflows, and have a quick access to them. | `TypeScript` | [Website](https://freeter.io) • [Source](https://github.com/FreeterApp/Freeter) | `MIT` |
| <a href="https://github.com/dwarvesf/hidden"><img src="./icons/project-icons/hidden-bar.png" width="32" height="32" alt="Hidden Bar"></a> | **[Hidden Bar](https://github.com/dwarvesf/hidden)** | Ultra-lightweight menu bar utility that gives Mac users full control over menu bar icons. | `Swift` | [Source](https://github.com/dwarvesf/hidden) | `MIT` |
| <a href="https://github.com/jordanbaird/Ice"><img src="./icons/project-icons/ice.png" width="32" height="32" alt="Ice"></a> | **[Ice](https://github.com/jordanbaird/Ice)** | Powerful menu bar manager that lets you hide, show, and organize menu bar items. | `Swift` | [Source](https://github.com/jordanbaird/Ice) | `MIT` |
| <a href="https://getkap.co"><img src="./icons/project-icons/kap.svg" width="32" height="32" alt="Kap"></a> | **[Kap](https://getkap.co)** | Open-source screen recorder built with web technologies that exports to GIF, MP4, and WebM. | `TypeScript` | [Website](https://getkap.co) • [Source](https://github.com/wulkano/kap) | `MIT` |
| <a href="https://github.com/Clipy/KeyHolder"><img src="./icons/project-icons/keyholder.png" width="32" height="32" alt="KeyHolder"></a> | **[KeyHolder](https://github.com/Clipy/KeyHolder)** | Record shortcuts in macOS, like Alfred.app. | `Swift` | [Source](https://github.com/Clipy/KeyHolder) | `MIT` |
| <a href="https://github.com/kiwix/apple"><img src="./icons/project-icons/kiwix.png" width="32" height="32" alt="Kiwix"></a> | **[Kiwix](https://github.com/kiwix/apple)** | Kiwix for iOS and macOS, build on Swift. | `Swift` | [Source](https://github.com/kiwix/apple) | `MIT` |
| <a href="https://linearmouse.app"><img src="./icons/project-icons/linearmouse.svg" width="32" height="32" alt="LinearMouse"></a> | **[LinearMouse](https://linearmouse.app)** | Utility to customize mouse and trackpad acceleration, scrolling direction, and cursor behaviors. | `Swift` | [Website](https://linearmouse.app) • [Source](https://github.com/linearmouse/linearmouse) | `MIT` |
| <a href="https://github.com/fespinoza/LinkedIdeas"><img src="./icons/project-icons/linked-ideas.png" width="32" height="32" alt="Linked Ideas"></a> | **[Linked Ideas](https://github.com/fespinoza/LinkedIdeas)** | macOS application to write down and connect ideas. | `Swift` | [Source](https://github.com/fespinoza/LinkedIdeas) | `MIT` |
| <a href="https://github.com/instance01/mac-screenshot-tracker"><img src="./icons/project-icons/mac-screenshot-tracker.png" width="32" height="32" alt="Mac Screenshot Tracker"></a> | **[Mac Screenshot Tracker](https://github.com/instance01/mac-screenshot-tracker)** | An open source, free and hackable screenshot tracker. Re-watch what you've been working on! | `Python` | [Source](https://github.com/instance01/mac-screenshot-tracker) | `MIT` |
| <a href="https://maccy.app"><img src="./icons/project-icons/maccy.png" width="32" height="32" alt="Maccy"></a> | **[Maccy](https://maccy.app)** | Lightweight, native clipboard manager with search history and zero telemetry. | `Swift` | [Website](https://maccy.app) • [Source](https://github.com/p0deje/Maccy) | `MIT` |
| <a href="https://github.com/shubhambatra3019/macOrganizer"><img src="./icons/project-icons/macorganizer.png" width="32" height="32" alt="macOrganizer"></a> | **[macOrganizer](https://github.com/shubhambatra3019/macOrganizer)** | macOS app for organizing files or removing unnecessary files. | `Swift` | [Source](https://github.com/shubhambatra3019/macOrganizer) | `MIT` |
| <a href="https://github.com/hql287/Manta"><img src="./icons/project-icons/manta.png" width="32" height="32" alt="Manta"></a> | **[Manta](https://github.com/hql287/Manta)** | Flexible invoicing desktop app with beautiful & customizable templates. | `JavaScript` | [Source](https://github.com/hql287/Manta) | `MIT` |
| <a href="https://omniprompt.app"><img src="./icons/project-icons/omniprompt.png" width="32" height="32" alt="OmniPrompt"></a> | **[OmniPrompt](https://omniprompt.app)** | Your ultimate GPT companion for seamless access on your Mac | `Swift` | [Website](https://omniprompt.app) • [Source](https://github.com/nsmet/omniprompt-gpt-mac-app) | `MIT` |
| <a href="https://github.com/thomasbrueggemann/paperless-desktop"><img src="./icons/project-icons/paperless-desktop.png" width="32" height="32" alt="Paperless Desktop"></a> | **[Paperless Desktop](https://github.com/thomasbrueggemann/paperless-desktop)** | Desktop app that uses the paperless API to manage your document scans. | `JavaScript` | [Source](https://github.com/thomasbrueggemann/paperless-desktop) | `MIT` |
| <a href="https://github.com/PDF-Archiver/PDF-Archiver"><img src="./icons/project-icons/pdf-archiver.png" width="32" height="32" alt="PDF Archiver"></a> | **[PDF Archiver](https://github.com/PDF-Archiver/PDF-Archiver)** | Nice tool for tagging and archiving tasks. | `Swift` | [Source](https://github.com/PDF-Archiver/PDF-Archiver) | `MIT` |
| <a href="https://github.com/ziulev/pomodoro-cycle-app/releases"><img src="./icons/project-icons/pomodoro-cycle.png" width="32" height="32" alt="Pomodoro Cycle"></a> | **[Pomodoro Cycle](https://github.com/ziulev/pomodoro-cycle-app/releases)** | Pomodoro Cycle for macOS | `TypeScript` | [Website](https://github.com/ziulev/pomodoro-cycle-app/releases) • [Source](https://github.com/ziulev/pomodoro-cycle-app) | `MIT` |
| <a href="https://github.com/quicksilver/Quicksilver"><img src="./icons/project-icons/quicksilver.png" width="32" height="32" alt="Quicksilver"></a> | **[Quicksilver](https://github.com/quicksilver/Quicksilver)** | Quicksilver is a fast macOS productivity application that gives you the power to control your Mac quickly and elegantly. | `Objective-C` | [Source](https://github.com/quicksilver/Quicksilver) | `MIT` |
| <a href="https://github.com/quickwords/quickwords"><img src="./icons/project-icons/quickwords.png" width="32" height="32" alt="Quickwords"></a> | **[Quickwords](https://github.com/quickwords/quickwords)** | Write anything in a matter of seconds. Create snippets that can substitute text, execute tedious tasks and more. | `JavaScript` | [Source](https://github.com/quickwords/quickwords) | `MIT` |
| <a href="https://readest.com"><img src="./icons/project-icons/readest.png" width="32" height="32" alt="Readest"></a> | **[Readest](https://readest.com)** | Readest is a modern, feature-rich ebook reader designed for avid readers. | `TypeScript` | [Website](https://readest.com) • [Source](https://github.com/readest/readest) | `MIT` |
| <a href="https://github.com/fikrikarim/repose"><img src="./icons/project-icons/repose.png" width="32" height="32" alt="Repose"></a> | **[Repose](https://github.com/fikrikarim/repose)** | Break reminder for macOS that automatically pauses during meetings. | `Swift` | [Source](https://github.com/fikrikarim/repose) | `MIT` |
| <a href="https://saneclip.com"><img src="./icons/project-icons/saneclip.png" width="32" height="32" alt="SaneClip"></a> | **[SaneClip](https://saneclip.com)** | Clipboard manager with Touch ID protection, AES-256-GCM encryption, and sensitive data detection. | `Swift` | [Website](https://saneclip.com) • [Source](https://github.com/sane-apps/SaneClip) | `MIT` |
| <a href="https://sanesales.com"><img src="./icons/project-icons/sanesales.png" width="32" height="32" alt="SaneSales"></a> | **[SaneSales](https://sanesales.com)** | Universal indie sales tracker for LemonSqueezy, Gumroad, and Stripe with on-device privacy. | `Swift` | [Website](https://sanesales.com) • [Source](https://github.com/sane-apps/SaneSales) | `MIT` |
| <a href="https://screenpi.pe"><img src="./icons/project-icons/screenpipe.png" width="32" height="32" alt="Screenpipe"></a> | **[Screenpipe](https://screenpi.pe)** | 24/7 screen and audio recording with AI-powered search. Local-first, privacy-focused rewind alternative. | `Rust` | [Website](https://screenpi.pe) • [Source](https://github.com/screenpipe/screenpipe) | `MIT` |
| <a href="https://github.com/SelfControlApp/selfcontrol"><img src="./icons/project-icons/selfcontrol.png" width="32" height="32" alt="SelfControl"></a> | **[SelfControl](https://github.com/SelfControlApp/selfcontrol)** | macOS app to block your own access to distracting websites etc for a predetermined period of time. It can not be undone by the app or by a restart – you must wait for the timer to run out. | `Objective-C` | [Source](https://github.com/SelfControlApp/selfcontrol) | `MIT` |
| <a href="https://github.com/Mas0nSun/Slime"><img src="./icons/project-icons/slime.png" width="32" height="32" alt="Slime"></a> | **[Slime](https://github.com/Mas0nSun/Slime)** | App icon assets generator written in SwiftUI | `Swift` | [Source](https://github.com/Mas0nSun/Slime) | `MIT` |
| <a href="https://github.com/ospfranco/sol"><img src="./icons/project-icons/sol.png" width="32" height="32" alt="Sol"></a> | **[Sol](https://github.com/ospfranco/sol)** | Open-source macOS launcher with calendar integration, window management, and bookmarks. | `TypeScript` | [Source](https://github.com/ospfranco/sol) | `MIT` |
| <a href="https://apps.apple.com/app/speed-reader/id1258448209"><img src="./icons/project-icons/speed-reader.png" width="32" height="32" alt="Speed Reader"></a> | **[Speed Reader](https://apps.apple.com/app/speed-reader/id1258448209)** | Read faster with the power of silencing vocalization with SpeedReader. | `Swift` | [Website](https://apps.apple.com/app/speed-reader/id1258448209) • [Source](https://github.com/LumingYin/SpeedReader) | `MIT` |
| <a href="https://github.com/spotter-application/spotter"><img src="./icons/project-icons/spotter.png" width="32" height="32" alt="Spotter"></a> | **[Spotter](https://github.com/spotter-application/spotter)** | Productivity tool, the main function is to search and launch external application actions and applications themselves, so you can stay focused on your current task. Kind of spotlight or alfred alternative. | `TypeScript` | [Source](https://github.com/spotter-application/spotter) | `MIT` |
| <a href="https://github.com/Onix-Systems/osx-status-bar-todo"><img src="./icons/project-icons/status-bar-todo.png" width="32" height="32" alt="status-bar-todo"></a> | **[status-bar-todo](https://github.com/Onix-Systems/osx-status-bar-todo)** | Simple macOS app to keep TODO-list in status bar. | `Swift` | [Source](https://github.com/Onix-Systems/osx-status-bar-todo) | `MIT` |
| <a href="https://github.com/LumingYin/StickyNotes/releases"><img src="./icons/project-icons/stickynotes.png" width="32" height="32" alt="StickyNotes"></a> | **[StickyNotes](https://github.com/LumingYin/StickyNotes/releases)** | A Windows 10-esque Sticky Notes app implemented in AppKit. | `Swift` | [Website](https://github.com/LumingYin/StickyNotes/releases) • [Source](https://github.com/LumingYin/StickyNotes) | `MIT` |
| <a href="https://khrykin.github.io/StrategrDesktop"><img src="./icons/project-icons/strategr.png" width="32" height="32" alt="Strategr"></a> | **[Strategr](https://khrykin.github.io/StrategrDesktop)** | No-fuss time management. | `C++` | [Website](https://khrykin.github.io/StrategrDesktop) • [Source](https://github.com/khrykin/StrategrDesktop) | `MIT` |
| <a href="https://github.com/hovancik/stretchly"><img src="./icons/project-icons/stretchly.png" width="32" height="32" alt="stretchly"></a> | **[stretchly](https://github.com/hovancik/stretchly)** | Cross-platform electron app that reminds you to take breaks when working with computer. | `JavaScript` | [Source](https://github.com/hovancik/stretchly) | `MIT` |
| <a href="https://super-productivity.com"><img src="./icons/project-icons/super-productivity.png" width="32" height="32" alt="Super Productivity"></a> | **[Super Productivity](https://super-productivity.com)** | Free to do list & time tracker for programmers & designers with Jira integration. | `TypeScript` | [Website](https://super-productivity.com) • [Source](https://github.com/johannesjo/super-productivity) | `MIT` |
| <a href="https://github.com/joaomoreno/thyme"><img src="./icons/project-icons/thyme.png" width="32" height="32" alt="Thyme"></a> | **[Thyme](https://github.com/joaomoreno/thyme)** | The task timer for OS X. | `Objective-C` | [Source](https://github.com/joaomoreno/thyme) | `MIT` |
| <a href="https://timetoleave.app"><img src="./icons/project-icons/time-to-leave.png" width="32" height="32" alt="Time to Leave"></a> | **[Time to Leave](https://timetoleave.app)** | Log work hours and get notified when it's time to leave the office and start to live. | `JavaScript` | [Website](https://timetoleave.app) • [Source](https://github.com/thamara/time-to-leave) | `MIT` |
| <a href="https://github.com/michaelvillar/timer-app"><img src="./icons/project-icons/timer.png" width="32" height="32" alt="Timer"></a> | **[Timer](https://github.com/michaelvillar/timer-app)** | Simple Timer app for Mac. | `Swift` | [Source](https://github.com/michaelvillar/timer-app) | `MIT` |
| <a href="https://github.com/toggl-open-source/toggldesktop"><img src="./icons/project-icons/toggl-desktop.png" width="32" height="32" alt="Toggl Desktop"></a> | **[Toggl Desktop](https://github.com/toggl-open-source/toggldesktop)** | Toggl Desktop app for Windows, Mac and Linux. | `C++` | [Source](https://github.com/toggl-open-source/toggldesktop) | `MIT` |
| <a href="https://github.com/ivoronin/TomatoBar"><img src="./icons/project-icons/tomatobar.png" width="32" height="32" alt="TomatoBar"></a> | **[TomatoBar](https://github.com/ivoronin/TomatoBar)** | Pomodoro Technique Timer for macOS with Touch Bar support. | `Swift` | [Source](https://github.com/ivoronin/TomatoBar) | `MIT` |
| <a href="https://github.com/jlong/TrelloApp"><img src="./icons/project-icons/trelloapp.png" width="32" height="32" alt="TrelloApp"></a> | **[TrelloApp](https://github.com/jlong/TrelloApp)** | Unofficial wrapper application for Trello.com written in Swift. This is almost a "Hello World" for a site specific browser. | `Swift` | [Source](https://github.com/jlong/TrelloApp) | `MIT` |
| <a href="https://ueli.app"><img src="./icons/project-icons/ueli.png" width="32" height="32" alt="Ueli"></a> | **[Ueli](https://ueli.app)** | A keystroke launcher for macOS (and Windows) like Spotlight or Alfred. | `TypeScript` | [Website](https://ueli.app) • [Source](https://github.com/oliverschwendener/ueli) | `MIT` |
| <a href="https://github.com/TailorDev/Watson"><img src="./icons/project-icons/watson.png" width="32" height="32" alt="Watson"></a> | **[Watson](https://github.com/TailorDev/Watson)** | A CLI application for time tracking. | `Python` | [Source](https://github.com/TailorDev/Watson) | `MIT` |
| <a href="https://github.com/1000ch/whale"><img src="./icons/project-icons/whale.png" width="32" height="32" alt="Whale"></a> | **[Whale](https://github.com/1000ch/whale)** | Unofficial Trello app. | `JavaScript` | [Source](https://github.com/1000ch/whale) | `MIT` |
| <a href="https://github.com/xournalpp/xournalpp/"><img src="./icons/project-icons/xournal.png" width="32" height="32" alt="Xournal++"></a> | **[Xournal++](https://github.com/xournalpp/xournalpp/)** | Take handwritten notes with ease | `C++` | [Source](https://github.com/xournalpp/xournalpp/) | `MIT` |
| <a href="https://yippy.mattdavo.com"><img src="./icons/project-icons/yippy.png" width="32" height="32" alt="Yippy"></a> | **[Yippy](https://yippy.mattdavo.com)** | macOS open source clipboard manager | `Swift` | [Website](https://yippy.mattdavo.com) • [Source](https://github.com/mattDavo/Yippy) | `MIT` |
| <a href="https://github.com/sendyhalim/Yomu"><img src="./icons/project-icons/yomu.png" width="32" height="32" alt="Yomu"></a> | **[Yomu](https://github.com/sendyhalim/Yomu)** | Manga reader app for macOS. | `Swift` | [Source](https://github.com/sendyhalim/Yomu) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="screensaver"></a>
### 🌙 Screensaver

> Aesthetic screensavers, clock displays, retro animations, and dynamic ambient visuals.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/JohnCoates/Aerial"><img src="./icons/project-icons/aerial.png" width="32" height="32" alt="Aerial"></a> | **[Aerial](https://github.com/JohnCoates/Aerial)** | Apple TV Aerial Screensaver for macOS. | `Swift` | [Source](https://github.com/JohnCoates/Aerial) | `MIT` |
| <a href="https://github.com/pedrommcarrasco/Brooklyn"><img src="./icons/project-icons/brooklyn.png" width="32" height="32" alt="Brooklyn"></a> | **[Brooklyn](https://github.com/pedrommcarrasco/Brooklyn)** | Screensaver inspired by Apple's Event on October 30, 2018. | `Swift` | [Source](https://github.com/pedrommcarrasco/Brooklyn) | `MIT` |
| <a href="https://github.com/chrstphrknwtn/epoch-flip-clock-screensaver"><img src="./icons/project-icons/epoch-flip-clock-screensaver.png" width="32" height="32" alt="Epoch Flip Clock Screensaver"></a> | **[Epoch Flip Clock Screensaver](https://github.com/chrstphrknwtn/epoch-flip-clock-screensaver)** | Unix epoch timestamp flip clock screensaver. | `Objective-C` | [Source](https://github.com/chrstphrknwtn/epoch-flip-clock-screensaver) | `MIT` |
| <a href="https://github.com/ved62/Image-As-Wallpaper"><img src="./icons/project-icons/image-as-wallpaper.png" width="32" height="32" alt="Image-As-Wallpaper"></a> | **[Image-As-Wallpaper](https://github.com/ved62/Image-As-Wallpaper)** | Utility application helps with selection of images for using as desktop wallpaper or in screensaver on Mac computers. | `Swift` | [Source](https://github.com/ved62/Image-As-Wallpaper) | `MIT` |
| <a href="https://github.com/leonspok/Irvue-Screensaver"><img src="./icons/project-icons/irvue.png" width="32" height="32" alt="Irvue"></a> | **[Irvue](https://github.com/leonspok/Irvue-Screensaver)** | Screensaver for macOS. | `Objective-C` | [Source](https://github.com/leonspok/Irvue-Screensaver) | `MIT` |
| <a href="https://github.com/amiantos/lifesaver"><img src="./icons/project-icons/life-saver.png" width="32" height="32" alt="Life Saver"></a> | **[Life Saver](https://github.com/amiantos/lifesaver)** | An abstract screensaver based on Conway's Game of Life implemented with SpriteKit | `Swift` | [Source](https://github.com/amiantos/lifesaver) | `MIT` |
| <a href="https://mattiarossini.github.io/MinimalClock"><img src="./icons/project-icons/minimalclock.png" width="32" height="32" alt="MinimalClock"></a> | **[MinimalClock](https://mattiarossini.github.io/MinimalClock)** | Simple and elegant screensaver that displays the time. | `Swift` | [Website](https://mattiarossini.github.io/MinimalClock) • [Source](https://github.com/mattiarossini/MinimalClock) | `MIT` |
| <a href="https://github.com/obrhoff/MusaicFM"><img src="./icons/project-icons/musaicfm.png" width="32" height="32" alt="MusaicFM"></a> | **[MusaicFM](https://github.com/obrhoff/MusaicFM)** | iTunes Screensaver Clone for Spotify and Last.fm | `Objective-C` | [Source](https://github.com/obrhoff/MusaicFM) | `MIT` |
| <a href="https://github.com/vpeschenkov/Predator"><img src="./icons/project-icons/predator.png" width="32" height="32" alt="Predator"></a> | **[Predator](https://github.com/vpeschenkov/Predator)** | A predator-inspired clock screensaver for macOS | `Swift` | [Source](https://github.com/vpeschenkov/Predator) | `MIT` |
| <a href="https://github.com/winterbe/github-matrix-screensaver"><img src="./icons/project-icons/the-github-matrix-screensaver.png" width="32" height="32" alt="The GitHub Matrix Screensaver"></a> | **[The GitHub Matrix Screensaver](https://github.com/winterbe/github-matrix-screensaver)** | The GitHub Matrix Screensaver for macOS. | `JavaScript` | [Source](https://github.com/winterbe/github-matrix-screensaver) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="security"></a>
### 🔒 Security

> Password vaults, personal application firewalls, disk encryption, and network monitors.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://bitwarden.com"><img src="./icons/project-icons/bitwarden.png" width="32" height="32" alt="Bitwarden"></a> | **[Bitwarden](https://bitwarden.com)** | Trusted open-source password manager with end-to-end encryption across all your devices. | `TypeScript` | [Website](https://bitwarden.com) • [Source](https://github.com/bitwarden/clients) | `GPL-3.0` |
| <a href="https://adequate.systems"><img src="./icons/project-icons/cloaker.png" width="32" height="32" alt="Cloaker"></a> | **[Cloaker](https://adequate.systems)** | simple drag-and-drop, password-based file encryption. | `Rust` | [Website](https://adequate.systems) • [Source](https://github.com/spieglt/cloaker) | `MIT` |
| <a href="https://cryptomator.org"><img src="./icons/project-icons/cryptomator.png" width="32" height="32" alt="Cryptomator"></a> | **[Cryptomator](https://cryptomator.org)** | Client-side encryption for your cloud files, preventing unauthorized inspection of documents. | `Java` | [Website](https://cryptomator.org) • [Source](https://github.com/cryptomator/cryptomator) | `GPL-3.0` |
| <a href="https://keepassxc.org"><img src="./icons/project-icons/keepassxc.png" width="32" height="32" alt="KeePassXC"></a> | **[KeePassXC](https://keepassxc.org)** | Community fork of KeePassX, a cross-platform password manager with local encrypted storage. | `C++` | [Website](https://keepassxc.org) • [Source](https://github.com/keepassxreboot/keepassxc) | `GPL-3.0` |
| <a href="https://objective-see.org/products/knockknock.html"><img src="./icons/project-icons/knockknock.png" width="32" height="32" alt="KnockKnock"></a> | **[KnockKnock](https://objective-see.org/products/knockknock.html)** | Scans your Mac for persistent software, background daemons, and launch items. | `Objective-C` | [Website](https://objective-see.org/products/knockknock.html) • [Source](https://github.com/objective-see/KnockKnock) | `GPL-3.0` |
| <a href="https://objective-see.org/products/lulu.html"><img src="./icons/project-icons/lulu.png" width="32" height="32" alt="LuLu"></a> | **[LuLu](https://objective-see.org/products/lulu.html)** | Free, open-source macOS firewall aimed at blocking unauthorized outgoing network connections. | `Objective-C` | [Website](https://objective-see.org/products/lulu.html) • [Source](https://github.com/objective-see/LuLu) | `GPL-3.0` |
| <a href="https://github.com/wynioux/macOS-GateKeeper-Helper"><img src="./icons/project-icons/macos-gatekeeper-helper.png" width="32" height="32" alt="macOS GateKeeper Helper"></a> | **[macOS GateKeeper Helper](https://github.com/wynioux/macOS-GateKeeper-Helper)** | Simple macOS GateKeeper script. It helps you to control your GateKeeper. | `Shell` | [Source](https://github.com/wynioux/macOS-GateKeeper-Helper) | `MIT` |
| <a href="https://sanehosts.com"><img src="./icons/project-icons/sanehosts.png" width="32" height="32" alt="SaneHosts"></a> | **[SaneHosts](https://sanehosts.com)** | System-level ad and tracker blocker via /etc/hosts with 200+ curated blocklists and Touch ID protection. | `Swift` | [Website](https://sanehosts.com) • [Source](https://github.com/sane-apps/SaneHosts) | `MIT` |
| <a href="https://github.com/alichtman/stronghold"><img src="./icons/project-icons/stronghold.png" width="32" height="32" alt="stronghold"></a> | **[stronghold](https://github.com/alichtman/stronghold)** | Easily configure macOS security settings from the terminal. | `Python` | [Source](https://github.com/alichtman/stronghold) | `MIT` |
| <a href="https://getswifty.pro"><img src="./icons/project-icons/swifty.png" width="32" height="32" alt="Swifty"></a> | **[Swifty](https://getswifty.pro)** | Free and offline password manager. | `JavaScript` | [Website](https://getswifty.pro) • [Source](https://github.com/swiftyapp/swifty) | `MIT` |
| <a href="https://www.torproject.org"><img src="./icons/project-icons/tor-browser.png" width="32" height="32" alt="Tor Browser"></a> | **[Tor Browser](https://www.torproject.org)** | Privacy-focused web browser that routes traffic through the encrypted Tor volunteer network. | `C++` | [Website](https://www.torproject.org) • [Source](https://github.com/torproject/tor-browser) | `BSD-3-Clause` |
| <a href="https://github.com/HMAKT99/UnTouchID"><img src="./icons/project-icons/untouchid.png" width="32" height="32" alt="UnTouchID"></a> | **[UnTouchID](https://github.com/HMAKT99/UnTouchID)** | Use your phone's fingerprint to authenticate on any Mac. | `Swift` | [Source](https://github.com/HMAKT99/UnTouchID) | `MIT` |
| <a href="https://www.veracrypt.fr"><img src="./icons/project-icons/veracrypt.png" width="32" height="32" alt="VeraCrypt"></a> | **[VeraCrypt](https://www.veracrypt.fr)** | Disk encryption with strong security based on TrueCrypt. | `C` | [Website](https://www.veracrypt.fr) • [Source](https://github.com/veracrypt/VeraCrypt) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="sharing-files"></a>
### 📤 Sharing Files

> P2P file transfer tools, AirDrop alternatives, local network sharing, and file sync apps.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/deluge-torrent/deluge"><img src="./icons/project-icons/deluge.png" width="32" height="32" alt="Deluge"></a> | **[Deluge](https://github.com/deluge-torrent/deluge)** | Lightweight cross-platform BitTorrent client. | `Python` | [Source](https://github.com/deluge-torrent/deluge) | `MIT` |
| <a href="https://ariessciences.com/highlight?product=easy-share-uploader"><img src="./icons/project-icons/easy-share-uploader.svg" width="32" height="32" alt="Easy Share Uploader"></a> | **[Easy Share Uploader](https://ariessciences.com/highlight?product=easy-share-uploader)** | Allows users to easily host their local images to the internet through multiple services and available on App Store. | `Objective-C` | [Website](https://ariessciences.com/highlight?product=easy-share-uploader) • [Source](https://github.com/Aries-Sciences-LLC/Easy-Share-Uploader) | `MIT` |
| <a href="https://localsend.org"><img src="./icons/project-icons/localsend.png" width="32" height="32" alt="LocalSend"></a> | **[LocalSend](https://localsend.org)** | AirDrop alternative to share files and messages nearby across macOS, iOS, Android, and Windows. | `Dart` | [Website](https://localsend.org) • [Source](https://github.com/localsend/localsend) | `MIT` |
| <a href="https://github.com/mileswd/mac2imgur"><img src="./icons/project-icons/mac2imgur.png" width="32" height="32" alt="mac2imgur"></a> | **[mac2imgur](https://github.com/mileswd/mac2imgur)** | Simple Mac app designed to make uploading images and screenshots to Imgur quick and effortless. | `Swift` | [Source](https://github.com/mileswd/mac2imgur) | `MIT` |
| <a href="https://nitroshare.net"><img src="./icons/project-icons/nitroshare.png" width="32" height="32" alt="NitroShare"></a> | **[NitroShare](https://nitroshare.net)** | Transferring files from one device to another | `C++` | [Website](https://nitroshare.net) • [Source](https://github.com/nitroshare/nitroshare-desktop) | `MIT` |
| <a href="https://github.com/qbittorrent/qBittorrent"><img src="./icons/project-icons/qbittorrent.png" width="32" height="32" alt="qBittorrent"></a> | **[qBittorrent](https://github.com/qbittorrent/qBittorrent)** | BitTorrent client in Qt. | `C++` | [Source](https://github.com/qbittorrent/qBittorrent) | `MIT` |
| <a href="https://github.com/timonus/Rhea"><img src="./icons/project-icons/rhea.png" width="32" height="32" alt="Rhea"></a> | **[Rhea](https://github.com/timonus/Rhea)** | macOS status bar app for quickly sharing files and URLs. | `Objective-C` | [Source](https://github.com/timonus/Rhea) | `MIT` |
| <a href="https://soduto.com"><img src="./icons/project-icons/soduto.png" width="32" height="32" alt="Soduto"></a> | **[Soduto](https://soduto.com)** | Soduto is a KDEConnect compatible application for macOS. It gives AirDrop like integration and allows file and clipboard sharing between your phones, desktops and tablets. | `Swift` | [Website](https://soduto.com) • [Source](https://github.com/soduto/Soduto) | `MIT` |
| <a href="https://syncthing.net"><img src="./icons/project-icons/syncthing-macos.png" width="32" height="32" alt="Syncthing macOS"></a> | **[Syncthing macOS](https://syncthing.net)** | Native macOS menu bar wrapper for continuous continuous file synchronization via Syncthing. | `Swift` | [Website](https://syncthing.net) • [Source](https://github.com/syncthing/syncthing-macos) | `MIT` |
| <a href="https://transmissionbt.com"><img src="./icons/project-icons/transmission.png" width="32" height="32" alt="Transmission"></a> | **[Transmission](https://transmissionbt.com)** | Fast, easy, and lightweight BitTorrent client with native Cocoa user interface. | `C++` | [Website](https://transmissionbt.com) • [Source](https://github.com/transmission/transmission) | `GPL-3.0` |
| <a href="https://github.com/Tribler/tribler"><img src="./icons/project-icons/tribler.png" width="32" height="32" alt="Tribler"></a> | **[Tribler](https://github.com/Tribler/tribler)** | Privacy enhanced BitTorrent client with P2P content discovery. | `Python` | [Source](https://github.com/Tribler/tribler) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="social-networking"></a>
### 👥 Social Networking

> Clients for decentralized social networks, Mastodon, Bluesky, and community platforms.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/sindresorhus/caprine#features"><img src="./icons/project-icons/caprine.png" width="32" height="32" alt="Caprine"></a> | **[Caprine](https://github.com/sindresorhus/caprine#features)** | Elegant Facebook Messenger desktop app. | `JavaScript` | [Source](https://github.com/sindresorhus/caprine#features) | `MIT` |
| <a href="https://github.com/danielbuechele/goofy"><img src="./icons/project-icons/goofy.png" width="32" height="32" alt="Goofy"></a> | **[Goofy](https://github.com/danielbuechele/goofy)** | Unofficial Facebook Messenger client. | `JavaScript` | [Source](https://github.com/danielbuechele/goofy) | `MIT` |
| <a href="https://github.com/Swiftodon/Leviathan"><img src="./icons/project-icons/leviathan.png" width="32" height="32" alt="Leviathan"></a> | **[Leviathan](https://github.com/Swiftodon/Leviathan)** | Leviathan is a iOS and macOS client application for the Mastodon social network. | `Swift` | [Source](https://github.com/Swiftodon/Leviathan) | `MIT` |
| <a href="https://github.com/rsms/fb-mac-messenger"><img src="./icons/project-icons/messenger.png" width="32" height="32" alt="Messenger"></a> | **[Messenger](https://github.com/rsms/fb-mac-messenger)** | macOS app wrapping Facebook's Messenger for desktop. | `Objective-C` | [Source](https://github.com/rsms/fb-mac-messenger) | `MIT` |
| <a href="https://github.com/producthunt/producthunt-osx"><img src="./icons/project-icons/product-hunt.png" width="32" height="32" alt="Product Hunt"></a> | **[Product Hunt](https://github.com/producthunt/producthunt-osx)** | share and discover your favorite new products and applications. | `Swift` | [Source](https://github.com/producthunt/producthunt-osx) | `MIT` |
| <a href="https://github.com/1000ch/quail"><img src="./icons/project-icons/quail.png" width="32" height="32" alt="Quail"></a> | **[Quail](https://github.com/1000ch/quail)** | Unofficial [esa](https://esa.io/) app. | `JavaScript` | [Source](https://github.com/1000ch/quail) | `MIT` |
| <a href="https://github.com/terkelg/ramme"><img src="./icons/project-icons/ramme.png" width="32" height="32" alt="Ramme"></a> | **[Ramme](https://github.com/terkelg/ramme)** | Unofficial Instagram Desktop App. | `JavaScript` | [Source](https://github.com/terkelg/ramme) | `MIT` |
| <a href="https://github.com/Dimillian/RedditOS"><img src="./icons/project-icons/redditos.png" width="32" height="32" alt="RedditOS"></a> | **[RedditOS](https://github.com/Dimillian/RedditOS)** | A SwiftUI Reddit client for macOS. | `Swift` | [Source](https://github.com/Dimillian/RedditOS) | `MIT` |
| <a href="https://github.com/KeliCheng/Simpo"><img src="./icons/project-icons/simpo.png" width="32" height="32" alt="Simpo"></a> | **[Simpo](https://github.com/KeliCheng/Simpo)** | macOS menubar app to post status quickly. | `Swift` | [Source](https://github.com/KeliCheng/Simpo) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="streaming"></a>
### 📡 Streaming

> Live broadcasting suites, desktop capture utilities, and livestream management apps.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/michealparks/galeri"><img src="./icons/project-icons/galeri.png" width="32" height="32" alt="Galeri"></a> | **[Galeri](https://github.com/michealparks/galeri)** | Perpetual artwork streaming app. | `JavaScript` | [Source](https://github.com/michealparks/galeri) | `MIT` |
| <a href="https://obsproject.com"><img src="./icons/project-icons/obs-studio.png" width="32" height="32" alt="OBS Studio"></a> | **[OBS Studio](https://obsproject.com)** | Free and open-source software for video recording and live streaming with full macOS ScreenCaptureKit. | `C` | [Website](https://obsproject.com) • [Source](https://github.com/obsproject/obs-studio) | `GPL-2.0` |

[⬆ Back to Top](#table-of-contents)


<a id="system"></a>
### ⚙️ System

> System diagnostics, hardware monitors, uninstallation cleaners, and maintenance apps.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/raphaelhanneken/apple-juice"><img src="./icons/project-icons/apple-juice.png" width="32" height="32" alt="Apple Juice"></a> | **[Apple Juice](https://github.com/raphaelhanneken/apple-juice)** | Advanced battery gauge for macOS. | `Swift` | [Source](https://github.com/raphaelhanneken/apple-juice) | `MIT` |
| <a href="https://github.com/AppPolice/AppPolice"><img src="./icons/project-icons/apppolice.png" width="32" height="32" alt="AppPolice"></a> | **[AppPolice](https://github.com/AppPolice/AppPolice)** | App for macOS with a minimalistic UI which lets you quickly throttle down the CPU usage of any running process. | `Objective-C` | [Source](https://github.com/AppPolice/AppPolice) | `MIT` |
| <a href="https://github.com/Kevin-De-Koninck/Clean-Me"><img src="./icons/project-icons/clean-me.png" width="32" height="32" alt="Clean-Me"></a> | **[Clean-Me](https://github.com/Kevin-De-Koninck/Clean-Me)** | Small macOS app that acts as a system cleaner (logs, cache, ...). | `Swift` | [Source](https://github.com/Kevin-De-Koninck/Clean-Me) | `MIT` |
| <a href="https://github.com/macmade/Diagnostics"><img src="./icons/project-icons/diagnostics.png" width="32" height="32" alt="Diagnostics"></a> | **[Diagnostics](https://github.com/macmade/Diagnostics)** | Diagnostics is an application displaying the diagnostic reports from applications on macOS. | `Swift` | [Source](https://github.com/macmade/Diagnostics) | `MIT` |
| <a href="https://github.com/Eun/DisableMonitor"><img src="./icons/project-icons/disablemonitor.png" width="32" height="32" alt="DisableMonitor"></a> | **[DisableMonitor](https://github.com/Eun/DisableMonitor)** | Easily disable or enable a monitor on your Mac. | `Objective-C` | [Source](https://github.com/Eun/DisableMonitor) | `MIT` |
| <a href="https://github.com/DanielStormApps/Fanny"><img src="./icons/project-icons/fanny.png" width="32" height="32" alt="Fanny"></a> | **[Fanny](https://github.com/DanielStormApps/Fanny)** | Monitor your Mac's fan speed and CPU temperature from your Notification Center. | `Objective-C` | [Source](https://github.com/DanielStormApps/Fanny) | `MIT` |
| <a href="https://brew.sh"><img src="./icons/project-icons/homebrew.png" width="32" height="32" alt="Homebrew"></a> | **[Homebrew](https://brew.sh)** | The missing package manager for macOS and Linux, installing software packages from the CLI. | `Ruby` | [Website](https://brew.sh) • [Source](https://github.com/Homebrew/brew) | `BSD-2-Clause` |
| <a href="https://github.com/jwise/HoRNDIS"><img src="./icons/project-icons/horndis.png" width="32" height="32" alt="HoRNDIS"></a> | **[HoRNDIS](https://github.com/jwise/HoRNDIS)** | Android USB tethering driver for macOS. | `C++` | [Source](https://github.com/jwise/HoRNDIS) | `MIT` |
| <a href="https://github.com/brianmichel/Juice"><img src="./icons/project-icons/juice.png" width="32" height="32" alt="Juice"></a> | **[Juice](https://github.com/brianmichel/Juice)** | Make your battery information a bit more interesting. | `Swift` | [Source](https://github.com/brianmichel/Juice) | `MIT` |
| <a href="https://github.com/newmarcel/KeepingYouAwake"><img src="./icons/project-icons/keepingyouawake.png" width="32" height="32" alt="KeepingYouAwake"></a> | **[KeepingYouAwake](https://github.com/newmarcel/KeepingYouAwake)** | Prevents your Mac from going to sleep. | `Objective-C` | [Source](https://github.com/newmarcel/KeepingYouAwake) | `MIT` |
| <a href="https://www.keka.io"><img src="./icons/project-icons/keka.png" width="32" height="32" alt="Keka"></a> | **[Keka](https://www.keka.io)** | Powerful file archiver for macOS supporting 7Z, ZIP, TAR, GZ, and password protection. | `Objective-C` | [Website](https://www.keka.io) • [Source](https://github.com/aonez/Keka) | `GPL-2.0` |
| <a href="https://max-langer.com/Latest"><img src="./icons/project-icons/latest.png" width="32" height="32" alt="Latest"></a> | **[Latest](https://max-langer.com/Latest)** | Native small utility that checks your installed Mac applications for available updates. | `Swift` | [Website](https://max-langer.com/Latest) • [Source](https://github.com/mangerlahn/Latest) | `MIT` |
| <a href="https://github.com/BonzaiThePenguin/Loading"><img src="./icons/project-icons/loading.png" width="32" height="32" alt="Loading"></a> | **[Loading](https://github.com/BonzaiThePenguin/Loading)** | Simple network activity monitor for macOS. | `Objective-C` | [Source](https://github.com/BonzaiThePenguin/Loading) | `MIT` |
| <a href="https://github.com/LumingYin/macOSLucidaGrande/releases"><img src="./icons/project-icons/macoslucidagrande.png" width="32" height="32" alt="macOSLucidaGrande"></a> | **[macOSLucidaGrande](https://github.com/LumingYin/macOSLucidaGrande/releases)** | A small utility to set Lucida Grande as your Mac's system UI font. | `Objective-C` | [Website](https://github.com/LumingYin/macOSLucidaGrande/releases) • [Source](https://github.com/LumingYin/macOSLucidaGrande) | `MIT` |
| <a href="https://github.com/MonitorControl/MonitorControl"><img src="./icons/project-icons/monitorcontrol.png" width="32" height="32" alt="MonitorControl"></a> | **[MonitorControl](https://github.com/MonitorControl/MonitorControl)** | Control external display brightness and volume using native Apple keyboard keys or slider controls. | `Swift` | [Source](https://github.com/MonitorControl/MonitorControl) | `MIT` |
| <a href="https://github.com/KrauseFx/overkill-for-mac"><img src="./icons/project-icons/overkill.png" width="32" height="32" alt="Overkill"></a> | **[Overkill](https://github.com/KrauseFx/overkill-for-mac)** | Stop iTunes from opening when you connect your iPhone. | `Swift` | [Source](https://github.com/KrauseFx/overkill-for-mac) | `MIT` |
| <a href="https://github.com/alienator88/Pearcleaner"><img src="./icons/project-icons/pearcleaner.png" width="32" height="32" alt="Pearcleaner"></a> | **[Pearcleaner](https://github.com/alienator88/Pearcleaner)** | Open-source Mac app uninstaller inspired by AppCleaner, written cleanly in native SwiftUI. | `Swift` | [Source](https://github.com/alienator88/Pearcleaner) | `GPL-3.0` |
| <a href="https://github.com/ProfileCreator/ProfileCreator"><img src="./icons/project-icons/profilecreator.png" width="32" height="32" alt="ProfileCreator"></a> | **[ProfileCreator](https://github.com/ProfileCreator/ProfileCreator)** | macOS Application to create standard or customized configuration profiles. | `Objective-C` | [Source](https://github.com/ProfileCreator/ProfileCreator) | `MIT` |
| <a href="https://github.com/sveinbjornt/Sloth"><img src="./icons/project-icons/sloth.png" width="32" height="32" alt="Sloth"></a> | **[Sloth](https://github.com/sveinbjornt/Sloth)** | Sloth is an macOS application that displays a list of all open files and sockets in use by all running applications on your system. | `Objective-C` | [Source](https://github.com/sveinbjornt/Sloth) | `MIT` |
| <a href="https://github.com/exelban/stats"><img src="./icons/project-icons/stats.png" width="32" height="32" alt="Stats"></a> | **[Stats](https://github.com/exelban/stats)** | Menu bar system monitor showing CPU, GPU, memory, disks, sensors, battery, and network speeds. | `Swift` | [Source](https://github.com/exelban/stats) | `MIT` |
| <a href="https://github.com/rugarciap/Turbo-Boost-Switcher"><img src="./icons/project-icons/turbo-boost-switcher.png" width="32" height="32" alt="Turbo Boost Switcher"></a> | **[Turbo Boost Switcher](https://github.com/rugarciap/Turbo-Boost-Switcher)** | Turbo Boost Switcher is a little application for Mac computers that allows to enable and/or disable the Turbo Boost feature. | `Objective-C` | [Source](https://github.com/rugarciap/Turbo-Boost-Switcher) | `MIT` |
| <a href="https://github.com/DeromirNeves/DockSeparator"><img src="./icons/project-icons/verticalbar.png" width="32" height="32" alt="VerticalBar"></a> | **[VerticalBar](https://github.com/DeromirNeves/DockSeparator)** | macOS application to add a vertical bar to Dock. | `Swift` | [Source](https://github.com/DeromirNeves/DockSeparator) | `MIT` |
| <a href="https://www.wireshark.org"><img src="./icons/project-icons/wireshark.svg" width="32" height="32" alt="Wireshark"></a> | **[Wireshark](https://www.wireshark.org)** | Wireshark is the world’s foremost and widely-used network protocol analyzer for macOS and multiple platforms. | `C` | [Website](https://www.wireshark.org) • [Source](https://gitlab.com/wireshark/wireshark/-/tree/master) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="terminal"></a>
### 📺 Terminal

> Modern terminal emulators, shell accelerators, multiplexers, and prompt personalizers.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://alacritty.org"><img src="./icons/project-icons/alacritty.png" width="32" height="32" alt="Alacritty"></a> | **[Alacritty](https://alacritty.org)** | Cross-platform, GPU-accelerated terminal emulator focused on simplicity and maximum performance. | `Rust` | [Website](https://alacritty.org) • [Source](https://github.com/alacritty/alacritty) | `Apache-2.0` |
| <a href="https://github.com/ishuah/bifrost"><img src="./icons/project-icons/bifrost.png" width="32" height="32" alt="Bifrost"></a> | **[Bifrost](https://github.com/ishuah/bifrost)** | A tiny terminal emulator for serial port communication (macOS/Linux). | `Go` | [Source](https://github.com/ishuah/bifrost) | `MIT` |
| <a href="https://github.com/macmade/Console"><img src="./icons/project-icons/console.png" width="32" height="32" alt="Console"></a> | **[Console](https://github.com/macmade/Console)** | macOS console application. | `Swift` | [Source](https://github.com/macmade/Console) | `MIT` |
| <a href="https://ghostty.org"><img src="./icons/project-icons/ghostty.png" width="32" height="32" alt="Ghostty"></a> | **[Ghostty](https://ghostty.org)** | Fast, feature-rich, and cross-platform terminal emulator leveraging native macOS UI and GPU acceleration. | `Zig` | [Website](https://ghostty.org) • [Source](https://github.com/ghostty-org/ghostty) | `MIT` |
| <a href="https://github.com/vercel/hyper"><img src="./icons/project-icons/hyper.png" width="32" height="32" alt="Hyper"></a> | **[Hyper](https://github.com/vercel/hyper)** | Terminal built on web technologies. | `JavaScript` | [Source](https://github.com/vercel/hyper) | `MIT` |
| <a href="https://iterm2.com"><img src="./icons/project-icons/iterm2.png" width="32" height="32" alt="iTerm2"></a> | **[iTerm2](https://iterm2.com)** | Full-featured macOS terminal emulator with split panes, search, autocomplete, and tmux integration. | `Objective-C` | [Website](https://iterm2.com) • [Source](https://github.com/gnachman/iTerm2) | `GPL-2.0` |
| <a href="https://sw.kovidgoyal.net/kitty"><img src="./icons/project-icons/kitty.png" width="32" height="32" alt="Kitty"></a> | **[Kitty](https://sw.kovidgoyal.net/kitty)** | Cross-platform, fast, feature-rich, GPU-based terminal emulator with graphics support. | `Python` | [Website](https://sw.kovidgoyal.net/kitty) • [Source](https://github.com/kovidgoyal/kitty) | `GPL-3.0` |
| <a href="https://github.com/es-kumagai/OpenTerminal"><img src="./icons/project-icons/openterminal.png" width="32" height="32" alt="OpenTerminal"></a> | **[OpenTerminal](https://github.com/es-kumagai/OpenTerminal)** | App for macOS that opens a new Finder window and changes the current directory to the folder launched by the app. | `Swift` | [Source](https://github.com/es-kumagai/OpenTerminal) | `MIT` |
| <a href="https://starship.rs"><img src="./icons/project-icons/starship.png" width="32" height="32" alt="Starship"></a> | **[Starship](https://starship.rs)** | Minimal, blazing-fast, and infinitely customizable cross-shell prompt for any shell. | `Rust` | [Website](https://starship.rs) • [Source](https://github.com/starship/starship) | `ISC` |
| <a href="https://github.com/Eugeny/tabby"><img src="./icons/project-icons/tabby.png" width="32" height="32" alt="Tabby"></a> | **[Tabby](https://github.com/Eugeny/tabby)** | Powerful cross-platform terminal emulator, featuring a modern GUI, and offering SSH, serial, Telnet, and SCP client support. | `TypeScript` | [Source](https://github.com/Eugeny/tabby) | `MIT` |
| <a href="https://gnome-terminator.org"><img src="./icons/project-icons/terminator.png" width="32" height="32" alt="Terminator"></a> | **[Terminator](https://gnome-terminator.org)** | Terminal emulator that lets you open multiple GNOME terminals in one window. | `Python` | [Website](https://gnome-terminator.org) • [Source](https://github.com/gnome-terminator/terminator) | `MIT` |
| <a href="https://github.com/mczachurski/wallpapper"><img src="./icons/project-icons/wallpapper.png" width="32" height="32" alt="wallpapper"></a> | **[wallpapper](https://github.com/mczachurski/wallpapper)** | wallpapper is a console application for creating dynamic wallpapers for Mojave. | `Swift` | [Source](https://github.com/mczachurski/wallpapper) | `MIT` |
| <a href="https://wezfurlong.org/wezterm"><img src="./icons/project-icons/wezterm.png" width="32" height="32" alt="WezTerm"></a> | **[WezTerm](https://wezfurlong.org/wezterm)** | GPU-accelerated cross-platform terminal emulator and multiplexer written in Rust. | `Rust` | [Website](https://wezfurlong.org/wezterm) • [Source](https://github.com/wez/wezterm) | `MIT` |
| <a href="https://zellij.dev"><img src="./icons/project-icons/zellij.png" width="32" height="32" alt="Zellij"></a> | **[Zellij](https://zellij.dev)** | Terminal workspace manager and multiplexer with built-in layout engines and plugin architecture. | `Rust` | [Website](https://zellij.dev) • [Source](https://github.com/zellij-org/zellij) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="touch-bar"></a>
### 🎚️ Touch Bar

> MacBook Pro Touch Bar customization utilities, widgets, and mini tactile applets.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/xzzz9097/Muse"><img src="./icons/project-icons/muse.png" width="32" height="32" alt="Muse"></a> | **[Muse](https://github.com/xzzz9097/Muse)** | Spotify controller with TouchBar support. | `Swift` | [Source](https://github.com/xzzz9097/Muse) | `MIT` |
| <a href="https://github.com/toxblh/MTMR"><img src="./icons/project-icons/mytouchbarmyrules.png" width="32" height="32" alt="MyTouchbarMyRules"></a> | **[MyTouchbarMyRules](https://github.com/toxblh/MTMR)** | App to customize your Touch Bar as you want. | `Swift` | [Source](https://github.com/toxblh/MTMR) | `MIT` |
| <a href="https://pock.app"><img src="./icons/project-icons/pock.png" width="32" height="32" alt="Pock"></a> | **[Pock](https://pock.app)** | Display macOS Dock in Touch Bar. | `Swift` | [Website](https://pock.app) • [Source](https://github.com/pock/pock) | `MIT` |
| <a href="https://github.com/touchbar/Touch-Bar-Preview"><img src="./icons/project-icons/touch-bar-preview.png" width="32" height="32" alt="Touch Bar Preview"></a> | **[Touch Bar Preview](https://github.com/touchbar/Touch-Bar-Preview)** | Small application to display your designs on the Touch Bar of the new MacBook Pro. | `Swift` | [Source](https://github.com/touchbar/Touch-Bar-Preview) | `MIT` |
| <a href="https://github.com/sindresorhus/touch-bar-simulator"><img src="./icons/project-icons/touch-bar-simulator.png" width="32" height="32" alt="Touch Bar Simulator"></a> | **[Touch Bar Simulator](https://github.com/sindresorhus/touch-bar-simulator)** | Use the Touch Bar on any Mac. | `Swift` | [Source](https://github.com/sindresorhus/touch-bar-simulator) | `MIT` |
| <a href="https://github.com/ilyalesik/touch-emoji"><img src="./icons/project-icons/touch-emoji.png" width="32" height="32" alt="Touch Emoji"></a> | **[Touch Emoji](https://github.com/ilyalesik/touch-emoji)** | Emoji picker for MacBook Pro Touch Bar. | `Swift` | [Source](https://github.com/ilyalesik/touch-emoji) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="utilities"></a>
### 🛠️ Utilities

> Everyday Mac utilities, mouse accelerators, audio routers, and desktop tools.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/mortenjust/androidtool-mac"><img src="./icons/project-icons/android-tool-for-mac.png" width="32" height="32" alt="Android tool for Mac"></a> | **[Android tool for Mac](https://github.com/mortenjust/androidtool-mac)** | One-click screenshots, video recordings, app installation for iOS and Android | `Swift` | [Source](https://github.com/mortenjust/androidtool-mac) | `MIT` |
| <a href="https://github.com/ivoronin/ArchiveMounter"><img src="./icons/project-icons/archivemounter.png" width="32" height="32" alt="ArchiveMounter"></a> | **[ArchiveMounter](https://github.com/ivoronin/ArchiveMounter)** | Mounts archives like disk images. | `Swift` | [Source](https://github.com/ivoronin/ArchiveMounter) | `MIT` |
| <a href="https://www.balena.io/etcher"><img src="./icons/project-icons/balena-etcher.png" width="32" height="32" alt="Balena Etcher"></a> | **[Balena Etcher](https://www.balena.io/etcher)** | Flash OS images to SD cards & USB drives, safely and easily. | `TypeScript` | [Website](https://www.balena.io/etcher) • [Source](https://github.com/balena-io/etcher) | `MIT` |
| <a href="https://github.com/beardedspice/beardedspice"><img src="./icons/project-icons/beardedspice.png" width="32" height="32" alt="BeardedSpice"></a> | **[BeardedSpice](https://github.com/beardedspice/beardedspice)** | Control web based media players with the media keys found on Mac keyboards. | `Objective-C` | [Source](https://github.com/beardedspice/beardedspice) | `MIT` |
| <a href="https://github.com/jnsdrtlf/bitwarden-menubar"><img src="./icons/project-icons/bitwarden-menu.svg" width="32" height="32" alt="Bitwarden Menu"></a> | **[Bitwarden Menu](https://github.com/jnsdrtlf/bitwarden-menubar)** | Bitwarden Password Manager in your menu bar | `TypeScript` | [Source](https://github.com/jnsdrtlf/bitwarden-menubar) | `MIT` |
| <a href="https://github.com/buttercup/buttercup-desktop"><img src="./icons/project-icons/buttercup-desktop.png" width="32" height="32" alt="Buttercup Desktop"></a> | **[Buttercup Desktop](https://github.com/buttercup/buttercup-desktop)** | Secure password manager for mac and other platforms. | `JavaScript` | [Source](https://github.com/buttercup/buttercup-desktop) | `MIT` |
| <a href="https://calibre-ebook.com"><img src="./icons/project-icons/calibre.png" width="32" height="32" alt="calibre"></a> | **[calibre](https://calibre-ebook.com)** | cross platform e-book manager. | `Python` | [Website](https://calibre-ebook.com) • [Source](https://github.com/kovidgoyal/calibre) | `MIT` |
| <a href="https://github.com/mipstian/catch/"><img src="./icons/project-icons/catch.png" width="32" height="32" alt="Catch"></a> | **[Catch](https://github.com/mipstian/catch/)** | Catch: Broadcatching made easy. | `Swift` | [Source](https://github.com/mipstian/catch/) | `MIT` |
| <a href="https://apps.apple.com/app/clear-clipboard-text-format/id1322855232"><img src="./icons/project-icons/clear-clipboard-text-format.png" width="32" height="32" alt="Clear Clipboard Text Format"></a> | **[Clear Clipboard Text Format](https://apps.apple.com/app/clear-clipboard-text-format/id1322855232)** | Easily clear the format of your clipboard text with Clear Clipboard Text Format. | `Objective-C` | [Website](https://apps.apple.com/app/clear-clipboard-text-format/id1322855232) • [Source](https://github.com/LumingYin/ClipboardClear) | `MIT` |
| <a href="https://github.com/fulldecent/corelocationcli"><img src="./icons/project-icons/corelocationcli.png" width="32" height="32" alt="CoreLocationCLI"></a> | **[CoreLocationCLI](https://github.com/fulldecent/corelocationcli)** | Get the physical location of your device and prints it to standard output | `Swift` | [Source](https://github.com/fulldecent/corelocationcli) | `MIT` |
| <a href="https://github.com/ekreutz/CornerCal"><img src="./icons/project-icons/cornercal.png" width="32" height="32" alt="CornerCal"></a> | **[CornerCal](https://github.com/ekreutz/CornerCal)** | Simple, clean calendar and clock app for macOS. | `Swift` | [Source](https://github.com/ekreutz/CornerCal) | `MIT` |
| <a href="https://github.com/HR/Crypter"><img src="./icons/project-icons/crypter.png" width="32" height="32" alt="Crypter"></a> | **[Crypter](https://github.com/HR/Crypter)** | Crypter is an innovative, convenient and secure cross-platform crypto app that simplifies secure password generation and management by requiring you to only remember one bit, the MasterPass. | `JavaScript` | [Source](https://github.com/HR/Crypter) | `MIT` |
| <a href="https://cyberduck.io"><img src="./icons/project-icons/cyberduck.png" width="32" height="32" alt="Cyberduck"></a> | **[Cyberduck](https://cyberduck.io)** | Libre cloud storage browser for macOS with support for FTP, SFTP, WebDAV, Amazon S3, and OpenStack. | `Java` | [Website](https://cyberduck.io) • [Source](https://github.com/iterate-ch/cyberduck) | `GPL-3.0` |
| <a href="https://github.com/josejuanqm/ECheck"><img src="./icons/project-icons/echeck.png" width="32" height="32" alt="ECheck"></a> | **[ECheck](https://github.com/josejuanqm/ECheck)** | Small tool to validate epub files for macOS. | `Swift` | [Source](https://github.com/josejuanqm/ECheck) | `MIT` |
| <a href="https://adequate.systems"><img src="./icons/project-icons/flying-carpet.png" width="32" height="32" alt="Flying Carpet"></a> | **[Flying Carpet](https://adequate.systems)** | cross-platform file transfer over ad-hoc wifi, like AirDrop but for Mac/Windows/Linux. | `Go` | [Website](https://adequate.systems) • [Source](https://github.com/spieglt/flyingcarpet) | `MIT` |
| <a href="https://github.com/jhspetersson/fselect"><img src="./icons/project-icons/fselect.png" width="32" height="32" alt="fselect"></a> | **[fselect](https://github.com/jhspetersson/fselect)** | Command-line tool to search files with SQL syntax. | `Rust` | [Source](https://github.com/jhspetersson/fselect) | `MIT` |
| <a href="https://github.com/thecatalinstan/Funky"><img src="./icons/project-icons/funky.png" width="32" height="32" alt="Funky"></a> | **[Funky](https://github.com/thecatalinstan/Funky)** | Easily toggle the function key on your Mac on a per app basis. | `Objective-C` | [Source](https://github.com/thecatalinstan/Funky) | `MIT` |
| <a href="https://grandperspectiv.sourceforge.net"><img src="./icons/project-icons/grandperspective.svg" width="32" height="32" alt="GrandPerspective"></a> | **[GrandPerspective](https://grandperspectiv.sourceforge.net)** | Small utility for visualizing disk usage using tree maps. | `Objective-C` | [Website](https://grandperspectiv.sourceforge.net) • [Source](https://git.code.sf.net/p/grandperspectiv/source) | `MIT` |
| <a href="https://github.com/zenangst/Gray"><img src="./icons/project-icons/gray.png" width="32" height="32" alt="Gray"></a> | **[Gray](https://github.com/zenangst/Gray)** | Pick between the light appearance and the dark appearance on a per-app basis with the click of a button | `Swift` | [Source](https://github.com/zenangst/Gray) | `MIT` |
| <a href="https://brew.sh"><img src="./icons/project-icons/homebrew-cask.png" width="32" height="32" alt="homebrew-cask"></a> | **[homebrew-cask](https://brew.sh)** | A CLI workflow for the administration of macOS applications distributed as binaries | `Ruby` | [Website](https://brew.sh) • [Source](https://github.com/Homebrew/homebrew-cask) | `MIT` |
| <a href="https://github.com/alessiomaffeis/iOScanX"><img src="./icons/project-icons/ioscanx.png" width="32" height="32" alt="iOScanX"></a> | **[iOScanX](https://github.com/alessiomaffeis/iOScanX)** | Cocoa application for semi-automated iOS app analysis and evaluation. | `Objective-C` | [Source](https://github.com/alessiomaffeis/iOScanX) | `MIT` |
| <a href="https://github.com/keeweb/keeweb"><img src="./icons/project-icons/keeweb.png" width="32" height="32" alt="KeeWeb"></a> | **[KeeWeb](https://github.com/keeweb/keeweb)** | Cross-platform password manager compatible with KeePass. | `JavaScript` | [Source](https://github.com/keeweb/keeweb) | `MIT` |
| <a href="https://github.com/vishaltelangre/Kyapchar"><img src="./icons/project-icons/kyapchar.png" width="32" height="32" alt="Kyapchar"></a> | **[Kyapchar](https://github.com/vishaltelangre/Kyapchar)** | Simple screen and microphone audio recorder for macOS. | `Swift` | [Source](https://github.com/vishaltelangre/Kyapchar) | `MIT` |
| <a href="https://github.com/alin23/lunar"><img src="./icons/project-icons/lunar.png" width="32" height="32" alt="Lunar"></a> | **[Lunar](https://github.com/alin23/lunar)** | Intelligent adaptive brightness for your external displays. | `Swift` | [Source](https://github.com/alin23/lunar) | `MIT` |
| <a href="https://github.com/dragstor/mac-sound-fix"><img src="./icons/project-icons/mac-sound-fix.png" width="32" height="32" alt="mac-sound-fix"></a> | **[mac-sound-fix](https://github.com/dragstor/mac-sound-fix)** | Mac Sound Re-Enabler. | `Swift` | [Source](https://github.com/dragstor/mac-sound-fix) | `MIT` |
| <a href="https://macpacker.app"><img src="./icons/project-icons/macpacker.png" width="32" height="32" alt="MacPacker"></a> | **[MacPacker](https://macpacker.app)** | Archive manager for macOS. Preview (nested) archives without extracting them. Extract single files. | `Swift` | [Website](https://macpacker.app) • [Source](https://github.com/sarensw/MacPacker/) | `MIT` |
| <a href="https://github.com/MacPass/MacPass"><img src="./icons/project-icons/macpass.png" width="32" height="32" alt="MacPass"></a> | **[MacPass](https://github.com/MacPass/MacPass)** | Native macOS KeePass client. | `Objective-C` | [Source](https://github.com/MacPass/MacPass) | `MIT` |
| <a href="https://github.com/shincurry/Maria"><img src="./icons/project-icons/maria.png" width="32" height="32" alt="Maria"></a> | **[Maria](https://github.com/shincurry/Maria)** | macOS native app/widget for aria2 download tool. | `Swift` | [Source](https://github.com/shincurry/Maria) | `MIT` |
| <a href="https://github.com/MemeMaker/Meme-Maker-Mac"><img src="./icons/project-icons/meme-maker.png" width="32" height="32" alt="Meme Maker"></a> | **[Meme Maker](https://github.com/MemeMaker/Meme-Maker-Mac)** | Meme Maker macOS application for meme creation. | `Swift` | [Source](https://github.com/MemeMaker/Meme-Maker-Mac) | `MIT` |
| <a href="https://github.com/NullPointerDepressiveDisorder/MiddleDrag"><img src="./icons/project-icons/middledrag.png" width="32" height="32" alt="MiddleDrag"></a> | **[MiddleDrag](https://github.com/NullPointerDepressiveDisorder/MiddleDrag)** | Three-finger trackpad gestures for middle-click and middle-drag. | `Swift` | [Source](https://github.com/NullPointerDepressiveDisorder/MiddleDrag) | `MIT` |
| <a href="https://github.com/IngmarStein/Monolingual"><img src="./icons/project-icons/monolingual.png" width="32" height="32" alt="Monolingual"></a> | **[Monolingual](https://github.com/IngmarStein/Monolingual)** | Remove unnecessary language resources from macOS | `Swift` | [Source](https://github.com/IngmarStein/Monolingual) | `MIT` |
| <a href="https://github.com/Caldis/Mos"><img src="./icons/project-icons/mos.svg" width="32" height="32" alt="Mos"></a> | **[Mos](https://github.com/Caldis/Mos)** | Smooth your mouse's scrolling and reverse the mouse scroll direction | `Swift` | [Source](https://github.com/Caldis/Mos) | `MIT` |
| <a href="https://nixos.org/explore.html"><img src="./icons/project-icons/nix-package-manager.svg" width="32" height="32" alt="nix-package-manager"></a> | **[nix-package-manager](https://nixos.org/explore.html)** | Nix is a reproducible package manager alternative to Homebrew, with over 80,000 packages. | `c++` | [Website](https://nixos.org/explore.html) • [Source](https://github.com/NixOS/nix) | `MIT` |
| <a href="https://nmap.org"><img src="./icons/project-icons/nmap.svg" width="32" height="32" alt="Nmap"></a> | **[Nmap](https://nmap.org)** | Nmap - the Network Mapper. | `C++` | [Website](https://nmap.org) • [Source](https://github.com/nmap/nmap) | `MIT` |
| <a href="https://github.com/jariz/Noti/"><img src="./icons/project-icons/noti.svg" width="32" height="32" alt="Noti"></a> | **[Noti](https://github.com/jariz/Noti/)** | Receive Android notifications on your mac (with PushBullet). | `Swift` | [Source](https://github.com/jariz/Noti/) | `MIT` |
| <a href="https://github.com/nvm-sh/nvm"><img src="./icons/project-icons/nvm.svg" width="32" height="32" alt="NVM"></a> | **[NVM](https://github.com/nvm-sh/nvm)** | Node Version Manager. | `Shell` | [Source](https://github.com/nvm-sh/nvm) | `MIT` |
| <a href="https://dortania.github.io/OpenCore-Legacy-Patcher"><img src="./icons/project-icons/opencore-legacy-patcher.svg" width="32" height="32" alt="OpenCore Legacy Patcher"></a> | **[OpenCore Legacy Patcher](https://dortania.github.io/OpenCore-Legacy-Patcher)** | OpenCore Legacy Patcher is a tool for installing new MacOS versions on legacy macs. | `Python` | [Website](https://dortania.github.io/OpenCore-Legacy-Patcher) • [Source](https://github.com/dortania/OpenCore-Legacy-Patcher) | `MIT` |
| <a href="https://openrocket.info"><img src="./icons/project-icons/openrocket.svg" width="32" height="32" alt="OpenRocket"></a> | **[OpenRocket](https://openrocket.info)** | OpenRocket is a cross-platform utility tool to model and simulate model rockets and their flight characteristics. | `Java` | [Website](https://openrocket.info) • [Source](https://github.com/openrocket/openrocket) | `MIT` |
| <a href="https://github.com/padloc/padloc"><img src="./icons/project-icons/padlock.svg" width="32" height="32" alt="Padlock"></a> | **[Padlock](https://github.com/padloc/padloc)** | A minimal, open source password manager for macOS. | `JavaScript` | [Source](https://github.com/padloc/padloc) | `MIT` |
| <a href="https://github.com/sidneys/pb-for-desktop"><img src="./icons/project-icons/pb-for-desktop.svg" width="32" height="32" alt="PB for Desktop"></a> | **[PB for Desktop](https://github.com/sidneys/pb-for-desktop)** | Receive native push notifications on macOS, Windows and Linux. | `JavaScript` | [Source](https://github.com/sidneys/pb-for-desktop) | `MIT` |
| <a href="https://peazip.github.io"><img src="./icons/project-icons/peazip.svg" width="32" height="32" alt="PeaZip"></a> | **[PeaZip](https://peazip.github.io)** | Free file archiver utility and open source file compression and encryption tool supporting 200+ formats. | `pascal` | [Website](https://peazip.github.io) • [Source](https://github.com/peazip/PeaZip) | `MIT` |
| <a href="https://github.com/cemolcay/PercentCalculator"><img src="./icons/project-icons/percentcalculator.svg" width="32" height="32" alt="PercentCalculator"></a> | **[PercentCalculator](https://github.com/cemolcay/PercentCalculator)** | A menu bar application that calculates percents. | `Swift` | [Source](https://github.com/cemolcay/PercentCalculator) | `MIT` |
| <a href="https://github.com/hisaac/PlainPasta"><img src="./icons/project-icons/plain-pasta.svg" width="32" height="32" alt="Plain Pasta"></a> | **[Plain Pasta](https://github.com/hisaac/PlainPasta)** | Plaintextify your clipboard | `Swift` | [Source](https://github.com/hisaac/PlainPasta) | `MIT` |
| <a href="https://github.com/Piero24/PlugNPlayMac"><img src="./icons/project-icons/plugnplaymac.svg" width="32" height="32" alt="PlugNPlayMac"></a> | **[PlugNPlayMac](https://github.com/Piero24/PlugNPlayMac)** | A script to automate tasks when connect a device to your Mac | `Shell` | [Source](https://github.com/Piero24/PlugNPlayMac) | `MIT` |
| <a href="https://github.com/powershell/powershell"><img src="./icons/project-icons/powershell.svg" width="32" height="32" alt="PowerShell"></a> | **[PowerShell](https://github.com/powershell/powershell)** | PowerShell is a cross-platform automation and configuration tool/framework that works well with your existing tools. | `C#` | [Source](https://github.com/powershell/powershell) | `MIT` |
| <a href="https://swiftyfinch.github.io/en/2021-03-09-rugby-story"><img src="./icons/project-icons/rugby.svg" width="32" height="32" alt="Rugby"></a> | **[Rugby](https://swiftyfinch.github.io/en/2021-03-09-rugby-story)** | 🏈 Cache CocoaPods for faster rebuild and indexing Xcode project. | `Swift` | [Website](https://swiftyfinch.github.io/en/2021-03-09-rugby-story) • [Source](https://github.com/swiftyfinch/Rugby) | `MIT` |
| <a href="https://github.com/maxogden/screencat"><img src="./icons/project-icons/screencat.svg" width="32" height="32" alt="ScreenCat"></a> | **[ScreenCat](https://github.com/maxogden/screencat)** | ScreenCat is a screen sharing + remote collaboration application. | `JavaScript` | [Source](https://github.com/maxogden/screencat) | `MIT` |
| <a href="https://screentranslate.filient.ai"><img src="./icons/project-icons/screentranslate.svg" width="32" height="32" alt="ScreenTranslate"></a> | **[ScreenTranslate](https://screentranslate.filient.ai)** | Capture any area or select text to translate instantly, fully on-device with Apple Vision OCR and Apple Translation. | `Swift` | [Website](https://screentranslate.filient.ai) • [Source](https://github.com/hcmhcs/screenTranslate) | `MIT` |
| <a href="https://github.com/dteoh/SlowQuitApps"><img src="./icons/project-icons/slowquitapps.svg" width="32" height="32" alt="SlowQuitApps"></a> | **[SlowQuitApps](https://github.com/dteoh/SlowQuitApps)** | Add a global delay to Command-Q to stop accidental app quits. | `Objective-C` | [Source](https://github.com/dteoh/SlowQuitApps) | `MIT` |
| <a href="https://github.com/Lukentui/smotrite-app"><img src="./icons/project-icons/smotrite.svg" width="32" height="32" alt="Smotrite"></a> | **[Smotrite](https://github.com/Lukentui/smotrite-app)** | Smotrite is a system monitor for macOS, which just work. | `TypeScript` | [Source](https://github.com/Lukentui/smotrite-app) | `MIT` |
| <a href="https://github.com/serhii-londar/open-source-mac-os-apps/blob/master/stirlingpdf.com"><img src="./icons/project-icons/stirling-pdf.svg" width="32" height="32" alt="Stirling-PDF"></a> | **[Stirling-PDF](https://github.com/serhii-londar/open-source-mac-os-apps/blob/master/stirlingpdf.com)** | Locally hosted web application that allows you to perform various operations on PDF files | `Java` | [Website](https://github.com/serhii-londar/open-source-mac-os-apps/blob/master/stirlingpdf.com) • [Source](https://github.com/Stirling-Tools/Stirling-PDF) | `MIT` |
| <a href="https://github.com/64characters/Telephone"><img src="./icons/project-icons/telephone.svg" width="32" height="32" alt="Telephone"></a> | **[Telephone](https://github.com/64characters/Telephone)** | SIP softphone for macOS. | `Objective-C` | [Source](https://github.com/64characters/Telephone) | `MIT` |
| <a href="https://github.com/stacks-network/blockstack-browser"><img src="./icons/project-icons/the-blockstack-browser.svg" width="32" height="32" alt="The Blockstack Browser"></a> | **[The Blockstack Browser](https://github.com/stacks-network/blockstack-browser)** | Blockstack is an internet for decentralized apps where users own their data. The Blockstack Browser allows you to explore the Blockstack internet. | `JavaScript` | [Source](https://github.com/stacks-network/blockstack-browser) | `MIT` |
| <a href="https://github.com/zenangst/ToTheTop"><img src="./icons/project-icons/tothetop.svg" width="32" height="32" alt="ToTheTop"></a> | **[ToTheTop](https://github.com/zenangst/ToTheTop)** | Small macOS application to help you scroll to the top. | `Swift` | [Source](https://github.com/zenangst/ToTheTop) | `MIT` |
| <a href="https://trex.ameba.co"><img src="./icons/project-icons/trex.svg" width="32" height="32" alt="TRex"></a> | **[TRex](https://trex.ameba.co)** | TRex is the easiest way to copy the uncopyable text from images, YouTube videos, Zoom calls and more. If you can see it - you can copy it. TRex captures any text right into your Clipboard with magic of OCR. | `Swift` | [Website](https://trex.ameba.co) • [Source](https://github.com/amebalabs/TRex) | `MIT` |
| <a href="https://wechsel.weise.io"><img src="./icons/project-icons/wechsel.svg" width="32" height="32" alt="wechsel"></a> | **[wechsel](https://wechsel.weise.io)** | manage bluetooth connections with your keyboard. | `Swift` | [Website](https://wechsel.weise.io) • [Source](https://github.com/friedrichweise/wechsel) | `MIT` |
| <a href="https://github.com/felixhageloh/uebersicht"><img src="./icons/project-icons/bersicht.svg" width="32" height="32" alt="Übersicht"></a> | **[Übersicht](https://github.com/felixhageloh/uebersicht)** | Keep an eye on what's happening on your machine and in the world. | `Objective-C` | [Source](https://github.com/felixhageloh/uebersicht) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="vpn-proxy"></a>
<a id="vpn--proxy"></a>
### 🔐 VPN & Proxy

> WireGuard, OpenVPN, Shadowsocks clients, and local network proxy toggle utilities.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/yichengchen/clashX"><img src="./icons/project-icons/clashx.svg" width="32" height="32" alt="clashX"></a> | **[clashX](https://github.com/yichengchen/clashX)** | A rule based custom proxy with GUI for Mac base on clash. | `Swift` | [Source](https://github.com/yichengchen/clashX) | `MIT` |
| <a href="https://github.com/riboseinc/cryptode-mac"><img src="./icons/project-icons/rvc-mac.svg" width="32" height="32" alt="rvc-mac"></a> | **[rvc-mac](https://github.com/riboseinc/cryptode-mac)** | Ribose VPN Client macOS Menu App. | `Swift` | [Source](https://github.com/riboseinc/cryptode-mac) | `MIT` |
| <a href="https://github.com/shadowsocks/ShadowsocksX-NG"><img src="./icons/project-icons/shadowsocksx-ng.svg" width="32" height="32" alt="ShadowsocksX-NG"></a> | **[ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG)** | Next Generation of ShadowsocksX. | `Swift` | [Source](https://github.com/shadowsocks/ShadowsocksX-NG) | `MIT` |
| <a href="https://github.com/zhuhaow/Specht"><img src="./icons/project-icons/specht.svg" width="32" height="32" alt="Specht"></a> | **[Specht](https://github.com/zhuhaow/Specht)** | Rule-based proxy app built with Network Extension for macOS. | `Swift` | [Source](https://github.com/zhuhaow/Specht) | `MIT` |
| <a href="https://github.com/zhuhaow/SpechtLite"><img src="./icons/project-icons/spechtlite.svg" width="32" height="32" alt="SpechtLite"></a> | **[SpechtLite](https://github.com/zhuhaow/SpechtLite)** | Rule-based proxy app for macOS. | `Swift` | [Source](https://github.com/zhuhaow/SpechtLite) | `MIT` |
| <a href="https://github.com/Tunnelblick/Tunnelblick"><img src="./icons/project-icons/tunnelblick.svg" width="32" height="32" alt="Tunnelblick"></a> | **[Tunnelblick](https://github.com/Tunnelblick/Tunnelblick)** | Tunnelblick is a graphic user interface for OpenVPN on macOS. | `Objective-C` | [Source](https://github.com/Tunnelblick/Tunnelblick) | `MIT` |
| <a href="https://www.wireguard.com"><img src="./icons/project-icons/wireguard.svg" width="32" height="32" alt="WireGuard"></a> | **[WireGuard](https://www.wireguard.com)** | Fast, Modern, Secure VPN Tunnel. | `Swift` | [Website](https://www.wireguard.com) • [Source](https://git.zx2c4.com/wireguard-apple/) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="video"></a>
### 🎬 Video

> Video players, subtitle editors, video encoders, and multimedia conversion tools.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/lostjared/Acid.Cam.v2.OSX"><img src="./icons/project-icons/acid-cam-v2-osx.svg" width="32" height="32" alt="Acid.Cam.v2.OSX"></a> | **[Acid.Cam.v2.OSX](https://github.com/lostjared/Acid.Cam.v2.OSX)** | Acid Cam v2 for macOS distorts video to create art. | `C++` | [Source](https://github.com/lostjared/Acid.Cam.v2.OSX) | `MIT` |
| <a href="https://github.com/insidegui/AppleEvents"><img src="./icons/project-icons/appleevents.svg" width="32" height="32" alt="AppleEvents"></a> | **[AppleEvents](https://github.com/insidegui/AppleEvents)** | Unofficial Apple Events app for macOS. | `Objective-C` | [Source](https://github.com/insidegui/AppleEvents) | `MIT` |
| <a href="https://github.com/zagahr/Conferences.digital"><img src="./icons/project-icons/conferences-digital.svg" width="32" height="32" alt="Conferences.digital"></a> | **[Conferences.digital](https://github.com/zagahr/Conferences.digital)** | Best way to watch the latest and greatest videos from your favourite developer conferences for free on your Mac. | `Swift` | [Source](https://github.com/zagahr/Conferences.digital) | `MIT` |
| <a href="https://github.com/maelswarm/Datamosh"><img src="./icons/project-icons/datamosh.svg" width="32" height="32" alt="Datamosh"></a> | **[Datamosh](https://github.com/maelswarm/Datamosh)** | Datamosh your videos on macOS. | `Swift` | [Source](https://github.com/maelswarm/Datamosh) | `MIT` |
| <a href="https://github.com/xiaohk/FaceData"><img src="./icons/project-icons/face-data.svg" width="32" height="32" alt="Face Data"></a> | **[Face Data](https://github.com/xiaohk/FaceData)** | macOS application used to auto-annotate landmarks from a video. | `Swift` | [Source](https://github.com/xiaohk/FaceData) | `MIT` |
| <a href="https://github.com/vdel26/gifted"><img src="./icons/project-icons/gifted.svg" width="32" height="32" alt="Gifted"></a> | **[Gifted](https://github.com/vdel26/gifted)** | Turn any short video into an animated GIF quickly and easily. | `Objective-C` | [Source](https://github.com/vdel26/gifted) | `MIT` |
| <a href="https://www.gnugk.org"><img src="./icons/project-icons/gnu-gatekeeper.svg" width="32" height="32" alt="GNU Gatekeeper"></a> | **[GNU Gatekeeper](https://www.gnugk.org)** | Video conferencing server for H.323 terminals. | `C++` | [Website](https://www.gnugk.org) • [Source](https://github.com/willamowius/gnugk) | `MIT` |
| <a href="https://handbrake.fr"><img src="./icons/project-icons/handbrake.png" width="32" height="32" alt="HandBrake"></a> | **[HandBrake](https://handbrake.fr)** | Open-source video transcoder for converting video from nearly any format to modern codecs. | `C` | [Website](https://handbrake.fr) • [Source](https://github.com/HandBrake/HandBrake) | `GPL-2.0` |
| <a href="https://iina.io"><img src="./icons/project-icons/iina.png" width="32" height="32" alt="IINA"></a> | **[IINA](https://iina.io)** | The modern media player for macOS, built with Swift and powered by mpv with native Picture-in-Picture. | `Swift` | [Website](https://iina.io) • [Source](https://github.com/iina/iina) | `GPL-3.0` |
| <a href="https://github.com/mifi/lossless-cut"><img src="./icons/project-icons/losslesscut.svg" width="32" height="32" alt="LosslessCut"></a> | **[LosslessCut](https://github.com/mifi/lossless-cut)** | Swiss army knife for lossless video and audio trimming, cutting, and slicing without re-encoding. | `TypeScript` | [Source](https://github.com/mifi/lossless-cut) | `GPL-2.0` |
| <a href="https://github.com/edanchenkov/MenuTube"><img src="./icons/project-icons/menutube.svg" width="32" height="32" alt="MenuTube"></a> | **[MenuTube](https://github.com/edanchenkov/MenuTube)** | Catch YouTube into your macOS menu bar! | `JavaScript` | [Source](https://github.com/edanchenkov/MenuTube) | `MIT` |
| <a href="https://github.com/OpenShot/openshot-qt"><img src="./icons/project-icons/openshot.svg" width="32" height="32" alt="OpenShot"></a> | **[OpenShot](https://github.com/OpenShot/openshot-qt)** | Easy to use, quick to learn, and surprisingly powerful video editor. | `Python` | [Source](https://github.com/OpenShot/openshot-qt) | `MIT` |
| <a href="https://apps.apple.com/app/quick-caption/id1363610340"><img src="./icons/project-icons/quick-caption.svg" width="32" height="32" alt="Quick Caption"></a> | **[Quick Caption](https://apps.apple.com/app/quick-caption/id1363610340)** | Transcribe and generate caption files (SRT, ASS and FCPXML) without manually entering time codes. | `Swift` | [Website](https://apps.apple.com/app/quick-caption/id1363610340) • [Source](https://github.com/LumingYin/Caption) | `MIT` |
| <a href="https://github.com/Marginal/QLVideo"><img src="./icons/project-icons/quicklook-video.svg" width="32" height="32" alt="QuickLook Video"></a> | **[QuickLook Video](https://github.com/Marginal/QLVideo)** | This package allows macOS Finder to display thumbnails, static QuickLook previews, cover art and metadata for most types of video files. | `Objective-C` | [Source](https://github.com/Marginal/QLVideo) | `MIT` |
| <a href="https://subler.org"><img src="./icons/project-icons/subler.svg" width="32" height="32" alt="Subler"></a> | **[Subler](https://subler.org)** | Subler is an macOS app created to mux and tag mp4 files. | `Objective-C` | [Website](https://subler.org) • [Source](https://bitbucket.org/galad87/subler/src) | `MIT` |
| <a href="https://github.com/sahil-a/vidquizcreator"><img src="./icons/project-icons/vid-quiz-creator.svg" width="32" height="32" alt="Vid Quiz Creator"></a> | **[Vid Quiz Creator](https://github.com/sahil-a/vidquizcreator)** | macOS application to insert quizzes within video playback and play those videos to receiving devices using the LISNR API. | `Swift` | [Source](https://github.com/sahil-a/vidquizcreator) | `MIT` |
| <a href="https://www.videolan.org/vlc"><img src="./icons/project-icons/vlc.png" width="32" height="32" alt="VLC"></a> | **[VLC](https://www.videolan.org/vlc)** | Renowned cross-platform multimedia player playing most multimedia files, discs, and streaming protocols. | `C` | [Website](https://www.videolan.org/vlc) • [Source](https://github.com/videolan/vlc) | `GPL-2.0` |
| <a href="https://github.com/webtorrent/webtorrent-desktop"><img src="./icons/project-icons/webtorrent-desktop.svg" width="32" height="32" alt="WebTorrent Desktop"></a> | **[WebTorrent Desktop](https://github.com/webtorrent/webtorrent-desktop)** | Streaming torrent app. For Mac, Windows, and Linux. | `JavaScript` | [Source](https://github.com/webtorrent/webtorrent-desktop) | `MIT` |
| <a href="https://github.com/whoisandy/yoda"><img src="./icons/project-icons/yoda.svg" width="32" height="32" alt="Yoda"></a> | **[Yoda](https://github.com/whoisandy/yoda)** | Nifty macOS application which enables you to browse and download videos from YouTube. | `JavaScript` | [Source](https://github.com/whoisandy/yoda) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="wallpaper"></a>
### 🖥️ Wallpaper

> Dynamic wallpaper rotators, aerial desktop engines, and custom wallpaper creators.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://github.com/markcheeky/500-mac-wallpaper"><img src="./icons/project-icons/500-mac-wallpaper.svg" width="32" height="32" alt="500-mac-wallpaper"></a> | **[500-mac-wallpaper](https://github.com/markcheeky/500-mac-wallpaper)** | Simple macOS app for the status bar to automatically download photos from 500px.com to a local folder that can be set as a source of wallpapers. | `Swift` | [Source](https://github.com/markcheeky/500-mac-wallpaper) | `MIT` |
| <a href="https://github.com/NghiaTranUIT/artify-macos"><img src="./icons/project-icons/artify.svg" width="32" height="32" alt="Artify"></a> | **[Artify](https://github.com/NghiaTranUIT/artify-macos)** | A macOS application for bringing dedicatedly 18th century Arts to everyone | `Swift` | [Source](https://github.com/NghiaTranUIT/artify-macos) | `MIT` |
| <a href="https://github.com/JustinFincher/ASWP-for-macOS"><img src="./icons/project-icons/artwall.svg" width="32" height="32" alt="ArtWall"></a> | **[ArtWall](https://github.com/JustinFincher/ASWP-for-macOS)** | ArtStation set as wallpapers from artwork.rss | `Objective-C` | [Source](https://github.com/JustinFincher/ASWP-for-macOS) | `MIT` |
| <a href="https://github.com/pengsrc/BingPaper"><img src="./icons/project-icons/bingpaper.svg" width="32" height="32" alt="BingPaper"></a> | **[BingPaper](https://github.com/pengsrc/BingPaper)** | Use Bing daily photo as your wallpaper on macOS. | `Swift` | [Source](https://github.com/pengsrc/BingPaper) | `MIT` |
| <a href="https://github.com/VioletGiraffe/desktop-wallpaper-switcher"><img src="./icons/project-icons/desktop-wallpaper-switcher.svg" width="32" height="32" alt="Desktop Wallpaper Switcher"></a> | **[Desktop Wallpaper Switcher](https://github.com/VioletGiraffe/desktop-wallpaper-switcher)** | Win / Linux / macOS tool for managing and cycling desktop wallpapers. | `C++` | [Source](https://github.com/VioletGiraffe/desktop-wallpaper-switcher) | `MIT` |
| <a href="https://equinoxmac.com"><img src="./icons/project-icons/equinox.svg" width="32" height="32" alt="Equinox"></a> | **[Equinox](https://equinoxmac.com)** | Equinox is an application that allows you to create macOS dynamic wallpapers. | `Swift` | [Website](https://equinoxmac.com) • [Source](https://github.com/rlxone/Equinox) | `MIT` |
| <a href="https://github.com/naman14/Muzei-macOS"><img src="./icons/project-icons/muzei.svg" width="32" height="32" alt="Muzei"></a> | **[Muzei](https://github.com/naman14/Muzei-macOS)** | Muzei wallpaper app for macOS. | `Swift` | [Source](https://github.com/naman14/Muzei-macOS) | `MIT` |
| <a href="https://github.com/IngoMeyer441/pyDailyChanger"><img src="./icons/project-icons/pydailychanger.svg" width="32" height="32" alt="pyDailyChanger"></a> | **[pyDailyChanger](https://github.com/IngoMeyer441/pyDailyChanger)** | pyDailyChanger is a program that changes your wallpaper daily. | `Python` | [Source](https://github.com/IngoMeyer441/pyDailyChanger) | `MIT` |
| <a href="https://github.com/tomtaylor/satellite-eyes"><img src="./icons/project-icons/satellite-eyes.svg" width="32" height="32" alt="Satellite Eyes"></a> | **[Satellite Eyes](https://github.com/tomtaylor/satellite-eyes)** | macOS app to automatically set your desktop wallpaper to the satellite view overhead. | `Objective-C` | [Source](https://github.com/tomtaylor/satellite-eyes) | `MIT` |
| <a href="https://github.com/davidcelis/Sunscreen"><img src="./icons/project-icons/sunscreen.svg" width="32" height="32" alt="Sunscreen"></a> | **[Sunscreen](https://github.com/davidcelis/Sunscreen)** | Sunscreen is a fun, lightweight application that changes your desktop wallpaper based on sunrise and sunset. | `Swift` | [Source](https://github.com/davidcelis/Sunscreen) | `MIT` |
| <a href="https://github.com/diogosantos/WallpaperMenu"><img src="./icons/project-icons/wallpapermenu.svg" width="32" height="32" alt="WallpaperMenu"></a> | **[WallpaperMenu](https://github.com/diogosantos/WallpaperMenu)** | macOS menubar application for navigation through beautiful pictures on the web and set them up as your desktop image. | `Ruby` | [Source](https://github.com/diogosantos/WallpaperMenu) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="window-management"></a>
### 🪟 Window Management

> Tiling window managers, keyboard snap helpers, and window switcher enhancements.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://nikitabobko.github.io/AeroSpace"><img src="./icons/project-icons/aerospace.png" width="32" height="32" alt="AeroSpace"></a> | **[AeroSpace](https://nikitabobko.github.io/AeroSpace)** | i3-like tiling window manager for macOS with tree-based workspace navigation. | `Swift` | [Website](https://nikitabobko.github.io/AeroSpace) • [Source](https://github.com/nikitabobko/AeroSpace) | `MIT` |
| <a href="https://ianyh.com/amethyst"><img src="./icons/project-icons/amethyst.png" width="32" height="32" alt="Amethyst"></a> | **[Amethyst](https://ianyh.com/amethyst)** | Automatic tiling window manager for macOS inspired by xmonad. | `Swift` | [Website](https://ianyh.com/amethyst) • [Source](https://github.com/ianyh/Amethyst) | `MIT` |
| <a href="https://github.com/mjolnirapp/AppGrid"><img src="./icons/project-icons/appgrid.svg" width="32" height="32" alt="AppGrid"></a> | **[AppGrid](https://github.com/mjolnirapp/AppGrid)** | Grid-based keyboard window manager for macOS. | `Objective-C` | [Source](https://github.com/mjolnirapp/AppGrid) | `MIT` |
| <a href="https://github.com/mamiksik/Desktop-Profiles"><img src="./icons/project-icons/desktop-profiles.svg" width="32" height="32" alt="Desktop Profiles"></a> | **[Desktop Profiles](https://github.com/mamiksik/Desktop-Profiles)** | An innovative desktop/window manager for macOS | `Swift` | [Source](https://github.com/mamiksik/Desktop-Profiles) | `MIT` |
| <a href="https://github.com/Hammerspoon/hammerspoon"><img src="./icons/project-icons/hammerspoon.svg" width="32" height="32" alt="Hammerspoon"></a> | **[Hammerspoon](https://github.com/Hammerspoon/hammerspoon)** | Staggeringly powerful macOS desktop automation with Lua. | `Lua` | [Source](https://github.com/Hammerspoon/hammerspoon) | `MIT` |
| <a href="https://github.com/MrKai77/Loop"><img src="./icons/project-icons/loop.svg" width="32" height="32" alt="Loop"></a> | **[Loop](https://github.com/MrKai77/Loop)** | Window management made elegant. | `Swift` | [Source](https://github.com/MrKai77/Loop) | `MIT` |
| <a href="https://nudge.run"><img src="./icons/project-icons/nudge.svg" width="32" height="32" alt="Nudge"></a> | **[Nudge](https://nudge.run)** | Free, open-source window manager with keyboard shortcuts and drag-to-edge snapping. | `Swift` | [Website](https://nudge.run) • [Source](https://github.com/mikusnuz/nudge) | `MIT` |
| <a href="https://github.com/kasper/phoenix"><img src="./icons/project-icons/phoenix.svg" width="32" height="32" alt="Phoenix"></a> | **[Phoenix](https://github.com/kasper/phoenix)** | Lightweight macOS window and app manager scriptable with JavaScript. | `Objective-C` | [Source](https://github.com/kasper/phoenix) | `MIT` |
| <a href="https://rectangleapp.com"><img src="./icons/project-icons/rectangle.png" width="32" height="32" alt="Rectangle"></a> | **[Rectangle](https://rectangleapp.com)** | Move and resize windows on macOS using keyboard shortcuts and snap areas. | `Swift` | [Website](https://rectangleapp.com) • [Source](https://github.com/rxhanson/Rectangle) | `MIT` |
| <a href="https://github.com/fikovnik/ShiftIt"><img src="./icons/project-icons/shiftit.svg" width="32" height="32" alt="ShiftIt"></a> | **[ShiftIt](https://github.com/fikovnik/ShiftIt)** | Managing windows size and position. | `Objective-C` | [Source](https://github.com/fikovnik/ShiftIt) | `MIT` |
| <a href="https://github.com/jigish/slate"><img src="./icons/project-icons/slate.svg" width="32" height="32" alt="Slate"></a> | **[Slate](https://github.com/jigish/slate)** | Slate is a window management application similar to Divvy and SizeUp | `Objective-C` | [Source](https://github.com/jigish/slate) | `MIT` |
| <a href="https://github.com/eczarny/spectacle"><img src="./icons/project-icons/spectacle.svg" width="32" height="32" alt="Spectacle"></a> | **[Spectacle](https://github.com/eczarny/spectacle)** | Spectacle allows you to organize your windows without using a mouse. | `Objective-C` | [Source](https://github.com/eczarny/spectacle) | `MIT` |
| <a href="https://github.com/Conxt/WindowGlue"><img src="./icons/project-icons/window-glue.svg" width="32" height="32" alt="Window Glue"></a> | **[Window Glue](https://github.com/Conxt/WindowGlue)** | A simple macOS menu bar utility that lets you glue two windows together so that they behave (mostly) as one. | `Swift` | [Source](https://github.com/Conxt/WindowGlue) | `MIT` |
| <a href="https://github.com/koekeishiya/yabai"><img src="./icons/project-icons/yabai.png" width="32" height="32" alt="yabai"></a> | **[yabai](https://github.com/koekeishiya/yabai)** | Tiling window management utility for macOS based on binary space partitioning. | `C` | [Source](https://github.com/koekeishiya/yabai) | `MIT` |

[⬆ Back to Top](#table-of-contents)


<a id="ai-ml"></a>
<a id="ai-machine-learning"></a>
### 🤖 AI & Machine Learning

> Local large language model runners, desktop AI frontends, and on-device ML workflows.

| Icon | Project | Description | Stack | Links | License |
| :---: | :--- | :--- | :---: | :---: | :---: |
| <a href="https://chatboxai.app"><img src="./icons/project-icons/chatbox.png" width="32" height="32" alt="Chatbox"></a> | **[Chatbox](https://chatboxai.app)** | Desktop client for multiple AI models with local data storage, prompt templates, and artifacts. | `TypeScript` | [Website](https://chatboxai.app) • [Source](https://github.com/Bin-Huang/chatbox) | `GPL-3.0` |
| <a href="https://diffusionbee.com"><img src="./icons/project-icons/diffusionbee.png" width="32" height="32" alt="DiffusionBee"></a> | **[DiffusionBee](https://diffusionbee.com)** | Easy offline way to run Stable Diffusion on Mac with Core ML hardware acceleration. | `JavaScript` | [Website](https://diffusionbee.com) • [Source](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui) | `GPL-3.0` |
| <a href="https://jan.ai"><img src="./icons/project-icons/jan.png" width="32" height="32" alt="Jan"></a> | **[Jan](https://jan.ai)** | Open-source local AI conversational assistant that runs offline on your Mac with zero data tracking. | `TypeScript` | [Website](https://jan.ai) • [Source](https://github.com/janhq/jan) | `AGPL-3.0` |
| <a href="https://ollama.com"><img src="./icons/project-icons/ollama.png" width="32" height="32" alt="Ollama"></a> | **[Ollama](https://ollama.com)** | Get up and running with large language models locally on Apple Silicon and Intel Macs. | `Go` | [Website](https://ollama.com) • [Source](https://github.com/ollama/ollama) | `MIT` |
| <a href="https://github.com/ggerganov/whisper.cpp"><img src="./icons/project-icons/whisper-cpp.png" width="32" height="32" alt="Whisper.cpp"></a> | **[Whisper.cpp](https://github.com/ggerganov/whisper.cpp)** | High-performance port of OpenAI's Whisper speech recognition model optimized for Apple Silicon Metal. | `C++` | [Source](https://github.com/ggerganov/whisper.cpp) | `MIT` |

[⬆ Back to Top](#table-of-contents)
<!-- PROJECTS:END -->

---

<a id="selection-criteria"></a>
<a id="open-source-criteria"></a>
## 🎯 Selection Criteria & License Policy

To preserve directory trust and quality, every submission is evaluated against rigorous qualification standards:

### ✅ Mandatory Requirements
1. **Public Source Repository**: Source code must reside in an active, publicly accessible Git host (GitHub, GitLab, Codeberg).
2. **Recognized Open-Source License**: Must carry an official [OSI-approved](https://opensource.org/licenses) or FSF-compliant open-source license.
3. **Genuine macOS Compatibility**: Must run natively on macOS (Apple Silicon or Intel) as a GUI desktop app, menu bar utility, or CLI workflow.
4. **Active or Verifiable Maintenance**: Projects must be compilable or provide pre-built release binaries (DMG, PKG, or Homebrew Cask).
5. **No Deceptive Pricing**: Apps that claim to be "free" but require paid keys to unlock primary functionality without providing the open source to build it locally are strictly disqualified.

### 📜 Accepted Licenses
- **Permissive**: `MIT`, `Apache-2.0`, `BSD-2-Clause`, `BSD-3-Clause`, `ISC`, `Unlicense`, `CC0-1.0`
- **Copyleft**: `GPL-2.0`, `GPL-3.0`, `AGPL-3.0`, `LGPL-2.1`, `LGPL-3.0`, `MPL-2.0`, `EPL-2.0`
- *Custom licenses are reviewed on a case-by-case basis and must strictly adhere to the Open Source Definition.*

### 🚦 Project Status Indicators
| Status | Definition |
| :--- | :--- |
| `active` | Actively maintained, frequent releases, responsive maintainers. |
| `maintenance` | Mature or stable codebase; updates occur primarily for OS compatibility or security patches. |
| `archived` | Read-only repository preserved for educational or legacy reference. |

---

<a id="how-to-contribute"></a>
<a id="add-a-project"></a>
## 🤝 How to Add a Project

Adding an open-source Mac app to OpenMac is fast and easy. Choose the method that suits you best:

### 🌟 Method 1: The 1-Click Form (No Git Required)
If you don't want to mess with Git or command lines, simply fill out our issue template:
👉 [**Open the Add Project Form**](https://github.com/shareefmx/OpenMac/issues/new?template=add-project.yml) — paste the GitHub link and details, and maintainers will add it for you!

---

### ⚡ Method 2: The Interactive CLI Wizard (Fastest for Developers)
We built an automated CLI helper that asks for your app details, creates the icon, runs validation, and updates `README.md` in seconds:

```bash
git clone https://github.com/YOUR_USERNAME/OpenMac.git
cd OpenMac

# Run the interactive wizard
python3 scripts/add-project.py
```
Follow the prompts on screen, then push your branch and open a PR!

---

### 🛠️ Method 3: Standard Manual Git Workflow
If you prefer manual control:

```bash
# 1. Clone your fork and create a branch
git checkout -b add/your-project-name

# 2. Add icon to icons/project-icons/ (SVG or PNG)
cp /path/to/icon.svg icons/project-icons/your-project-name.svg

# 3. Add project metadata to data/projects.yml
# 4. Run automated validation & README compiler
python3 scripts/validate-projects.py
python3 scripts/generate-readme.py

# 5. Commit and push
git add .
git commit -m "Add Your Project Name to Category"
git push origin add/your-project-name
```

For complete guidelines, schema definitions, and tips, please read our [**Contributing Guide (CONTRIBUTING.md)**](./CONTRIBUTING.md).

---

<a id="icon-system"></a>
## 🎨 Icon System

All icons are version-controlled inside [`icons/project-icons/`](./icons/project-icons/) to prevent broken images and maintain long-term archival permanence.

- **Size & Format**: 1:1 square vector SVG (preferred) or 256×256 / 512×512 PNG.
- **Naming Rule**: Filename must match the project ID (`icons/project-icons/<id>.svg`).
- **Trademark Notice**: Project logos belong to their respective creators. Inclusion does not imply endorsement.

Refer to the [**Icon Guidelines**](./icons/README.md) for full submission details.

---

<a id="faq"></a>
## ❓ Frequently Asked Questions (FAQ)

<details>
<summary><b>Is every application in this repository 100% open source?</b></summary>
<p>Yes. That is the foundational promise of OpenMac. If you spot an entry that has turned proprietary or closed its source code, please <a href="https://github.com/shareefmx/OpenMac/issues/new?template=report-project.yml">report it immediately</a> and it will be updated or removed.</p>
</details>

<details>
<summary><b>Can I submit my own open-source macOS app?</b></summary>
<p>Absolutely! Authors and contributors are actively encouraged to showcase their work. Ensure your repository has an explicit open-source LICENSE file and includes installation/build instructions.</p>
</details>

<details>
<summary><b>Why is my favorite Mac app (e.g. Raycast, Alfred, Obsidian) not included?</b></summary>
<p>While excellent applications, they are closed-source proprietary software. OpenMac strictly indexes software with publicly verifiable, forkable, and auditable source code.</p>
</details>

<details>
<summary><b>How are star counts or rankings determined?</b></summary>
<p>We deliberately avoid vanity sorting based on GitHub stars alone. Tables are arranged alphabetically within categories to give equal discovery opportunities to emerging tools as well as industry stalwarts. Standout mature projects are highlighted in the Featured section based on objective community criteria.</p>
</details>

<details>
<summary><b>Can I request a new category?</b></summary>
<p>Yes! If an emerging domain (such as local AI or Apple Silicon audio processing) warrants dedicated grouping, submit a <a href="https://github.com/shareefmx/OpenMac/issues/new?template=request-category.yml">Category Request Issue</a>.</p>
</details>

---

<a id="contributors"></a>
## 👥 Contributors & Acknowledgements

OpenMac thrives on open community collaboration. Thank you to everyone who submits projects, reports issues, and enhances the macOS open-source ecosystem.

<p align="left">
  <a href="https://github.com/shareefmx/OpenMac/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=shareefmx/OpenMac" alt="Community Contributors" />
  </a>
</p>

See [**CONTRIBUTORS.md**](./CONTRIBUTORS.md) for details.

---

<a id="license"></a>
## ⚖️ License & Trademarks

- **Directory Content**: The OpenMac directory, automated tooling, documentation, and metadata are distributed under the [**MIT License**](./LICENSE).
- **Third-Party Applications**: Each application listed within this directory is governed by its own independent open-source license as indicated in the respective tables.
- **Trademarks**: macOS, Mac, and the Apple logo are trademarks of Apple Inc., registered in the U.S. and other countries. All project names, icons, and logos are properties of their respective copyright holders. OpenMac is an independent community initiative and is not affiliated with or endorsed by Apple Inc.

---

<div align="center">

**Built with pride by the open-source community for Mac users worldwide.**

<sub>Found a great open-source Mac app? <a href="./CONTRIBUTING.md">Submit a Pull Request</a> and help grow the ecosystem!</sub>

</div>
