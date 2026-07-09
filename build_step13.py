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
# SKILLS.HTML (Skills + Tools)
# ===================================
skills_body = """<section class="skills" id="skills" style="padding-top: 160px;">
  <div class="container">
    <div class="section-tag">Skills</div>
    <h2>What I bring to the table</h2>
    <div class="skills-list" id="skillsList">
      <span class="skill-pill">Social Media Management</span>
      <span class="skill-pill">Content Strategy</span>
      <span class="skill-pill">Short-Form Video Creation</span>
      <span class="skill-pill">Graphic Design</span>
      <span class="skill-pill">Community Management</span>
      <span class="skill-pill">Analytics & Reporting</span>
      <span class="skill-pill">WordPress Management</span>
      <span class="skill-pill">Digital Marketing</span>
    </div>
  </div>
</section>

<section class="tools" id="tools">
  <div class="container">
    <div class="section-tag">Tools I Use</div>
    <h2>My toolkit</h2>
    <div class="tools-grid" id="toolsGrid">
      <div class="tool-item">Canva</div>
      <div class="tool-item">CapCut</div>
      <div class="tool-item">Adobe Photoshop</div>
      <div class="tool-item">Meta Business Suite</div>
      <div class="tool-item">TikTok Studio</div>
      <div class="tool-item">WordPress</div>
      <div class="tool-item">Notion</div>
      <div class="tool-item">Google Analytics</div>
    </div>
  </div>
</section>

"""

with open("skills.html", "w") as file:
    file.write(
        head_template.format(
            title="Skills & Tools | Samuel Annane Mensah",
            description="Core skills and tools used by Samuel Annane Mensah for social media management and digital marketing."
        )
        + navbar
        + skills_body
        + footer
    )
print("skills.html created successfully")

# ===================================
# CASE-STUDIES.HTML
# ===================================
case_studies_body = """<section class="case-studies" id="case-studies" style="padding-top: 160px;">
  <div class="container">
    <div class="section-tag">Featured Results</div>
    <h2>Real growth. Real numbers.</h2>
    <p class="section-subtext">A look at how strategic content execution turns into measurable business results.</p>

    <div class="case-study-card">
      <div class="case-study-header">
        <h3>TikTok Account Growth: 0 to 694 Followers</h3>
        <p class="case-study-meta">Organic Growth &middot; Content Strategy &middot; Short-Form Video</p>
      </div>

      <div class="case-study-block">
        <h4>The Challenge</h4>
        <p>Starting completely from zero — no audience, no prior content, no existing brand recognition on the platform.</p>
      </div>

      <div class="case-study-block">
        <h4>The Strategy</h4>
        <ul>
          <li>Created strong, scroll-stopping hooks for every video</li>
          <li>Built audience-focused content pillars around real pain points</li>
          <li>Optimized future videos based on analytics from top performers</li>
          <li>Designed content specifically to drive comments and engagement</li>
        </ul>
      </div>

      <div class="case-study-block">
        <h4>The Results</h4>
        <div class="metrics-grid">
          <div class="metric"><span class="metric-number">31.4K</span><span class="metric-label">Total Post Views</span></div>
          <div class="metric"><span class="metric-number">25K</span><span class="metric-label">Viewers Reached</span></div>
          <div class="metric"><span class="metric-number">22K</span><span class="metric-label">Unique New Viewers</span></div>
          <div class="metric"><span class="metric-number">1.1K</span><span class="metric-label">Profile Views</span></div>
          <div class="metric"><span class="metric-number">2K</span><span class="metric-label">Likes</span></div>
          <div class="metric"><span class="metric-number">212</span><span class="metric-label">Comments</span></div>
          <div class="metric"><span class="metric-number">694</span><span class="metric-label">Followers Built</span></div>
          <div class="metric"><span class="metric-number">88.1%</span><span class="metric-label">Traffic From FYP</span></div>
        </div>
      </div>

      <div class="case-study-block">
        <h4>Top Performing Content</h4>
        <ol class="top-content-list">
          <li><span>"Tech is not for the weak..."</span><strong>11K views</strong></li>
          <li><span>Graphic Design / Photoshop Trends</span><strong>3.8K views</strong></li>
          <li><span>Graphic Design Viral Trends</span><strong>2.7K views</strong></li>
          <li><span>Local Business Strategy Video</span><strong>1.5K views</strong></li>
        </ol>
      </div>

      <div class="case-study-block">
        <h4>Screenshots</h4>
        <div class="screenshot-placeholders">
          <div class="screenshot-box">Screenshot 1</div>
          <div class="screenshot-box">Screenshot 2</div>
          <div class="screenshot-box">Screenshot 3</div>
        </div>
      </div>

      <div class="case-study-block lessons-block">
        <h4>Lessons Learned</h4>
        <p>Strong hooks and consistent analytics review were the single biggest drivers of growth — content that
        underperformed always pointed to the next optimization, and content that overperformed revealed exactly
        what the audience wanted more of.</p>
      </div>
    </div>
  </div>
</section>

"""

with open("case-studies.html", "w") as file:
    file.write(
        head_template.format(
            title="Case Studies | Samuel Annane Mensah",
            description="Real social media growth case studies and results by Samuel Annane Mensah."
        )
        + navbar
        + case_studies_body
        + footer
    )
print("case-studies.html created successfully")