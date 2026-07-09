with open("portfolio.html", "r") as file:
    content = file.read()

old_filters = """    <div class="portfolio-filters" id="portfolioFilters">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="graphics">Graphics</button>
      <button class="filter-btn" data-filter="reels">Reels</button>
      <button class="filter-btn" data-filter="carousels">Carousels</button>
      <button class="filter-btn" data-filter="flyers">Flyers</button>
      <button class="filter-btn" data-filter="campaigns">Campaigns</button>
      <button class="filter-btn" data-filter="websites">Websites</button>
    </div>"""

new_filters = """    <div class="portfolio-filters" id="portfolioFilters">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="graphics">Graphics</button>
      <button class="filter-btn" data-filter="campaigns">Campaigns</button>
      <button class="filter-btn" data-filter="websites">Websites</button>
    </div>"""

if old_filters in content:
    content = content.replace(old_filters, new_filters)
    print("Filter buttons updated in portfolio.html")
else:
    print("WARNING: filter buttons pattern not found — no changes made")

old_placeholder_reel = """      <div class="portfolio-item" data-category="reels"><div class="portfolio-placeholder">Reel</div></div>
"""
old_placeholder_carousel = """      <div class="portfolio-item" data-category="carousels"><div class="portfolio-placeholder">Carousel</div></div>
"""
old_placeholder_flyer = """      <div class="portfolio-item" data-category="flyers"><div class="portfolio-placeholder">Flyer</div></div>
"""

for placeholder, label in [
    (old_placeholder_reel, "Reel"),
    (old_placeholder_carousel, "Carousel"),
    (old_placeholder_flyer, "Flyer"),
]:
    if placeholder in content:
        content = content.replace(placeholder, "")
        print(label + " placeholder item removed from portfolio.html")
    else:
        print("WARNING: " + label + " placeholder not found — no changes made")

with open("portfolio.html", "w") as file:
    file.write(content)

print("portfolio.html saved successfully")