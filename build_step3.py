with open("css/style.css", "w") as file:
    file.write("""/* ===================================
   1. CSS VARIABLES / DESIGN SYSTEM
=================================== */
:root {
  --color-bg: #ffffff;
  --color-bg-alt: #f8f9fb;
  --color-text: #14161a;
  --color-text-muted: #5b616e;
  --color-border: #e7e9ee;

  --color-primary: #2f5bff;
  --color-primary-dark: #1d3fd1;
  --color-primary-light: #eaf0ff;
  --color-accent: #10b981;

  --font-heading: 'Plus Jakarta Sans', sans-serif;
  --font-body: 'Inter', sans-serif;

  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 22px;

  --shadow-sm: 0 1px 2px rgba(20, 22, 26, 0.04), 0 1px 3px rgba(20, 22, 26, 0.06);
  --shadow-md: 0 4px 16px rgba(20, 22, 26, 0.06), 0 2px 6px rgba(20, 22, 26, 0.04);
  --shadow-lg: 0 20px 40px rgba(20, 22, 26, 0.08), 0 8px 16px rgba(20, 22, 26, 0.04);

  --container-width: 1180px;
  --section-padding: 120px;

  --transition-fast: 0.2s ease;
  --transition-medium: 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}

/* ===================================
   2. RESET
=================================== */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-body);
  color: var(--color-text);
  background: var(--color-bg);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

img {
  max-width: 100%;
  display: block;
}

a {
  text-decoration: none;
  color: inherit;
}

ul, ol {
  list-style: none;
}

button {
  font-family: inherit;
  cursor: pointer;
  border: none;
  background: none;
}

/* ===================================
   3. TYPOGRAPHY
=================================== */
h1, h2, h3, h4 {
  font-family: var(--font-heading);
  font-weight: 700;
  color: var(--color-text);
  letter-spacing: -0.02em;
  line-height: 1.15;
}

h1 {
  font-size: clamp(2.6rem, 5vw, 4.2rem);
  font-weight: 800;
}

h2 {
  font-size: clamp(2rem, 3.5vw, 2.75rem);
  margin-bottom: 20px;
}

h3 {
  font-size: 1.25rem;
  margin-bottom: 10px;
}

h4 {
  font-size: 1.05rem;
  margin-bottom: 12px;
  color: var(--color-text);
}

p {
  color: var(--color-text-muted);
  font-size: 1.05rem;
}

.section-tag {
  display: inline-block;
  font-family: var(--font-heading);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-primary);
  background: var(--color-primary-light);
  padding: 6px 14px;
  border-radius: 100px;
  margin-bottom: 18px;
}

.section-subtext {
  max-width: 620px;
  margin-bottom: 50px;
  font-size: 1.1rem;
}

/* ===================================
   4. LAYOUT / CONTAINERS
=================================== */
.container {
  width: 100%;
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 0 24px;
}

section {
  padding: var(--section-padding) 0;
}

/* ===================================
   5. BUTTONS
=================================== */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.95rem;
  padding: 15px 30px;
  border-radius: var(--radius-sm);
  transition: var(--transition-fast);
}

.btn-primary {
  background: var(--color-primary);
  color: #ffffff;
  box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
  background: var(--color-primary-dark);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-secondary {
  background: var(--color-bg);
  color: var(--color-text);
  border: 1.5px solid var(--color-border);
}

.btn-secondary:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
  transform: translateY(-2px);
}
""")
print("css/style.css created successfully")