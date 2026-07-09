with open("index.html", "r") as file:
    content = file.read()

old_title_tag = "<title>Samuel Annane Mensah | Remote Social Media Manager & Digital Marketer</title>"
new_title_tag = "<title>Kodrixlabs | Dev & Digital Growth Specialist</title>"

if old_title_tag in content:
    content = content.replace(old_title_tag, new_title_tag)
    with open("index.html", "w") as file:
        file.write(content)
    print("index.html title updated successfully")
else:
    print("WARNING: old title tag not found in index.html — no changes made")
