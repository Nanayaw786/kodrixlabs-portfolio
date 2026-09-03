pages = [
    "index.html",
    "about.html",
    "services.html",
    "skills.html",
    "case-studies.html",
    "portfolio.html",
    "contact.html",
]

old_nav = """      <a href="services.html">Services</a>
      <a href="skills.html">Skills</a>"""

new_nav = """      <a href="services.html">Services</a>
      <a href="pricing.html">Pricing</a>
      <a href="skills.html">Skills</a>"""

for page in pages:
    with open(page, "r", encoding="utf-8") as file:
        content = file.read()

    if "pricing.html" in content:
        print(page + ": pricing link already present (skipped)")
        continue

    if old_nav in content:
        content = content.replace(old_nav, new_nav)
        with open(page, "w", encoding="utf-8") as file:
            file.write(content)
        print(page + ": pricing nav link added successfully")
    else:
        print("WARNING: nav pattern not found in " + page)
