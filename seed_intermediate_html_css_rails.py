#!/usr/bin/env python3
"""Intermediate HTML and CSS — Full Stack Ruby on Rails path"""
import os, subprocess

BASE  = os.path.expanduser("~/devpath")
IHCSS = os.path.join(BASE, "paths", "full-stack-ruby-on-rails", "courses")
ROOT  = "../../../../../"
LOGO  = '<svg viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="13" stroke="currentColor" stroke-width="1.8"/><path d="M8 14 L14 7 L20 14 L14 21 Z" fill="currentColor"/></svg>'


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
    esc = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<div class="code-block"><pre><code>{esc}</code></pre></div>'


def write(ldir, course_title, all_lessons, sidebar_html, slug,
          title, intro, overview, body, kc, assignments, resources):
    idx = next((i for i, l in enumerate(all_lessons) if l[0] == slug), None)
    p = (all_lessons[idx - 1][1], all_lessons[idx - 1][0] + ".html") if idx and idx > 0 else None
    n = (all_lessons[idx + 1][1], all_lessons[idx + 1][0] + ".html") if idx is not None and idx < len(all_lessons) - 1 else None
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
    ph = f'<a href="{p[1]}" class="pagination-link prev"><span class="pagination-label">&#8592; Previous</span><span class="pagination-title">{p[0]}</span></a>' if p else "<span></span>"
    nh = f'<a href="{n[1]}" class="pagination-link next"><span class="pagination-label">Next &#8594;</span><span class="pagination-title">{n[0]}</span></a>' if n else "<span></span>"
    html = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '  <meta charset="UTF-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
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


def seed_intermediate_html_css():
    ldir = os.path.join(IHCSS, "intermediate-html-css", "lessons")
    os.makedirs(ldir, exist_ok=True)

    ALL = [
        ("int-intro",                       "Introduction"),
        ("emmet",                            "Emmet"),
        ("svg",                              "SVG"),
        ("tables",                           "HTML Tables"),
        ("default-styles",                   "Default Styles"),
        ("css-units",                        "CSS Units"),
        ("more-text-styles",                 "More Text Styles"),
        ("more-css-properties",              "More CSS Properties"),
        ("advanced-selectors",               "Advanced Selectors"),
        ("positioning",                      "Positioning"),
        ("custom-properties",                "Custom Properties"),
        ("browser-compatibility",            "Browser Compatibility"),
        ("css-functions",                    "CSS Functions"),
        ("project-sign-up-form",             "Project: Sign-Up Form"),
        ("introduction-to-grid",             "Introduction to Grid"),
        ("creating-a-grid",                  "Creating a Grid"),
        ("positioning-grid-elements",        "Positioning Grid Elements"),
        ("advanced-grid-properties",         "Advanced Grid Properties"),
        ("using-flexbox-and-grid",           "Using Flexbox and Grid"),
        ("project-admin-dashboard",          "Project: Admin Dashboard"),
        ("introduction-to-responsive-design","Introduction to Responsive Design"),
        ("natural-responsiveness",           "Natural Responsiveness"),
        ("responsive-images",                "Responsive Images"),
        ("media-queries",                    "Media Queries"),
        ("project-homepage",                 "Project: Homepage"),
        ("intro-to-accessibility",           "Introduction to Web Accessibility"),
        ("the-web-content-accessibility-guidelines", "The Web Content Accessibility Guidelines"),
        ("accessible-colors",                "Accessible Colors"),
        ("meaningful-text",                  "Meaningful Text"),
        ("wai-aria",                         "WAI-ARIA"),
        ("keyboard-navigation",              "Keyboard Navigation"),
    ]

    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">Intermediate HTML and CSS</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">Introduction</div>'
        + lnk("int-intro", "Introduction")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Intermediate HTML</div>'
        + lnk("emmet", "Emmet")
        + lnk("svg", "SVG")
        + lnk("tables", "HTML Tables")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Intermediate CSS</div>'
        + lnk("default-styles", "Default Styles")
        + lnk("css-units", "CSS Units")
        + lnk("more-text-styles", "More Text Styles")
        + lnk("more-css-properties", "More CSS Properties")
        + lnk("advanced-selectors", "Advanced Selectors")
        + lnk("positioning", "Positioning")
        + lnk("custom-properties", "Custom Properties")
        + lnk("browser-compatibility", "Browser Compatibility")
        + lnk("css-functions", "CSS Functions")
        + lnk("project-sign-up-form", "Project: Sign-Up Form", True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Grid</div>'
        + lnk("introduction-to-grid", "Introduction to Grid")
        + lnk("creating-a-grid", "Creating a Grid")
        + lnk("positioning-grid-elements", "Positioning Grid Elements")
        + lnk("advanced-grid-properties", "Advanced Grid Properties")
        + lnk("using-flexbox-and-grid", "Using Flexbox and Grid")
        + lnk("project-admin-dashboard", "Project: Admin Dashboard", True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Responsive Design</div>'
        + lnk("introduction-to-responsive-design", "Introduction to Responsive Design")
        + lnk("natural-responsiveness", "Natural Responsiveness")
        + lnk("responsive-images", "Responsive Images")
        + lnk("media-queries", "Media Queries")
        + lnk("project-homepage", "Project: Homepage", True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Accessibility</div>'
        + lnk("intro-to-accessibility", "Introduction to Web Accessibility")
        + lnk("the-web-content-accessibility-guidelines", "WCAG")
        + lnk("accessible-colors", "Accessible Colors")
        + lnk("meaningful-text", "Meaningful Text")
        + lnk("wai-aria", "WAI-ARIA")
        + lnk("keyboard-navigation", "Keyboard Navigation")
        + '</div></aside>'
    )

    def w(slug, title, intro, overview, body, kc, assignments, resources):
        write(ldir, "Intermediate HTML and CSS", ALL, sidebar, slug, title, intro, overview, body, kc, assignments, resources)

    # ── 1. Introduction ──────────────────────────────────────────────────
    w("int-intro", "Introduction",
    intro="This course builds on the Foundations HTML and CSS you already know. You will learn the tools and techniques professional developers use every day — from Emmet shortcuts to CSS Grid, responsive design, and web accessibility.",
    overview=["Know what topics this course covers.", "Understand how this course fits into the Rails path.", "Set up your workspace for the lessons ahead."],
    body="""
<h2 class="lesson-section-title" id="what-this-course-covers">What This Course Covers</h2>
<p>Intermediate HTML and CSS is divided into four sections:</p>
<ul>
  <li><strong>Intermediate HTML</strong> — Emmet, SVG, and HTML tables.</li>
  <li><strong>Intermediate CSS</strong> — units, selectors, positioning, custom properties, browser compatibility, and CSS functions.</li>
  <li><strong>CSS Grid</strong> — the two-dimensional layout system that works alongside Flexbox.</li>
  <li><strong>Responsive Design and Accessibility</strong> — making sites work on every screen and for every user.</li>
</ul>
<p>By the end you will have built three portfolio-worthy projects: a Sign-Up Form, an Admin Dashboard, and a Homepage.</p>
""",
    kc=[("What are the four main sections of this course?", "what-this-course-covers")],
    assignments=["Review your Foundations HTML and CSS notes before starting.", "Make sure your code editor, browser DevTools, and Git are ready."],
    resources=[
        ("MDN — Learn Web Development", "https://developer.mozilla.org/en-US/docs/Learn"),
        ("web.dev — Learn CSS", "https://web.dev/learn/css/"),
    ])

    # ── 2. Emmet ─────────────────────────────────────────────────────────
    w("emmet", "Emmet",
    intro="Emmet is a plugin built into VS Code that lets you write HTML and CSS at lightning speed using short abbreviations that expand into full markup.",
    overview=["Use Emmet abbreviations to generate HTML boilerplate.", "Use child, sibling, and multiplication operators.", "Use Emmet for CSS shorthand.", "Customise Emmet settings in VS Code."],
    body="""
<h2 class="lesson-section-title" id="html-abbreviations">HTML Abbreviations</h2>
""" + code("""<!-- Type this, then press Tab -->
ul>li*5>a

<!-- Expands to -->
<ul>
  <li><a href=""></a></li>
  <li><a href=""></a></li>
  <li><a href=""></a></li>
  <li><a href=""></a></li>
  <li><a href=""></a></li>
</ul>
""") + """
<h2 class="lesson-section-title" id="operators">Operators</h2>
""" + code("""<!-- Child:  >  -->
nav>ul>li

<!-- Sibling:  +  -->
header+main+footer

<!-- Climb-up:  ^  -->
div>p^div    <!-- second div is sibling of first div, not child of p -->

<!-- Multiplication:  *  -->
ul>li*3

<!-- Grouping:  ()  -->
(header>nav)+(main>section*2)+footer

<!-- Numbering:  $  -->
ul>li.item$*3
<!-- produces: class="item1", class="item2", class="item3" -->

<!-- Text:  {}  -->
a{Click me}
p{Hello $}*3
""") + """
<h2 class="lesson-section-title" id="css-emmet">CSS Emmet</h2>
""" + code("""/* Type abbreviation + Tab in a CSS file */
m10        → margin: 10px;
p10-20     → padding: 10px 20px;
df         → display: flex;
jcc        → justify-content: center;
aic        → align-items: center;
w100p      → width: 100%;
bgc#fff    → background-color: #fff;
fz1.5rem   → font-size: 1.5rem;
"""),
    kc=[("What operator creates a child element in Emmet?", "operators"),
        ("How do you number repeated elements with Emmet?", "operators"),
        ("How do you add text content inside a tag with Emmet?", "operators")],
    assignments=["Practice the top 20 Emmet abbreviations until they are muscle memory.", "Re-create a previous project's HTML using only Emmet — no manual tag typing."],
    resources=[
        ("Emmet Cheat Sheet", "https://docs.emmet.io/cheat-sheet/"),
        ("VS Code Emmet Docs", "https://code.visualstudio.com/docs/editor/emmet"),
    ])

    # ── 3. SVG ───────────────────────────────────────────────────────────
    w("svg", "SVG",
    intro="SVG (Scalable Vector Graphics) is an XML-based image format that scales perfectly to any size. It is ideal for icons, logos, and illustrations used in web interfaces.",
    overview=["Understand what SVG is and why it is used on the web.", "Embed SVG inline, as an <img>, or as a CSS background.", "Use basic SVG shapes and attributes.", "Style SVG with CSS."],
    body="""
<h2 class="lesson-section-title" id="what-is-svg">What Is SVG?</h2>
<p>Unlike raster images (PNG, JPEG) that store pixel data, SVG stores geometric descriptions. A circle is literally <code>cx, cy, r</code> — coordinates and a radius. This means SVG looks crisp at any resolution, has tiny file sizes for simple shapes, and can be manipulated with CSS and JavaScript.</p>

<h2 class="lesson-section-title" id="embedding-svg">Embedding SVG</h2>
""" + code("""<!-- 1. Inline SVG — best for icons you need to style with CSS -->
<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2L2 7l10 5 10-5-10-5z" stroke="currentColor" stroke-width="2"/>
</svg>

<!-- 2. As an <img> — simple, cached, but can't style internals -->
<img src="icon.svg" alt="Menu icon" width="24" height="24">

<!-- 3. As CSS background — for decorative images -->
.hero {
  background-image: url('background.svg');
}
""") + """
<h2 class="lesson-section-title" id="basic-shapes">Basic Shapes and Attributes</h2>
""" + code("""<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <!-- Rectangle -->
  <rect x="10" y="10" width="80" height="50" rx="5" fill="#4f46e5"/>

  <!-- Circle -->
  <circle cx="150" cy="40" r="30" fill="#10b981"/>

  <!-- Line -->
  <line x1="10" y1="100" x2="190" y2="100" stroke="#6b7280" stroke-width="2"/>

  <!-- Polyline -->
  <polyline points="10,150 50,120 90,160 130,110 170,150"
            fill="none" stroke="#f59e0b" stroke-width="2"/>

  <!-- Path — most powerful; d= is the drawing instructions -->
  <path d="M10 180 Q100 140 190 180" fill="none" stroke="#ef4444" stroke-width="2"/>
</svg>
""") + """
<h2 class="lesson-section-title" id="styling-svg">Styling SVG with CSS</h2>
""" + code("""/* Inline SVG can use CSS like any HTML element */
svg {
  width: 2rem;
  height: 2rem;
}

/* currentColor inherits the parent's color — great for icon systems */
.icon {
  color: #4f46e5;   /* SVG strokes/fills using currentColor will pick this up */
}

/* Animate SVG with CSS */
circle {
  transition: r 0.3s ease;
}
circle:hover {
  r: 40;
}
"""),
    kc=[("What is the viewBox attribute in SVG?", "embedding-svg"),
        ("What does currentColor do in an SVG?", "styling-svg"),
        ("When would you use inline SVG vs an <img> tag?", "embedding-svg")],
    assignments=["Convert three PNG icons in a project to inline SVG.", "Create a simple SVG illustration using only basic shapes."],
    resources=[
        ("MDN — SVG Tutorial", "https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial"),
        ("SVG on the Web — Practical Guide", "https://svgontheweb.com/"),
        ("heroicons.com — Free SVG Icons", "https://heroicons.com/"),
    ])

    # ── 4. HTML Tables ───────────────────────────────────────────────────
    w("tables", "HTML Tables",
    intro="HTML tables are for displaying tabular data — information that has meaningful rows and columns. They are not for page layout. This lesson covers correct semantic table markup and CSS table styling.",
    overview=["Use <table>, <thead>, <tbody>, <tfoot>, <tr>, <th>, and <td> correctly.", "Span rows and columns with rowspan and colspan.", "Style tables with CSS.", "Understand when to use tables vs other layouts."],
    body="""
<h2 class="lesson-section-title" id="table-structure">Table Structure</h2>
""" + code("""<table>
  <caption>Q1 2024 Sales by Region</caption>
  <thead>
    <tr>
      <th scope="col">Region</th>
      <th scope="col">Jan</th>
      <th scope="col">Feb</th>
      <th scope="col">Mar</th>
      <th scope="col">Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">North</th>
      <td>$12,400</td>
      <td>$14,200</td>
      <td>$11,800</td>
      <td>$38,400</td>
    </tr>
    <tr>
      <th scope="row">South</th>
      <td>$9,800</td>
      <td>$10,500</td>
      <td>$13,200</td>
      <td>$33,500</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th scope="row">Total</th>
      <td>$22,200</td>
      <td>$24,700</td>
      <td>$25,000</td>
      <td>$71,900</td>
    </tr>
  </tfoot>
</table>
""") + """
<h2 class="lesson-section-title" id="spanning">Spanning Rows and Columns</h2>
""" + code("""<table>
  <tr>
    <th colspan="2">Name</th>      <!-- spans 2 columns -->
    <th>Age</th>
  </tr>
  <tr>
    <td>First</td>
    <td>Last</td>
    <td rowspan="2">28</td>        <!-- spans 2 rows -->
  </tr>
  <tr>
    <td>John</td>
    <td>Doe</td>
  </tr>
</table>
""") + """
<h2 class="lesson-section-title" id="css-tables">CSS Table Styling</h2>
""" + code("""table {
  width: 100%;
  border-collapse: collapse;   /* removes double borders */
  font-size: 0.9rem;
}

th, td {
  padding: 0.75rem 1rem;
  text-align: left;
  border-bottom: 1px solid #e5e7eb;
}

th {
  background-color: #f9fafb;
  font-weight: 600;
  color: #374151;
}

tbody tr:hover {
  background-color: #f3f4f6;
}

/* Zebra striping */
tbody tr:nth-child(even) {
  background-color: #f9fafb;
}
"""),
    kc=[("What is the difference between <th> and <td>?", "table-structure"),
        ("What does border-collapse: collapse do?", "css-tables"),
        ("What attributes span a cell across multiple rows or columns?", "spanning")],
    assignments=["Build a styled data table for a real dataset (sports stats, sales data, etc.).", "Make the table horizontally scrollable on mobile with overflow-x: auto."],
    resources=[
        ("MDN — HTML Tables", "https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables"),
        ("CSS-Tricks — Complete Guide to Tables", "https://css-tricks.com/complete-guide-table-element/"),
    ])

    # ── 5. Default Styles ────────────────────────────────────────────────
    w("default-styles", "Default Styles",
    intro="Every browser applies its own default stylesheet to HTML elements. Understanding these defaults — and how to reset or normalise them — is essential for consistent cross-browser design.",
    overview=["Understand what browser default styles are.", "Know the difference between a CSS reset and a normalise stylesheet.", "Use box-sizing: border-box globally.", "Use a modern minimal CSS reset."],
    body="""
<h2 class="lesson-section-title" id="browser-defaults">Browser Default Styles</h2>
<p>Browsers ship with a built-in stylesheet called the <em>user-agent stylesheet</em>. It gives headings their size, lists their bullets, links their blue underline, and so on. The problem is that every browser's defaults differ slightly, causing cross-browser inconsistencies.</p>

<h2 class="lesson-section-title" id="reset-vs-normalize">Reset vs Normalise</h2>
<p>A <strong>CSS reset</strong> strips all browser defaults to zero, giving you a blank slate. A <strong>normalise stylesheet</strong> instead makes defaults consistent across browsers without removing useful ones.</p>
""" + code("""/* ── Modern minimal reset (Andy Bell / Josh Comeau style) ── */

*, *::before, *::after {
  box-sizing: border-box;   /* padding and border included in width */
}

* {
  margin: 0;
}

body {
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}

input, button, textarea, select {
  font: inherit;
}

p, h1, h2, h3, h4, h5, h6 {
  overflow-wrap: break-word;
}
""") + """
<h2 class="lesson-section-title" id="box-sizing">Why box-sizing: border-box?</h2>
""" + code("""/* Default: content-box — width does NOT include padding/border */
.box {
  width: 200px;
  padding: 20px;
  /* actual rendered width: 240px (200 + 20 + 20) — surprising! */
}

/* border-box — width DOES include padding/border */
.box {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  /* actual rendered width: 200px — predictable */
}
"""),
    kc=[("What is the user-agent stylesheet?", "browser-defaults"),
        ("What is the difference between a reset and normalise?", "reset-vs-normalize"),
        ("Why is box-sizing: border-box preferred?", "box-sizing")],
    assignments=["Add a modern CSS reset to your current project.", "Inspect the user-agent styles for h1, p, and ul in DevTools."],
    resources=[
        ("Josh Comeau — CSS Reset", "https://www.joshwcomeau.com/css/custom-css-reset/"),
        ("Andy Bell — A Modern CSS Reset", "https://piccalil.li/blog/a-modern-css-reset/"),
        ("Normalise.css", "https://necolas.github.io/normalize.css/"),
    ])

    # ── 6. CSS Units ─────────────────────────────────────────────────────
    w("css-units", "CSS Units",
    intro="CSS has many units for expressing sizes — pixels, ems, rems, percentages, viewport units, and more. Knowing when to use each one is key to building robust, accessible layouts.",
    overview=["Know the difference between absolute and relative units.", "Use rem for font sizes and spacing.", "Use em for component-relative sizing.", "Use viewport units for full-screen layouts.", "Use ch and ex for typographic sizing."],
    body="""
<h2 class="lesson-section-title" id="absolute-units">Absolute Units</h2>
<p>Absolute units are fixed — they do not respond to user preferences or parent element sizes. <code>px</code> is the only one commonly used on screen.</p>
""" + code("""/* Absolute — avoid for font sizes */
.box {
  border: 1px solid black;   /* px fine for borders */
  width: 300px;              /* px fine for small fixed elements */
}
""") + """
<h2 class="lesson-section-title" id="relative-units">Relative Units</h2>
""" + code("""/* rem — relative to the ROOT font size (html element, usually 16px)
   Best for: font-size, margin, padding — anything that should scale with user preferences */
h1 { font-size: 2rem; }     /* 32px if root is 16px */
p  { font-size: 1rem; }     /* 16px */
.card { padding: 1.5rem; }  /* 24px */

/* em — relative to the CURRENT element's font size
   Best for: padding/margin that should scale with the element's own text */
button {
  font-size: 1rem;
  padding: 0.5em 1em;   /* padding is relative to button's font-size */
}

/* % — relative to the parent element
   Best for: widths in fluid layouts */
.sidebar { width: 30%; }
.main    { width: 70%; }

/* Viewport units */
.hero   { height: 100vh; }        /* 100% of viewport height */
.banner { width: 100vw; }         /* 100% of viewport width */
.text   { font-size: clamp(1rem, 2.5vw, 2rem); }  /* fluid type */

/* ch — width of the "0" character — great for line lengths */
p { max-width: 65ch; }   /* readable line length */
""") + """
<h2 class="lesson-section-title" id="when-to-use">When to Use Each Unit</h2>
<ul>
  <li><strong>rem</strong> — font sizes, spacing (margins, padding, gaps)</li>
  <li><strong>em</strong> — component-internal spacing that should scale with its own font size</li>
  <li><strong>px</strong> — borders, shadows, minimum sizes, media query breakpoints</li>
  <li><strong>%</strong> — widths in flex/grid children, positioning offsets</li>
  <li><strong>vh / vw</strong> — full-screen sections, viewport-relative sizes</li>
  <li><strong>ch</strong> — constraining line length for readability</li>
</ul>
""",
    kc=[("What is the difference between rem and em?", "relative-units"),
        ("Why should you avoid px for font sizes?", "relative-units"),
        ("What is ch and when would you use it?", "relative-units")],
    assignments=["Audit a project and replace all px font sizes with rem.", "Use max-width: 65ch on your body text paragraphs."],
    resources=[
        ("MDN — CSS Values and Units", "https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units"),
        ("Josh Comeau — The Surprising Truth About Pixels and Accessibility", "https://www.joshwcomeau.com/css/surprising-truth-about-pixels-and-accessibility/"),
    ])

    # ── 7. More Text Styles ──────────────────────────────────────────────
    w("more-text-styles", "More Text Styles",
    intro="Beyond font-size and color, CSS has a rich set of typographic properties for controlling letter spacing, line height, text decoration, font variants, and web font loading.",
    overview=["Use font-style, font-weight, and font-variant.", "Control letter-spacing, word-spacing, and line-height.", "Use text-transform and text-decoration.", "Load and use web fonts with @font-face and Google Fonts.", "Use system font stacks."],
    body="""
<h2 class="lesson-section-title" id="font-properties">Font Properties</h2>
""" + code("""p {
  font-style: italic;
  font-weight: 700;           /* or: bold, 100–900 */
  font-variant: small-caps;
  font-stretch: condensed;
}

/* Shorthand: style weight size/line-height family */
p {
  font: italic 700 1.125rem/1.6 'Inter', sans-serif;
}
""") + """
<h2 class="lesson-section-title" id="spacing-and-decoration">Spacing and Decoration</h2>
""" + code("""h1 {
  letter-spacing: -0.02em;    /* tighten headings */
  word-spacing: 0.05em;
  line-height: 1.2;           /* unitless — scales with font size */
  text-transform: uppercase;
  text-decoration: underline wavy #ef4444;
  text-indent: 2rem;
}

/* Text shadow */
h2 {
  text-shadow: 1px 1px 2px rgba(0,0,0,0.15);
}

/* Overflow handling */
.truncate {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
""") + """
<h2 class="lesson-section-title" id="web-fonts">Web Fonts</h2>
""" + code("""/* Google Fonts — simplest approach */
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

/* @font-face — self-hosted fonts */
@font-face {
  font-family: 'MyFont';
  src: url('/fonts/myfont.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;    /* show fallback immediately, swap when loaded */
}

/* System font stack — no network request, fast, native feel */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
               Oxygen, Ubuntu, sans-serif;
}
"""),
    kc=[("What does line-height: 1.5 mean — 1.5 what?", "font-properties"),
        ("What does font-display: swap do?", "web-fonts"),
        ("What is the benefit of a system font stack?", "web-fonts")],
    assignments=["Add a Google Font to a project and apply it with a proper fallback stack.", "Style a blog post with optimal typography: line-height, max-width, letter-spacing."],
    resources=[
        ("MDN — Fundamental Text and Font Styling", "https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals"),
        ("Google Fonts", "https://fonts.google.com/"),
        ("Modern Font Stacks", "https://modernfontstacks.com/"),
    ])

    # ── 8. More CSS Properties ───────────────────────────────────────────
    w("more-css-properties", "More CSS Properties",
    intro="This lesson covers CSS properties that are extremely useful in practice but often overlooked: background shorthand, borders, shadows, overflow, opacity, and the all-important filter.",
    overview=["Use the background shorthand fully.", "Apply box-shadow and text-shadow effectively.", "Control overflow behaviour.", "Use opacity and visibility.", "Apply CSS filters."],
    body="""
<h2 class="lesson-section-title" id="background">Background</h2>
""" + code("""/* Shorthand: color image repeat position / size attachment */
.hero {
  background: #1e1b4b url('/img/pattern.svg') no-repeat center / cover fixed;
}

/* Multiple backgrounds (layered, first = top) */
.card {
  background:
    linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
    url('/img/photo.jpg') center / cover;
}

/* Gradients */
.btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
.donut {
  background: conic-gradient(#4f46e5 0% 25%, #e5e7eb 25% 100%);
}
""") + """
<h2 class="lesson-section-title" id="shadows">Shadows</h2>
""" + code("""/* box-shadow: offset-x offset-y blur spread color */
.card {
  box-shadow:
    0 1px 3px rgba(0,0,0,0.12),
    0 1px 2px rgba(0,0,0,0.08);
}

/* Inset shadow */
.input:focus {
  box-shadow: inset 0 0 0 2px #4f46e5;
}

/* Multiple shadows */
.elevated {
  box-shadow:
    0 4px 6px -1px rgba(0,0,0,0.1),
    0 2px 4px -1px rgba(0,0,0,0.06);
}
""") + """
<h2 class="lesson-section-title" id="overflow-opacity-filter">Overflow, Opacity, and Filter</h2>
""" + code("""/* overflow */
.scroll-area  { overflow: auto; }
.no-scroll    { overflow: hidden; }
.x-scroll     { overflow-x: auto; overflow-y: hidden; }

/* opacity vs visibility */
.hidden-but-space  { visibility: hidden; }  /* hidden, keeps space */
.faded             { opacity: 0.5; }        /* semi-transparent */
.gone              { display: none; }       /* removed from layout */

/* CSS filters */
.grayscale { filter: grayscale(100%); }
.blur      { filter: blur(4px); }
.darken    { filter: brightness(0.7); }

/* backdrop-filter — blurs content behind an element */
.glass-card {
  background: rgba(255,255,255,0.15);
  backdrop-filter: blur(12px);
}
"""),
    kc=[("What is the difference between opacity: 0 and visibility: hidden?", "overflow-opacity-filter"),
        ("What does backdrop-filter do?", "overflow-opacity-filter"),
        ("How do you layer multiple backgrounds?", "background")],
    assignments=["Create a glass-morphism card using backdrop-filter.", "Build a photo card with a gradient overlay on a background image."],
    resources=[
        ("MDN — background", "https://developer.mozilla.org/en-US/docs/Web/CSS/background"),
        ("MDN — filter", "https://developer.mozilla.org/en-US/docs/Web/CSS/filter"),
        ("CSS-Tricks — box-shadow", "https://css-tricks.com/almanac/properties/b/box-shadow/"),
    ])

    # ── 9. Advanced Selectors ────────────────────────────────────────────
    w("advanced-selectors", "Advanced Selectors",
    intro="CSS has a rich set of selectors beyond classes and IDs. Mastering attribute selectors, pseudo-classes, pseudo-elements, and combinators lets you write cleaner, more specific CSS without cluttering your HTML.",
    overview=["Use attribute selectors.", "Use structural pseudo-classes like :nth-child and :not.", "Use pseudo-elements ::before and ::after.", "Understand selector specificity.", "Use the :is(), :where(), and :has() selectors."],
    body="""
<h2 class="lesson-section-title" id="attribute-selectors">Attribute Selectors</h2>
""" + code("""/* Element has the attribute */
[disabled] { opacity: 0.5; }

/* Exact attribute value */
[type="submit"] { background: #4f46e5; }

/* Attribute starts with */
a[href^="https"] { color: green; }

/* Attribute ends with */
a[href$=".pdf"]::after { content: " (PDF)"; }

/* Attribute contains */
[class*="btn"] { cursor: pointer; }
""") + """
<h2 class="lesson-section-title" id="pseudo-classes">Pseudo-Classes</h2>
""" + code("""/* Structural */
li:first-child   { font-weight: bold; }
li:last-child    { border-bottom: none; }
li:nth-child(2n) { background: #f9fafb; }   /* even rows */
li:nth-child(3n+1) { color: red; }          /* every 3rd starting at 1 */

/* Negation */
input:not([type="checkbox"]):not([type="radio"]) {
  border: 1px solid #d1d5db;
}

/* State */
a:hover, a:focus { text-decoration: underline; }
input:focus-visible { outline: 2px solid #4f46e5; }
input:invalid { border-color: #ef4444; }
details:open summary { font-weight: bold; }

/* Modern: :is() and :where() */
:is(h1, h2, h3, h4) { line-height: 1.2; }   /* specificity = highest arg */
:where(h1, h2, h3)  { margin-block: 1em; }   /* specificity = 0 always */

/* :has() — parent selector! */
.card:has(img) { padding-top: 0; }           /* card that contains an img */
form:has(input:invalid) .submit-btn { opacity: 0.5; }
""") + """
<h2 class="lesson-section-title" id="pseudo-elements">Pseudo-Elements</h2>
""" + code("""/* ::before and ::after — generated content */
.required-label::after {
  content: " *";
  color: #ef4444;
}

blockquote::before {
  content: '"';
  font-size: 4rem;
  color: #d1d5db;
  line-height: 0;
  vertical-align: -0.4em;
}

/* ::first-line and ::first-letter */
p::first-letter {
  font-size: 3em;
  float: left;
  line-height: 1;
  margin-right: 0.1em;
}

/* ::placeholder */
input::placeholder { color: #9ca3af; font-style: italic; }

/* ::selection */
::selection { background: #ddd6fe; color: #1e1b4b; }
"""),
    kc=[("What does the * attribute selector check for?", "attribute-selectors"),
        ("What is the difference between :is() and :where()?", "pseudo-classes"),
        ("What does :has() allow you to do that was previously impossible?", "pseudo-classes")],
    assignments=["Style all external links differently using attribute selectors.", "Build a striped table using only :nth-child — no extra classes.", "Create a custom bullet list using ::before pseudo-elements."],
    resources=[
        ("MDN — CSS Selectors", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors"),
        ("CSS-Tricks — :has()", "https://css-tricks.com/the-css-has-selector/"),
        ("Specificity Calculator", "https://specificity.keegan.st/"),
    ])

    # ── 10. Positioning ──────────────────────────────────────────────────
    w("positioning", "Positioning",
    intro="CSS positioning takes elements out of normal document flow or adjusts their placement. Understanding static, relative, absolute, fixed, and sticky positioning is essential for building real interfaces.",
    overview=["Understand the five position values.", "Use relative and absolute positioning together.", "Use fixed positioning for persistent UI elements.", "Use sticky positioning for scroll-aware headers.", "Understand z-index and stacking contexts."],
    body="""
<h2 class="lesson-section-title" id="position-values">Position Values</h2>
""" + code("""/* static — default, normal flow, top/left/etc. have no effect */
.normal { position: static; }

/* relative — stays in flow, offsets are from its own original position */
.nudged { position: relative; top: 10px; left: 5px; }

/* absolute — removed from flow, positioned relative to nearest
   positioned ancestor (any position other than static) */
.badge {
  position: absolute;
  top: -0.5rem;
  right: -0.5rem;
}

/* fixed — removed from flow, positioned relative to the VIEWPORT,
   stays on screen when you scroll */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
}

/* sticky — stays in flow until it hits the threshold, then sticks */
.table-header {
  position: sticky;
  top: 0;         /* sticks when it reaches 0px from the top */
  background: white;
}
""") + """
<h2 class="lesson-section-title" id="absolute-patterns">Common Absolute Positioning Patterns</h2>
""" + code("""/* Centre a child inside a parent */
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

/* Stretch to fill parent */
.overlay {
  position: absolute;
  inset: 0;   /* shorthand for top/right/bottom/left: 0 */
}
""") + """
<h2 class="lesson-section-title" id="z-index">z-index and Stacking Contexts</h2>
""" + code("""/* z-index only works on positioned elements (not static) */
.modal-overlay { position: fixed; z-index: 100; }
.modal-content { position: relative; z-index: 101; }

/* A stacking context is created by:
   - position + z-index (not auto)
   - opacity < 1
   - transform, filter, will-change
   Elements inside a stacking context are painted together */
"""),
    kc=[("What is the difference between fixed and sticky positioning?", "position-values"),
        ("What does an element need to be positioned relative to for absolute children to work?", "absolute-patterns"),
        ("What creates a new stacking context?", "z-index")],
    assignments=["Build a card with an absolutely positioned badge in its corner.", "Create a sticky table header that stays visible while scrolling.", "Build a modal overlay with a centred dialog using fixed + absolute positioning."],
    resources=[
        ("MDN — position", "https://developer.mozilla.org/en-US/docs/Web/CSS/position"),
        ("CSS-Tricks — position", "https://css-tricks.com/almanac/properties/p/position/"),
        ("Josh Comeau — What the Heck is z-index?", "https://www.joshwcomeau.com/css/stacking-contexts/"),
    ])

    # ── 11. Custom Properties ────────────────────────────────────────────
    w("custom-properties", "Custom Properties",
    intro="CSS custom properties (CSS variables) let you store values in named variables and reuse them throughout your stylesheet. They are the foundation of design tokens and theming.",
    overview=["Define and use CSS custom properties.", "Understand scope and inheritance.", "Build a colour theme with custom properties.", "Implement a dark mode toggle.", "Use custom properties with calc()."],
    body="""
<h2 class="lesson-section-title" id="defining-variables">Defining and Using Variables</h2>
""" + code("""/* Define on :root to make globally available */
:root {
  --color-primary: #4f46e5;
  --color-primary-dark: #3730a3;
  --color-text: #111827;
  --color-bg: #ffffff;
  --font-sans: 'Inter', system-ui, sans-serif;
  --radius: 0.5rem;
  --shadow: 0 1px 3px rgba(0,0,0,0.12);

  /* Spacing scale */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --space-8: 2rem;
}

/* Use with var() */
.btn {
  background-color: var(--color-primary);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: var(--space-2) var(--space-4);
  font-family: var(--font-sans);
}

/* Fallback value */
color: var(--color-accent, #10b981);
""") + """
<h2 class="lesson-section-title" id="dark-mode">Dark Mode with Custom Properties</h2>
""" + code(""":root {
  --color-bg: #ffffff;
  --color-text: #111827;
  --color-surface: #f9fafb;
}

[data-theme="dark"] {
  --color-bg: #111827;
  --color-text: #f9fafb;
  --color-surface: #1f2937;
}

/* All components automatically pick up the right values */
body {
  background-color: var(--color-bg);
  color: var(--color-text);
}
""") + code("""// Toggle dark mode with one line of JS
document.documentElement.dataset.theme =
  document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
""") + """
<h2 class="lesson-section-title" id="calc-with-variables">Using calc() with Variables</h2>
""" + code(""":root {
  --base-size: 1rem;
  --scale: 1.25;
}

h3 { font-size: calc(var(--base-size) * var(--scale)); }
h2 { font-size: calc(var(--base-size) * var(--scale) * var(--scale)); }
h1 { font-size: calc(var(--base-size) * var(--scale) * var(--scale) * var(--scale)); }
"""),
    kc=[("What is the difference between CSS custom properties and Sass variables?", "defining-variables"),
        ("How do you implement dark mode using custom properties?", "dark-mode"),
        ("What does var(--color, fallback) do when --color is not defined?", "defining-variables")],
    assignments=["Refactor a project to use a full design token system with custom properties.", "Implement a dark mode toggle that persists using localStorage."],
    resources=[
        ("MDN — CSS Custom Properties", "https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties"),
        ("web.dev — CSS Custom Properties", "https://web.dev/articles/css-variables"),
    ])

    # ── 12. Browser Compatibility ─────────────────────────────────────────
    w("browser-compatibility", "Browser Compatibility",
    intro="Not all CSS features are supported in all browsers. This lesson covers how to check compatibility, use feature queries, set up PostCSS, and write CSS that degrades gracefully.",
    overview=["Use Can I Use to check browser support.", "Use @supports feature queries.", "Understand vendor prefixes.", "Set up PostCSS and Autoprefixer.", "Write progressively enhanced CSS."],
    body="""
<h2 class="lesson-section-title" id="checking-support">Checking Browser Support</h2>
<p><a href="https://caniuse.com" target="_blank" rel="noopener">caniuse.com</a> shows exactly which browsers support which features, with version-level detail. MDN's compatibility tables are equally useful and updated continuously.</p>

<h2 class="lesson-section-title" id="feature-queries">@supports Feature Queries</h2>
""" + code("""/* Apply styles only if the browser supports the feature */
@supports (display: grid) {
  .layout { display: grid; grid-template-columns: 1fr 1fr; }
}

/* Negation — fallback for browsers that DON'T support something */
@supports not (backdrop-filter: blur(1px)) {
  .glass { background: rgba(255,255,255,0.9); }
}

/* Combining conditions */
@supports (display: grid) and (gap: 1rem) {
  .grid { display: grid; gap: 1rem; }
}
""") + """
<h2 class="lesson-section-title" id="progressive-enhancement">Progressive Enhancement</h2>
""" + code("""/* Write the baseline first, then enhance */

/* Step 1: Baseline — works everywhere */
.layout {
  display: flex;
  flex-wrap: wrap;
}

/* Step 2: Enhancement — modern browsers only */
@supports (display: grid) {
  .layout {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }
}

/* Vendor prefixes — Autoprefixer handles these automatically */
.element {
  -webkit-transform: rotate(45deg);   /* old WebKit */
          transform: rotate(45deg);   /* standard */
}
"""),
    kc=[("What does @supports do?", "feature-queries"),
        ("What is progressive enhancement?", "progressive-enhancement"),
        ("What tool automatically adds vendor prefixes?", "progressive-enhancement")],
    assignments=["Check the caniuse support for CSS Grid and :has() — what is the current support?", "Add an @supports fallback to a feature you use that has less than 95% global support."],
    resources=[
        ("Can I Use", "https://caniuse.com/"),
        ("MDN — @supports", "https://developer.mozilla.org/en-US/docs/Web/CSS/@supports"),
        ("Autoprefixer", "https://autoprefixer.github.io/"),
    ])

    # ── 13. CSS Functions ────────────────────────────────────────────────
    w("css-functions", "CSS Functions",
    intro="CSS has a growing library of built-in functions for maths, colours, sizing, and layout. calc(), clamp(), min(), max(), and color functions unlock powerful, responsive design without JavaScript.",
    overview=["Use calc() for mathematical expressions.", "Use min(), max(), and clamp() for responsive sizing.", "Use CSS colour functions.", "Use env() for safe-area insets."],
    body="""
<h2 class="lesson-section-title" id="calc">calc()</h2>
""" + code("""/* Mix units freely */
.sidebar {
  width: calc(300px - 2rem);
}

.full-minus-nav {
  height: calc(100vh - 64px);   /* full height minus navbar */
}

/* Use with custom properties */
.grid {
  gap: calc(var(--space-4) * 1.5);
}
""") + """
<h2 class="lesson-section-title" id="min-max-clamp">min(), max(), and clamp()</h2>
""" + code("""/* min() — uses the smallest value (prevents growing too large) */
.container {
  width: min(100%, 1200px);   /* fluid until 1200px, then fixed */
}

/* max() — uses the largest value (ensures minimum size) */
.btn {
  padding: max(0.5rem, 2vw);  /* at least 0.5rem, more on wide screens */
}

/* clamp(min, preferred, max) — the fluid type workhorse */
h1 {
  font-size: clamp(1.75rem, 4vw + 1rem, 3.5rem);
  /* never smaller than 1.75rem, never larger than 3.5rem,
     scales fluidly with viewport in between */
}

.container {
  width: clamp(320px, 90%, 1200px);
}
""") + """
<h2 class="lesson-section-title" id="color-functions">Colour Functions</h2>
""" + code("""/* Modern colour with oklch — perceptually uniform */
:root {
  --color-primary: oklch(55% 0.2 264);
}

/* hsl — easy to reason about */
.btn {
  background: hsl(245, 75%, 58%);
}
.btn:hover {
  background: hsl(245, 75%, 48%);   /* just darken the lightness */
}

/* color-mix() — mix two colours */
.muted {
  color: color-mix(in srgb, var(--color-primary) 20%, white);
}
"""),
    kc=[("What does clamp(min, preferred, max) do?", "min-max-clamp"),
        ("How is min() different from clamp()?", "min-max-clamp"),
        ("What advantage does oklch have over hsl?", "color-functions")],
    assignments=["Use clamp() for all heading font sizes in a project.", "Replace a fixed max-width with min(100%, 1200px)."],
    resources=[
        ("MDN — calc()", "https://developer.mozilla.org/en-US/docs/Web/CSS/calc"),
        ("MDN — clamp()", "https://developer.mozilla.org/en-US/docs/Web/CSS/clamp"),
        ("web.dev — CSS Color Functions", "https://web.dev/articles/css-color-functions"),
    ])

    # ── 14. Project: Sign-Up Form ─────────────────────────────────────────
    w("project-sign-up-form", "Project: Sign-Up Form",
    intro="Build a beautiful sign-up form that demonstrates everything you have learned so far in the Intermediate CSS section: custom properties, positioning, advanced selectors, and more.",
    overview=["Build a multi-field registration form.", "Style form inputs with focus states and validation feedback.", "Use a split-layout with an image panel and form panel.", "Apply your CSS reset and custom property system."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>A split-screen layout: decorative image/brand panel on the left, form on the right</li>
  <li>Fields: first name, last name, email, phone, password, confirm password</li>
  <li>A logo or branding element overlaid on the image panel</li>
  <li>Custom-styled inputs with :focus-visible outlines</li>
  <li>Password mismatch shown with :invalid CSS (no JS required)</li>
  <li>Submit button with hover and active states</li>
  <li>Fully responsive — stacks to single column on mobile</li>
</ul>
""" + code("""/* Suggested layout structure */
<div class="wrapper">
  <div class="image-panel">
    <div class="logo">DevPath</div>
  </div>
  <div class="form-panel">
    <h1>Create Account</h1>
    <form>
      <div class="field-row">
        <label>First Name <input type="text" required></label>
        <label>Last Name  <input type="text" required></label>
      </div>
      <!-- more fields -->
      <button type="submit">Create Account</button>
      <p>Already have an account? <a href="#">Log in</a></p>
    </form>
  </div>
</div>
"""),
    kc=[("How do you show validation styles without JavaScript?", "requirements"),
        ("How do you create a split-screen layout?", "requirements")],
    assignments=["Complete the Sign-Up Form meeting all requirements.", "Push to GitHub Pages and share the live URL."],
    resources=[
        ("MDN — HTML Forms", "https://developer.mozilla.org/en-US/docs/Learn/Forms"),
        ("web.dev — Learn Forms", "https://web.dev/learn/forms/"),
    ])

    # ── 15. Introduction to Grid ──────────────────────────────────────────
    w("introduction-to-grid", "Introduction to Grid",
    intro="CSS Grid is a two-dimensional layout system that lets you control both rows and columns simultaneously. It solves layout problems that were extremely difficult or impossible with Flexbox alone.",
    overview=["Understand what CSS Grid is and when to use it.", "Define a grid with grid-template-columns and grid-template-rows.", "Place items with grid-column and grid-row.", "Understand the difference between Grid and Flexbox."],
    body="""
<h2 class="lesson-section-title" id="grid-vs-flexbox">Grid vs Flexbox</h2>
<p>Flexbox is <strong>one-dimensional</strong> — it lays items out in a row OR a column. Grid is <strong>two-dimensional</strong> — it controls rows AND columns simultaneously. A common rule: use Flexbox for components (navigation, button groups, cards in a row), use Grid for page layouts and two-dimensional designs.</p>

<h2 class="lesson-section-title" id="defining-a-grid">Defining a Grid</h2>
""" + code(""".container {
  display: grid;

  /* Three equal columns */
  grid-template-columns: 1fr 1fr 1fr;

  /* Or with repeat() */
  grid-template-columns: repeat(3, 1fr);

  /* Mixed column sizes */
  grid-template-columns: 250px 1fr 1fr;

  /* Three rows, 100px each */
  grid-template-rows: repeat(3, 100px);

  /* Gap between cells */
  gap: 1rem;                /* row-gap and column-gap */
  row-gap: 1.5rem;
  column-gap: 1rem;
}
""") + """
<h2 class="lesson-section-title" id="placing-items">Placing Items</h2>
""" + code("""/* grid-column: start / end (line numbers, 1-indexed) */
.header {
  grid-column: 1 / 4;    /* spans all 3 columns */
  /* shorthand: grid-column: 1 / -1 (to the last line) */
}

.sidebar {
  grid-column: 1 / 2;
  grid-row: 2 / 4;       /* spans 2 rows */
}

.main {
  grid-column: 2 / 4;
  grid-row: 2 / 3;
}

/* span keyword — more readable */
.featured {
  grid-column: span 2;   /* spans 2 columns from wherever it is */
  grid-row: span 2;
}
"""),
    kc=[("When should you use Grid instead of Flexbox?", "grid-vs-flexbox"),
        ("What does 1fr mean?", "defining-a-grid"),
        ("What is the difference between grid-column: 1/4 and span 3?", "placing-items")],
    assignments=["Build a basic page layout (header, sidebar, main, footer) with CSS Grid.", "Inspect an existing Grid layout in DevTools — turn on the Grid overlay."],
    resources=[
        ("CSS-Tricks — Complete Guide to CSS Grid", "https://css-tricks.com/snippets/css/complete-guide-grid/"),
        ("Grid Garden — Learn Grid interactively", "https://cssgridgarden.com/"),
        ("MDN — CSS Grid Layout", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout"),
    ])

    # ── 16. Creating a Grid ───────────────────────────────────────────────
    w("creating-a-grid", "Creating a Grid",
    intro="This lesson goes deeper into grid definition — using grid-template-areas for named layouts, the minmax() function for flexible tracks, and auto-fill / auto-fit for responsive grids without media queries.",
    overview=["Use grid-template-areas for named, visual layouts.", "Use minmax() for flexible track sizes.", "Use auto-fill and auto-fit for responsive grids.", "Understand implicit vs explicit grid tracks."],
    body="""
<h2 class="lesson-section-title" id="template-areas">grid-template-areas</h2>
""" + code(""".page {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header  header"
    "sidebar main"
    "footer  footer";
  min-height: 100vh;
}

.site-header  { grid-area: header; }
.site-sidebar { grid-area: sidebar; }
.site-main    { grid-area: main; }
.site-footer  { grid-area: footer; }

/* Responsive: collapse to single column */
@media (max-width: 768px) {
  .page {
    grid-template-columns: 1fr;
    grid-template-areas:
      "header"
      "main"
      "sidebar"
      "footer";
  }
}
""") + """
<h2 class="lesson-section-title" id="minmax-autofit">minmax(), auto-fill, and auto-fit</h2>
""" + code("""/* minmax(min, max) — track must be at least min, at most max */
.grid {
  grid-template-columns: repeat(3, minmax(200px, 1fr));
}

/* auto-fill — creates as many tracks as fit, keeps empty tracks */
.gallery {
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
}

/* auto-fit — creates as many tracks as fit, collapses empty tracks
   (items stretch to fill the row) */
.cards {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

/* The magic responsive grid — no media queries! */
.responsive-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));
  gap: 1.5rem;
}
""") + """
<h2 class="lesson-section-title" id="implicit-grid">Implicit Grid</h2>
""" + code(""".grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  /* Only defined columns — rows are created implicitly */

  /* Control the size of implicit rows */
  grid-auto-rows: minmax(100px, auto);

  /* Control the flow direction */
  grid-auto-flow: dense;  /* fills gaps with smaller items */
}
"""),
    kc=[("What does grid-template-areas let you do?", "template-areas"),
        ("What is the difference between auto-fill and auto-fit?", "minmax-autofit"),
        ("What is the implicit grid?", "implicit-grid")],
    assignments=["Build a full page layout using grid-template-areas.", "Build a responsive card grid using auto-fit and minmax — no media queries."],
    resources=[
        ("MDN — grid-template-areas", "https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas"),
        ("CSS-Tricks — auto-fill vs auto-fit", "https://css-tricks.com/auto-sizing-columns-css-grid-auto-fill-vs-auto-fit/"),
    ])

    # ── 17. Positioning Grid Elements ────────────────────────────────────
    w("positioning-grid-elements", "Positioning Grid Elements",
    intro="Once a grid is defined, you have precise control over where each item lands — spanning multiple cells, aligning within a cell, and layering items on top of each other.",
    overview=["Place items precisely with line numbers.", "Align and justify grid items and tracks.", "Layer items in the same grid cells.", "Use grid-area shorthand."],
    body="""
<h2 class="lesson-section-title" id="alignment">Alignment in Grid</h2>
""" + code("""/* Align ALL items within their cells */
.grid {
  align-items: center;      /* vertical alignment (start|center|end|stretch) */
  justify-items: start;     /* horizontal alignment */

  /* Align the entire grid within its container */
  align-content: center;
  justify-content: space-between;

  /* Shorthand: place-items: align / justify */
  place-items: center start;
}

/* Align a SINGLE item */
.special {
  align-self: end;
  justify-self: center;
  /* shorthand */
  place-self: end center;
}
""") + """
<h2 class="lesson-section-title" id="layering">Layering Grid Items</h2>
""" + code("""/* Multiple items can occupy the same grid cells — use z-index to control order */
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 300px;
}

.background-image {
  grid-column: 1 / -1;
  grid-row: 1;
  z-index: 1;
}

.overlay-text {
  grid-column: 1 / -1;
  grid-row: 1;              /* same cell as background! */
  z-index: 2;
  place-self: center;
}
""") + """
<h2 class="lesson-section-title" id="grid-area-shorthand">grid-area Shorthand</h2>
""" + code("""/* grid-area: row-start / col-start / row-end / col-end */
.item {
  grid-area: 1 / 2 / 3 / 4;
  /* same as:
     grid-row: 1 / 3;
     grid-column: 2 / 4;
  */
}
"""),
    kc=[("What is the difference between align-items and align-content in Grid?", "alignment"),
        ("How do you place two items in the same grid cell?", "layering"),
        ("What does grid-area: 1/1/3/4 mean?", "grid-area-shorthand")],
    assignments=["Build a magazine-style layout where a hero image spans across multiple grid cells.", "Create a photo mosaic layout with items of different sizes using explicit line placement."],
    resources=[
        ("MDN — Box alignment in CSS Grid", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Box_alignment_in_grid_layout"),
    ])

    # ── 18. Advanced Grid Properties ──────────────────────────────────────
    w("advanced-grid-properties", "Advanced Grid Properties",
    intro="This lesson covers the advanced Grid features used in production: subgrid for nested grid alignment, grid shorthand, and masonry-style layouts.",
    overview=["Use the grid shorthand property.", "Use subgrid to align nested grids.", "Understand grid-auto-flow: dense.", "Build a masonry-style layout."],
    body="""
<h2 class="lesson-section-title" id="grid-shorthand">grid Shorthand</h2>
""" + code("""/* grid: rows / columns */
.layout {
  grid: auto 1fr auto / 250px 1fr;
  /* same as:
     grid-template-rows: auto 1fr auto;
     grid-template-columns: 250px 1fr;
  */
}

/* With template areas */
.page {
  grid:
    "header header" auto
    "sidebar main"  1fr
    "footer footer" auto
    / 250px 1fr;
}
""") + """
<h2 class="lesson-section-title" id="subgrid">subgrid</h2>
""" + code("""/* Problem: nested grids don't align with the outer grid */
/* Solution: subgrid — child inherits parent's track definitions */

.outer-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.card {
  display: grid;
  /* Use the outer grid's column tracks inside the card */
  grid-column: span 1;
  grid-template-rows: subgrid;
  /* or: grid-template-columns: subgrid; */
  grid-row: span 3;  /* card spans 3 rows of the outer grid */
}

/* Now all card internals (image, title, body) line up across cards */
.card-image  { grid-row: 1; }
.card-title  { grid-row: 2; }
.card-body   { grid-row: 3; }
""") + """
<h2 class="lesson-section-title" id="dense-packing">Dense Packing</h2>
""" + code("""/* grid-auto-flow: dense fills gaps left by larger items */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  grid-auto-rows: 150px;
  grid-auto-flow: dense;
}

.tall  { grid-row: span 2; }
.wide  { grid-column: span 2; }
.large { grid-column: span 2; grid-row: span 2; }
"""),
    kc=[("What problem does subgrid solve?", "subgrid"),
        ("What does grid-auto-flow: dense do?", "dense-packing"),
        ("Write the grid shorthand for a 3-row, 2-column layout.", "grid-shorthand")],
    assignments=["Build a card grid where all card titles align using subgrid.", "Build a Pinterest-style gallery using auto-fill and dense packing."],
    resources=[
        ("MDN — subgrid", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Subgrid"),
        ("CSS-Tricks — Complete Guide to CSS Grid", "https://css-tricks.com/snippets/css/complete-guide-grid/"),
    ])

    # ── 19. Using Flexbox and Grid Together ───────────────────────────────
    w("using-flexbox-and-grid", "Using Flexbox and Grid",
    intro="Flexbox and Grid are complementary, not competing. This lesson covers the mental model for choosing between them and how to combine them effectively in real layouts.",
    overview=["Know when to use Flexbox vs Grid.", "Combine Grid for layout and Flexbox for components.", "Avoid common layout mistakes.", "Build a full-page layout using both."],
    body="""
<h2 class="lesson-section-title" id="mental-model">The Mental Model</h2>
<ul>
  <li><strong>Use Grid</strong> when you need to control both rows and columns, when layout comes first (you design the grid then place items), or for page-level layout.</li>
  <li><strong>Use Flexbox</strong> when you need to distribute items along a single axis, when content drives the size (items are as big as they need to be), or for components like navbars, button groups, form rows, and media objects.</li>
</ul>

<h2 class="lesson-section-title" id="combining">Combining Both</h2>
""" + code("""/* Page layout → Grid */
.page {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "footer";
  min-height: 100vh;
  grid-template-rows: auto 1fr auto;
}

/* Navbar inside header → Flexbox */
.site-header {
  grid-area: header;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
}

/* Card grid inside main → Grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  padding: 2rem;
}

/* Individual card → Flexbox (column direction) */
.card {
  display: flex;
  flex-direction: column;
}

.card-body {
  flex: 1;   /* pushes the button to the bottom */
}
"""),
    kc=[("In one sentence, when do you choose Grid over Flexbox?", "mental-model"),
        ("Why would you use Flexbox inside a Grid layout?", "combining"),
        ("How do you push a button to the bottom of a card with Flexbox?", "combining")],
    assignments=["Rebuild a past project's layout using Grid for structure and Flexbox for components.", "Identify 5 places in a real website where Grid is used and 5 where Flexbox is used."],
    resources=[
        ("web.dev — CSS Grid vs Flexbox", "https://web.dev/articles/css-grid"),
        ("CSS-Tricks — Does CSS Grid Replace Flexbox?", "https://css-tricks.com/css-grid-replace-flexbox/"),
    ])

    # ── 20. Project: Admin Dashboard ─────────────────────────────────────
    w("project-admin-dashboard", "Project: Admin Dashboard",
    intro="Build a full admin dashboard UI using CSS Grid for the layout and Flexbox for the internal components. This is a portfolio-worthy project that demonstrates mastery of both layout systems.",
    overview=["Build a sidebar + header + main content layout with Grid.", "Create stat cards, recent activity, and trending sections.", "Use Flexbox within each component.", "Make the layout responsive."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>Layout</strong>: fixed sidebar on the left, header at the top, main content area filling the rest — all with CSS Grid</li>
  <li><strong>Sidebar</strong>: logo, navigation links with icons, branding at bottom</li>
  <li><strong>Header</strong>: search bar, notification bell, user avatar — use Flexbox</li>
  <li><strong>Projects section</strong>: grid of project cards with action buttons</li>
  <li><strong>Announcements panel</strong>: stacked announcement items</li>
  <li><strong>Trending panel</strong>: user + project trending list</li>
  <li>Use CSS custom properties for your colour theme</li>
  <li>Use SVG icons (heroicons or similar)</li>
</ul>
""" + code("""/* Suggested top-level grid */
.dashboard {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-rows: auto 1fr;
  grid-template-areas:
    "sidebar header"
    "sidebar main";
  min-height: 100vh;
}

/* Main content inner grid */
.main-content {
  display: grid;
  grid-template-columns: 1fr 300px;
  grid-template-rows: 1fr auto;
  gap: 1.5rem;
  padding: 1.5rem;
}
"""),
    kc=[("How do you make the sidebar span the full height?", "requirements"),
        ("Which layout system should control the dashboard structure vs the card internals?", "requirements")],
    assignments=["Complete the Admin Dashboard meeting all requirements.", "Push to GitHub Pages."],
    resources=[
        ("CSS-Tricks — Complete Guide to Grid", "https://css-tricks.com/snippets/css/complete-guide-grid/"),
        ("heroicons.com", "https://heroicons.com/"),
    ])

    # ── 21. Introduction to Responsive Design ────────────────────────────
    w("introduction-to-responsive-design", "Introduction to Responsive Design",
    intro="Responsive design is the practice of building websites that work well on any screen size — from a 320px phone to a 4K monitor. This lesson introduces the core concepts and vocabulary.",
    overview=["Understand what responsive design means.", "Know the viewport meta tag and why it is required.", "Understand mobile-first vs desktop-first approaches.", "Know the three pillars of responsive design."],
    body="""
<h2 class="lesson-section-title" id="what-is-responsive">What Is Responsive Design?</h2>
<p>Responsive design means a single HTML document adapts its layout and presentation to any viewport size. It was coined by Ethan Marcotte in 2010 and has three pillars: fluid grids, flexible images, and media queries.</p>

<h2 class="lesson-section-title" id="viewport-meta">The Viewport Meta Tag</h2>
""" + code("""<!-- Required in every HTML page — tells mobile browsers not to zoom out -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Without this tag, mobile browsers render at ~980px and zoom out,
     making your responsive CSS useless -->
""") + """
<h2 class="lesson-section-title" id="mobile-first">Mobile-First vs Desktop-First</h2>
<p><strong>Mobile-first</strong>: write baseline styles for small screens, then use <code>min-width</code> media queries to add complexity for larger screens. This is the recommended approach — it forces you to prioritise content over decoration.</p>
<p><strong>Desktop-first</strong>: write for large screens, then use <code>max-width</code> queries to strip things down for mobile. Harder to maintain and often produces heavier mobile payloads.</p>
""" + code("""/* Mobile-first (preferred) */
.card { font-size: 1rem; }

@media (min-width: 768px) {
  .card { font-size: 1.125rem; }
}

/* Desktop-first (avoid) */
.card { font-size: 1.125rem; }

@media (max-width: 767px) {
  .card { font-size: 1rem; }
}
"""),
    kc=[("What are the three pillars of responsive design?", "what-is-responsive"),
        ("What does the viewport meta tag do?", "viewport-meta"),
        ("Why is mobile-first preferred over desktop-first?", "mobile-first")],
    assignments=["Check three popular websites on a phone — are they responsive?", "Add the viewport meta tag to a project and test it in DevTools' device mode."],
    resources=[
        ("MDN — Responsive Design", "https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design"),
        ("web.dev — Responsive Web Design Basics", "https://web.dev/articles/responsive-web-design-basics"),
    ])

    # ── 22. Natural Responsiveness ────────────────────────────────────────
    w("natural-responsiveness", "Natural Responsiveness",
    intro="The best responsive design uses as few media queries as possible by writing CSS that is naturally fluid. Techniques like auto-fit grids, clamp(), and percentage widths adapt without explicit breakpoints.",
    overview=["Use fluid typography with clamp().", "Use percentage and max-width for fluid layouts.", "Use auto-fit grids for naturally responsive components.", "Minimise media queries."],
    body="""
<h2 class="lesson-section-title" id="fluid-typography">Fluid Typography</h2>
""" + code("""/* Instead of this: */
h1 { font-size: 2rem; }
@media (min-width: 768px) { h1 { font-size: 3rem; } }

/* Use clamp() for smooth scaling: */
h1 { font-size: clamp(1.75rem, 4vw + 1rem, 3.5rem); }
h2 { font-size: clamp(1.5rem, 3vw + 0.75rem, 2.5rem); }
p  { font-size: clamp(1rem, 1vw + 0.75rem, 1.25rem); }

/* Or use a fluid type scale tool (utopia.fyi) */
""") + """
<h2 class="lesson-section-title" id="fluid-layouts">Fluid Layouts</h2>
""" + code("""/* Naturally fluid container */
.container {
  width: min(100% - 3rem, 1200px);
  margin-inline: auto;
}

/* Naturally responsive grid — NO media queries */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: 1.5rem;
}

/* Naturally fluid sidebar layout */
.layout {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}
.sidebar { flex: 1 1 250px; }   /* grows, shrinks, basis 250px */
.main    { flex: 3 1 450px; }   /* prefers 3x the space */
"""),
    kc=[("What does clamp() do that a media query cannot?", "fluid-typography"),
        ("How does auto-fit with minmax create a responsive grid without media queries?", "fluid-layouts"),
        ("What does flex: 3 1 450px mean?", "fluid-layouts")],
    assignments=["Rewrite a fixed-width layout to be fully fluid using clamp(), min(), and auto-fit.", "Try utopia.fyi to generate a complete fluid type scale."],
    resources=[
        ("Every Layout — Fluid Type", "https://every-layout.dev/"),
        ("Utopia — Fluid Type Scale Calculator", "https://utopia.fyi/"),
        ("web.dev — Responsive Design Patterns", "https://web.dev/articles/responsive-web-design-patterns"),
    ])

    # ── 23. Responsive Images ─────────────────────────────────────────────
    w("responsive-images", "Responsive Images",
    intro="Images are the biggest contributor to page weight. Responsive images serve the right size image to the right device, dramatically improving performance on mobile.",
    overview=["Use max-width: 100% for basic image flexibility.", "Use srcset to serve different resolutions.", "Use the sizes attribute for layout-aware image loading.", "Use the <picture> element for art direction.", "Use modern image formats (WebP, AVIF)."],
    body="""
<h2 class="lesson-section-title" id="basic-responsive">Basic Responsive Images</h2>
""" + code("""/* Images never overflow their container */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Modern reset includes this already */
img, video {
  max-width: 100%;
  height: auto;
}
""") + """
<h2 class="lesson-section-title" id="srcset-sizes">srcset and sizes</h2>
""" + code("""<!-- srcset: list available image widths -->
<!-- sizes: tell the browser how wide the image will be rendered -->
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w,
          photo-800.jpg 800w,
          photo-1200.jpg 1200w"
  sizes="(max-width: 600px) 100vw,
         (max-width: 1200px) 50vw,
         800px"
  alt="A descriptive alt text"
  loading="lazy"
  decoding="async"
>
""") + """
<h2 class="lesson-section-title" id="picture-element">The picture Element</h2>
""" + code("""<!-- Art direction: serve completely different images at different sizes -->
<picture>
  <!-- Modern format, wide screen -->
  <source
    media="(min-width: 800px)"
    srcset="hero-wide.avif"
    type="image/avif"
  >
  <!-- Modern format, mobile -->
  <source
    media="(max-width: 799px)"
    srcset="hero-square.avif"
    type="image/avif"
  >
  <!-- WebP fallback -->
  <source srcset="hero-wide.webp" type="image/webp">
  <!-- Final fallback — always include an <img> -->
  <img src="hero-wide.jpg" alt="Hero image" width="1200" height="600">
</picture>
"""),
    kc=[("What is the difference between srcset and the picture element?", "srcset-sizes"),
        ("What does the sizes attribute tell the browser?", "srcset-sizes"),
        ("Why should you always include an <img> inside <picture>?", "picture-element")],
    assignments=["Add srcset to all images in a project.", "Convert a JPEG to WebP and AVIF and serve them with <picture>."],
    resources=[
        ("MDN — Responsive Images", "https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images"),
        ("web.dev — Serve Images in Modern Formats", "https://web.dev/articles/uses-webp-images"),
        ("Squoosh — Image Compression Tool", "https://squoosh.app/"),
    ])

    # ── 24. Media Queries ─────────────────────────────────────────────────
    w("media-queries", "Media Queries",
    intro="Media queries are the tool that lets CSS adapt to screen size, orientation, colour scheme preference, and other media features. This lesson covers syntax, breakpoint strategy, and modern range queries.",
    overview=["Write min-width and max-width media queries.", "Understand and choose breakpoints.", "Use modern range syntax.", "Use prefers-color-scheme and prefers-reduced-motion.", "Combine media queries."],
    body="""
<h2 class="lesson-section-title" id="syntax">Media Query Syntax</h2>
""" + code("""/* Classic syntax */
@media screen and (min-width: 768px) {
  .container { max-width: 960px; }
}

/* Modern range syntax (widely supported 2023+) */
@media (width >= 768px) {
  .container { max-width: 960px; }
}

@media (768px <= width <= 1200px) {
  /* Tablet range only */
}

/* Common breakpoint scale */
/* Mobile:  < 640px  (default — no query needed, mobile-first) */
/* Tablet:  640px–1024px */
/* Desktop: 1024px+ */
/* Wide:    1280px+ */

@media (min-width: 640px)  { /* sm  */ }
@media (min-width: 768px)  { /* md  */ }
@media (min-width: 1024px) { /* lg  */ }
@media (min-width: 1280px) { /* xl  */ }
""") + """
<h2 class="lesson-section-title" id="preference-queries">Preference Queries</h2>
""" + code("""/* Respect user's OS dark mode preference */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #111827;
    --color-text: #f9fafb;
  }
}

/* Respect user's motion preferences — critical for accessibility */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* Print styles */
@media print {
  nav, .sidebar, .ads { display: none; }
  body { font-size: 12pt; color: black; }
}
"""),
    kc=[("What is the difference between min-width and max-width media queries?", "syntax"),
        ("Why should breakpoints be based on content, not devices?", "syntax"),
        ("What does prefers-reduced-motion affect?", "preference-queries")],
    assignments=["Add prefers-reduced-motion support to any animations in your projects.", "Implement system dark mode using prefers-color-scheme and custom properties."],
    resources=[
        ("MDN — Using Media Queries", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries"),
        ("web.dev — Media Queries for Standard Devices", "https://web.dev/articles/media-queries-in-html"),
    ])

    # ── 25. Project: Homepage ─────────────────────────────────────────────
    w("project-homepage", "Project: Homepage",
    intro="Design and build a fully responsive personal homepage or portfolio landing page. This project brings together everything from Intermediate HTML and CSS — Grid, Flexbox, responsive images, media queries, and custom properties.",
    overview=["Plan and design a responsive homepage.", "Build it mobile-first.", "Use Grid and Flexbox appropriately throughout.", "Optimise images and performance.", "Deploy to GitHub Pages."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>A hero section with a headline, subheading, CTA button, and an image</li>
  <li>A features/skills section using a responsive Grid</li>
  <li>A projects section (cards with image, title, description, links)</li>
  <li>A contact section with a form</li>
  <li>A navigation bar (sticky or fixed) with mobile hamburger menu (CSS-only or JS)</li>
  <li>Fully responsive — looks excellent from 320px to 1440px+</li>
  <li>Uses CSS custom properties for the entire colour/spacing system</li>
  <li>Responsive images with srcset or picture</li>
  <li>prefers-reduced-motion support for any animations</li>
  <li>Deployed live on GitHub Pages</li>
</ul>
""",
    kc=[("How do you make a navigation bar collapse on mobile?", "requirements"),
        ("What should srcset provide that a plain src cannot?", "requirements")],
    assignments=["Complete the Homepage meeting all requirements.", "Submit the live URL and the GitHub repo link."],
    resources=[
        ("GitHub Pages Docs", "https://pages.github.com/"),
        ("web.dev — Responsive Web Design", "https://web.dev/articles/responsive-web-design-basics"),
    ])

    # ── 26. Introduction to Web Accessibility ─────────────────────────────
    w("intro-to-accessibility", "Introduction to Web Accessibility",
    intro="Web accessibility (a11y) means building websites that everyone can use — including people with visual, auditory, motor, or cognitive disabilities. It is not optional; it is fundamental to good web development.",
    overview=["Understand what web accessibility means and why it matters.", "Know the four principles of WCAG (POUR).", "Understand assistive technologies and how they interact with the web.", "Learn the legal context around accessibility."],
    body="""
<h2 class="lesson-section-title" id="what-is-a11y">What Is Accessibility?</h2>
<p>Accessibility is the practice of making your websites usable by as many people as possible. Approximately 15% of the world's population has some form of disability. Accessible websites benefit everyone — better keyboard navigation, clearer structure, and higher contrast help all users, not just those with disabilities.</p>

<h2 class="lesson-section-title" id="pour">The POUR Principles</h2>
<ul>
  <li><strong>Perceivable</strong> — Information must be presentable in ways users can perceive (alt text, captions, sufficient contrast).</li>
  <li><strong>Operable</strong> — Interface components must be operable by all users (keyboard navigation, enough time, no seizure-inducing content).</li>
  <li><strong>Understandable</strong> — Information and UI operation must be understandable (readable text, predictable navigation, error messages).</li>
  <li><strong>Robust</strong> — Content must be interpretable by assistive technologies (valid HTML, ARIA when needed).</li>
</ul>

<h2 class="lesson-section-title" id="assistive-tech">Assistive Technologies</h2>
<ul>
  <li><strong>Screen readers</strong> — NVDA (Windows, free), JAWS (Windows), VoiceOver (macOS/iOS built-in), TalkBack (Android)</li>
  <li><strong>Keyboard navigation</strong> — Many users cannot use a mouse; all functionality must be reachable via keyboard</li>
  <li><strong>Switch access</strong> — Users with limited mobility use single-button switches to navigate</li>
  <li><strong>Screen magnifiers</strong> — Users with low vision zoom in significantly</li>
</ul>
""",
    kc=[("What does POUR stand for?", "pour"),
        ("Name two common screen readers.", "assistive-tech"),
        ("Why does accessibility benefit all users, not just those with disabilities?", "what-is-a11y")],
    assignments=["Install NVDA (Windows) or enable VoiceOver (Mac/iOS) and try navigating a website with it.", "Run an accessibility audit on a project using Chrome's Lighthouse tool."],
    resources=[
        ("WebAIM — Introduction to Accessibility", "https://webaim.org/intro/"),
        ("MDN — Accessibility", "https://developer.mozilla.org/en-US/docs/Web/Accessibility"),
        ("A11y Project", "https://www.a11yproject.com/"),
    ])

    # ── 27. WCAG ──────────────────────────────────────────────────────────
    w("the-web-content-accessibility-guidelines", "The Web Content Accessibility Guidelines",
    intro="The Web Content Accessibility Guidelines (WCAG) are the international standard for web accessibility. This lesson covers the three conformance levels and the most actionable success criteria.",
    overview=["Understand WCAG 2.1 conformance levels A, AA, and AAA.", "Know the most important success criteria.", "Know how to test for WCAG compliance.", "Understand the legal requirements in different countries."],
    body="""
<h2 class="lesson-section-title" id="conformance-levels">Conformance Levels</h2>
<ul>
  <li><strong>Level A</strong> — Minimum. If not met, some users cannot access content at all.</li>
  <li><strong>Level AA</strong> — Standard target. Required by most laws and regulations worldwide. This is what you should aim for.</li>
  <li><strong>Level AAA</strong> — Highest. Not required for entire sites but good for critical functionality.</li>
</ul>

<h2 class="lesson-section-title" id="key-criteria">Key Success Criteria</h2>
""" + code("""/* 1.1.1 Non-text Content (Level A)
   All images need alt text. Decorative images get alt="" */
<img src="chart.png" alt="Bar chart showing Q1 revenue by region">
<img src="divider.png" alt="">  <!-- decorative — empty alt -->

/* 1.4.3 Contrast Minimum (Level AA)
   Normal text: 4.5:1 contrast ratio minimum
   Large text (18pt+ or 14pt bold): 3:1 minimum */

/* 2.1.1 Keyboard (Level A)
   All functionality available from keyboard */

/* 2.4.7 Focus Visible (Level AA)
   Keyboard focus must be visible — never do this: */
*:focus { outline: none; }  /* NEVER */

/* Do this instead: */
*:focus-visible {
  outline: 2px solid #4f46e5;
  outline-offset: 2px;
}

/* 3.1.1 Language of Page (Level A) */
<html lang="en">

/* 4.1.2 Name, Role, Value (Level A)
   Use semantic HTML — it provides name, role, value for free */
""") + """
<h2 class="lesson-section-title" id="testing">Testing for Accessibility</h2>
<ul>
  <li><strong>Automated</strong>: Lighthouse (Chrome DevTools), axe DevTools browser extension, WAVE</li>
  <li><strong>Manual keyboard test</strong>: Tab through the entire page — can you reach everything?</li>
  <li><strong>Screen reader test</strong>: VoiceOver or NVDA — does the page make sense?</li>
  <li><strong>Contrast checker</strong>: WebAIM Contrast Checker or browser DevTools</li>
</ul>
<p>Automated tools catch about 30% of issues. Manual testing is essential.</p>
""",
    kc=[("What conformance level should most websites target?", "conformance-levels"),
        ("What contrast ratio is required for normal body text at AA level?", "key-criteria"),
        ("Why is removing focus outlines a serious accessibility problem?", "key-criteria")],
    assignments=["Run axe DevTools on three pages of a project and fix every issue found.", "Check the contrast ratio of your colour scheme using WebAIM's contrast checker."],
    resources=[
        ("WCAG 2.1 — Official", "https://www.w3.org/TR/WCAG21/"),
        ("WebAIM — WCAG 2 Checklist", "https://webaim.org/standards/wcag/checklist"),
        ("WebAIM — Contrast Checker", "https://webaim.org/resources/contrastchecker/"),
        ("axe DevTools", "https://www.deque.com/axe/devtools/"),
    ])

    # ── 28. Accessible Colors ─────────────────────────────────────────────
    w("accessible-colors", "Accessible Colors",
    intro="Colour contrast is one of the most common accessibility failures. This lesson covers WCAG contrast requirements, how to check and fix contrast issues, and how to design colour systems that are accessible by default.",
    overview=["Understand the WCAG contrast ratio requirements.", "Use tools to check and fix contrast.", "Design accessible colour palettes.", "Handle colour-blindness considerations.", "Never rely on colour alone to convey information."],
    body="""
<h2 class="lesson-section-title" id="contrast-ratios">Contrast Ratios</h2>
""" + code("""/* WCAG 2.1 AA Requirements */

/* Normal text (< 18pt / 14pt bold): 4.5:1 minimum */
/* Large text (18pt+ / 14pt bold+):  3:1 minimum */
/* UI components and graphics:       3:1 minimum */

/* Common failures */
color: #aaa; background: #fff;   /* 2.32:1 — FAIL */
color: #767676; background: #fff; /* 4.54:1 — PASS (barely) */
color: #595959; background: #fff; /* 7.0:1  — PASS AAA */

/* Dark mode — same ratios apply */
color: #e5e7eb; background: #111827; /* Check this too! */
""") + """
<h2 class="lesson-section-title" id="not-color-alone">Never Colour Alone</h2>
""" + code("""<!-- BAD: only colour distinguishes valid from invalid -->
<input style="border-color: red">

<!-- GOOD: colour + icon + text -->
<div class="field-error">
  <input aria-invalid="true" aria-describedby="email-error">
  <p id="email-error">
    <svg aria-hidden="true"><!-- error icon --></svg>
    Please enter a valid email address.
  </p>
</div>

<!-- Required fields: colour + asterisk + legend -->
<fieldset>
  <legend>Fields marked <span aria-hidden="true">*</span>
  <span class="sr-only">with an asterisk</span> are required.</legend>
  <label>Email <span aria-hidden="true" class="required">*</span>
    <input type="email" required>
  </label>
</fieldset>
"""),
    kc=[("What contrast ratio does WCAG AA require for normal body text?", "contrast-ratios"),
        ("Why can you never rely on colour alone to convey information?", "not-color-alone"),
        ("How do you make an error state accessible beyond just a red border?", "not-color-alone")],
    assignments=["Check every text/background combination in your design system against WCAG AA.", "Add a text label or icon to any place you use colour alone (error states, status indicators)."],
    resources=[
        ("WebAIM — Contrast Checker", "https://webaim.org/resources/contrastchecker/"),
        ("Coolors — Colour Contrast Checker", "https://coolors.co/contrast-checker"),
        ("Accessible Color Palette Builder", "https://toolness.github.io/accessible-color-matrix/"),
    ])

    # ── 29. Meaningful Text ───────────────────────────────────────────────
    w("meaningful-text", "Meaningful Text",
    intro="Screen reader users often navigate by headings, links, and buttons — hearing just those elements out of context. This lesson covers how to write text that is meaningful in isolation.",
    overview=["Write descriptive alt text for images.", "Write descriptive link text.", "Write descriptive button labels.", "Use visually hidden text for screen reader context.", "Use proper heading hierarchy."],
    body="""
<h2 class="lesson-section-title" id="alt-text">Alt Text</h2>
""" + code("""<!-- Informative image — describe what it shows and why it matters -->
<img src="revenue-chart.png"
     alt="Bar chart: Q1 revenue grew 23% year-over-year to $4.2M">

<!-- Decorative image — empty alt so screen readers skip it -->
<img src="divider-wave.svg" alt="">

<!-- Functional image (button/link with only an image) — describe the action -->
<a href="/cart">
  <img src="cart-icon.svg" alt="Shopping cart (3 items)">
</a>

<!-- Complex image — provide a long description -->
<figure>
  <img src="org-chart.png" alt="Company organisational chart"
       aria-describedby="chart-desc">
  <figcaption id="chart-desc">
    The CEO reports to the Board. The CTO, CFO, and CMO report to the CEO...
  </figcaption>
</figure>
""") + """
<h2 class="lesson-section-title" id="link-text">Link and Button Text</h2>
""" + code("""<!-- BAD: meaningless out of context -->
<a href="/article">Read more</a>
<button>Click here</button>

<!-- GOOD: descriptive in isolation -->
<a href="/article">Read more about responsive design</a>
<button>Add item to cart</button>

<!-- When you must use short visual text, add sr-only context -->
<a href="/article">
  Read more
  <span class="sr-only">about responsive design</span>
</a>
""") + """
<h2 class="lesson-section-title" id="sr-only">Visually Hidden Text</h2>
""" + code("""/* The .sr-only pattern — visible to screen readers, hidden visually */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Usage */
<button>
  <svg aria-hidden="true"><!-- hamburger icon --></svg>
  <span class="sr-only">Open navigation menu</span>
</button>
"""),
    kc=[("What alt text should a decorative image have?", "alt-text"),
        ("Why is 'Read more' a bad link text?", "link-text"),
        ("What does the .sr-only class do?", "sr-only")],
    assignments=["Audit all images in a project — does every informative image have good alt text?", "Audit all links and buttons — are they meaningful out of context?"],
    resources=[
        ("WebAIM — Alternative Text", "https://webaim.org/techniques/alttext/"),
        ("WebAIM — Links and Hypertext", "https://webaim.org/techniques/hypertext/"),
        ("A11y Project — Alt Text Checklist", "https://www.a11yproject.com/checklist/#images"),
    ])

    # ── 30. WAI-ARIA ──────────────────────────────────────────────────────
    w("wai-aria", "WAI-ARIA",
    intro="WAI-ARIA (Web Accessibility Initiative — Accessible Rich Internet Applications) is a set of HTML attributes that add semantic meaning to elements that lack it, particularly for dynamic content and custom widgets.",
    overview=["Understand when to use ARIA and when not to.", "Use aria-label, aria-labelledby, and aria-describedby.", "Use roles to define element semantics.", "Use aria-live for dynamic content.", "Follow the first rule of ARIA."],
    body="""
<h2 class="lesson-section-title" id="first-rule">The First Rule of ARIA</h2>
<p><strong>Don't use ARIA if you can use a native HTML element instead.</strong> Semantic HTML provides accessibility for free — <code>&lt;button&gt;</code> is always better than <code>&lt;div role="button"&gt;</code>. ARIA fills the gaps where HTML is insufficient.</p>

<h2 class="lesson-section-title" id="aria-attributes">Common ARIA Attributes</h2>
""" + code("""<!-- aria-label — provides an accessible name when no visible text exists -->
<button aria-label="Close dialog">✕</button>
<nav aria-label="Main navigation">...</nav>
<nav aria-label="Breadcrumb">...</nav>

<!-- aria-labelledby — points to an element that labels this one -->
<section aria-labelledby="section-heading">
  <h2 id="section-heading">Recent Projects</h2>
  ...
</section>

<!-- aria-describedby — points to additional description -->
<input type="password" aria-describedby="pw-hint">
<p id="pw-hint">Must be at least 8 characters with one number.</p>

<!-- aria-hidden — hides decorative content from screen readers -->
<span aria-hidden="true">⭐⭐⭐⭐⭐</span>
<span class="sr-only">5 out of 5 stars</span>

<!-- aria-expanded — for toggleable components -->
<button aria-expanded="false" aria-controls="menu">Menu</button>
<ul id="menu" hidden>...</ul>

<!-- aria-invalid and aria-required -->
<input aria-required="true" aria-invalid="true">

<!-- aria-live — announces dynamic content changes -->
<div aria-live="polite">   <!-- waits for quiet moment -->
  <!-- Search results: 42 results found -->
</div>
<div aria-live="assertive"> <!-- interrupts immediately — use sparingly -->
  <!-- Error: Session expired -->
</div>
"""),
    kc=[("What is the first rule of ARIA?", "first-rule"),
        ("What is the difference between aria-label and aria-labelledby?", "aria-attributes"),
        ("When would you use aria-live='assertive' vs 'polite'?", "aria-attributes")],
    assignments=["Add aria-label to all icon-only buttons in a project.", "Implement an accessible accordion using aria-expanded and aria-controls."],
    resources=[
        ("MDN — ARIA", "https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA"),
        ("WebAIM — ARIA Introduction", "https://webaim.org/techniques/aria/"),
        ("ARIA Authoring Practices Guide", "https://www.w3.org/WAI/ARIA/apg/"),
    ])

    # ── 31. Keyboard Navigation ───────────────────────────────────────────
    w("keyboard-navigation", "Keyboard Navigation",
    intro="All functionality on a webpage must be reachable and operable using only a keyboard. This is required by WCAG and is essential for users with motor disabilities who cannot use a mouse.",
    overview=["Understand how keyboard navigation works.", "Manage tab order and tabindex.", "Style focus states effectively.", "Implement skip links.", "Build accessible interactive components."],
    body="""
<h2 class="lesson-section-title" id="how-keyboard-nav-works">How Keyboard Navigation Works</h2>
<ul>
  <li><strong>Tab</strong> — moves focus forward through interactive elements</li>
  <li><strong>Shift+Tab</strong> — moves focus backward</li>
  <li><strong>Enter / Space</strong> — activates buttons and links</li>
  <li><strong>Arrow keys</strong> — navigate within components (menus, tabs, sliders)</li>
  <li><strong>Escape</strong> — closes modals, dropdowns, tooltips</li>
</ul>
<p>Focusable elements by default: <code>a[href]</code>, <code>button</code>, <code>input</code>, <code>select</code>, <code>textarea</code>, <code>[tabindex="0"]</code>.</p>

<h2 class="lesson-section-title" id="tabindex">tabindex</h2>
""" + code("""<!-- tabindex="0" — adds element to natural tab order -->
<div tabindex="0" role="button">Custom Button</div>

<!-- tabindex="-1" — focusable via JS/script, but not in tab order
     Use for managing focus programmatically (modals, alerts) -->
<div id="modal" tabindex="-1" role="dialog">...</div>
document.getElementById('modal').focus();

<!-- AVOID tabindex > 0 — it creates unpredictable tab order -->
<input tabindex="3">  <!-- bad practice -->
""") + """
<h2 class="lesson-section-title" id="focus-styles">Focus Styles</h2>
""" + code("""/* NEVER remove focus outlines entirely */
/* BAD */
* { outline: none; }
a:focus { outline: none; }

/* GOOD — remove only for mouse users, keep for keyboard users */
*:focus:not(:focus-visible) { outline: none; }
*:focus-visible {
  outline: 2px solid #4f46e5;
  outline-offset: 3px;
  border-radius: 2px;
}
""") + """
<h2 class="lesson-section-title" id="skip-links">Skip Links</h2>
""" + code("""<!-- Skip to main content — allows keyboard users to bypass navigation -->
<!-- Place as the FIRST element in <body> -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<main id="main-content" tabindex="-1">...</main>

<style>
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  background: #4f46e5;
  color: white;
  padding: 0.5rem 1rem;
  z-index: 9999;
}
.skip-link:focus {
  top: 0;   /* appears when focused */
}
</style>
"""),
    kc=[("What does tabindex=\"-1\" do?", "tabindex"),
        ("Why should you never use outline: none on :focus?", "focus-styles"),
        ("What is a skip link and why is it important?", "skip-links")],
    assignments=["Tab through an entire project — can you reach and operate every interactive element?", "Add a skip link to the top of a project.", "Style visible focus states for all interactive elements."],
    resources=[
        ("WebAIM — Keyboard Accessibility", "https://webaim.org/techniques/keyboard/"),
        ("A11y Project — Skip Navigation Links", "https://www.a11yproject.com/posts/skip-nav-links/"),
        ("MDN — tabindex", "https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex"),
    ])

    print(f"  Intermediate HTML and CSS (Rails path): {len(ALL)} lessons done")


def main():
    seed_intermediate_html_css()
    print("\nIntermediate HTML & CSS complete. Committing...")
    os.chdir(BASE)
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", "Seed Intermediate HTML & CSS — Rails path (31 lessons)"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Pushed.")


if __name__ == "__main__":
    main()
