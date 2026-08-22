#!/usr/bin/env python3
"""
Static site assembler for Tanveer Mohammed's portfolio.
Not part of the deployed site — run locally to regenerate the HTML pages
from the shared header/footer/icon fragments so every page stays consistent.
Usage: python3 build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE_NAME = "Tanveer Mohammed"
SITE_TAGLINE = "Lead Software Engineer — Java, Spring Boot & Cloud Architecture"
SITE_URL_PLACEHOLDER = "https://mohammedtanveer.github.io"  # update after deployment

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("experience.html", "Experience"),
    ("skills.html", "Skills"),
    ("projects.html", "Projects"),
    ("certifications.html", "Certifications"),
    ("education.html", "Education"),
    ("interests.html", "Interests"),
    ("contact.html", "Contact"),
]

ICONS = {
    "sun": '<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>',
    "moon": '<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79Z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>',
}


def render_head(title, description, canonical, og_type="website"):
    return f"""<meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{SITE_URL_PLACEHOLDER}/{canonical}" />
  <meta name="author" content="Tanveer Mohammed" />
  <meta name="robots" content="index, follow" />

  <meta property="og:type" content="{og_type}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{SITE_URL_PLACEHOLDER}/{canonical}" />
  <meta property="og:site_name" content="{SITE_NAME}" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{description}" />

  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/style.css" />
"""


def render_header(active):
    links = []
    for href, label in NAV_ITEMS:
        links.append(f'        <li><a href="{href}">{label}</a></li>')
    links_html = "\n".join(links)
    return f"""  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <nav class="nav" aria-label="Primary">
      <a class="brand" href="index.html">
        <span class="brand-mark">TM</span>
        {SITE_NAME}
      </a>
      <div class="nav-right">
        <ul class="nav-links" id="nav-links" data-nav-links>
{links_html}
        </ul>
        <button class="theme-toggle" type="button" data-theme-toggle aria-label="Toggle dark and light mode">
          {ICONS['sun']}
          {ICONS['moon']}
        </button>
        <button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="nav-links" aria-label="Toggle navigation menu">
          {ICONS['menu']}
        </button>
      </div>
    </nav>
  </header>
"""


FOOTER = f"""  <footer class="site-footer">
    <div class="container footer-inner">
      <p>&copy; <span data-year>2026</span> {SITE_NAME}. Built with static HTML, CSS &amp; JS — hosted for free.</p>
      <div class="footer-links">
        <a href="https://www.linkedin.com/in/mohammedtanveer/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        <a href="contact.html">Contact</a>
        <a href="sitemap.xml">Sitemap</a>
      </div>
    </div>
  </footer>
  <script src="assets/js/main.js"></script>
"""


def page(title, description, canonical, body, active=None, og_type="website", extra_head="", body_class=""):
    head = render_head(title, description, canonical, og_type)
    header = render_header(active)
    cls = f' class="{body_class}"' if body_class else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head}{extra_head}</head>
<body{cls}>
  <script>document.documentElement.classList.add('js');</script>
{header}
  <main id="main">
{body}
  </main>
{FOOTER}
</body>
</html>
"""


def write(filename, content):
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", filename)


if __name__ == "__main__":
    print("Fragments loaded. Import into page-building script.")
