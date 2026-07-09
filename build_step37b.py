with open("js/main.js", "a") as file:
    file.write("""

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
""")
print("Portfolio lightbox JavaScript added successfully")