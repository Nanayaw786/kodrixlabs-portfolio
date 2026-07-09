import os

# ===================================
# PART 1: RENAME WEBSITE SCREENSHOTS
# ===================================
folder = "assets/images/portfolio"

old_names = [
    "Screen Shot 2026-07-09 at 9.50.37 PM.png",
    "Screen Shot 2026-07-09 at 9.50.51 PM.png",
    "Screen Shot 2026-07-09 at 9.51.09 PM.png",
    "Screen Shot 2026-07-09 at 9.53.50 PM.png",
    "Screen Shot 2026-07-09 at 9.54.17 PM.png",
    "Screen Shot 2026-07-09 at 9.54.31 PM.png",
]

new_names = []
for index, old_name in enumerate(old_names, start=1):
    new_name = "website-" + str(index) + ".png"
    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print("Renamed: " + old_name + " -> " + new_name)
        new_names.append(new_name)
    else:
        print("WARNING: file not found, skipped: " + old_name)

# ===================================
# PART 2: REPLACE PORTFOLIO GRID IN portfolio.html
# ===================================
with open("portfolio.html", "r") as file:
    content = file.read()

old_grid = """    <div class="portfolio-grid" id="portfolioGrid">
      <div class="portfolio-item" data-category="graphics"><div class="portfolio-placeholder">Graphic Design</div></div>
      <div class="portfolio-item" data-category="reels"><div class="portfolio-placeholder">Reel</div></div>
      <div class="portfolio-item" data-category="carousels"><div class="portfolio-placeholder">Carousel</div></div>
      <div class="portfolio-item" data-category="flyers"><div class="portfolio-placeholder">Flyer</div></div>
      <div class="portfolio-item" data-category="campaigns"><div class="portfolio-placeholder">Campaign</div></div>
      <div class="portfolio-item" data-category="websites"><div class="portfolio-placeholder">Website</div></div>
    </div>"""

website_items = ""
for name in new_names:
    website_items += '      <div class="portfolio-item" data-category="websites"><div class="portfolio-image"><img src="assets/images/portfolio/' + name + '" alt="Client website homepage design" loading="lazy"></div></div>\n'

new_grid = """    <div class="portfolio-grid" id="portfolioGrid">
      <div class="portfolio-item" data-category="graphics"><div class="portfolio-placeholder">Graphic Design</div></div>
      <div class="portfolio-item" data-category="reels"><div class="portfolio-placeholder">Reel</div></div>
      <div class="portfolio-item" data-category="carousels"><div class="portfolio-placeholder">Carousel</div></div>
      <div class="portfolio-item" data-category="flyers"><div class="portfolio-placeholder">Flyer</div></div>
      <div class="portfolio-item" data-category="campaigns"><div class="portfolio-placeholder">Campaign</div></div>
""" + website_items + """    </div>"""

if old_grid in content:
    content = content.replace(old_grid, new_grid)
    with open("portfolio.html", "w") as file:
        file.write(content)
    print("portfolio.html updated with real website screenshots successfully")
else:
    print("WARNING: portfolio grid pattern not found in portfolio.html — no changes made")