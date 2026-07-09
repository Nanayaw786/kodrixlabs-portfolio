with open("css/style.css", "r") as file:
    content = file.read()

old_css = """.hero p.eyebrow {
  font-family: var(--font-heading);
  font-size: clamp(1rem, 2vw, 1.3rem);
  font-weight: 900;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--color-primary);
  margin-bottom: 22px;
}

.hero h1.hero-headline {
  font-family: var(--font-heading);
  font-size: clamp(3rem, 6vw, 5rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.1;
  color: var(--color-text);
  margin-bottom: 24px;
}

.hero h1.hero-headline .highlight {
  color: var(--color-primary);
}

.hero p.hero-subtext {
  font-family: var(--font-body);
  font-size: 1.35rem;
  font-weight: 500;
  color: var(--color-text);
  max-width: 700px;
  line-height: 1.55;
  margin: 0 auto 40px;
}

@media (max-width: 768px) {
  .hero h1.hero-headline {
    font-size: 2.4rem;
  }

  .hero p.hero-subtext {
    font-size: 1.1rem;
  }

  .hero p.eyebrow {
    font-size: 0.95rem;
  }
}"""

new_css = """.hero p.eyebrow {
  font-family: var(--font-heading);
  font-size: clamp(2.2rem, 4.5vw, 3.4rem);
  font-weight: 900;
  letter-spacing: 0.01em;
  text-transform: uppercase;
  color: var(--color-primary);
  line-height: 1.15;
  margin-bottom: 22px;
}

.hero h1.hero-headline {
  font-family: var(--font-heading);
  font-size: clamp(1.8rem, 3.2vw, 2.6rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.25;
  color: var(--color-text);
  margin-bottom: 24px;
}

.hero h1.hero-headline .highlight {
  color: var(--color-primary);
}

.hero p.hero-subtext {
  font-family: var(--font-body);
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--color-text);
  max-width: 700px;
  line-height: 1.55;
  margin: 0 auto 40px;
}

@media (max-width: 768px) {
  .hero p.eyebrow {
    font-size: 1.8rem;
  }

  .hero h1.hero-headline {
    font-size: 1.5rem;
  }

  .hero p.hero-subtext {
    font-size: 1.05rem;
  }
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open("css/style.css", "w") as file:
        file.write(content)
    print("css/style.css hero sizing updated successfully")
else:
    print("WARNING: CSS pattern not found in style.css — no changes made")