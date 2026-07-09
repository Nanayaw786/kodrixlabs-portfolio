with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   15. CASE STUDIES SECTION
=================================== */
.case-studies {
  background: var(--color-bg);
}

.case-study-card {
  background: var(--color-bg-alt);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 50px;
  margin-top: 20px;
}

.case-study-header {
  margin-bottom: 40px;
  padding-bottom: 30px;
  border-bottom: 1px solid var(--color-border);
}

.case-study-header h3 {
  font-size: 1.6rem;
  margin-bottom: 8px;
}

.case-study-meta {
  font-size: 0.92rem;
  color: var(--color-primary);
  font-weight: 600;
  margin-bottom: 0;
}

.case-study-block {
  margin-bottom: 40px;
}

.case-study-block:last-child {
  margin-bottom: 0;
}

.case-study-block h4 {
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--color-text-muted);
  margin-bottom: 16px;
}

.case-study-block p {
  font-size: 1rem;
}

.case-study-block ul {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.case-study-block ul li {
  position: relative;
  padding-left: 26px;
  font-size: 1rem;
  color: var(--color-text-muted);
}

.case-study-block ul li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-primary);
}

/* Metrics Grid */
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.metric {
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 22px 16px;
  text-align: center;
  transition: var(--transition-fast);
}

.metric:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
  border-color: var(--color-primary-light);
}

.metric-number {
  display: block;
  font-family: var(--font-heading);
  font-size: 1.7rem;
  font-weight: 800;
  color: var(--color-primary);
  margin-bottom: 4px;
}

.metric-label {
  font-size: 0.82rem;
  color: var(--color-text-muted);
  font-weight: 500;
}

/* Top Content List */
.top-content-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.top-content-list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 16px 20px;
  counter-increment: item;
}

.top-content-list li span {
  font-size: 0.98rem;
  font-weight: 500;
  color: var(--color-text);
}

.top-content-list li strong {
  font-family: var(--font-heading);
  color: var(--color-primary);
  font-size: 0.95rem;
  white-space: nowrap;
  margin-left: 20px;
}

/* Screenshots */
.screenshot-placeholders {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.screenshot-box {
  aspect-ratio: 9 / 16;
  background: linear-gradient(135deg, var(--color-bg-alt), #eef0f4);
  border: 1.5px dashed var(--color-border);
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-muted);
  font-size: 0.9rem;
  font-weight: 500;
}

/* Lessons Learned Callout */
.lessons-block {
  background: var(--color-primary-light);
  border-radius: var(--radius-md);
  padding: 28px 30px;
  border-left: 4px solid var(--color-primary);
}

.lessons-block h4 {
  color: var(--color-primary-dark);
}

.lessons-block p {
  color: var(--color-text);
  margin-bottom: 0;
}

/* ===================================
   16. RESPONSIVE: CASE STUDIES
=================================== */
@media (max-width: 900px) {
  .metrics-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .screenshot-placeholders {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 700px) {
  .case-study-card {
    padding: 30px 24px;
  }

  .top-content-list li {
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
  }

  .top-content-list li strong {
    margin-left: 0;
  }

  .screenshot-placeholders {
    grid-template-columns: repeat(1, 1fr);
  }
}
""")
print("Case Studies styles added successfully")