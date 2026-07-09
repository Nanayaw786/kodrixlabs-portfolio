title_updates = {
    "about.html": ("<title>About | Samuel Annane Mensah</title>", "<title>About | Kodrixlabs</title>"),
    "services.html": ("<title>Services | Samuel Annane Mensah</title>", "<title>Services | Kodrixlabs</title>"),
    "skills.html": ("<title>Skills & Tools | Samuel Annane Mensah</title>", "<title>Skills & Tools | Kodrixlabs</title>"),
    "case-studies.html": ("<title>Case Studies | Samuel Annane Mensah</title>", "<title>Case Studies | Kodrixlabs</title>"),
    "portfolio.html": ("<title>Portfolio | Samuel Annane Mensah</title>", "<title>Portfolio | Kodrixlabs</title>"),
    "contact.html": ("<title>Contact | Samuel Annane Mensah</title>", "<title>Contact | Kodrixlabs</title>"),
}

for page, (old_title, new_title) in title_updates.items():
    with open(page, "r") as file:
        content = file.read()

    if old_title in content:
        content = content.replace(old_title, new_title)
        with open(page, "w") as file:
            file.write(content)
        print(page + ": title updated successfully")
    else:
        print("WARNING: old title not found in " + page)
