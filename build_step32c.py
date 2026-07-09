with open("js/main.js", "a") as file:
    file.write("""

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
""")
print("Lightbox JavaScript added successfully")