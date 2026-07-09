pages = [
    "index.html",
    "about.html",
    "services.html",
    "skills.html",
    "case-studies.html",
    "portfolio.html",
    "contact.html",
]

old_email = "youremail@example.com"
new_email = "samuel.kodrixlabs@gmail.com"

for page in pages:
    with open(page, "r") as file:
        content = file.read()

    if old_email in content:
        count = content.count(old_email)
        content = content.replace(old_email, new_email)
        with open(page, "w") as file:
            file.write(content)
        print(page + ": replaced " + str(count) + " occurrence(s)")
    else:
        print(page + ": no occurrences found (skipped)")