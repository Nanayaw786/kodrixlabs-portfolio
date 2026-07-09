with open("about.html", "r") as file:
    content = file.read()

old_about = """    <div class="section-tag">About Me</div>
    <h2>Strategy-first social media management, built on real results.</h2>
    <p>
      I'm a Ghana-based Social Media Manager and Digital Marketer working with clients remotely across the globe.
      My background spans content strategy, short-form video, graphic design, and analytics — which means I don't just
      post content, I build systems that grow audiences and convert them into engaged communities.
    </p>
    <p>
      I've grown accounts from zero to tens of thousands of views using hook-driven content, audience research,
      and consistent optimization based on performance data. I also manage WordPress websites, meaning I can support
      brands across both their social presence and their web presence.
    </p>
    <div class="about-highlights">
      <div class="highlight-card">
        <h3>Data-Driven</h3>
        <p>Every content decision is backed by analytics, not guesswork.</p>
      </div>
      <div class="highlight-card">
        <h3>Full-Stack Marketer</h3>
        <p>Content, design, strategy, and website management — one person, full coverage.</p>
      </div>
      <div class="highlight-card">
        <h3>Remote-Ready</h3>
        <p>Experienced working independently with international clients and teams.</p>
      </div>
    </div>"""

new_about = """    <div class="section-tag">About Me</div>
    <h2>I build the product. Then I build the audience for it.</h2>
    <p>
      I'm Samuel Annane Mensah, a Ghana-based Software Developer and Digital Growth Specialist working remotely
      with clients across the globe. I design and build websites and mobile apps from the ground up, then apply
      social media strategy, content creation, and digital marketing to get real people using them. Most freelancers
      hand you off between a developer and a marketer — I remove that handoff entirely.
    </p>
    <p>
      On the technical side, I build web platforms, mobile apps, and WordPress sites. On the growth side, I've taken
      accounts from zero to tens of thousands of views using hook-driven content, audience research, and consistent
      optimization based on real analytics. I also bring graphic design into everything I make, so the end product
      looks as sharp as it performs.
    </p>
    <div class="about-highlights">
      <div class="highlight-card">
        <h3>Builder & Marketer</h3>
        <p>I develop the product and grow its audience — one person, full ownership, no gaps in translation.</p>
      </div>
      <div class="highlight-card">
        <h3>Data-Driven</h3>
        <p>Every design, content, and growth decision is backed by analytics, not guesswork.</p>
      </div>
      <div class="highlight-card">
        <h3>Remote-Ready</h3>
        <p>Experienced working independently with international clients, agencies, and cross-timezone teams.</p>
      </div>
    </div>"""

if old_about in content:
    content = content.replace(old_about, new_about)
    with open("about.html", "w") as file:
        file.write(content)
    print("about.html updated successfully")
else:
    print("WARNING: about pattern not found in about.html — no changes made")