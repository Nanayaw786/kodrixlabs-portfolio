with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   12. SKILLS SECTION
=================================== */
.skills {
  background: var(--color-bg);
  text-align: center;
}

.skills h2 {
  text-align: center;
}

.skills-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 14px;
  margin-top: 40px;
}

.skill-pill {
  display: inline-flex;
  align-items: center;
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--color-text);
  background: var(--color-bg-alt);
  border: 1px solid var(--color-border);
  padding: 12px 24px;
  border-radius: 100px;
  transition: var(--transition-fast);
}

.skill-pill:hover {
  background: var(--color-primary-light);
  border-color: var(--color-primary);
  color: var(--color-primary-dark);
  transform: translateY(-3px);
}

/* ===================================
   13. TOOLS SECTION
=================================== */
.tools {
  background: var(--color-bg-alt);
  text-align: center;
}

.tools h2 {
  text-align: center;
}

.tools-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-top: 45px;
}

.tool-item {
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 26px 16px;
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.98rem;
  transition: var(--transition-fast);
}

.tool-item:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  color: var(--color-primary);
  border-color: var(--color-primary-light);
}

/* ===================================
   14. RESPONSIVE: SKILLS / TOOLS
=================================== */
@media (max-width: 700px) {
  .tools-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .skill-pill {
    font-size: 0.88rem;
    padding: 10px 18px;
  }
}
""")
print("Skills and Tools styles added successfully")