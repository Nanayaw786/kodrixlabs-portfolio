with open("pricing.html", "r", encoding="utf-8") as file:
    content = file.read()

if "main.js" in content:
    print("main.js already referenced in pricing.html")
else:
    old_tag = "</body>"
    new_tag = "<script src=\"js/main.js\" defer></script>\n</body>"
    content = content.replace(old_tag, new_tag, 1)
    with open("pricing.html", "w", encoding="utf-8") as file:
        file.write(content)
    print("main.js script tag added to pricing.html successfully")
