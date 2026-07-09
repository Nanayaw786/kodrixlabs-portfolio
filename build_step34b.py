with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   26. PORTFOLIO REAL IMAGES
=================================== */
.portfolio-image {
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: var(--color-bg-alt);
}

.portfolio-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top;
  display: block;
  transition: transform 0.5s ease;
}

.portfolio-item:hover .portfolio-image img {
  transform: scale(1.05);
}
""")
print("Portfolio image styling added successfully")