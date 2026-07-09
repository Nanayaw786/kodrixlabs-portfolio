with open("css/style.css", "r") as file:
    content = file.read()

old_css = """.screenshot-box {
  aspect-ratio: 9 / 16;
  background: linear-gradient(135deg, var(--color-bg-alt), #eef0f4);
  border: 1.5px dashed var(--color-border);
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-muted);
  font-size: 0.9rem;
  font-weight: 500;
}"""

new_css = """.screenshot-box {
  aspect-ratio: 16 / 10;
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: var(--transition-fast);
}

.screenshot-box:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

.screenshot-box img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top;
  display: block;
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open("css/style.css", "w") as file:
        file.write(content)
    print("css/style.css screenshot-box styling updated for laptop screenshots successfully")
else:
    print("WARNING: CSS pattern not found in style.css — no changes made")