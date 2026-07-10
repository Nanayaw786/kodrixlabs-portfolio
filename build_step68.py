pages = [
    "index.html",
    "about.html",
    "services.html",
    "skills.html",
    "case-studies.html",
    "portfolio.html",
    "contact.html",
]

old_tag = '<script src="js/main.js"></script>'
new_tag = '<script src="js/main.js" defer></script>'

for page in pages:
    with open(page, "r") as file:
        content = file.read()

    if new_tag in content:
        print(page + ": already has defer (skipped)")
        continue

    if old_tag in content:
        content = content.replace(old_tag, new_tag)
        with open(page, "w") as file:
            file.write(content)
        print(page + ": defer added successfully")
    else:
        print("WARNING: script tag pattern not found in " + page)
