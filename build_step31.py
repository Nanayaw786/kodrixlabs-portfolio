import os

# ===================================
# PART 1: RENAME SCREENSHOTS
# ===================================
folder = "assets/images/case-studies"

old_names = [
    "Screen Shot 2026-07-09 at 8.53.00 PM.png",
    "Screen Shot 2026-07-09 at 8.53.20 PM.png",
    "Screen Shot 2026-07-09 at 8.53.37 PM.png",
    "Screen Shot 2026-07-09 at 8.53.49 PM.png",
    "Screen Shot 2026-07-09 at 8.53.53 PM.png",
    "Screen Shot 2026-07-09 at 9.06.41 PM.png",
    "Screen Shot 2026-07-09 at 9.06.56 PM.png",
    "Screen Shot 2026-07-09 at 9.07.10 PM.png",
    "Screen Shot 2026-07-09 at 9.09.09 PM.png",
]

new_names = []
for index, old_name in enumerate(old_names, start=1):
    new_name = "tiktok-screenshot-" + str(index) + ".png"
    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print("Renamed: " + old_name + " -> " + new_name)
        new_names.append(new_name)
    else:
        print("WARNING: file not found, skipped: " + old_name)

# ===================================
# PART 2: SWAP PLACEHOLDERS IN CASE-STUDIES.HTML
# ===================================
with open("case-studies.html", "r") as file:
    content = file.read()

old_screenshots_block = """      <div class="case-study-block">
        <h4>Screenshots</h4>
        <div class="screenshot-placeholders">
          <div class="screenshot-box">Screenshot 1</div>
          <div class="screenshot-box">Screenshot 2</div>
          <div class="screenshot-box">Screenshot 3</div>
        </div>
      </div>"""

image_tags = ""
for name in new_names:
    image_tags += '          <div class="screenshot-box"><img src="assets/images/case-studies/' + name + '" alt="TikTok analytics screenshot" loading="lazy"></div>\n'

new_screenshots_block = """      <div class="case-study-block">
        <h4>Screenshots</h4>
        <div class="screenshot-placeholders">
""" + image_tags + """        </div>
      </div>"""

if old_screenshots_block in content:
    content = content.replace(old_screenshots_block, new_screenshots_block)
    with open("case-studies.html", "w") as file:
        file.write(content)
    print("case-studies.html updated with real screenshots successfully")
else:
    print("WARNING: screenshots block pattern not found in case-studies.html — no changes made")