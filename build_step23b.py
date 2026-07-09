with open("css/style.css", "r") as file:
    content = file.read()

old_css = """.hero h1.eyebrow {
  font-family: var(--font-heading);
  font-size: clamp(1rem, 2vw, 1.3rem);
  font-weight: 900;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--color-primary);
  margin-bottom: 22px;
}

.hero h3.hero-headline {
  font-family: var(--font-heading);
  font-size: clamp(3rem, 6vw, 5rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.1;
  color: var(--color-text);
  margin-bottom: 24px;
}

.hero h3.hero-headline .highlight {
  color: var(--color-primary);
}

.hero h4.hero-subtext {
  font-family: var(--font-body);
  font-size: 1.35rem;
  font-weight: 500;
  color: var(--color-text);
  max-width: 700px;
  line-height: 1.55;
  margin: 0 auto 40px;
}

@media (max-width: 768px) {
  .hero h3.hero-headline {
    font-size: 2.4rem;
  }

  .hero h4.hero-subtext {
    font-size: 1.1rem;
  }

  .hero h1.eyebrow {
    font-size: 0.95rem;
  }
}"""

new_css = """.hero p.eyebrow {
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

if old_css in content:
    content = content.replace(old_css, new_css)
    with open("css/style.css", "w") as file:
        file.write(content)
    print("css/style.css heading selectors corrected successfully")
else:
    print("WARNING: CSS pattern not found in style.css — no changes made")