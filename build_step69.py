with open("css/style.css", "r") as file:
    content = file.read()

old_css = """elevenlabs-convai {
  display: none;
}

elevenlabs-convai.visible {
  display: block;
}"""

new_css = """elevenlabs-convai {
  position: fixed;
  bottom: -9999px;
  left: -9999px;
  opacity: 0;
  pointer-events: none;
}

elevenlabs-convai.visible {
  position: fixed;
  bottom: 24px;
  right: 24px;
  left: auto;
  opacity: 1;
  pointer-events: auto;
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open("css/style.css", "w") as file:
        file.write(content)
    print("css/style.css elevenlabs-convai visibility fix applied successfully")
else:
    print("WARNING: CSS pattern not found in style.css — no changes made")
