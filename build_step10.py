with open("js/main.js", "w") as file:
    file.write("""// ===================================
// 1. STICKY NAVBAR ON SCROLL
// ===================================
const navbar = document.getElementById('navbar');

function handleNavbarScroll() {
  if (window.scrollY > 20) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
}

window.addEventListener('scroll', handleNavbarScroll);
handleNavbarScroll();

// ===================================
// 2. MOBILE NAV TOGGLE
// ===================================
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

navToggle.addEventListener('click', function () {
  navLinks.classList.toggle('open');
  navToggle.classList.toggle('active');
});

// Close mobile menu when a link is clicked
document.querySelectorAll('.nav-links a').forEach(function (link) {
  link.addEventListener('click', function () {
    navLinks.classList.remove('open');
    navToggle.classList.remove('active');
  });
});

// ===================================
// 3. PORTFOLIO FILTERING
// ===================================
const filterButtons = document.querySelectorAll('.filter-btn');
const portfolioItems = document.querySelectorAll('.portfolio-item');

filterButtons.forEach(function (button) {
  button.addEventListener('click', function () {
    // Update active button state
    filterButtons.forEach(function (btn) {
      btn.classList.remove('active');
    });
    button.classList.add('active');

    const selectedFilter = button.getAttribute('data-filter');

    portfolioItems.forEach(function (item) {
      const itemCategory = item.getAttribute('data-category');

      if (selectedFilter === 'all' || selectedFilter === itemCategory) {
        item.classList.remove('hidden');
      } else {
        item.classList.add('hidden');
      }
    });
  });
});

// ===================================
// 4. SCROLL REVEAL ANIMATIONS
// ===================================
const revealTargets = document.querySelectorAll(
  '.highlight-card, .service-card, .skill-pill, .tool-item, .case-study-card, .portfolio-item, .metric, .top-content-list li'
);

revealTargets.forEach(function (el) {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
});

const observer = new IntersectionObserver(
  function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.15 }
);

revealTargets.forEach(function (el) {
  observer.observe(el);
});
""")
print("js/main.js created successfully")