with open("js/main.js", "a", encoding="utf-8") as file:
    file.write("""

// ===================================
// 10. PRICING QUOTE MODAL
// ===================================
const quoteModal = document.getElementById('quoteModal');

if (quoteModal) {
  const quoteModalClose = document.getElementById('quoteModalClose');
  const quoteModalPlan = document.getElementById('quoteModalPlan');
  const quoteFormPlan = document.getElementById('quoteFormPlan');
  const quoteWhatsappBtn = document.getElementById('quoteWhatsappBtn');
  const quoteForm = document.getElementById('quoteForm');
  const quoteFormSubmitBtn = document.getElementById('quoteFormSubmitBtn');
  const quoteFormStatus = document.getElementById('quoteFormStatus');
  const whatsappNumber = '233505216213';

  const priceCards = document.querySelectorAll('.price-card[data-plan]');

  priceCards.forEach(function (card) {
    card.addEventListener('click', function () {
      const planName = card.getAttribute('data-plan');
      quoteModalPlan.textContent = 'Selected: ' + planName;
      quoteFormPlan.value = planName;

      const message = 'Hi Samuel, I am interested in the ' + planName + ' package. Can you tell me more?';
      quoteWhatsappBtn.href = 'https://wa.me/' + whatsappNumber + '?text=' + encodeURIComponent(message);

      quoteModal.classList.add('active');
      document.body.style.overflow = 'hidden';
    });
  });

  function closeQuoteModal() {
    quoteModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  quoteModalClose.addEventListener('click', closeQuoteModal);

  quoteModal.addEventListener('click', function (event) {
    if (event.target === quoteModal) {
      closeQuoteModal();
    }
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && quoteModal.classList.contains('active')) {
      closeQuoteModal();
    }
  });

  if (quoteForm) {
    quoteForm.addEventListener('submit', function (event) {
      event.preventDefault();

      quoteFormSubmitBtn.disabled = true;
      quoteFormSubmitBtn.textContent = 'Sending...';
      quoteFormStatus.textContent = '';
      quoteFormStatus.className = 'form-status';

      const formData = new FormData(quoteForm);

      fetch(quoteForm.action, {
        method: 'POST',
        body: formData,
        headers: { Accept: 'application/json' }
      })
        .then(function (response) {
          if (response.ok) {
            quoteFormStatus.textContent = 'Thanks! Samuel will follow up with a quote soon.';
            quoteFormStatus.classList.add('success');
            quoteForm.reset();
          } else {
            quoteFormStatus.textContent = 'Something went wrong. Please try WhatsApp instead.';
            quoteFormStatus.classList.add('error');
          }
        })
        .catch(function () {
          quoteFormStatus.textContent = 'Something went wrong. Please try WhatsApp instead.';
          quoteFormStatus.classList.add('error');
        })
        .finally(function () {
          quoteFormSubmitBtn.disabled = false;
          quoteFormSubmitBtn.textContent = 'Send Request';
        });
    });
  }
}
""")
print("Quote modal JavaScript added successfully")
