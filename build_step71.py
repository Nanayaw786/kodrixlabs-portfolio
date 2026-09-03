with open("css/style.css", "a", encoding="utf-8") as file:
    file.write("""

/* ===================================
   30. PRICING PAGE
=================================== */
.pricing {
  background: var(--color-bg);
}

.currency-toggle-label {
  font-weight: 600;
  color: var(--color-text);
  margin-left: 8px;
}

.currency-select {
  font-family: var(--font-heading);
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--color-primary);
  background: var(--color-primary-light);
  border: 1px solid var(--color-primary);
  border-radius: 100px;
  padding: 6px 14px;
  margin-left: 8px;
  cursor: pointer;
}

.rate-note {
  display: block;
  font-size: 0.82rem;
  color: var(--color-text-muted);
  margin-top: 8px;
}

.pricing-why {
  background: var(--color-primary-light);
  border-radius: var(--radius-md);
  padding: 28px 30px;
  margin-bottom: 60px;
  border-left: 4px solid var(--color-primary);
}

.pricing-why h3 {
  color: var(--color-primary-dark);
  font-size: 1.1rem;
}

.pricing-why p {
  color: var(--color-text);
  margin-bottom: 0;
}

.pricing-block {
  margin-bottom: 70px;
}

.pricing-block-title {
  font-size: 1.5rem;
  margin-bottom: 30px;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.save-tag {
  font-family: var(--font-heading);
  font-size: 0.75rem;
  font-weight: 700;
  background: var(--color-accent);
  color: #ffffff;
  padding: 4px 12px;
  border-radius: 100px;
  letter-spacing: 0.02em;
}

.pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.pricing-grid-4 {
  grid-template-columns: repeat(4, 1fr);
}

.price-card {
  background: var(--color-bg-alt);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 32px 26px;
  position: relative;
  transition: var(--transition-fast);
}

.price-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

.price-card.featured {
  background: var(--color-bg);
  border: 2px solid var(--color-primary);
  box-shadow: var(--shadow-lg);
}

.price-badge {
  position: absolute;
  top: -14px;
  left: 26px;
  background: var(--color-primary);
  color: #ffffff;
  font-family: var(--font-heading);
  font-size: 0.75rem;
  font-weight: 700;
  padding: 5px 14px;
  border-radius: 100px;
}

.price-card h4 {
  font-size: 1.1rem;
  margin-bottom: 12px;
}

.price-amount {
  font-family: var(--font-heading);
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--color-primary);
  margin-bottom: 18px;
}

.price-amount span {
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--color-text-muted);
}

.price-features {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.price-features li {
  position: relative;
  padding-left: 22px;
  font-size: 0.92rem;
  color: var(--color-text-muted);
}

.price-features li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 7px;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--color-accent);
}

.bundle-desc {
  font-size: 0.92rem;
  margin-bottom: 12px;
}

.bundle-for {
  font-size: 0.85rem;
  font-style: italic;
  color: var(--color-text-muted);
  margin-bottom: 0;
}

.price-note {
  font-size: 0.88rem;
  color: var(--color-text-muted);
  margin-top: 20px;
}

.easy-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.easy-list li {
  position: relative;
  padding-left: 28px;
  font-size: 1rem;
  color: var(--color-text-muted);
}

.easy-list li::before {
  content: '\\2713';
  position: absolute;
  left: 0;
  top: 0;
  color: var(--color-accent);
  font-weight: 700;
}

.price-disclaimer {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  border-top: 1px solid var(--color-border);
  padding-top: 24px;
  margin-top: 20px;
  margin-bottom: 40px;
}

@media (max-width: 1024px) {
  .pricing-grid,
  .pricing-grid-4 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 700px) {
  .pricing-grid,
  .pricing-grid-4 {
    grid-template-columns: 1fr;
  }

  .currency-select {
    display: block;
    margin: 10px 0 0;
  }
}
""")
print("Pricing page CSS added successfully")
