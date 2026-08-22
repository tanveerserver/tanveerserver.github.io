#!/usr/bin/env python3
"""Second half of the page set: Experience, Skills, Projects, Certifications,
Education, Interests, Contact. Run after (or via) pages.py."""
from build import page, write
from pages import ICO, DESC_DEFAULT

# ---------------------------------------------------------------------------
# EXPERIENCE
# ---------------------------------------------------------------------------
def role(title, company, dates, duration, location, badge, bullets, tech):
    bullets_html = "\n".join(f"          <li>{b}</li>" for b in bullets)
    tags_html = "\n".join(f'          <span class="tag">{t}</span>' for t in tech)
    cur_class = " current" if badge else ""
    badge_html = '<span class="badge-current">Current</span>' if badge else ""
    return f"""
      <div class="timeline-item{cur_class}">
        <span class="timeline-dot"></span>
        <div class="card">
          <h3 class="role-title">{title} {badge_html}</h3>
          <div class="role-meta">
            <span><strong>{company}</strong></span>
            <span>{dates} · {duration}</span>
            <span>{location}</span>
          </div>
          <ul class="role-list">
{bullets_html}
          </ul>
          <div class="tag-row">
{tags_html}
          </div>
        </div>
      </div>"""

experience_body = f"""
    <section class="page-hero container reveal in-view">
      <p class="kicker">Experience</p>
      <h1>Career timeline</h1>
      <p>Thirteen-plus years of enterprise backend engineering and cloud architecture, from healthcare and government systems to Fortune 500 SaaS to insurance claims platforms.</p>
    </section>

    <section class="section reveal">
      <div class="container">
        <div class="timeline">
{role(
    "Lead Software Engineer / Lead Data Engineer", "MetLife", "Feb 2024 – Present", "2 yrs 7 mos", "Cary, North Carolina · Hybrid", True,
    [
        "Serve as lead engineer for MetLife's claims-processing platform, owning backend architecture, cloud infrastructure, and data engineering.",
        "Architected and deployed enterprise claims-processing systems on Azure Kubernetes Service (AKS) using Java Spring Boot microservices, improving system resiliency and enabling horizontal scalability across high-volume insurance workflows.",
        "Strengthened enterprise security posture by implementing OAuth 2.0 authentication flows and API governance through Azure API Management (APIM), reducing unauthorized access exposure across 10+ downstream services.",
        "Optimized SQL queries and Oracle database query plans, improving performance by 80%+ and introducing Redis caching strategies that cut average application response times.",
        "Built end-to-end observability pipelines integrating Azure Monitor and AWS CloudWatch, enabling proactive incident detection and reducing mean time to resolution (MTTR).",
        "Enabled Azure–AWS cross-cloud integration, delivering a resilient multi-cloud architecture that supports enterprise SLAs.",
        "Led modernization efforts for MetLife's Disability and Absence Insurance Tech Maturity platform, improving system efficiency and innovation.",
        "Serves as a key technical expert, providing architectural guidance, implementation strategies, and troubleshooting across Azure DevOps (Boards, Repos, Pipelines) and Databricks.",
    ],
    ["Java", "Spring Boot", "Azure Kubernetes Service", "Azure API Management", "OAuth 2.0", "Oracle Database", "Redis", "Azure Monitor", "AWS CloudWatch", "Azure DevOps", "Databricks", "GitHub Copilot"],
)}
{role(
    "Principal Software Engineer", "Oracle", "Feb 2017 – Dec 2023", "6 yrs 11 mos", "Redwood City, California · Hybrid", False,
    [
        "Architected and delivered high-impact enhancements to Oracle CRM Fusion SaaS modules used by Fortune 500 customers, supporting product lines with millions of end users.",
        "Designed and shipped high-performance REST APIs and full-stack solutions spanning database, services, and UI layers, reducing integration complexity for enterprise clients.",
        "Introduced AI-driven recommendation and analytics features that improved lead prioritization and user decision workflows, measurably increasing platform engagement and sales conversion.",
        "Built an internal automation platform for patch and change deployment across CRM, ERP, and HCM cloud products, implementing predictive deployment logic to eliminate manual release overhead.",
        "Developed ML-backed testing workflows in Python as part of that automation platform, reducing regression risk across releases.",
        "Mentored junior and mid-level engineers and established code review standards and design patterns adopted across the team.",
    ],
    ["Java", "Oracle APEX", "Oracle ADF", "REST APIs", "Python", "Oracle CRM Fusion SaaS"],
)}
{role(
    "Senior Software Engineer", "NetApp", "Jan 2015 – Feb 2017", "2 yrs 2 mos", "North Carolina", False,
    [
        "Enhanced NetApp's enterprise customer support portal, delivering improved service workflows, automated notifications, and scalable features using Java, Oracle ADF, JSP, MySQL, and WebLogic Server.",
        "Delivered high-availability application features with a focus on performance and long-term maintainability across a distributed enterprise environment.",
    ],
    ["Java", "Oracle ADF", "JSP", "MySQL", "WebLogic Server"],
)}
{role(
    "Technical Software Consultant", "Oracle", "Sep 2012 – Jan 2015", "2 yrs 5 mos", "Greater Phoenix Area", False,
    [
        "Delivered enterprise healthcare and government solutions by integrating distributed systems and complex workflows using Java, PL/SQL, Oracle SOA Suite, and ADF BC.",
        "Designed backend APIs and enterprise integrations supporting mission-critical government and healthcare clients across multiple jurisdictions.",
    ],
    ["Java", "PL/SQL", "Oracle SOA Suite", "ADF BC"],
)}
        </div>
      </div>
    </section>
"""

write("experience.html", page(
    title="Experience — Tanveer Mohammed",
    description="Career timeline: Lead Software Engineer at MetLife, Principal Software Engineer at Oracle, Senior Software Engineer at NetApp, and Technical Software Consultant at Oracle.",
    canonical="experience.html",
    body=experience_body,
    active="experience.html",
))

# ---------------------------------------------------------------------------
# SKILLS
# ---------------------------------------------------------------------------
def skill_card(icon, title, items):
    tags = "\n".join(f'        <span class="tag">{i}</span>' for i in items)
    return f"""
      <div class="card skill-card reveal">
        <h3><span class="ic">{icon}</span>{title}</h3>
        <div class="tag-row">
{tags}
        </div>
      </div>"""

skills_body = f"""
    <section class="page-hero container reveal in-view">
      <p class="kicker">Skills &amp; Technologies</p>
      <h1>What I build with</h1>
      <p>Organized by category, drawn directly from my professional experience — not a percentage in sight.</p>
    </section>

    <section class="section reveal">
      <div class="container">
        <div class="grid grid-2">
{skill_card(ICO['code'], "Programming Languages", ["Java", "Python", "SQL", "PL/SQL"])}
{skill_card(ICO['layers'], "Backend &amp; Frameworks", ["Spring Boot", "REST APIs", "Oracle ADF", "JSP", "Oracle SOA Suite"])}
{skill_card(ICO['cloud'], "Cloud Platforms", ["Microsoft Azure", "Azure Kubernetes Service (AKS)", "Azure API Management (APIM)", "Azure DevOps", "Azure Monitor", "Amazon Web Services (AWS)", "AWS CloudWatch"])}
{skill_card(ICO['database'], "Databases &amp; Data", ["Oracle Database", "MySQL", "Redis", "Databricks"])}
{skill_card(ICO['tool'], "DevOps &amp; Tools", ["Docker", "Kubernetes", "CI/CD", "WebLogic Server", "GitHub Copilot", "Azure Repos"])}
{skill_card(ICO['sparkles'], "AI &amp; Modern Development", ["Generative AI", "Artificial Intelligence (AI)", "Machine Learning", "Natural Language Processing (NLP)", "AI-driven recommendation systems", "ML-backed test automation"])}
{skill_card(ICO['shield'], "Architecture &amp; Security", ["Distributed Systems", "OAuth 2.0", "API Governance", "Enterprise SaaS Architecture"])}
{skill_card(ICO['cpu'], "Ways of Working", ["Agile Methodologies", "Technical Mentorship", "Code Review Standards", "Cross-cloud Integration"])}
        </div>
      </div>
    </section>
"""

write("skills.html", page(
    title="Skills & Technologies — Tanveer Mohammed",
    description="Java, Spring Boot, Microsoft Azure, AWS, Oracle Database, Generative AI and the rest of the technology stack Tanveer Mohammed works in day to day.",
    canonical="skills.html",
    body=skills_body,
    active="skills.html",
))

# ---------------------------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------------------------
projects_body = f"""
    <section class="page-hero container reveal in-view">
      <p class="kicker">Selected Professional Work</p>
      <h1>Projects</h1>
      <p>Most of my work sits inside large enterprise platforms rather than standalone public repos. Here's the flagship product line I contributed to, plus portfolio projects I'm planning to build in the open.</p>
    </section>

    <section class="section reveal">
      <div class="container">
        <div class="card project-card reveal">
          <span class="eyebrow"><span class="dot"></span>Oracle · Jan 2017 – Dec 2023</span>
          <h3>Oracle CX (Advertising &amp; Customer Experience)</h3>
          <p>Oracle's connected CX suite goes beyond a traditional CRM — unifying advertising, marketing, sales, commerce, and service data so businesses can build a complete view of every customer interaction. As a Principal Software Engineer on the team, I worked on the Oracle CRM Fusion SaaS modules within this suite, used by Fortune 500 customers and product lines serving millions of end users.</p>
          <dl class="project-meta-grid">
            <div>
              <dt>My Role</dt>
              <dd>Principal Software Engineer — backend architecture, REST APIs, and full-stack enhancements</dd>
            </div>
            <div>
              <dt>Technologies</dt>
              <dd>Java, Oracle ADF, Oracle APEX, REST APIs, Docker</dd>
            </div>
            <div>
              <dt>Contribution</dt>
              <dd>High-performance REST APIs and full-stack solutions spanning database, service, and UI layers; AI-driven recommendation features</dd>
            </div>
          </dl>
          <a class="btn btn-secondary" href="https://www.linkedin.com/in/mohammedtanveer/" target="_blank" rel="noopener noreferrer">See on LinkedIn {ICO['external']}</a>
        </div>
      </div>
    </section>

    <section class="section alt reveal">
      <div class="container">
        <div class="section-head">
          <p class="kicker">On the roadmap</p>
          <h2>Projects I could build next</h2>
          <p>Not yet built — future portfolio work I'm considering to demonstrate hands-on, publicly-shareable engineering alongside my enterprise experience.</p>
        </div>
        <div class="grid grid-3">
          <div class="card future-card reveal">
            <span class="kicker-inline">Future project</span>
            <h3 style="margin:0 0 8px;font-size:1.02rem;">Cloud-native claims workflow demo</h3>
            <p style="margin:0;color:var(--text-muted);font-size:0.92rem;">A Spring Boot + AKS reference microservice showcasing OAuth 2.0, API governance, and observability patterns in the open.</p>
          </div>
          <div class="card future-card reveal">
            <span class="kicker-inline">Future project</span>
            <h3 style="margin:0 0 8px;font-size:1.02rem;">Generative AI code-review assistant</h3>
            <p style="margin:0;color:var(--text-muted);font-size:0.92rem;">An experiment applying LLM-based review to Java pull requests, building on production AI-assisted development experience.</p>
          </div>
          <div class="card future-card reveal">
            <span class="kicker-inline">Future project</span>
            <h3 style="margin:0 0 8px;font-size:1.02rem;">Open-source Azure/AWS cost-observability dashboard</h3>
            <p style="margin:0;color:var(--text-muted);font-size:0.92rem;">A small tool pulling Azure Monitor and AWS CloudWatch metrics into one cross-cloud view.</p>
          </div>
        </div>
      </div>
    </section>
"""

write("projects.html", page(
    title="Projects — Tanveer Mohammed",
    description="Selected professional work from Tanveer Mohammed's career, including Oracle CX (Advertising and Customer Experience), plus planned future portfolio projects.",
    canonical="projects.html",
    body=projects_body,
    active="projects.html",
))

# ---------------------------------------------------------------------------
# CERTIFICATIONS
# ---------------------------------------------------------------------------
def cert_card(name, issuer, date):
    return f"""
      <div class="card cert-card reveal">
        <div class="cert-icon">{ICO['award']}</div>
        <div>
          <h3>{name}</h3>
          <p class="issuer">{issuer}</p>
          <p class="date">{date}</p>
        </div>
      </div>"""

featured_certs = [
    ("AWS Certified Cloud Practitioner", "Amazon Web Services (AWS)", "Issued Oct 2023 · Expires Oct 2026"),
    ("Oracle Cloud Infrastructure 2023 Certified Foundations Associate", "Oracle", "Issued Nov 2023"),
    ("Oracle APEX Foundation", "Oracle", "Issued Nov 2023"),
    ("Oracle WebCenter Portal 11.1.1.8 Certified Implementation Specialist", "Oracle", "Issued Apr 2016"),
    ("Java J2EE Certified", "NIIT Limited", "Issued May 2008"),
    ("Software Architecture: From Developer to Architect", "LinkedIn Learning", "Issued Mar 2014"),
    ("Programming Fundamentals and Data Structures", "LinkedIn Learning", "Issued Oct 2022"),
]

additional_certs = [
    "AWS Certified Cloud Practitioner Prep — Part 4: Billing and Pricing (LinkedIn Learning, Oct 2023)",
    "AWS Certified Cloud Practitioner Prep — Part 3: Core Services (LinkedIn Learning, Oct 2023)",
    "AWS Certified Cloud Practitioner Prep — Part 2: Security (LinkedIn Learning, Oct 2023)",
    "AWS Certified Cloud Practitioner Prep — Part 1: Cloud Concepts (LinkedIn Learning, Oct 2023)",
    "Java Collections In Depth (Java Brains, Aug 2023)",
    "Mastering the 12 Factor App (Java Brains)",
    "Cloud Essentials (Java Brains, Jul 2023)",
    "JavaScript Essential Training (LinkedIn Learning, Dec 2022)",
    "Docker Foundations (LinkedIn Learning, Dec 2022)",
    "Java Arrays (LinkedIn Learning, Oct 2022)",
]

cards_html = "\n".join(cert_card(*c) for c in featured_certs)
additional_html = "\n".join(f"          <li>{c}</li>" for c in additional_certs)

certs_body = f"""
    <section class="page-hero container reveal in-view">
      <p class="kicker">Certifications</p>
      <h1>Licenses &amp; certifications</h1>
      <p>17 credentials on file with LinkedIn in total. The most substantial are featured below; shorter course completions are grouped underneath.</p>
    </section>

    <section class="section reveal">
      <div class="container">
        <div class="grid grid-2">
{cards_html}
        </div>

        <div class="more-toggle">
          <button class="btn btn-secondary" type="button" data-toggle-list="additional-certs" data-label-open="Show 10 additional course completions {'↓'}" data-label-close="Hide additional course completions {'↑'}" aria-expanded="false">
            Show 10 additional course completions ↓
          </button>
          <div class="more-list card" id="additional-certs">
            <ul>
{additional_html}
            </ul>
          </div>
        </div>
      </div>
    </section>
"""

write("certifications.html", page(
    title="Certifications — Tanveer Mohammed",
    description="AWS Certified Cloud Practitioner, Oracle Cloud Infrastructure Certified Foundations Associate, Oracle APEX, and other certifications held by Tanveer Mohammed.",
    canonical="certifications.html",
    body=certs_body,
    active="certifications.html",
))

# ---------------------------------------------------------------------------
# EDUCATION
# ---------------------------------------------------------------------------
education_body = f"""
    <section class="page-hero container reveal in-view">
      <p class="kicker">Education</p>
      <h1>Academic background</h1>
      <p>Computer Science, undergraduate through graduate, at the University of Pune, India.</p>
    </section>

    <section class="section reveal">
      <div class="container">
        <div class="grid grid-2">
          <div class="card edu-card reveal">
            <div class="edu-icon">{ICO['graduation']}</div>
            <div>
              <h3>Modern Education Society's Nowrosjee Wadia College</h3>
              <p class="degree">Master's in Computer Science, Computer Science</p>
              <p class="meta">2005 – 2007 · Grade: First Class</p>
            </div>
          </div>
          <div class="card edu-card reveal">
            <div class="edu-icon">{ICO['graduation']}</div>
            <div>
              <h3>AKI's Poona College of Arts, Science &amp; Commerce</h3>
              <p class="degree">Bachelor's in Computer Science, Computer Science</p>
              <p class="meta">2002 – 2005 · Grade: First Class Distinction</p>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

write("education.html", page(
    title="Education — Tanveer Mohammed",
    description="Tanveer Mohammed's academic background: Master's and Bachelor's degrees in Computer Science.",
    canonical="education.html",
    body=education_body,
    active="education.html",
))

# ---------------------------------------------------------------------------
# INTERESTS
# ---------------------------------------------------------------------------
def interest_card(icon, title, text):
    return f"""
      <div class="card interest-card reveal">
        <div class="ic">{icon}</div>
        <h3>{title}</h3>
        <p>{text}</p>
      </div>"""

interests_body = f"""
    <section class="page-hero container reveal in-view">
      <p class="kicker">Professional Interests</p>
      <h1>What I'm focused on</h1>
      <p>The areas I keep coming back to — in my day job and in what I read, learn, and experiment with.</p>
    </section>

    <section class="section reveal">
      <div class="container">
        <div class="grid grid-3">
{interest_card(ICO['layers'], "Software Architecture", "Designing systems that stay maintainable as scale and team size grow — from microservices boundaries to API contracts.")}
{interest_card(ICO['server'], "Enterprise Software &amp; SaaS", "Building the reliable, auditable systems that Fortune 500 and regulated-industry customers depend on.")}
{interest_card(ICO['cloud'], "Cloud Computing", "Hands-on with Azure and AWS — infrastructure, cross-cloud integration, and the operational discipline that keeps it running.")}
{interest_card(ICO['sparkles'], "Artificial Intelligence &amp; Generative AI", "Applying AI and ML to real engineering workflows — from recommendation systems to AI-assisted development with tools like GitHub Copilot.")}
{interest_card(ICO['code'], "Backend Engineering &amp; APIs", "REST API design, service architecture, and the full-stack layers that connect them to real users.")}
{interest_card(ICO['database'], "Data Engineering", "Query optimization, caching strategy, and pipelines that turn raw data into something a business can act on.")}
{interest_card(ICO['cpu'], "Distributed &amp; Scalable Systems", "Designing for horizontal scale and resiliency across high-volume, high-availability enterprise workflows.")}
{interest_card(ICO['tool'], "DevOps &amp; Reliability", "CI/CD, observability, and the pipelines and monitoring that keep enterprise SLAs intact.")}
        </div>
      </div>
    </section>
"""

write("interests.html", page(
    title="Professional Interests — Tanveer Mohammed",
    description="Tanveer Mohammed's professional interests: software architecture, cloud computing, generative AI, backend engineering, and distributed systems.",
    canonical="interests.html",
    body=interests_body,
    active="interests.html",
))

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
contact_body = f"""
    <section class="page-hero container reveal in-view">
      <p class="kicker">Contact</p>
      <h1>Let's talk</h1>
      <p>Open to hearing from recruiters, hiring managers, technology leaders, and potential collaborators. I read every message.</p>
    </section>

    <section class="section reveal">
      <div class="container contact-grid">
        <div class="card reveal">
          <h2 style="margin:0 0 20px;font-size:1.15rem;">Send a message</h2>
          <form data-contact-form data-mailto="tanveer.server@gmail.com">
            <div class="form-field">
              <label for="name">Name</label>
              <input type="text" id="name" name="name" required autocomplete="name" />
            </div>
            <div class="form-field">
              <label for="email">Your email</label>
              <input type="email" id="email" name="email" required autocomplete="email" />
            </div>
            <div class="form-field">
              <label for="message">Message</label>
              <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button class="btn btn-primary" type="submit">Send Message {ICO['arrow']}</button>
            <p class="form-note">This site is static with no backend — submitting opens a pre-filled email in your mail client addressed to Tanveer. Prefer email directly? Use the address below.</p>
          </form>
        </div>

        <div class="reveal">
          <a class="card contact-link-card" href="mailto:tanveer.server@gmail.com">
            <span class="ic">{ICO['mail']}</span>
            <span>
              <p class="label">Email</p>
              <p class="value">tanveer.server@gmail.com</p>
            </span>
          </a>
          <a class="card contact-link-card" href="https://www.linkedin.com/in/mohammedtanveer/" target="_blank" rel="noopener noreferrer">
            <span class="ic">{ICO['linkedin']}</span>
            <span>
              <p class="label">LinkedIn</p>
              <p class="value">linkedin.com/in/mohammedtanveer</p>
            </span>
          </a>
          <a class="card contact-link-card" href="#" aria-disabled="true" style="opacity:.55;pointer-events:none;">
            <span class="ic">{ICO['map']}</span>
            <span>
              <p class="label">Location</p>
              <p class="value">Cary, North Carolina, United States</p>
            </span>
          </a>
        </div>
      </div>
    </section>
"""

write("contact.html", page(
    title="Contact — Tanveer Mohammed",
    description="Get in touch with Tanveer Mohammed — Lead Software Engineer. Reach out via email, LinkedIn, or the contact form.",
    canonical="contact.html",
    body=contact_body,
    active="contact.html",
))

print("pages_2.py complete — all pages generated.")
