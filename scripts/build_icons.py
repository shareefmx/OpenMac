#!/usr/bin/env python3
"""
Generates crisp, branded vector SVG icons for all OpenMac projects.
Icons feature standard Apple macOS squircle geometry (rx=26 on 128x128 grid)
with authentic color palettes and distinct app iconography.
"""

import os

ICONS = {
    "zed": {
        "bg": ["#1F2430", "#14171F"],
        "border": "#2E3440",
        "svg": """<path d="M40 42 L88 42 L48 86 L88 86" fill="none" stroke="#25B4FF" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
                  <circle cx="88" cy="42" r="5" fill="#FFE066"/>"""
    },
    "vscodium": {
        "bg": ["#007ACC", "#005A9E"],
        "border": "#29B6F6",
        "svg": """<path d="M84 34 L54 58 L38 46 L30 52 L30 76 L38 82 L54 70 L84 94 L98 86 L98 42 Z" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linejoin="round"/>
                  <line x1="54" y1="58" x2="54" y2="70" stroke="#FFFFFF" stroke-width="7"/>"""
    },
    "coteditor": {
        "bg": ["#2B60DE", "#1F3A8A"],
        "border": "#60A5FA",
        "svg": """<rect x="36" y="30" width="56" height="68" rx="6" fill="#F8FAFC"/>
                  <line x1="46" y1="46" x2="72" y2="46" stroke="#94A3B8" stroke-width="4" stroke-linecap="round"/>
                  <line x1="46" y1="58" x2="82" y2="58" stroke="#3B82F6" stroke-width="4" stroke-linecap="round"/>
                  <line x1="46" y1="70" x2="78" y2="70" stroke="#94A3B8" stroke-width="4" stroke-linecap="round"/>
                  <line x1="46" y1="82" x2="64" y2="82" stroke="#94A3B8" stroke-width="4" stroke-linecap="round"/>
                  <path d="M86 36 L94 28 L98 32 L90 40 Z" fill="#F59E0B"/>"""
    },
    "macvim": {
        "bg": ["#0B7A3E", "#044E25"],
        "border": "#34D399",
        "svg": """<path d="M40 36 L64 88 L74 68 L88 36 Z" fill="#10B981" opacity="0.3"/>
                  <path d="M38 36 L64 92 L76 68 L90 36" fill="none" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
                  <circle cx="64" cy="46" r="6" fill="#FCD34D"/>"""
    },
    "bruno": {
        "bg": ["#F59E0B", "#B45309"],
        "border": "#FBBF24",
        "svg": """<circle cx="64" cy="64" r="28" fill="#FEF3C7"/>
                  <circle cx="54" cy="60" r="4" fill="#78350F"/>
                  <circle cx="74" cy="60" r="4" fill="#78350F"/>
                  <path d="M60 70 Q64 74 68 70" fill="none" stroke="#78350F" stroke-width="3" stroke-linecap="round"/>
                  <ellipse cx="44" cy="50" rx="6" ry="12" fill="#92400E" transform="rotate(-20 44 50)"/>
                  <ellipse cx="84" cy="50" rx="6" ry="12" fill="#92400E" transform="rotate(20 84 50)"/>"""
    },
    "gitup": {
        "bg": ["#4F46E5", "#312E81"],
        "border": "#818CF8",
        "svg": """<circle cx="46" cy="84" r="8" fill="#F43F5E"/>
                  <circle cx="46" cy="44" r="8" fill="#10B981"/>
                  <circle cx="82" cy="56" r="8" fill="#38BDF8"/>
                  <path d="M46 76 L46 52" stroke="#FFFFFF" stroke-width="4"/>
                  <path d="M46 76 C46 64, 82 68, 82 64" fill="none" stroke="#FFFFFF" stroke-width="4"/>"""
    },
    "beekeeper-studio": {
        "bg": ["#F59E0B", "#D97706"],
        "border": "#FDE68A",
        "svg": """<polygon points="64,30 92,46 92,78 64,94 36,78 36,46" fill="#1F2937"/>
                  <ellipse cx="64" cy="52" rx="16" ry="6" fill="#FBBF24"/>
                  <path d="M48 52 v14 c0 3 7 6 16 6 s16 -3 16 -6 v-14" fill="none" stroke="#FBBF24" stroke-width="3"/>
                  <path d="M48 66 v14 c0 3 7 6 16 6 s16 -3 16 -6 v-14" fill="none" stroke="#FBBF24" stroke-width="3"/>"""
    },
    "colima": {
        "bg": ["#0284C7", "#0369A1"],
        "border": "#38BDF8",
        "svg": """<rect x="40" y="44" width="48" height="36" rx="6" fill="#E0F2FE"/>
                  <line x1="56" y1="44" x2="56" y2="80" stroke="#0284C7" stroke-width="3"/>
                  <line x1="72" y1="44" x2="72" y2="80" stroke="#0284C7" stroke-width="3"/>
                  <line x1="40" y1="62" x2="88" y2="62" stroke="#0284C7" stroke-width="3"/>
                  <circle cx="64" cy="92" r="4" fill="#38BDF8"/>"""
    },
    "podman-desktop": {
        "bg": ["#8B5CF6", "#6D28D9"],
        "border": "#C4B5FD",
        "svg": """<path d="M64 34 C44 34, 36 50, 36 66 C36 82, 48 94, 64 94 C80 94, 92 82, 92 66 C92 50, 84 34, 64 34 Z" fill="#EDE9FE"/>
                  <ellipse cx="54" cy="62" rx="4" ry="6" fill="#6D28D9"/>
                  <ellipse cx="74" cy="62" rx="4" ry="6" fill="#6D28D9"/>
                  <ellipse cx="64" cy="74" rx="8" ry="4" fill="#6D28D9"/>"""
    },
    "iterm2": {
        "bg": ["#18181B", "#09090B"],
        "border": "#3F3F46",
        "svg": """<rect x="24" y="28" width="80" height="72" rx="8" fill="#18181B" stroke="#52525B" stroke-width="3"/>
                  <circle cx="34" cy="38" r="3" fill="#EF4444"/>
                  <circle cx="44" cy="38" r="3" fill="#F59E0B"/>
                  <circle cx="54" cy="38" r="3" fill="#10B981"/>
                  <path d="M38 54 L52 64 L38 74" fill="none" stroke="#22C55E" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                  <line x1="58" y1="74" x2="76" y2="74" stroke="#22C55E" stroke-width="5" stroke-linecap="round"/>"""
    },
    "ghostty": {
        "bg": ["#000000", "#111111"],
        "border": "#22C55E",
        "svg": """<path d="M64 34 C46 34, 38 48, 38 66 L38 88 L46 80 L54 88 L64 80 L74 88 L82 80 L90 88 L90 66 C90 48, 82 34, 64 34 Z" fill="#22C55E"/>
                  <circle cx="52" cy="56" r="5" fill="#000000"/>
                  <circle cx="76" cy="56" r="5" fill="#000000"/>"""
    },
    "alacritty": {
        "bg": ["#F97316", "#C2410C"],
        "border": "#FDBA74",
        "svg": """<path d="M64 32 L88 88 L72 88 L64 68 L56 88 L40 88 Z" fill="#FFFFFF"/>
                  <path d="M64 48 L70 64 L58 64 Z" fill="#C2410C"/>"""
    },
    "kitty": {
        "bg": ["#0284C7", "#0F172A"],
        "border": "#38BDF8",
        "svg": """<polygon points="40,44 48,64 36,64" fill="#38BDF8"/>
                  <polygon points="88,44 80,64 92,64" fill="#38BDF8"/>
                  <ellipse cx="64" cy="68" rx="26" ry="20" fill="#38BDF8"/>
                  <circle cx="54" cy="66" r="4" fill="#0F172A"/>
                  <circle cx="74" cy="66" r="4" fill="#0F172A"/>
                  <line x1="42" y1="72" x2="30" y2="70" stroke="#0F172A" stroke-width="2"/>
                  <line x1="86" y1="72" x2="98" y2="70" stroke="#0F172A" stroke-width="2"/>"""
    },
    "wezterm": {
        "bg": ["#4F46E5", "#3730A3"],
        "border": "#818CF8",
        "svg": """<rect x="30" y="32" width="68" height="64" rx="8" fill="#1E1B4B" stroke="#818CF8" stroke-width="3"/>
                  <path d="M42 48 L56 60 L42 72" fill="none" stroke="#F43F5E" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                  <line x1="62" y1="72" x2="80" y2="72" stroke="#38BDF8" stroke-width="5" stroke-linecap="round"/>"""
    },
    "starship": {
        "bg": ["#9333EA", "#6B21A8"],
        "border": "#D8B4FE",
        "svg": """<path d="M64 32 C64 32, 50 48, 50 68 L50 82 L64 76 L78 82 L78 68 C78 48, 64 32, 64 32 Z" fill="#FFFFFF"/>
                  <circle cx="64" cy="54" r="6" fill="#9333EA"/>
                  <polygon points="50,74 38,82 46,68" fill="#F43F5E"/>
                  <polygon points="78,74 90,82 82,68" fill="#F43F5E"/>
                  <polygon points="60,80 64,92 68,80" fill="#FBBF24"/>"""
    },
    "zellij": {
        "bg": ["#D97706", "#78350F"],
        "border": "#FCD34D",
        "svg": """<rect x="32" y="32" width="30" height="64" rx="4" fill="#FCD34D"/>
                  <rect x="66" y="32" width="30" height="30" rx="4" fill="#FCD34D"/>
                  <rect x="66" y="66" width="30" height="30" rx="4" fill="#FCD34D"/>"""
    },
    "rectangle": {
        "bg": ["#6366F1", "#4338CA"],
        "border": "#A5B4FC",
        "svg": """<rect x="30" y="34" width="68" height="60" rx="6" fill="#312E81" stroke="#A5B4FC" stroke-width="3"/>
                  <rect x="36" y="40" width="26" height="48" rx="3" fill="#818CF8"/>
                  <rect x="66" y="40" width="26" height="48" rx="3" fill="#4338CA"/>"""
    },
    "aerospace": {
        "bg": ["#0284C7", "#075985"],
        "border": "#7DD3FC",
        "svg": """<polygon points="64,30 96,88 64,74 32,88" fill="#BAE6FD"/>
                  <polygon points="64,48 80,78 64,70 48,78" fill="#0284C7"/>"""
    },
    "yabai": {
        "bg": ["#18181B", "#27272A"],
        "border": "#E4E4E7",
        "svg": """<rect x="32" y="32" width="28" height="28" rx="4" fill="#F43F5E"/>
                  <rect x="68" y="32" width="28" height="40" rx="4" fill="#38BDF8"/>
                  <rect x="32" y="68" width="28" height="28" rx="4" fill="#A855F7"/>
                  <rect x="68" y="80" width="28" height="16" rx="4" fill="#10B981"/>"""
    },
    "amethyst": {
        "bg": ["#7C3AED", "#5B21B6"],
        "border": "#C4B5FD",
        "svg": """<polygon points="64,32 92,52 82,90 46,90 36,52" fill="#DDD6FE"/>
                  <polygon points="64,44 82,56 74,80 54,80 46,56" fill="#7C3AED"/>"""
    },
    "maccy": {
        "bg": ["#DC2626", "#991B1B"],
        "border": "#FCA5A5",
        "svg": """<rect x="36" y="36" width="56" height="64" rx="8" fill="#FEE2E2"/>
                  <rect x="48" y="30" width="32" height="12" rx="4" fill="#DC2626"/>
                  <line x1="48" y1="56" x2="80" y2="56" stroke="#DC2626" stroke-width="4" stroke-linecap="round"/>
                  <line x1="48" y1="68" x2="72" y2="68" stroke="#DC2626" stroke-width="4" stroke-linecap="round"/>
                  <line x1="48" y1="80" x2="76" y2="80" stroke="#DC2626" stroke-width="4" stroke-linecap="round"/>"""
    },
    "alt-tab-macos": {
        "bg": ["#0284C7", "#0369A1"],
        "border": "#7DD3FC",
        "svg": """<rect x="30" y="44" width="40" height="34" rx="4" fill="#0C4A6E" stroke="#38BDF8" stroke-width="3"/>
                  <rect x="58" y="50" width="40" height="34" rx="4" fill="#E0F2FE" stroke="#0284C7" stroke-width="3"/>
                  <path d="M46 36 L70 36 L64 30 M70 36 L64 42" stroke="#FDE047" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>"""
    },
    "ice": {
        "bg": ["#0EA5E9", "#0284C7"],
        "border": "#BAE6FD",
        "svg": """<rect x="38" y="38" width="52" height="52" rx="10" fill="#E0F2FE" opacity="0.9"/>
                  <path d="M38 56 L64 64 L90 56 M64 64 L64 90" stroke="#0284C7" stroke-width="3"/>
                  <circle cx="50" cy="50" r="3" fill="#38BDF8"/>"""
    },
    "hidden-bar": {
        "bg": ["#334155", "#0F172A"],
        "border": "#64748B",
        "svg": """<rect x="28" y="48" width="72" height="32" rx="6" fill="#1E293B" stroke="#64748B" stroke-width="2"/>
                  <circle cx="42" cy="64" r="4" fill="#94A3B8"/>
                  <circle cx="54" cy="64" r="4" fill="#94A3B8"/>
                  <path d="M76 56 L68 64 L76 72" fill="none" stroke="#38BDF8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>"""
    },
    "sol": {
        "bg": ["#F59E0B", "#D97706"],
        "border": "#FDE68A",
        "svg": """<circle cx="64" cy="64" r="16" fill="#FEF3C7"/>
                  <line x1="64" y1="36" x2="64" y2="44" stroke="#FEF3C7" stroke-width="4" stroke-linecap="round"/>
                  <line x1="64" y1="84" x2="64" y2="92" stroke="#FEF3C7" stroke-width="4" stroke-linecap="round"/>
                  <line x1="36" y1="64" x2="44" y2="64" stroke="#FEF3C7" stroke-width="4" stroke-linecap="round"/>
                  <line x1="84" y1="64" x2="92" y2="64" stroke="#FEF3C7" stroke-width="4" stroke-linecap="round"/>"""
    },
    "linearmouse": {
        "bg": ["#3B82F6", "#1D4ED8"],
        "border": "#93C5FD",
        "svg": """<rect x="44" y="32" width="40" height="64" rx="20" fill="#EFF6FF" stroke="#1D4ED8" stroke-width="3"/>
                  <line x1="64" y1="32" x2="64" y2="54" stroke="#1D4ED8" stroke-width="3"/>
                  <rect x="61" y="42" width="6" height="12" rx="3" fill="#3B82F6"/>"""
    },
    "kap": {
        "bg": ["#10B981", "#047857"],
        "border": "#6EE7B7",
        "svg": """<circle cx="64" cy="64" r="28" fill="none" stroke="#FFFFFF" stroke-width="6"/>
                  <circle cx="64" cy="64" r="14" fill="#EF4444"/>"""
    },
    "flameshot": {
        "bg": ["#EA580C", "#9A3412"],
        "border": "#FDBA74",
        "svg": """<path d="M64 30 C52 46 44 60 44 72 C44 86 52 94 64 94 C76 94 84 86 84 72 C84 60 76 46 64 30 Z" fill="#FDE047"/>
                  <path d="M64 50 C58 60 54 68 54 76 C54 82 58 86 64 86 C70 86 74 82 74 76 C74 68 70 60 64 50 Z" fill="#EF4444"/>"""
    },
    "stats": {
        "bg": ["#1E293B", "#0F172A"],
        "border": "#475569",
        "svg": """<rect x="28" y="32" width="72" height="64" rx="8" fill="#111827" stroke="#374151" stroke-width="2"/>
                  <path d="M36 74 L48 56 L60 68 L74 46 L92 62" fill="none" stroke="#10B981" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                  <circle cx="74" cy="46" r="3" fill="#34D399"/>"""
    },
    "pearcleaner": {
        "bg": ["#84CC16", "#4D7C0F"],
        "border": "#BEF264",
        "svg": """<ellipse cx="64" cy="70" rx="22" ry="20" fill="#ECFCCB"/>
                  <ellipse cx="64" cy="50" rx="14" ry="14" fill="#ECFCCB"/>
                  <path d="M64 36 C64 30, 72 26, 76 24" fill="none" stroke="#78350F" stroke-width="4" stroke-linecap="round"/>
                  <path d="M66 32 C72 32, 78 28, 80 26 C80 32, 74 34, 66 32 Z" fill="#84CC16"/>"""
    },
    "monitorcontrol": {
        "bg": ["#475569", "#1E293B"],
        "border": "#94A3B8",
        "svg": """<rect x="32" y="34" width="64" height="44" rx="4" fill="#0F172A" stroke="#94A3B8" stroke-width="3"/>
                  <rect x="58" y="78" width="12" height="12" fill="#94A3B8"/>
                  <line x1="50" y1="90" x2="78" y2="90" stroke="#94A3B8" stroke-width="4" stroke-linecap="round"/>
                  <circle cx="64" cy="56" r="8" fill="#F59E0B"/>"""
    },
    "latest": {
        "bg": ["#0284C7", "#0369A1"],
        "border": "#38BDF8",
        "svg": """<circle cx="64" cy="64" r="26" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-dasharray="120" stroke-dashoffset="20"/>
                  <polygon points="76,38 88,44 76,50" fill="#FFFFFF"/>"""
    },
    "keka": {
        "bg": ["#059669", "#064E3B"],
        "border": "#6EE7B7",
        "svg": """<ellipse cx="64" cy="64" rx="26" ry="22" fill="#D1FAE5"/>
                  <circle cx="54" cy="60" r="4" fill="#065F46"/>
                  <circle cx="74" cy="60" r="4" fill="#065F46"/>
                  <line x1="64" y1="42" x2="64" y2="86" stroke="#059669" stroke-width="3" stroke-dasharray="4 2"/>"""
    },
    "homebrew": {
        "bg": ["#D97706", "#B45309"],
        "border": "#FDE68A",
        "svg": """<rect x="44" y="44" width="36" height="46" rx="6" fill="#F59E0B"/>
                  <path d="M80 50 h12 a6 6 0 0 1 6 6 v14 a6 6 0 0 1 -6 6 h-12" fill="none" stroke="#F59E0B" stroke-width="5"/>
                  <rect x="40" y="34" width="44" height="14" rx="6" fill="#FFFFFF"/>
                  <ellipse cx="62" cy="40" rx="18" ry="6" fill="#FFFFFF"/>"""
    },
    "ollama": {
        "bg": ["#18181B", "#09090B"],
        "border": "#52525B",
        "svg": """<ellipse cx="64" cy="74" rx="22" ry="16" fill="#FFFFFF"/>
                  <rect x="48" y="46" width="14" height="32" rx="7" fill="#FFFFFF"/>
                  <circle cx="55" cy="46" r="10" fill="#FFFFFF"/>
                  <polygon points="50,36 48,26 54,34" fill="#FFFFFF"/>
                  <polygon points="56,36 60,26 62,34" fill="#FFFFFF"/>
                  <circle cx="53" cy="44" r="2.5" fill="#09090B"/>"""
    },
    "jan": {
        "bg": ["#6366F1", "#4338CA"],
        "border": "#A5B4FC",
        "svg": """<circle cx="64" cy="64" r="26" fill="#E0E7FF"/>
                  <path d="M54 54 C54 48, 64 48, 64 58 L64 74 C64 78, 60 82, 54 82" fill="none" stroke="#4338CA" stroke-width="6" stroke-linecap="round"/>"""
    },
    "chatbox": {
        "bg": ["#0284C7", "#0369A1"],
        "border": "#38BDF8",
        "svg": """<path d="M36 42 h56 a8 8 0 0 1 8 8 v32 a8 8 0 0 1 -8 8 h-36 l-16 12 v-12 h-4 a8 8 0 0 1 -8 -8 v-32 a8 8 0 0 1 8 -8 z" fill="#F0F9FF"/>
                  <circle cx="52" cy="62" r="4" fill="#0284C7"/>
                  <circle cx="64" cy="62" r="4" fill="#0284C7"/>
                  <circle cx="76" cy="62" r="4" fill="#0284C7"/>"""
    },
    "whisper-cpp": {
        "bg": ["#10B981", "#047857"],
        "border": "#6EE7B7",
        "svg": """<line x1="38" y1="64" x2="38" y2="64" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
                  <line x1="48" y1="52" x2="48" y2="76" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
                  <line x1="58" y1="40" x2="58" y2="88" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
                  <line x1="68" y1="46" x2="68" y2="82" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
                  <line x1="78" y1="54" x2="78" y2="74" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
                  <line x1="88" y1="64" x2="88" y2="64" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>"""
    },
    "diffusionbee": {
        "bg": ["#F59E0B", "#B45309"],
        "border": "#FCD34D",
        "svg": """<ellipse cx="64" cy="64" rx="20" ry="16" fill="#FDE047"/>
                  <path d="M52 56 Q64 42 76 56" stroke="#78350F" stroke-width="3" fill="none"/>
                  <line x1="58" y1="50" x2="58" y2="78" stroke="#78350F" stroke-width="4"/>
                  <line x1="70" y1="50" x2="70" y2="78" stroke="#78350F" stroke-width="4"/>
                  <ellipse cx="50" cy="46" rx="8" ry="14" fill="#FFFFFF" opacity="0.7" transform="rotate(-30 50 46)"/>
                  <ellipse cx="78" cy="46" rx="8" ry="14" fill="#FFFFFF" opacity="0.7" transform="rotate(30 78 46)"/>"""
    },
    "iina": {
        "bg": ["#EF4444", "#B91C1C"],
        "border": "#FCA5A5",
        "svg": """<polygon points="52,42 86,64 52,86" fill="#FFFFFF"/>"""
    },
    "vlc": {
        "bg": ["#F97316", "#C2410C"],
        "border": "#FDBA74",
        "svg": """<polygon points="64,28 78,82 50,82" fill="#EA580C"/>
                  <rect x="38" y="82" width="52" height="10" rx="3" fill="#EA580C"/>
                  <polygon points="60,44 68,44 71,56 57,56" fill="#FFFFFF"/>
                  <polygon points="55,64 73,64 76,74 52,74" fill="#FFFFFF"/>"""
    },
    "handbrake": {
        "bg": ["#0284C7", "#0369A1"],
        "border": "#38BDF8",
        "svg": """<ellipse cx="64" cy="68" rx="16" ry="20" fill="#F59E0B"/>
                  <path d="M64 48 C64 36, 72 32, 76 30" stroke="#10B981" stroke-width="4" stroke-linecap="round" fill="none"/>
                  <path d="M64 48 C56 36, 48 34, 44 32" stroke="#10B981" stroke-width="4" stroke-linecap="round" fill="none"/>"""
    },
    "audacity": {
        "bg": ["#1D4ED8", "#1E3A8A"],
        "border": "#60A5FA",
        "svg": """<path d="M40 68 C34 68, 30 60, 30 50 C30 36, 44 28, 64 28 C84 28, 98 36, 98 50 C98 60, 94 68, 88 68" fill="none" stroke="#93C5FD" stroke-width="6"/>
                  <path d="M38 64 L50 48 L64 76 L76 52 L90 64" fill="none" stroke="#FBBF24" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>"""
    },
    "losslesscut": {
        "bg": ["#475569", "#1E293B"],
        "border": "#94A3B8",
        "svg": """<circle cx="50" cy="74" r="8" fill="none" stroke="#F43F5E" stroke-width="4"/>
                  <circle cx="78" cy="74" r="8" fill="none" stroke="#F43F5E" stroke-width="4"/>
                  <line x1="56" y1="68" x2="82" y2="40" stroke="#F43F5E" stroke-width="4" stroke-linecap="round"/>
                  <line x1="72" y1="68" x2="46" y2="40" stroke="#F43F5E" stroke-width="4" stroke-linecap="round"/>"""
    },
    "obs-studio": {
        "bg": ["#18181B", "#000000"],
        "border": "#71717A",
        "svg": """<circle cx="64" cy="64" r="28" fill="none" stroke="#E4E4E7" stroke-width="6"/>
                  <circle cx="64" cy="64" r="10" fill="#E4E4E7"/>
                  <circle cx="64" cy="42" r="5" fill="#E4E4E7"/>
                  <circle cx="45" cy="75" r="5" fill="#E4E4E7"/>
                  <circle cx="83" cy="75" r="5" fill="#E4E4E7"/>"""
    },
    "blackhole": {
        "bg": ["#09090B", "#000000"],
        "border": "#A855F7",
        "svg": """<circle cx="64" cy="64" r="24" fill="#000000" stroke="#C084FC" stroke-width="4"/>
                  <ellipse cx="64" cy="64" rx="36" ry="12" fill="none" stroke="#E879F9" stroke-width="3" transform="rotate(-25 64 64)"/>"""
    },
    "bitwarden": {
        "bg": ["#175DDC", "#11429E"],
        "border": "#60A5FA",
        "svg": """<path d="M64 30 L88 38 V62 C88 78, 64 92, 64 92 C64 92, 40 78, 40 62 V38 Z" fill="#FFFFFF"/>
                  <path d="M64 36 L82 43 V62 C82 74, 64 85, 64 85 C64 85, 46 74, 46 62 V43 Z" fill="#175DDC"/>
                  <circle cx="58" cy="56" r="4" fill="#FFFFFF"/>
                  <circle cx="70" cy="56" r="4" fill="#FFFFFF"/>"""
    },
    "keepassxc": {
        "bg": ["#15803D", "#166534"],
        "border": "#86EFAC",
        "svg": """<rect x="42" y="52" width="44" height="36" rx="6" fill="#DCFCE7"/>
                  <path d="M50 52 V42 C50 34, 78 34, 78 42 V52" fill="none" stroke="#DCFCE7" stroke-width="6"/>
                  <circle cx="64" cy="68" r="4" fill="#166534"/>
                  <line x1="64" y1="72" x2="64" y2="78" stroke="#166534" stroke-width="3"/>"""
    },
    "lulu": {
        "bg": ["#0284C7", "#0369A1"],
        "border": "#38BDF8",
        "svg": """<path d="M64 30 L88 40 V62 C88 78, 64 92, 64 92 C64 92, 40 78, 40 62 V40 Z" fill="#E0F2FE"/>
                  <ellipse cx="64" cy="64" rx="14" ry="12" fill="#0284C7"/>
                  <circle cx="58" cy="60" r="2.5" fill="#FFFFFF"/>
                  <circle cx="70" cy="60" r="2.5" fill="#FFFFFF"/>
                  <ellipse cx="64" cy="68" rx="4" ry="2" fill="#0C4A6E"/>"""
    },
    "knockknock": {
        "bg": ["#B45309", "#78350F"],
        "border": "#FDE68A",
        "svg": """<rect x="40" y="32" width="48" height="64" rx="4" fill="#FEF3C7" stroke="#92400E" stroke-width="3"/>
                  <circle cx="64" cy="56" r="8" fill="none" stroke="#B45309" stroke-width="4"/>
                  <circle cx="64" cy="50" r="3" fill="#B45309"/>"""
    },
    "cryptomator": {
        "bg": ["#059669", "#064E3B"],
        "border": "#6EE7B7",
        "svg": """<path d="M46 64 C40 64 36 68 36 74 C36 80 40 84 46 84 H82 C88 84 92 80 92 74 C92 68 88 64 82 64 C82 52 72 44 60 44 C52 44 46 50 46 64 Z" fill="#D1FAE5"/>
                  <rect x="56" y="66" width="16" height="14" rx="2" fill="#059669"/>
                  <path d="M59 66 V60 C59 56 69 56 69 60 V66" fill="none" stroke="#059669" stroke-width="2.5"/>"""
    },
    "tor-browser": {
        "bg": ["#7E22CE", "#581C87"],
        "border": "#D8B4FE",
        "svg": """<circle cx="64" cy="64" r="28" fill="none" stroke="#E9D5FF" stroke-width="4"/>
                  <path d="M64 36 C50 46, 50 82, 64 92" fill="none" stroke="#E9D5FF" stroke-width="4"/>
                  <path d="M64 42 C56 50, 56 78, 64 86" fill="none" stroke="#E9D5FF" stroke-width="4"/>"""
    },
    "logseq": {
        "bg": ["#0D9488", "#115E59"],
        "border": "#5EEAD4",
        "svg": """<circle cx="48" cy="48" r="8" fill="#CCFBF1"/>
                  <circle cx="80" cy="52" r="8" fill="#CCFBF1"/>
                  <circle cx="60" cy="78" r="8" fill="#CCFBF1"/>
                  <line x1="48" y1="48" x2="80" y2="52" stroke="#CCFBF1" stroke-width="4"/>
                  <line x1="48" y1="48" x2="60" y2="78" stroke="#CCFBF1" stroke-width="4"/>
                  <line x1="80" y1="52" x2="60" y2="78" stroke="#CCFBF1" stroke-width="4"/>"""
    },
    "joplin": {
        "bg": ["#1D4ED8", "#1E40AF"],
        "border": "#93C5FD",
        "svg": """<path d="M72 34 V68 C72 80, 62 86, 50 84" fill="none" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round"/>"""
    },
    "appflowy": {
        "bg": ["#4F46E5", "#312E81"],
        "border": "#A5B4FC",
        "svg": """<rect x="34" y="34" width="26" height="42" rx="4" fill="#818CF8"/>
                  <rect x="68" y="34" width="26" height="60" rx="4" fill="#C7D2FE"/>
                  <rect x="34" y="82" width="26" height="12" rx="3" fill="#818CF8"/>"""
    },
    "zettlr": {
        "bg": ["#15803D", "#166534"],
        "border": "#86EFAC",
        "svg": """<path d="M42 42 H86 L48 86 H86" fill="none" stroke="#DCFCE7" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>"""
    },
    "marktext": {
        "bg": ["#475569", "#1E293B"],
        "border": "#94A3B8",
        "svg": """<path d="M38 76 V52 L50 64 L62 52 V76" fill="none" stroke="#F8FAFC" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M76 54 V74 M70 68 L76 74 L82 68" fill="none" stroke="#38BDF8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>"""
    },
    "localsend": {
        "bg": ["#0284C7", "#0369A1"],
        "border": "#38BDF8",
        "svg": """<path d="M36 64 L88 36 L68 88 L58 70 Z" fill="#E0F2FE"/>
                  <line x1="88" y1="36" x2="58" y2="70" stroke="#0284C7" stroke-width="3"/>"""
    },
    "cyberduck": {
        "bg": ["#EAB308", "#CA8A04"],
        "border": "#FEF08A",
        "svg": """<ellipse cx="64" cy="70" rx="22" ry="16" fill="#FEF9C3"/>
                  <circle cx="54" cy="54" r="12" fill="#FEF9C3"/>
                  <polygon points="42,54 32,58 42,62" fill="#F97316"/>
                  <circle cx="50" cy="50" r="3" fill="#1F2937"/>"""
    },
    "transmission": {
        "bg": ["#DC2626", "#991B1B"],
        "border": "#FCA5A5",
        "svg": """<circle cx="64" cy="64" r="26" fill="none" stroke="#FFFFFF" stroke-width="6"/>
                  <circle cx="64" cy="64" r="8" fill="#FFFFFF"/>
                  <line x1="64" y1="38" x2="64" y2="56" stroke="#FFFFFF" stroke-width="6"/>
                  <line x1="64" y1="72" x2="64" y2="90" stroke="#FFFFFF" stroke-width="6"/>
                  <line x1="38" y1="64" x2="56" y2="64" stroke="#FFFFFF" stroke-width="6"/>
                  <line x1="72" y1="64" x2="90" y2="64" stroke="#FFFFFF" stroke-width="6"/>"""
    },
    "syncthing-macos": {
        "bg": ["#0284C7", "#075985"],
        "border": "#7DD3FC",
        "svg": """<circle cx="64" cy="64" r="28" fill="none" stroke="#BAE6FD" stroke-width="4"/>
                  <circle cx="64" cy="44" r="6" fill="#38BDF8"/>
                  <circle cx="48" cy="74" r="6" fill="#38BDF8"/>
                  <circle cx="80" cy="74" r="6" fill="#38BDF8"/>
                  <line x1="64" y1="44" x2="48" y2="74" stroke="#BAE6FD" stroke-width="3"/>
                  <line x1="64" y1="44" x2="80" y2="74" stroke="#BAE6FD" stroke-width="3"/>
                  <line x1="48" y1="74" x2="80" y2="74" stroke="#BAE6FD" stroke-width="3"/>"""
    },
    "blender": {
        "bg": ["#EA580C", "#9A3412"],
        "border": "#FDBA74",
        "svg": """<circle cx="64" cy="64" r="16" fill="#0284C7"/>
                  <circle cx="64" cy="64" r="8" fill="#FFFFFF"/>
                  <line x1="64" y1="48" x2="64" y2="30" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>
                  <line x1="50" y1="56" x2="34" y2="44" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>
                  <line x1="78" y1="56" x2="94" y2="44" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>"""
    },
    "inkscape": {
        "bg": ["#18181B", "#27272A"],
        "border": "#A1A1AA",
        "svg": """<polygon points="64,30 92,86 36,86" fill="#F4F4F5"/>
                  <polygon points="64,30 76,54 64,60 52,54" fill="#000000"/>"""
    },
    "gimp": {
        "bg": ["#475569", "#334155"],
        "border": "#94A3B8",
        "svg": """<ellipse cx="60" cy="64" rx="24" ry="18" fill="#F1F5F9"/>
                  <circle cx="52" cy="58" r="4" fill="#0F172A"/>
                  <circle cx="70" cy="60" r="3" fill="#0F172A"/>
                  <line x1="68" y1="74" x2="92" y2="50" stroke="#D97706" stroke-width="5" stroke-linecap="round"/>"""
    },
    "krita": {
        "bg": ["#BE185D", "#831843"],
        "border": "#F472B6",
        "svg": """<path d="M40 76 C32 60, 44 38, 64 38 C84 38, 96 52, 92 72 C88 88, 52 90, 40 76 Z" fill="#FCE7F3"/>
                  <circle cx="52" cy="50" r="4" fill="#0284C7"/>
                  <circle cx="68" cy="48" r="4" fill="#10B981"/>
                  <circle cx="80" cy="60" r="4" fill="#F59E0B"/>"""
    },
    "karabiner-elements": {
        "bg": ["#DC2626", "#991B1B"],
        "border": "#FCA5A5",
        "svg": """<rect x="34" y="34" width="60" height="60" rx="8" fill="#FEE2E2" stroke="#B91C1C" stroke-width="4"/>
                  <text x="64" y="74" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="34" font-weight="bold" fill="#DC2626" text-anchor="middle">⌘</text>"""
    },
    "sketchybar": {
        "bg": ["#1E293B", "#0F172A"],
        "border": "#38BDF8",
        "svg": """<rect x="26" y="52" width="76" height="24" rx="6" fill="#0F172A" stroke="#38BDF8" stroke-width="3"/>
                  <circle cx="38" cy="64" r="4" fill="#F43F5E"/>
                  <rect x="48" y="60" width="16" height="8" rx="2" fill="#10B981"/>
                  <rect x="70" y="60" width="22" height="8" rx="2" fill="#FBBF24"/>"""
    },
    "sensible-side-buttons": {
        "bg": ["#0284C7", "#0369A1"],
        "border": "#38BDF8",
        "svg": """<rect x="44" y="32" width="40" height="64" rx="20" fill="#E0F2FE" stroke="#0284C7" stroke-width="3"/>
                  <line x1="64" y1="32" x2="64" y2="54" stroke="#0284C7" stroke-width="3"/>
                  <rect x="38" y="46" width="6" height="10" rx="2" fill="#F43F5E"/>
                  <rect x="38" y="60" width="6" height="10" rx="2" fill="#F43F5E"/>"""
    }
}

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
  <defs>
    <linearGradient id="grad_{id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
  </defs>
  <rect x="8" y="8" width="112" height="112" rx="26" fill="url(#grad_{id})" stroke="{border}" stroke-width="3"/>
  {content}
</svg>
"""

def generate_icons():
    output_dir = "icons/project-icons"
    os.makedirs(output_dir, exist_ok=True)
    count = 0
    for project_id, spec in ICONS.items():
        svg_content = TEMPLATE.format(
            id=project_id.replace("-", "_"),
            c1=spec["bg"][0],
            c2=spec["bg"][1],
            border=spec["border"],
            content=spec["svg"].strip()
        )
        file_path = os.path.join(output_dir, f"{project_id}.svg")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(svg_content.strip() + "\n")
        count += 1
    print(f"Successfully generated {count} vector SVG icons in {output_dir}/")

if __name__ == "__main__":
    generate_icons()

