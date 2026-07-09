with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   19. CONTACT SECTION
=================================== */
.contact {
  background: var(--color-bg);
  position: relative;
}

.contact-inner {
  max-width: 640px;
  text-align: center;
  margin: 0 auto;
}

.contact .section-tag {
  display: inline-block;
}

.contact h2 {
  text-align: center;
}

.contact .section-subtext {
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}

.contact-cta {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin: 36px 0 44px;
}

.contact-details {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding-top: 30px;
  border-top: 1px solid var(--color-border);
}

.contact-details p {
  font-size: 0.95rem;
  color: var(--color-text-muted);
}

/* ===================================
   20. FOOTER
=================================== */
.footer {
  background: var(--color-bg-alt);
  border-top: 1px solid var(--color-border);
  padding: 30px 0;
}

.footer-inner {
  text-align: center;
}

.footer-inner p {
  font-size: 0.88rem;
  color: var(--color-text-muted);
  margin-bottom: 0;
}

/* ===================================
   21. RESPONSIVE: CONTACT
=================================== */
@media (max-width: 600px) {
  .contact-cta {
    flex-direction: column;
    align-items: center;
  }

  .contact-cta .btn {
    width: 100%;
    max-width: 280px;
  }
}
""")
print("Contact and footer styles added successfully")