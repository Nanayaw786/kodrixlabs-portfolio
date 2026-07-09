with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   23. HERO TEXT EMPHASIS (BOLDER + LARGER)
=================================== */
.hero h1 {
  font-size: clamp(3rem, 6vw, 5rem);
  font-weight: 800;
  letter-spacing: -0.03em;
}

.hero-subtext {
  font-size: 1.35rem;
  font-weight: 500;
  color: var(--color-text);
  max-width: 700px;
  line-height: 1.55;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2.4rem;
  }

  .hero-subtext {
    font-size: 1.1rem;
  }
}
""")
print("Hero text emphasis styles added successfully")