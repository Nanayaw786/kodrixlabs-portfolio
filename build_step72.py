with open("js/main.js", "a", encoding="utf-8") as file:
    file.write("""

// ===================================
// 9. LIVE CURRENCY CONVERTER (PRICING PAGE)
// ===================================
const currencySelect = document.getElementById('currencySelect');

if (currencySelect) {
  const rateNote = document.getElementById('rateNote');
  const priceElements = document.querySelectorAll('.price-amount[data-ghs]');

  let exchangeRates = null;

  function formatCurrency(amount, currency) {
    const symbols = { USD: '$', GBP: '\\u00a3', EUR: '\\u20ac', CAD: 'CA$' };
    const rounded = Math.round(amount);
    return (symbols[currency] || currency + ' ') + rounded.toLocaleString();
  }

  function applyCurrency(currency) {
    priceElements.forEach(function (el) {
      const ghsValue = parseFloat(el.getAttribute('data-ghs'));
      const suffixSpan = el.querySelector('span');
      const suffixText = suffixSpan ? suffixSpan.outerHTML : '';

      if (currency === 'GHS' || !exchangeRates) {
        const displayText = el.getAttribute('data-original') || el.textContent;
        return;
      }

      const rate = exchangeRates[currency];
      if (!rate) return;

      const converted = ghsValue * rate;
      const isRange = el.textContent.includes('-') || el.textContent.includes('From');
      const prefix = el.textContent.includes('From') ? 'From ' : '';

      el.innerHTML = prefix + formatCurrency(converted, currency) + suffixText;
    });
  }

  // Store original GHS text before any conversion
  priceElements.forEach(function (el) {
    el.setAttribute('data-original', el.innerHTML);
  });

  currencySelect.addEventListener('change', function () {
    const selected = currencySelect.value;

    if (selected === 'GHS') {
      priceElements.forEach(function (el) {
        el.innerHTML = el.getAttribute('data-original');
      });
      rateNote.textContent = '';
      return;
    }

    if (exchangeRates) {
      applyCurrency(selected);
      return;
    }

    rateNote.textContent = 'Loading live rates...';

    fetch('https://open.er-api.com/v6/latest/GHS')
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        if (data && data.rates) {
          exchangeRates = data.rates;
          applyCurrency(selected);
          rateNote.textContent = 'Live rate as of ' + (data.time_last_update_utc || 'today') + '. Approximate only.';
        } else {
          rateNote.textContent = 'Could not load live rates. Showing GHS.';
        }
      })
      .catch(function () {
        rateNote.textContent = 'Could not load live rates. Showing GHS.';
      });
  });
}
""")
print("Currency converter JavaScript added successfully")
