#!/usr/bin/env python3
"""
Seed: Full Stack JavaScript — Intermediate HTML and CSS
All 33 lessons, no references to any specific curriculum site,
using MDN, CSS-Tricks, Kevin Powell, and other quality resources.
"""
import os, subprocess

BASE    = os.path.expanduser("~/devpath")
COURSE  = os.path.join(BASE, "paths", "full-stack-javascript", "courses", "intermediate-html-css")
LESSONS = os.path.join(COURSE, "lessons")

LOGO = '<svg viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="13" stroke="currentColor" stroke-width="1.8"/><path d="M8 14 L14 7 L20 14 L14 21 Z" fill="currentColor"/></svg>'

ALL_LESSONS = [
    ("int-html-css-intro",                  "Introduction"),
    ("emmet",                               "Emmet"),
    ("svg",                                 "SVG"),
    ("html-tables",                         "Tables"),
    ("default-styles",                      "Default Styles"),
    ("css-units",                           "CSS Units"),
    ("more-text-styles",                    "More Text Styles"),
    ("more-css-properties",                 "More CSS Properties"),
    ("advanced-selectors",                  "Advanced Selectors"),
    ("positioning",                         "Positioning"),
    ("css-functions",                       "CSS Functions"),
    ("custom-properties",                   "Custom Properties"),
    ("browser-compatibility",               "Browser Compatibility"),
    ("form-basics",                         "Form Basics"),
    ("form-validation",                     "Form Validation"),
    ("project-sign-up-form",                "Project: Sign-Up Form"),
    ("introduction-to-grid",                "Introduction to Grid"),
    ("creating-a-grid",                     "Creating a Grid"),
    ("positioning-grid-elements",           "Positioning Grid Elements"),
    ("advanced-grid-properties",            "Advanced Grid Properties"),
    ("using-flexbox-and-grid",              "Using Flexbox and Grid"),
    ("project-admin-dashboard",             "Project: Admin Dashboard"),
    ("introduction-to-web-accessibility",   "Introduction to Web Accessibility"),
    ("the-web-content-accessibility-guidelines", "The Web Content Accessibility Guidelines (WCAG)"),
    ("accessible-colors",                   "Accessible Colors"),
    ("keyboard-navigation",                 "Keyboard Navigation"),
    ("meaningful-text",                     "Meaningful Text"),
    ("wai-aria",                            "WAI-ARIA"),
    ("introduction-to-responsive-design",   "Introduction to Responsive Design"),
    ("natural-responsiveness",              "Natural Responsiveness"),
    ("responsive-images",                   "Responsive Images"),
    ("media-queries",                       "Media Queries"),
    ("project-homepage",                    "Project: Homepage"),
]

def nav():
    return (
        '<nav class="site-nav">'
        f'<a href="../../../../../../index.html" class="nav-logo">{LOGO} DevPath</a>'
        '<ul class="nav-links">'
        '<li><a href="../../../../../../index.html">Home</a></li>'
        '<li><a href="../../../../../../foundations/index.html">Foundations</a></li>'
        '<li><a href="../../../../index.html">Full Stack JS</a></li>'
        '<li><a href="../../index.html">Intermediate HTML &amp; CSS</a></li>'
        '</ul></nav>'
    )

def footer():
    return '<footer class="site-footer"><p>DevPath — A free, open, project-based web development curriculum.</p></footer>'

def sidebar(active):
    sections = [
        ("Introduction", [("int-html-css-intro","Introduction",False)]),
        ("Intermediate HTML", [
            ("emmet","Emmet",False),
            ("svg","SVG",False),
            ("html-tables","Tables",False),
        ]),
        ("Intermediate CSS", [
            ("default-styles","Default Styles",False),
            ("css-units","CSS Units",False),
            ("more-text-styles","More Text Styles",False),
            ("more-css-properties","More CSS Properties",False),
            ("advanced-selectors","Advanced Selectors",False),
            ("positioning","Positioning",False),
            ("css-functions","CSS Functions",False),
            ("custom-properties","Custom Properties",False),
            ("browser-compatibility","Browser Compatibility",False),
        ]),
        ("Forms", [
            ("form-basics","Form Basics",False),
            ("form-validation","Form Validation",False),
            ("project-sign-up-form","Project: Sign-Up Form",True),
        ]),
        ("Grid", [
            ("introduction-to-grid","Introduction to Grid",False),
            ("creating-a-grid","Creating a Grid",False),
            ("positioning-grid-elements","Positioning Grid Elements",False),
            ("advanced-grid-properties","Advanced Grid Properties",False),
            ("using-flexbox-and-grid","Using Flexbox and Grid",False),
            ("project-admin-dashboard","Project: Admin Dashboard",True),
        ]),
        ("Accessibility", [
            ("introduction-to-web-accessibility","Introduction to Web Accessibility",False),
            ("the-web-content-accessibility-guidelines","The Web Content Accessibility Guidelines",False),
            ("accessible-colors","Accessible Colors",False),
            ("keyboard-navigation","Keyboard Navigation",False),
            ("meaningful-text","Meaningful Text",False),
            ("wai-aria","WAI-ARIA",False),
        ]),
        ("Responsive Design", [
            ("introduction-to-responsive-design","Introduction to Responsive Design",False),
            ("natural-responsiveness","Natural Responsiveness",False),
            ("responsive-images","Responsive Images",False),
            ("media-queries","Media Queries",False),
            ("project-homepage","Project: Homepage",True),
        ]),
    ]
    s = '<aside class="sidebar"><div class="sidebar-course-title">Intermediate HTML &amp; CSS</div>'
    for label, items in sections:
        s += f'<div class="sidebar-section"><div class="sidebar-section-label">{label}</div>'
        for sl, ti, proj in items:
            cls = "sidebar-link" + (" is-project" if proj else "") + (" active" if sl == active else "")
            s += f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'
        s += '</div>'
    s += '</aside>'
    return s

def code(snippet):
    esc = snippet.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f'<div class="code-block"><pre><code>{esc}</code></pre></div>'

def pn(slug):
    idx = next((i for i,l in enumerate(ALL_LESSONS) if l[0]==slug), None)
    p = (ALL_LESSONS[idx-1][1], ALL_LESSONS[idx-1][0]+".html") if idx and idx>0 else None
    n = (ALL_LESSONS[idx+1][1], ALL_LESSONS[idx+1][0]+".html") if idx is not None and idx<len(ALL_LESSONS)-1 else None
    return p, n

def navbar(slug):
    p, n = pn(slug)
    pb = f'<a href="{p[1]}" class="btn btn-blue-outline">&#8592; Previous</a>' if p else '<span></span>'
    nb = f'<a href="{n[1]}" class="btn btn-blue">Next &#8594;</a>' if n else '<span></span>'
    return (
        '<div class="lesson-nav-bar">'
        f'<div class="lesson-nav-bar-group">{pb}</div>'
        '<div class="lesson-nav-bar-group">'
        '<button class="btn btn-green mark-complete-btn">Mark Completed</button>'
        '</div>'
        f'<div class="lesson-nav-bar-group">{nb}</div>'
        '</div>'
    )

def write(slug, title, intro, overview, body, kc, assignments, resources):
    p, n = pn(slug)
    bc = (
        '<nav class="breadcrumb">'
        '<a href="../../../../../../index.html">Home</a>'
        '<span class="breadcrumb-sep">/</span>'
        '<a href="../../../../index.html">Full Stack JS</a>'
        '<span class="breadcrumb-sep">/</span>'
        '<a href="../../index.html">Intermediate HTML &amp; CSS</a>'
        '<span class="breadcrumb-sep">/</span>'
        f'<span class="breadcrumb-current">{title}</span></nav>'
    )
    ov   = "".join(f"<li>{i}</li>" for i in overview)
    kcli = "".join(f'<li><a href="#{k[1]}" data-target="{k[1]}">{k[0]}</a></li>' for k in kc)
    asli = "".join(f"<li>{a}</li>" for a in assignments)
    rsli = "".join(f'<li><a href="{r[1]}" target="_blank" rel="noopener">{r[0]}</a></li>' for r in resources)
    ph   = f'<a href="{p[1]}" class="pagination-link prev"><span class="pagination-label">&#8592; Previous</span><span class="pagination-title">{p[0]}</span></a>' if p else "<span></span>"
    nh   = f'<a href="{n[1]}" class="pagination-link next"><span class="pagination-label">Next &#8594;</span><span class="pagination-title">{n[0]}</span></a>' if n else "<span></span>"

    html = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '  <meta charset="UTF-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'  <title>{title} | DevPath</title>\n'
        '  <link rel="stylesheet" href="../../../../../../css/styles.css">\n'
        '</head>\n<body>\n'
        + nav() + '\n'
        + navbar(slug) + '\n'
        + f'<div class="page-header"><div class="page-header-inner">{bc}<h1>{title}</h1></div></div>\n'
        + f'<div class="lesson-layout">{sidebar(slug)}<main><div class="lesson-body">\n'
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
        + '<script src="../../../../../../js/main.js"></script>\n</body>\n</html>'
    )
    with open(os.path.join(LESSONS, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  {slug}")


# ════════════════════════════════════════════════════════════
#  LESSONS
# ════════════════════════════════════════════════════════════
def seed():

    write("int-html-css-intro","Introduction",
    intro="Welcome to Intermediate HTML and CSS. You already know the fundamentals — now you will fill in the gaps and master the tools professional developers use every day.",
    overview=[
        "Understand what this course covers and why each topic matters.",
        "Know the order lessons should be taken.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-this-covers">What This Course Covers</h2>
<p>Foundations gave you the skeleton of web development. This course adds the muscle. You will learn the HTML and CSS features that are everywhere in professional codebases but are often skipped in beginner courses:</p>
<ul>
  <li><strong>Intermediate HTML</strong> — Emmet shortcuts, SVG graphics, and HTML tables.</li>
  <li><strong>Intermediate CSS</strong> — Units, text styling, advanced selectors, positioning, CSS functions, custom properties, and browser compatibility.</li>
  <li><strong>Forms</strong> — Building and validating real HTML forms.</li>
  <li><strong>CSS Grid</strong> — The two-dimensional layout system that makes complex layouts manageable.</li>
  <li><strong>Accessibility</strong> — Building websites that work for everyone, including users of assistive technology.</li>
  <li><strong>Responsive Design</strong> — Sites that look great on every screen size.</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Take lessons in order. Each section builds directly on the previous one. Skipping ahead causes confusion when topics reference earlier concepts.</p>
</div>
""",
    kc=[("What six topic areas does this course cover?","what-this-covers")],
    assignments=["Read through this introduction and continue to the next lesson."],
    resources=[
        ("MDN — Learn Web Development","https://developer.mozilla.org/en-US/docs/Learn"),
        ("CSS Tricks — Guides","https://css-tricks.com/guides/"),
    ])

    write("emmet","Emmet",
    intro="Emmet is a toolkit built into VS Code that expands short abbreviations into full HTML and CSS. Once it becomes muscle memory, you will write markup significantly faster.",
    overview=[
        "Use Emmet to generate HTML boilerplate and elements.",
        "Write nested structures, siblings, and repeated elements with one abbreviation.",
        "Use Emmet for CSS property shortcuts.",
    ],
    body="""
<h2 class="lesson-section-title" id="html-abbreviations">HTML Abbreviations</h2>
<p>Type an abbreviation in a <code>.html</code> file and press <kbd>Tab</kbd>:</p>
""" + code("""! + Tab
→ Full HTML5 boilerplate

div.container + Tab
→ <div class="container"></div>

div#hero.section + Tab
→ <div id="hero" class="section"></div>

ul>li*5 + Tab
→ <ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
  </ul>

nav>ul>li*3>a[href=#]{Link $} + Tab
→ <nav>
    <ul>
      <li><a href="#">Link 1</a></li>
      <li><a href="#">Link 2</a></li>
      <li><a href="#">Link 3</a></li>
    </ul>
  </nav>
""") + """
<h2 class="lesson-section-title" id="operators">Emmet Operators</h2>
<ul>
  <li><code>&gt;</code> — child: <code>div&gt;p</code> → p inside div</li>
  <li><code>+</code> — sibling: <code>h1+p</code> → h1 then p</li>
  <li><code>*</code> — multiply: <code>li*3</code> → three li elements</li>
  <li><code>$</code> — counter: <code>item$*3</code> → item1, item2, item3</li>
  <li><code>{}</code> — text content: <code>p{Hello}</code> → &lt;p&gt;Hello&lt;/p&gt;</li>
  <li><code>[]</code> — custom attribute: <code>input[type=email]</code></li>
  <li><code>()</code> — grouping: <code>(li&gt;a)*3</code></li>
</ul>

<h2 class="lesson-section-title" id="css-emmet">CSS Abbreviations</h2>
""" + code("""/* In a .css file, type abbreviation + Tab */

m10        → margin: 10px;
p20        → padding: 20px;
df         → display: flex;
jcc        → justify-content: center;
aic        → align-items: center;
w100p      → width: 100%;
bgc#fff    → background-color: #fff;
fz1.5rem   → font-size: 1.5rem;
fw700      → font-weight: 700;
"""),
    kc=[
        ("What does the Emmet operator > do?","operators"),
        ("How do you create five li elements with one Emmet abbreviation?","html-abbreviations"),
        ("What does the $ symbol do in Emmet?","operators"),
    ],
    assignments=[
        "Open a new HTML file and recreate a full page structure (nav, header, main with three sections, footer) using only one Emmet abbreviation.",
        "Read the full Emmet documentation linked below.",
    ],
    resources=[
        ("Emmet — Official Docs","https://docs.emmet.io/"),
        ("Emmet — Cheat Sheet","https://docs.emmet.io/cheat-sheet/"),
        ("YouTube — Emmet in VS Code (Kevin Powell)","https://www.youtube.com/watch?v=EzGWXTASWWo"),
    ])

    write("svg","SVG",
    intro="SVG (Scalable Vector Graphics) is an XML-based image format that scales to any size without losing quality. It is the right choice for icons, logos, illustrations, and animations.",
    overview=[
        "Understand what SVG is and when to use it over raster formats.",
        "Read and write basic SVG markup.",
        "Embed SVGs in HTML using inline, img, and background-image methods.",
        "Style SVGs with CSS.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-is-svg">What Is SVG?</h2>
<p>SVG describes shapes mathematically rather than storing pixel data. This means an SVG logo looks crisp on a phone screen and a 4K monitor — it never blurs. The tradeoff is that SVGs are better suited to geometric shapes and illustrations than complex photographs (use JPEG/WebP for photos).</p>

<h2 class="lesson-section-title" id="basic-svg">Basic SVG Markup</h2>
""" + code("""<!-- SVG is XML — it lives in .svg files or directly in HTML -->
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">

  <!-- Circle: cx cy = centre, r = radius -->
  <circle cx="50" cy="50" r="40" fill="#2563eb" />

  <!-- Rectangle: x y = top-left corner -->
  <rect x="10" y="10" width="80" height="80" fill="none" stroke="#f0c040" stroke-width="4" />

  <!-- Line: x1 y1 = start, x2 y2 = end -->
  <line x1="0" y1="50" x2="100" y2="50" stroke="red" stroke-width="2" />

  <!-- Text -->
  <text x="50" y="55" text-anchor="middle" fill="white" font-size="16">Hello</text>

  <!-- Path: the most powerful SVG element -->
  <path d="M 10 80 Q 50 10 90 80" stroke="#e05c7a" fill="none" stroke-width="3" />

</svg>
""") + """
<h2 class="lesson-section-title" id="embedding">Three Ways to Embed SVG</h2>
""" + code("""<!-- 1. Inline — best for icons you want to style with CSS -->
<button>
  <svg viewBox="0 0 24 24" width="20" height="20">
    <path d="M12 2L2 7l10 5 10-5-10-5z" />
  </svg>
  Save
</button>

<!-- 2. img tag — simple, cacheable, but not styleable with CSS -->
<img src="logo.svg" alt="Company logo" width="200">

<!-- 3. CSS background-image — for decorative SVGs -->
.hero {
  background-image: url('pattern.svg');
}
""") + """
<h2 class="lesson-section-title" id="styling">Styling SVGs with CSS</h2>
""" + code("""/* Inline SVGs can be styled directly with CSS */
svg {
  width: 48px;
  height: 48px;
}

/* Style SVG-specific properties */
.icon {
  fill: currentColor;       /* inherits text colour from parent */
  stroke: none;
  transition: fill 0.2s;
}

.icon:hover {
  fill: #2563eb;
}

/* Using CSS variables for theming */
svg path {
  fill: var(--icon-color, #64748b);
}
"""),
    kc=[
        ("When should you use SVG instead of PNG/JPEG?","what-is-svg"),
        ("What is the difference between fill and stroke in SVG?","basic-svg"),
        ("Which embedding method lets you style SVG with CSS?","embedding"),
    ],
    assignments=[
        "Draw a simple house using only SVG shapes (rect, triangle path, circle for window) without any tools — just code.",
        "Take any icon from heroicons.com, embed it inline, and style its colour and hover state with CSS.",
        "Read MDN's SVG tutorial linked below.",
    ],
    resources=[
        ("MDN — SVG Tutorial","https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial"),
        ("Heroicons — Free SVG Icons","https://heroicons.com/"),
        ("YouTube — SVG Explained (Fireship)","https://www.youtube.com/watch?v=ZJSCl6XEdP8"),
        ("CSS Tricks — Using SVG","https://css-tricks.com/using-svg/"),
    ])

    write("html-tables","Tables",
    intro="HTML tables are for displaying tabular data — information with rows and columns. They are often misused for layout (do not do that) but are exactly right for spreadsheet-style data.",
    overview=[
        "Build a table with thead, tbody, and tfoot.",
        "Span cells across multiple columns and rows.",
        "Style tables with CSS.",
        "Understand when tables are appropriate.",
    ],
    body="""
<h2 class="lesson-section-title" id="table-structure">Table Structure</h2>
""" + code("""<table>
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Role</th>
      <th scope="col">Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice</td>
      <td>Engineer</td>
      <td>$120,000</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>Designer</td>
      <td>$105,000</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="2">Average</td>
      <td>$112,500</td>
    </tr>
  </tfoot>
</table>
""") + """
<h2 class="lesson-section-title" id="spanning">Spanning Cells</h2>
""" + code("""<!-- colspan spans across multiple columns -->
<td colspan="2">Covers two columns</td>

<!-- rowspan spans across multiple rows -->
<td rowspan="3">Covers three rows</td>
""") + """
<h2 class="lesson-section-title" id="styling-tables">Styling Tables</h2>
""" + code("""table {
  width: 100%;
  border-collapse: collapse; /* removes double borders */
  font-size: 0.9rem;
}

th, td {
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
}

th {
  background: #1e3a8a;
  color: white;
  font-weight: 600;
}

/* Alternating row colours */
tbody tr:nth-child(even) {
  background: #f8fafc;
}

tbody tr:hover {
  background: #eff6ff;
}
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Never use tables for page layout. That was a 1990s technique. Tables are for data — schedules, pricing grids, comparison charts, spreadsheet-style information.</p>
</div>
""",
    kc=[
        ("What is the purpose of thead, tbody, and tfoot?","table-structure"),
        ("How do you make a cell span two columns?","spanning"),
        ("What does border-collapse: collapse do?","styling-tables"),
    ],
    assignments=[
        "Build a monthly expense table with categories, amounts, and a total row using tfoot.",
        "Style it with alternating row colours and a hover highlight.",
        "Read MDN's HTML Tables guide linked below.",
    ],
    resources=[
        ("MDN — HTML Table Basics","https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics"),
        ("MDN — HTML Table Advanced","https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Advanced"),
        ("YouTube — HTML Tables (Kevin Powell)","https://www.youtube.com/watch?v=SIzHxPL6Sc8"),
    ])

    write("default-styles","Default Styles",
    intro="Every browser applies its own default styles to HTML elements before your CSS runs. Understanding this explains why things look different across browsers — and what to do about it.",
    overview=[
        "Understand what browser default styles are and why they exist.",
        "Know the difference between a CSS reset and a CSS normalizer.",
        "Apply a modern CSS reset to your projects.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-are-defaults">What Are Default Styles?</h2>
<p>When you create an HTML file and open it without any CSS, the browser still applies styles: headings are large and bold, links are blue and underlined, lists have bullet points and indentation. These come from the browser's built-in <strong>user-agent stylesheet</strong>.</p>
<p>The problem is that different browsers (Chrome, Firefox, Safari) have slightly different defaults. An <code>h1</code> might have a different margin in Firefox than in Chrome. These inconsistencies cause layout differences across browsers.</p>

<h2 class="lesson-section-title" id="reset-vs-normalize">Reset vs. Normalize</h2>
<p>Two strategies exist for dealing with defaults:</p>
<ul>
  <li><strong>CSS Reset</strong> — strips away all default styles, giving you a blank slate. You then add back everything you need.</li>
  <li><strong>CSS Normalize</strong> — keeps useful defaults but makes them consistent across browsers. Less work, but you inherit more.</li>
</ul>

<h2 class="lesson-section-title" id="modern-reset">A Modern CSS Reset</h2>
<p>A minimal, practical reset that most professional projects start with:</p>
""" + code("""/* Modern CSS Reset */
*, *::before, *::after {
  box-sizing: border-box;
}

* {
  margin: 0;
  padding: 0;
}

html {
  font-size: 100%;
  scroll-behavior: smooth;
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
  font: inherit; /* form elements do NOT inherit font by default */
}

p, h1, h2, h3, h4, h5, h6 {
  overflow-wrap: break-word;
}
"""),
    kc=[
        ("What is a browser user-agent stylesheet?","what-are-defaults"),
        ("What is the difference between a CSS reset and normalize?","reset-vs-normalize"),
        ("Why do form elements need font: inherit in a reset?","modern-reset"),
    ],
    assignments=[
        "Add the modern CSS reset above to your current project. Notice what changes visually.",
        "Read Josh Comeau's 'A Modern CSS Reset' article linked below — it explains every rule.",
    ],
    resources=[
        ("Josh Comeau — A Modern CSS Reset","https://www.joshwcomeau.com/css/custom-css-reset/"),
        ("MDN — CSS Cascade — User-Agent Styles","https://developer.mozilla.org/en-US/docs/Web/CSS/Cascade"),
        ("YouTube — CSS Resets (Kevin Powell)","https://www.youtube.com/watch?v=eWmDW4zEXt4"),
    ])

    write("css-units","CSS Units",
    intro="CSS has many units for expressing size. Choosing the right unit for each context is one of the most important skills for building layouts that are flexible, accessible, and responsive.",
    overview=[
        "Understand absolute units (px) and when to use them.",
        "Use relative units: em, rem, %, vw, vh.",
        "Choose the right unit for font sizes, spacing, and layout.",
    ],
    body="""
<h2 class="lesson-section-title" id="absolute">Absolute Units</h2>
<p><code>px</code> (pixels) is the only absolute unit you will use in web development. It maps to a consistent size on screen and is predictable. Use it for: borders, box shadows, small fixed dimensions, and media query breakpoints.</p>
""" + code("""border: 1px solid #e2e8f0;
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
""") + """
<h2 class="lesson-section-title" id="relative">Relative Units</h2>
""" + code("""/* rem — relative to the ROOT font size (html element) */
/* Default: 1rem = 16px */
/* Best for: font sizes, spacing (margins, paddings) */
h1 { font-size: 2.5rem; }  /* 40px at default settings */
p  { margin-bottom: 1rem; }

/* em — relative to the PARENT element's font size */
/* Useful for: padding/margin that scales with the element's own font */
button {
  font-size: 1rem;
  padding: 0.75em 1.5em; /* scales if button font-size changes */
}

/* % — relative to the parent element */
/* Best for: widths in a flow layout */
.container { width: 90%; max-width: 1200px; }
.column    { width: 50%; }

/* vw / vh — relative to the viewport (visible screen area) */
/* 1vw = 1% of viewport width, 1vh = 1% of viewport height */
.hero    { min-height: 100vh; }  /* full screen height */
.sidebar { width: 25vw; }

/* ch — relative to the width of the "0" character */
/* Great for constraining line length for readability */
p { max-width: 65ch; }
""") + """
<h2 class="lesson-section-title" id="best-practices">Practical Guidelines</h2>
<ul>
  <li><strong>Font sizes:</strong> use <code>rem</code> — respects user browser font preferences.</li>
  <li><strong>Padding and margins:</strong> use <code>rem</code> for consistency, <code>em</code> when you want it to scale with the element.</li>
  <li><strong>Layout widths:</strong> use <code>%</code> or <code>vw</code> for fluid layouts.</li>
  <li><strong>Line length:</strong> use <code>ch</code> — <code>max-width: 65ch</code> on paragraphs is a classic readability technique.</li>
  <li><strong>Borders and shadows:</strong> use <code>px</code> — these should not scale.</li>
</ul>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Avoid setting font sizes in <code>px</code> — it overrides the user's browser font size preference and harms accessibility. Use <code>rem</code> instead.</p>
</div>
""",
    kc=[
        ("What is the difference between rem and em?","relative"),
        ("What does 1vh equal?","relative"),
        ("Why should you avoid using px for font sizes?","best-practices"),
        ("What unit is ideal for constraining paragraph line length?","best-practices"),
    ],
    assignments=[
        "Refactor a small project to replace all px font sizes with rem values.",
        "Create a full-viewport hero section using vh and vw units.",
        "Read MDN's CSS values and units guide linked below.",
    ],
    resources=[
        ("MDN — CSS Values and Units","https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units"),
        ("CSS Tricks — The Lengths of CSS","https://css-tricks.com/the-lengths-of-css/"),
        ("YouTube — CSS Units (Kevin Powell)","https://www.youtube.com/watch?v=N5wpD9Ov_To"),
    ])

    write("more-text-styles","More Text Styles",
    intro="Typography is one of the biggest levers you have for making a design look professional. This lesson covers the CSS properties that give you precise control over how text looks.",
    overview=[
        "Use font-family, font-weight, and font-style.",
        "Control text with letter-spacing, line-height, and text-transform.",
        "Load custom fonts using Google Fonts and @font-face.",
        "Apply text-shadow and text-overflow.",
    ],
    body="""
<h2 class="lesson-section-title" id="font-properties">Core Font Properties</h2>
""" + code("""body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  font-size: 1rem;       /* base size */
  font-weight: 400;      /* normal */
  font-style: normal;
  line-height: 1.6;      /* unitless — multiplied by font-size */
}

h1 { font-weight: 700; font-size: 2.5rem; }
em { font-style: italic; }
""") + """
<h2 class="lesson-section-title" id="text-properties">Text Properties</h2>
""" + code(""".nav-link {
  text-transform: uppercase;    /* UPPERCASE */
  letter-spacing: 0.1em;        /* space between letters */
  text-decoration: none;        /* remove underline */
}

.card-title {
  white-space: nowrap;           /* prevent wrapping */
  overflow: hidden;
  text-overflow: ellipsis;       /* show ... when text overflows */
  max-width: 200px;
}

.pull-quote {
  text-align: center;
  font-style: italic;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.15);
}
""") + """
<h2 class="lesson-section-title" id="custom-fonts">Loading Custom Fonts</h2>
""" + code("""/* Method 1: Google Fonts (easiest) */
/* Add to <head> in HTML: */
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

/* Then use in CSS: */
body { font-family: 'Inter', sans-serif; }

/* Method 2: @font-face (self-hosted) */
@font-face {
  font-family: 'MyFont';
  src: url('fonts/myfont.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap; /* show fallback font while custom font loads */
}
""") + """
<h2 class="lesson-section-title" id="system-fonts">System Font Stack</h2>
""" + code("""/* Uses the operating system's native font — fast, no loading */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
               Roboto, Helvetica, Arial, sans-serif;
}
"""),
    kc=[
        ("What is the difference between line-height: 1.6 and line-height: 1.6rem?","font-properties"),
        ("How do you show an ellipsis when text overflows its container?","text-properties"),
        ("What does font-display: swap do?","custom-fonts"),
    ],
    assignments=[
        "Style a typographic hierarchy: h1, h2, h3, body text, and a caption using different weights, sizes, and letter-spacing.",
        "Load an Inter or Sora font from Google Fonts and apply it to a project.",
        "Read MDN's Fundamental Text and Font Styling guide linked below.",
    ],
    resources=[
        ("MDN — Fundamental Text and Font Styling","https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals"),
        ("Google Fonts","https://fonts.google.com/"),
        ("YouTube — Typography in CSS (Kevin Powell)","https://www.youtube.com/watch?v=l0GX6ezSw_E"),
    ])

    write("more-css-properties","More CSS Properties",
    intro="This lesson covers a collection of highly useful CSS properties that come up constantly in real projects but did not fit neatly into earlier lessons.",
    overview=[
        "Use overflow to control content that exceeds its container.",
        "Apply opacity and visibility correctly.",
        "Use background shorthand with gradients and multiple values.",
        "Control element stacking with z-index.",
    ],
    body="""
<h2 class="lesson-section-title" id="overflow">overflow</h2>
""" + code(""".card {
  overflow: hidden;    /* clip content that exceeds the box */
  overflow: scroll;    /* always show scrollbars */
  overflow: auto;      /* scrollbars only when needed */
  overflow: visible;   /* default — content flows outside the box */
}

/* Control axes separately */
.code-block {
  overflow-x: auto;   /* horizontal scroll for wide code */
  overflow-y: hidden;
}
""") + """
<h2 class="lesson-section-title" id="opacity-visibility">opacity and visibility</h2>
""" + code(""".faded   { opacity: 0.5; }        /* 50% transparent but still takes up space */
.hidden  { opacity: 0; }           /* invisible but still takes up space */
.gone    { visibility: hidden; }   /* invisible but still takes up space */
.removed { display: none; }        /* invisible AND removed from layout flow */

/* opacity: 0 vs visibility: hidden vs display: none */
/* opacity: 0 — invisible, takes space, can receive events */
/* visibility: hidden — invisible, takes space, cannot receive events */
/* display: none — invisible, no space, no events */
""") + """
<h2 class="lesson-section-title" id="background">background Shorthand</h2>
""" + code(""".hero {
  /* Gradient */
  background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);

  /* Image with fallback colour */
  background: #1e3a8a url('hero.jpg') center/cover no-repeat;

  /* Multiple backgrounds — first listed is on top */
  background:
    linear-gradient(to bottom, rgba(0,0,0,0.4), transparent),
    url('photo.jpg') center/cover no-repeat;
}
""") + """
<h2 class="lesson-section-title" id="z-index">z-index and Stacking Context</h2>
""" + code("""/* z-index only works on positioned elements */
/* (position: relative, absolute, fixed, or sticky) */

.modal-overlay {
  position: fixed;
  z-index: 1000;
}

.dropdown {
  position: absolute;
  z-index: 100;
}

.card {
  position: relative;
  z-index: 1;
}

/* Higher z-index = closer to viewer */
/* Stacking context: a new context is created by position + z-index, */
/* opacity < 1, transform, filter, and a few others */
"""),
    kc=[
        ("What is the difference between overflow: hidden and overflow: auto?","overflow"),
        ("What is the difference between opacity: 0, visibility: hidden, and display: none?","opacity-visibility"),
        ("Why does z-index have no effect on a static element?","z-index"),
    ],
    assignments=[
        "Build a card with overflow: hidden so a hover image scale effect stays clipped to the card boundary.",
        "Create a modal overlay using position: fixed and z-index.",
    ],
    resources=[
        ("MDN — overflow","https://developer.mozilla.org/en-US/docs/Web/CSS/overflow"),
        ("MDN — z-index","https://developer.mozilla.org/en-US/docs/Web/CSS/z-index"),
        ("CSS Tricks — What No One Told You About z-index","https://philipwalton.com/articles/what-no-one-told-you-about-z-index/"),
        ("YouTube — CSS overflow (Kevin Powell)","https://www.youtube.com/watch?v=DFemev-iEBY"),
    ])

    write("advanced-selectors","Advanced Selectors",
    intro="CSS selectors are far more powerful than element, class, and ID. Advanced selectors let you target elements based on their relationship to other elements, their state, and their attributes — often without adding any extra classes to your HTML.",
    overview=[
        "Use combinators: descendant, child, adjacent sibling, general sibling.",
        "Use pseudo-classes: :hover, :focus, :nth-child, :not, :is, :where.",
        "Use pseudo-elements: ::before, ::after, ::placeholder.",
        "Use attribute selectors.",
    ],
    body="""
<h2 class="lesson-section-title" id="combinators">Combinators</h2>
""" + code("""/* Descendant — any p inside .card (any depth) */
.card p { color: #475569; }

/* Child — direct children only */
.nav > li { display: inline-block; }

/* Adjacent sibling — h2 immediately following an img */
img + h2 { margin-top: 1rem; }

/* General sibling — all p elements after an h2 */
h2 ~ p { color: #64748b; }
""") + """
<h2 class="lesson-section-title" id="pseudo-classes">Pseudo-Classes</h2>
""" + code("""/* User state */
a:hover  { color: #2563eb; }
a:focus  { outline: 2px solid #2563eb; }
a:active { color: #1d4ed8; }
input:focus { border-color: #2563eb; }

/* Structural */
li:first-child  { font-weight: bold; }
li:last-child   { border-bottom: none; }
li:nth-child(2) { color: red; }
li:nth-child(odd)  { background: #f8fafc; }
li:nth-child(even) { background: white; }
li:nth-child(3n)   { color: blue; } /* every third */

/* Negation and grouping */
p:not(.intro)  { font-size: 0.9rem; }
:is(h1, h2, h3) { font-family: 'Sora', sans-serif; } /* matches any */
:where(h1, h2, h3) { margin-bottom: 0.5em; } /* zero specificity */

/* Form states */
input:disabled  { opacity: 0.5; cursor: not-allowed; }
input:checked   { accent-color: #2563eb; }
input:required  { border-color: #ef4444; }
input:valid     { border-color: #10b981; }
""") + """
<h2 class="lesson-section-title" id="pseudo-elements">Pseudo-Elements</h2>
""" + code("""/* ::before and ::after — insert generated content */
.card::before {
  content: '';        /* required — even if empty */
  display: block;
  height: 4px;
  background: #2563eb;
  border-radius: 4px 4px 0 0;
}

blockquote::before {
  content: '"';
  font-size: 4rem;
  color: #2563eb;
  line-height: 0;
  vertical-align: -0.4em;
}

/* ::placeholder — style input placeholder text */
input::placeholder {
  color: #94a3b8;
  font-style: italic;
}

/* ::selection — style highlighted text */
::selection {
  background: #2563eb;
  color: white;
}
""") + """
<h2 class="lesson-section-title" id="attribute-selectors">Attribute Selectors</h2>
""" + code("""/* Has the attribute */
[disabled]          { opacity: 0.5; }

/* Exact value */
[type="email"]      { padding-right: 2.5rem; }

/* Starts with */
a[href^="https"]    { color: green; }

/* Ends with */
a[href$=".pdf"]::after { content: ' (PDF)'; }

/* Contains */
[class*="btn-"]     { cursor: pointer; }
"""),
    kc=[
        ("What is the difference between a descendant selector and a child selector?","combinators"),
        ("What does :nth-child(odd) select?","pseudo-classes"),
        ("What is the difference between :is() and :where()?","pseudo-classes"),
        ("What does the content property do on ::before?","pseudo-elements"),
    ],
    assignments=[
        "Style a navigation menu using only combinators and pseudo-classes — no extra classes.",
        "Add a decorative coloured top border to all cards using ::before.",
        "Work through the advanced selector exercises on CSS Diner linked below.",
    ],
    resources=[
        ("CSS Diner — Selector Game","https://flukeout.github.io/"),
        ("MDN — CSS Selectors","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors"),
        ("YouTube — Advanced CSS Selectors (Kevin Powell)","https://www.youtube.com/watch?v=Bcr70LIJcOk"),
    ])

    write("positioning","Positioning",
    intro="CSS positioning takes elements out of the normal document flow and lets you place them precisely anywhere on the page. Understanding it is essential for navbars, modals, tooltips, and sticky sidebars.",
    overview=[
        "Understand the five position values: static, relative, absolute, fixed, sticky.",
        "Know when each type is appropriate.",
        "Use top, right, bottom, left to place positioned elements.",
        "Understand how positioned elements interact with z-index.",
    ],
    body="""
<h2 class="lesson-section-title" id="static">static (default)</h2>
<p>Every element starts as <code>position: static</code>. It flows in the normal document order. The <code>top/right/bottom/left</code> and <code>z-index</code> properties have no effect on static elements.</p>

<h2 class="lesson-section-title" id="relative">relative</h2>
""" + code(""".nudged {
  position: relative;
  top: 10px;    /* moves DOWN 10px from its normal position */
  left: 20px;   /* moves RIGHT 20px */
}
/* Important: the space the element originally occupied is KEPT */
/* Other elements do not shift to fill the gap */
""") + """
<h2 class="lesson-section-title" id="absolute">absolute</h2>
""" + code("""/* Absolutely positioned elements are REMOVED from normal flow */
/* They position relative to the nearest positioned ancestor */
/* If no positioned ancestor exists, they use the viewport */

.card {
  position: relative; /* establish a positioning context */
}

.badge {
  position: absolute;
  top: 12px;
  right: 12px;
  /* Positioned relative to .card, not the page */
}
""") + """
<h2 class="lesson-section-title" id="fixed">fixed</h2>
""" + code("""/* Fixed relative to the VIEWPORT — stays on screen when scrolling */
.site-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: white;
}

/* Floating action button */
.fab {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 50;
}
""") + """
<h2 class="lesson-section-title" id="sticky">sticky</h2>
""" + code("""/* Sticky is a hybrid: flows normally until a scroll threshold,
   then behaves like fixed relative to its scroll container */

.section-header {
  position: sticky;
  top: 64px;    /* sticks when it reaches 64px from the top of the viewport */
  background: white;
  z-index: 10;
}

/* The element must have a defined parent with overflow to stick within */
"""),
    kc=[
        ("What is the difference between relative and absolute positioning?","absolute"),
        ("What does an absolutely positioned element position itself relative to?","absolute"),
        ("When does a sticky element switch from flowing to fixed?","sticky"),
        ("Why does z-index not work on static elements?","static"),
    ],
    assignments=[
        "Build a card with an absolutely positioned badge (e.g. 'Sale!') in its top-right corner.",
        "Build a sticky header that stays at the top of the viewport while scrolling.",
        "Work through the positioning exercises linked below.",
    ],
    resources=[
        ("MDN — CSS Positioning","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning"),
        ("CSS Tricks — position","https://css-tricks.com/almanac/properties/p/position/"),
        ("YouTube — CSS Position Explained (Kevin Powell)","https://www.youtube.com/watch?v=jx5jmI0UlXU"),
    ])

    write("css-functions","CSS Functions",
    intro="CSS functions let you compute values dynamically — calculating sizes based on context, clamping values to a range, and mixing colours. They make stylesheets more adaptable and maintainable.",
    overview=[
        "Use calc() to compute values from mixed units.",
        "Use min(), max(), and clamp() for responsive sizing.",
        "Use color functions: rgb(), hsl(), and modern oklch().",
    ],
    body="""
<h2 class="lesson-section-title" id="calc">calc()</h2>
<p><code>calc()</code> lets you perform arithmetic with different units — something impossible otherwise:</p>
""" + code(""".sidebar {
  width: calc(300px - 2rem);  /* mix px and rem */
}

.full-bleed {
  width: calc(100% + 4rem);
  margin-left: -2rem;
}

/* Useful with CSS variables */
:root { --nav-height: 64px; }
.main {
  min-height: calc(100vh - var(--nav-height));
}
""") + """
<h2 class="lesson-section-title" id="min-max-clamp">min(), max(), and clamp()</h2>
""" + code("""/* min() — use the SMALLEST value */
.container {
  width: min(90%, 1200px);  /* 90% on small screens, max 1200px */
}

/* max() — use the LARGEST value */
.sidebar {
  width: max(200px, 20%);  /* at least 200px, grows with viewport */
}

/* clamp(minimum, preferred, maximum) */
/* The preferred value is usually a viewport-relative unit */
h1 {
  font-size: clamp(1.75rem, 5vw, 4rem);
  /* never smaller than 1.75rem, never larger than 4rem */
  /* scales smoothly with viewport width in between */
}

.content {
  padding: clamp(1rem, 5%, 4rem);
}
""") + """
<h2 class="lesson-section-title" id="color-functions">Color Functions</h2>
""" + code("""/* rgb() / rgba() — red, green, blue (0-255), optional alpha (0-1) */
color: rgb(37, 99, 235);
background: rgba(37, 99, 235, 0.1);

/* hsl() — hue (0-360°), saturation (%), lightness (%) */
/* More intuitive for creating colour variations */
color: hsl(217, 91%, 60%);
background: hsl(217, 91%, 97%);  /* same hue, much lighter */

/* Modern: oklch() — perceptually uniform, great for design systems */
color: oklch(60% 0.2 240);

/* CSS relative colour syntax (modern) */
.lighter {
  background: hsl(from var(--brand-color) h s calc(l + 20%));
}
"""),
    kc=[
        ("When would you use calc() instead of a plain value?","calc"),
        ("What does clamp(1rem, 5vw, 3rem) mean?","min-max-clamp"),
        ("What advantage does hsl() have over rgb() for colour design?","color-functions"),
    ],
    assignments=[
        "Refactor a project to use clamp() for all heading font sizes — eliminating media queries for typography.",
        "Use calc() to create a full-bleed section inside a centred container.",
    ],
    resources=[
        ("MDN — calc()","https://developer.mozilla.org/en-US/docs/Web/CSS/calc"),
        ("MDN — clamp()","https://developer.mozilla.org/en-US/docs/Web/CSS/clamp"),
        ("YouTube — CSS clamp() (Kevin Powell)","https://www.youtube.com/watch?v=U9VF-4euyRo"),
        ("CSS Tricks — A Complete Guide to CSS Functions","https://css-tricks.com/complete-guide-to-css-functions/"),
    ])

    write("custom-properties","Custom Properties",
    intro="CSS custom properties (CSS variables) let you define reusable values once and reference them everywhere. They are the foundation of maintainable design systems and dynamic theming.",
    overview=[
        "Declare and use CSS custom properties.",
        "Understand scope and inheritance with custom properties.",
        "Build a colour theme using custom properties.",
        "Update custom properties with JavaScript for dynamic theming.",
    ],
    body="""
<h2 class="lesson-section-title" id="declaring">Declaring and Using Custom Properties</h2>
""" + code("""/* Declare on :root to make globally available */
:root {
  --color-primary:   #2563eb;
  --color-secondary: #64748b;
  --color-bg:        #0f172a;
  --color-surface:   #1e293b;
  --color-text:      #e2e8f0;

  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'IBM Plex Mono', monospace;

  --radius-sm: 4px;
  --radius:    8px;
  --radius-lg: 16px;

  --shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

/* Use with var() */
.button {
  background: var(--color-primary);
  border-radius: var(--radius);
  font-family: var(--font-sans);
}

/* var() with a fallback value */
color: var(--color-accent, #f59e0b);  /* uses #f59e0b if --color-accent is not defined */
""") + """
<h2 class="lesson-section-title" id="scope">Scope and Inheritance</h2>
""" + code("""/* Custom properties are scoped and inherited */

:root { --color: blue; }

.card {
  --color: red;         /* overrides within .card and its children */
  color: var(--color);  /* red */
}

.card p {
  color: var(--color);  /* also red — inherits from .card */
}

p {
  color: var(--color);  /* blue — no .card ancestor */
}
""") + """
<h2 class="lesson-section-title" id="theming">Dark / Light Theme</h2>
""" + code(""":root {
  --bg:      #ffffff;
  --surface: #f8fafc;
  --text:    #0f172a;
}

[data-theme="dark"] {
  --bg:      #0f172a;
  --surface: #1e293b;
  --text:    #e2e8f0;
}

body {
  background: var(--bg);
  color: var(--text);
}
""") + code("""// Toggle theme with JavaScript
const btn = document.querySelector('#theme-toggle');
btn.addEventListener('click', () => {
  const isDark = document.documentElement.dataset.theme === 'dark';
  document.documentElement.dataset.theme = isDark ? 'light' : 'dark';
});
"""),
    kc=[
        ("How do you declare a CSS custom property?","declaring"),
        ("What is the scope of a custom property declared on :root?","scope"),
        ("How do you provide a fallback value with var()?","declaring"),
    ],
    assignments=[
        "Refactor a project to use CSS variables for all colours, spacing values, and border radii.",
        "Implement a working dark/light mode toggle using a data-theme attribute and CSS custom properties.",
    ],
    resources=[
        ("MDN — Using CSS Custom Properties","https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties"),
        ("CSS Tricks — A Complete Guide to Custom Properties","https://css-tricks.com/a-complete-guide-to-custom-properties/"),
        ("YouTube — CSS Variables (Kevin Powell)","https://www.youtube.com/watch?v=PHO6TBq_auI"),
    ])

    write("browser-compatibility","Browser Compatibility",
    intro="Not every browser supports every CSS feature. This lesson covers how to check compatibility, write resilient CSS, and use the tools that handle most compatibility work automatically.",
    overview=[
        "Use Can I Use to check browser support for CSS features.",
        "Write fallbacks for unsupported features.",
        "Understand vendor prefixes and when they are needed.",
        "Use Autoprefixer in a build workflow.",
    ],
    body="""
<h2 class="lesson-section-title" id="caniuse">Checking Support</h2>
<p>Before using a newer CSS feature, check <a href="https://caniuse.com" target="_blank" rel="noopener">caniuse.com</a>. Search for the feature and see which browsers and versions support it. Pay attention to your target audience — a site for developers can safely use cutting-edge features; a site for general consumers should be more conservative.</p>

<h2 class="lesson-section-title" id="fallbacks">Writing Fallbacks</h2>
<p>CSS ignores properties it does not understand — this is a feature, not a bug. You can stack declarations to provide progressively better experiences:</p>
""" + code(""".element {
  /* Fallback for old browsers */
  color: #2563eb;
  background: #f0f9ff;

  /* Modern enhancement — old browsers just ignore these */
  color: oklch(60% 0.2 240);
  background: color-mix(in oklch, #2563eb 10%, white);
}

/* @supports — feature query */
@supports (display: grid) {
  .layout {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }
}

@supports not (display: grid) {
  .layout {
    display: flex;
    flex-wrap: wrap;
  }
}
""") + """
<h2 class="lesson-section-title" id="prefixes">Vendor Prefixes</h2>
<p>Some CSS features required browser-specific prefixes during development. Most modern features no longer need them, but you will see them in older codebases:</p>
""" + code("""/* Old code you might encounter */
-webkit-transform: rotate(45deg);  /* Chrome, Safari */
-moz-transform: rotate(45deg);     /* Firefox */
-ms-transform: rotate(45deg);      /* IE */
transform: rotate(45deg);          /* standard — always last */
""") + """
<h2 class="lesson-section-title" id="autoprefixer">Autoprefixer</h2>
<p>Writing prefixes manually is error-prone. <strong>Autoprefixer</strong> is a PostCSS plugin that adds prefixes automatically based on a target browser list. Most modern build tools (Vite, Create React App, Next.js) include it automatically.</p>
""" + code("""/* You write: */
.box {
  display: flex;
  user-select: none;
}

/* Autoprefixer outputs: */
.box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-user-select: none;
  user-select: none;
}
"""),
    kc=[
        ("Where do you check browser support for a CSS feature?","caniuse"),
        ("What does @supports do?","fallbacks"),
        ("What is Autoprefixer and what does it do?","autoprefixer"),
    ],
    assignments=[
        "Visit caniuse.com and check support for CSS Grid, CSS custom properties, and the :has() selector.",
        "Add an @supports query to a project to provide a flexbox fallback when grid is unavailable.",
    ],
    resources=[
        ("Can I Use — Browser Compatibility","https://caniuse.com/"),
        ("MDN — @supports","https://developer.mozilla.org/en-US/docs/Web/CSS/@supports"),
        ("Autoprefixer","https://autoprefixer.github.io/"),
        ("YouTube — Browser Compatibility CSS (Kevin Powell)","https://www.youtube.com/watch?v=nn_-pSNOEKE"),
    ])

    write("form-basics","Form Basics",
    intro="Forms are how users interact with web applications — logging in, searching, submitting data. This lesson covers how to build accessible, well-structured HTML forms.",
    overview=[
        "Build a form with input, select, textarea, and button elements.",
        "Use label elements correctly for accessibility.",
        "Group related fields with fieldset and legend.",
        "Understand the different input types.",
    ],
    body="""
<h2 class="lesson-section-title" id="form-structure">Form Structure</h2>
""" + code("""<form action="/submit" method="POST">

  <!-- Label + input pair — always link them -->
  <div class="field">
    <label for="email">Email address</label>
    <input
      type="email"
      id="email"
      name="email"
      placeholder="you@example.com"
      required
      autocomplete="email"
    >
  </div>

  <div class="field">
    <label for="password">Password</label>
    <input
      type="password"
      id="password"
      name="password"
      minlength="8"
      required
    >
  </div>

  <button type="submit">Sign In</button>

</form>
""") + """
<h2 class="lesson-section-title" id="input-types">Input Types</h2>
""" + code("""<input type="text">        <!-- plain text -->
<input type="email">       <!-- validates email format -->
<input type="password">    <!-- hides characters -->
<input type="number">      <!-- numeric keyboard on mobile -->
<input type="tel">         <!-- phone keyboard on mobile -->
<input type="url">         <!-- validates URL format -->
<input type="date">        <!-- date picker -->
<input type="checkbox">    <!-- boolean on/off -->
<input type="radio">       <!-- one choice from a group -->
<input type="range">       <!-- slider -->
<input type="file">        <!-- file upload -->
<input type="search">      <!-- with clear button on mobile -->
<input type="hidden">      <!-- not shown, sent with form data -->
""") + """
<h2 class="lesson-section-title" id="other-inputs">Other Form Elements</h2>
""" + code("""<!-- Multi-line text input -->
<textarea id="message" name="message" rows="4" cols="50"></textarea>

<!-- Dropdown select -->
<select id="country" name="country">
  <option value="">Select a country</option>
  <option value="et">Ethiopia</option>
  <option value="us">United States</option>
  <option value="gb">United Kingdom</option>
</select>

<!-- Grouping related fields -->
<fieldset>
  <legend>Delivery address</legend>
  <label for="street">Street</label>
  <input type="text" id="street" name="street">
  <label for="city">City</label>
  <input type="text" id="city" name="city">
</fieldset>
""") + """
<h2 class="lesson-section-title" id="styling-forms">Styling Forms</h2>
""" + code(""".field {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  margin-bottom: 1.25rem;
}

label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #374151;
}

input, textarea, select {
  padding: 0.6rem 0.85rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 1rem;
  font-family: inherit;      /* form elements do not inherit font */
  transition: border-color 0.15s;
}

input:focus {
  outline: none;
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
}
"""),
    kc=[
        ("Why must every input have a matching label?","form-structure"),
        ("What is the purpose of the for attribute on a label?","form-structure"),
        ("What does fieldset do?","other-inputs"),
        ("Why does form CSS need font-family: inherit?","styling-forms"),
    ],
    assignments=[
        "Build a contact form with: name, email, subject (select), message (textarea), and a submit button. Style it fully.",
        "Read MDN's Your First Form guide linked below.",
    ],
    resources=[
        ("MDN — Your First HTML Form","https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form"),
        ("MDN — HTML Form Elements","https://developer.mozilla.org/en-US/docs/Learn/Forms/Basic_native_form_controls"),
        ("YouTube — HTML Forms (Web Dev Simplified)","https://www.youtube.com/watch?v=fNcJuPIZ2WE"),
    ])

    write("form-validation","Form Validation",
    intro="Form validation ensures users submit correct data before it reaches your server. HTML5 provides built-in validation that requires no JavaScript, and CSS lets you style the validation states.",
    overview=[
        "Use HTML5 built-in validation attributes.",
        "Style form states with :valid, :invalid, and :user-invalid.",
        "Provide accessible error messages.",
        "Understand the limits of client-side validation.",
    ],
    body="""
<h2 class="lesson-section-title" id="html5-validation">HTML5 Validation Attributes</h2>
""" + code("""<!-- required — must not be empty -->
<input type="text" required>

<!-- minlength / maxlength — character limits -->
<input type="text" minlength="3" maxlength="50">

<!-- min / max — numeric range -->
<input type="number" min="1" max="100">

<!-- pattern — regex pattern -->
<input type="text" pattern="[A-Za-z]{3}" title="Three letters only">

<!-- type itself validates -->
<input type="email">  <!-- must contain @ and a domain -->
<input type="url">    <!-- must start with http:// or similar -->
""") + """
<h2 class="lesson-section-title" id="css-states">Styling Validation States</h2>
""" + code("""/* :user-invalid — only shows after user has interacted with the field */
/* Better UX than :invalid (which fires immediately on page load) */

input:user-invalid {
  border-color: #ef4444;
  background: #fef2f2;
}

input:user-valid {
  border-color: #10b981;
}

input:user-invalid + .error-message {
  display: block;
}

.error-message {
  display: none;
  color: #ef4444;
  font-size: 0.8rem;
  margin-top: 0.25rem;
}
""") + """
<h2 class="lesson-section-title" id="accessible-errors">Accessible Error Messages</h2>
""" + code("""<!-- Connect error message to input with aria-describedby -->
<div class="field">
  <label for="email">Email</label>
  <input
    type="email"
    id="email"
    name="email"
    aria-describedby="email-error"
    required
  >
  <span id="email-error" class="error-message" role="alert">
    Please enter a valid email address.
  </span>
</div>
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Client-side validation is a UX convenience, not a security measure. Always validate data on the server too — any user can bypass HTML validation using browser DevTools.</p>
</div>
""",
    kc=[
        ("What is the difference between :invalid and :user-invalid?","css-states"),
        ("How do you connect an error message to an input for screen readers?","accessible-errors"),
        ("Why is client-side validation not a security measure?","accessible-errors"),
    ],
    assignments=[
        "Add validation to your contact form from the previous lesson: make fields required, add minlength, and style error states.",
        "Read MDN's Client-Side Form Validation guide linked below.",
    ],
    resources=[
        ("MDN — Client-Side Form Validation","https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation"),
        ("MDN — Constraint Validation","https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation"),
        ("YouTube — HTML Form Validation (Web Dev Simplified)","https://www.youtube.com/watch?v=In0nB0ABaUk"),
    ])

    write("project-sign-up-form","Project: Sign-Up Form",
    intro="Build a polished, accessible sign-up form that uses everything from the Forms section — proper HTML structure, custom styling, and client-side validation.",
    overview=[
        "Build a complete sign-up form with multiple field types.",
        "Apply custom styling that overrides browser defaults.",
        "Add client-side validation with styled error states.",
        "Ensure the form is accessible.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>A full-page layout with a background image or gradient on one side and the form on the other</li>
  <li>Fields: first name, last name, email, phone number, password, confirm password</li>
  <li>All fields required with appropriate validation attributes</li>
  <li>A visual indicator when passwords do not match</li>
  <li>Custom-styled inputs (no browser default appearance)</li>
  <li>A submit button and a link to a hypothetical login page</li>
  <li>Fully accessible: all labels connected, all errors announced</li>
</ul>

<h2 class="lesson-section-title" id="structure">Project Structure</h2>
""" + code("""mkdir ~/devpath-projects/sign-up-form
cd ~/devpath-projects/sign-up-form
git init
touch index.html styles.css script.js
code .
""") + """
<h2 class="lesson-section-title" id="password-check">Password Match Check</h2>
""" + code("""// Check passwords match on input
const password = document.getElementById('password');
const confirm  = document.getElementById('confirm-password');
const error    = document.getElementById('password-error');

function checkPasswords() {
  if (confirm.value && confirm.value !== password.value) {
    confirm.setCustomValidity('Passwords do not match');
    error.textContent = 'Passwords do not match';
  } else {
    confirm.setCustomValidity('');
    error.textContent = '';
  }
}

password.addEventListener('input', checkPasswords);
confirm.addEventListener('input', checkPasswords);
"""),
    kc=[
        ("What method sets a custom validation message on an input?","password-check"),
        ("How do you visually show a validation error without JavaScript?","requirements"),
    ],
    assignments=[
        "Build the sign-up form meeting all requirements above.",
        "Push to GitHub and publish on GitHub Pages.",
    ],
    resources=[
        ("MDN — HTML Forms","https://developer.mozilla.org/en-US/docs/Learn/Forms"),
        ("YouTube — Sign Up Form Project (Kevin Powell)","https://www.youtube.com/watch?v=a1ByMkEOBos"),
    ])

    write("introduction-to-grid","Introduction to Grid",
    intro="CSS Grid is a two-dimensional layout system — it handles rows and columns simultaneously. Where Flexbox excels at one-dimensional layouts, Grid excels at placing items in a defined two-dimensional space.",
    overview=[
        "Understand when Grid is more appropriate than Flexbox.",
        "Activate Grid with display: grid.",
        "Define columns and rows with grid-template-columns and grid-template-rows.",
        "Use the fr unit and repeat() for flexible tracks.",
    ],
    body="""
<h2 class="lesson-section-title" id="grid-vs-flex">Grid vs. Flexbox</h2>
<p>Use <strong>Flexbox</strong> for one-dimensional layouts — a row of buttons, a navigation bar, a set of cards where you mainly care about spacing in one direction.</p>
<p>Use <strong>Grid</strong> for two-dimensional layouts — page structure with header/sidebar/main/footer, image galleries, dashboards where you need precise row and column control.</p>
<p>They are not competitors — you will routinely use both on the same page: Grid for the overall structure, Flexbox for components inside grid areas.</p>

<h2 class="lesson-section-title" id="basics">Grid Basics</h2>
""" + code("""<div class="grid-container">
  <div>One</div>
  <div>Two</div>
  <div>Three</div>
  <div>Four</div>
  <div>Five</div>
  <div>Six</div>
</div>
""") + code(""".grid-container {
  display: grid;

  /* Define three equal columns */
  grid-template-columns: 200px 200px 200px;

  /* Three columns using the fr (fraction) unit */
  grid-template-columns: 1fr 1fr 1fr;

  /* Shorthand with repeat() */
  grid-template-columns: repeat(3, 1fr);

  /* Define rows */
  grid-template-rows: 100px auto 100px;

  /* Gap between cells */
  gap: 1rem;
  row-gap: 1rem;
  column-gap: 2rem;
}
""") + """
<h2 class="lesson-section-title" id="fr-unit">The fr Unit</h2>
""" + code(""".layout {
  display: grid;
  grid-template-columns: 250px 1fr 1fr;
  /* Fixed 250px sidebar, two equal remaining columns */
}

.layout-2 {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  /* Middle column gets twice the space of either side column */
}
""") + """
<h2 class="lesson-section-title" id="auto-fit">Responsive Grids with auto-fit</h2>
""" + code(""".card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}
/* Cards fill the available space
   When the container gets too narrow for 250px cards they wrap
   No media queries needed */
"""),
    kc=[
        ("When should you use Grid instead of Flexbox?","grid-vs-flex"),
        ("What does the fr unit represent?","fr-unit"),
        ("What does repeat(auto-fit, minmax(250px, 1fr)) do?","auto-fit"),
    ],
    assignments=[
        "Create a three-column card grid using CSS Grid with auto-fit and minmax. Resize the browser and observe it adapting.",
        "Play CSS Grid Garden (linked below) — all levels.",
    ],
    resources=[
        ("CSS Grid Garden — Learn Grid with a game","https://cssgridgarden.com/"),
        ("CSS Tricks — A Complete Guide to Grid","https://css-tricks.com/snippets/css/complete-guide-grid/"),
        ("MDN — CSS Grid Layout","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Grids"),
        ("YouTube — CSS Grid in 20 Minutes (Traversy Media)","https://www.youtube.com/watch?v=jV8B24rSN5o"),
    ])

    write("creating-a-grid","Creating a Grid",
    intro="Now that you understand Grid's core concepts, this lesson goes deeper into defining grid tracks, controlling implicit grids, and using grid-template-areas for readable layouts.",
    overview=[
        "Define explicit columns and rows.",
        "Understand implicit grid tracks created automatically.",
        "Use grid-template-areas for named layout zones.",
        "Control implicit track sizing with grid-auto-rows and grid-auto-columns.",
    ],
    body="""
<h2 class="lesson-section-title" id="explicit-implicit">Explicit vs. Implicit Grids</h2>
<p>The tracks you define with <code>grid-template-columns</code> and <code>grid-template-rows</code> form the <strong>explicit grid</strong>. When items exceed those defined tracks, the browser automatically creates new rows — these are <strong>implicit tracks</strong>.</p>
""" + code(""".grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 200px;  /* only one explicit row */

  /* Control the size of auto-created rows */
  grid-auto-rows: 150px;

  /* Or use minmax so rows adapt to content */
  grid-auto-rows: minmax(150px, auto);
}
""") + """
<h2 class="lesson-section-title" id="template-areas">grid-template-areas</h2>
<p>Named areas give your grid a readable, visual structure right in your CSS:</p>
""" + code(""".page {
  display: grid;
  grid-template-columns: 260px 1fr;
  grid-template-rows: 64px 1fr 60px;
  grid-template-areas:
    "header  header"
    "sidebar main"
    "footer  footer";
  min-height: 100vh;
  gap: 0;
}

.site-header { grid-area: header;  background: #1e3a8a; }
.sidebar     { grid-area: sidebar; background: #f8fafc; }
.main        { grid-area: main; }
.site-footer { grid-area: footer;  background: #1e3a8a; }
""") + """
<h2 class="lesson-section-title" id="shorthand">grid Shorthand</h2>
""" + code(""".grid {
  /* grid: rows / columns */
  grid: auto 1fr auto / 260px 1fr;

  /* Or define everything including areas */
  grid:
    "header header" 64px
    "sidebar main"  1fr
    "footer footer" 60px
    / 260px 1fr;
}
"""),
    kc=[
        ("What is the difference between explicit and implicit grid tracks?","explicit-implicit"),
        ("What does grid-auto-rows do?","explicit-implicit"),
        ("How do you assign an element to a named grid area?","template-areas"),
    ],
    assignments=[
        "Build a full-page layout (header, sidebar, main content, footer) using grid-template-areas.",
        "Create a photo gallery where images automatically create new rows using grid-auto-rows.",
    ],
    resources=[
        ("MDN — Grid Template Areas","https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas"),
        ("CSS Tricks — Complete Guide to Grid","https://css-tricks.com/snippets/css/complete-guide-grid/"),
        ("YouTube — grid-template-areas (Kevin Powell)","https://www.youtube.com/watch?v=d1BCT2yrLgo"),
    ])

    write("positioning-grid-elements","Positioning Grid Elements",
    intro="So far grid items have been placed automatically. This lesson covers how to manually position and span items across specific rows and columns.",
    overview=[
        "Use grid-column and grid-row to place items manually.",
        "Span items across multiple tracks.",
        "Use grid line numbers and named lines.",
        "Use the span keyword for relative sizing.",
    ],
    body="""
<h2 class="lesson-section-title" id="line-numbers">Grid Line Numbers</h2>
<p>Grid lines are numbered starting from 1 on the left/top. A 3-column grid has 4 vertical lines (1, 2, 3, 4) and negative numbers count from the opposite end (-1 is the last line).</p>
""" + code(""".grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(3, 100px);
  gap: 1rem;
}

/* Place an item from column line 1 to 3 */
.featured {
  grid-column: 1 / 3;   /* start / end */
  grid-row: 1 / 2;
}

/* Shorthand: start / span count */
.wide {
  grid-column: 1 / span 3;  /* starts at 1, spans 3 columns */
  grid-row: 2 / span 2;     /* starts at 2, spans 2 rows */
}

/* Reach the last line with -1 */
.full-width {
  grid-column: 1 / -1;  /* spans all columns regardless of count */
}
""") + """
<h2 class="lesson-section-title" id="named-lines">Named Lines</h2>
""" + code(""".grid {
  grid-template-columns:
    [content-start] 1fr 1fr [content-end]
    [sidebar-start] 300px [sidebar-end];
}

.article {
  grid-column: content-start / content-end;
}
.aside {
  grid-column: sidebar-start / sidebar-end;
}
""") + """
<h2 class="lesson-section-title" id="auto-placement">Auto Placement Control</h2>
""" + code(""".grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);

  /* dense: fills gaps left by large items */
  grid-auto-flow: row dense;
}

.large-item {
  grid-column: span 2;  /* takes two columns */
}
"""),
    kc=[
        ("How do you make a grid item span three columns?","line-numbers"),
        ("What does grid-column: 1 / -1 mean?","line-numbers"),
        ("What does grid-auto-flow: dense do?","auto-placement"),
    ],
    assignments=[
        "Build a magazine-style layout where the featured article spans two columns and one featured image spans the full width.",
        "Create a dashboard layout with differently sized widgets using manual placement.",
    ],
    resources=[
        ("MDN — Line-Based Placement with CSS Grid","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Grid_layout_using_line-based_placement"),
        ("CSS Tricks — Complete Guide to Grid","https://css-tricks.com/snippets/css/complete-guide-grid/"),
        ("YouTube — CSS Grid Item Placement (Kevin Powell)","https://www.youtube.com/watch?v=M3qBpPw77qo"),
    ])

    write("advanced-grid-properties","Advanced Grid Properties",
    intro="This lesson covers the remaining Grid properties that round out your toolkit: alignment inside grid cells, subgrid for nested alignment, and the masonry-style layout pattern.",
    overview=[
        "Use justify-items, align-items, justify-self, and align-self within grid.",
        "Understand subgrid for aligning nested grid items.",
        "Use place-items and place-self shorthand.",
    ],
    body="""
<h2 class="lesson-section-title" id="alignment">Alignment in Grid</h2>
""" + code(""".grid {
  display: grid;
  grid-template-columns: repeat(3, 200px);
  grid-template-rows: repeat(2, 150px);

  /* Align ALL items within their cells */
  justify-items: center;   /* horizontal alignment in cell */
  align-items: center;     /* vertical alignment in cell */

  /* Align the entire grid within its container */
  justify-content: space-between;
  align-content: start;
}

/* Override for a single item */
.special {
  justify-self: start;
  align-self: end;
}

/* Shorthand: place-items = align-items + justify-items */
.grid { place-items: center; }

/* place-self = align-self + justify-self */
.item { place-self: center; }
""") + """
<h2 class="lesson-section-title" id="subgrid">subgrid</h2>
<p>The classic problem: cards in a grid where the card title spans different amounts of text, making buttons misalign across cards. <code>subgrid</code> solves this by making nested grids participate in the parent grid's track definitions:</p>
""" + code(""".card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto;
  gap: 1rem;
}

.card {
  display: grid;
  /* inherit the parent's ROW tracks */
  grid-row: span 3;
  grid-template-rows: subgrid;
  /* Now: title, description, and button in each card
     all align to the same row lines */
}

.card-title   { grid-row: 1; }
.card-desc    { grid-row: 2; }
.card-button  { grid-row: 3; align-self: end; }
""") + """
<h2 class="lesson-section-title" id="responsive-grid">Fully Responsive Grid Patterns</h2>
""" + code(""".card-grid {
  display: grid;
  /* auto-fit: create as many columns as fit at minimum 280px */
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

/* auto-fill vs auto-fit:
   auto-fill: keeps empty tracks (columns exist even if empty)
   auto-fit: collapses empty tracks (only as many as needed) */
"""),
    kc=[
        ("What is the difference between justify-items and justify-self?","alignment"),
        ("What problem does subgrid solve?","subgrid"),
        ("What is the difference between auto-fill and auto-fit?","responsive-grid"),
    ],
    assignments=[
        "Build a card grid where all card buttons align to the same baseline using subgrid.",
        "Experiment with auto-fill vs auto-fit to understand their difference visually.",
    ],
    resources=[
        ("MDN — CSS Grid Layout — Box Alignment","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Box_alignment_in_grid_layout"),
        ("MDN — Subgrid","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Subgrid"),
        ("YouTube — CSS subgrid (Kevin Powell)","https://www.youtube.com/watch?v=Yl8hg2FG20Q"),
    ])

    write("using-flexbox-and-grid","Using Flexbox and Grid",
    intro="Flexbox and Grid are complementary tools, not competitors. This lesson covers the decision framework for choosing between them and how to combine them effectively in real layouts.",
    overview=[
        "Know when to choose Grid and when to choose Flexbox.",
        "Combine both in the same layout.",
        "Understand content-first vs layout-first design.",
    ],
    body="""
<h2 class="lesson-section-title" id="decision-framework">The Decision Framework</h2>
<p>The key question is: <strong>are you laying out content, or are you placing items into a predefined structure?</strong></p>
<ul>
  <li><strong>Use Flexbox</strong> when the layout should adapt to the content — items grow and shrink based on what they contain. Navigation bars, button groups, card rows where you want items to fill available space.</li>
  <li><strong>Use Grid</strong> when you have a predefined layout structure that items should fit into. Page layouts, dashboards, galleries where rows and columns must align across items.</li>
</ul>
""" + code("""/* Page structure — Grid */
.page {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "footer";
  min-height: 100vh;
}

/* Navigation inside the header — Flexbox */
.site-header {
  grid-area: header;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
}

/* Card grid — Grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

/* Card interior — Flexbox */
.card {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.card .card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto; /* push to bottom */
}
""") + """
<h2 class="lesson-section-title" id="common-patterns">Common Combination Patterns</h2>
""" + code("""/* Holy Grail Layout — Grid for structure */
.holy-grail {
  display: grid;
  grid-template:
    "header header header" 64px
    "nav    main   aside"  1fr
    "footer footer footer" 60px
    / 200px 1fr 200px;
  min-height: 100vh;
}

/* Inside each section — Flexbox for component layout */
.main-content {
  grid-area: main;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 2rem;
}
"""),
    kc=[
        ("When should you choose Flexbox over Grid?","decision-framework"),
        ("When should you choose Grid over Flexbox?","decision-framework"),
        ("Is it acceptable to nest Flexbox inside a Grid area?","common-patterns"),
    ],
    assignments=[
        "Build a full page layout using Grid for structure and Flexbox for every component inside the layout.",
        "Refactor a previous Flexbox-only layout and identify which parts should be Grid.",
    ],
    resources=[
        ("MDN — Relationship of Grid Layout to Other Layout Methods","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Relationship_of_grid_layout_with_other_layout_methods"),
        ("CSS Tricks — Does CSS Grid Replace Flexbox?","https://css-tricks.com/css-grid-replace-flexbox/"),
        ("YouTube — Grid vs Flexbox (Kevin Powell)","https://www.youtube.com/watch?v=3elGSZSWTbM"),
    ])

    write("project-admin-dashboard","Project: Admin Dashboard",
    intro="Build a fully functional admin dashboard layout — the capstone of the Grid section. This project requires CSS Grid for the overall layout and Flexbox for components throughout.",
    overview=[
        "Build a complete admin dashboard using CSS Grid.",
        "Use Flexbox for navigation and component layouts.",
        "Apply custom properties for consistent theming.",
        "Make it responsive.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>Sidebar navigation</strong> — fixed width, full height, with logo and nav links</li>
  <li><strong>Header bar</strong> — across the top of the main area, with search and user info</li>
  <li><strong>Stats cards</strong> — a row of 4 metric cards</li>
  <li><strong>Recent activity</strong> — a table or list of recent actions</li>
  <li><strong>Charts/data section</strong> — two side-by-side data panels</li>
  <li>Responsive: sidebar collapses on mobile</li>
</ul>

<h2 class="lesson-section-title" id="layout-structure">Layout Structure</h2>
""" + code("""/* Overall layout */
.app {
  display: grid;
  grid-template-columns: 260px 1fr;
  grid-template-rows: 1fr;
  min-height: 100vh;
}

.sidebar { grid-column: 1; }

.main-area {
  grid-column: 2;
  display: grid;
  grid-template-rows: 64px 1fr;
}

.header { /* top bar */ }

.content {
  padding: 2rem;
  display: grid;
  grid-template-columns: repeat(4, 1fr);  /* stats row */
  grid-template-rows: auto auto;
  gap: 1.5rem;
}

/* Stats cards span one column each */
.stat-card { grid-column: span 1; }

/* Activity table spans all columns */
.activity  { grid-column: 1 / -1; }

/* Two data panels side by side */
.panel-left  { grid-column: span 2; }
.panel-right { grid-column: span 2; }
""") + code("""mkdir ~/devpath-projects/admin-dashboard
cd ~/devpath-projects/admin-dashboard
git init
touch index.html styles.css
code .
"""),
    kc=[
        ("What CSS layout method is best for the overall page structure?","layout-structure"),
        ("How do you make the activity table span all four columns?","layout-structure"),
    ],
    assignments=[
        "Build the admin dashboard meeting all requirements above.",
        "Push to GitHub and publish on GitHub Pages.",
    ],
    resources=[
        ("CSS Tricks — Complete Guide to Grid","https://css-tricks.com/snippets/css/complete-guide-grid/"),
        ("YouTube — CSS Grid Admin Dashboard (Traversy Media)","https://www.youtube.com/watch?v=moBhzSC455o"),
    ])

    write("introduction-to-web-accessibility","Introduction to Web Accessibility",
    intro="Web accessibility means building websites that work for everyone — including people who use screen readers, keyboard-only navigation, or who have visual, motor, or cognitive differences. It is not optional.",
    overview=[
        "Understand what web accessibility is and why it matters.",
        "Know the four principles of accessibility (POUR).",
        "Understand the difference between assistive technology types.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-is-a11y">What Is Accessibility?</h2>
<p>Roughly 15% of the world's population lives with some form of disability. Web accessibility (often abbreviated <strong>a11y</strong> — the 11 letters between 'a' and 'y') ensures your websites work for all of them. This includes:</p>
<ul>
  <li><strong>Visual</strong> — blindness, low vision, colour blindness</li>
  <li><strong>Motor</strong> — cannot use a mouse, uses keyboard only or switch controls</li>
  <li><strong>Hearing</strong> — deafness or hearing impairment</li>
  <li><strong>Cognitive</strong> — dyslexia, ADHD, memory or attention differences</li>
</ul>
<p>Beyond being the right thing to do, accessibility is often a legal requirement and improves usability for everyone — captions help people in noisy environments; keyboard navigation helps power users; clear language helps non-native speakers.</p>

<h2 class="lesson-section-title" id="pour">The POUR Principles</h2>
<p>The Web Content Accessibility Guidelines (WCAG) organise accessibility around four principles. Content must be:</p>
<ol>
  <li><strong>Perceivable</strong> — can be perceived by all senses (provide alt text, captions, sufficient contrast).</li>
  <li><strong>Operable</strong> — can be operated by all input methods (keyboard navigable, no seizure-inducing content).</li>
  <li><strong>Understandable</strong> — content and UI are clear (plain language, predictable behaviour, helpful errors).</li>
  <li><strong>Robust</strong> — works reliably across browsers, devices, and assistive technologies.</li>
</ol>

<h2 class="lesson-section-title" id="assistive-tech">Assistive Technologies</h2>
<ul>
  <li><strong>Screen readers</strong> — announce page content aloud (NVDA, JAWS, VoiceOver, TalkBack).</li>
  <li><strong>Keyboard navigation</strong> — no mouse; Tab to move between interactive elements, Enter/Space to activate.</li>
  <li><strong>Switch controls</strong> — single buttons for people with limited motor function.</li>
  <li><strong>Screen magnifiers</strong> — zoom into portions of the screen.</li>
  <li><strong>Voice control</strong> — navigate and interact by speaking.</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Try navigating your own website using only the keyboard (Tab, Shift+Tab, Enter, Space, arrow keys). If you get stuck, so will your users who rely on keyboard navigation.</p>
</div>
""",
    kc=[
        ("What are the four categories of disability that accessibility addresses?","what-is-a11y"),
        ("What do the four POUR principles stand for?","pour"),
        ("Name three types of assistive technology.","assistive-tech"),
    ],
    assignments=[
        "Navigate your most recent project using only the keyboard. Note every place you get stuck or confused.",
        "Install a screen reader (VoiceOver on Mac, NVDA on Windows — both free) and navigate a webpage with your eyes closed.",
        "Read the WebAIM Introduction to Accessibility linked below.",
    ],
    resources=[
        ("WebAIM — Introduction to Web Accessibility","https://webaim.org/intro/"),
        ("MDN — Accessibility","https://developer.mozilla.org/en-US/docs/Learn/Accessibility"),
        ("YouTube — Web Accessibility Introduction (Google Chrome Developers)","https://www.youtube.com/watch?v=20SHvU2PKsM"),
    ])

    write("the-web-content-accessibility-guidelines","The Web Content Accessibility Guidelines (WCAG)",
    intro="WCAG is the internationally recognised standard for web accessibility. Understanding its structure lets you make informed decisions about which requirements apply to your projects.",
    overview=[
        "Understand WCAG's three conformance levels: A, AA, AAA.",
        "Know the most important success criteria for everyday development.",
        "Use automated tools to check WCAG compliance.",
    ],
    body="""
<h2 class="lesson-section-title" id="levels">Conformance Levels</h2>
<p>WCAG organises success criteria into three levels:</p>
<ul>
  <li><strong>Level A</strong> — Minimum. Failing these makes content inaccessible to some users. Example: all images have alt text.</li>
  <li><strong>Level AA</strong> — The standard most legal requirements reference. Most organisations target AA. Example: text contrast ratio of at least 4.5:1.</li>
  <li><strong>Level AAA</strong> — Enhanced. Not required for entire sites but desirable where feasible. Example: contrast ratio of 7:1.</li>
</ul>

<h2 class="lesson-section-title" id="key-criteria">Key Success Criteria for Developers</h2>
""" + code("""/* 1.1.1 Non-text Content (A) — all images have alt text */
<img src="photo.jpg" alt="A description of the photo">

/* 1.4.3 Contrast Minimum (AA) — text contrast ratio ≥ 4.5:1 */
/* Use a contrast checker to verify */

/* 2.1.1 Keyboard (A) — all functionality available via keyboard */
/* Never use outline: none without a replacement focus style */
:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}

/* 2.4.6 Headings and Labels (AA) — headings are descriptive */
/* Good: <h2>Contact Form</h2> */
/* Bad:  <h2>Section</h2> */

/* 3.1.1 Language of Page (A) — html lang attribute */
<html lang="en">

/* 4.1.2 Name, Role, Value (A) — interactive elements have labels */
<button aria-label="Close modal">✕</button>
""") + """
<h2 class="lesson-section-title" id="testing-tools">Testing Tools</h2>
<ul>
  <li><strong>axe DevTools</strong> — Browser extension that audits pages for WCAG issues.</li>
  <li><strong>Chrome Lighthouse</strong> — Built into Chrome DevTools, includes an Accessibility audit.</li>
  <li><strong>WAVE</strong> — Visual overlay showing accessibility errors and warnings.</li>
  <li><strong>Colour Contrast Checker</strong> — webaim.org/resources/contrastchecker/</li>
</ul>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Automated tools catch roughly 30% of accessibility issues. Manual testing — especially keyboard navigation and screen reader testing — is essential for the rest.</p>
</div>
""",
    kc=[
        ("What is the difference between WCAG Level A and Level AA?","levels"),
        ("What contrast ratio does WCAG AA require for normal text?","key-criteria"),
        ("Why can automated tools not catch all accessibility issues?","testing-tools"),
    ],
    assignments=[
        "Run Chrome Lighthouse on one of your projects. Read the Accessibility score breakdown and fix at least three issues.",
        "Install the axe DevTools extension and audit your sign-up form.",
    ],
    resources=[
        ("WCAG 2.1 Quick Reference","https://www.w3.org/WAI/WCAG21/quickref/"),
        ("WebAIM — WCAG 2 Checklist","https://webaim.org/standards/wcag/checklist"),
        ("Chrome Lighthouse — Accessibility","https://developer.chrome.com/docs/lighthouse/accessibility/"),
        ("YouTube — WCAG Explained (Kevin Powell)","https://www.youtube.com/watch?v=vMKRc3TmFoE"),
    ])

    write("accessible-colors","Accessible Colors",
    intro="Colour contrast is one of the most common accessibility failures on the web. This lesson covers how to choose colours that meet WCAG standards and work for people with colour vision deficiencies.",
    overview=[
        "Understand contrast ratio and how it is calculated.",
        "Meet WCAG AA and AAA contrast requirements.",
        "Design for colour blindness.",
        "Use tools to check and fix contrast issues.",
    ],
    body="""
<h2 class="lesson-section-title" id="contrast-ratio">Contrast Ratio</h2>
<p>Contrast ratio compares the relative luminance of two colours on a scale from 1:1 (identical) to 21:1 (black on white). WCAG requirements:</p>
<ul>
  <li><strong>Normal text (below 18pt / 14pt bold):</strong> 4.5:1 minimum (AA), 7:1 enhanced (AAA)</li>
  <li><strong>Large text (18pt+ / 14pt+ bold):</strong> 3:1 minimum (AA), 4.5:1 enhanced (AAA)</li>
  <li><strong>UI components and graphical objects:</strong> 3:1 minimum (AA)</li>
</ul>

<h2 class="lesson-section-title" id="checking">Checking Contrast</h2>
""" + code("""/* Common contrast issues */

/* FAIL — 2.3:1 ratio — light grey on white */
.low-contrast {
  color: #aaaaaa;
  background: #ffffff;
}

/* PASS AA — 4.6:1 ratio */
.good-contrast {
  color: #595959;
  background: #ffffff;
}

/* PASS AA — dark blue on white — 8.6:1 */
.high-contrast {
  color: #1e3a8a;
  background: #ffffff;
}

/* For dark backgrounds: use light foreground colours */
.dark-bg {
  background: #0f172a;
  color: #e2e8f0; /* 14.5:1 — excellent */
}
""") + """
<h2 class="lesson-section-title" id="color-blindness">Designing for Colour Blindness</h2>
<p>About 8% of men have some form of colour vision deficiency. Red-green colour blindness is most common. The rule: <strong>never use colour as the only way to convey information</strong>.</p>
""" + code("""<!-- BAD: only colour distinguishes required fields -->
<label style="color: red">Email *</label>

<!-- GOOD: colour + text + icon -->
<label>
  Email
  <span class="required" aria-label="required">*</span>
</label>

<!-- BAD: error state communicated only by red border -->
input.error { border-color: red; }

<!-- GOOD: colour + icon + text message -->
<div class="field">
  <input class="error" aria-describedby="email-error">
  <span id="email-error" class="error-message">
    ⚠ Please enter a valid email address
  </span>
</div>
"""),
    kc=[
        ("What is the minimum contrast ratio for normal body text at WCAG AA?","contrast-ratio"),
        ("Why should you never use colour as the only way to convey information?","color-blindness"),
        ("What tool can you use to check contrast ratio?","checking"),
    ],
    assignments=[
        "Check the contrast ratio of every colour combination in one of your projects using WebAIM's contrast checker.",
        "Find and fix any failing contrast ratios.",
        "Enable Chrome's colour blindness emulation (DevTools → Rendering → Emulate vision deficiencies) and check your UI.",
    ],
    resources=[
        ("WebAIM — Colour Contrast Checker","https://webaim.org/resources/contrastchecker/"),
        ("MDN — Colour and Accessibility","https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG/Perceivable/Color_contrast"),
        ("YouTube — Accessible Colour Design (Google Chrome Developers)","https://www.youtube.com/watch?v=SL_YcLbG9B0"),
    ])

    write("keyboard-navigation","Keyboard Navigation",
    intro="Many users navigate entirely by keyboard — people with motor disabilities, power users, and screen reader users. Building keyboard-accessible sites is a core accessibility requirement.",
    overview=[
        "Understand how keyboard navigation works in browsers.",
        "Manage focus correctly with tabindex.",
        "Style focus indicators that are visible and attractive.",
        "Avoid common keyboard accessibility pitfalls.",
    ],
    body="""
<h2 class="lesson-section-title" id="how-it-works">How Keyboard Navigation Works</h2>
<ul>
  <li><kbd>Tab</kbd> — moves focus to the next interactive element</li>
  <li><kbd>Shift+Tab</kbd> — moves focus to the previous interactive element</li>
  <li><kbd>Enter</kbd> — activates links and buttons</li>
  <li><kbd>Space</kbd> — activates buttons, checks checkboxes</li>
  <li><kbd>Arrow keys</kbd> — moves within components (radio groups, select dropdowns, carousels)</li>
  <li><kbd>Escape</kbd> — closes modals and dropdowns</li>
</ul>
<p>By default, only naturally focusable elements receive Tab focus: <code>a</code>, <code>button</code>, <code>input</code>, <code>select</code>, <code>textarea</code>.</p>

<h2 class="lesson-section-title" id="tabindex">tabindex</h2>
""" + code("""<!-- tabindex="0" — add to the natural tab order -->
<!-- Use for custom interactive elements that are not buttons -->
<div role="button" tabindex="0" class="custom-card">
  Clickable card
</div>

<!-- tabindex="-1" — focusable by JavaScript but not by Tab -->
<!-- Use for modal content you want to focus programmatically -->
<div id="modal" tabindex="-1">
  Modal content
</div>
// Focus it with JS:
document.getElementById('modal').focus();

<!-- tabindex > 0 — AVOID — creates confusing non-linear tab order -->
""") + """
<h2 class="lesson-section-title" id="focus-styles">Focus Styles</h2>
""" + code("""/* NEVER do this without a replacement */
* { outline: none; } /* kills keyboard navigation */

/* Modern approach — :focus-visible shows outline only for keyboard */
:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 3px;
  border-radius: 2px;
}

/* Remove the outline for mouse clicks (handled by :focus-visible) */
:focus:not(:focus-visible) {
  outline: none;
}

/* Custom focus styles that match your design */
.button:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.5);
}
""") + """
<h2 class="lesson-section-title" id="skip-links">Skip Navigation Links</h2>
""" + code("""<!-- Allow keyboard users to skip to main content -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<nav>...</nav>
<main id="main-content" tabindex="-1">...</main>
""") + code(""".skip-link {
  position: absolute;
  top: -100%;
  left: 1rem;
  background: #2563eb;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0 0 4px 4px;
  transition: top 0.2s;
}

.skip-link:focus {
  top: 0;  /* visible when focused via keyboard */
}
"""),
    kc=[
        ("What is the difference between tabindex 0 and tabindex -1?","tabindex"),
        ("Why should you avoid outline: none without a replacement?","focus-styles"),
        ("What is a skip navigation link and who benefits from it?","skip-links"),
    ],
    assignments=[
        "Add a skip navigation link to your admin dashboard project.",
        "Remove all outline: none declarations from your project and replace them with proper :focus-visible styles.",
        "Navigate your admin dashboard with keyboard only and fix any focus order issues.",
    ],
    resources=[
        ("WebAIM — Keyboard Accessibility","https://webaim.org/techniques/keyboard/"),
        ("MDN — tabindex","https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex"),
        ("YouTube — Focus Styles (Kevin Powell)","https://www.youtube.com/watch?v=Mvu5OMGcdVA"),
    ])

    write("meaningful-text","Meaningful Text",
    intro="The words you choose — in link text, button labels, headings, and alt text — dramatically affect accessibility. Screen reader users often navigate by heading or link lists, so every label must stand alone.",
    overview=[
        "Write link text that makes sense out of context.",
        "Use headings to create a logical document outline.",
        "Write alt text that conveys the meaning of images.",
        "Use plain language and clear error messages.",
    ],
    body="""
<h2 class="lesson-section-title" id="link-text">Meaningful Link Text</h2>
<p>Screen reader users can call up a list of all links on a page and navigate between them without surrounding context. "Click here" and "Read more" are useless in that list.</p>
""" + code("""<!-- BAD — meaningless out of context -->
<a href="/docs">Click here</a>
<a href="/blog/css-grid">Read more</a>
<a href="/contact">Here</a>

<!-- GOOD — descriptive and self-contained -->
<a href="/docs">View the documentation</a>
<a href="/blog/css-grid">Read: CSS Grid in Depth</a>
<a href="/contact">Contact the support team</a>

<!-- When the context is visually obvious but not to screen readers -->
<article>
  <h2>CSS Grid in Depth</h2>
  <p>A comprehensive guide to CSS Grid...</p>
  <a href="/blog/css-grid" aria-label="Read CSS Grid in Depth">Read more</a>
</article>
""") + """
<h2 class="lesson-section-title" id="headings">Heading Hierarchy</h2>
""" + code("""<!-- BAD — heading levels chosen for visual size -->
<h3>Sign In</h3>           <!-- actually the page title -->
<h5>Email</h5>             <!-- form section label -->

<!-- GOOD — logical outline -->
<h1>Sign In</h1>
<h2>Enter Your Credentials</h2>

<!-- Screen readers navigate by heading — every heading should
     describe the content that follows it -->
""") + """
<h2 class="lesson-section-title" id="plain-language">Plain Language and Error Messages</h2>
""" + code("""<!-- BAD — technical error message -->
<span class="error">
  ERR_FORM_VALIDATION_422: email field regex mismatch
</span>

<!-- GOOD — human, specific, actionable -->
<span class="error" role="alert">
  Please enter a valid email address — for example, name@example.com
</span>

<!-- Error messages should:
     1. Say what went wrong
     2. Say how to fix it
     3. Not blame the user -->
"""),
    kc=[
        ("Why must link text be descriptive without surrounding context?","link-text"),
        ("Why should headings be chosen based on hierarchy, not visual size?","headings"),
        ("What three things should a good error message do?","plain-language"),
    ],
    assignments=[
        "Audit all link text in a project. Replace any 'click here' or 'read more' with descriptive text.",
        "Run your page through a headings outline checker (linked below) to verify your hierarchy is logical.",
    ],
    resources=[
        ("WebAIM — Links and Hypertext","https://webaim.org/techniques/hypertext/"),
        ("MDN — Writing Good Alt Text","https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML#text_alternatives"),
        ("YouTube — Accessible Link Text (Google Chrome Developers)","https://www.youtube.com/watch?v=3f31oufqFSM"),
    ])

    write("wai-aria","WAI-ARIA",
    intro="WAI-ARIA (Web Accessibility Initiative – Accessible Rich Internet Applications) is a set of HTML attributes that communicate the role, state, and properties of elements to assistive technologies — especially for dynamic content that HTML alone cannot describe.",
    overview=[
        "Understand the three types of ARIA attributes: roles, states, and properties.",
        "Know when to use ARIA and when not to.",
        "Apply common ARIA patterns correctly.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-aria">What ARIA Does</h2>
<p>When you build a custom dropdown menu out of divs rather than a native <code>&lt;select&gt;</code>, screen readers have no idea what it is. ARIA lets you annotate it: "this is a listbox, these are options, this option is currently selected."</p>
<p>The first rule of ARIA is: <strong>use native HTML elements before reaching for ARIA</strong>. A <code>&lt;button&gt;</code> already has the correct role, keyboard behaviour, and accessibility semantics. A <code>&lt;div role="button"&gt;</code> requires you to manually add everything the button provides for free.</p>

<h2 class="lesson-section-title" id="roles">ARIA Roles</h2>
""" + code("""<!-- Landmark roles — help screen readers navigate the page -->
<header  role="banner">...</header>    <!-- usually implicit on header -->
<nav     role="navigation">...</nav>  <!-- usually implicit on nav -->
<main    role="main">...</main>        <!-- usually implicit on main -->
<aside   role="complementary">...</aside>
<footer  role="contentinfo">...</footer>
<form    role="form">...</form>

<!-- Widget roles — for custom interactive components -->
<div role="button" tabindex="0">Custom button</div>
<ul  role="listbox">
  <li role="option" aria-selected="true">Option 1</li>
</ul>
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm Delete</h2>
</div>
""") + """
<h2 class="lesson-section-title" id="states-properties">States and Properties</h2>
""" + code("""<!-- aria-label — accessible name when visible text is absent -->
<button aria-label="Close modal">✕</button>

<!-- aria-labelledby — point to an existing element for the name -->
<section aria-labelledby="section-title">
  <h2 id="section-title">Recent Orders</h2>
</section>

<!-- aria-describedby — additional descriptive text -->
<input aria-describedby="password-hint" type="password">
<p id="password-hint">Must be at least 8 characters with one number</p>

<!-- aria-expanded — open/closed state for dropdowns, accordions -->
<button aria-expanded="false" aria-controls="menu">Menu</button>
<ul id="menu" hidden>...</ul>

<!-- aria-hidden — hide decorative elements from screen readers -->
<span aria-hidden="true">🎉</span> Congratulations!

<!-- role="alert" — announce dynamic content immediately -->
<div role="alert" aria-live="polite">
  Form submitted successfully!
</div>
"""),
    kc=[
        ("What is the first rule of ARIA?","what-aria"),
        ("What does aria-label do?","states-properties"),
        ("What does aria-expanded communicate?","states-properties"),
        ("When should you use role='alert'?","states-properties"),
    ],
    assignments=[
        "Add appropriate ARIA attributes to any custom components in your admin dashboard (dropdown menus, modals, tabs).",
        "Read the ARIA Authoring Practices Guide to see correct patterns for common widgets.",
    ],
    resources=[
        ("ARIA Authoring Practices Guide (APG)","https://www.w3.org/WAI/ARIA/apg/"),
        ("MDN — ARIA","https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA"),
        ("YouTube — ARIA Explained (Google Chrome Developers)","https://www.youtube.com/watch?v=g9Qff0b-lHk"),
    ])

    write("introduction-to-responsive-design","Introduction to Responsive Design",
    intro="Responsive design means your website looks and works well on every screen size — from a 375px phone to a 2560px monitor. This lesson introduces the philosophy and tools behind responsive web development.",
    overview=[
        "Define responsive design and its three core ingredients.",
        "Understand the viewport meta tag.",
        "Know the mobile-first approach and why it is preferred.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-is-rwd">What Is Responsive Design?</h2>
<p>Responsive design is an approach where the layout, images, and typography adapt to the available space. A single codebase serves all screen sizes gracefully — no separate mobile site required.</p>
<p>Ethan Marcotte coined the term in 2010 and defined three core ingredients:</p>
<ol>
  <li><strong>Fluid grids</strong> — use relative units (%, fr, vw) instead of fixed pixel widths.</li>
  <li><strong>Flexible images</strong> — images scale within their containers.</li>
  <li><strong>Media queries</strong> — apply different CSS at different viewport widths.</li>
</ol>

<h2 class="lesson-section-title" id="viewport-meta">The Viewport Meta Tag</h2>
<p>Without this tag, mobile browsers render your page at ~980px wide and scale it down — making everything tiny and unreadable:</p>
""" + code("""<!-- Required in every HTML file — already in your boilerplate -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- width=device-width: use the device's actual screen width -->
<!-- initial-scale=1.0:  no initial zoom -->
""") + """
<h2 class="lesson-section-title" id="mobile-first">Mobile-First Approach</h2>
<p>Write your base CSS for the smallest screen first, then progressively enhance for larger screens using <code>min-width</code> media queries.</p>
""" + code("""/* MOBILE FIRST — base styles for small screens */
.container {
  padding: 1rem;
}

.card-grid {
  display: grid;
  grid-template-columns: 1fr;  /* single column on mobile */
  gap: 1rem;
}

/* TABLET — enhance at 640px */
@media (min-width: 640px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* DESKTOP — enhance further at 1024px */
@media (min-width: 1024px) {
  .container { padding: 2rem; }
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Mobile-first is better because mobile CSS is simpler (single column), and overriding simple with complex is easier than overriding complex with simple. It also performs better — mobile devices only download what they need.</p>
</div>
""",
    kc=[
        ("What are the three ingredients of responsive design?","what-is-rwd"),
        ("What does the viewport meta tag do?","viewport-meta"),
        ("Why is mobile-first preferred over desktop-first?","mobile-first"),
    ],
    assignments=[
        "Read Ethan Marcotte's original 'Responsive Web Design' article (linked below) — the article that started it all.",
        "Check each of your current projects to confirm they all have the viewport meta tag.",
    ],
    resources=[
        ("A List Apart — Responsive Web Design (Ethan Marcotte)","https://alistapart.com/article/responsive-web-design/"),
        ("MDN — Responsive Design","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design"),
        ("YouTube — Responsive Web Design Introduction (Kevin Powell)","https://www.youtube.com/watch?v=bn-DQznwa14"),
    ])

    write("natural-responsiveness","Natural Responsiveness",
    intro="Before reaching for media queries, many elements can be made responsive naturally using the CSS techniques you already know. This lesson covers the layout approaches that adapt to screen size without breakpoints.",
    overview=[
        "Use relative units to make text and spacing fluid.",
        "Use auto-fit/auto-fill for responsive grids without media queries.",
        "Apply min(), max(), and clamp() for adaptive sizing.",
        "Use min-width and max-width to contain layouts.",
    ],
    body="""
<h2 class="lesson-section-title" id="fluid-typography">Fluid Typography</h2>
""" + code("""/* WITHOUT clamp: need media queries to control font size */
h1 { font-size: 2rem; }
@media (min-width: 768px)  { h1 { font-size: 2.5rem; } }
@media (min-width: 1024px) { h1 { font-size: 3.5rem; } }

/* WITH clamp: fluid scaling with no breakpoints */
h1 { font-size: clamp(1.75rem, 5vw, 3.5rem); }
/* Never smaller than 1.75rem, never bigger than 3.5rem,
   scales smoothly with viewport in between */

/* A readable line length at any screen size */
p { max-width: 65ch; }
""") + """
<h2 class="lesson-section-title" id="intrinsic-grid">Intrinsic Responsive Grid</h2>
""" + code(""".grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr));
  gap: 1.5rem;
}
/* Breakdown:
   auto-fit: create as many columns as fit
   minmax: each column is at least 280px (or 100% if container is smaller)
   1fr: columns grow to fill available space
   Result: 1 column on phones, 2-3 on tablets, 4 on desktop — no media queries */
""") + """
<h2 class="lesson-section-title" id="contain">max-width and min-width for Containment</h2>
""" + code(""".container {
  width: min(90%, 1200px);  /* 90% on small screens, capped at 1200px */
  margin-inline: auto;       /* centre horizontally */
  padding-inline: 1rem;
}

/* Prevent images from overflowing */
img {
  max-width: 100%;
  height: auto;
}

/* Sidebar that never gets too narrow */
.sidebar {
  width: max(200px, 25%);
}
"""),
    kc=[
        ("What does clamp(1.75rem, 5vw, 3.5rem) mean for font-size?","fluid-typography"),
        ("How does auto-fit with minmax create a responsive grid without media queries?","intrinsic-grid"),
        ("What does width: min(90%, 1200px) do?","contain"),
    ],
    assignments=[
        "Refactor a project's typography to use clamp() for all heading sizes. Remove the corresponding media query font-size overrides.",
        "Replace a media-query-based card grid with auto-fit and minmax.",
    ],
    resources=[
        ("MDN — min()","https://developer.mozilla.org/en-US/docs/Web/CSS/min"),
        ("CSS Tricks — A Complete Guide to CSS Media Queries","https://css-tricks.com/a-complete-guide-to-css-media-queries/"),
        ("YouTube — Intrinsic Responsive Design (Kevin Powell)","https://www.youtube.com/watch?v=VsNAuGkCpQU"),
    ])

    write("responsive-images","Responsive Images",
    intro="Images are typically the largest assets on a page. Serving the right image for each device — the right size, the right format, the right art direction — dramatically improves performance and user experience.",
    overview=[
        "Use max-width: 100% for basic image responsiveness.",
        "Use srcset to serve different resolutions.",
        "Use the picture element for art direction.",
        "Choose the right image format for each use case.",
    ],
    body="""
<h2 class="lesson-section-title" id="basic">Basic Responsive Images</h2>
""" + code("""/* Add to your CSS reset — images never overflow their container */
img {
  max-width: 100%;
  height: auto;
  display: block;
}
""") + """
<h2 class="lesson-section-title" id="srcset">srcset — Serving Different Resolutions</h2>
""" + code("""<!-- srcset: list of images and their widths
     sizes: which image to use at each viewport width -->
<img
  src="hero-800.jpg"
  srcset="
    hero-400.jpg  400w,
    hero-800.jpg  800w,
    hero-1200.jpg 1200w,
    hero-2400.jpg 2400w
  "
  sizes="
    (max-width: 600px) 100vw,
    (max-width: 1200px) 80vw,
    1200px
  "
  alt="A scenic mountain landscape"
>
<!-- The browser picks the most appropriate image automatically
     based on screen size and pixel density -->
""") + """
<h2 class="lesson-section-title" id="picture">picture — Art Direction</h2>
""" + code("""<!-- Show a different image crop depending on screen size -->
<picture>
  <!-- Wide landscape crop for large screens -->
  <source
    media="(min-width: 900px)"
    srcset="hero-wide.jpg"
  >
  <!-- Square crop for medium screens -->
  <source
    media="(min-width: 500px)"
    srcset="hero-square.jpg"
  >
  <!-- Tall portrait crop for phones -->
  <img src="hero-portrait.jpg" alt="Our team at the annual conference">
</picture>
""") + """
<h2 class="lesson-section-title" id="formats">Modern Image Formats</h2>
<ul>
  <li><strong>WebP</strong> — 25-35% smaller than JPEG/PNG with equivalent quality. Excellent browser support.</li>
  <li><strong>AVIF</strong> — Even smaller than WebP. Growing support.</li>
  <li><strong>JPEG</strong> — Photos. Still widely used as a fallback.</li>
  <li><strong>PNG</strong> — Images needing transparency with no quality loss.</li>
  <li><strong>SVG</strong> — Icons, logos, illustrations. Infinitely scalable.</li>
</ul>
""" + code("""<picture>
  <source type="image/avif" srcset="hero.avif">
  <source type="image/webp" srcset="hero.webp">
  <img src="hero.jpg" alt="Description">
</picture>
"""),
    kc=[
        ("What does max-width: 100% do for images?","basic"),
        ("What is the difference between srcset and the picture element?","picture"),
        ("What modern format should you prefer over JPEG for photos?","formats"),
    ],
    assignments=[
        "Convert a JPEG image to WebP using Squoosh (linked below) and implement it with a picture fallback.",
        "Add srcset to the main hero image of your homepage project.",
    ],
    resources=[
        ("MDN — Responsive Images","https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images"),
        ("Squoosh — Image Compression Tool","https://squoosh.app/"),
        ("YouTube — Responsive Images (Kevin Powell)","https://www.youtube.com/watch?v=2QYpkrX2N48"),
    ])

    write("media-queries","Media Queries",
    intro="Media queries let you apply CSS conditionally based on viewport size, device capabilities, or user preferences. They are the final tool for handling what natural responsiveness cannot.",
    overview=[
        "Write min-width and max-width media queries.",
        "Use common breakpoints effectively.",
        "Use media queries for user preferences: prefers-color-scheme, prefers-reduced-motion.",
        "Know when not to use media queries.",
    ],
    body="""
<h2 class="lesson-section-title" id="syntax">Media Query Syntax</h2>
""" + code("""/* Basic syntax */
@media (min-width: 768px) {
  /* styles applied when viewport is 768px or wider */
}

/* Multiple conditions */
@media (min-width: 640px) and (max-width: 1024px) {
  /* tablet range only */
}

/* Target media type */
@media screen and (min-width: 768px) { }
@media print { }
""") + """
<h2 class="lesson-section-title" id="breakpoints">Common Breakpoints</h2>
""" + code("""/* Mobile-first — apply styles progressively */
/* Base: < 640px (mobile) — no media query */

/* Small: 640px — large phones, small tablets */
@media (min-width: 640px)  { }

/* Medium: 768px — tablets */
@media (min-width: 768px)  { }

/* Large: 1024px — laptops */
@media (min-width: 1024px) { }

/* XL: 1280px — desktops */
@media (min-width: 1280px) { }

/* 2XL: 1536px — wide screens */
@media (min-width: 1536px) { }

/* TIP: set breakpoints where your content breaks,
   not at device sizes */
""") + """
<h2 class="lesson-section-title" id="preference-queries">User Preference Queries</h2>
""" + code("""/* Respect the OS dark mode preference */
@media (prefers-color-scheme: dark) {
  :root {
    --bg:   #0f172a;
    --text: #e2e8f0;
  }
}

/* Respect the OS reduced motion preference */
/* Critical for users with vestibular disorders */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* High contrast preference */
@media (prefers-contrast: high) {
  .card {
    border: 2px solid currentColor;
  }
}
""") + """
<h2 class="lesson-section-title" id="when-not-to">When Not to Use Media Queries</h2>
<p>Before adding a breakpoint, ask whether the problem can be solved with:</p>
<ul>
  <li><code>clamp()</code> for fluid typography and spacing</li>
  <li><code>auto-fit</code>/<code>auto-fill</code> for responsive grids</li>
  <li><code>min()</code>/<code>max()</code> for adaptive sizing</li>
  <li>Flexbox wrapping with <code>flex-wrap: wrap</code></li>
</ul>
<p>Media queries are powerful but add complexity. Use them for structural layout changes that cannot be handled intrinsically.</p>
""",
    kc=[
        ("What is the difference between min-width and max-width queries?","syntax"),
        ("Why should breakpoints be set where content breaks rather than at device sizes?","breakpoints"),
        ("What does prefers-reduced-motion do and why is it important?","preference-queries"),
    ],
    assignments=[
        "Add prefers-reduced-motion to your CSS reset and verify it disables animations.",
        "Implement a dark mode using prefers-color-scheme and your existing CSS custom properties.",
        "Read MDN's Using Media Queries guide linked below.",
    ],
    resources=[
        ("MDN — Using Media Queries","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries"),
        ("CSS Tricks — A Complete Guide to CSS Media Queries","https://css-tricks.com/a-complete-guide-to-css-media-queries/"),
        ("YouTube — Media Queries (Kevin Powell)","https://www.youtube.com/watch?v=2KL-z9A56SQ"),
    ])

    write("project-homepage","Project: Homepage",
    intro="The capstone project for this course. Build a fully responsive, accessible personal portfolio homepage that showcases everything you have learned in Intermediate HTML and CSS.",
    overview=[
        "Build a complete responsive homepage from scratch.",
        "Apply Grid and Flexbox appropriately throughout.",
        "Implement accessibility best practices.",
        "Use CSS custom properties for theming.",
        "Publish on GitHub Pages.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>Navigation</strong> — sticky header with logo, nav links, and a theme toggle button</li>
  <li><strong>Hero section</strong> — large heading with clamp() typography, subtext, CTA buttons, and an image</li>
  <li><strong>Skills/Technologies section</strong> — a responsive grid of skill cards using auto-fit</li>
  <li><strong>Projects section</strong> — at least three project cards with image, title, description, and links</li>
  <li><strong>Contact section</strong> — a form with name, email, and message fields</li>
  <li><strong>Footer</strong> — social links and copyright</li>
  <li><strong>Responsive</strong> — works on mobile, tablet, and desktop</li>
  <li><strong>Accessible</strong> — keyboard navigable, skip link, semantic HTML, ARIA where needed</li>
  <li><strong>Dark/light mode</strong> — using CSS custom properties and prefers-color-scheme</li>
</ul>

<h2 class="lesson-section-title" id="setup">Setup</h2>
""" + code("""mkdir ~/devpath-projects/personal-homepage
cd ~/devpath-projects/personal-homepage
git init
touch index.html styles.css script.js
code .
""") + """
<h2 class="lesson-section-title" id="checklist">Accessibility Checklist</h2>
<ul>
  <li>All images have descriptive alt text</li>
  <li>Skip navigation link present</li>
  <li>All interactive elements reachable by keyboard</li>
  <li>Focus styles are visible and attractive</li>
  <li>Colour contrast meets WCAG AA (4.5:1 for text)</li>
  <li>Headings form a logical h1 → h2 → h3 hierarchy</li>
  <li>Form labels are connected to inputs</li>
  <li>prefers-reduced-motion removes animations</li>
  <li>HTML lang attribute is set</li>
  <li>Lighthouse accessibility score is 90+</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>This project goes in your portfolio. Take your time to make it genuinely good — the quality of this page is often the first impression future employers have of your skills.</p>
</div>
""",
    kc=[
        ("What CSS technique creates a responsive skills grid without media queries?","requirements"),
        ("How do you implement a dark/light mode toggle?","requirements"),
    ],
    assignments=[
        "Build the homepage meeting all requirements above.",
        "Run Lighthouse and fix all accessibility issues until you hit 90+ score.",
        "Push to GitHub and publish on GitHub Pages.",
    ],
    resources=[
        ("MDN — Responsive Design","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design"),
        ("CSS Tricks — A Complete Guide to Grid","https://css-tricks.com/snippets/css/complete-guide-grid/"),
        ("WebAIM — Web Accessibility Checklist","https://webaim.org/standards/wcag/checklist"),
        ("YouTube — Build a Responsive Website (Kevin Powell)","https://www.youtube.com/watch?v=p0bGHP-PXD4"),
    ])

    print("\nAll 33 Intermediate HTML & CSS lessons seeded.")
    os.chdir(BASE)
    subprocess.run(["git","add","-A"], check=True)
    subprocess.run(["git","commit","-m","Seed: Intermediate HTML and CSS — all 33 lessons complete"], check=True)
    subprocess.run(["git","push"], check=True)
    print("Pushed to GitHub.")

if __name__ == "__main__":
    seed()
