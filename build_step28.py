with open("css/style.css", "r") as file:
    content = file.read()

old_css = """.eyebrow {
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
}"""

new_css = """/* .eyebrow base rule removed in Step 28 - superseded by .hero p.eyebrow */
.eyebrow {
  opacity: 0;
  animation: fadeUp 0.8s ease forwards;
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open("css/style.css", "w") as file:
        file.write(content)
    print("css/style.css conflicting eyebrow rule removed successfully")
else:
    print("WARNING: CSS pattern not found in style.css — no changes made")