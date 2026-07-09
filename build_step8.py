with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   17. PORTFOLIO SECTION
=================================== */
.portfolio {
  background: var(--color-bg-alt);
}

.portfolio-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 40px;
}

.filter-btn {
  font-family: var(--font-heading);
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--color-text-muted);
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  padding: 10px 20px;
  border-radius: 100px;
  transition: var(--transition-fast);
}

.filter-btn:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
}

.filter-btn.active {
  background: var(--color-primary);
  border-color: var(--color-primary);
  color: #ffffff;
}

.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 22px;
}

.portfolio-item {
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid var(--color-border);
  transition: var(--transition-medium);
  opacity: 1;
  transform: scale(1);
}

.portfolio-item.hidden {
  display: none;
}

.portfolio-item:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
}

.portfolio-placeholder {
  aspect-ratio: 4 / 5;
  background: linear-gradient(135deg, #eef0f4, var(--color-bg-alt));
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-muted);
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 1rem;
  position: relative;
}

.portfolio-placeholder::after {
  content: '';
  position: absolute;
  inset: 0;
  border: 1.5px dashed var(--color-border);
  border-radius: var(--radius-md);
  margin: 10px;
  pointer-events: none;
}

/* ===================================
   18. RESPONSIVE: PORTFOLIO
=================================== */
@media (max-width: 900px) {
  .portfolio-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 560px) {
  .portfolio-grid {
    grid-template-columns: 1fr;
  }

  .portfolio-filters {
    gap: 8px;
  }

  .filter-btn {
    font-size: 0.82rem;
    padding: 8px 16px;
  }
}
""")
print("Portfolio styles added successfully")