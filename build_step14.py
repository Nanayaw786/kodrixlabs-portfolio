navbar = """<header class="navbar" id="navbar">
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

footer = """<footer class="footer">
  <div class="container footer-inner">
    <p>&copy; 2026 Samuel Annane Mensah. All rights reserved.</p>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
"""

head_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>

"""

# ===================================
# PORTFOLIO.HTML
# ===================================
portfolio_body = """<section class="portfolio" id="portfolio" style="padding-top: 160px;">
  <div class="container">
    <div class="section-tag">Portfolio</div>
    <h2>A look at my work</h2>

    <div class="portfolio-filters" id="portfolioFilters">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="graphics">Graphics</button>
      <button class="filter-btn" data-filter="reels">Reels</button>
      <button class="filter-btn" data-filter="carousels">Carousels</button>
      <button class="filter-btn" data-filter="flyers">Flyers</button>
      <button class="filter-btn" data-filter="campaigns">Campaigns</button>
      <button class="filter-btn" data-filter="websites">Websites</button>
    </div>

    <div class="portfolio-grid" id="portfolioGrid">
      <div class="portfolio-item" data-category="graphics"><div class="portfolio-placeholder">Graphic Design</div></div>
      <div class="portfolio-item" data-category="reels"><div class="portfolio-placeholder">Reel</div></div>
      <div class="portfolio-item" data-category="carousels"><div class="portfolio-placeholder">Carousel</div></div>
      <div class="portfolio-item" data-category="flyers"><div class="portfolio-placeholder">Flyer</div></div>
      <div class="portfolio-item" data-category="campaigns"><div class="portfolio-placeholder">Campaign</div></div>
      <div class="portfolio-item" data-category="websites"><div class="portfolio-placeholder">Website</div></div>
    </div>
  </div>
</section>

"""

with open("portfolio.html", "w") as file:
    file.write(
        head_template.format(
            title="Portfolio | Samuel Annane Mensah",
            description="A visual portfolio of social media graphics, reels, carousels, flyers, campaigns, and websites by Samuel Annane Mensah."
        )
        + navbar
        + portfolio_body
        + footer
    )
print("portfolio.html created successfully")

# ===================================
# CONTACT.HTML
# ===================================
contact_body = """<section class="contact" id="contact" style="padding-top: 160px;">
  <div class="container contact-inner">
    <div class="section-tag">Contact</div>
    <h2>Let's grow your brand together</h2>
    <p class="section-subtext">
      Available for remote roles and freelance projects with international companies and agencies.
    </p>
    <div class="contact-cta">
      <a href="mailto:youremail@example.com" class="btn btn-primary">Email Me</a>
      <a href="#" class="btn btn-secondary" target="_blank">LinkedIn</a>
    </div>
    <div class="contact-details">
      <p>Email: youremail@example.com</p>
      <p>Location: Accra, Ghana (Remote Worldwide)</p>
    </div>
  </div>
</section>

"""

with open("contact.html", "w") as file:
    file.write(
        head_template.format(
            title="Contact | Samuel Annane Mensah",
            description="Get in touch with Samuel Annane Mensah for remote social media management and digital marketing work."
        )
        + navbar
        + contact_body
        + footer
    )
print("contact.html created successfully")