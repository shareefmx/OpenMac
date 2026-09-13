/**
 * OpenMac — Client-Side Application Engine
 * High-performance search, filtering, and interaction for 1,165+ macOS apps.
 */

(function () {
  'use strict';

  // State
  let catalogData = {
    stats: {},
    categories: [],
    featured: [],
    projects: []
  };

  let categoryMap = new Map();
  let currentCategory = 'all';
  let searchQuery = '';
  let currentSort = 'stars-desc';
  let visibleLimit = 48;
  const PAGE_INCREMENT = 48;
  let filteredProjects = [];

  // DOM Elements
  const mainSearchInput = document.getElementById('main-search-input');
  const clearSearchBtn = document.getElementById('clear-search-btn');
  const quickChips = document.getElementById('quick-chips');
  const categorySelect = document.getElementById('category-select');
  const sortSelect = document.getElementById('sort-select');
  const categoriesScroll = document.getElementById('categories-scroll');
  const projectsGrid = document.getElementById('projects-grid');
  const featuredGrid = document.getElementById('featured-grid');
  const emptyState = document.getElementById('empty-state');
  const resetFiltersBtn = document.getElementById('reset-filters-btn');
  const paginationWrapper = document.getElementById('pagination-wrapper');
  const loadMoreBtn = document.getElementById('load-more-btn');
  const resultsCount = document.getElementById('results-count');
  const activeFilterBadge = document.getElementById('active-filter-badge');
  const heroBadgeText = document.getElementById('hero-badge-text');
  const themeBtn = document.getElementById('theme-btn');

  // Spotlight Modal Elements
  const spotlightBtn = document.getElementById('spotlight-btn');
  const spotlightModal = document.getElementById('spotlight-modal');
  const modalSearchInput = document.getElementById('modal-search-input');
  const modalResults = document.getElementById('modal-results');
  const modalStats = document.getElementById('modal-stats');
  const closeModalBtn = document.getElementById('close-modal-btn');
  let modalSelectedIndex = 0;
  let modalCurrentList = [];

  // Helper: Escape HTML to prevent injection
  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Helper: Format Star counts (e.g. 192096 -> 192.1k)
  function formatStars(num) {
    if (typeof num !== 'number' || isNaN(num)) return '0';
    if (num >= 1000000) return (num / 1000000).toFixed(1) + 'M';
    if (num >= 1000) return (num / 1000).toFixed(1) + 'k';
    return num.toLocaleString();
  }

  // Theme Management
  function initTheme() {
    const savedTheme = localStorage.getItem('openmac_theme') || 'system';
    document.documentElement.setAttribute('data-theme', savedTheme);
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || 'system';
    let next = 'dark';
    if (current === 'dark') {
      next = 'light';
    } else if (current === 'light') {
      next = 'dark';
    } else {
      // System default toggles to opposite of OS preference
      const isDarkOS = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      next = isDarkOS ? 'light' : 'dark';
    }
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('openmac_theme', next);
  }

  // Load Data
  async function loadSiteData() {
    try {
      const response = await fetch('./site-data.json');
      if (!response.ok) throw new Error(`HTTP error ${response.status}`);
      catalogData = await response.json();

      // Build category lookup
      catalogData.categories.forEach(cat => {
        categoryMap.set(cat.id, cat);
      });

      // Update hero badge
      if (heroBadgeText && catalogData.stats.total_projects) {
        heroBadgeText.textContent = `${catalogData.stats.total_projects.toLocaleString()} Verified macOS Apps • ${catalogData.stats.total_categories} Categories • 100% Open Source`;
      }

      // Render components
      renderFeaturedProjects();
      renderCategoryNavigation();
      populateCategorySelect();
      applyFiltersAndSort();
    } catch (err) {
      console.error('Failed to load site data:', err);
      if (resultsCount) {
        resultsCount.textContent = 'Failed to load catalog. Please refresh the page.';
      }
    }
  }

  // Render Featured Projects
  function renderFeaturedProjects() {
    if (!featuredGrid || !catalogData.featured) return;
    const items = catalogData.featured.slice(0, 10);

    featuredGrid.innerHTML = items.map(p => {
      const cat = categoryMap.get(p.category) || { name: p.category, icon: '📦' };
      const iconPath = p.icon || './icons/logo.svg';
      const webUrl = p.website && p.website !== p.github ? p.website : p.github;

      return `
        <article class="featured-card">
          <div class="card-top">
            <img class="app-icon" src="${escapeHtml(iconPath)}" alt="${escapeHtml(p.name)}" loading="lazy" onerror="this.onerror=null;this.src='./icons/logo.svg';">
            <div class="app-info">
              <div class="app-title-row">
                <h3 class="app-name" title="${escapeHtml(p.name)}">${escapeHtml(p.name)}</h3>
                <span class="app-stars" title="${p.stars.toLocaleString()} GitHub Stars">★ ${formatStars(p.stars)}</span>
              </div>
              <div class="app-category-badge">
                <span>${cat.icon}</span>
                <span>${escapeHtml(cat.name)}</span>
              </div>
            </div>
          </div>
          <p class="app-desc" title="${escapeHtml(p.description)}">${escapeHtml(p.description)}</p>
          <div class="card-tags">
            ${p.language ? `<span class="tag stack">${escapeHtml(p.language)}</span>` : ''}
            ${p.license ? `<span class="tag license">${escapeHtml(p.license)}</span>` : ''}
          </div>
          <div class="card-actions">
            <a href="${escapeHtml(p.github)}" target="_blank" rel="noopener noreferrer" class="card-btn" aria-label="GitHub repository for ${escapeHtml(p.name)}">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
              <span>GitHub</span>
            </a>
            <a href="${escapeHtml(webUrl)}" target="_blank" rel="noopener noreferrer" class="card-btn primary" aria-label="Website for ${escapeHtml(p.name)}">
              <span>Visit</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>
          </div>
        </article>
      `;
    }).join('');
  }

  // Render Horizontal Category Pills
  function renderCategoryNavigation() {
    if (!categoriesScroll || !catalogData.categories) return;

    let html = `
      <button class="cat-pill ${currentCategory === 'all' ? 'active' : ''}" data-cat="all">
        <span>All</span>
        <span class="cat-pill-count">(${catalogData.projects.length})</span>
      </button>
    `;

    catalogData.categories.forEach(cat => {
      const isActive = currentCategory === cat.id ? 'active' : '';
      html += `
        <button class="cat-pill ${isActive}" data-cat="${cat.id}">
          <span>${cat.icon}</span>
          <span>${escapeHtml(cat.name)}</span>
          <span class="cat-pill-count">(${cat.count})</span>
        </button>
      `;
    });

    categoriesScroll.innerHTML = html;

    // Attach click handlers
    categoriesScroll.querySelectorAll('.cat-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        setCategory(btn.getAttribute('data-cat'));
      });
    });
  }

  // Populate Dropdown for Mobile / Screen Readers
  function populateCategorySelect() {
    if (!categorySelect || !catalogData.categories) return;
    let options = `<option value="all">All Categories (${catalogData.projects.length})</option>`;
    catalogData.categories.forEach(cat => {
      options += `<option value="${cat.id}">${cat.icon} ${escapeHtml(cat.name)} (${cat.count})</option>`;
    });
    categorySelect.innerHTML = options;
    categorySelect.value = currentCategory;
  }

  // Category Selector Action
  function setCategory(catId) {
    currentCategory = catId;
    visibleLimit = PAGE_INCREMENT;

    // Sync UI
    if (categorySelect) categorySelect.value = catId;
    if (categoriesScroll) {
      categoriesScroll.querySelectorAll('.cat-pill').forEach(pill => {
        pill.classList.toggle('active', pill.getAttribute('data-cat') === catId);
      });
    }

    // Sync quick chips if matching
    if (quickChips) {
      quickChips.querySelectorAll('.chip').forEach(chip => {
        chip.classList.toggle('active', chip.getAttribute('data-cat') === catId);
      });
    }

    applyFiltersAndSort();
  }

  // Main Filter and Sort Engine
  function applyFiltersAndSort() {
    const query = searchQuery.trim().toLowerCase();

    filteredProjects = catalogData.projects.filter(project => {
      // Category Match
      if (currentCategory !== 'all' && project.category !== currentCategory) {
        return false;
      }

      // Search Query Match
      if (query) {
        const cat = categoryMap.get(project.category);
        const catName = cat ? cat.name.toLowerCase() : '';
        const name = (project.name || '').toLowerCase();
        const desc = (project.description || '').toLowerCase();
        const lang = (project.language || '').toLowerCase();
        const subcat = (project.subcategory || '').toLowerCase();
        const license = (project.license || '').toLowerCase();

        const match =
          name.includes(query) ||
          desc.includes(query) ||
          lang.includes(query) ||
          subcat.includes(query) ||
          license.includes(query) ||
          catName.includes(query);

        if (!match) return false;
      }

      return true;
    });

    // Sorting
    filteredProjects.sort((a, b) => {
      if (currentSort === 'stars-desc') {
        return (b.stars || 0) - (a.stars || 0);
      }
      if (currentSort === 'stars-asc') {
        return (a.stars || 0) - (b.stars || 0);
      }
      if (currentSort === 'name-asc') {
        return a.name.localeCompare(b.name, undefined, { sensitivity: 'base' });
      }
      if (currentSort === 'name-desc') {
        return b.name.localeCompare(a.name, undefined, { sensitivity: 'base' });
      }
      return 0;
    });

    renderProjectsCatalog();
  }

  // Render Projects Grid
  function renderProjectsCatalog() {
    if (!projectsGrid) return;

    const totalCount = filteredProjects.length;

    // Update Toolbar status
    if (resultsCount) {
      if (searchQuery.trim()) {
        resultsCount.textContent = `${totalCount.toLocaleString()} result${totalCount === 1 ? '' : 's'} for "${searchQuery}"`;
      } else if (currentCategory !== 'all') {
        const cat = categoryMap.get(currentCategory);
        resultsCount.textContent = `${totalCount.toLocaleString()} app${totalCount === 1 ? '' : 's'} in ${cat ? cat.name : currentCategory}`;
      } else {
        resultsCount.textContent = `${totalCount.toLocaleString()} Open-Source Applications`;
      }
    }

    if (activeFilterBadge) {
      if (currentCategory !== 'all') {
        const cat = categoryMap.get(currentCategory);
        activeFilterBadge.style.display = 'inline-block';
        activeFilterBadge.textContent = `${cat ? cat.icon + ' ' + cat.name : currentCategory}`;
      } else {
        activeFilterBadge.style.display = 'none';
      }
    }

    // Empty State Check
    if (totalCount === 0) {
      projectsGrid.innerHTML = '';
      if (emptyState) emptyState.style.display = 'block';
      if (paginationWrapper) paginationWrapper.style.display = 'none';
      return;
    }

    if (emptyState) emptyState.style.display = 'none';

    // Slice for infinite/paginated render
    const displayList = filteredProjects.slice(0, visibleLimit);

    projectsGrid.innerHTML = displayList.map(p => {
      const cat = categoryMap.get(p.category) || { name: p.category, icon: '📦' };
      const iconPath = p.icon || './icons/logo.svg';
      const webUrl = p.website && p.website !== p.github ? p.website : p.github;

      return `
        <article class="project-card">
          <div>
            <div class="card-top">
              <img class="app-icon" src="${escapeHtml(iconPath)}" alt="${escapeHtml(p.name)}" loading="lazy" onerror="this.onerror=null;this.src='./icons/logo.svg';">
              <div class="app-info">
                <div class="app-title-row">
                  <h3 class="app-name" title="${escapeHtml(p.name)}">${escapeHtml(p.name)}</h3>
                  <span class="app-stars" title="${(p.stars || 0).toLocaleString()} GitHub Stars">★ ${formatStars(p.stars || 0)}</span>
                </div>
                <div class="app-category-badge">
                  <span>${cat.icon}</span>
                  <span>${escapeHtml(cat.name)}</span>
                </div>
              </div>
            </div>
            <p class="app-desc" title="${escapeHtml(p.description)}">${escapeHtml(p.description)}</p>
          </div>
          <div>
            <div class="card-tags">
              ${p.language ? `<span class="tag stack">${escapeHtml(p.language)}</span>` : ''}
              ${p.subcategory ? `<span class="tag subcat">${escapeHtml(p.subcategory)}</span>` : ''}
              ${p.license ? `<span class="tag license">${escapeHtml(p.license)}</span>` : ''}
            </div>
            <div class="card-actions">
              <a href="${escapeHtml(p.github)}" target="_blank" rel="noopener noreferrer" class="card-btn" aria-label="GitHub repository for ${escapeHtml(p.name)}">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
                <span>GitHub</span>
              </a>
              <a href="${escapeHtml(webUrl)}" target="_blank" rel="noopener noreferrer" class="card-btn primary" aria-label="Website for ${escapeHtml(p.name)}">
                <span>Website</span>
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
              </a>
            </div>
          </div>
        </article>
      `;
    }).join('');

    // Pagination / Load More Button
    if (paginationWrapper && loadMoreBtn) {
      if (visibleLimit < totalCount) {
        paginationWrapper.style.display = 'flex';
        loadMoreBtn.querySelector('span').textContent = `Load More (${totalCount - visibleLimit} remaining)`;
      } else {
        paginationWrapper.style.display = 'none';
      }
    }
  }

  // Spotlight Search Modal Functionality
  function openSpotlight() {
    if (!spotlightModal) return;
    spotlightModal.classList.add('open');
    spotlightModal.setAttribute('aria-hidden', 'false');
    if (modalSearchInput) {
      modalSearchInput.value = '';
      modalSearchInput.focus();
    }
    updateSpotlightResults('');
  }

  function closeSpotlight() {
    if (!spotlightModal) return;
    spotlightModal.classList.remove('open');
    spotlightModal.setAttribute('aria-hidden', 'true');
  }

  function updateSpotlightResults(query) {
    const q = query.trim().toLowerCase();
    modalSelectedIndex = 0;

    if (!q) {
      // Show top 8 featured or highest-starred
      modalCurrentList = (catalogData.featured || catalogData.projects || []).slice(0, 8);
    } else {
      modalCurrentList = (catalogData.projects || []).filter(p => {
        const name = (p.name || '').toLowerCase();
        const desc = (p.description || '').toLowerCase();
        const lang = (p.language || '').toLowerCase();
        const cat = categoryMap.get(p.category);
        const catName = cat ? cat.name.toLowerCase() : '';
        return name.includes(q) || desc.includes(q) || lang.includes(q) || catName.includes(q);
      }).slice(0, 10);
    }

    if (modalStats) {
      modalStats.textContent = q ? `${modalCurrentList.length} matches` : 'Top suggestions';
    }

    if (modalCurrentList.length === 0) {
      modalResults.innerHTML = `
        <div style="padding: 2rem; text-align: center; color: var(--text-tertiary); font-size: 0.875rem;">
          No matching applications found for "${escapeHtml(q)}"
        </div>
      `;
      return;
    }

    modalResults.innerHTML = modalCurrentList.map((p, idx) => {
      const cat = categoryMap.get(p.category) || { name: p.category, icon: '📦' };
      const iconPath = p.icon || './icons/logo.svg';
      const isSelected = idx === modalSelectedIndex ? 'active' : '';

      return `
        <div class="modal-item ${isSelected}" data-index="${idx}" role="button" tabindex="0">
          <div class="modal-item-left">
            <img class="modal-app-icon" src="${escapeHtml(iconPath)}" alt="${escapeHtml(p.name)}" onerror="this.onerror=null;this.src='./icons/logo.svg';">
            <div>
              <div class="modal-app-name">${escapeHtml(p.name)}</div>
              <div class="modal-app-desc">${escapeHtml(p.description)}</div>
            </div>
          </div>
          <div class="modal-item-right">
            <span class="tag stack" style="font-size: 0.7rem;">${cat.icon} ${escapeHtml(cat.name)}</span>
            <span class="app-stars" style="font-size: 0.72rem;">★ ${formatStars(p.stars || 0)}</span>
          </div>
        </div>
      `;
    }).join('');

    // Attach click events
    modalResults.querySelectorAll('.modal-item').forEach(item => {
      item.addEventListener('click', () => {
        const idx = parseInt(item.getAttribute('data-index'), 10);
        selectSpotlightItem(idx);
      });
    });
  }

  function selectSpotlightItem(index) {
    const item = modalCurrentList[index];
    if (item && item.github) {
      window.open(item.github, '_blank', 'noopener,noreferrer');
      closeSpotlight();
    }
  }

  function handleSpotlightKeydown(e) {
    if (!spotlightModal.classList.contains('open')) return;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (modalCurrentList.length > 0) {
        modalSelectedIndex = (modalSelectedIndex + 1) % modalCurrentList.length;
        refreshModalSelection();
      }
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (modalCurrentList.length > 0) {
        modalSelectedIndex = (modalSelectedIndex - 1 + modalCurrentList.length) % modalCurrentList.length;
        refreshModalSelection();
      }
    } else if (e.key === 'Enter') {
      e.preventDefault();
      selectSpotlightItem(modalSelectedIndex);
    } else if (e.key === 'Escape') {
      e.preventDefault();
      closeSpotlight();
    }
  }

  function refreshModalSelection() {
    const items = modalResults.querySelectorAll('.modal-item');
    items.forEach((item, idx) => {
      item.classList.toggle('active', idx === modalSelectedIndex);
      if (idx === modalSelectedIndex) {
        item.scrollIntoView({ block: 'nearest' });
      }
    });
  }

  // Setup Event Listeners
  function setupEventListeners() {
    // Theme Toggle
    if (themeBtn) {
      themeBtn.addEventListener('click', toggleTheme);
    }

    // Main Search Input
    if (mainSearchInput) {
      mainSearchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value;
        visibleLimit = PAGE_INCREMENT;
        if (clearSearchBtn) {
          clearSearchBtn.style.display = searchQuery ? 'block' : 'none';
        }
        applyFiltersAndSort();
      });
    }

    // Clear Search Button
    if (clearSearchBtn) {
      clearSearchBtn.addEventListener('click', () => {
        if (mainSearchInput) mainSearchInput.value = '';
        searchQuery = '';
        clearSearchBtn.style.display = 'none';
        visibleLimit = PAGE_INCREMENT;
        applyFiltersAndSort();
        if (mainSearchInput) mainSearchInput.focus();
      });
    }

    // Quick Chips in Hero
    if (quickChips) {
      quickChips.querySelectorAll('.chip').forEach(chip => {
        chip.addEventListener('click', () => {
          const cat = chip.getAttribute('data-cat');
          setCategory(cat);
          const catalogSection = document.getElementById('catalog-section');
          if (catalogSection) {
            catalogSection.scrollIntoView({ behavior: 'smooth' });
          }
        });
      });
    }

    // Category Select Dropdown
    if (categorySelect) {
      categorySelect.addEventListener('change', (e) => {
        setCategory(e.target.value);
      });
    }

    // Sort Select Dropdown
    if (sortSelect) {
      sortSelect.addEventListener('change', (e) => {
        currentSort = e.target.value;
        applyFiltersAndSort();
      });
    }

    // Reset Filters Button in Empty State
    if (resetFiltersBtn) {
      resetFiltersBtn.addEventListener('click', () => {
        searchQuery = '';
        currentCategory = 'all';
        if (mainSearchInput) mainSearchInput.value = '';
        if (clearSearchBtn) clearSearchBtn.style.display = 'none';
        setCategory('all');
      });
    }

    // Load More Button
    if (loadMoreBtn) {
      loadMoreBtn.addEventListener('click', () => {
        visibleLimit += PAGE_INCREMENT;
        renderProjectsCatalog();
      });
    }

    // Spotlight Trigger Button
    if (spotlightBtn) {
      spotlightBtn.addEventListener('click', openSpotlight);
    }

    // Spotlight Input
    if (modalSearchInput) {
      modalSearchInput.addEventListener('input', (e) => {
        updateSpotlightResults(e.target.value);
      });
    }

    // Spotlight Modal Close
    if (closeModalBtn) {
      closeModalBtn.addEventListener('click', closeSpotlight);
    }

    if (spotlightModal) {
      spotlightModal.addEventListener('click', (e) => {
        if (e.target === spotlightModal) {
          closeSpotlight();
        }
      });
    }

    // Global Keybindings (⌘K, Ctrl+K, /, ESC)
    window.addEventListener('keydown', (e) => {
      // ⌘K or Ctrl+K
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (spotlightModal.classList.contains('open')) {
          closeSpotlight();
        } else {
          openSpotlight();
        }
        return;
      }

      // '/' to focus search if not in an input
      if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        openSpotlight();
        return;
      }

      // Handle arrows/enter in modal
      if (spotlightModal && spotlightModal.classList.contains('open')) {
        handleSpotlightKeydown(e);
      }
    });
  }

  // Initialization
  function init() {
    initTheme();
    setupEventListeners();
    loadSiteData();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
