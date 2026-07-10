pages = [
    "index.html",
    "about.html",
    "services.html",
    "skills.html",
    "case-studies.html",
    "portfolio.html",
    "contact.html",
]

widget_snippet = """<elevenlabs-convai agent-id="agent_5101kx4n1q8we3jtaa46r9zz0fty"></elevenlabs-convai>
<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
"""

anchor = "</body>"

for page in pages:
    with open(page, "r") as file:
        content = file.read()

    if "elevenlabs-convai" in content:
        print(page + ": widget already present (skipped)")
        continue

    if anchor in content:
        content = content.replace(anchor, widget_snippet + anchor, 1)
        with open(page, "w") as file:
            file.write(content)
        print(page + ": AI chat widget added successfully")
    else:
        print("WARNING: closing body tag not found in " + page)
