with open("services.html", "r") as file:
    content = file.read()

old_services = """    <div class="section-tag">Services</div>
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
    </div>"""

new_services = """    <div class="section-tag">Services</div>
    <h2>Build your product. Grow your audience. One partner for both.</h2>
    <div class="services-grid" id="servicesGrid">
      <div class="service-card">
        <h3>Software Development</h3>
        <p>Custom software and web applications built from the ground up to solve real business problems.</p>
      </div>
      <div class="service-card">
        <h3>Mobile App Development</h3>
        <p>iOS and cross-platform mobile apps designed for real users, from concept through to launch.</p>
      </div>
      <div class="service-card">
        <h3>Website Development</h3>
        <p>Fast, modern, responsive websites and WordPress builds that convert visitors into customers.</p>
      </div>
      <div class="service-card">
        <h3>Digital Marketing</h3>
        <p>Cross-platform marketing strategy to grow your brand's overall online presence and reach.</p>
      </div>
      <div class="service-card">
        <h3>Social Media Management</h3>
        <p>Full account management — content calendars, posting, community engagement, and growth strategy.</p>
      </div>
      <div class="service-card">
        <h3>Content Strategy & Short-Form Video</h3>
        <p>Audience-focused content pillars and scroll-stopping Reels/TikToks built around strong hooks.</p>
      </div>
      <div class="service-card">
        <h3>Graphic Design</h3>
        <p>On-brand graphics, carousels, and flyers that make your product and your feed look professional.</p>
      </div>
      <div class="service-card">
        <h3>Analytics & Reporting</h3>
        <p>Clear, actionable performance reports so you always know what's working and why — on web and social.</p>
      </div>
    </div>"""

if old_services in content:
    content = content.replace(old_services, new_services)
    with open("services.html", "w") as file:
        file.write(content)
    print("services.html updated successfully")
else:
    print("WARNING: services pattern not found in services.html — no changes made")