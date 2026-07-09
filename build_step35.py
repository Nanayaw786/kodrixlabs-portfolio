import os

# ===================================
# PART 1: RENAME GRAPHIC FILES
# ===================================
folder = "assets/images/portfolio"

old_names = [
    "Graphic 1.jpg",
    "Graphic 2.jpg",
    "Graphic 3.jpg",
    "Graphic 4.jpg",
    "Graphic 5.jpg",
    "Graphic 6.jpg",
    "Graphic 7.jpg",
    "Graphic 8.jpg",
    "Graphic 9.jpg",
    "Graphic 10.jpg",
    "Graphic 11.jpg",
    "Graphic 12.jpg",
]

new_names = []
for index, old_name in enumerate(old_names, start=1):
    new_name = "graphic-" + str(index) + ".jpg"
    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print("Renamed: " + old_name + " -> " + new_name)
        new_names.append(new_name)
    else:
        print("WARNING: file not found, skipped: " + old_name)

# ===================================
# PART 2: REPLACE GRAPHICS PLACEHOLDER IN portfolio.html
# ===================================
with open("portfolio.html", "r") as file:
    content = file.read()

old_graphics_item = """      <div class="portfolio-item" data-category="graphics"><div class="portfolio-placeholder">Graphic Design</div></div>"""

graphic_items = ""
for name in new_names:
    graphic_items += '      <div class="portfolio-item" data-category="graphics"><div class="portfolio-image"><img src="assets/images/portfolio/' + name + '" alt="Graphic design sample" loading="lazy"></div></div>\n'

new_graphics_items = graphic_items.rstrip("\n")

if old_graphics_item in content:
    content = content.replace(old_graphics_item, new_graphics_items)
    with open("portfolio.html", "w") as file:
        file.write(content)
    print("portfolio.html updated with real graphic designs successfully")
else:
    print("WARNING: graphics placeholder pattern not found in portfolio.html — no changes made")