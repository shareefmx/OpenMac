#!/usr/bin/env python3
"""
Builds the OpenMac interactive web search application in docs/index.html
and index.html, pre-populated with canonical catalog data.
Features an instant macOS Spotlight-style search bar with a live
Top-4 auto-suggest dropdown menu as you type.
"""

import os
import json
import yaml

PROJECTS_FILE = "data/projects.yml"
CATEGORIES_FILE = "data/categories.yml"
OUTPUT_HTML = "docs/index.html"
ROOT_HTML = "index.html"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OpenMac — The Open-Source macOS Directory</title>
  <meta name="description" content="Discover 1,165+ genuine open-source macOS apps, developer tools, and system utilities. Searchable, verified, and community-driven.">
  <link rel="icon" type="image/svg+xml" href="./icons/logo.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0d1117;
      --bg-card: rgba(22, 27, 34, 0.75);
      --bg-card-hover: rgba(33, 38, 45, 0.9);
      --border: rgba(240, 246, 252, 0.1);
      --border-focus: #58a6ff;
      --text: #f0f6fc;
      --text-muted: #8b949e;
      --accent: #2f81f7;
      --accent-glow: rgba(47, 129, 247, 0.25);
      --accent-star: #e3b341;
      --tag-bg: rgba(56, 139, 253, 0.15);
      --tag-border: rgba(56, 139, 253, 0.3);
      --glass: backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
      --font: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--font);
      min-height: 100vh;
      line-height: 1.5;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(56, 139, 253, 0.12) 0%, transparent 50%),
        radial-gradient(circle at 10% 20%, rgba(137, 87, 229, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 90% 40%, rgba(63, 185, 80, 0.06) 0%, transparent 40%);
      background-attachment: fixed;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    header {
      padding: 2.5rem 1.5rem 1.5rem;
      text-align: center;
      max-width: 900px;
      margin: 0 auto;
    }

    .logo-container {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 0.75rem;
    }

    .logo-img {
      width: 48px;
      height: 48px;
      filter: drop-shadow(0 4px 12px rgba(47, 129, 247, 0.4));
    }

    h1 {
      font-size: 2.5rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      background: linear-gradient(135deg, #ffffff 40%, #8b949e 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .subtitle {
      color: var(--text-muted);
      font-size: 1.05rem;
      max-width: 620px;
      margin: 0 auto 1.5rem;
    }

    .meta-badges {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-bottom: 2rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      font-size: 0.82rem;
      font-weight: 600;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border);
    }

    .badge.stars {
      color: var(--accent-star);
      border-color: rgba(227, 179, 65, 0.3);
      background: rgba(227, 179, 65, 0.1);
    }

    /* Search Box & Floating Dropdown Container */
    .search-wrapper {
      max-width: 680px;
      margin: 0 auto 2.5rem;
      position: relative;
      z-index: 100;
    }

    .search-input-box {
      display: flex;
      align-items: center;
      background: rgba(22, 27, 34, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 8px 16px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.05);
      transition: all 0.2s ease;
    }

    .search-input-box:focus-within {
      border-color: var(--accent);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5), 0 0 0 2px var(--accent-glow);
    }

    .search-icon {
      font-size: 1.25rem;
      margin-right: 12px;
      opacity: 0.7;
    }

    .search-input {
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      font-family: var(--font);
      font-size: 1.05rem;
      color: var(--text);
      padding: 6px 0;
    }

    .search-input::placeholder {
      color: var(--text-muted);
    }

    .hotkey-badge {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      padding: 3px 7px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--text-muted);
      user-select: none;
    }

    .clear-btn {
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.1rem;
      cursor: pointer;
      padding: 4px 8px;
      display: none;
      transition: color 0.15s ease;
    }

    .clear-btn:hover {
      color: var(--text);
    }

    /* TOP 4 SUGGESTIONS DROPDOWN MENU */
    .suggest-menu {
      position: absolute;
      top: calc(100% + 8px);
      left: 0;
      right: 0;
      background: rgba(22, 27, 34, 0.95);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 16px;
      box-shadow: 0 16px 48px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.05);
      overflow: hidden;
      display: none;
      animation: fadeInSlide 0.18s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes fadeInSlide {
      from {
        opacity: 0;
        transform: translateY(-8px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .suggest-header {
      padding: 10px 16px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.02);
    }

    .suggest-list {
      list-style: none;
    }

    .suggest-item {
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      cursor: pointer;
      transition: background 0.15s ease;
      text-decoration: none;
    }

    .suggest-item:last-child {
      border-bottom: none;
    }

    .suggest-item:hover, .suggest-item.selected {
      background: rgba(47, 129, 247, 0.15);
    }

    .suggest-icon {
      width: 36px;
      height: 36px;
      border-radius: 8px;
      object-fit: contain;
      background: rgba(255, 255, 255, 0.05);
      padding: 2px;
      flex-shrink: 0;
    }

    .suggest-info {
      flex: 1;
      min-width: 0;
    }

    .suggest-top-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 3px;
    }

    .suggest-name {
      font-weight: 700;
      font-size: 0.95rem;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .suggest-badge {
      font-size: 0.72rem;
      padding: 2px 7px;
      border-radius: 12px;
      background: var(--tag-bg);
      border: 1px solid var(--tag-border);
      color: #79c0ff;
      font-weight: 600;
    }

    .suggest-stars {
      display: flex;
      align-items: center;
      gap: 4px;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--accent-star);
      margin-left: auto;
      background: rgba(227, 179, 65, 0.12);
      padding: 2px 8px;
      border-radius: 10px;
      border: 1px solid rgba(227, 179, 65, 0.25);
    }

    .suggest-desc {
      font-size: 0.8rem;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .suggest-footer {
      padding: 8px 16px;
      background: rgba(0, 0, 0, 0.2);
      font-size: 0.72rem;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      border-top: 1px solid var(--border);
    }

    /* Category Filter Pills */
    .categories-filter {
      max-width: 1200px;
      margin: 0 auto 2rem;
      padding: 0 1.5rem;
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 10px;
      scrollbar-width: thin;
    }

    .categories-filter::-webkit-scrollbar {
      height: 6px;
    }
    .categories-filter::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.15);
      border-radius: 3px;
    }

    .filter-chip {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
      font-size: 0.84rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
      user-select: none;
    }

    .filter-chip:hover {
      background: rgba(255, 255, 255, 0.08);
      color: var(--text);
    }

    .filter-chip.active {
      background: var(--accent);
      border-color: var(--accent);
      color: #ffffff;
      box-shadow: 0 2px 10px var(--accent-glow);
    }

    /* Projects Grid */
    .main-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 1.5rem 4rem;
    }

    .results-count {
      margin-bottom: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 16px;
    }

    .card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }

    .card:hover {
      transform: translateY(-2px);
      background: var(--bg-card-hover);
      border-color: rgba(255, 255, 255, 0.2);
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.4);
    }

    .card-top {
      display: flex;
      align-items: flex-start;
      gap: 14px;
      margin-bottom: 12px;
    }

    .card-icon {
      width: 44px;
      height: 44px;
      border-radius: 10px;
      object-fit: contain;
      background: rgba(255, 255, 255, 0.04);
      padding: 3px;
      flex-shrink: 0;
    }

    .card-title-box {
      flex: 1;
      min-width: 0;
    }

    .card-name {
      font-size: 1.05rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.3;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .card-category {
      font-size: 0.72rem;
      color: var(--text-muted);
      display: inline-block;
      margin-top: 2px;
    }

    .card-stars {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--accent-star);
      background: rgba(227, 179, 65, 0.12);
      padding: 3px 8px;
      border-radius: 8px;
      border: 1px solid rgba(227, 179, 65, 0.25);
      flex-shrink: 0;
    }

    .card-desc {
      font-size: 0.88rem;
      color: #8b949e;
      line-height: 1.45;
      margin-bottom: 14px;
      flex-grow: 1;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .card-bottom {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 10px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      font-size: 0.75rem;
    }

    .card-tags {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .tag {
      padding: 2px 7px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.05);
      color: #c9d1d9;
      font-family: var(--font-mono);
      font-size: 0.72rem;
    }

    .tag.license {
      color: #7ee787;
      background: rgba(46, 160, 67, 0.15);
    }

    .card-links {
      display: flex;
      gap: 10px;
    }

    .card-link {
      color: var(--accent);
      font-weight: 600;
      transition: color 0.15s ease;
    }

    .card-link:hover {
      text-decoration: underline;
      color: #58a6ff;
    }

    /* GitHub Repo Backlink */
    .github-corner {
      position: fixed;
      top: 1.5rem;
      right: 1.5rem;
      z-index: 200;
    }

    .repo-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(22, 27, 34, 0.85);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 6px 14px;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text);
      transition: all 0.2s ease;
    }

    .repo-btn:hover {
      background: rgba(33, 38, 45, 0.95);
      border-color: rgba(255, 255, 255, 0.25);
    }

    /* Empty state */
    .empty-state {
      grid-column: 1 / -1;
      text-align: center;
      padding: 4rem 1rem;
      color: var(--text-muted);
    }
    .empty-state h3 {
      font-size: 1.25rem;
      color: var(--text);
      margin-bottom: 0.5rem;
    }

    @media (max-width: 640px) {
      h1 { font-size: 1.8rem; }
      .github-corner { top: 1rem; right: 1rem; }
      .search-wrapper { margin-bottom: 1.5rem; }
    }
  </style>
</head>
<body>

  <div class="github-corner">
    <a href="https://github.com/shareefmx/OpenMac" class="repo-btn" target="_blank" rel="noopener">
      <svg height="16" width="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path></svg>
      GitHub Repo
    </a>
  </div>

  <header>
    <div class="logo-container">
      <img src="./icons/logo.svg" alt="OpenMac" class="logo-img">
      <h1>OpenMac</h1>
    </div>
    <p class="subtitle">The community-powered directory of genuinely open-source macOS software, developer tools, and system utilities.</p>
    
    <div class="meta-badges">
      <span class="badge">📦 <strong>1,165</strong> Projects</span>
      <span class="badge">🗂️ <strong>50</strong> Categories</span>
      <span class="badge">🛡️ <strong>100%</strong> Open Source</span>
      <span class="badge stars">⭐ Ranked by Real-Time Stars</span>
    </div>

    <!-- SPOTLIGHT SEARCH & TOP-4 SUGGESTIONS -->
    <div class="search-wrapper">
      <div class="search-input-box">
        <span class="search-icon">🔍</span>
        <input 
          type="text" 
          id="searchInput" 
          class="search-input" 
          placeholder="Search 1,165 macOS apps (e.g. ollama, window manager, rust)..." 
          autocomplete="off" 
          spellcheck="false"
        >
        <button id="clearBtn" class="clear-btn" title="Clear">✕</button>
        <span class="hotkey-badge">⌘K</span>
      </div>

      <!-- SUGGESTION MENU DROPDOWN (TOP 4 MATCHES) -->
      <div id="suggestMenu" class="suggest-menu">
        <div class="suggest-header">
          <span>Top 4 Suggested Matches</span>
          <span id="suggestMatchCount">4 of 0 matches</span>
        </div>
        <ul id="suggestList" class="suggest-list">
          <!-- Populated dynamically by JavaScript -->
        </ul>
        <div class="suggest-footer">
          <span>Press <strong>Enter</strong> to filter catalog below</span>
          <span>Press <strong>Esc</strong> to close</span>
        </div>
      </div>
    </div>
  </header>

  <!-- CATEGORY FILTER CHIPS -->
  <div class="categories-filter" id="categoryChips">
    <button class="filter-chip active" data-cat="all">All Apps (1,165)</button>
    <!-- Categories populated by JS -->
  </div>

  <!-- MAIN CATALOG RESULTS GRID -->
  <main class="main-container">
    <div class="results-count">
      <span id="resultsLabel">Showing 1,165 open-source macOS apps</span>
      <span>Sorted by Stars (Highest to Lowest)</span>
    </div>

    <div class="grid" id="projectsGrid">
      <!-- Cards rendered by JS -->
    </div>
  </main>

  <script>
    const CATALOG_DATA = __CATALOG_DATA_JSON__;
    const CATEGORIES_DATA = __CATEGORIES_DATA_JSON__;

    const searchInput = document.getElementById('searchInput');
    const clearBtn = document.getElementById('clearBtn');
    const suggestMenu = document.getElementById('suggestMenu');
    const suggestList = document.getElementById('suggestList');
    const suggestMatchCount = document.getElementById('suggestMatchCount');
    const categoryChips = document.getElementById('categoryChips');
    const projectsGrid = document.getElementById('projectsGrid');
    const resultsLabel = document.getElementById('resultsLabel');

    let activeCategory = 'all';
    let currentQuery = '';
    let selectedSuggestIndex = -1;

    // Build category map
    const catMap = {};
    CATEGORIES_DATA.forEach(c => {
      catMap[c.id] = c;
    });

    // Populate Category Chips
    function initCategoryChips() {
      // Sort categories by project count descending
      const catCounts = {};
      CATALOG_DATA.forEach(p => {
        catCounts[p.category] = (catCounts[p.category] || 0) + 1;
      });

      const sortedCats = [...CATEGORIES_DATA].sort((a, b) => {
        return (catCounts[b.id] || 0) - (catCounts[a.id] || 0);
      });

      sortedCats.forEach(c => {
        const count = catCounts[c.id] || 0;
        if (count > 0) {
          const btn = document.createElement('button');
          btn.className = 'filter-chip';
          btn.dataset.cat = c.id;
          btn.innerHTML = `${c.icon || '📦'} ${c.name} (${count})`;
          btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-chip').forEach(el => el.classList.remove('active'));
            btn.classList.add('active');
            activeCategory = c.id;
            renderGrid();
          });
          categoryChips.appendChild(btn);
        }
      });
    }

    // Filter Logic
    function getFilteredProjects() {
      let list = CATALOG_DATA;

      if (activeCategory !== 'all') {
        list = list.filter(p => p.category === activeCategory);
      }

      if (currentQuery) {
        const q = currentQuery.toLowerCase();
        list = list.filter(p => {
          return p.name.toLowerCase().includes(q) ||
                 p.description.toLowerCase().includes(q) ||
                 (p.language && p.language.toLowerCase().includes(q)) ||
                 (catMap[p.category] && catMap[p.category].name.toLowerCase().includes(q));
        });
      }

      // Catalog projects are already sorted by stars descending!
      return list;
    }

    // Render Main Grid
    function renderGrid() {
      const filtered = getFilteredProjects();
      resultsLabel.textContent = `Showing ${filtered.length.toLocaleString()} open-source macOS apps`;

      if (filtered.length === 0) {
        projectsGrid.innerHTML = `
          <div class="empty-state">
            <h3>No matching Mac apps found</h3>
            <p>Try refining your search terms or selecting "All Apps".</p>
          </div>
        `;
        return;
      }

      // Render up to 100 items at a time for high performance, with infinite scroll or full display
      const displayCount = Math.min(filtered.length, 120);
      let html = '';

      for (let i = 0; i < displayCount; i++) {
        const p = filtered[i];
        const cat = catMap[p.category] || { name: p.category, icon: '📦' };
        const starsFormatted = (p.stars || 0) > 999 
          ? ((p.stars / 1000).toFixed(1).replace('.0', '') + 'k') 
          : (p.stars || 0);

        const site = p.website || p.github;
        const iconPath = p.icon || 'icons/default.svg';

        html += `
          <div class="card">
            <div class="card-top">
              <a href="${site}" target="_blank" rel="noopener">
                <img class="card-icon" src="./${iconPath}" alt="${p.name}" onerror="this.src='./icons/default.svg'">
              </a>
              <div class="card-title-box">
                <a href="${site}" target="_blank" rel="noopener" class="card-name" title="${p.name}">${p.name}</a>
                <span class="card-category">${cat.icon || '📦'} ${cat.name}</span>
              </div>
              <a href="${p.github}/stargazers" target="_blank" rel="noopener" class="card-stars" title="${(p.stars || 0).toLocaleString()} stars">
                ⭐ ${starsFormatted}
              </a>
            </div>
            <p class="card-desc">${p.description}</p>
            <div class="card-bottom">
              <div class="card-tags">
                <span class="tag">${p.language || 'Native'}</span>
                <span class="tag license">${p.license || 'OSI'}</span>
              </div>
              <div class="card-links">
                ${p.website && p.website !== p.github ? `<a href="${p.website}" target="_blank" rel="noopener" class="card-link">Website</a>` : ''}
                <a href="${p.github}" target="_blank" rel="noopener" class="card-link">Source</a>
              </div>
            </div>
          </div>
        `;
      }

      projectsGrid.innerHTML = html;
    }

    // TOP-4 SUGGESTION DROPDOWN ENGINE
    function updateSuggestions() {
      const q = searchInput.value.trim().toLowerCase();
      if (!q) {
        suggestMenu.style.display = 'none';
        clearBtn.style.display = 'none';
        return;
      }

      clearBtn.style.display = 'block';

      // Find matches in entire catalog, ranked by stars descending
      const matches = CATALOG_DATA.filter(p => {
        return p.name.toLowerCase().includes(q) ||
               p.description.toLowerCase().includes(q) ||
               (p.language && p.language.toLowerCase().includes(q)) ||
               (catMap[p.category] && catMap[p.category].name.toLowerCase().includes(q));
      });

      if (matches.length === 0) {
        suggestMenu.style.display = 'block';
        suggestMatchCount.textContent = `0 matches`;
        suggestList.innerHTML = `
          <li style="padding: 16px; text-align: center; color: var(--text-muted); font-size: 0.88rem;">
            No applications found matching "${escapeHtml(q)}"
          </li>
        `;
        return;
      }

      // Exact top 4 recommendations based on stars descending
      const top4 = matches.slice(0, 4);
      suggestMatchCount.textContent = `Top ${top4.length} of ${matches.length} matches`;

      let listHtml = '';
      top4.forEach((p, idx) => {
        const cat = catMap[p.category] || { name: p.category, icon: '📦' };
        const starsFormatted = (p.stars || 0) > 999 
          ? ((p.stars / 1000).toFixed(1).replace('.0', '') + 'k') 
          : (p.stars || 0);
        const iconPath = p.icon || 'icons/default.svg';
        const site = p.website || p.github;

        // Highlight matching query in title
        const highlightedName = highlightMatch(p.name, q);

        listHtml += `
          <li>
            <a href="${site}" target="_blank" rel="noopener" class="suggest-item ${idx === selectedSuggestIndex ? 'selected' : ''}" data-index="${idx}">
              <img src="./${iconPath}" alt="${p.name}" class="suggest-icon" onerror="this.src='./icons/default.svg'">
              <div class="suggest-info">
                <div class="suggest-top-row">
                  <span class="suggest-name">${highlightedName}</span>
                  <span class="suggest-badge">${cat.icon || '📦'} ${cat.name}</span>
                  <span class="suggest-stars">⭐ ${starsFormatted}</span>
                </div>
                <div class="suggest-desc">${escapeHtml(p.description)}</div>
              </div>
            </a>
          </li>
        `;
      });

      suggestList.innerHTML = listHtml;
      suggestMenu.style.display = 'block';
    }

    function highlightMatch(text, query) {
      if (!query) return escapeHtml(text);
      const idx = text.toLowerCase().indexOf(query);
      if (idx === -1) return escapeHtml(text);
      const before = escapeHtml(text.slice(0, idx));
      const match = escapeHtml(text.slice(idx, idx + query.length));
      const after = escapeHtml(text.slice(idx + query.length));
      return `${before}<span style="color: #58a6ff; text-decoration: underline;">${match}</span>${after}`;
    }

    function escapeHtml(str) {
      return (str || '').replace(/[&<>"']/g, m => ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      }[m]));
    }

    // Event Listeners
    searchInput.addEventListener('input', (e) => {
      currentQuery = e.target.value.trim();
      selectedSuggestIndex = -1;
      updateSuggestions();
      renderGrid();
    });

    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        suggestMenu.style.display = 'none';
        searchInput.blur();
      } else if (e.key === 'Enter') {
        suggestMenu.style.display = 'none';
        renderGrid();
      }
    });

    clearBtn.addEventListener('click', () => {
      searchInput.value = '';
      currentQuery = '';
      clearBtn.style.display = 'none';
      suggestMenu.style.display = 'none';
      renderGrid();
      searchInput.focus();
    });

    // Close suggestion menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.search-wrapper')) {
        suggestMenu.style.display = 'none';
      }
    });

    // Keyboard Hotkey (Cmd+K or Ctrl+K or /)
    document.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        searchInput.focus();
        searchInput.select();
      } else if (e.key === '/' && document.activeElement !== searchInput) {
        e.preventDefault();
        searchInput.focus();
      }
    });

    // Handle "All Apps" Chip
    document.querySelector('.filter-chip[data-cat="all"]').addEventListener('click', function() {
      document.querySelectorAll('.filter-chip').forEach(el => el.classList.remove('active'));
      this.classList.add('active');
      activeCategory = 'all';
      renderGrid();
    });

    // Initialize
    initCategoryChips();
    renderGrid();
  </script>
</body>
</html>
"""

def main():
    with open(CATEGORIES_FILE, "r", encoding="utf-8") as f:
        categories = yaml.safe_load(f).get("categories", [])

    with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
        projects = yaml.safe_load(f).get("projects", [])

    # Sort projects descending by stars
    projects.sort(key=lambda x: (-x.get("stars", 0), x["name"].lower()))

    categories_json = json.dumps(categories, ensure_ascii=False)
    projects_json = json.dumps(projects, ensure_ascii=False)

    html_content = HTML_TEMPLATE.replace("__CATEGORIES_DATA_JSON__", categories_json)
    html_content = html_content.replace("__CATALOG_DATA_JSON__", projects_json)

    os.makedirs("docs", exist_ok=True)
    import shutil
    shutil.copytree("icons", "docs/icons", dirs_exist_ok=True)

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated web search app in {OUTPUT_HTML} ({len(projects)} projects).")

    with open(ROOT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Synced root {ROOT_HTML} for root-level access.")

if __name__ == "__main__":
    main()
