with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   9. ABOUT SECTION
=================================== */
.about {
  background: var(--color-bg);
}

.about-inner {
  max-width: 820px;
}

.about-inner p {
  margin-bottom: 20px;
  font-size: 1.08rem;
}

.about-highlights {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 50px;
}

.highlight-card {
  padding: 28px 24px;
  background: var(--color-bg-alt);
  border-radius: var(--radius-md);
  border: 1px solid var(--color-border);
  transition: var(--transition-fast);
}

.highlight-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: transparent;
}

.highlight-card h3 {
  font-size: 1.05rem;
  color: var(--color-primary);
  margin-bottom: 8px;
}

.highlight-card p {
  font-size: 0.95rem;
  margin-bottom: 0;
}

/* ===================================
   10. SERVICES SECTION
=================================== */
.services {
  background: var(--color-bg-alt);
}

.services h2 {
  max-width: 600px;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-top: 50px;
}

.service-card {
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 30px 26px;
  transition: var(--transition-medium);
}

.service-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-primary-light);
}

.service-card h3 {
  font-size: 1.1rem;
  margin-bottom: 10px;
}

.service-card p {
  font-size: 0.95rem;
  margin-bottom: 0;
}

/* ===================================
   11. RESPONSIVE: ABOUT / SERVICES
=================================== */
@media (max-width: 1024px) {
  .services-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 700px) {
  .about-highlights {
    grid-template-columns: 1fr;
  }

  .services-grid {
    grid-template-columns: 1fr;
  }
}
""")
print("About and Services styles added successfully")