import re

with open("pricing.html", "r", encoding="utf-8") as file:
    content = file.read()

# Add data-plan and cursor-pointer class to every price-card div, using each card's <h4> text as the plan name
def add_plan_attr(match):
    full_card = match.group(0)
    title_match = re.search(r"<h4>(.*?)</h4>", full_card)
    plan_name = title_match.group(1) if title_match else "Plan"
    if 'data-plan=' in full_card:
        return full_card
    updated = full_card.replace('class="price-card"', 'class="price-card" data-plan="' + plan_name + '"', 1)
    updated = updated.replace('class="price-card featured"', 'class="price-card featured" data-plan="' + plan_name + '"', 1)
    return updated

content = re.sub(r'<div class="price-card( featured)?">.*?</div>\s*(?=<div class="price-card|</div>\s*<p class="price-note"|</div>\s*</div>)', add_plan_attr, content, flags=re.DOTALL)

# Insert modal HTML right before the closing </section>, only once
modal_html = """
    <div class="quote-modal" id="quoteModal">
      <div class="quote-modal-inner">
        <button class="quote-modal-close" id="quoteModalClose" aria-label="Close">&times;</button>
        <h3 id="quoteModalTitle">Get a Quote</h3>
        <p class="quote-modal-plan" id="quoteModalPlan"></p>

        <div class="quote-modal-options">
          <a href="#" id="quoteWhatsappBtn" class="btn btn-primary" target="_blank" rel="noopener">Message on WhatsApp</a>
          <p class="quote-or">or</p>
          <form class="quote-form" id="quoteForm" action="https://formspree.io/f/xdarqobe" method="POST">
            <input type="hidden" name="plan" id="quoteFormPlan">
            <div class="form-group">
              <label for="quoteName">Name</label>
              <input type="text" id="quoteName" name="name" placeholder="Your full name" required>
            </div>
            <div class="form-group">
              <label for="quoteEmail">Email</label>
              <input type="email" id="quoteEmail" name="email" placeholder="you@company.com" required>
            </div>
            <div class="form-group">
              <label for="quotePhone">Phone</label>
              <input type="tel" id="quotePhone" name="phone" placeholder="+233 00 000 0000" required>
            </div>
            <button type="submit" class="btn btn-secondary form-submit" id="quoteFormSubmitBtn">Send Request</button>
            <p class="form-status" id="quoteFormStatus"></p>
          </form>
        </div>
      </div>
    </div>

"""

if 'id="quoteModal"' not in content:
    content = content.replace("  </div>\n</section>", "  </div>\n" + modal_html + "</section>", 1)

with open("pricing.html", "w", encoding="utf-8") as file:
    file.write(content)

print("Price cards made clickable and quote modal added successfully")
