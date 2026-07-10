with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   29. COMBINED CONTACT FAB (AI + WHATSAPP)
=================================== */

/* Hide ElevenLabs widget's default bubble until user opts in via our menu */
elevenlabs-convai {
  display: none;
}

elevenlabs-convai.visible {
  display: block;
}

.contact-fab-wrapper {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 1600;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 14px;
}

.contact-fab-main {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-lg);
  transition: var(--transition-fast);
}

.contact-fab-main:hover {
  transform: scale(1.06);
  background: var(--color-primary-dark);
}

.contact-fab-menu {
  display: flex;
  flex-direction: column;
  gap: 10px;
  opacity: 0;
  transform: translateY(10px);
  pointer-events: none;
  transition: var(--transition-fast);
}

.contact-fab-menu.open {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.contact-fab-option {
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: 100px;
  padding: 12px 20px 12px 16px;
  box-shadow: var(--shadow-md);
  font-family: var(--font-heading);
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--color-text);
  transition: var(--transition-fast);
  white-space: nowrap;
}

.contact-fab-option:hover {
  transform: translateX(-4px);
  box-shadow: var(--shadow-lg);
}

@media (max-width: 700px) {
  .contact-fab-wrapper {
    bottom: 18px;
    right: 18px;
  }

  .contact-fab-main {
    width: 54px;
    height: 54px;
  }
}
""")
print("Combined contact FAB CSS added successfully")
