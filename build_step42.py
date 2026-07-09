with open("contact.html", "r") as file:
    content = file.read()

old_form = """    <form class="contact-form" id="contactForm" action="https://formspree.io/f/xdarqobe" method="POST">
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
    </form>"""

new_form = """    <div class="contact-form-card">
      <form class="contact-form" id="contactForm" action="https://formspree.io/f/xdarqobe" method="POST">
        <div class="form-row">
          <div class="form-group">
            <label for="name">Full Name</label>
            <input type="text" id="name" name="name" placeholder="Your full name" required>
          </div>
          <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" placeholder="+233 00 000 0000" required>
          </div>
        </div>
        <div class="form-group">
          <label for="email">Email Address</label>
          <input type="email" id="email" name="email" placeholder="you@company.com" required>
        </div>
        <div class="form-group">
          <label for="message">Project Details</label>
          <textarea id="message" name="message" rows="5" placeholder="Tell me about your project, timeline, and goals..." required></textarea>
        </div>
        <button type="submit" class="btn btn-primary form-submit" id="formSubmitBtn">
          <span>Send Message</span>
        </button>
        <p class="form-status" id="formStatus"></p>
      </form>
    </div>"""

if old_form in content:
    content = content.replace(old_form, new_form)
    with open("contact.html", "w") as file:
        file.write(content)
    print("contact.html form updated with phone field and card wrapper successfully")
else:
    print("WARNING: form pattern not found in contact.html — no changes made")