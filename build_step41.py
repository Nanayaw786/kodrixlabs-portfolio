with open("contact.html", "r") as file:
    content = file.read()

old_contact_block = """    <div class="contact-cta">
      <a href="mailto:samuel.kodrixlabs@gmail.com" class="btn btn-primary">Email Me</a>
      <a href="#" class="btn btn-secondary" target="_blank">LinkedIn</a>
    </div>
    <div class="contact-details">
      <p>Email: samuel.kodrixlabs@gmail.com</p>
      <p>Location: Accra, Ghana (Remote Worldwide)</p>
    </div>"""

new_contact_block = """    <form class="contact-form" id="contactForm" action="https://formspree.io/f/xdarqobe" method="POST">
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" placeholder="Your full name" required>
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" placeholder="you@company.com" required>
      </div>
      <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" placeholder="Tell me about your project..." required></textarea>
      </div>
      <button type="submit" class="btn btn-primary form-submit" id="formSubmitBtn">Send Message</button>
      <p class="form-status" id="formStatus"></p>
    </form>

    <div class="contact-cta contact-cta-secondary">
      <a href="https://vt.tiktok.com/ZSCTcsRFe/" class="btn btn-secondary" target="_blank" rel="noopener">TikTok</a>
    </div>

    <div class="contact-details">
      <p>Email: samuel.kodrixlabs@gmail.com</p>
      <p>Location: Accra, Ghana (Remote Worldwide)</p>
    </div>"""

if old_contact_block in content:
    content = content.replace(old_contact_block, new_contact_block)
    with open("contact.html", "w") as file:
        file.write(content)
    print("contact.html updated with real contact form and TikTok link successfully")
else:
    print("WARNING: contact block pattern not found in contact.html — no changes made")