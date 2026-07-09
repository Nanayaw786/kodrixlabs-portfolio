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
# INDEX.HTML (HOME / HERO PAGE)
# ===================================
index_body = """<section class="hero" id="hero">
  <div class="container hero-inner">
    <p class="eyebrow">Remote Social Media Manager & Digital Marketer</p>
    <h1>I help brands turn <span class="highlight">followers into customers</span> through strategic social media growth.</h1>
    <p class="hero-subtext">
      I'm Samuel Annane Mensah — a Social Media Manager and Content Strategist who builds audiences from scratch,
      grows engagement with data-driven content, and manages end-to-end digital presence for brands worldwide.
    </p>
    <div class="hero-cta">
      <a href="case-studies.html" class="btn btn-primary">View My Results</a>
      <a href="contact.html" class="btn btn-secondary">Hire Me</a>
    </div>
    <div class="hero-stats">
      <div class="stat">
        <span class="stat-number">31.4K+</span>
        <span class="stat-label">Post Views Generated</span>
      </div>
      <div class="stat">
        <span class="stat-number">694</span>
        <span class="stat-label">Followers From Zero</span>
      </div>
      <div class="stat">
        <span class="stat-number">88.1%</span>
        <span class="stat-label">FYP Reach Rate</span>
      </div>
    </div>
  </div>
</section>

"""

with open("index.html", "w") as file:
    file.write(
        head_template.format(
            title="Samuel Annane Mensah | Remote Social Media Manager & Digital Marketer",
            description="Social Media Manager & Digital Marketer helping international brands grow through strategic content, data-driven campaigns, and community engagement."
        )
        + navbar
        + index_body
        + footer
    )
print("index.html rebuilt successfully")

# ===================================
# ABOUT.HTML
# ===================================
about_body = """<section class="about" id="about" style="padding-top: 160px;">
  <div class="container about-inner">
    <div class="section-tag">About Me</div>
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
    </div>
  </div>
</section>

"""

with open("about.html", "w") as file:
    file.write(
        head_template.format(
            title="About | Samuel Annane Mensah",
            description="Learn more about Samuel Annane Mensah, a Ghana-based Social Media Manager and Digital Marketer."
        )
        + navbar
        + about_body
        + footer
    )
print("about.html created successfully")

# ===================================
# SERVICES.HTML
# ===================================
services_body = """<section class="services" id="services" style="padding-top: 160px;">
  <div class="container">
    <div class="section-tag">Services</div>
    <h2>How I can help your brand grow</h2>
    <div class="services-grid" id="servicesGrid">
      <div class="service-card">
        <h3>Social Media Management</h3>
        <p>Full account management — content calendars, posting, community engagement, and growth strategy.</p>
      </div>
      <div class="service-card">
        <h3>Content Strategy</h3>
        <p>Audience research and content pillars designed to attract, engage, and convert your ideal customer.</p>
      </div>
      <div class="service-card">
        <h3>Short-Form Video Creation</h3>
        <p>Scroll-stopping Reels and TikToks built around strong hooks and platform-native trends.</p>
      </div>
      <div class="service-card">
        <h3>Graphic Design</h3>
        <p>On-brand graphics, carousels, and flyers that make your feed look professional and consistent.</p>
      </div>
      <div class="service-card">
        <h3>Community Management</h3>
        <p>Responding, engaging, and building real relationships with your audience — not just posting and ghosting.</p>
      </div>
      <div class="service-card">
        <h3>Analytics & Reporting</h3>
        <p>Clear, actionable performance reports so you always know what's working and why.</p>
      </div>
      <div class="service-card">
        <h3>WordPress Website Management</h3>
        <p>Updates, maintenance, and content management to keep your website running smoothly.</p>
      </div>
      <div class="service-card">
        <h3>Digital Marketing</h3>
        <p>Cross-platform marketing support to grow your brand's overall online presence.</p>
      </div>
    </div>
  </div>
</section>

"""

with open("services.html", "w") as file:
    file.write(
        head_template.format(
            title="Services | Samuel Annane Mensah",
            description="Social media management, content strategy, video creation, graphic design, and more."
        )
        + navbar
        + services_body
        + footer
    )
print("services.html created successfully")