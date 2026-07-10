with open("js/main.js", "a") as file:
    file.write("""

// ===================================
// 8. COMBINED CONTACT FAB (AI + WHATSAPP)
// ===================================
const contactFabMain = document.getElementById('contactFabMain');
const contactFabMenu = document.getElementById('contactFabMenu');
const fabIconOpen = document.getElementById('fabIconOpen');
const fabIconClose = document.getElementById('fabIconClose');
const openAiChatBtn = document.getElementById('openAiChatBtn');

if (contactFabMain && contactFabMenu) {
  contactFabMain.addEventListener('click', function () {
    const isOpen = contactFabMenu.classList.toggle('open');
    fabIconOpen.style.display = isOpen ? 'none' : 'block';
    fabIconClose.style.display = isOpen ? 'block' : 'none';
  });

  document.addEventListener('click', function (event) {
    const wrapper = document.getElementById('contactFabWrapper');
    if (wrapper && !wrapper.contains(event.target)) {
      contactFabMenu.classList.remove('open');
      fabIconOpen.style.display = 'block';
      fabIconClose.style.display = 'none';
    }
  });
}

if (openAiChatBtn) {
  openAiChatBtn.addEventListener('click', function () {
    const aiWidget = document.querySelector('elevenlabs-convai');
    if (aiWidget) {
      aiWidget.classList.add('visible');
    }
    contactFabMenu.classList.remove('open');
    fabIconOpen.style.display = 'block';
    fabIconClose.style.display = 'none';
  });
}
""")
print("Combined contact FAB JavaScript added successfully")
