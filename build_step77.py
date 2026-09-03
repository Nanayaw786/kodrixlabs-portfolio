with open("css/style.css", "a", encoding="utf-8") as file:
    file.write("""

/* ===================================
   31. PRICING QUOTE MODAL
=================================== */
.price-card[data-plan] {
  cursor: pointer;
}

.quote-modal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(10, 11, 14, 0.6);
  z-index: 2100;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.quote-modal.active {
  display: flex;
}

.quote-modal-inner {
  background: var(--color-bg);
  border-radius: var(--radius-lg);
  padding: 36px 32px;
  max-width: 460px;
  width: 100%;
  max-height: 88vh;
  overflow-y: auto;
  position: relative;
  box-shadow: var(--shadow-lg);
}

.quote-modal-close {
  position: absolute;
  top: 18px;
  right: 20px;
  font-size: 1.8rem;
  color: var(--color-text-muted);
  line-height: 1;
}

.quote-modal-close:hover {
  color: var(--color-text);
}

.quote-modal-plan {
  color: var(--color-primary);
  font-weight: 600;
  margin-bottom: 24px;
}

.quote-modal-options {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.quote-or {
  text-align: center;
  font-size: 0.85rem;
  color: var(--color-text-muted);
  margin: 0;
}

.quote-form {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.quote-form .form-group input {
  padding: 12px 14px;
}
""")
print("Quote modal CSS added successfully")
