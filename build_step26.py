with open("css/style.css", "r") as file:
    content = file.read()

old_css = """.hero p.eyebrow {
  font-family: var(--font-heading);
  font-size: clamp(2.2rem, 4.5vw, 3.4rem);
  font-weight: 900;
  letter-spacing: 0.01em;
  text-transform: uppercase;
  color: var(--color-primary);
  line-height: 1.15;
  margin-bottom: 22px;
}"""

new_css = """.hero p.eyebrow {
  font-family: var(--font-heading);
  font-size: clamp(1.8rem, 4.2vw, 3.2rem);
  font-weight: 900;
  letter-spacing: 0.01em;
  text-transform: uppercase;
  color: var(--color-primary);
  line-height: 1.15;
  margin-bottom: 22px;
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  padding: 0 24px;
  text-align: center;
  white-space: nowrap;
}

@media (max-width: 900px) {
  .hero p.eyebrow {
    white-space: normal;
  }
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open("css/style.css", "w") as file:
        file.write(content)
    print("css/style.css eyebrow full-width updated successfully")
else:
    print("WARNING: CSS pattern not found in style.css — no changes made")