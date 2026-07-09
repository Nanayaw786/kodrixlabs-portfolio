with open("css/style.css", "a") as file:
    file.write("""

/* ===================================
   22. GLOBAL MOBILE REFINEMENTS
=================================== */

/* Ensure filtered-out portfolio items stay hidden regardless of inline JS styles */
.portfolio-item.hidden {
  display: none !important;
}

@media (max-width: 768px) {
  :root {
    --section-padding: 80px;
  }

  .container {
    padding: 0 20px;
  }

  h1 {
    font-size: 2.2rem;
  }

  h2 {
    font-size: 1.7rem;
  }

  .hero {
    padding-top: 130px;
    padding-bottom: 70px;
  }

  .hero-subtext {
    font-size: 1rem;
  }

  .hero-cta {
    flex-direction: column;
    align-items: center;
    gap: 12px;
  }

  .hero-cta .btn {
    width: 100%;
    max-width: 280px;
  }

  .hero-stats {
    gap: 24px;
  }

  .stat-number {
    font-size: 1.7rem;
  }

  .case-study-card {
    padding: 26px 18px;
  }

  .case-study-header h3 {
    font-size: 1.3rem;
  }

  .metrics-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }

  .metric {
    padding: 16px 10px;
  }

  .metric-number {
    font-size: 1.4rem;
  }

  .about-inner p,
  .services p,
  .section-subtext {
    font-size: 0.98rem;
  }

  .navbar-inner {
    height: 68px;
  }
}

@media (max-width: 420px) {
  h1 {
    font-size: 1.9rem;
  }

  .metrics-grid {
    grid-template-columns: 1fr 1fr;
  }

  .screenshot-placeholders {
    grid-template-columns: 1fr;
  }

  .stat-number {
    font-size: 1.5rem;
  }

  .stat-label {
    font-size: 0.78rem;
  }
}
""")
print("Mobile responsiveness refinements added successfully")