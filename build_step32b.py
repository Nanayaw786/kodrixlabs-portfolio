with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   25. LIGHTBOX (SCREENSHOT VIEWER)
=================================== */
.screenshot-box {
  cursor: zoom-in;
}

.lightbox {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(10, 11, 14, 0.92);
  z-index: 2000;
  align-items: center;
  justify-content: center;
  padding: 40px;
}

.lightbox.active {
  display: flex;
}

.lightbox-image {
  max-width: 90vw;
  max-height: 85vh;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  opacity: 0;
  transform: scale(0.96);
  transition: opacity 0.25s ease, transform 0.25s ease;
}

.lightbox-image.loaded {
  opacity: 1;
  transform: scale(1);
}

.lightbox-close {
  position: absolute;
  top: 24px;
  right: 30px;
  font-size: 2.4rem;
  color: #ffffff;
  line-height: 1;
  opacity: 0.8;
  transition: var(--transition-fast);
}

.lightbox-close:hover {
  opacity: 1;
  transform: scale(1.1);
}

.lightbox-prev,
.lightbox-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font-size: 3rem;
  color: #ffffff;
  opacity: 0.8;
  padding: 10px 18px;
  transition: var(--transition-fast);
}

.lightbox-prev:hover,
.lightbox-next:hover {
  opacity: 1;
  transform: translateY(-50%) scale(1.15);
}

.lightbox-prev {
  left: 10px;
}

.lightbox-next {
  right: 10px;
}

.lightbox-counter {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  color: rgba(255, 255, 255, 0.7);
  font-family: var(--font-heading);
  font-size: 0.9rem;
  font-weight: 600;
  letter-spacing: 0.04em;
}

@media (max-width: 700px) {
  .lightbox {
    padding: 20px;
  }

  .lightbox-prev,
  .lightbox-next {
    font-size: 2.2rem;
    padding: 8px 12px;
  }

  .lightbox-close {
    top: 14px;
    right: 18px;
    font-size: 2rem;
  }
}
""")
print("Lightbox CSS added successfully")