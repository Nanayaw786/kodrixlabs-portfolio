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
prefilled_message = "Hi%20Samuel,%20I%20found%20your%20site%20and%20I'd%20like%20to%20talk%20about%20a%20project."

combined_snippet = """<div class="contact-fab-wrapper" id="contactFabWrapper">
  <div class="contact-fab-menu" id="contactFabMenu">
    <a href="https://wa.me/""" + whatsapp_number + """?text=""" + prefilled_message + """" class="contact-fab-option" target="_blank" rel="noopener">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" fill="#25D366">
        <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21h.01c5.46 0 9.9-4.45 9.9-9.91 0-2.65-1.03-5.14-2.9-7.01A9.876 9.876 0 0 0 12.04 2zm0 1.67c2.2 0 4.27.86 5.82 2.42a8.183 8.183 0 0 1 2.41 5.82c0 4.54-3.7 8.23-8.24 8.23-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.188 8.188 0 0 1-1.26-4.38c.01-4.55 3.71-8.23 8.26-8.23zm-4.52 4.7c-.16 0-.42.06-.64.31-.22.25-.85.83-.85 2.02 0 1.19.87 2.34.99 2.5.12.16 1.7 2.72 4.19 3.71 2.07.82 2.49.66 2.94.62.45-.04 1.45-.59 1.65-1.16.2-.57.2-1.06.14-1.16-.06-.1-.22-.16-.46-.28-.24-.12-1.45-.71-1.67-.79-.22-.08-.39-.12-.55.12-.16.24-.63.79-.77.95-.14.16-.28.18-.52.06-.24-.12-1.02-.38-1.94-1.2-.72-.64-1.2-1.43-1.34-1.67-.14-.24-.01-.37.11-.49.11-.11.24-.28.36-.42.12-.14.16-.24.24-.4.08-.16.04-.3-.02-.42-.06-.12-.55-1.34-.76-1.83-.2-.48-.4-.42-.55-.42h-.47z"/>
      </svg>
      <span>WhatsApp</span>
    </a>
    <button class="contact-fab-option" id="openAiChatBtn" type="button">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="var(--color-primary)" stroke-width="2">
        <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
      </svg>
      <span>Chat with AI</span>
    </button>
  </div>
  <button class="contact-fab-main" id="contactFabMain" aria-label="Contact options" type="button">
    <svg id="fabIconOpen" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#ffffff" stroke-width="2">
      <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
    </svg>
    <svg id="fabIconClose" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#ffffff" stroke-width="2" style="display:none;">
      <line x1="18" y1="6" x2="6" y2="18"/>
      <line x1="6" y1="6" x2="18" y2="18"/>
    </svg>
  </button>
</div>
"""

anchor = "</body>"

for page in pages:
    with open(page, "r") as file:
        content = file.read()

    if "contact-fab-wrapper" in content:
        print(page + ": combined FAB already present (skipped)")
        continue

    if anchor in content:
        content = content.replace(anchor, combined_snippet + anchor, 1)
        with open(page, "w") as file:
            file.write(content)
        print(page + ": combined contact FAB added successfully")
    else:
        print("WARNING: closing body tag not found in " + page)
