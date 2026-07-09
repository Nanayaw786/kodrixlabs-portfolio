with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   6. NAVBAR
=================================== */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid transparent;
  transition: var(--transition-fast);
}

.navbar.scrolled {
  border-bottom: 1px solid var(--color-border);
  box-shadow: var(--shadow-sm);
}

.navbar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 78px;
}

.logo {
  font-family: var(--font-heading);
  font-size: 1.3rem;
  font-weight: 800;
}

.logo span {
  color: var(--color-primary);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 36px;
}

.nav-links a {
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--color-text-muted);
  transition: var(--transition-fast);
  position: relative;
}

.nav-links a:hover {
  color: var(--color-text);
}

.nav-cta {
  background: var(--color-primary);
  color: #ffffff !important;
  padding: 10px 22px;
  border-radius: var(--radius-sm);
  font-weight: 600 !important;
}

.nav-cta:hover {
  background: var(--color-primary-dark);
}

.nav-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  width: 28px;
}

.nav-toggle span {
  display: block;
  height: 2px;
  width: 100%;
  background: var(--color-text);
  transition: var(--transition-fast);
}

/* ===================================
   7. HERO SECTION
=================================== */
.hero {
  position: relative;
  padding-top: 200px;
  padding-bottom: 100px;
  background: radial-gradient(circle at 20% 20%, rgba(47, 91, 255, 0.06), transparent 45%),
              radial-gradient(circle at 80% 10%, rgba(16, 185, 129, 0.06), transparent 40%),
              var(--color-bg);
  overflow: hidden;
}

.hero-inner {
  max-width: 880px;
  text-align: center;
  margin: 0 auto;
}

.eyebrow {
  display: inline-block;
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--color-primary);
  margin-bottom: 22px;
  opacity: 0;
  animation: fadeUp 0.8s ease forwards;
}

.hero h1 {
  margin-bottom: 24px;
  opacity: 0;
  animation: fadeUp 0.8s ease 0.15s forwards;
}

.hero h1 .highlight {
  color: var(--color-primary);
  position: relative;
}

.hero-subtext {
  font-size: 1.15rem;
  max-width: 620px;
  margin: 0 auto 40px;
  opacity: 0;
  animation: fadeUp 0.8s ease 0.3s forwards;
}

.hero-cta {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-bottom: 80px;
  opacity: 0;
  animation: fadeUp 0.8s ease 0.45s forwards;
}

.hero-stats {
  display: flex;
  justify-content: center;
  gap: 60px;
  padding-top: 50px;
  border-top: 1px solid var(--color-border);
  opacity: 0;
  animation: fadeUp 0.8s ease 0.6s forwards;
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-number {
  font-family: var(--font-heading);
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--color-text);
  margin-bottom: 6px;
}

.stat-label {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  font-weight: 500;
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(24px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* ===================================
   8. MOBILE NAV (base rules, refined later)
=================================== */
@media (max-width: 860px) {
  .nav-links {
    position: fixed;
    top: 78px;
    left: 0;
    width: 100%;
    background: var(--color-bg);
    flex-direction: column;
    align-items: flex-start;
    gap: 0;
    padding: 10px 24px 30px;
    border-bottom: 1px solid var(--color-border);
    transform: translateY(-150%);
    transition: var(--transition-medium);
  }

  .nav-links.open {
    transform: translateY(0);
  }

  .nav-links a {
    width: 100%;
    padding: 14px 0;
    border-bottom: 1px solid var(--color-border);
  }

  .nav-cta {
    margin-top: 10px;
    text-align: center;
  }

  .nav-toggle {
    display: flex;
  }

  .hero {
    padding-top: 150px;
  }

  .hero-stats {
    flex-wrap: wrap;
    gap: 32px;
  }
}
""")
print("Hero and navbar styles added successfully")