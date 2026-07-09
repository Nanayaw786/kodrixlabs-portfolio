with open("index.html", "r") as file:
    content = file.read()

anchor = '<link rel="icon" type="image/png" href="assets/images/favicon.png">'
verification_tag = '<meta name="google-site-verification" content="eNhVv3JbihUcripAtbOvXrdK-5PTSFQPK-7ehspj4ao" />'

if verification_tag in content:
    print("Verification tag already present in index.html (skipped)")
elif anchor in content:
    new_content = content.replace(anchor, anchor + "\n" + verification_tag, 1)
    with open("index.html", "w") as file:
        file.write(new_content)
    print("Google verification tag added to index.html successfully")
else:
    print("WARNING: anchor not found in index.html — no changes made")
