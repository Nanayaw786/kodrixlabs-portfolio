with open("index.html", "r") as file:
    content = file.read()

old_hero = """    <p class="eyebrow">Remote Social Media Manager & Digital Marketer</p>
    <h1>I help brands turn <span class="highlight">followers into customers</span> through strategic social media growth.</h1>
    <p class="hero-subtext">
      I'm Samuel Annane Mensah — a Social Media Manager and Content Strategist who builds audiences from scratch,
      grows engagement with data-driven content, and manages end-to-end digital presence for brands worldwide.
    </p>"""

new_hero = """    <p class="eyebrow">Software Developer &amp; Digital Growth Specialist</p>
    <h1>I build the <span class="highlight">products and the audience</span> that make your brand impossible to ignore.</h1>
    <p class="hero-subtext">
      I'm Samuel Annane Mensah. I design and build websites and mobile apps, then use social media strategy,
      content creation, and digital marketing to get them in front of the right people. Most people can build
      OR market — I do both, so nothing gets lost in translation between your product and your audience.
    </p>"""

if old_hero in content:
    content = content.replace(old_hero, new_hero)
    with open("index.html", "w") as file:
        file.write(content)
    print("index.html hero updated successfully")
else:
    print("WARNING: hero pattern not found in index.html — no changes made")