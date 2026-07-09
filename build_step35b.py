with open("css/style.css", "r") as file:
    content = file.read()

old_css = """.portfolio-image {
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: var(--color-bg-alt);
}"""

new_css = """.portfolio-image {
  aspect-ratio: 4 / 5;
  overflow: hidden;
  background: var(--color-bg-alt);
}

.portfolio-item[data-category="websites"] .portfolio-image {
  aspect-ratio: 16 / 10;
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open("css/style.css", "w") as file:
        file.write(content)
    print("css/style.css portfolio image aspect ratios updated successfully")
else:
    print("WARNING: CSS pattern not found in style.css — no changes made")