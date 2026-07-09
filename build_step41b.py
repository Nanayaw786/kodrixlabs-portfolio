with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   27. CONTACT FORM
=================================== */
.contact-form {
  text-align: left;
  max-width: 480px;
  margin: 0 auto 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-family: var(--font-heading);
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--color-text);
}

.form-group input,
.form-group textarea {
  font-family: var(--font-body);
  font-size: 1rem;
  color: var(--color-text);
  background: var(--color-bg);
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 14px 16px;
  transition: var(--transition-fast);
  resize: vertical;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px var(--color-primary-light);
}

.form-submit {
  width: 100%;
  margin-top: 4px;
}

.form-submit:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.form-status {
  text-align: center;
  font-size: 0.95rem;
  font-weight: 500;
  min-height: 22px;
}

.form-status.success {
  color: var(--color-accent);
}

.form-status.error {
  color: #e0433f;
}

.contact-cta-secondary {
  margin-bottom: 30px;
}
""")
print("Contact form CSS added successfully")