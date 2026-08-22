#!/usr/bin/env python3
"""Generates all HTML pages for the portfolio from build.py fragments.
Run: python3 pages.py
"""
from build import page, write

# ---------------------------------------------------------------------------
# Reusable icon snippets (inline SVG, currentColor so they follow theme)
# ---------------------------------------------------------------------------
ICO = {
    "briefcase": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "map": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "sparkles": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v4M12 17v4M5 5l2.5 2.5M16.5 16.5L19 19M3 12h4M17 12h4M5 19l2.5-2.5M16.5 7.5L19 5"/></svg>',
    "award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M9 13.5 7 22l5-3 5 3-2-8.5"/></svg>',
    "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    "cloud": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>',
    "database": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3"/></svg>',
    "tool": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "cpu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg>',
    "graduation": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.66 2.69 3 6 3s6-1.34 6-3v-5"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.03-1.85-3.03-1.85 0-2.14 1.45-2.14 2.94v5.66H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    "server": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="7" rx="1"/><rect x="2" y="14" width="20" height="7" rx="1"/><line x1="6" y1="6.5" x2="6.01" y2="6.5"/><line x1="6" y1="17.5" x2="6.01" y2="17.5"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "external": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>',
}

DESC_DEFAULT = "Tanveer Mohammed is a Lead Software Engineer specializing in Java, Spring Boot, enterprise cloud architecture (Azure & AWS), and AI-enabled backend platforms."

# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
home_body = f"""
    <section class="hero">
      <div class="hero-inner">
        <div class="reveal in-view">
          <span class="eyebrow"><span class="dot"></span>Open to select opportunities</span>
          <h1>Tanveer Mohammed</h1>
          <p class="headline">Lead Software Engineer — Java &amp; Spring Boot, Azure &amp; AWS Cloud Architecture, AI-Enabled Enterprise Platforms</p>
          <p class="lede">I design and ship backend systems and cloud architecture for enterprise-scale platforms — currently leading engineering for MetLife's claims-processing systems on Azure, after seven years architecting Oracle's CRM Fusion SaaS products used by Fortune&nbsp;500 customers.</p>
          <div class="hero-cta">
            <a class="btn btn-primary" href="experience.html">View My Experience {ICO['arrow']}</a>
            <a class="btn btn-secondary" href="skills.html">View My Skills</a>
            <a class="btn btn-ghost" href="contact.html">Contact Me</a>
          </div>
          <div class="hero-meta">
            <span>{ICO['map']} Cary, North Carolina, United States</span>
            <span>{ICO['briefcase']} Lead Software Engineer / Lead Data Engineer at MetLife</span>
          </div>
        </div>
        <div class="hero-portrait reveal in-view">
          <div class="portrait-frame">
            <!-- Swap this monogram block for <img src="assets/img/portrait.jpg" alt="Portrait of Tanveer Mohammed" /> once a headshot file is provided. -->
            <div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg, var(--accent-soft), transparent);">
              <span style="font-family:var(--font-mono);font-weight:700;font-size:3.4rem;color:var(--accent);">TM</span>
            </div>
          </div>
          <div class="portrait-badge"><span class="dot"></span>Cary, NC · Hybrid</div>
        </div>
      </div>
    </section>

    <section class="section reveal">
      <div class="container">
        <div class="section-head">
          <p class="kicker">Snapshot</p>
          <h2>A decade-plus building enterprise software that scales</h2>
          <p>From government and healthcare integrations to Fortune 500 CRM platforms to enterprise insurance claims systems — here's the throughline.</p>
        </div>
        <div class="grid grid-4">
          <div class="card reveal">
            <div class="skill-card"><h3><span class="ic">{ICO['briefcase']}</span>13+ years</h3></div>
            <p style="color:var(--text-muted);font-size:0.92rem;margin:0;">In enterprise software engineering, from Oracle to NetApp to MetLife.</p>
          </div>
          <div class="card reveal">
            <div class="skill-card"><h3><span class="ic">{ICO['cloud']}</span>Multi-cloud</h3></div>
            <p style="color:var(--text-muted);font-size:0.92rem;margin:0;">Hands-on Azure (AKS, APIM, DevOps) and AWS (CloudWatch), certified in both ecosystems.</p>
          </div>
          <div class="card reveal">
            <div class="skill-card"><h3><span class="ic">{ICO['layers']}</span>Full-stack depth</h3></div>
            <p style="color:var(--text-muted);font-size:0.92rem;margin:0;">Java &amp; Spring Boot services, REST APIs, Oracle/SQL databases, and the DevOps pipelines that ship them.</p>
          </div>
          <div class="card reveal">
            <div class="skill-card"><h3><span class="ic">{ICO['sparkles']}</span>AI-enabled</h3></div>
            <p style="color:var(--text-muted);font-size:0.92rem;margin:0;">Generative AI, ML-backed testing, and AI-driven recommendation features shipped in production.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section alt reveal">
      <div class="container">
        <div class="section-head">
          <p class="kicker">Currently</p>
          <h2>Lead Software Engineer / Lead Data Engineer — MetLife</h2>
          <p>Feb 2024 – Present · Cary, North Carolina · Hybrid</p>
        </div>
        <div class="card">
          <ul class="role-list" style="margin:0;">
            <li>Lead engineer for MetLife's claims-processing platform — owning backend architecture, cloud infrastructure, and data engineering end to end.</li>
            <li>Architected enterprise claims-processing systems on Azure Kubernetes Service (AKS) with Java Spring Boot microservices, improving resiliency and horizontal scalability across high-volume insurance workflows.</li>
            <li>Optimized SQL and Oracle database query plans for 80%+ performance gains, layering in Redis caching to cut response times.</li>
          </ul>
        </div>
        <div class="section-cta">
          <a class="btn btn-secondary" href="experience.html">See the full career timeline {ICO['arrow']}</a>
        </div>
      </div>
    </section>

    <section class="section reveal">
      <div class="container center">
        <div class="section-head" style="margin-left:auto;margin-right:auto;">
          <p class="kicker">Let's connect</p>
          <h2>Hiring, collaborating, or just want to talk architecture?</h2>
          <p style="margin:0 auto;">I'm always glad to hear from recruiters, technology leaders, and fellow engineers.</p>
        </div>
        <div class="hero-cta" style="justify-content:center;">
          <a class="btn btn-primary" href="contact.html">Contact Me {ICO['arrow']}</a>
          <a class="btn btn-secondary" href="https://www.linkedin.com/in/mohammedtanveer/" target="_blank" rel="noopener noreferrer">{ICO['linkedin']} LinkedIn Profile</a>
        </div>
      </div>
    </section>
"""

write("index.html", page(
    title="Tanveer Mohammed — Lead Software Engineer | Java, Spring Boot & Cloud Architecture",
    description=DESC_DEFAULT,
    canonical="index.html",
    body=home_body,
    active="index.html",
    extra_head='  <script type="application/ld+json">\n  {\n    "@context": "https://schema.org",\n    "@type": "Person",\n    "name": "Tanveer Mohammed",\n    "jobTitle": "Lead Software Engineer",\n    "worksFor": {"@type": "Organization", "name": "MetLife"},\n    "url": "https://mohammedtanveer.github.io",\n    "sameAs": ["https://www.linkedin.com/in/mohammedtanveer/"],\n    "address": {"@type": "PostalAddress", "addressLocality": "Cary", "addressRegion": "NC", "addressCountry": "US"},\n    "knowsAbout": ["Java", "Spring Boot", "Microsoft Azure", "Amazon Web Services", "Enterprise Software Architecture", "Generative AI"]\n  }\n  </script>\n',
))

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
about_body = f"""
    <section class="page-hero container reveal in-view">
      <p class="kicker">About</p>
      <h1>Enterprise software, built to last — and built to scale.</h1>
      <p>The story behind thirteen-plus years of backend engineering, cloud architecture, and a steady move toward AI-assisted development.</p>
    </section>

    <section class="section reveal">
      <div class="container about-grid">
        <div class="prose">
          <p>I'm a Lead Software Engineer based in Cary, North Carolina, currently leading backend architecture and data engineering for MetLife's claims-processing platform. My work sits at the intersection of enterprise software, cloud infrastructure, and — increasingly — AI-assisted engineering: designing systems that are resilient enough for regulated industries like insurance and healthcare, while staying fast enough to iterate on.</p>

          <p>My path here started in enterprise Java. Early in my career as a Technical Software Consultant and later Senior Software Engineer, I built backend APIs and distributed integrations for healthcare and government clients — the kind of work where correctness and auditability aren't optional. That grounding in disciplined, enterprise-grade engineering carried into seven years at Oracle, where as a Principal Software Engineer I architected enhancements to Oracle's CRM Fusion SaaS modules, products used by Fortune 500 customers and millions of end users. I designed REST APIs and full-stack solutions spanning database, service, and UI layers, and later built an internal automation platform for patch and change deployment across Oracle's CRM, ERP, and HCM cloud products — including ML-backed testing workflows in Python to reduce regression risk.</p>

          <p>Today, at MetLife, that experience translates into owning cloud-native architecture end to end: Java Spring Boot microservices running on Azure Kubernetes Service, API governance through Azure API Management, cross-cloud integration between Azure and AWS, and observability pipelines that catch problems before customers do. I care about the unglamorous parts of the job as much as the interesting ones — query plans, caching strategy, authentication flows, incident response — because that's what actually keeps an enterprise platform reliable.</p>

          <h2>What I specialize in</h2>
          <p>Backend architecture and microservices in Java and Spring Boot; cloud infrastructure across Azure (AKS, APIM, DevOps, Monitor) and AWS (CloudWatch, and AWS-certified); relational data at scale with Oracle Database, SQL/PL-SQL, and Redis caching; and increasingly, applying generative AI and machine learning to development workflows — from AI-driven recommendation features to GitHub Copilot–assisted delivery.</p>

          <h2>How I approach the work</h2>
          <p>I think in systems, not just tickets: how a service will behave under load, how a schema decision today constrains options in a year, how an API contract ripples across ten downstream consumers. I'd rather fix the query plan than add another cache layer to mask it — though I'll use both when the data calls for it. And I like mentoring engineers earlier in their careers, because the code review conversations that stick are usually about the "why," not the "what."</p>
        </div>

        <aside>
          <div class="stat-card card">
            <div class="num">13+ yrs</div>
            <div class="label">Enterprise software engineering</div>
          </div>
          <div class="stat-card card">
            <div class="num">4</div>
            <div class="label">Companies: MetLife, Oracle, NetApp, Oracle</div>
          </div>
          <div class="stat-card card">
            <div class="num">Java · Azure · AWS</div>
            <div class="label">Core technical focus areas</div>
          </div>
          <div class="stat-card card">
            <div class="num">Cary, NC</div>
            <div class="label">Based in the United States, hybrid</div>
          </div>
        </aside>
      </div>
    </section>
"""

write("about.html", page(
    title="About Tanveer Mohammed — Lead Software Engineer",
    description="A professional biography of Tanveer Mohammed: enterprise Java and Spring Boot engineering, cloud architecture across Azure and AWS, and AI-enabled software delivery.",
    canonical="about.html",
    body=about_body,
    active="about.html",
))

write_marker = True  # continuation in pages_2.py
print("pages.py (home + about) complete")
