site_url = "https://kodrixlabs-portfolio.vercel.app"

pages = [
    "",
    "about.html",
    "services.html",
    "skills.html",
    "case-studies.html",
    "portfolio.html",
    "contact.html",
]

url_entries = ""
for page in pages:
    loc = site_url + "/" + page if page else site_url + "/"
    url_entries += "  <url>\n    <loc>" + loc + "</loc>\n  </url>\n"

sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + url_entries + """</urlset>
"""

with open("sitemap.xml", "w") as file:
    file.write(sitemap_content)
print("sitemap.xml created successfully")

robots_content = """User-agent: *
Allow: /

Sitemap: """ + site_url + """/sitemap.xml
"""

with open("robots.txt", "w") as file:
    file.write(robots_content)
print("robots.txt created successfully")
