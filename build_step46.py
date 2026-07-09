from PIL import Image, ImageDraw, ImageFont

width, height = 1200, 630

color_bg_top = (234, 240, 255)
color_bg_bottom = (255, 255, 255)
color_primary = (47, 91, 255)
color_text = (20, 22, 26)
color_muted = (91, 97, 110)
color_accent = (16, 185, 129)

img = Image.new("RGB", (width, height), color_bg_bottom)
draw = ImageDraw.Draw(img)

for y in range(height):
    ratio = y / height
    r = int(color_bg_top[0] + (color_bg_bottom[0] - color_bg_top[0]) * ratio)
    g = int(color_bg_top[1] + (color_bg_bottom[1] - color_bg_top[1]) * ratio)
    b = int(color_bg_top[2] + (color_bg_bottom[2] - color_bg_top[2]) * ratio)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

for x in range(width):
    ratio = x / width
    r = int(color_primary[0] + (color_accent[0] - color_primary[0]) * ratio)
    g = int(color_primary[1] + (color_accent[1] - color_primary[1]) * ratio)
    b = int(color_primary[2] + (color_accent[2] - color_primary[2]) * ratio)
    draw.line([(x, 0), (x, 10)], fill=(r, g, b))

def load_font(paths, size):
    for path in paths:
        try:
            return ImageFont.truetype(path, size)
        except:
            continue
    return ImageFont.load_default()

bold_font_paths = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial Bold.ttf",
]
regular_font_paths = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial.ttf",
]

logo_font = load_font(bold_font_paths, 72)
tagline_font = load_font(bold_font_paths, 40)
subtext_font = load_font(regular_font_paths, 28)

logo_text = "Kodrixlabs."
draw.text((80, 220), logo_text, font=logo_font, fill=color_text)

tagline_text = "Software Developer & Digital Growth Specialist"
draw.text((80, 320), tagline_text, font=tagline_font, fill=color_primary)

subtext = "Websites, Mobile Apps & Social Media Growth"
draw.text((80, 390), subtext, font=subtext_font, fill=color_muted)

draw.ellipse((980, 480, 1120, 620), fill=color_primary)
draw.ellipse((1010, 510, 1090, 590), fill=(255, 255, 255))

img.save("assets/images/og-image.png")
print("assets/images/og-image.png created successfully")
