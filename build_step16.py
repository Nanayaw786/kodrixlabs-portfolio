old_navbar = """<header class="navbar" id="navbar">
  <div class="container navbar-inner">
    <a href="index.html" class="logo">Samuel<span>.</span></a>
    <nav class="nav-links" id="navLinks">
      <a href="about.html">About</a>
      <a href="services.html">Services</a>
      <a href="skills.html">Skills</a>
      <a href="case-studies.html">Case Studies</a>
      <a href="portfolio.html">Portfolio</a>
      <a href="contact.html" class="nav-cta">Contact</a>
    </nav>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
"""

new_navbar = """<header class="navbar" id="navbar">
  <div class="container navbar-inner">
    <a href="index.html" class="logo">Kodrixlabs<span>.</span></a>
    <nav class="nav-links" id="navLinks">
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="services.html">Services</a>
      <a href="skills.html">Skills</a>
      <a href="case-studies.html">Case Studies</a>
      <a href="portfolio.html">Portfolio</a>
      <a href="contact.html" class="nav-cta">Contact</a>
    </nav>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
"""

pages = [
    "index.html",
    "about.html",
    "services.html",
    "skills.html",
    "case-studies.html",
    "portfolio.html",
    "contact.html",
]

for page in pages:
    with open(page, "r") as file:
        content = file.read()

    if old_navbar in content:
        content = content.replace(old_navbar, new_navbar)
        with open(page, "w") as file:
            file.write(content)
        print(page + " updated successfully")
    else:
        print("WARNING: navbar pattern not found in " + page + " (skipped)")