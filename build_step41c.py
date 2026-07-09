with open("js/main.js", "a") as file:
    file.write("""

// ===================================
// 7. CONTACT FORM SUBMISSION (FORMSPREE)
// ===================================
const contactForm = document.getElementById('contactForm');

if (contactForm) {
  const formSubmitBtn = document.getElementById('formSubmitBtn');
  const formStatus = document.getElementById('formStatus');

  contactForm.addEventListener('submit', function (event) {
    event.preventDefault();

    formSubmitBtn.disabled = true;
    formSubmitBtn.textContent = 'Sending...';
    formStatus.textContent = '';
    formStatus.className = 'form-status';

    const formData = new FormData(contactForm);

    fetch(contactForm.action, {
      method: 'POST',
      body: formData,
      headers: {
        Accept: 'application/json'
      }
    })
      .then(function (response) {
        if (response.ok) {
          formStatus.textContent = "Thanks! Your message has been sent — I'll get back to you soon.";
          formStatus.classList.add('success');
          contactForm.reset();
        } else {
          formStatus.textContent = 'Something went wrong. Please try again or email me directly.';
          formStatus.classList.add('error');
        }
      })
      .catch(function () {
        formStatus.textContent = 'Something went wrong. Please try again or email me directly.';
        formStatus.classList.add('error');
      })
      .finally(function () {
        formSubmitBtn.disabled = false;
        formSubmitBtn.textContent = 'Send Message';
      });
  });
}
""")
print("Contact form JavaScript added successfully")