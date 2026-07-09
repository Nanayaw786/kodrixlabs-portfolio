import os
import shutil

portfolio_folder = "assets/images/portfolio"
case_studies_folder = "assets/images/case-studies"

# ===================================
# PART 1: RENAME FACEBOOK FILES
# ===================================
old_fb_names = ["Facebook 1.png", "Facebook 2.png", "Facebook 3.png"]
new_fb_names = []

for index, old_name in enumerate(old_fb_names, start=1):
    new_name = "campaign-facebook-" + str(index) + ".png"
    old_path = os.path.join(portfolio_folder, old_name)
    new_path = os.path.join(portfolio_folder, new_name)

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print("Renamed: " + old_name + " -> " + new_name)
        new_fb_names.append(new_name)
    else:
        print("WARNING: file not found, skipped: " + old_name)

# ===================================
# PART 2: COPY TIKTOK SCREENSHOTS INTO PORTFOLIO FOLDER
# ===================================
tiktok_names = []
for i in range(1, 10):
    source_name = "tiktok-screenshot-" + str(i) + ".png"
    dest_name = "campaign-tiktok-" + str(i) + ".png"
    source_path = os.path.join(case_studies_folder, source_name)
    dest_path = os.path.join(portfolio_folder, dest_name)

    if os.path.exists(source_path):
        shutil.copyfile(source_path, dest_path)
        print("Copied: " + source_name + " -> portfolio/" + dest_name)
        tiktok_names.append(dest_name)
    else:
        print("WARNING: source file not found, skipped: " + source_name)

all_campaign_images = tiktok_names + new_fb_names

# ===================================
# PART 3: REPLACE CAMPAIGN PLACEHOLDER IN portfolio.html
# ===================================
with open("portfolio.html", "r") as file:
    content = file.read()

old_campaign_item = """      <div class="portfolio-item" data-category="campaigns"><div class="portfolio-placeholder">Campaign</div></div>"""

campaign_items = ""
for name in all_campaign_images:
    campaign_items += '      <div class="portfolio-item" data-category="campaigns"><div class="portfolio-image"><img src="assets/images/portfolio/' + name + '" alt="Campaign screenshot" loading="lazy"></div></div>\n'

new_campaign_items = campaign_items.rstrip("\n")

if old_campaign_item in content:
    content = content.replace(old_campaign_item, new_campaign_items)
    with open("portfolio.html", "w") as file:
        file.write(content)
    print("portfolio.html updated with campaign screenshots successfully")
else:
    print("WARNING: campaign placeholder pattern not found in portfolio.html — no changes made")