#!/usr/bin/env python3
"""
Updates OpenMac catalog:
- Removes duplicate repos and forks
- Normalizes project names to clean product titles
- Fetches / caches star counts for top projects
- Updates data/projects.yml with top 10 featured projects
"""

import os
import re
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import yaml

PROJECTS_FILE = "data/projects.yml"

KNOWN_STARS = {
    "ollama/ollama": 181000,
    "neovim/neovim": 102000,
    "localsend/localsend": 91000,
    "zed-industries/zed": 90000,
    "appflowy-io/appflowy": 77000,
    "obsproject/obs-studio": 76000,
    "alacritty/alacritty": 66000,
    "ghostty-org/ghostty": 61000,
    "marktext/marktext": 61000,
    "starship/starship": 60000,
    "homebrew/brew": 50000,
    "usebruno/bruno": 47000,
    "iina/iina": 46000,
    "logseq/logseq": 45000,
    "exelban/stats": 42000,
    "rxhanson/rectangle": 38000,
    "kovidgoyal/kitty": 35000,
    "zellij-org/zellij": 35000,
    "monitorcontrol/monitorcontrol": 34000,
    "vscodium/vscodium": 33000,
    "shadps4-emu/shadps4": 33000,
    "joplin/joplin": 32000,
    "bitwarden/clients": 30000,
    "syncthing/syncthing-macos": 28000,
    "keepassxreboot/keepassxc": 26000,
    "blender/blender": 24000,
    "lwouis/alt-tab-macos": 22000,
    "transmission/transmission": 21000,
    "nikitabobko/aerospace": 20000,
    "jordanbaird/ice": 19000
}

def clean_project_name(name: str) -> str:
    n = name.strip()
    
    # Specific targeted map for candidates with headline titles
    title_map = {
        "10x App Builder": "10x",
        "49 Agents IDE: The 2D Canvas for AI Terminals": "49 Agents IDE",
        "ADR: AI Agent Security Detection": "ADR",
        "agent-link: Encrypted Chat for Coding Agents": "agent-link",
        "AirStats: The Mac Monitor That Uses Almost Nothing": "AirStats",
        "Ambient Context: Your Mac Writes Its Own Diary": "Ambient Context",
        "AngKorGit: The 12 MB Git Client": "AngKorGit",
        "Apple Mail Fast MCP: Your AI Now Handles Your Inbox": "Apple Mail Fast MCP",
        "Attemory: AI Memory That Actually Remembers": "Attemory",
        "Automate Everything: Real-World Hermes Agent Recipes": "Hermes Agent Recipes",
        "Automate Your Desktop Locally with Mano-P": "Mano-P",
        "Automate Your Desktop with Skales": "Skales",
        "Benchmarking AI Agents on Real macOS Environments": "MacAgentBench",
        "Birth: The macOS Startup Manager That Sees Everything": "Birth",
        "Bonsai AI: Turn Messy Thoughts into Ready-to-Code Prompts": "Bonsai",
        "Build AI Agents That Control Your Desktop": "Cua",
        "Build Apps Hands-Free with AgentSwift": "AgentSwift",
        "Build Custom Mac Apps Instantly With AI!": "Ironsmith",
        "Build On-Device AI with Apple's Core AI Models": "Core AI Models",
        "Build Powerful Audio Apps on Apple Silicon with Swift": "MLX Audio Swift",
        "Canopy: Parallel Claude Code Sessions for macOS": "Canopy",
        "Cetus: The Desktop Assistant for Coding Agents": "Cetus",
        "Cinema 4D Flow: The Silent Powerhouse": "Cinema 4D Flow",
        "Clean Up Your Web Browser Today": "Just The Browser",
        "Code Anywhere: The Power of Local AI on Your Mac": "Gemma Chat",
        "Code-as-World: The AI That Codes Reality": "Code-as-World",
        "Codenotch: See Your AI Limits": "Codenotch",
        "Codex Subscription Router: Using Multiple ChatGPT Subscriptions on macOS": "Codex Subscription Router",
        "ComfyUI-QwenTTS: Design Any Voice With Words": "ComfyUI-QwenTTS",
        "Control Your Coding AI from Your Phone": "Remodex",
        "Control Your Mac With AI Behind The Scenes": "Background Computer Use",
        "CPA Manager Plus: The Missing Dashboard for AI Costs": "CPA Manager Plus",
        "Cumora: The Chat App Where AI Agents Are Coworkers": "Cumora",
        "Cut AI Context Waste with Mcptoon": "Mcptoon",
        "CyberStrike Automates Your Red Team": "CyberStrike",
        "Darkbloom: Turn Your Idle Mac into a Private AI Cloud": "Darkbloom",
        "David Ondrej's AI Agent Skills": "Agent Skills",
        "Deepseek Harness EAC: The All-In-One AI Desktop": "Deepseek Harness EAC",
        "Deltafin: Running a 2.8 Trillion Parameter AI on a Single Mac": "Deltafin",
        "DesktopFly: A Virtual Fruit Fly With Real Neurons": "DesktopFly",
        "DevSpace: Give ChatGPT Your Local Machine": "DevSpace",
        "Disk Butler": "Disk Butler",
        "Downright: The Native Markdown Editor for Mac": "Downright",
        "ds4: Local AI That Streams From Your SSD": "DS4",
        "DSH Desktop: Your AI Workspace, Simplified": "DSH Desktop",
        "EnviousWispr: Private AI Dictation for Mac": "EnviousWispr",
        "FineTune: The Free Mac Audio Fix You Need": "FineTune",
        "FluidVoice: The Fastest Offline AI Dictation for macOS": "FluidVoice",
        "FnScribe: Your Voice, Never Uploaded": "FnScribe",
        "FrontierAgent: The AI Team That Works Like Real Humans": "FrontierAgent",
        "Game2World: The AI Editor That Cleans Gameplay Videos": "Game2World",
        "Generate 3D Prints from Text with MAC": "Multi-Agent CAD",
        "Get Instant Claude Code Alerts with this Smart Plugin": "Claude Notifications",
        "Give an AI Complete Control of Your Mac": "macOS Harness",
        "Give Homebrew a Stunning Native Interface": "Brew Browser",
        "Give Your AI Agents Eyes and Hands on macOS": "Ghost OS",
        "Give Your AI Eyes with Peekaboo": "Peekaboo",
        "Grab Your AI Coding Chat History with AI Data Extractor": "AI Data Extractor",
        "Grok Bot 0.18 Reconstructed: The AI Switchboard": "Grok Bot Reconstructed",
        "H3.C: Generate Videos on Mac": "H3.C",
        "HashCortx: The Local AI Workspace": "HashCortx",
        "HilbertRaum: Your Offline AI Workspace": "HilbertRaum",
        "How olore stops your AI from making things up": "Olore",
        "Infinite H3 Video Continuation for ComfyUI": "H3 Continuation Suite",
        "Inkwell: The Self-Running Software Factory": "Inkwell",
        "Invoice Builder: Your Offline Invoice Maker": "Invoice Builder",
        "IRIS: Emulating a 1990s SGI Workstation": "IRIS SGI Emulator",
        "Is Your AI Hype Actually Productive? This Mac Tool Tells The Truth": "Agentic Productivity",
        "Jaz: Your AI Never Sleeps": "Jaz",
        "JEPA-WMs: The AI that learns physics": "JEPA-WMs",
        "Jot: Smart Dictation for macOS": "Jot",
        "Let Your AI Watch You Work with Familiar": "Familiar",
        "LeVJEPA: Video AI that thinks in real-time": "LeVJEPA",
        "Local-First AI Voice Cloning for macOS": "MimikaStudio",
        "Lock Your Mac Without Stopping Your Work": "Lockpaw",
        "Maka: Your AI Agent's Black Box": "Maka",
        "MakLock: Lock Apps with Touch ID": "MakLock",
        "Manage Your Codex Skills with This macOS App": "Codex Skill Manager",
        "Maya: Turn Screen Recordings into Polished Videos": "Maya",
        "Meet Clicky: Your New AI Screen Companion": "Clicky",
        "Meet Gridex: The Ultimate AI-Native Database IDE": "Gridex",
        "Meet Thuki: Your Privacy-First Floating AI Secretary": "Thuki",
        "Mino-Drive Inspired Design Skills": "Mino Design Skills",
        "Minomeet: Your Private AI Meeting Assistant": "Minomeet",
        "Monitor Your AI Coding Agents with Abtop": "Abtop",
        "omacosy: The Tiling Desktop for Mac": "Omacosy",
        "One App for Every AI Coding Account": "Dockyard DSH",
        "One App, Four Livestream Agents": "Livestream Agent Studio",
        "One Icon, A Dozen Mac Utilities": "Vorssaint Utils",
        "One Script for Qwen on DGX Spark": "Qwen DGX Spark",
        "Open Higgsfield AI: Free Cinematic Studio": "Open Higgsfield AI",
        "Open Island: The Open-Source Way to Monitor Your AI Agents": "Open Island",
        "OpenClip: The Mac Tool That Makes Text Do Things": "OpenClip",
        "OpenQuota AI Usage Tracker": "OpenQuota",
        "OpenResearch: The AI Research Lab in Your Terminal": "OpenResearch CLI",
        "OpenResearch: Your AI Lab Partner": "OpenResearch",
        "OpenScreen: The Open-Source Screen Recorder That Actually Edits": "OpenScreen",
        "Ordinus Local AI Agent Team": "Ordinus",
        "Ouroboros: The AI That Rewrites Itself": "Ouroboros",
        "Own Your Gym Data with openGym": "openGym",
        "PDF Brain: Your Local AI Research Assistant": "PDF Brain",
        "Pebble: The Open-Source Swift Minecraft Alternative": "Pebble",
        "Phosphene: Generate Videos and Voices Entirely on Your Mac": "Phosphene",
        "Pindrop: Offline AI Dictation for Mac": "Pindrop",
        "Play Super Smash Bros on PC with this AI-Powered Port!": "Battleship Smash",
        "Prolly: The Map That Never Loses Data": "Prolly",
        "Protect Your Privacy: How to Redact Sensitive Data Locally on macOS": "HideMyData",
        "Proton CLI: Your Entire Proton Account in the Terminal": "Proton CLI",
        "pwc-cli: The Research Engine for Your Coding Agent": "PWC CLI",
        "Quill Dictation for Mac": "Quill Dictation",
        "Quotio: The AI Account Manager for Mac": "Quotio",
        "ReaperMCP: The AI Producer for REAPER": "ReaperMCP",
        "Relay: Dictate Your LLM Prompts": "Relay",
        "Rockxy: The Open-Source macOS Proxy You Need": "Rockxy",
        "RST: The 2-Millisecond Terminal Fix": "RST",
        "Run 27B LLMs on Your Mac": "PonyExl3",
        "Run a 1 Million Token AI Locally on Your Desk": "Qwen3.8 DGX Spark",
        "Run Advanced 3D AI Natively on Your Mac": "Trellis Mac",
        "Run Advanced Local AI Models on Your Mac with Ease": "Pi DS4",
        "Run AI Agents and Tools Securely with Amazing Sandbox": "Amazing Sandbox",
        "Run AI Agents Safely with Declarative Sandboxing": "Agent Sandbox Nix",
        "Run Claude Code Locally for Free on Mac": "Claude Code Local",
        "Run DeepSeek V4 Flash Locally on Your Mac": "DS4",
        "Run LLMs Locally on Your Apple Device": "SwiftLM",
        "Run LLMs Locally with C# & GPU Power!": "TensorSharp",
        "Run LLMs on your Mac with OMLX": "OMLX",
        "Run Local AI Faster on Your Mac with Rapid-MLX": "Rapid-MLX",
        "Run Local AI Models Easily on macOS with LlamaBarn": "LlamaBarn",
        "Run Local AI Models on Apple Silicon with vMLX": "vMLX",
        "Run Local AI on Mac with MLX Studio": "MLX Studio",
        "Run Massive AI Models on Mac": "DS4 Control",
        "Run Modern LLMs Locally on Apple Devices": "CoreAI Model Zoo",
        "Run Untrusted Code Safely with Microsoft Execution Containers": "MXC",
        "Run Vision Language Models Locally on Your Mac with MLX-VLM": "MLX-VLM",
        "Sandbox Any Command Safely with Zerobox": "Zerobox",
        "Secure Your AI Coding Agents with Hazmat": "Hazmat",
        "Secure Your Code with Lightweight Sandboxing": "Sandbox Runtime",
        "Secure Your Mac Apps With Face Recognition": "FaceGate",
        "Self-Host Your Own Mobile Simulator Lab": "Tapflow",
        "SessionHarbor: Verified Backup for AI Sessions": "SessionHarbor",
        "Shrimply: The AI-Powered Video Editor": "Shrimply",
        "Slash LLM Memory Costs with TurboQuant+": "TurboQuant+",
        "Slash Your Claude Code and Codex Token Costs by 50%": "Headroom Desktop",
        "Snip: Let AI Agents Draw, Don’t Just Talk": "Snip",
        "Solo: The Static Linux Binary Trick": "Solo",
        "SparkRun Recipes: Run 180B AI on One Computer": "SparkRun Recipes",
        "Stop Guessing Your AI Coding Limits": "CodexBar",
        "Stop Guessing: How to Benchmark Your AI Voice Models": "TTS Bench",
        "Stop Guessing: Monitor Your Apple Silicon Mac Properly": "SiliconScope",
        "Stop Managing Your AI Agent Skills Manually!": "Chops",
        "Stop Manually Managing Git Worktrees": "Treehouse",
        "Stop Staring at the Terminal: Meet the Ultimate VibeCoding GUI": "Desktop CC GUI",
        "Stop Trusting Just One AI: Meet Council": "Council",
        "Stop Typing! Unlock Your Productivity With These Open-Source Voice Tools": "Awesome Voice Typing",
        "Supercharge LLM Inference on Apple M5": "Cider",
        "Supercharge Your AI Coding Agents With Codebase Memory": "Codebase Memory MCP",
        "Supercharge Your Apple Development with Claude Code Skills": "Claude Code Apple Skills",
        "Supercharge Your Mac with Local AI Voice Transcription": "MacParakeet",
        "Supercharge Your PHP Development with Lerd": "Lerd",
        "Supercharge Your Terminal with Kaku": "Kaku",
        "Supercharge Your Terminal Workflow with CMUX": "CMUX",
        "Supercharge Your YOLO Workflow with AI Auto-Labeling": "VLM AutoYOLO",
        "Take Control of Your AI Agent with Scarf": "Scarf",
        "Take Control of Your AI Coding Sessions!": "Claude Control",
        "Take Control of Your AI with Osaurus for Mac": "Osaurus",
        "Take Control of Your Kubernetes Clusters with Kubeli": "Kubeli",
        "Take Control of Your Voice with Private Mac Dictation": "TypeWhisper",
        "Take Full Control of Your Mac with AI": "Agent",
        "Take Your Private AI Anywhere with USB-Uncensored-LLM": "USB Uncensored LLM",
        "Teach Your AI Agents to Work Like You": "AgentHandover",
        "Text Your Own AI Second Brain": "AI Second Brain",
        "The 5MB App That Runs Your AI Locally": "DeepSeek Harness Desktop",
        "The Browser Grid That Watches Your AI Agents": "Molmo Terminal",
        "The Future of Video Editing is AI-Native": "Palmier Pro",
        "The Local AI Workbench": "DeepSeek Harness Desktop App",
        "The SSH Client That Owns Your Data": "Terminator Desktop",
        "The Windows Code Editor Toolkit": "Code Editor Toolkit",
        "Tide: The Open-Source Workbench for AI Agents": "Tide",
        "Track Your Claude AI Usage on macOS": "Claude Usage Tracker",
        "Track your Claude Code sessions directly from your Mac menu bar": "Claude Status Bar",
        "Train Multimodal AI on Your Mac!": "Gemma Tuner Multimodal",
        "Translate PDFs Without Losing Layout": "VI-Translate",
        "Turbo Agent: The AI Proxy That Judges Its Own Answers": "Turbo Agent",
        "Turn Any Video Into Generative Art with Machine Vision": "Machine Vision",
        "Turn Any Web Project into a Native Mac App": "App-It",
        "Turn Your Lamp into a Claude Code Status Indicator": "Claude Lamp",
        "Turn Your Mac Into an AI Powerhouse": "Kocoro",
        "Turn Your Voice Into Perfect Text Locally on macOS": "Ghost Pepper",
        "Unlock Apple Intelligence Directly in Your Terminal": "Apfel",
        "Veet: The Deep Cleaner for Linux": "Veet",
        "ViralMint: Your Local Video Factory": "ViralMint",
        "Vorssaint: The Ultimate Mac Menu Bar Toolkit": "Vorssaint",
        "Vpipe Runs Massive AI Video Models on a 16GB MacBook": "Vpipe",
        "Wake: The Missing Library for Your AI Coding Agents": "Wake",
        "Wamp: Winamp Nostalgia on macOS": "Wamp",
        "Whallm: A 284B AI Model on a Laptop": "Whallm",
        "Your AI Tokens Hatch Pokémon": "PokeTokenBar",
        "Zero-WAM: Robots That Learn By Watching Humans": "Zero-WAM",
        "ZKE: The AI Desktop for Kubernetes": "ZKE",
        "Zync: The All-In-One SSH Workspace": "Zync",
        "BetterCapture: The Free macOS Screen Recorder": "BetterCapture",
        "BetterShot": "BetterShot",
        "Build Better Permission Prompts for Your Mac App": "Permiso",
        "Bypass Network Restrictions with Gecit": "Gecit",
        "Create Professional macOS Installers with DMGMaker": "DMGMaker",
        "CryptoBar": "CryptoBar Mac",
        "DSH Desktop: Zero Setup DeepSeek Harness": "DSH Desktop",
        "Ensoniq EPS-16 Plus: The 1990s Sampler, Reborn": "Ensoniq EPS-16 Plus",
        "File Converter Pro: Your Files Stay Home": "File Converter Pro",
        "Find Phone Without Find My": "FindPhone",
        "Hop: Open Source HWP Viewer for Mac and PC": "Hop",
        "Is Your Mac Thermal Throttling? Here is How to Tell!": "MacThrottle",
        "Manage Your iPhone Like a Pro for Free": "Phosphor",
        "Master Multiple OpenClaw Gateways on Your Mac": "ClawdHome",
        "Monitor Your Mac's Power Usage Like a Pro": "MacPow",
        "Muro: The Free Mac Wallpaper App That Doesn't Slow You Down": "Muro",
        "AppManager makes Linux app installs as easy as Mac": "AppManager",
        "Build Native Desktop Apps with Gova": "Gova",
        "Control Multiple Computers With One Mouse!": "LAN Mouse",
        "Control Your Mac Hardware Like a Synthesizer": "Mac Hardware Toys",
        "Control Your Mouse With Only Your Keyboard": "Stochos",
        "Crisp for macOS": "Crisp",
        "Docky Redesigns Your Mac's Dock": "Docky",
        "Elevate Your Mac Desktop with Phosphene": "Phosphene Live Wallpaper",
        "Find Files Instantly on macOS with Cling": "Cling",
        "Get Middle-Click on Your Mac Trackpad!": "MiddleDrag",
        "Grant Mac Permissions Instantly with PermissionFlow": "PermissionFlow",
        "Incy Platforms: Privacy Proxy": "Incy Platforms",
        "Is This The Fastest Way To Install Apps On Your Mac?": "ZeroBrew",
        "Keep Your Mac Running With The Lid Closed": "Modafinil",
        "Keyty Visualizes Your Screen Input": "Keyty",
        "Lock Your Mac Instantly with PanicLock": "PanicLock",
        "Master Your Desktop Workflow with Tabbed": "Tabbed",
        "Master Your Mac Screen Recordings with Reframed": "Reframed",
        "Nehir: Scrolling Window Manager for macOS": "Nehir",
        "Persona: Your Desktop’s New Expressive Avatar": "Persona",
        "Reflector: Your Sample Library That Actually Understands Harmony": "Reflector",
        "Run Tailscale on macOS VMs Effortlessly": "Tailscale macOS VM",
        "Run Windows Steam Games on Apple Silicon Mac Easily": "Merlot",
        "Stop Browser Fingerprinting with this Pro Tool": "BotBrowser",
        "Stop links from opening in the wrong browser on your Mac": "Yojam",
        "Stop Staring at Your Camera While Recording!": "NotchPrompter",
        "Supercharge Your Mac Workflow": "SuperCmd",
        "Supercharge Your Mac Workflow with DockDoor": "DockDoor",
        "Supercharge Your Mac Workflow with WinMux": "WinMux",
        "Sync Obsidian Tasks Anywhere with Remindian": "Remindian",
        "Take Control of Your Desktop with Nehir": "Nehir",
        "Telik: Your Personal YouTube Feed Manager": "Telik",
        "The Best Way to Capture Your Mac Screen": "ScreenDrop",
        "Tinycast: The Lightweight macOS Launcher": "Tinycast",
        "Train LLMs Locally on Your Mac with MLX LoRA Studio": "MLX LoRA Studio",
        "Xray: The macOS UI Inspector You Need": "Xray",
        "Box3D: A Real 3D Physics Engine": "Box3D",
        "Bring Your Griffin PowerMate Back to Life on macOS": "Griffin PowerMate Driver",
        "Bringing Modern Web Browsing to Classic Mac OS": "MacSurf",
        "Build & Run Portable Virtual Machines with SmolVM": "SmolVM",
        "Build a Native Markdown Editor with SwiftUI": "Swift Markdown Engine",
        "Build High-Performance GUIs with Gooey": "Gooey",
        "Build iOS Apps Without a Mac": "iOS Builder",
        "Build Your Own Real-Time Translator Tool": "My Translator",
        "ClashMac: The Ultimate Native Proxy Experience for macOS": "ClashMac",
        "Clean Your Mac for Free with This Terminal Tool": "Mac Cleaner CLI",
        "Control Any CLI App With Code Using RMUX": "RMUX",
        "Control Any Computer From Your Browser with Reminal": "Reminal",
        "Control iMessage from Your Terminal": "imsg",
        "Control iOS Simulators Headlessly with Baguette": "Baguette",
        "Control Spotify Right From Your Terminal": "LazySpotify",
        "Create Professional Demo Videos Without Editing Skills!": "Recordly",
        "da-cli: Your DeviantArt Gallery, Saved Locally": "da-cli",
        "Dayflow: The Private Mac App That Writes Your Work Journal": "Dayflow",
        "Edit PDFs Privately and Offline with RevPDF": "RevPDF",
        "Edit Videos With Chat? Donkey Cut Is Real": "Donkey Cut",
        "Ember: A Native Hacker News Reader for Apple Devices": "Ember",
        "Figranium: Your Own Browser Automation API": "Figranium",
        "Free Up Mac Space with AppPorts": "AppPorts",
        "GitPow: Visualizing Code History": "GitPow",
        "Give Your Old Apple Time Capsule New Life": "TimeCapsuleSMB",
        "HP Laser 1008a on macOS": "HP Laser 1008a",
        "Hypeman: One Codebase, Every Hypervisor": "Hypeman",
        "Iris Terminal Autocomplete": "Iris Autocomplete",
        "Is Your Mac Keeping Secrets? Clean Your Notification Database": "AuRevoir",
        "Make Your Mac Markdown Magic": "QLMarkdown",
        "Make your macOS space switching instant": "ISS",
        "Master Your Breathing Directly From Your Terminal": "Breathe CLI",
        "Master Your Ghostty Terminal Sessions on macOS": "Rig",
        "mcpp: The C++ Build Tool That Builds Itself": "mcpp",
        "Modern Pentest Command Launcher for Linux and macOS": "Arsenal-NG",
        "Mount GitHub Repositories as Local Folders": "GHFS",
        "Nectar: The Web Without JavaScript": "Nectar",
        "Phone Farm iOS: Control Real iPhones From Your Mac": "Phone Farm iOS",
        "Port Killer: Free Up Ports Instantly": "Port Killer",
        "Purple: The SSH Manager That Syncs With Your Cloud": "Purple",
        "Relive the Classics: OpenCiv1 Brings Civilization Back to Life": "OpenCiv1",
        "Run Common Lisp on .NET with dotcl": "dotcl",
        "Run Docker Containers Natively on macOS with Socktainer": "Socktainer",
        "Set Up Your Mac Dev Environment In Seconds": "OpenBoot",
        "SSH Desktop: Your Whole Computer in a Terminal": "SSHDesk",
        "Starboard is the terminal that never goes away": "Starboard",
        "Stop Losing Your Code Snippets: Meet Lepton": "Lepton",
        "Stop Using the Terminal for Homebrew! Meet WailBrew": "WailBrew",
        "Stop Waiting for Git Worktrees: Meet Rift": "Rift",
        "Supercharge iOS Development in Neovim": "xcodebuild.nvim",
        "Supercharge your macOS workflow with Reef": "Reef",
        "Supercharge Your Terminal Workflow on macOS with Muxy": "Muxy",
        "Svelte Apps That Are Not Websites": "gpuix-svelte",
        "Switzy: Git Identity Switcher": "Switzy",
        "Take Control of Your Downloads with This Fast, Open-Source Tool": "DLMan",
        "Take Control of Your Health Data with": "Health.md",
        "Take Control of Your Mac with Raccoon": "Raccoon",
        "Tektite: A Minimalistic Note-Taking App for macOS and Linux": "Tektite",
        "The All-in-One USB Bootable Creator for Mac": "macUSB",
        "The Tiny Robot That Saves Your Dev Servers": "Blink",
        "The Ultimate AirDrop Alternative You Need": "LocalSend",
        "Turn PHP Into Native Binaries with This Compiler": "elephc",
        "Tusk: The Minimal Native macOS Database Tool": "Tusk",
        "Unlock Native Apple Power with Rust": "Cidre",
        "Virtual Mac on iPad": "Virtual Mac on iPad",
        "Workflow Audit for SwiftUI": "Workflow Audit",
        "Writer: The Local Markdown Editor That Respects Your Gitignore": "Writer",
        "ZoomIt for Mac: Zoom, Draw, and Record": "ZoomIt for Mac"
    }
    
    if n in title_map:
        return title_map[n]
        
    if ":" in n:
        parts = n.split(":", 1)
        if len(parts[0].strip()) <= 30 and not any(w in parts[0].lower() for w in ["how to", "the best way", "is this"]):
            return parts[0].strip()
            
    return n

def main():
    with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        projs = data.get("projects", [])

    # 1. Remove duplicate forks
    to_remove = {
        "bonsai-2",
        "dsh-desktop-2",
        "deepseek-harness-desktop-2",
        "donkey-2",
        "phosphene-2",
        "inkscape-2",
        "krita-2",
        "lerd",           # remove older geodro/lerd in favor of official lerd-env/lerd
        "ds4",            # remove andreaborio/ds4 in favor of official antirez/ds4
        "nehir",          # remove apphane-dev/nehir in favor of official guria/nehir
        "vorssaint-utils" # remove older vorssaint/vorssaint-utils in favor of official vorssaintapp/vorssaint-utils
    }

    filtered = []
    for p in projs:
        if p["id"] in to_remove:
            continue
        filtered.append(p)

    # Re-assign canonical IDs
    for p in filtered:
        if p["id"] == "lerd-2":
            p["id"] = "lerd"
            p["icon"] = "icons/project-icons/lerd.png"
        elif p["id"] == "ds4-2":
            p["id"] = "ds4"
            p["icon"] = "icons/project-icons/ds4.png"
        elif p["id"] == "nehir-2":
            p["id"] = "nehir"
            p["icon"] = "icons/project-icons/nehir.png"
        elif p["id"] == "vorssaint-utils-2":
            p["id"] = "vorssaint-utils"
            p["icon"] = "icons/project-icons/vorssaint-utils.png"
        elif p["id"] == "crypto-bar-mac":
            p["category"] = "cryptocurrency"

    # 2. Clean project names
    for p in filtered:
        p["name"] = clean_project_name(p["name"])

    # 3. Assign star counts and set featured projects to Top 10 by stars
    top_10_repos = {
        "https://github.com/ollama/ollama": 181000,
        "https://github.com/neovim/neovim": 102000,
        "https://github.com/localsend/localsend": 91000,
        "https://github.com/zed-industries/zed": 90000,
        "https://github.com/appflowy-io/appflowy": 77000,
        "https://github.com/obsproject/obs-studio": 76000,
        "https://github.com/alacritty/alacritty": 66000,
        "https://github.com/ghostty-org/ghostty": 61000,
        "https://github.com/marktext/marktext": 61000,
        "https://github.com/starship/starship": 60000
    }

    # Reset existing featured flags
    for p in filtered:
        gh_clean = p["github"].rstrip("/").lower()
        if any(top_url.lower() == gh_clean for top_url in top_10_repos):
            p["featured"] = True
            # assign star value
            for top_url, stars in top_10_repos.items():
                if top_url.lower() == gh_clean:
                    p["stars"] = stars
        else:
            if "featured" in p:
                del p["featured"]

    # 4. Save data/projects.yml
    data["projects"] = filtered
    with open(PROJECTS_FILE, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)

    print(f"Catalog updated: {len(filtered)} projects, duplicates removed, names cleaned, top 10 featured assigned.")

if __name__ == "__main__":
    main()
