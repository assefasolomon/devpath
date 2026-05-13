#!/usr/bin/env python3
"""Rails Path — Advanced HTML and CSS (10 lessons)"""
import os, subprocess

BASE  = os.path.expanduser("~/devpath")
RAILS = os.path.join(BASE, "paths", "full-stack-ruby-on-rails", "courses")
ROOT  = "../../../../../"
LOGO  = ('<svg viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="13" '
         'stroke="currentColor" stroke-width="1.8"/><path d="M8 14 L14 7 L20 14 '
         'L14 21 Z" fill="currentColor"/></svg>')

def nav():
    return (
        '<nav class="site-nav">'
        f'<a href="{ROOT}index.html" class="nav-logo">{LOGO} DevPath</a>'
        '<ul class="nav-links">'
        f'<li><a href="{ROOT}index.html">Home</a></li>'
        f'<li><a href="{ROOT}foundations/index.html">Foundations</a></li>'
        f'<li><a href="{ROOT}paths/full-stack-javascript/index.html">Full Stack JS</a></li>'
        f'<li><a href="{ROOT}paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a></li>'
        '</ul></nav>'
    )

def footer():
    return '<footer class="site-footer"><p>DevPath — A free, open, project-based web development curriculum.</p></footer>'

def code(s):
    esc = s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f'<div class="code-block"><pre><code>{esc}</code></pre></div>'

def tip(t):
    return f'<div class="callout callout-tip"><span class="callout-icon">💡</span><p>{t}</p></div>'

def write(ldir, course_title, all_lessons, sidebar_html, slug,
          title, intro, overview, body, kc, assignments, resources):
    idx = next((i for i,l in enumerate(all_lessons) if l[0]==slug), None)
    p = (all_lessons[idx-1][1], all_lessons[idx-1][0]+".html") if idx and idx>0 else None
    n = (all_lessons[idx+1][1], all_lessons[idx+1][0]+".html") if idx is not None and idx<len(all_lessons)-1 else None
    pb = f'<a href="{p[1]}" class="btn btn-blue-outline">&#8592; Previous</a>' if p else '<span></span>'
    nb = f'<a href="{n[1]}" class="btn btn-blue">Next &#8594;</a>' if n else '<span></span>'
    navb = (f'<div class="lesson-nav-bar">'
            f'<div class="lesson-nav-bar-group">{pb}</div>'
            f'<div class="lesson-nav-bar-group"><button class="btn btn-green mark-complete-btn">Mark Completed</button></div>'
            f'<div class="lesson-nav-bar-group">{nb}</div></div>')
    bc = (f'<nav class="breadcrumb"><a href="{ROOT}index.html">Home</a>'
          f'<span class="breadcrumb-sep">/</span>'
          f'<a href="{ROOT}paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a>'
          f'<span class="breadcrumb-sep">/</span>'
          f'<a href="../index.html">{course_title}</a>'
          f'<span class="breadcrumb-sep">/</span>'
          f'<span class="breadcrumb-current">{title}</span></nav>')
    ov   = "".join(f"<li>{i}</li>" for i in overview)
    kcli = "".join(f'<li><a href="#{k[1]}" data-target="{k[1]}">{k[0]}</a></li>' for k in kc)
    asli = "".join(f"<li>{a}</li>" for a in assignments)
    rsli = "".join(f'<li><a href="{r[1]}" target="_blank" rel="noopener">{r[0]}</a></li>' for r in resources)
    ph = (f'<a href="{p[1]}" class="pagination-link prev"><span class="pagination-label">&#8592; Previous</span>'
          f'<span class="pagination-title">{p[0]}</span></a>' if p else "<span></span>")
    nh = (f'<a href="{n[1]}" class="pagination-link next"><span class="pagination-label">Next &#8594;</span>'
          f'<span class="pagination-title">{n[0]}</span></a>' if n else "<span></span>")
    html = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'  <title>{title} | DevPath</title>\n'
        f'  <link rel="stylesheet" href="{ROOT}css/styles.css">\n'
        '</head>\n<body>\n'
        + nav() + '\n' + navb + '\n'
        + f'<div class="page-header"><div class="page-header-inner">{bc}<h1>{title}</h1></div></div>\n'
        + f'<div class="lesson-layout">{sidebar_html}<main><div class="lesson-body">\n'
        + f'<div class="block-intro"><p>{intro}</p></div>\n'
        + f'<div class="block-overview"><div class="block-overview-label">Lesson Overview</div><ul>{ov}</ul></div>\n'
        + body
        + f'\n<div class="block-kc"><div class="block-kc-label">Knowledge Check</div>'
        + '<p class="kc-note">Click any question to jump to the section that answers it.</p>'
        + f'<ol>{kcli}</ol></div>\n'
        + f'<div class="block-assignments"><div class="block-assignments-label">Assignments</div><ol>{asli}</ol></div>\n'
        + f'<div class="block-resources"><div class="block-resources-label">Additional Resources</div><ul>{rsli}</ul></div>\n'
        + f'</div><div class="lesson-pagination">{ph}{nh}</div></main></div>\n'
        + footer() + '\n'
        + f'<script src="{ROOT}js/main.js"></script>\n</body>\n</html>'
    )
    with open(os.path.join(ldir, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  {slug}")

def write_index(course_dir, title, description, sections):
    cards = ""
    for sec, lessons in sections:
        cards += f'<div class="index-section"><h2 class="index-section-title">{sec}</h2><ul class="index-lesson-list">'
        for slug, ltitle, proj in lessons:
            cls = "index-lesson-item" + (" is-project" if proj else "")
            cards += f'<li class="{cls}"><a href="lessons/{slug}.html">{ltitle}</a></li>'
        cards += "</ul></div>"
    html = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'  <title>{title} | DevPath</title>\n'
        f'  <link rel="stylesheet" href="{ROOT}css/styles.css">\n'
        '</head>\n<body>\n' + nav() + '\n'
        + f'<div class="page-header"><div class="page-header-inner">'
        + f'<nav class="breadcrumb"><a href="{ROOT}index.html">Home</a><span class="breadcrumb-sep">/</span>'
        + f'<a href="{ROOT}paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a>'
        + f'<span class="breadcrumb-sep">/</span><span class="breadcrumb-current">{title}</span></nav>'
        + f'<h1>{title}</h1><p class="course-description">{description}</p></div></div>\n'
        + f'<div class="course-index">{cards}</div>\n'
        + footer() + '\n'
        + f'<script src="{ROOT}js/main.js"></script>\n</body>\n</html>'
    )
    with open(os.path.join(course_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  index → {course_dir}/index.html")

def seed_advanced_html_css():
    course_dir = os.path.join(RAILS, "advanced-html-css")
    ldir = os.path.join(course_dir, "lessons")
    os.makedirs(ldir, exist_ok=True)

    ALL = [
        ("animation",               "Animation"),
        ("accessibility",           "Accessibility"),
        ("responsive-design",       "Responsive Design"),
        ("css-grid",                "CSS Grid"),
        ("natural-responsiveness",  "Natural Responsiveness"),
        ("media-queries",           "Media Queries"),
        ("images-in-html-css",      "Images in HTML/CSS"),
        ("css-grid-advanced",       "CSS Grid — Advanced"),
        ("performance",             "Performance"),
        ("project-personal-portfolio","Project: Personal Portfolio"),
    ]

    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">Advanced HTML &amp; CSS</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">Animation</div>'
        + lnk("animation","Animation")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Accessibility</div>'
        + lnk("accessibility","Accessibility")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Responsive Design</div>'
        + lnk("responsive-design","Responsive Design")
        + lnk("css-grid","CSS Grid")
        + lnk("natural-responsiveness","Natural Responsiveness")
        + lnk("media-queries","Media Queries")
        + lnk("images-in-html-css","Images in HTML/CSS")
        + lnk("css-grid-advanced","CSS Grid — Advanced")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Performance</div>'
        + lnk("performance","Performance")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Project</div>'
        + lnk("project-personal-portfolio","Project: Personal Portfolio",True)
        + '</div></aside>'
    )

    def w(slug, title, intro, overview, body, kc, assignments, resources):
        write(ldir, "Advanced HTML and CSS", ALL, sidebar,
              slug, title, intro, overview, body, kc, assignments, resources)

    write_index(course_dir, "Advanced HTML and CSS",
        "Master CSS animations, accessibility, responsive design, CSS Grid, performance, and build a professional personal portfolio.",
        [("Animation",[("animation","Animation",False)]),
         ("Accessibility",[("accessibility","Accessibility",False)]),
         ("Responsive Design",[
            ("responsive-design","Responsive Design",False),
            ("css-grid","CSS Grid",False),
            ("natural-responsiveness","Natural Responsiveness",False),
            ("media-queries","Media Queries",False),
            ("images-in-html-css","Images in HTML/CSS",False),
            ("css-grid-advanced","CSS Grid — Advanced",False)]),
         ("Performance",[("performance","Performance",False)]),
         ("Project",[("project-personal-portfolio","Project: Personal Portfolio",True)])])

    w("animation","Animation",
      intro="CSS animations and transitions bring interfaces to life. Done well, they guide attention and communicate state. This lesson covers transitions, keyframe animations, and the motion principles behind good UI animation.",
      overview=["Use transition for hover and state changes.","Write @keyframes animations.","Use animation shorthand properties.","Follow motion design principles."],
      body=(
        '<h2 class="lesson-section-title" id="transitions">Transitions</h2>'
        + code("""\
/* transition: property duration easing delay */
.btn {
  background: #3b82f6;
  transition: background 200ms ease, transform 150ms ease, box-shadow 150ms ease;
}
.btn:hover {
  background: #2563eb;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(59,130,246,.4);
}

/* transition: all — convenient but can cause performance issues */
/* Prefer specific properties */

/* Easing functions */
ease          /* slow-fast-slow (default) */
ease-in       /* slow start */
ease-out      /* slow end — best for elements leaving the screen */
ease-in-out   /* slow start and end */
linear        /* constant speed */
cubic-bezier(.17,.67,.83,.67)  /* custom */
""")
        + '<h2 class="lesson-section-title" id="keyframes">Keyframe Animations</h2>'
        + code("""\
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50%       { transform: scale(1.05); }
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Apply */
.modal    { animation: fadeIn 250ms ease forwards; }
.badge    { animation: pulse 2s ease-in-out infinite; }
.spinner  { animation: spin 800ms linear infinite; }

/* animation shorthand: name duration easing delay iterations direction fill-mode */
.alert { animation: fadeIn 300ms ease-out 100ms 1 normal both; }

/* Respect user motion preferences */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; }
}
""")
      ),
      kc=[("What is the difference between transition and animation?","transitions"),
          ("What does animation-fill-mode: forwards do?","keyframes"),
          ("How do you respect the user's reduced-motion preference?","keyframes")],
      assignments=["Add a fadeIn animation to a modal dialog.",
                   "Build a loading spinner using a CSS keyframe animation.",
                   "Add prefers-reduced-motion support to all animations."],
      resources=[("MDN — CSS Animations","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations"),
                 ("Cubic Bezier Tool","https://cubic-bezier.com/"),
                 ("Motion Design Principles — Material Design","https://m3.material.io/styles/motion/overview")])

    w("accessibility","Accessibility",
      intro="Accessibility (a11y) means building web experiences that work for everyone — including people using screen readers, keyboard navigation, or assistive technology. It is both an ethical requirement and a legal one in many countries.",
      overview=["Understand WCAG guidelines.","Write semantic HTML for screen readers.","Use ARIA attributes correctly.","Test accessibility with keyboard navigation and screen readers.","Meet color contrast requirements."],
      body=(
        '<h2 class="lesson-section-title" id="semantic-html">Semantic HTML</h2>'
        + code("""\
<!-- BAD — div soup -->
<div class="header"><div class="nav"><div class="nav-link" onclick="go()">Home</div></div></div>
<div class="main"><div class="article"><div class="heading">Title</div></div></div>

<!-- GOOD — semantic HTML -->
<header>
  <nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
  </nav>
</header>
<main>
  <article>
    <h1>Title</h1>
    <p>Content</p>
  </article>
</main>
<footer>...</footer>

<!-- Interactive elements must be focusable -->
<!-- BAD: -->  <div onclick="submit()">Submit</div>
<!-- GOOD: --> <button type="submit">Submit</button>
""")
        + '<h2 class="lesson-section-title" id="aria">ARIA</h2>'
        + code("""\
<!-- ARIA labels for elements without visible text -->
<button aria-label="Close dialog">
  <svg>...</svg>
</button>

<!-- Live regions — announce dynamic content to screen readers -->
<div aria-live="polite" aria-atomic="true">
  <%= flash[:notice] %>
</div>

<!-- Role for custom interactive elements -->
<div role="button" tabindex="0" aria-pressed="false">Toggle</div>

<!-- Hiding decorative elements from screen readers -->
<img src="decoration.png" alt="" aria-hidden="true">

<!-- Describing form fields -->
<label for="email">Email address</label>
<input type="email" id="email" aria-describedby="email-hint" required>
<p id="email-hint">We will send a confirmation to this address.</p>
""")
        + '<h2 class="lesson-section-title" id="color-contrast">Color Contrast</h2>'
        + code("""\
/* WCAG AA requires:
   - 4.5:1 contrast ratio for normal text
   - 3:1 for large text (18px+ or 14px+ bold)
   - 3:1 for UI components and graphics */

/* Check with: https://webaim.org/resources/contrastchecker/ */

/* Good combinations: */
color: #111827;  background: #ffffff;  /* 16.1:1 */
color: #ffffff;  background: #1d4ed8;  /* 5.9:1 */

/* Failing: */
color: #9ca3af;  background: #ffffff;  /* 2.9:1 — too low */
""")
      ),
      kc=[("Why must interactive elements be actual buttons or links?","semantic-html"),
          ("What does aria-live do?","aria"),
          ("What contrast ratio does WCAG AA require for normal text?","color-contrast")],
      assignments=["Audit a project page with a keyboard only (Tab, Enter, Space). Fix any issues.",
                   "Install the axe DevTools browser extension and fix all critical errors on a page.",
                   "Check all text color/background combinations in a project for WCAG AA compliance."],
      resources=[("WebAIM — Contrast Checker","https://webaim.org/resources/contrastchecker/"),
                 ("MDN — Accessibility","https://developer.mozilla.org/en-US/docs/Web/Accessibility"),
                 ("axe DevTools Browser Extension","https://www.deque.com/axe/devtools/")])

    w("responsive-design","Responsive Design",
      intro="Responsive design means your website works well on every screen size — from a 320px phone to a 4K monitor. This is not optional: over half of web traffic is mobile.",
      overview=["Understand mobile-first design.","Use the viewport meta tag.","Build fluid layouts with flexbox.","Apply responsive typography."],
      body=(
        '<h2 class="lesson-section-title" id="mobile-first">Mobile-First Design</h2>'
        + code("""\
/* Mobile-first: write base styles for small screens,
   then add media queries for larger screens */

/* Base (mobile) */
.container { padding: 1rem; }
.card-grid { display: flex; flex-direction: column; gap: 1rem; }

/* Tablet and up */
@media (min-width: 640px) {
  .card-grid { flex-direction: row; flex-wrap: wrap; }
  .card-grid > * { flex: 1 1 calc(50% - 0.5rem); }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
  .card-grid > * { flex: 1 1 calc(33% - 0.67rem); }
}
""")
        + '<h2 class="lesson-section-title" id="viewport">Viewport Meta Tag</h2>'
        + code("""\
<!-- Required in every HTML page -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Without this, mobile browsers zoom out to show the desktop layout -->
""")
      ),
      kc=[("What does mobile-first mean in practice?","mobile-first"),
          ("What does the viewport meta tag do?","viewport")],
      assignments=["Take a desktop layout and make it responsive using mobile-first media queries.",
                   "Test your layout in Chrome DevTools device mode at 375px, 768px, and 1440px."],
      resources=[("MDN — Responsive Design","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design")])

    w("css-grid","CSS Grid",
      intro="CSS Grid is the most powerful layout system in CSS. It lets you place elements in two dimensions — rows and columns — with precise control. It's ideal for page layouts, card grids, and any two-dimensional arrangement.",
      overview=["Define grid rows and columns.","Place items with grid-column and grid-row.","Use grid template areas for named layouts.","Combine Grid and Flexbox."],
      body=(
        '<h2 class="lesson-section-title" id="grid-basics">Grid Basics</h2>'
        + code("""\
.grid {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;     /* 3 columns */
  grid-template-rows: auto 1fr auto;       /* 3 rows */
  gap: 1.5rem;                             /* row and column gap */
  min-height: 100vh;
}

/* Repeat and minmax */
grid-template-columns: repeat(3, 1fr);
grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));  /* responsive */
""")
        + '<h2 class="lesson-section-title" id="placement">Item Placement</h2>'
        + code("""\
.header  { grid-column: 1 / -1; }          /* span full width */
.sidebar { grid-column: 1 / 2; grid-row: 2 / 4; }
.main    { grid-column: 2 / -1; }

/* Named template areas */
.layout {
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
}
.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }
.footer  { grid-area: footer; }
""")
      ),
      kc=[("What does 1fr mean in CSS Grid?","grid-basics"),
          ("What does repeat(auto-fill, minmax(280px, 1fr)) do?","grid-basics"),
          ("How do you name grid areas?","placement")],
      assignments=["Build a classic holy-grail layout (header, sidebar, main, footer) using grid-template-areas.",
                   "Build a responsive card grid using repeat(auto-fill, minmax(280px, 1fr))."],
      resources=[("CSS Tricks — Complete Guide to Grid","https://css-tricks.com/snippets/css/complete-guide-grid/"),
                 ("Grid Garden — CSS Grid Game","https://cssgridgarden.com/")])

    w("natural-responsiveness","Natural Responsiveness",
      intro="The best responsive layouts don't need many media queries because the CSS is written to be naturally fluid. This lesson covers intrinsic sizing, logical properties, and writing CSS that responds automatically.",
      overview=["Use intrinsic sizing: min-content, max-content, fit-content.","Use logical properties for internationalisation.","Write fluid layouts that need fewer media queries."],
      body=(
        '<h2 class="lesson-section-title" id="intrinsic">Intrinsic Sizing</h2>'
        + code("""\
/* min-content — shrink to smallest possible size */
.tag { width: min-content; white-space: nowrap; }

/* max-content — expand to fit all content */
.tooltip { width: max-content; }

/* fit-content — use available space up to max-content */
.label { width: fit-content; }

/* Naturally fluid column layout */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr));
  gap: 1.5rem;
}
/* This grid reflows naturally — no media queries needed */
""")
        + '<h2 class="lesson-section-title" id="logical">Logical Properties</h2>'
        + code("""\
/* Physical → Logical equivalents */
margin-top    → margin-block-start
margin-bottom → margin-block-end
margin-left   → margin-inline-start
margin-right  → margin-inline-end
padding-left  → padding-inline-start
width         → inline-size
height        → block-size

/* Why: logical properties work in RTL languages automatically */
.card { padding-inline: 1.5rem; margin-block: 1rem; }
""")
      ),
      kc=[("What is the difference between min-content and max-content?","intrinsic"),
          ("What problem do logical properties solve?","logical")],
      assignments=["Rewrite a layout using logical properties instead of margin-left/right.",
                   "Build a card grid that reflows with no media queries using auto-fill and minmax."],
      resources=[("MDN — Logical Properties","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties")])

    w("media-queries","Media Queries",
      intro="Media queries are the standard mechanism for applying different CSS at different viewport sizes, device types, and user preferences. This lesson covers syntax, breakpoints, and modern media query features.",
      overview=["Write min-width and max-width media queries.","Choose sensible breakpoints.","Use media queries for print, color scheme, and motion preferences.","Use container queries for component-level responsiveness."],
      body=(
        '<h2 class="lesson-section-title" id="syntax">Media Query Syntax</h2>'
        + code("""\
/* min-width (mobile-first — preferred) */
@media (min-width: 640px)  { /* sm */ }
@media (min-width: 768px)  { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }

/* max-width (desktop-first) */
@media (max-width: 767px) { /* mobile only */ }

/* Modern range syntax */
@media (640px <= width < 1024px) { /* tablet only */ }

/* Combining */
@media (min-width: 768px) and (orientation: landscape) { }

/* User preferences */
@media (prefers-color-scheme: dark) { }
@media (prefers-reduced-motion: reduce) { }
@media print { .no-print { display: none; } }
""")
        + '<h2 class="lesson-section-title" id="container-queries">Container Queries</h2>'
        + code("""\
/* Container queries — respond to parent container size, not viewport */
.card-wrapper { container-type: inline-size; container-name: card; }

@container card (min-width: 400px) {
  .card { display: flex; flex-direction: row; }
}

/* More powerful than media queries for component libraries:
   the same card component responds to its own container,
   whether it's in a 3-column grid or a 1-column sidebar */
""")
      ),
      kc=[("What breakpoints should a mobile-first design use?","syntax"),
          ("What is the difference between a media query and a container query?","container-queries")],
      assignments=["Build a navigation that switches from a hamburger menu on mobile to a horizontal bar on desktop.",
                   "Use a container query to make a card component adapt to its container width."],
      resources=[("MDN — Media Queries","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries"),
                 ("MDN — Container Queries","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Container_Queries")])

    w("images-in-html-css","Images in HTML/CSS",
      intro="Images are the heaviest assets on most web pages. This lesson covers responsive images, modern formats, lazy loading, and techniques for using images in CSS — essential for performance and quality.",
      overview=["Use srcset and sizes for responsive images.","Use modern image formats: WebP, AVIF.","Implement lazy loading.","Use CSS background images correctly.","Optimise images for the web."],
      body=(
        '<h2 class="lesson-section-title" id="responsive-images">Responsive Images</h2>'
        + code("""\
<!-- srcset — let the browser pick the right size -->
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
  sizes="(max-width: 600px) 100vw, (max-width: 1200px) 50vw, 800px"
  alt="A mountain landscape"
  loading="lazy"
  width="800" height="533"
>

<!-- picture — art direction, different crop at different sizes -->
<picture>
  <source media="(max-width: 600px)" srcset="photo-portrait.webp">
  <source srcset="photo-landscape.webp" type="image/webp">
  <img src="photo-landscape.jpg" alt="Photo" loading="lazy">
</picture>
""")
        + '<h2 class="lesson-section-title" id="formats">Modern Image Formats</h2>'
        + code("""\
# Format comparison (same image):
# JPEG: 240 KB  — good for photos, no transparency
# PNG:  420 KB  — lossless, transparency, icons
# WebP:  85 KB  — 25-35% smaller than JPEG, transparency, modern browsers
# AVIF:  55 KB  — best compression, good browser support (2023+)

# In Rails with Active Storage variants:
@post.cover_image.variant(format: :webp, resize_to_limit: [800, nil])
""")
      ),
      kc=[("What does srcset do?","responsive-images"),
          ("What is the difference between WebP and AVIF?","formats"),
          ("What does loading='lazy' do?","responsive-images")],
      assignments=["Convert all images in a project to use srcset with 3 sizes.",
                   "Add lazy loading to all below-the-fold images.",
                   "Convert a JPEG to WebP and compare file sizes."],
      resources=[("MDN — Responsive Images","https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images"),
                 ("Squoosh — Image Compression Tool","https://squoosh.app/")])

    w("css-grid-advanced","CSS Grid — Advanced",
      intro="Building on the CSS Grid basics, this lesson covers dense packing, subgrid, grid animations, and real-world layout patterns used in production Rails applications.",
      overview=["Use grid-auto-flow: dense for masonry-like layouts.","Use subgrid to align nested elements.","Build a magazine-style layout.","Debug Grid with browser DevTools."],
      body=(
        '<h2 class="lesson-section-title" id="dense">Dense Packing</h2>'
        + code("""\
/* grid-auto-flow: dense — fill holes left by spanning items */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-rows: 200px;
  gap: 1rem;
  grid-auto-flow: dense;
}
.gallery .featured {
  grid-column: span 2;
  grid-row: span 2;
}
""")
        + '<h2 class="lesson-section-title" id="subgrid">Subgrid</h2>'
        + code("""\
/* subgrid — nested elements participate in parent grid tracks */
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto 1fr auto;  /* image | content | footer */
}

.card {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid;  /* use parent's row definitions */
}

/* Result: all cards have perfectly aligned image, content, and footer rows
   regardless of content length */
""")
        + tip("Open Grid DevTools in Firefox (right-click → Inspect → Grid overlay) to visualise your grid tracks. Far easier than guessing from the code.")
      ),
      kc=[("What does grid-auto-flow: dense do?","dense"),
          ("What problem does subgrid solve?","subgrid")],
      assignments=["Build a photo gallery with dense auto-flow and some featured (spanning) images.",
                   "Build a 3-card layout using subgrid so all footers align at the same row."],
      resources=[("MDN — subgrid","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Subgrid"),
                 ("CSS Tricks — Grid Auto Flow","https://css-tricks.com/almanac/properties/g/grid-auto-flow/")])

    w("performance","Performance",
      intro="Web performance directly affects user experience, SEO rankings, and conversion rates. This lesson covers the metrics that matter, the most impactful optimisations, and how to measure performance.",
      overview=["Understand Core Web Vitals: LCP, FID/INP, CLS.","Optimise images, fonts, and CSS.","Use browser caching and the asset pipeline.","Measure performance with Lighthouse and PageSpeed Insights."],
      body=(
        '<h2 class="lesson-section-title" id="core-web-vitals">Core Web Vitals</h2>'
        + code("""\
# LCP — Largest Contentful Paint — when the main content loads
# Target: < 2.5 seconds
# Common causes: large unoptimised hero images, slow server, render-blocking resources
# Fix: optimise images, preload hero image, use CDN

# CLS — Cumulative Layout Shift — unexpected layout jumps
# Target: < 0.1
# Common causes: images/ads without width/height, late-loading fonts
# Fix: always set width + height on img, use font-display: swap

# INP — Interaction to Next Paint — responsiveness
# Target: < 200ms
# Common causes: heavy JavaScript on the main thread
# Fix: defer non-critical JS, use web workers for heavy computation
""")
        + '<h2 class="lesson-section-title" id="optimisations">Key Optimisations</h2>'
        + code("""\
<!-- Preload critical assets -->
<link rel="preload" as="image" href="hero.webp" fetchpriority="high">
<link rel="preload" as="font" href="/fonts/inter.woff2" crossorigin>

<!-- Defer non-critical JavaScript -->
<script src="analytics.js" defer></script>
<script src="chat-widget.js" async></script>

<!-- Image optimisation checklist -->
<!-- ✓ Use WebP/AVIF format -->
<!-- ✓ Set width and height attributes -->
<!-- ✓ Use loading="lazy" for below-fold images -->
<!-- ✓ Use srcset for responsive images -->
<!-- ✓ Compress with Squoosh or Sharp -->

# Rails production optimisations (automatic):
# ✓ Asset fingerprinting (cache busting)
# ✓ CSS/JS concatenation and minification
# ✓ Gzip/Brotli compression (configure on your host)
""")
      ),
      kc=[("What does LCP measure?","core-web-vitals"),
          ("What causes CLS and how do you fix it?","core-web-vitals"),
          ("What does the preload link hint do?","optimisations")],
      assignments=["Run Lighthouse on a deployed project and record your scores.",
                   "Fix at least one LCP issue and one CLS issue and re-run Lighthouse.",
                   "Add width and height to every img tag in a project."],
      resources=[("Google PageSpeed Insights","https://pagespeed.web.dev/"),
                 ("web.dev — Core Web Vitals","https://web.dev/vitals/"),
                 ("Squoosh — Image Optimiser","https://squoosh.app/")])

    w("project-personal-portfolio","Project: Personal Portfolio",
      intro="Build your personal portfolio website from scratch using everything from this course — responsive layout, CSS Grid, animations, accessibility, dark mode, and performance. This is the page employers will visit.",
      overview=["Build a complete responsive portfolio site.","Apply advanced CSS techniques throughout.","Meet WCAG AA accessibility standards.","Score 90+ on Lighthouse for performance.","Deploy on GitHub Pages or Netlify."],
      body=(
        '<h2 class="lesson-section-title" id="requirements">Requirements</h2>'
        "<ul>"
        "<li><strong>Hero section</strong> — name, title, and CTA buttons. Fluid typography with clamp().</li>"
        "<li><strong>About section</strong> — short bio, skills grid, a photo.</li>"
        "<li><strong>Projects section</strong> — CSS Grid card layout with at least 3 projects, live demo + GitHub links.</li>"
        "<li><strong>Contact section</strong> — links to email, GitHub, LinkedIn.</li>"
        "<li><strong>Dark mode</strong> — via prefers-color-scheme and CSS custom properties.</li>"
        "<li><strong>Animations</strong> — subtle scroll-triggered fade-ins (IntersectionObserver).</li>"
        "<li><strong>Accessible</strong> — keyboard navigable, all images have alt text, 4.5:1 contrast.</li>"
        "<li><strong>Fast</strong> — Lighthouse performance score ≥ 90.</li>"
        "</ul>"
        + code("""\
mkdir ~/devpath-projects/advanced-html-css/portfolio
cd ~/devpath-projects/advanced-html-css/portfolio
git init
touch index.html
mkdir css js images

# Recommended CSS file structure:
# css/reset.css       — minimal reset
# css/variables.css   — all custom properties
# css/layout.css      — grid and flex containers
# css/components.css  — cards, buttons, nav
# css/animations.css  — keyframes and transitions
# css/dark.css        — dark mode overrides
""")
        + tip("Your portfolio is itself a demonstration of your skills. If it loads slowly, has bad contrast, or breaks on mobile — that tells employers something. Make it excellent.")
      ),
      kc=[("What CSS technique handles dark mode without JavaScript?","requirements"),
          ("How do you trigger animations on scroll without JavaScript libraries?","requirements")],
      assignments=["Complete the portfolio meeting all requirements.",
                   "Run Lighthouse and fix all issues until you score 90+ on performance and accessibility.",
                   "Deploy on GitHub Pages. Share the URL in your resume."],
      resources=[("Kevin Powell — Build a Portfolio","https://www.youtube.com/watch?v=_xkSvufmjEs"),
                 ("Netlify — Deploy in Seconds","https://www.netlify.com/"),
                 ("Intersection Observer API — MDN","https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API")])

    print(f"  Advanced HTML & CSS: {len(ALL)} lessons done")

def main():
    seed_advanced_html_css()
    print("\nCommitting...")
    os.chdir(BASE)
    subprocess.run(["git","add","-A"], check=True)
    subprocess.run(["git","commit","-m","Seed Advanced HTML & CSS (10 lessons)"], check=True)
    subprocess.run(["git","push"], check=True)
    print("Done.")

if __name__ == "__main__":
    main()
