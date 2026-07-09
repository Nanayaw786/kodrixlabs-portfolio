// ===================================
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


// ===================================
// 5. LIGHTBOX (SCREENSHOT VIEWER)
// ===================================
const lightbox = document.getElementById('lightbox');
const lightboxImage = document.getElementById('lightboxImage');
const lightboxClose = document.getElementById('lightboxClose');
const lightboxPrev = document.getElementById('lightboxPrev');
const lightboxNext = document.getElementById('lightboxNext');
const lightboxCounter = document.getElementById('lightboxCounter');

if (lightbox) {
  const screenshotBoxes = document.querySelectorAll('.screenshot-box img');
  const imageSources = Array.from(screenshotBoxes).map(function (img) {
    return img.getAttribute('src');
  });

  let currentIndex = 0;

  function openLightbox(index) {
    currentIndex = index;
    showImage(currentIndex);
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  function showImage(index) {
    lightboxImage.classList.remove('loaded');
    lightboxImage.src = imageSources[index];
    lightboxCounter.textContent = (index + 1) + ' / ' + imageSources.length;

    lightboxImage.onload = function () {
      lightboxImage.classList.add('loaded');
    };
  }

  function showNext() {
    currentIndex = (currentIndex + 1) % imageSources.length;
    showImage(currentIndex);
  }

  function showPrev() {
    currentIndex = (currentIndex - 1 + imageSources.length) % imageSources.length;
    showImage(currentIndex);
  }

  screenshotBoxes.forEach(function (img, index) {
    img.parentElement.addEventListener('click', function () {
      openLightbox(index);
    });
  });

  lightboxClose.addEventListener('click', closeLightbox);
  lightboxNext.addEventListener('click', showNext);
  lightboxPrev.addEventListener('click', showPrev);

  // Close when clicking the dark background (not the image itself)
  lightbox.addEventListener('click', function (event) {
    if (event.target === lightbox) {
      closeLightbox();
    }
  });

  // Keyboard navigation
  document.addEventListener('keydown', function (event) {
    if (!lightbox.classList.contains('active')) return;

    if (event.key === 'Escape') closeLightbox();
    if (event.key === 'ArrowRight') showNext();
    if (event.key === 'ArrowLeft') showPrev();
  });
}


// ===================================
// 6. LIGHTBOX FOR PORTFOLIO GRID (FILTER-AWARE)
// ===================================
const portfolioLightbox = document.getElementById('lightbox');
const portfolioGridEl = document.getElementById('portfolioGrid');

if (portfolioLightbox && portfolioGridEl && !lightboxImage) {
  // Guard: only runs on pages where the case-study lightbox script above did NOT already initialize.
}

if (portfolioGridEl) {
  const pfLightboxImage = document.getElementById('lightboxImage');
  const pfLightboxClose = document.getElementById('lightboxClose');
  const pfLightboxPrev = document.getElementById('lightboxPrev');
  const pfLightboxNext = document.getElementById('lightboxNext');
  const pfLightboxCounter = document.getElementById('lightboxCounter');

  let pfCurrentIndex = 0;
  let pfVisibleImages = [];

  function getVisiblePortfolioImages() {
    const visibleItems = Array.from(portfolioGridEl.querySelectorAll('.portfolio-item:not(.hidden) .portfolio-image img'));
    return visibleItems.map(function (img) {
      return img.getAttribute('src');
    });
  }

  function openPortfolioLightbox(clickedImg) {
    pfVisibleImages = getVisiblePortfolioImages();
    const clickedSrc = clickedImg.getAttribute('src');
    pfCurrentIndex = pfVisibleImages.indexOf(clickedSrc);
    if (pfCurrentIndex === -1) pfCurrentIndex = 0;

    showPortfolioImage(pfCurrentIndex);
    portfolioLightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closePortfolioLightbox() {
    portfolioLightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  function showPortfolioImage(index) {
    pfLightboxImage.classList.remove('loaded');
    pfLightboxImage.src = pfVisibleImages[index];
    pfLightboxCounter.textContent = (index + 1) + ' / ' + pfVisibleImages.length;

    pfLightboxImage.onload = function () {
      pfLightboxImage.classList.add('loaded');
    };
  }

  function showPortfolioNext() {
    pfCurrentIndex = (pfCurrentIndex + 1) % pfVisibleImages.length;
    showPortfolioImage(pfCurrentIndex);
  }

  function showPortfolioPrev() {
    pfCurrentIndex = (pfCurrentIndex - 1 + pfVisibleImages.length) % pfVisibleImages.length;
    showPortfolioImage(pfCurrentIndex);
  }

  portfolioGridEl.addEventListener('click', function (event) {
    const clickedImage = event.target.closest('.portfolio-image img');
    if (clickedImage) {
      openPortfolioLightbox(clickedImage);
    }
  });

  pfLightboxClose.addEventListener('click', closePortfolioLightbox);
  pfLightboxNext.addEventListener('click', showPortfolioNext);
  pfLightboxPrev.addEventListener('click', showPortfolioPrev);

  portfolioLightbox.addEventListener('click', function (event) {
    if (event.target === portfolioLightbox) {
      closePortfolioLightbox();
    }
  });

  document.addEventListener('keydown', function (event) {
    if (!portfolioLightbox.classList.contains('active')) return;

    if (event.key === 'Escape') closePortfolioLightbox();
    if (event.key === 'ArrowRight') showPortfolioNext();
    if (event.key === 'ArrowLeft') showPortfolioPrev();
  });
}


// ===================================
// 7. CONTACT FORM SUBMISSION (FORMSPREE)
// ===================================
const contactForm = document.getElementById('contactForm');

if (contactForm) {
  const formSubmitBtn = document.getElementById('formSubmitBtn');
  const formStatus = document.getElementById('formStatus');

  contactForm.addEventListener('submit', function (event) {
    event.preventDefault();

    formSubmitBtn.disabled = true;
    formSubmitBtn.textContent = 'Sending...';
    formStatus.textContent = '';
    formStatus.className = 'form-status';

    const formData = new FormData(contactForm);

    fetch(contactForm.action, {
      method: 'POST',
      body: formData,
      headers: {
        Accept: 'application/json'
      }
    })
      .then(function (response) {
        if (response.ok) {
          formStatus.textContent = "Thanks! Your message has been sent — I'll get back to you soon.";
          formStatus.classList.add('success');
          contactForm.reset();
        } else {
          formStatus.textContent = 'Something went wrong. Please try again or email me directly.';
          formStatus.classList.add('error');
        }
      })
      .catch(function () {
        formStatus.textContent = 'Something went wrong. Please try again or email me directly.';
        formStatus.classList.add('error');
      })
      .finally(function () {
        formSubmitBtn.disabled = false;
        formSubmitBtn.textContent = 'Send Message';
      });
  });
}
