pages = [
    "index.html",
    "about.html",
    "services.html",
    "skills.html",
    "case-studies.html",
    "portfolio.html",
    "contact.html",
]

whatsapp_number = "233505216213"
prefilled_message = "Hi Samuel, I found your site and I'd like to talk about a project."

old_snippet = """<a href="https://wa.me/""" + whatsapp_number + """?text=""" + prefilled_message.replace(" ", "%20") + """" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28" fill="#ffffff">
    <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21h.01c5.46 0 9.9-4.45 9.9-9.91 0-2.65-1.03-5.14-2.9-7.01A9.876 9.876 0 0 0 12.04 2zm0 1.67c2.2 0 4.27.86 5.82 2.42a8.183 8.183 0 0 1 2.41 5.82c0 4.54-3.7 8.23-8.24 8.23-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.188 8.188 0 0 1-1.26-4.38c.01-4.55 3.71-8.23 8.26-8.23zm-4.52 4.7c-.16 0-.42.06-.64.31-.22.25-.85.83-.85 2.02 0 1.19.87 2.34.99 2.5.12.16 1.7 2.72 4.19 3.71 2.07.82 2.49.66 2.94.62.45-.04 1.45-.59 1.65-1.16.2-.57.2-1.06.14-1.16-.06-.1-.22-.16-.46-.28-.24-.12-1.45-.71-1.67-.79-.22-.08-.39-.12-.55.12-.16.24-.63.79-.77.95-.14.16-.28.18-.52.06-.24-.12-1.02-.38-1.94-1.2-.72-.64-1.2-1.43-1.34-1.67-.14-.24-.01-.37.11-.49.11-.11.24-.28.36-.42.12-.14.16-.24.24-.4.08-.16.04-.3-.02-.42-.06-.12-.55-1.34-.76-1.83-.2-.48-.4-.42-.55-.42h-.47z"/>
  </svg>
</a>
"""

for page in pages:
    with open(page, "r") as file:
        content = file.read()

    if old_snippet in content:
        content = content.replace(old_snippet, "")
        with open(page, "w") as file:
            file.write(content)
        print(page + ": standalone WhatsApp button removed")
    else:
        print(page + ": pattern not found (may already be removed)")
