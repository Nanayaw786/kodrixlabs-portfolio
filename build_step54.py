# Shorter titles (under 60 chars) and descriptions (under 125 chars)
pages_meta = {
    "index.html": {
        "old_title": "Samuel Annane Mensah | Kodrixlabs - Software Developer & Digital Growth Specialist",
        "new_title": "Kodrixlabs | Dev & Digital Growth Specialist",
        "old_desc": "Kodrixlabs helps brands build websites, mobile apps, and grow their social media presence. Software development and digital marketing under one roof.",
        "new_desc": "Websites, mobile apps, and social media growth — built and marketed by one developer at Kodrixlabs."
    },
    "about.html": {
        "old_title": "About | Kodrixlabs",
        "new_title": "About | Kodrixlabs",
        "old_desc": "Learn more about Samuel Annane Mensah, a Ghana-based Software Developer and Digital Growth Specialist.",
        "new_desc": "Meet Samuel Annane Mensah, a Ghana-based developer and digital growth specialist at Kodrixlabs."
    },
    "services.html": {
        "old_title": "Services | Kodrixlabs",
        "new_title": "Services | Kodrixlabs",
        "old_desc": "Software development, mobile apps, websites, digital marketing, and social media management services by Kodrixlabs.",
        "new_desc": "Web, mobile app development, and digital marketing services by Kodrixlabs."
    },
    "skills.html": {
        "old_title": "Skills & Tools | Kodrixlabs",
        "new_title": "Skills & Tools | Kodrixlabs",
        "old_desc": "Core skills and tools used by Samuel Annane Mensah for software development and digital marketing.",
        "new_desc": "Development and digital marketing skills and tools used by Kodrixlabs."
    },
    "case-studies.html": {
        "old_title": "Case Studies | Kodrixlabs",
        "new_title": "Case Studies | Kodrixlabs",
        "old_desc": "Real social media growth case studies and results by Samuel Annane Mensah of Kodrixlabs.",
        "new_desc": "Real growth case studies and results from Kodrixlabs social media campaigns."
    },
    "portfolio.html": {
        "old_title": "Portfolio | Kodrixlabs",
        "new_title": "Portfolio | Kodrixlabs",
        "old_desc": "A visual portfolio of websites, graphic design, and social media campaigns by Kodrixlabs.",
        "new_desc": "Websites, graphic design, and campaign work from the Kodrixlabs portfolio."
    },
    "contact.html": {
        "old_title": "Contact | Kodrixlabs",
        "new_title": "Contact | Kodrixlabs",
        "old_desc": "Get in touch with Kodrixlabs for remote software development and digital marketing work.",
        "new_desc": "Get in touch with Kodrixlabs for remote development and digital marketing work."
    },
}

for page, meta in pages_meta.items():
    with open(page, "r") as file:
        content = file.read()

    changed = False

    old_title_tag = "<title>" + meta["old_title"] + "</title>"
    new_title_tag = "<title>" + meta["new_title"] + "</title>"
    if old_title_tag in content:
        content = content.replace(old_title_tag, new_title_tag)
        changed = True

    old_desc_tag = 'content="' + meta["old_desc"] + '"'
    new_desc_tag = 'content="' + meta["new_desc"] + '"'
    occurrences = content.count(old_desc_tag)
    if occurrences > 0:
        content = content.replace(old_desc_tag, new_desc_tag)
        changed = True

    if changed:
        with open(page, "w") as file:
            file.write(content)
        print(page + ": title/description shortened successfully")
    else:
        print("WARNING: no matching title/description found in " + page)
