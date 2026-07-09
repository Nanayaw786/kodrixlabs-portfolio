from PIL import Image, ImageDraw, ImageFont

size = 512
color_primary = (47, 91, 255)

img = Image.new("RGB", (size, size), color_primary)
draw = ImageDraw.Draw(img)

# Rounded corners effect via mask
mask = Image.new("L", (size, size), 0)
mask_draw = ImageDraw.Draw(mask)
radius = 100
mask_draw.rounded_rectangle([(0, 0), (size, size)], radius=radius, fill=255)

def load_font(paths, font_size):
    for path in paths:
        try:
            return ImageFont.truetype(path, font_size)
        except:
            continue
    return ImageFont.load_default()

bold_font_paths = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial Bold.ttf",
]

font = load_font(bold_font_paths, 300)

text = "K"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
position = ((size - text_width) / 2 - bbox[0], (size - text_height) / 2 - bbox[1])

draw.text(position, text, font=font, fill=(255, 255, 255))

final_img = Image.new("RGBA", (size, size))
final_img.paste(img, (0, 0), mask)

final_img.save("assets/images/favicon.png")
print("assets/images/favicon.png created successfully")
