#!/usr/bin/env python3
"""
Rails Path — Part 3: Getting Hired (12 lessons)

Covers:
  Course: Getting Hired
    Section: Preparing for Job Search       (4 lessons)
    Section: Applying and Interviewing      (5 lessons)
    Section: Technical Interview Prep       (3 lessons)

Run:
    python3 seed_rails_part3_getting_hired.py

Preview in browser:
    cd ~/devpath
    python3 -m http.server 8080
    # Then open: http://localhost:8080/paths/full-stack-ruby-on-rails/courses/getting-hired/index.html
"""

import os, subprocess

BASE  = os.path.expanduser("~/devpath")
RAILS = os.path.join(BASE, "paths", "full-stack-ruby-on-rails", "courses")
ROOT  = "../../../../../"
LOGO  = (
    '<svg viewBox="0 0 28 28" fill="none">'
    '<circle cx="14" cy="14" r="13" stroke="currentColor" stroke-width="1.8"/>'
    '<path d="M8 14 L14 7 L20 14 L14 21 Z" fill="currentColor"/>'
    "</svg>"
)


# ── shared helpers ─────────────────────────────────────────────────────────────

def nav():
    return (
        '<nav class="site-nav">'
        f'<a href="{ROOT}index.html" class="nav-logo">{LOGO} DevPath</a>'
        '<ul class="nav-links">'
        f'<li><a href="{ROOT}index.html">Home</a></li>'
        f'<li><a href="{ROOT}foundations/index.html">Foundations</a></li>'
        f'<li><a href="{ROOT}paths/full-stack-javascript/index.html">Full Stack JS</a></li>'
        f'<li><a href="{ROOT}paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a></li>'
        "</ul></nav>"
    )


def footer():
    return (
        '<footer class="site-footer">'
        "<p>DevPath — A free, open, project-based web development curriculum.</p>"
        "</footer>"
    )


def code(s):
    esc = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<div class="code-block"><pre><code>{esc}</code></pre></div>'


def tip(text):
    return (
        '<div class="callout callout-tip">'
        '<span class="callout-icon">💡</span>'
        f"<p>{text}</p>"
        "</div>"
    )


def warn(text):
    return (
        '<div class="callout callout-warn">'
        '<span class="callout-icon">⚠️</span>'
        f"<p>{text}</p>"
        "</div>"
    )


def write(ldir, course_title, all_lessons, sidebar_html, slug,
          title, intro, overview, body, kc, assignments, resources):
    idx = next((i for i, l in enumerate(all_lessons) if l[0] == slug), None)
    p = (all_lessons[idx - 1][1], all_lessons[idx - 1][0] + ".html") if idx and idx > 0 else None
    n = (all_lessons[idx + 1][1], all_lessons[idx + 1][0] + ".html") if idx is not None and idx < len(all_lessons) - 1 else None
    pb = f'<a href="{p[1]}" class="btn btn-blue-outline">&#8592; Previous</a>' if p else "<span></span>"
    nb = f'<a href="{n[1]}" class="btn btn-blue">Next &#8594;</a>' if n else "<span></span>"
    navb = (
        f'<div class="lesson-nav-bar">'
        f'<div class="lesson-nav-bar-group">{pb}</div>'
        f'<div class="lesson-nav-bar-group"><button class="btn btn-green mark-complete-btn">Mark Completed</button></div>'
        f'<div class="lesson-nav-bar-group">{nb}</div></div>'
    )
    bc = (
        f'<nav class="breadcrumb"><a href="{ROOT}index.html">Home</a>'
        f'<span class="breadcrumb-sep">/</span>'
        f'<a href="{ROOT}paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a>'
        f'<span class="breadcrumb-sep">/</span>'
        f'<a href="../index.html">{course_title}</a>'
        f'<span class="breadcrumb-sep">/</span>'
        f'<span class="breadcrumb-current">{title}</span></nav>'
    )
    ov   = "".join(f"<li>{i}</li>" for i in overview)
    kcli = "".join(f'<li><a href="#{k[1]}" data-target="{k[1]}">{k[0]}</a></li>' for k in kc)
    asli = "".join(f"<li>{a}</li>" for a in assignments)
    rsli = "".join(f'<li><a href="{r[1]}" target="_blank" rel="noopener">{r[0]}</a></li>' for r in resources)
    ph = (
        f'<a href="{p[1]}" class="pagination-link prev">'
        f'<span class="pagination-label">&#8592; Previous</span>'
        f'<span class="pagination-title">{p[0]}</span></a>'
        if p else "<span></span>"
    )
    nh = (
        f'<a href="{n[1]}" class="pagination-link next">'
        f'<span class="pagination-label">Next &#8594;</span>'
        f'<span class="pagination-title">{n[0]}</span></a>'
        if n else "<span></span>"
    )
    html = (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "  <meta charset=\"UTF-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        f"  <title>{title} | DevPath</title>\n"
        f"  <link rel=\"stylesheet\" href=\"{ROOT}css/styles.css\">\n"
        "</head>\n<body>\n"
        + nav() + "\n" + navb + "\n"
        + f'<div class="page-header"><div class="page-header-inner">{bc}<h1>{title}</h1></div></div>\n'
        + f'<div class="lesson-layout">{sidebar_html}<main><div class="lesson-body">\n'
        + f'<div class="block-intro"><p>{intro}</p></div>\n'
        + f'<div class="block-overview"><div class="block-overview-label">Lesson Overview</div><ul>{ov}</ul></div>\n'
        + body
        + f'\n<div class="block-kc"><div class="block-kc-label">Knowledge Check</div>'
        + '<p class="kc-note">Click any question to jump to the section that answers it.</p>'
        + f"<ol>{kcli}</ol></div>\n"
        + f'<div class="block-assignments"><div class="block-assignments-label">Assignments</div><ol>{asli}</ol></div>\n'
        + f'<div class="block-resources"><div class="block-resources-label">Additional Resources</div><ul>{rsli}</ul></div>\n'
        + f'</div><div class="lesson-pagination">{ph}{nh}</div></main></div>\n'
        + footer() + "\n"
        + f'<script src="{ROOT}js/main.js"></script>\n</body>\n</html>'
    )
    with open(os.path.join(ldir, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  {slug}")


# ── course index page ──────────────────────────────────────────────────────────

def write_course_index(course_dir, title, description, sections):
    """
    sections = list of (section_title, [(slug, lesson_title, is_project), ...])
    """
    cards_html = ""
    for sec_title, lessons in sections:
        cards_html += f'<div class="index-section"><h2 class="index-section-title">{sec_title}</h2><ul class="index-lesson-list">'
        for slug, ltitle, is_proj in lessons:
            cls = "index-lesson-item" + (" is-project" if is_proj else "")
            cards_html += f'<li class="{cls}"><a href="lessons/{slug}.html">{ltitle}</a></li>'
        cards_html += "</ul></div>"

    html = (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "  <meta charset=\"UTF-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        f"  <title>{title} | DevPath</title>\n"
        f"  <link rel=\"stylesheet\" href=\"{ROOT}css/styles.css\">\n"
        "</head>\n<body>\n"
        + nav() + "\n"
        + f'<div class="page-header"><div class="page-header-inner">'
        + f'<nav class="breadcrumb">'
        + f'<a href="{ROOT}index.html">Home</a><span class="breadcrumb-sep">/</span>'
        + f'<a href="{ROOT}paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a>'
        + f'<span class="breadcrumb-sep">/</span>'
        + f'<span class="breadcrumb-current">{title}</span></nav>'
        + f"<h1>{title}</h1>"
        + f'<p class="course-description">{description}</p>'
        + "</div></div>\n"
        + f'<div class="course-index">{cards_html}</div>\n'
        + footer() + "\n"
        + f'<script src="{ROOT}js/main.js"></script>\n</body>\n</html>'
    )
    path = os.path.join(course_dir, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  course index → {path}")


# ══════════════════════════════════════════════════════════════════════════════
#  GETTING HIRED COURSE
# ══════════════════════════════════════════════════════════════════════════════

def seed_getting_hired():
    course_dir = os.path.join(RAILS, "getting-hired")
    ldir       = os.path.join(course_dir, "lessons")
    os.makedirs(ldir, exist_ok=True)

    ALL = [
        # Preparing for Job Search
        ("preparing-for-job-search",    "Preparing for Your Job Search"),
        ("building-your-portfolio",     "Building Your Portfolio"),
        ("cleaning-up-your-github",     "Cleaning Up Your GitHub"),
        ("building-your-resume",        "Building Your Resume"),
        # Applying and Interviewing
        ("applying-for-jobs",           "Applying for Jobs"),
        ("preparing-for-interviews",    "Preparing for Interviews"),
        ("conducting-the-search",       "Conducting the Job Search"),
        ("handling-offers",             "Handling Job Offers"),
        ("professional-networking",     "Professional Networking"),
        # Technical Interview Prep
        ("ruby-and-rails-interviews",   "Ruby and Rails Interview Questions"),
        ("databases-interviews",        "Database Interview Questions"),
        ("system-design-basics",        "System Design Basics"),
    ]

    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">Getting Hired</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">Preparing for Your Job Search</div>'
        + lnk("preparing-for-job-search",  "Preparing for Your Job Search")
        + lnk("building-your-portfolio",   "Building Your Portfolio")
        + lnk("cleaning-up-your-github",   "Cleaning Up Your GitHub")
        + lnk("building-your-resume",      "Building Your Resume")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Applying and Interviewing</div>'
        + lnk("applying-for-jobs",         "Applying for Jobs")
        + lnk("preparing-for-interviews",  "Preparing for Interviews")
        + lnk("conducting-the-search",     "Conducting the Job Search")
        + lnk("handling-offers",           "Handling Job Offers")
        + lnk("professional-networking",   "Professional Networking")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Technical Interview Prep</div>'
        + lnk("ruby-and-rails-interviews", "Ruby and Rails Interview Questions")
        + lnk("databases-interviews",      "Database Interview Questions")
        + lnk("system-design-basics",      "System Design Basics")
        + "</div></aside>"
    )

    def w(slug, title, intro, overview, body, kc, assignments, resources):
        write(ldir, "Getting Hired", ALL, sidebar, slug, title,
              intro, overview, body, kc, assignments, resources)

    # ── Course index ──────────────────────────────────────
    write_course_index(
        course_dir,
        "Getting Hired",
        "The final stage of the Full Stack Rails path. Learn how to build a compelling portfolio, write a strong resume, conduct a focused job search, ace technical interviews, and negotiate your first offer.",
        [
            ("Preparing for Your Job Search", [
                ("preparing-for-job-search",  "Preparing for Your Job Search", False),
                ("building-your-portfolio",   "Building Your Portfolio",       False),
                ("cleaning-up-your-github",   "Cleaning Up Your GitHub",       False),
                ("building-your-resume",      "Building Your Resume",          False),
            ]),
            ("Applying and Interviewing", [
                ("applying-for-jobs",         "Applying for Jobs",             False),
                ("preparing-for-interviews",  "Preparing for Interviews",      False),
                ("conducting-the-search",     "Conducting the Job Search",     False),
                ("handling-offers",           "Handling Job Offers",           False),
                ("professional-networking",   "Professional Networking",       False),
            ]),
            ("Technical Interview Prep", [
                ("ruby-and-rails-interviews", "Ruby and Rails Interview Questions", False),
                ("databases-interviews",      "Database Interview Questions",       False),
                ("system-design-basics",      "System Design Basics",              False),
            ]),
        ],
    )

    # ══════════════════════════
    #  SECTION 1 — PREPARING
    # ══════════════════════════

    # ── preparing-for-job-search ──────────────────────────
    w("preparing-for-job-search", "Preparing for Your Job Search",
      intro="Before sending a single application, you need a plan. The developers who land jobs fastest are not necessarily the best coders — they are the most prepared. This lesson shows you how to get ready.",
      overview=[
          "Set realistic expectations for timeline and effort.",
          "Understand what employers actually look for in junior developers.",
          "Build a job-search system that keeps you organised.",
          "Know the difference between a warm and a cold application.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="mindset">The Right Mindset</h2>'
          "<p>Job searching is a skill, just like coding. It takes practice, iteration, and resilience. Most junior developers send 50–150 applications before landing their first role. That is normal. Treat the search like a project: track your work, measure results, iterate.</p>"
          + tip("Set a daily quota — e.g. 5 tailored applications per day — rather than aiming for a number of responses. You control inputs, not outcomes.")
          + '<h2 class="lesson-section-title" id="what-employers-want">What Employers Look For</h2>'
          "<p>Hiring managers for junior roles prioritise these signals, roughly in order:</p>"
          "<ol>"
          "<li><strong>Completed projects</strong> — deployed, working apps on your GitHub and portfolio.</li>"
          "<li><strong>Communication</strong> — clear writing, thoughtful answers, professional behaviour.</li>"
          "<li><strong>Fundamentals</strong> — you understand Ruby, Rails, SQL, HTTP, and the web platform.</li>"
          "<li><strong>Culture fit</strong> — curiosity, humility, willingness to learn.</li>"
          "<li><strong>Relevant experience</strong> — bootcamp, degree, or prior work in any technical field.</li>"
          "</ol>"
          + tip("Companies rarely hire on potential alone. Shipped projects are evidence. Build them before you search.")
          + '<h2 class="lesson-section-title" id="tracking">Tracking Your Search</h2>'
          + code("""\
# Spreadsheet columns that work well:
# Date | Company | Role | Source | Status | Contact | Follow-up Date | Notes

# Status values:
# Researching → Applied → Phone Screen → Technical → Onsite → Offer → Rejected

# Tools:
# - Google Sheets / Notion (free, simple)
# - Huntr (job tracker with kanban board — free tier)
# - Trello (kanban board)
""")
          + '<h2 class="lesson-section-title" id="warm-vs-cold">Warm vs Cold Applications</h2>'
          "<p>A <strong>cold application</strong> is submitting your resume through a job board with no prior contact. A <strong>warm application</strong> is applying after some connection — a coffee chat, a referral, a conversation at a meetup. Warm applications are 5–10× more likely to lead to an interview.</p>"
          + warn("Don't spend all your time applying cold on LinkedIn. Spend at least 30% of your search time on networking and warm outreach.")
      ),
      kc=[
          ("What do hiring managers prioritise when evaluating junior candidates?", "what-employers-want"),
          ("What is the difference between a warm and cold application?", "warm-vs-cold"),
          ("Why should you track every application in a spreadsheet?", "tracking"),
      ],
      assignments=[
          "Set up a job-search tracking spreadsheet with the columns above.",
          "Write a 2–3 sentence answer to 'Tell me about yourself' tailored for a junior Rails developer role.",
          "Identify 10 target companies in your area or remote-first companies that use Ruby on Rails.",
      ],
      resources=[
          ("Huntr — Job Application Tracker", "https://huntr.co/"),
          ("Companies using Ruby on Rails (StackShare)", "https://stackshare.io/ruby-on-rails"),
          ("YouTube — How to Get a Developer Job (Traversy Media)", "https://www.youtube.com/watch?v=cYMzFO5bPz8"),
      ])

    # ── building-your-portfolio ───────────────────────────
    w("building-your-portfolio", "Building Your Portfolio",
      intro="Your portfolio is your most important job-search asset. It shows employers what you can actually build. This lesson covers what to include, how to present your projects, and how to build a portfolio site.",
      overview=[
          "Know which projects to feature and how to describe them.",
          "Build a clean, professional portfolio website.",
          "Write compelling project descriptions.",
          "Deploy all portfolio projects so they are live.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="what-to-include">What to Include</h2>'
          "<p>Quality beats quantity. Two or three polished, deployed projects are worth more than ten unfinished ones. A strong junior portfolio includes:</p>"
          "<ul>"
          "<li><strong>A capstone full-stack Rails app</strong> — e.g. your Odin-Book or a personal project. Deployed, with auth, CRUD, associations, and a real feature set.</li>"
          "<li><strong>A Ruby project</strong> — shows you know the language underneath the framework. Chess, Hangman, Connect Four are all fine.</li>"
          "<li><strong>An API integration or external service</strong> — shows you can work with the real web. A weather app, a Spotify wrapper, a GitHub stats page.</li>"
          "</ul>"
          + warn("Never feature a tutorial project as your own work. Employers recognise them. Only show projects you designed and built yourself.")
          + '<h2 class="lesson-section-title" id="project-descriptions">Writing Project Descriptions</h2>'
          "<p>Each project in your portfolio needs: a live demo link, a GitHub link, a 2–3 sentence description, and a tech stack list. Use the <strong>problem → solution → result</strong> format:</p>"
          + code("""\
# Weak description:
"A Rails app with users and posts."

# Strong description:
"OdinBook — A social network built with Ruby on Rails, PostgreSQL, and Tailwind CSS.
Users can register, post updates, attach photos via Active Storage, send friend
requests, and view a live news feed of friends' activity. Deployed on Fly.io with
GitHub Actions CI."

# Tech stack list: Ruby on Rails · PostgreSQL · Tailwind CSS · Active Storage · Fly.io
""")
          + '<h2 class="lesson-section-title" id="portfolio-site">Building Your Portfolio Site</h2>'
          + code("""\
# Options (simplest to most custom):

# 1. GitHub Pages + Jekyll (free, fast, no backend needed)
gem install jekyll bundler
jekyll new my-portfolio
cd my-portfolio
bundle exec jekyll serve
# Deploy: push to gh-pages branch or use GitHub Pages settings

# 2. Simple HTML/CSS site on Netlify (free)
# Build index.html, projects.html, about.html
# Push to GitHub → connect to Netlify → auto-deploys on push

# 3. Rails portfolio app on Fly.io
rails new portfolio --css tailwind
# Add projects, blog, contact form
""")
          + tip("Your portfolio site itself is a project. Keep it simple and professional. A clean one-page site beats a flashy broken one every time.")
      ),
      kc=[
          ("What three types of projects make a strong junior portfolio?", "what-to-include"),
          ("What format should project descriptions follow?", "project-descriptions"),
          ("What must every portfolio project have?", "project-descriptions"),
      ],
      assignments=[
          "Deploy all your Rails projects (Odin-Book, Blog App, Flight Booker) to Fly.io or Render.",
          "Write a strong project description for each using the problem → solution → result format.",
          "Build or update your portfolio site to feature your three best projects.",
      ],
      resources=[
          ("GitHub Pages Documentation", "https://pages.github.com/"),
          ("Netlify — Deploy in Seconds", "https://www.netlify.com/"),
          ("Fly.io — Deploy Rails Apps", "https://fly.io/docs/rails/getting-started/"),
          ("YouTube — Build a Portfolio Site (Kevin Powell)", "https://www.youtube.com/watch?v=0YFrGy_mzjY"),
      ])

    # ── cleaning-up-your-github ───────────────────────────
    w("cleaning-up-your-github", "Cleaning Up Your GitHub",
      intro="Employers look at your GitHub profile the moment they see your resume. A professional, well-maintained GitHub signals that you take your craft seriously. This lesson walks through every step.",
      overview=[
          "Set up a professional GitHub profile.",
          "Write good READMEs for every project.",
          "Maintain a consistent commit history.",
          "Pin your best repositories.",
          "Clean up or hide unfinished/tutorial projects.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="profile">Profile Setup</h2>'
          "<p>Your GitHub profile is a landing page. Fill out every field:</p>"
          "<ul>"
          "<li><strong>Profile photo</strong> — a clear, professional headshot (not a logo or avatar).</li>"
          "<li><strong>Name</strong> — your real full name.</li>"
          "<li><strong>Bio</strong> — one sentence: \"Full-stack Rails developer. Open to work.\"</li>"
          "<li><strong>Location</strong> — city, country (helps recruiters find you).</li>"
          "<li><strong>Website</strong> — link to your portfolio site.</li>"
          "<li><strong>LinkedIn</strong> — link in social section.</li>"
          "</ul>"
          + '<h2 class="lesson-section-title" id="profile-readme">Profile README</h2>'
          + code("""\
# Create a special repo: username/username (e.g. alice/alice)
# Add a README.md — it appears on your GitHub profile page

# Example README.md:
## Hi, I'm Alice 👋

Full-stack developer specialising in **Ruby on Rails** and **PostgreSQL**.
I love building clean, well-tested web applications.

### 🛠 Tech Stack
- Ruby · Rails · RSpec
- PostgreSQL · Active Record
- Tailwind CSS · Hotwire
- Git · Docker · Fly.io

### 🚀 Featured Projects
| Project | Description | Stack |
|---------|-------------|-------|
| [OdinBook](https://github.com/alice/odinbook) | Social network with friend requests & news feed | Rails · PostgreSQL · Tailwind |
| [Flight Booker](https://github.com/alice/flight-booker) | Multi-step booking form | Rails · Active Record |

### 📫 Contact
[alice@example.com](mailto:alice@example.com) · [Portfolio](https://alice.dev) · [LinkedIn](https://linkedin.com/in/alice)
""")
          + '<h2 class="lesson-section-title" id="readmes">Project READMEs</h2>'
          "<p>Every pinned repository needs a README with these sections:</p>"
          + code("""\
# Project Name

Brief description (2–3 sentences).

## Live Demo
[https://myapp.fly.dev](https://myapp.fly.dev)

## Features
- User authentication with Devise
- Real-time notifications via Action Cable
- Image uploads via Active Storage
- Full test suite (RSpec, 95% coverage)

## Tech Stack
- Ruby 3.3 / Rails 7.1
- PostgreSQL
- Tailwind CSS
- Fly.io (hosting)

## Setup
```bash
git clone https://github.com/you/project
cd project
bundle install
rails db:setup
bin/dev
```

## Screenshots
[Add 1–2 screenshots of the running app]
""")
          + tip("The README is read by humans, not machines. Write it as if you're explaining the project to a fellow developer who has never seen it.")
      ),
      kc=[
          ("What six fields should a professional GitHub profile have?", "profile"),
          ("What sections belong in every project README?", "readmes"),
          ("What is a GitHub profile README and how do you create one?", "profile-readme"),
      ],
      assignments=[
          "Complete every field on your GitHub profile.",
          "Create a profile README using the template above.",
          "Write a full README for each of your three portfolio projects.",
          "Pin your three best repositories and hide or archive tutorial/incomplete repos.",
      ],
      resources=[
          ("GitHub Docs — Profile README", "https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme"),
          ("Awesome GitHub Profile READMEs", "https://github.com/abhisheknaiidu/awesome-github-profile-readme"),
          ("Make a README", "https://www.makeareadme.com/"),
      ])

    # ── building-your-resume ──────────────────────────────
    w("building-your-resume", "Building Your Resume",
      intro="A developer resume has a different format than a general resume. It must pass an Applicant Tracking System (ATS), get a recruiter's attention in 6 seconds, and show a hiring manager that you can do the job.",
      overview=[
          "Understand ATS and how to optimise for it.",
          "Know the correct sections and order for a developer resume.",
          "Write strong bullet points using the STAR format.",
          "Tailor your resume to each job description.",
          "Avoid the most common resume mistakes.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="structure">Resume Structure</h2>'
          "<p>Use this order and nothing else for a junior developer resume:</p>"
          "<ol>"
          "<li><strong>Header</strong> — name, email, phone, location (city/country), GitHub, LinkedIn, portfolio URL.</li>"
          "<li><strong>Skills</strong> — keep it tight: Languages, Frameworks, Databases, Tools. No skill bars or ratings.</li>"
          "<li><strong>Projects</strong> — your 2–3 best projects with bullet points. Include the live URL.</li>"
          "<li><strong>Education</strong> — degree or bootcamp. Include graduation year.</li>"
          "<li><strong>Experience</strong> — if you have prior work experience (any industry), list it briefly.</li>"
          "</ol>"
          + warn("Do not include: a photo, an objective statement, references, your age, marital status, or a skill bar graphic. These hurt you.")
          + '<h2 class="lesson-section-title" id="bullet-points">Writing Strong Bullet Points</h2>'
          + code("""\
# Weak: "Built a Rails app"
# Strong: "Built a Rails 7 social network (OdinBook) with Devise auth, Active Storage
#          photo uploads, and a PostgreSQL news feed query optimised with includes
#          to eliminate N+1 queries — deployed on Fly.io."

# Formula: [Action verb] + [what you built/did] + [tech used] + [measurable result or scale]

# Good action verbs for developers:
# Built · Architected · Implemented · Designed · Optimised · Reduced · Deployed
# Integrated · Migrated · Refactored · Tested · Automated · Shipped
""")
          + '<h2 class="lesson-section-title" id="ats">ATS Optimisation</h2>'
          "<p>Most companies use Applicant Tracking Systems to filter resumes before a human reads them. To pass:</p>"
          "<ul>"
          "<li>Use a <strong>single-column, plain layout</strong> — no tables, columns, or text boxes.</li>"
          "<li>Save as <strong>PDF</strong> (unless the job posting asks for .docx).</li>"
          "<li>Use the <strong>exact keywords</strong> from the job description (e.g. if it says 'RSpec', write 'RSpec', not 'testing').</li>"
          "<li>Avoid headers/footers, graphics, and unusual fonts.</li>"
          "</ul>"
          + tip("Use jobscan.co to compare your resume against a job description and see your ATS match score before applying.")
      ),
      kc=[
          ("What is the correct order of sections on a junior developer resume?", "structure"),
          ("What formula should bullet points follow?", "bullet-points"),
          ("What four things help a resume pass an ATS?", "ats"),
      ],
      assignments=[
          "Build your resume using the structure above. Use a clean, ATS-friendly template from resume.io or rxresu.me.",
          "Write bullet points for each of your three portfolio projects using the action verb formula.",
          "Run your resume through jobscan.co against a real job posting and fix any gaps.",
      ],
      resources=[
          ("RxResume — Free Resume Builder", "https://rxresu.me/"),
          ("Jobscan — ATS Resume Checker", "https://www.jobscan.co/"),
          ("YouTube — Developer Resume Tips (TechLead)", "https://www.youtube.com/watch?v=9J3xNDcxHGc"),
      ])

    # ══════════════════════════
    #  SECTION 2 — APPLYING
    # ══════════════════════════

    # ── applying-for-jobs ─────────────────────────────────
    w("applying-for-jobs", "Applying for Jobs",
      intro="Knowing where to look, how to filter good opportunities, and how to write a cover letter that gets read separates developers who get interviews from those who don't.",
      overview=[
          "Find Rails developer jobs on the right platforms.",
          "Filter job postings to find genuinely junior-friendly roles.",
          "Write a cover letter that gets read.",
          "Customise your application for each company.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="where-to-look">Where to Look</h2>'
          "<p>Not all job boards are equal. Start with these:</p>"
          "<ul>"
          "<li><strong>LinkedIn Jobs</strong> — set alerts for 'Ruby on Rails developer junior'. Apply within 24h of posting for best results.</li>"
          "<li><strong>We Work Remotely</strong> — remote-first. Rails roles appear regularly.</li>"
          "<li><strong>Ruby on Rails Jobs</strong> (railsjobs.dev) — niche board, high signal.</li>"
          "<li><strong>Hacker News Who's Hiring</strong> — monthly thread, first of the month. Search for 'Ruby' or 'Rails'.</li>"
          "<li><strong>AngelList / Wellfound</strong> — startups. Many use Rails. More flexible on experience.</li>"
          "<li><strong>Company websites directly</strong> — if you admire a company, go to their careers page. Skip the middleman.</li>"
          "</ul>"
          + '<h2 class="lesson-section-title" id="filtering">Filtering Job Postings</h2>'
          + code("""\
# Green flags — genuinely junior-friendly:
# ✓ "0–2 years experience" or "entry-level"
# ✓ Mentions mentorship, onboarding, or learning budget
# ✓ Small engineering team (2–15 people)
# ✓ The job title says "Junior" or "Associate"
# ✓ Uses Rails / Ruby in the primary stack

# Red flags — apply with caution:
# ✗ "3–5 years required" for a junior title
# ✗ Lists 10+ required technologies
# ✗ "Fast-paced startup" with no mention of support
# ✗ Equity-only or very low salary
""")
          + '<h2 class="lesson-section-title" id="cover-letter">Cover Letters</h2>'
          "<p>Most cover letters are ignored because they are generic. A tailored, specific letter stands out. Keep it to three short paragraphs:</p>"
          + code("""\
# Paragraph 1 — the hook: why THIS company?
"I've been following Basecamp's approach to calm software development for two years.
Your writing on Shape Up changed how I think about project planning, and I'd love
to contribute to a team that ships thoughtfully."

# Paragraph 2 — your strongest evidence:
"I recently built OdinBook, a social network in Rails 7 with friend requests,
a PostgreSQL news feed, and Active Storage photo uploads — deployed on Fly.io.
I'm comfortable with RSpec, N+1 optimisation, and service objects."

# Paragraph 3 — the ask:
"I'd welcome the chance to talk about the junior Rails role. My GitHub is
github.com/you and my portfolio is yourdomain.com."
""")
          + tip("Mention something specific about the company that is not on the careers page — a blog post, an open source project, a product decision. It shows you actually care.")
      ),
      kc=[
          ("Name three job boards that regularly post Rails developer roles.", "where-to-look"),
          ("What are three green flags that a role is genuinely junior-friendly?", "filtering"),
          ("What are the three paragraphs of an effective cover letter?", "cover-letter"),
      ],
      assignments=[
          "Set up job alerts on LinkedIn and We Work Remotely for 'Ruby on Rails junior'.",
          "Write a tailored cover letter for a real job posting you find.",
          "Apply to 5 roles this week using the cover letter format above.",
      ],
      resources=[
          ("We Work Remotely — Rails Jobs", "https://weworkremotely.com/"),
          ("Rails Jobs Board", "https://railsjobs.dev/"),
          ("HN Who's Hiring Thread", "https://news.ycombinator.com/"),
          ("Wellfound (AngelList)", "https://wellfound.com/"),
      ])

    # ── preparing-for-interviews ──────────────────────────
    w("preparing-for-interviews", "Preparing for Interviews",
      intro="Developer interviews have a predictable structure. Knowing what to expect and practising each stage removes fear and lets you perform at your best.",
      overview=[
          "Understand the typical Rails developer interview pipeline.",
          "Prepare for behavioural questions with the STAR method.",
          "Practise talking through your projects confidently.",
          "Know what to research before every interview.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="pipeline">The Interview Pipeline</h2>'
          "<p>A typical junior Rails developer interview has these stages:</p>"
          "<ol>"
          "<li><strong>Recruiter screen (30 min)</strong> — culture fit, salary expectations, timeline, logistics. Be enthusiastic and professional.</li>"
          "<li><strong>Technical phone screen (45–60 min)</strong> — basic Ruby/Rails questions, maybe a small live-coding problem. Know your fundamentals cold.</li>"
          "<li><strong>Take-home assignment (2–5 hours)</strong> — build a small Rails feature or fix bugs in a codebase. Write tests. Clean code. Good README.</li>"
          "<li><strong>Technical interview / pairing session (60–90 min)</strong> — walk through your take-home, answer deeper questions, maybe pair-program.</li>"
          "<li><strong>Final interview (45–60 min)</strong> — meet the team. Mostly behavioural and culture. Ask good questions.</li>"
          "</ol>"
          + '<h2 class="lesson-section-title" id="star">Behavioural Questions — STAR Method</h2>'
          + code("""\
# STAR = Situation, Task, Action, Result
# Use for: "Tell me about a time when..." questions

# Question: "Tell me about a time you got stuck on a technical problem."

# Weak answer: "I had a bug once and fixed it after a while."

# STAR answer:
# Situation: "While building my Blog App, my polymorphic comment
#             association was silently failing on save."
# Task:      "I needed to debug it without breaking existing functionality."
# Action:    "I used the Rails console to inspect the error object, found a
#             missing commentable_type column in my migration, added it,
#             and wrote an RSpec test to prevent regression."
# Result:    "Comments saved correctly and my test suite caught two similar
#             issues in the next feature I added."
""")
          + '<h2 class="lesson-section-title" id="pre-interview">Before Every Interview</h2>'
          + code("""\
# Research checklist (do this the day before):
# 1. Read the company's About page and recent blog posts
# 2. Use their product if possible — know what it does and who it's for
# 3. Find the engineering team on LinkedIn — know 1–2 engineers' backgrounds
# 4. Read their engineering blog (many companies have one)
# 5. Prepare 3–5 thoughtful questions to ask (see below)

# Good questions to ask interviewers:
# - "What does a typical first week look like for a new junior developer?"
# - "How does code review work on your team?"
# - "What is the biggest technical challenge the team is working on?"
# - "How do you handle on-call and production incidents?"
# - "What does career progression look like from junior to mid-level?"
""")
          + tip("The best question you can ask: 'What would make someone wildly successful in this role in their first 90 days?' It shows you're thinking about impact, not just getting hired.")
      ),
      kc=[
          ("What are the five stages of a typical Rails developer interview pipeline?", "pipeline"),
          ("What does STAR stand for and when do you use it?", "star"),
          ("What five things should you research before every interview?", "pre-interview"),
      ],
      assignments=[
          "Write STAR answers for these five questions: a time you debugged a hard problem; a time you learned something quickly; a time you disagreed with a technical decision; your proudest project; a time you failed.",
          "Record yourself answering 'Tell me about yourself' and watch it back. Aim for 90 seconds, clear and confident.",
      ],
      resources=[
          ("YouTube — STAR Interview Method (Jeff H Sipe)", "https://www.youtube.com/watch?v=WSbN-0swDgM"),
          ("Glassdoor — Rails Interview Questions", "https://www.glassdoor.com/Interview/ruby-on-rails-interview-questions-SRCH_KT0,13.htm"),
      ])

    # ── conducting-the-search ─────────────────────────────
    w("conducting-the-search", "Conducting the Job Search",
      intro="A structured, consistent job search gets results faster than random bursts of effort. This lesson covers the weekly system that keeps you moving without burning out.",
      overview=[
          "Build a sustainable weekly job-search routine.",
          "Balance applying, networking, and skill-building.",
          "Follow up professionally without being annoying.",
          "Deal with rejection and maintain momentum.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="weekly-system">The Weekly System</h2>'
          + code("""\
# Recommended weekly schedule during active job search:

# Monday
# - Review job boards, identify 5 new target roles
# - Send 2–3 tailored applications with cover letters

# Tuesday
# - Send 2–3 more applications
# - 1 hour of technical interview practice (see next lessons)

# Wednesday
# - Follow up on applications sent 1 week ago (one polite email)
# - Coffee chat or informational interview if scheduled
# - 1 hour coding practice

# Thursday
# - 2–3 more applications
# - Update tracking spreadsheet

# Friday
# - Review the week: what worked, what didn't
# - Reach out to 1 new person on LinkedIn or at a meetup
# - Improve one portfolio project or fix a README

# Total: 10–15 applications/week, 3–5 hours networking, 2–3 hours coding
""")
          + '<h2 class="lesson-section-title" id="follow-up">Following Up</h2>'
          + code("""\
# Follow-up email template (send 5–7 business days after applying):

Subject: Following up — Junior Rails Developer Application

Hi [Name / Hiring Team],

I wanted to follow up on my application for the Junior Rails Developer
role I submitted on [date]. I remain very interested in [Company] and
would love the chance to discuss how my experience with Rails, PostgreSQL,
and RSpec could contribute to your team.

Please let me know if you need any additional information.

Best,
[Your Name]
[GitHub] [Portfolio]
""")
          + '<h2 class="lesson-section-title" id="rejection">Handling Rejection</h2>'
          "<p>Rejection is not a measure of your worth — it is a measurement of fit, timing, and competition. Every rejection has a lesson:</p>"
          "<ul>"
          "<li>If rejected before an interview → improve your resume and portfolio.</li>"
          "<li>If rejected after a phone screen → practise verbal communication and fundamentals.</li>"
          "<li>If rejected after a take-home → ask for feedback; review your code quality and test coverage.</li>"
          "<li>If rejected after a final → it was likely culture or internal candidate. Keep going.</li>"
          "</ul>"
          + tip("Send a brief, gracious rejection response asking for feedback. Most companies won't reply, but some will — and that feedback is gold.")
      ),
      kc=[
          ("What does a productive job-search week look like?", "weekly-system"),
          ("When and how should you follow up on an application?", "follow-up"),
          ("What should you do differently after each type of rejection?", "rejection"),
      ],
      assignments=[
          "Set up your weekly job-search calendar with dedicated blocks for applying, networking, and practice.",
          "Write a follow-up email template and save it so you can send it quickly.",
      ],
      resources=[
          ("YouTube — How to Follow Up After a Job Application", "https://www.youtube.com/watch?v=sEhNV0PJNMQ"),
          ("Dev.to — Junior Dev Job Search Guide", "https://dev.to/"),
      ])

    # ── handling-offers ───────────────────────────────────
    w("handling-offers", "Handling Job Offers",
      intro="Getting an offer is exciting — but how you respond matters. This lesson covers evaluating offers, negotiating salary, and avoiding common mistakes that cost developers thousands of dollars.",
      overview=[
          "Evaluate an offer beyond base salary.",
          "Negotiate confidently and professionally.",
          "Understand equity, benefits, and total compensation.",
          "Handle multiple offers at the same time.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="evaluating">Evaluating an Offer</h2>'
          "<p>Total compensation is more than salary. Evaluate all of these:</p>"
          + code("""\
# Total compensation checklist:
# Base salary         — annual gross
# Equity              — stock options or RSUs (startups especially)
# Health insurance    — who pays, what's covered
# Paid time off       — days per year, rollover policy
# Remote policy       — fully remote, hybrid, or in-office
# Learning budget     — conferences, books, courses (many companies offer $500–$2000/yr)
# Equipment budget    — MacBook, monitors, home office stipend
# Signing bonus       — one-time, sometimes negotiable
# Bonus structure     — performance, company, discretionary
# Pension / 401k      — employer match percentage
# Parental leave      — weeks, paid/unpaid
# Career progression  — how long to mid-level, review process
""")
          + '<h2 class="lesson-section-title" id="negotiating">Negotiating</h2>'
          + code("""\
# Rule 1: Always negotiate. Always. The worst they can say is no.
# Rule 2: Never give the first number. Let them anchor.
# Rule 3: Negotiate via email — gives you time to think.

# When asked "What are your salary expectations?":
"I'm still researching the full scope of the role, but based on my
research I'm targeting the £40,000–£50,000 range. Is that in line
with the band for this position?"

# When you receive an offer:
"Thank you so much — I'm really excited about this opportunity.
Could I have until [3–5 business days] to review the details?
I want to give it the consideration it deserves."

# Negotiating the offer:
"I'm very excited about [Company] and the role. Based on my research
and the projects I've shipped, I was hoping we could get to £48,000.
Is there flexibility there?"

# If they can't move on salary, negotiate other terms:
"I understand on salary. Would you be able to add an extra 5 days PTO
or a learning budget?"
""")
          + tip("Research market rates before any negotiation. Use levels.fyi, Glassdoor, LinkedIn Salary, and local developer salary surveys. Know your number before you get on the call.")
      ),
      kc=[
          ("What components make up total compensation beyond base salary?", "evaluating"),
          ("What is the correct response when asked for your salary expectations?", "negotiating"),
          ("If a company can't move on salary, what else can you negotiate?", "negotiating"),
      ],
      assignments=[
          "Research junior Rails developer salaries in your target location using Glassdoor and LinkedIn Salary.",
          "Write out your negotiation script so you can say it confidently out loud.",
      ],
      resources=[
          ("Levels.fyi — Tech Salaries", "https://www.levels.fyi/"),
          ("Patrick McKenzie — Salary Negotiation", "https://www.kalzumeus.com/2012/01/23/salary-negotiation/"),
          ("YouTube — How to Negotiate Salary (Cassidy Williams)", "https://www.youtube.com/watch?v=u9BoG1n1948"),
      ])

    # ── professional-networking ───────────────────────────
    w("professional-networking", "Professional Networking",
      intro="The hidden job market — roles filled through referrals before ever being posted — accounts for 70–80% of hires. Networking is not schmoozing. It is building genuine professional relationships over time.",
      overview=[
          "Build a professional LinkedIn profile.",
          "Do informational interviews effectively.",
          "Engage with the Rails community online and in person.",
          "Ask for referrals naturally and professionally.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="linkedin">LinkedIn Profile</h2>'
          "<p>Your LinkedIn profile should mirror and supplement your resume. Key fields:</p>"
          "<ul>"
          "<li><strong>Headline</strong> — 'Junior Rails Developer | Ruby · PostgreSQL · Tailwind' (not 'Looking for work').</li>"
          "<li><strong>About section</strong> — 3–4 sentences: who you are, what you build, what you're looking for.</li>"
          "<li><strong>Featured section</strong> — pin your portfolio site and GitHub.</li>"
          "<li><strong>Open to Work</strong> — enable this; set it to visible to recruiters only if you're employed.</li>"
          "<li><strong>Skills</strong> — add Ruby, Rails, PostgreSQL, RSpec, Git. Get endorsements.</li>"
          "</ul>"
          + '<h2 class="lesson-section-title" id="informational-interviews">Informational Interviews</h2>'
          + code("""\
# Informational interview = a 20-min coffee chat to learn, not to ask for a job.
# How to request one on LinkedIn:

"Hi [Name], I've been following your work at [Company] and really admire
[specific thing — their blog post, open source project, product decision].
I'm a junior Rails developer finishing up my portfolio and would love
to hear about your experience transitioning into the role.
Would you be open to a 20-minute chat sometime in the next few weeks?
Totally understand if you're too busy!"

# During the chat, ask:
# - "How did you get your first developer job?"
# - "What do you wish you'd known as a junior?"
# - "What does your team look for when hiring juniors?"
# - "Is there anyone else you'd recommend I talk to?"

# After the chat:
# - Send a thank-you email within 24 hours
# - Connect on LinkedIn
# - Follow up in 2–3 months with an update on your progress
""")
          + '<h2 class="lesson-section-title" id="community">Rails Community</h2>'
          + code("""\
# Online:
# - Ruby on Rails Slack (rubyonrails.link/slack) — active community
# - Ruby on Rails Forum (discuss.rubyonrails.org)
# - Dev.to Ruby tag
# - Reddit r/rails, r/ruby

# Meetups and Conferences:
# - Local Ruby/Rails meetups (meetup.com → search 'ruby' in your city)
# - RailsConf (annual, North America)
# - RubyConf (annual, North America)
# - Brighton Ruby, EuRuKo (Europe)

# How to contribute:
# - Answer questions in the Rails Slack
# - Write a blog post about something you learned
# - Submit a small fix to an open source Rails project
# - Give a lightning talk at a local meetup
""")
          + tip("One warm referral is worth fifty cold applications. When you finish an informational interview, it is completely appropriate to say: 'If you ever hear of a junior Rails opening, I'd really appreciate you thinking of me.'")
      ),
      kc=[
          ("What should your LinkedIn headline say?", "linkedin"),
          ("What is an informational interview and what should you ask?", "informational-interviews"),
          ("Where can you engage with the Rails community online?", "community"),
      ],
      assignments=[
          "Optimise your LinkedIn profile using the checklist above.",
          "Send three informational interview requests to Rails developers on LinkedIn this week.",
          "Join the Ruby on Rails Slack and introduce yourself in the #beginners channel.",
      ],
      resources=[
          ("Ruby on Rails Slack", "https://rubyonrails.link/slack"),
          ("Rails Forum", "https://discuss.rubyonrails.org/"),
          ("YouTube — LinkedIn for Developers (Joshua Fluke)", "https://www.youtube.com/watch?v=SG5Sb5WTV_g"),
      ])

    # ══════════════════════════════════
    #  SECTION 3 — TECHNICAL PREP
    # ══════════════════════════════════

    # ── ruby-and-rails-interviews ─────────────────────────
    w("ruby-and-rails-interviews", "Ruby and Rails Interview Questions",
      intro="Technical interviews for Rails roles follow predictable patterns. This lesson gives you the most common questions, model answers, and the concepts behind them so you can answer confidently.",
      overview=[
          "Answer common Ruby language questions.",
          "Answer common Rails framework questions.",
          "Walk through your projects confidently.",
          "Understand what depth of answer is expected at the junior level.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="ruby-questions">Common Ruby Questions</h2>'
          + code("""\
# Q: What is the difference between a Symbol and a String?
# A: Symbols are immutable, unique identifiers stored once in memory.
#    Strings are mutable objects; each occurrence is a new object.
#    Use symbols for hash keys and identifiers; strings for text data.
:name.object_id == :name.object_id  # true — same object
"name".object_id == "name".object_id  # false — different objects

# Q: What are blocks, Procs, and Lambdas? How do they differ?
# A: All three are callable pieces of code.
#    Blocks — anonymous, passed to methods with do..end or {}.
#    Procs   — blocks saved as objects. Lenient on argument count.
#              return exits the enclosing method.
#    Lambdas — strict Procs. Check argument count.
#              return exits only the lambda itself.

# Q: What does attr_accessor do?
# A: Creates getter and setter instance methods for the named attribute.
class Person
  attr_accessor :name  # equivalent to:
  def name; @name; end
  def name=(val); @name = val; end
end

# Q: Explain Ruby's object model.
# A: Everything in Ruby is an object — including classes and nil.
#    Every object has a class. Every class has a superclass.
#    Methods are looked up through the ancestor chain:
#    Object → Kernel → BasicObject.
#    Modules are inserted into the ancestor chain with include/prepend.

# Q: What is the difference between include and extend?
# A: include adds module methods as instance methods.
#    extend adds module methods as class methods.
""")
          + '<h2 class="lesson-section-title" id="rails-questions">Common Rails Questions</h2>'
          + code("""\
# Q: Explain the Rails request-response cycle.
# A: 1. Browser sends HTTP request to server.
#    2. Router (config/routes.rb) matches URL to controller#action.
#    3. Controller action runs: fetches data from models, assigns @vars.
#    4. Rails renders the matching view template (ERB).
#    5. HTML response sent back to browser.

# Q: What is Active Record and what pattern does it implement?
# A: Active Record is Rails' ORM. It implements the Active Record pattern:
#    each database table maps to a Ruby class; each row is an instance.
#    It provides query, validation, association, and callback methods.

# Q: What is the N+1 query problem and how do you fix it?
# A: N+1 occurs when you load N records then run 1 additional query
#    for each — e.g. loading posts then calling post.user for each.
#    Fix: Post.includes(:user) — eager-loads all users in one query.

# Q: What is the difference between render and redirect_to?
# A: render — renders a view template without a new HTTP request.
#             Used when you want to re-show a form (e.g. after validation failure).
#    redirect_to — sends a 302 HTTP response, browser makes a new request.
#                  Used after a successful action (Post/Redirect/Get pattern).

# Q: What are strong parameters and why do we need them?
# A: Strong parameters (params.require().permit()) protect against
#    mass assignment attacks where a malicious user sends extra fields
#    (e.g. admin: true) that get written to the database.

# Q: What is a Rails migration and why is it important?
# A: Migrations are version-controlled database schema changes.
#    They let the whole team apply the same schema changes in order,
#    making the database state reproducible from git history.

# Q: What is a scope in Active Record?
# A: A reusable query fragment defined on the model:
scope :published, -> { where(published: true).order(created_at: :desc) }
# Called as: Post.published — chainable with other queries.

# Q: Explain the difference between has_many :through and has_and_belongs_to_many.
# A: Both model many-to-many. has_many :through uses an explicit join model
#    (PostTag) which can have its own attributes and validations.
#    HABTM uses an automatic join table with no model — simpler but limited.
""")
          + '<h2 class="lesson-section-title" id="project-walkthrough">Walking Through Your Projects</h2>'
          + code("""\
# Interviewers will say: "Walk me through one of your projects."
# Structure your answer:

# 1. What problem does it solve / what does it do? (1–2 sentences)
# 2. What is the tech stack and why did you choose it? (1 sentence)
# 3. What was the hardest technical challenge? (2–3 sentences)
# 4. What would you do differently if you rebuilt it? (1–2 sentences)

# Example for OdinBook:
# "OdinBook is a social network built with Rails 7, PostgreSQL, and Tailwind.
# The hardest part was modelling friend requests — a user can send, receive,
# accept, or reject a request, and I needed both directions of the friendship
# to be queryable efficiently. I used a self-referential has_many :through
# with a separate Friendship model that stores requester, receiver, and status.
# If I rebuilt it, I'd add proper pagination from the start — my news feed
# query gets expensive fast without it."
""")
      ),
      kc=[
          ("What is the difference between a Symbol and a String in Ruby?", "ruby-questions"),
          ("Explain the Rails request-response cycle in order.", "rails-questions"),
          ("What is the difference between render and redirect_to?", "rails-questions"),
          ("How should you structure a project walkthrough answer?", "project-walkthrough"),
      ],
      assignments=[
          "Answer every question in this lesson out loud, without reading the answers. Time yourself.",
          "Record a 3-minute project walkthrough for OdinBook using the four-part structure.",
      ],
      resources=[
          ("Rails Interview Questions (GitHub)", "https://github.com/brookr/rails-interview-questions"),
          ("Ruby Interview Questions (Big List)", "https://www.toptal.com/ruby/interview-questions"),
          ("YouTube — Rails Developer Interview (GoRails)", "https://www.youtube.com/watch?v=sUhBE6bVQQw"),
      ])

    # ── databases-interviews ──────────────────────────────
    w("databases-interviews", "Database Interview Questions",
      intro="SQL and database design questions are common in Rails interviews. Junior developers are expected to understand basic query writing, indexing, and when to use specific database features.",
      overview=[
          "Answer SQL query questions confidently.",
          "Explain indexing and when to add indexes.",
          "Describe database design and normalisation.",
          "Understand Rails-specific database patterns.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="sql-questions">Common SQL Questions</h2>'
          + code("""\
-- Q: What is the difference between INNER JOIN and LEFT JOIN?
-- A: INNER JOIN returns only rows where the join condition matches in both tables.
--    LEFT JOIN returns all rows from the left table, with NULLs for non-matching right rows.

-- Example: find all users, with their post count (including users with 0 posts)
SELECT users.name, COUNT(posts.id) AS post_count
FROM users
LEFT JOIN posts ON posts.user_id = users.id
GROUP BY users.id, users.name;
-- INNER JOIN would exclude users with no posts.

-- Q: What is the difference between WHERE and HAVING?
-- A: WHERE filters rows before grouping.
--    HAVING filters groups after GROUP BY.
SELECT user_id, COUNT(*) AS post_count
FROM posts
WHERE published = true          -- filter rows first
GROUP BY user_id
HAVING COUNT(*) > 5;           -- then filter groups

-- Q: What does EXPLAIN ANALYZE do?
-- A: Shows the query execution plan and actual run time.
--    Use it to find slow queries and missing indexes.
EXPLAIN ANALYZE SELECT * FROM posts WHERE user_id = 42;
""")
          + '<h2 class="lesson-section-title" id="indexing">Indexing</h2>'
          + code("""\
-- Q: What is a database index and when should you add one?
-- A: An index is a data structure (usually B-tree) that speeds up lookups
--    on a column at the cost of slightly slower writes and extra storage.

-- Add an index when:
-- 1. You query a column frequently in WHERE, JOIN, or ORDER BY
-- 2. The column has high cardinality (many unique values)
-- 3. The table has many rows (1,000+ is a rough threshold)

-- In Rails migrations:
add_index :posts, :user_id                          # single column
add_index :posts, [:user_id, :created_at]           # composite
add_index :users, :email, unique: true              # unique constraint

-- Q: What is a composite index and when is it useful?
-- A: An index on multiple columns. Useful when you frequently filter
--    by two columns together (e.g. user_id AND created_at).
--    Order matters: (user_id, created_at) helps queries on user_id alone
--    but NOT queries on created_at alone.

-- Q: What is an N+1 at the database level?
-- A: Running N individual SELECT queries instead of one JOIN/IN query.
--    Rails' .includes() fixes this by using one IN () query.
""")
          + '<h2 class="lesson-section-title" id="design-questions">Design Questions</h2>'
          + code("""\
-- Q: What is database normalisation?
-- A: Organising tables to reduce redundancy and improve data integrity.
--    1NF: no repeating groups, atomic values.
--    2NF: no partial dependencies on composite keys.
--    3NF: no transitive dependencies (non-key columns depend only on the key).

-- Q: When would you denormalise?
-- A: When read performance is critical and data changes rarely.
--    E.g. storing a cached post_count on users to avoid COUNT(*) every page load.
--    Rails counter_cache: belongs_to :user, counter_cache: true

-- Q: What is the difference between a SQL and NoSQL database?
-- A: SQL (PostgreSQL, MySQL) — structured, relational, ACID transactions, schema-first.
--    NoSQL (MongoDB, Redis) — flexible schema, horizontal scaling, eventual consistency.
--    Rails uses SQL by default. Redis is often added for caching/queues (Sidekiq).
""")
      ),
      kc=[
          ("What is the difference between INNER JOIN and LEFT JOIN?", "sql-questions"),
          ("When should you add a database index?", "indexing"),
          ("What is the difference between WHERE and HAVING?", "sql-questions"),
      ],
      assignments=[
          "Open a Rails console on one of your projects and run Post.all.explain. Read the output.",
          "Answer every question in this lesson out loud without looking at the answers.",
          "Draw the ERD for your OdinBook database from memory, then check it against your schema.rb.",
      ],
      resources=[
          ("PostgreSQL — EXPLAIN Documentation", "https://www.postgresql.org/docs/current/using-explain.html"),
          ("Use The Index, Luke — Indexing Guide", "https://use-the-index-luke.com/"),
          ("SQLZoo — Interactive Practice", "https://sqlzoo.net/"),
      ])

    # ── system-design-basics ──────────────────────────────
    w("system-design-basics", "System Design Basics",
      intro="Junior developers are not expected to design distributed systems, but you should be able to discuss how a web application is structured, how to scale a Rails app, and what happens when things go wrong.",
      overview=[
          "Understand the basic architecture of a deployed Rails application.",
          "Know the main strategies for scaling a web app.",
          "Discuss caching, background jobs, and CDNs.",
          "Answer basic system design questions in an interview.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="architecture">Rails App Architecture</h2>'
          + code("""\
# A deployed Rails app has these layers:

# Browser / Client
#   ↓ HTTPS
# CDN (Cloudflare, Fastly) — caches static assets, DDoS protection
#   ↓
# Load Balancer (Fly.io Proxy, AWS ALB) — distributes traffic across app servers
#   ↓
# App Servers (Puma) — multiple Rails processes handling requests
#   ↓
# Database (PostgreSQL) — primary + optional read replicas
#   ↓
# Background Workers (Sidekiq + Redis) — async jobs (emails, file processing)
#   ↓
# File Storage (S3 / Active Storage) — user-uploaded files
#   ↓
# Cache (Redis / Memcached) — session data, fragment caches, low-level caches
#   ↓
# External APIs (Stripe, SendGrid, Twilio, etc.)
""")
          + '<h2 class="lesson-section-title" id="scaling">Scaling a Rails App</h2>'
          + code("""\
# Vertical scaling — bigger server (more RAM/CPU). Simple, has limits.
# Horizontal scaling — more servers behind a load balancer.

# Common scaling strategies in Rails:

# 1. Database indexing — fastest win for slow query performance
# 2. Caching
#    - Fragment caching: cache parts of views
#      <%= cache @post do %> ... <% end %>
#    - Low-level caching:
#      Rails.cache.fetch("user_#{id}_stats", expires_in: 5.minutes) { ... }
#    - HTTP caching: ETag / Last-Modified headers

# 3. Background jobs (Sidekiq)
#    Move slow work (emails, image processing, API calls) out of the request cycle

# 4. Database read replicas
#    Route read-heavy queries to a replica to reduce primary load

# 5. CDN for assets
#    Serve CSS/JS/images from edge servers close to the user

# 6. Database connection pooling (PgBouncer)
#    Reuse DB connections instead of creating new ones per request
""")
          + '<h2 class="lesson-section-title" id="interview-approach">Approaching System Design in an Interview</h2>'
          + code("""\
# If asked a system design question (e.g. "Design a URL shortener"):

# Step 1 — Clarify requirements (2 min)
# "How many URLs per day? Read-heavy or write-heavy?
#  Any analytics needed? Custom short codes?"

# Step 2 — Sketch the basic architecture
# Browser → Rails app → PostgreSQL
# Redirect route: GET /:code → look up long URL → redirect

# Step 3 — Discuss the data model
# CREATE TABLE short_urls (
#   id SERIAL PRIMARY KEY,
#   code VARCHAR(10) UNIQUE NOT NULL,
#   original_url TEXT NOT NULL,
#   click_count INTEGER DEFAULT 0,
#   created_at TIMESTAMP
# );

# Step 4 — Discuss scaling concerns
# "At high traffic, the redirect lookup is a hot path.
#  I'd add an index on code and consider caching it in Redis
#  with a short TTL to avoid hitting the DB on every redirect."

# Step 5 — Mention what you'd add later
# "For analytics I'd log clicks asynchronously via a background job
#  so it doesn't slow down the redirect."
""")
          + tip("At the junior level, interviewers want to see structured thinking, not perfect answers. Show you can break a problem down, consider trade-offs, and ask the right questions.")
      ),
      kc=[
          ("What are the main layers in a deployed Rails application?", "architecture"),
          ("What are three strategies for scaling a Rails app?", "scaling"),
          ("What are the five steps for approaching a system design question?", "interview-approach"),
      ],
      assignments=[
          "Draw the architecture of your OdinBook deployment from memory, then check it.",
          "Practice the URL shortener system design question out loud, following the five steps.",
          "Read the High Scalability blog for one example of how a real Rails company scaled.",
      ],
      resources=[
          ("High Scalability Blog", "http://highscalability.com/"),
          ("The System Design Primer (GitHub)", "https://github.com/donnemartin/system-design-primer"),
          ("YouTube — System Design for Beginners (NeetCode)", "https://www.youtube.com/watch?v=i53Gi_K3o7I"),
          ("Sidekiq — Background Jobs for Ruby", "https://sidekiq.org/"),
      ])

    print(f"\n  Getting Hired: {len(ALL)} lessons done")


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    seed_getting_hired()
    print("\nPart 3 complete. Committing...")
    os.chdir(BASE)
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", "Seed Rails path Part 3: Getting Hired (12 lessons)"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Pushed.\n")
    print("=" * 60)
    print("  PREVIEW IN BROWSER")
    print("=" * 60)
    print("  cd ~/devpath")
    print("  python3 -m http.server 8080")
    print()
    print("  Then open:")
    print("  http://localhost:8080/paths/full-stack-ruby-on-rails/courses/getting-hired/index.html")
    print()
    print("  First lesson:")
    print("  http://localhost:8080/paths/full-stack-ruby-on-rails/courses/getting-hired/lessons/preparing-for-job-search.html")
    print("=" * 60)


if __name__ == "__main__":
    main()
