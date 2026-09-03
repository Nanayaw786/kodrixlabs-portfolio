with open("pricing.html", "r", encoding="utf-8") as file:
    content = file.read()

old_block = """      All prices in Ghana Cedis (GHS). Traveling internationally?
      <span class="currency-toggle-label">Convert to:</span>
      <select id="currencySelect" class="currency-select">
        <option value="GHS">GHS (default)</option>
        <option value="USD">USD</option>
        <option value="GBP">GBP</option>
        <option value="EUR">EUR</option>
        <option value="CAD">CAD</option>
      </select>
      <span id="rateNote" class="rate-note"></span>"""

new_block = """      All prices in Ghana Cedis (GHS). Tap any plan to get a custom quote."""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open("pricing.html", "w", encoding="utf-8") as file:
        file.write(content)
    print("Currency selector removed from pricing.html")
else:
    print("WARNING: currency block not found — no changes made")
