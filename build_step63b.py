with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   28. WHATSAPP FLOATING BUTTON
=================================== */
.whatsapp-float {
  position: fixed;
  bottom: 24px;
  left: 24px;
  width: 58px;
  height: 58px;
  background: #25D366;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(37, 211, 102, 0.4);
  z-index: 1500;
  transition: var(--transition-fast);
}

.whatsapp-float:hover {
  transform: scale(1.08);
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.5);
}

@media (max-width: 700px) {
  .whatsapp-float {
    width: 52px;
    height: 52px;
    bottom: 18px;
    left: 18px;
  }
}
""")
print("WhatsApp button CSS added successfully")
