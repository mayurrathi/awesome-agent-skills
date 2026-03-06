let originalSkills = [];
let currentCategory = 'All Skills';
let searchQuery = '';

// DOM Elements
const skillsGrid = document.getElementById('skills-grid');
const searchInput = document.getElementById('search-input');
const categoriesNav = document.getElementById('categories-nav');
const countLabel = document.getElementById('skill-count-label');
const noResults = document.getElementById('no-results');

// Modal Elements
const modalOverlay = document.getElementById('skill-modal');
const closeModalBtn = document.getElementById('close-modal-btn');
const modalTitle = document.getElementById('modal-title');
const modalCategory = document.getElementById('modal-category');
const modalDescription = document.getElementById('modal-description');
const modalPrompt = document.getElementById('modal-prompt');
const copyBtn = document.getElementById('copy-prompt-btn');

async function init() {
    try {
        const response = await fetch('skills.json');
        originalSkills = await response.json();

        // Setup UI
        createCategoryNavigation();
        renderSkills(originalSkills);
        setupEventListeners();

    } catch (error) {
        skillsGrid.innerHTML = `
            <div class="no-results">
                <h3>Error loading skills registry</h3>
                <p>Ensure you have generated the skills.json file by running: <br><code>python3 scripts/build_registry.py</code></p>
                <p style="color:var(--text-muted); font-family:monospace; margin-top:10px;">${error.message}</p>
            </div>
        `;
    }
}

function createCategoryNavigation() {
    // Extract unique categories and counts
    const categoriesMap = new Map();
    categoriesMap.set('All Skills', originalSkills.length);

    originalSkills.forEach(skill => {
        const cat = skill.category || 'Uncategorized';
        categoriesMap.set(cat, (categoriesMap.get(cat) || 0) + 1);
    });

    // Create sorted array (All Skills first, then alphabetical)
    const sortedCategories = Array.from(categoriesMap.entries()).sort((a, b) => {
        if (a[0] === 'All Skills') return -1;
        if (b[0] === 'All Skills') return 1;
        return a[0].localeCompare(b[0]);
    });

    categoriesNav.innerHTML = sortedCategories.map(([cat, count]) => `
        <a class="category-link ${cat === currentCategory ? 'active' : ''}" data-category="${cat}">
            <span>${cat}</span>
            <span class="category-count">${count}</span>
        </a>
    `).join('');
}

function renderSkills(skillsToRender) {
    countLabel.textContent = `Showing ${skillsToRender.length} skills`;

    if (skillsToRender.length === 0) {
        skillsGrid.classList.add('hidden');
        noResults.classList.remove('hidden');
        return;
    }

    skillsGrid.classList.remove('hidden');
    noResults.classList.add('hidden');

    skillsGrid.innerHTML = skillsToRender.map((skill, index) => `
        <div class="skill-card" data-index="${index}" onclick="openModal('${encodeURIComponent(JSON.stringify(skill))}')">
            <div class="skill-meta">
                <span class="tag">${skill.category || 'Uncategorized'}</span>
            </div>
            <h3>${skill.name}</h3>
            <p>${skill.description}</p>
            <div class="card-actions">
                <span style="font-size:12px; color:var(--text-muted); font-family:var(--font-mono)">${skill.id}</span>
                <button class="btn btn-icon-only">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </button>
            </div>
        </div>
    `).join('');
}

function filterSkills() {
    let filtered = originalSkills;

    // Category filter
    if (currentCategory !== 'All Skills') {
        filtered = filtered.filter(s => s.category === currentCategory);
    }

    // Search text filter
    if (searchQuery) {
        const q = searchQuery.toLowerCase();
        filtered = filtered.filter(s =>
            (s.name && s.name.toLowerCase().includes(q)) ||
            (s.description && s.description.toLowerCase().includes(q)) ||
            (s.id && s.id.toLowerCase().includes(q))
        );
    }

    renderSkills(filtered);
}

function setupEventListeners() {
    // Search input
    searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value;
        filterSkills();
    });

    // Keyboard shortcut (/) to focus search
    document.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
        if (e.key === 'Escape') {
            closeModal();
        }
    });

    // Category navigation clicks
    categoriesNav.addEventListener('click', (e) => {
        const link = e.target.closest('.category-link');
        if (!link) return;

        // Update active state
        document.querySelectorAll('.category-link').forEach(l => l.classList.remove('active'));
        link.classList.add('active');

        currentCategory = link.dataset.category;
        filterSkills();

        // On mobile, scroll up slightly
        if (window.innerWidth <= 768) {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    });

    closeModalBtn.addEventListener('click', closeModal);
    modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) closeModal();
    });
}

window.openModal = function (skillDataEncoded) {
    const skill = JSON.parse(decodeURIComponent(skillDataEncoded));

    modalTitle.textContent = skill.name;
    modalCategory.textContent = skill.category || 'Uncategorized';
    modalDescription.textContent = skill.description;

    // Render markdown prompt if marked is available, otherwise plain text
    if (window.marked && skill.prompt) {
        modalPrompt.innerHTML = marked.parse(skill.prompt);
        // Apply syntax highlighting
        if (window.hljs) {
            document.querySelectorAll('#modal-prompt blockquote, #modal-prompt pre code').forEach((block) => {
                // simple heuristic for markdown highlight
                hljs.highlightElement(block);
            });
        }
    } else {
        modalPrompt.textContent = skill.prompt || 'No prompt content available.';
    }

    // Prepare copy button
    copyBtn.onclick = () => {
        navigator.clipboard.writeText(skill.prompt).then(() => {
            const originalText = copyBtn.innerHTML;
            copyBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M20 6L9 17l-5-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Copied!';
            copyBtn.style.background = 'var(--accent-hover)';
            setTimeout(() => {
                copyBtn.innerHTML = originalText;
                copyBtn.style.background = '';
            }, 2000);
        });
    };

    // Show modal & prevent body scroll
    modalOverlay.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    modalOverlay.classList.add('hidden');
    document.body.style.overflow = '';
}

// Start app
document.addEventListener('DOMContentLoaded', init);
