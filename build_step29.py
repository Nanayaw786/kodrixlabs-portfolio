with open("css/style.css", "r") as file:
    content = file.read()

old_css = """.hero h1.hero-headline {
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
}"""

new_css = """.hero h1.hero-headline {
  font-family: var(--font-heading);
  font-size: clamp(1.8rem, 3.2vw, 2.6rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.25;
  color: var(--color-text);
  margin-bottom: 24px;
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  padding: 0 24px;
  text-align: center;
  max-width: none;
}

.hero h1.hero-headline .highlight {
  color: var(--color-primary);
}

.hero p.hero-subtext {
  font-family: var(--font-body);
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--color-text);
  line-height: 1.55;
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  padding: 0 24px;
  text-align: center;
  max-width: none;
  margin-bottom: 40px;
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open("css/style.css", "w") as file:
        file.write(content)
    print("css/style.css headline and subtext full-width updated successfully")
else:
    print("WARNING: CSS pattern not found in style.css — no changes made")