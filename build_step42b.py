with open("css/style.css", "r") as file:
    content = file.read()

old_css = """.contact-form {
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
}"""

new_css = """.contact-form-card {
  max-width: 560px;
  margin: 0 auto 30px;
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 44px 40px;
  box-shadow: var(--shadow-lg);
  position: relative;
  overflow: hidden;
}

.contact-form-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, var(--color-primary), var(--color-accent));
}

.contact-form {
  text-align: left;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-family: var(--font-heading);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  color: var(--color-text-muted);
}

.form-group input,
.form-group textarea {
  font-family: var(--font-body);
  font-size: 1rem;
  color: var(--color-text);
  background: var(--color-bg-alt);
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 15px 18px;
  transition: var(--transition-fast);
  resize: vertical;
}

.form-group input::placeholder,
.form-group textarea::placeholder {
  color: #a4a9b3;
}

.form-group input:hover,
.form-group textarea:hover {
  border-color: #c9cdd6;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  background: var(--color-bg);
  border-color: var(--color-primary);
  box-shadow: 0 0 0 4px var(--color-primary-light);
}

.form-submit {
  width: 100%;
  margin-top: 6px;
  padding: 17px 30px;
  font-size: 1rem;
  letter-spacing: 0.02em;
  position: relative;
}

.form-submit:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.form-submit:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.form-status {
  text-align: center;
  font-size: 0.92rem;
  font-weight: 600;
  min-height: 22px;
  margin: 0;
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

@media (max-width: 600px) {
  .contact-form-card {
    padding: 30px 22px;
  }

  .form-row {
    grid-template-columns: 1fr;
  }
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open("css/style.css", "w") as file:
        file.write(content)
    print("css/style.css contact form redesign added successfully")
else:
    print("WARNING: CSS pattern not found in style.css — no changes made")