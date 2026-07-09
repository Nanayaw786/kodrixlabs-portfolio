with open("portfolio.html", "r") as file:
    content = file.read()

old_closing = """</section>
"""

new_closing = """</section>

<div class="lightbox" id="lightbox">
  <button class="lightbox-close" id="lightboxClose" aria-label="Close">&times;</button>
  <button class="lightbox-prev" id="lightboxPrev" aria-label="Previous image">&#8249;</button>
  <img class="lightbox-image" id="lightboxImage" src="" alt="Enlarged portfolio image">
  <button class="lightbox-next" id="lightboxNext" aria-label="Next image">&#8250;</button>
  <div class="lightbox-counter" id="lightboxCounter"></div>
</div>
"""

last_index = content.rfind(old_closing)
if last_index != -1:
    content = content[:last_index] + new_closing + content[last_index + len(old_closing):]
    with open("portfolio.html", "w") as file:
        file.write(content)
    print("Lightbox markup added to portfolio.html successfully")
else:
    print("WARNING: closing section tag not found in portfolio.html — no changes made")