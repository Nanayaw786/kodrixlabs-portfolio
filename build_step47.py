import re

# Page-specific title/description pairs already used in each file
pages_meta = {
    "index.html": {
        "title": "Samuel Annane Mensah | Kodrixlabs - Software Developer & Digital Growth Specialist",
        "description": "Kodrixlabs helps brands build websites, mobile apps, and grow their social media presence. Software development and digital marketing under one roof."
    },
    "about.html": {
        "title": "About | Kodrixlabs",
        "description": "Learn more about Samuel Annane Mensah, a Ghana-based Software Developer and Digital Growth Specialist."
    },
    "services.html": {
        "title": "Services | Kodrixlabs",
        "description": "Software development, mobile apps, websites, digital marketing, and social media management services by Kodrixlabs."
    },
    "skills.html": {
        "title": "Skills & Tools | Kodrixlabs",
        "description": "Core skills and tools used by Samuel Annane Mensah for software development and digital marketing."
    },
    "case-studies.html": {
        "title": "Case Studies | Kodrixlabs",
        "description": "Real social media growth case studies and results by Samuel Annane Mensah of Kodrixlabs."
    },
    "portfolio.html": {
        "title": "Portfolio | Kodrixlabs",
        "description": "A visual portfolio of websites, graphic design, and social media campaigns by Kodrixlabs."
    },
    "contact.html": {
        "title": "Contact | Kodrixlabs",
        "description": "Get in touch with Kodrixlabs for remote software development and digital marketing work."
    },
}

site_url_base = "https://kodrixlabs-portfolio.vercel.app"
og_image_path = "assets/images/og-image.png"

for page, meta in pages_meta.items():
    with open(page, "r") as file:
        content = file.read()

    # Find the existing description meta tag line to insert new tags after it
    description_pattern = '<meta name="description" content="' + re.escape(meta["description"]) + '">'

    if description_pattern in content:
        page_url = site_url_base + "/" + page
        new_tags = description_pattern + """
<link rel="icon" type="image/png" href="assets/images/favicon.png">
<meta property="og:type" content="website">
<meta property="og:title" content=\"""" + meta["title"] + """\">
<meta property="og:description" content=\"""" + meta["description"] + """\">
<meta property="og:image" content=\"""" + site_url_base + "/" + og_image_path + """\">
<meta property="og:url" content=\"""" + page_url + """\">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content=\"""" + meta["title"] + """\">
<meta name="twitter:description" content=\"""" + meta["description"] + """\">
<meta name="twitter:image" content=\"""" + site_url_base + "/" + og_image_path + """\">"""

        content = content.replace(description_pattern, new_tags)
        with open(page, "w") as file:
            file.write(content)
        print(page + ": meta tags added successfully")
    else:
        print("WARNING: description pattern not found in " + page + " (skipped) - description may not match exactly")
