#!/usr/bin/env python3
"""
Seed: Intermediate HTML and CSS course
Path: Full Stack JavaScript
"""
import os, subprocess

BASE   = os.path.expanduser("~/devpath")
COURSE = os.path.join(BASE, "paths", "full-stack-javascript", "courses", "intermediate-html-css")
LDIR   = os.path.join(COURSE, "lessons")

ALL_LESSONS = [
    ("int-html-css-intro",                "Introduction"),
    ("emmet",                             "Emmet"),
    ("svg",                               "SVG"),
    ("html-tables",                       "Tables"),
    ("default-styles",                    "Default Styles"),
    ("css-units",                         "CSS Units"),
    ("more-text-styles",                  "More Text Styles"),
    ("more-css-properties",               "More CSS Properties"),
    ("advanced-selectors",                "Advanced Selectors"),
    ("positioning",                       "Positioning"),
    ("css-functions",                     "CSS Functions"),
    ("custom-properties",                 "Custom Properties"),
    ("browser-compatibility",             "Browser Compatibility"),
    ("form-basics",                       "Form Basics"),
    ("form-validation",                   "Form Validation"),
    ("project-sign-up-form",              "Project: Sign-Up Form"),
    ("introduction-to-grid",              "Introduction to Grid"),
    ("creating-a-grid",                   "Creating a Grid"),
    ("positioning-grid-elements",         "Positioning Grid Elements"),
    ("advanced-grid-properties",          "Advanced Grid Properties"),
    ("using-flexbox-and-grid",            "Using Flexbox and Grid"),
    ("project-admin-dashboard",           "Project: Admin Dashboard"),
    ("introduction-to-web-accessibility", "Introduction to Web Accessibility"),
    ("wcag",                              "The Web Content Accessibility Guidelines"),
    ("accessible-colors",                 "Accessible Colors"),
    ("keyboard-navigation",               "Keyboard Navigation"),
    ("meaningful-text",                   "Meaningful Text"),
    ("wai-aria",                          "WAI-ARIA"),
    ("introduction-to-responsive-design", "Introduction to Responsive Design"),
    ("natural-responsiveness",            "Natural Responsiveness"),
    ("responsive-images",                 "Responsive Images"),
    ("media-queries",                     "Media Queries"),
    ("project-homepage",                  "Project: Homepage"),
]

LOGO = '<svg viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="13" stroke="currentColor" stroke-width="1.8"/><path d="M8 14 L14 7 L20 14 L14 21 Z" fill="currentColor"/></svg>'
ROOT = "../../../../../"

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

def sidebar(active):
    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "") + (" active" if sl == active else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'
    sections = [
        ("Introduction",    [("int-html-css-intro","Introduction",False)]),
        ("Intermediate HTML",[("emmet","Emmet",False),("svg","SVG",False),("html-tables","Tables",False)]),
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
            ("wcag","The Web Content Accessibility Guidelines",False),
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
    s = '<aside class="sidebar"><div class="sidebar-course-title">Intermediate HTML and CSS</div>'
    for label, items in sections:
        s += f'<div class="sidebar-section"><div class="sidebar-section-label">{label}</div>'
        for sl, ti, proj in items:
            s += lnk(sl, ti, proj)
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
        f'<a href="{ROOT}index.html">Home</a>'
        '<span class="breadcrumb-sep">/</span>'
        f'<a href="{ROOT}paths/full-stack-javascript/index.html">Full Stack JS</a>'
        '<span class="breadcrumb-sep">/</span>'
        '<a href="../index.html">Intermediate HTML and CSS</a>'
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
        f'  <link rel="stylesheet" href="{ROOT}css/styles.css">\n'
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
        + f'<script src="{ROOT}js/main.js"></script>\n</body>\n</html>'
    )
    with open(os.path.join(LDIR, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  {slug}")


# ═══════════════════════════════════════════════════════════
#  LESSONS
# ═══════════════════════════════════════════════════════════
def seed():

    write("int-html-css-intro","Introduction",
    intro="You have completed Foundations. This course takes your HTML and CSS skills to the next level — deeper selectors, real forms, CSS Grid, accessibility, and responsive design. Everything here is used daily in professional front-end work.",
    overview=[
        "Understand what this course covers and why each topic matters.",
        "Know the order of topics and how they build on each other.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-youll-learn">What This Course Covers</h2>
<p>Foundations gave you the core tools. This course sharpens them. You will work through seven major topic areas:</p>
<ul>
  <li><strong>Intermediate HTML</strong> — Emmet productivity shortcuts, SVG graphics, and HTML tables.</li>
  <li><strong>Intermediate CSS</strong> — Units, text styling, advanced selectors, positioning, CSS functions, and custom properties.</li>
  <li><strong>Forms</strong> — Building and validating real HTML forms.</li>
  <li><strong>CSS Grid</strong> — Two-dimensional layout that pairs with Flexbox for complete layout control.</li>
  <li><strong>Accessibility</strong> — Making websites usable for everyone, including people using assistive technology.</li>
  <li><strong>Responsive Design</strong> — Layouts that work on every screen size.</li>
</ul>
<p>Each section ends with a project that applies everything from that section. By the end of this course you will build a full responsive homepage.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Take the lessons in order. Each one builds directly on the previous. Grid makes much more sense after you fully understand Flexbox, and responsive design makes much more sense after Grid.</p>
</div>
""",
    kc=[("What seven topic areas does this course cover?","what-youll-learn")],
    assignments=["Read through the course index page to get familiar with what is coming.","Make sure your Foundations projects are pushed to GitHub — you will continue building on them."],
    resources=[
        ("MDN — Learn Web Development","https://developer.mozilla.org/en-US/docs/Learn"),
        ("CSS Tricks — Almanac","https://css-tricks.com/almanac/"),
    ])

    write("emmet","Emmet",
    intro="Emmet is a plugin built into VS Code that expands short abbreviations into full HTML and CSS. Once you learn it, writing HTML by hand feels painfully slow by comparison.",
    overview=[
        "Use Emmet abbreviations to generate HTML structure instantly.",
        "Chain, nest, and multiply elements with Emmet syntax.",
        "Use Emmet for CSS property shortcuts.",
    ],
    body="""
<h2 class="lesson-section-title" id="html-abbrev">HTML Abbreviations</h2>
<p>Type an abbreviation in a <code>.html</code> file and press <kbd>Tab</kbd>:</p>
""" + code("""! + Tab
→ Full HTML5 boilerplate

div.container + Tab
→ <div class="container"></div>

div#hero + Tab
→ <div id="hero"></div>

div.card.featured + Tab
→ <div class="card featured"></div>
""") + """
<h2 class="lesson-section-title" id="nesting-multiplying">Nesting and Multiplying</h2>
""" + code("""ul>li*5 + Tab
→ <ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
  </ul>

nav>ul>li*3>a + Tab
→ <nav>
    <ul>
      <li><a href=""></a></li>
      <li><a href=""></a></li>
      <li><a href=""></a></li>
    </ul>
  </nav>

div.card*3 + Tab
→ three div.card elements side by side
""") + """
<h2 class="lesson-section-title" id="content-attributes">Content and Attributes</h2>
""" + code("""h1{Hello World} + Tab
→ <h1>Hello World</h1>

a[href=https://example.com]{Visit} + Tab
→ <a href="https://example.com">Visit</a>

input[type=email placeholder="Enter email"] + Tab
→ <input type="email" placeholder="Enter email">

p.item$*3 + Tab
→ <p class="item1"></p>
  <p class="item2"></p>
  <p class="item3"></p>
""") + """
<h2 class="lesson-section-title" id="sibling-climb">Siblings and Climbing</h2>
""" + code("""/* + creates a sibling, ^ climbs up one level */
div>p+span + Tab
→ <div>
    <p></p>
    <span></span>
  </div>

header>nav^main>section + Tab
→ <header><nav></nav></header>
  <main><section></section></main>
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>You do not need to memorise all of this now. Start with the basic element, class, ID, and multiplication syntax. Add more as you naturally want to type faster.</p>
</div>
""",
    kc=[
        ("What does the Emmet abbreviation <code>ul>li*5</code> produce?","nesting-multiplying"),
        ("How do you add content inside an element with Emmet?","content-attributes"),
        ("What does the <code>^</code> operator do?","sibling-climb"),
    ],
    assignments=[
        "Open a blank HTML file and reproduce the following structure using a single Emmet abbreviation: a nav containing an unordered list of five list items each containing an anchor tag.",
        "Build the skeleton of a blog post page (header, nav, main with two article elements each containing h2 and p, sidebar, footer) using Emmet in one line.",
    ],
    resources=[
        ("Emmet Official Documentation","https://docs.emmet.io/"),
        ("Emmet Cheat Sheet","https://docs.emmet.io/cheat-sheet/"),
        ("YouTube — Emmet in VS Code (Traversy Media)","https://www.youtube.com/watch?v=5BIAdWNcr8Y"),
    ])

    write("svg","SVG",
    intro="SVG (Scalable Vector Graphics) lets you display graphics that stay perfectly sharp at any size — from a small icon to a billboard. Unlike images, SVG is written in code and can be styled with CSS.",
    overview=[
        "Understand what SVG is and why it is used for icons and graphics.",
        "Embed SVG inline in HTML and as an img src.",
        "Style SVG elements with CSS.",
        "Understand basic SVG shapes and attributes.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-is-svg">What Is SVG?</h2>
<p>SVG is an XML-based format for describing two-dimensional graphics. Unlike raster images (PNG, JPG) which store pixel data, SVG stores mathematical descriptions of shapes. This means SVG graphics are infinitely scalable with no loss of quality — perfect for logos, icons, and illustrations.</p>

<h2 class="lesson-section-title" id="basic-shapes">Basic SVG Shapes</h2>
""" + code("""<!-- SVG is written directly in HTML -->
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" width="200" height="200">

  <!-- Circle: cx/cy = center, r = radius -->
  <circle cx="50" cy="50" r="40" fill="#2563eb" />

  <!-- Rectangle: x/y = top-left corner -->
  <rect x="10" y="10" width="80" height="40" fill="#1e3a8a" rx="8" />

  <!-- Line -->
  <line x1="0" y1="0" x2="100" y2="100" stroke="#93c5fd" stroke-width="2" />

  <!-- Polygon -->
  <polygon points="50,10 90,90 10,90" fill="#60a5fa" />

  <!-- Path — the most powerful, draws anything -->
  <path d="M 10 80 Q 50 10 90 80" stroke="#2563eb" fill="none" stroke-width="3" />

</svg>
""") + """
<h2 class="lesson-section-title" id="embedding">Ways to Embed SVG</h2>
""" + code("""<!-- 1. Inline SVG — full CSS/JS access, no extra HTTP request -->
<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2L2 7l10 5 10-5-10-5z" stroke="currentColor" stroke-width="2"/>
</svg>

<!-- 2. As an img tag — simple but no CSS access to internals -->
<img src="logo.svg" alt="Company logo" width="120" height="40">

<!-- 3. As CSS background — decorative only, no accessibility -->
.hero {
  background-image: url('pattern.svg');
}
""") + """
<h2 class="lesson-section-title" id="styling">Styling SVG with CSS</h2>
""" + code("""/* SVG-specific CSS properties */
svg {
  fill: #2563eb;       /* fill colour of shapes */
  stroke: #1e3a8a;     /* border/outline colour */
  stroke-width: 2;     /* border thickness */
}

/* Style specific SVG elements */
svg circle { fill: #60a5fa; }
svg rect   { fill: #1d4ed8; }

/* currentColor inherits the CSS color property — very useful for icons */
.icon { color: #2563eb; }
.icon svg { fill: currentColor; }
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Use <code>fill="currentColor"</code> on inline SVG icons. Then you can change the icon colour just by setting <code>color</code> on the parent element — no need to touch the SVG itself.</p>
</div>
""",
    kc=[
        ("What is the main advantage of SVG over PNG for icons?","what-is-svg"),
        ("What are the three ways to embed SVG in HTML?","embedding"),
        ("What does <code>fill: currentColor</code> do?","styling"),
    ],
    assignments=[
        "Create an SVG file containing at least four different shapes. Embed it inline in HTML and style the shapes with CSS.",
        "Find a free SVG icon from a resource like Heroicons or Feather Icons. Embed it inline and change its colour using CSS.",
    ],
    resources=[
        ("MDN — SVG Tutorial","https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial"),
        ("Heroicons — Free SVG Icons","https://heroicons.com/"),
        ("YouTube — SVG Tutorial for Beginners (Web Dev Simplified)","https://www.youtube.com/watch?v=ZJSCl6XEdP8"),
    ])

    write("html-tables","Tables",
    intro="HTML tables exist for one purpose: displaying tabular data — information that has a natural row-and-column structure. This lesson covers how to build accessible, well-structured tables.",
    overview=[
        "Build a complete HTML table with thead, tbody, and tfoot.",
        "Use th, td, colspan, and rowspan correctly.",
        "Make tables accessible with scope and caption.",
    ],
    body="""
<h2 class="lesson-section-title" id="basic-table">Basic Table Structure</h2>
""" + code("""<table>
  <caption>Monthly Sales Figures</caption>

  <thead>
    <tr>
      <th scope="col">Month</th>
      <th scope="col">Revenue</th>
      <th scope="col">Orders</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>January</td>
      <td>$12,400</td>
      <td>248</td>
    </tr>
    <tr>
      <td>February</td>
      <td>$10,200</td>
      <td>204</td>
    </tr>
  </tbody>

  <tfoot>
    <tr>
      <th scope="row">Total</th>
      <td>$22,600</td>
      <td>452</td>
    </tr>
  </tfoot>
</table>
""") + """
<h2 class="lesson-section-title" id="spanning">Spanning Columns and Rows</h2>
""" + code("""<!-- colspan — cell spans multiple columns -->
<tr>
  <td colspan="2">This cell spans two columns</td>
  <td>Normal cell</td>
</tr>

<!-- rowspan — cell spans multiple rows -->
<tr>
  <td rowspan="3">This spans three rows</td>
  <td>Row 1 data</td>
</tr>
<tr>
  <td>Row 2 data</td>
</tr>
<tr>
  <td>Row 3 data</td>
</tr>
""") + """
<h2 class="lesson-section-title" id="accessibility">Accessible Tables</h2>
""" + code("""<!-- scope tells screen readers if a th applies to a column or row -->
<th scope="col">Name</th>    <!-- column header -->
<th scope="row">Total</th>   <!-- row header -->

<!-- caption provides a visible title and helps screen readers -->
<table>
  <caption>Q1 2024 Product Performance</caption>
  ...
</table>
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Never use tables for page layout. Tables are only for tabular data. Use CSS Grid or Flexbox for layout purposes.</p>
</div>
""",
    kc=[
        ("What are the three structural sections of an HTML table?","basic-table"),
        ("What does colspan do?","spanning"),
        ("What does the scope attribute on a th element do for accessibility?","accessibility"),
    ],
    assignments=[
        "Build a weekly schedule table with colspan and rowspan to represent classes that span multiple periods.",
        "Read MDN's HTML Table tutorial — linked below.",
    ],
    resources=[
        ("MDN — HTML Table Basics","https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics"),
        ("MDN — HTML Table Advanced Features","https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Advanced"),
        ("YouTube — HTML Tables (Web Dev Simplified)","https://www.youtube.com/watch?v=dFEqTyMJ2B8"),
    ])

    write("default-styles","Default Styles",
    intro="Every browser applies its own default styles to HTML elements before you write a single line of CSS. Understanding these defaults — and how to reset or normalise them — is essential for consistent cross-browser layouts.",
    overview=[
        "Understand what browser default styles are.",
        "Know the difference between a CSS reset and a normalise stylesheet.",
        "Apply a modern CSS reset to your projects.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-are-defaults">What Are Default Styles?</h2>
<p>Every browser ships with a built-in stylesheet called the <strong>user agent stylesheet</strong>. This is what gives headings their size hierarchy, links their blue colour, lists their bullet points, and blockquotes their indentation — before you write any CSS.</p>
<p>The problem is these defaults differ between browsers. Chrome, Firefox, and Safari all have slightly different default margins, paddings, and font sizes. This leads to your site looking different across browsers unless you address the defaults explicitly.</p>

<h2 class="lesson-section-title" id="reset-vs-normalize">Reset vs. Normalise</h2>
<p>Two approaches exist for handling default styles:</p>
<ul>
  <li><strong>CSS Reset</strong> — Removes all browser defaults, giving you a blank slate. Everything must be styled from scratch.</li>
  <li><strong>Normalise.css</strong> — Preserves useful defaults while correcting inconsistencies between browsers. More conservative approach.</li>
</ul>

<h2 class="lesson-section-title" id="modern-reset">A Modern CSS Reset</h2>
<p>Most modern projects use a lightweight targeted reset rather than a full nuclear one:</p>
""" + code("""/* Box sizing — border-box for everything */
*, *::before, *::after {
  box-sizing: border-box;
}

/* Remove default margins */
* {
  margin: 0;
}

/* Improve text rendering */
body {
  -webkit-font-smoothing: antialiased;
  line-height: 1.5;
}

/* Sensible media defaults */
img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}

/* Inherit fonts for form elements */
input, button, textarea, select {
  font: inherit;
}

/* Avoid text overflow */
p, h1, h2, h3, h4, h5, h6 {
  overflow-wrap: break-word;
}

/* Remove list styles when a list has a role attribute */
ul[role="list"], ol[role="list"] {
  list-style: none;
}
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Add this reset to the very top of every project stylesheet. It takes about two minutes and prevents hours of cross-browser debugging.</p>
</div>
""",
    kc=[
        ("What is the user agent stylesheet?","what-are-defaults"),
        ("What is the difference between a CSS reset and Normalise.css?","reset-vs-normalize"),
        ("Why should box-sizing: border-box be in every reset?","modern-reset"),
    ],
    assignments=[
        "Add the modern reset above to your projects and observe what changes in the browser.",
        "Read Josh Comeau's CSS Reset article — linked below.",
    ],
    resources=[
        ("Josh Comeau — A Modern CSS Reset","https://www.joshwcomeau.com/css/custom-css-reset/"),
        ("Normalise.css","https://necolas.github.io/normalize.css/"),
        ("YouTube — CSS Resets Explained (Kevin Powell)","https://www.youtube.com/watch?v=eWmDW4zEXt4"),
    ])

    write("css-units","CSS Units",
    intro="CSS has many different units for expressing sizes. Using the right unit for each situation — absolute vs relative, viewport vs font-relative — has a significant impact on how your layouts respond to different screens and user preferences.",
    overview=[
        "Distinguish between absolute units (px) and relative units (em, rem, %, vw, vh).",
        "Know when to use each unit type.",
        "Understand why rem is preferred for font sizes and spacing.",
    ],
    body="""
<h2 class="lesson-section-title" id="absolute">Absolute Units</h2>
<p><code>px</code> (pixels) is the only absolute unit you will regularly use in web development. One CSS pixel corresponds to one device pixel on standard displays (though high-DPI displays handle this automatically). Pixels are useful for borders, shadows, and small precise measurements.</p>

<h2 class="lesson-section-title" id="relative">Relative Units</h2>
""" + code("""/* em — relative to the element's own font-size */
.parent { font-size: 20px; }
.child  { font-size: 0.8em; }  /* 0.8 × 20 = 16px */
.child  { padding: 1em; }       /* 1 × 16 = 16px padding */

/* rem — relative to the ROOT element's font-size (usually 16px) */
/* Predictable — not affected by nested font sizes */
h1 { font-size: 2.5rem; }    /* 2.5 × 16 = 40px */
p  { font-size: 1rem; }      /* 1 × 16 = 16px */
.container { max-width: 75rem; }  /* 75 × 16 = 1200px */

/* % — percentage of the parent element's corresponding property */
.sidebar { width: 25%; }     /* 25% of parent width */

/* vw / vh — percentage of the viewport width/height */
.hero   { height: 100vh; }   /* full viewport height */
.banner { width: 100vw; }    /* full viewport width */

/* ch — width of the '0' character. Great for text containers */
p { max-width: 65ch; }       /* readable line length */
""") + """
<h2 class="lesson-section-title" id="when-to-use">When to Use Each Unit</h2>
<ul>
  <li><code>rem</code> — font sizes, spacing (padding/margin), container widths</li>
  <li><code>em</code> — spacing that should scale relative to the element's own font size (button padding, icon sizes)</li>
  <li><code>px</code> — borders, box shadows, very small precise values</li>
  <li><code>%</code> — widths inside a flex or grid container</li>
  <li><code>vw</code> / <code>vh</code> — full-screen sections, viewport-relative font sizes</li>
  <li><code>ch</code> — controlling text line length for readability</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Use <code>rem</code> for font sizes and spacing by default. It respects users' browser font size settings (an important accessibility consideration) and is far more predictable than <code>em</code>.</p>
</div>
""",
    kc=[
        ("What is the difference between em and rem?","relative"),
        ("What does 100vh mean?","relative"),
        ("Why is rem preferred over px for font sizes?","when-to-use"),
    ],
    assignments=[
        "Take a previous project and convert all px font-size and spacing values to rem.",
        "Create a hero section using vh for height and vw for font size. Observe how it responds to browser resizing.",
    ],
    resources=[
        ("MDN — CSS Values and Units","https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units"),
        ("YouTube — CSS Units Explained (Kevin Powell)","https://www.youtube.com/watch?v=N5wpD9Ov_To"),
        ("CSS Tricks — The Lengths of CSS","https://css-tricks.com/the-lengths-of-css/"),
    ])

    write("more-text-styles","More Text Styles",
    intro="Typography is one of the most powerful tools in web design. This lesson covers the CSS properties that control how text looks — beyond just font-size and color.",
    overview=[
        "Control font families, weights, and styles.",
        "Use letter-spacing, line-height, and text-transform.",
        "Load and apply custom web fonts.",
        "Use text-shadow and other decorative text properties.",
    ],
    body="""
<h2 class="lesson-section-title" id="font-properties">Font Properties</h2>
""" + code("""/* font-family — always provide fallbacks */
body {
  font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif;
}

/* font-weight — numeric values are more precise than keywords */
.light    { font-weight: 300; }
.regular  { font-weight: 400; }
.medium   { font-weight: 500; }
.semibold { font-weight: 600; }
.bold     { font-weight: 700; }
.extrabold{ font-weight: 800; }

/* font-style */
em, .italic { font-style: italic; }

/* font-size */
h1 { font-size: 2.5rem; }
p  { font-size: 1rem; }
""") + """
<h2 class="lesson-section-title" id="text-properties">Text Spacing and Transform</h2>
""" + code("""/* line-height — unitless values are recommended */
p { line-height: 1.7; }           /* 1.7x the font-size */
h1 { line-height: 1.15; }         /* tighter for headings */

/* letter-spacing */
.eyebrow { letter-spacing: 0.12em; text-transform: uppercase; }
p        { letter-spacing: -0.01em; }  /* slight tightening for body text */

/* text-transform */
.caps    { text-transform: uppercase; }
.title   { text-transform: capitalize; }

/* text-decoration */
a        { text-decoration: none; }
.strikethrough { text-decoration: line-through; }
.underline { text-decoration: underline #2563eb 2px; }
""") + """
<h2 class="lesson-section-title" id="web-fonts">Loading Custom Web Fonts</h2>
""" + code("""/* Method 1: Google Fonts (easiest) */
/* Add this in the <head> of your HTML */
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

/* Then use in CSS */
body { font-family: 'Inter', sans-serif; }

/* Method 2: @font-face (self-hosted fonts) */
@font-face {
  font-family: 'MyFont';
  src: url('/fonts/myfont.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;  /* prevents invisible text during font load */
}
""") + """
<h2 class="lesson-section-title" id="text-effects">Text Shadow and Effects</h2>
""" + code("""/* text-shadow: x-offset y-offset blur-radius color */
h1 { text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }

/* Multiple shadows */
.glow { text-shadow: 0 0 10px #2563eb, 0 0 20px #2563eb; }

/* white-space controls how whitespace is handled */
.nowrap { white-space: nowrap; }   /* prevent line breaks */
.pre    { white-space: pre; }      /* preserve whitespace exactly */
"""),
    kc=[
        ("Why should you always provide fallback fonts in font-family?","font-properties"),
        ("Why are unitless values recommended for line-height?","text-properties"),
        ("What does font-display: swap do?","web-fonts"),
    ],
    assignments=[
        "Apply a Google Font to one of your projects. Set appropriate line-height, letter-spacing, and font-weight for headings and body text.",
        "Create a typographic scale with at least six size steps using rem units.",
    ],
    resources=[
        ("MDN — Fundamental Text and Font Styling","https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals"),
        ("Google Fonts","https://fonts.google.com/"),
        ("YouTube — Typography in CSS (Kevin Powell)","https://www.youtube.com/watch?v=6x7AjMJNLmo"),
    ])

    write("more-css-properties","More CSS Properties",
    intro="This lesson covers a set of highly useful CSS properties that did not fit neatly into earlier lessons but appear constantly in real projects: overflow, opacity, filter, transitions, and more.",
    overview=[
        "Control overflow behaviour with the overflow property.",
        "Use opacity and visibility.",
        "Apply CSS filter effects.",
        "Use the cursor property.",
        "Control element stacking with z-index.",
    ],
    body="""
<h2 class="lesson-section-title" id="overflow">Overflow</h2>
""" + code("""/* What happens when content is larger than its container */
.container {
  overflow: visible;  /* default — content spills outside */
  overflow: hidden;   /* content is clipped at the border */
  overflow: scroll;   /* always show scrollbars */
  overflow: auto;     /* show scrollbars only when needed */
}

/* Control horizontal and vertical separately */
.code-block { overflow-x: auto; }    /* horizontal scroll only */
.sidebar    { overflow-y: auto; }    /* vertical scroll only */

/* text-overflow — what to show when text is clipped */
.truncate {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;   /* shows "..." when text is too long */
}
""") + """
<h2 class="lesson-section-title" id="opacity-visibility">Opacity and Visibility</h2>
""" + code("""/* opacity — 0 (invisible) to 1 (fully visible) */
/* Element still takes up space, can receive click events */
.faded { opacity: 0.5; }
.invisible-but-there { opacity: 0; }

/* visibility — hidden removes from visual display */
/* Element STILL takes up space, cannot receive events */
.hidden { visibility: hidden; }

/* display:none — removes from layout entirely */
.gone { display: none; }
""") + """
<h2 class="lesson-section-title" id="filters">CSS Filters</h2>
""" + code("""/* Apply visual effects to any element */
img { filter: grayscale(100%); }           /* black and white */
img { filter: blur(4px); }                 /* blur */
img { filter: brightness(1.2); }           /* brighter */
img { filter: contrast(1.5); }             /* more contrast */
img { filter: sepia(80%); }                /* sepia tone */
img { filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.3)); }

/* Chain multiple filters */
.hero-bg {
  filter: brightness(0.7) contrast(1.2) blur(1px);
}
""") + """
<h2 class="lesson-section-title" id="other">Other Useful Properties</h2>
""" + code("""/* cursor — change the mouse cursor */
button { cursor: pointer; }     /* hand cursor */
.grab  { cursor: grab; }
.loading { cursor: wait; }
.no-select { cursor: not-allowed; }

/* z-index — stacking order (only works on positioned elements) */
.modal-backdrop { position: fixed; z-index: 100; }
.modal          { position: fixed; z-index: 101; }
.tooltip        { position: absolute; z-index: 50; }

/* pointer-events — disable click interactions */
.overlay { pointer-events: none; }
"""),
    kc=[
        ("What is the difference between overflow: hidden and overflow: auto?","overflow"),
        ("What is the difference between opacity: 0 and display: none?","opacity-visibility"),
        ("How do you chain multiple CSS filters?","filters"),
    ],
    assignments=[
        "Build a card component with a hover effect that uses filter: brightness() and a smooth transition.",
        "Create a text truncation component that shows ellipsis when text overflows a single line.",
    ],
    resources=[
        ("MDN — overflow","https://developer.mozilla.org/en-US/docs/Web/CSS/overflow"),
        ("MDN — CSS filter","https://developer.mozilla.org/en-US/docs/Web/CSS/filter"),
        ("YouTube — CSS Properties You Should Know (Kevin Powell)","https://www.youtube.com/watch?v=N5wpD9Ov_To"),
    ])

    write("advanced-selectors","Advanced Selectors",
    intro="CSS selectors go far beyond element, class, and ID. Advanced selectors let you target elements based on their position, state, attributes, and relationship to other elements — often without adding any extra classes to your HTML.",
    overview=[
        "Use combinators: descendant, child, adjacent sibling, general sibling.",
        "Use pseudo-classes: :hover, :focus, :nth-child, :not, :is, :where.",
        "Use pseudo-elements: ::before, ::after, ::first-line, ::placeholder.",
        "Use attribute selectors.",
    ],
    body="""
<h2 class="lesson-section-title" id="combinators">Combinators</h2>
""" + code("""/* Descendant — any p inside .article, no matter how deep */
.article p { color: #334155; }

/* Child — only DIRECT children */
.nav > li { display: inline-block; }

/* Adjacent sibling — h2 immediately followed by p */
h2 + p { font-size: 1.15rem; font-weight: 500; }

/* General sibling — all p after h2 in the same parent */
h2 ~ p { margin-top: 0.5rem; }
""") + """
<h2 class="lesson-section-title" id="pseudo-classes">Pseudo-Classes</h2>
""" + code("""/* State pseudo-classes */
a:hover       { color: #1d4ed8; }
button:focus  { outline: 2px solid #2563eb; outline-offset: 2px; }
input:disabled{ opacity: 0.5; }
input:checked { accent-color: #2563eb; }

/* Structural pseudo-classes */
li:first-child  { font-weight: 700; }
li:last-child   { border-bottom: none; }
li:nth-child(2) { background: #f0f9ff; }
li:nth-child(odd)  { background: #f8fafc; }
li:nth-child(even) { background: #ffffff; }

/* Negation */
p:not(.intro) { color: #64748b; }

/* :is() — matches any selector in the list */
:is(h1, h2, h3) { line-height: 1.2; }

/* :where() — same as :is() but zero specificity */
:where(h1, h2, h3) { margin-bottom: 0.75em; }
""") + """
<h2 class="lesson-section-title" id="pseudo-elements">Pseudo-Elements</h2>
""" + code("""/* ::before and ::after — inject content before/after element */
.card::before {
  content: '';
  display: block;
  width: 100%;
  height: 4px;
  background: #2563eb;
  border-radius: 4px 4px 0 0;
}

/* ::first-line — style just the first line of text */
p::first-line { font-weight: 600; }

/* ::placeholder — style input placeholder text */
input::placeholder { color: #94a3b8; font-style: italic; }

/* ::selection — style highlighted/selected text */
::selection { background: #2563eb; color: white; }
""") + """
<h2 class="lesson-section-title" id="attribute-selectors">Attribute Selectors</h2>
""" + code("""/* Has the attribute */
[disabled] { opacity: 0.5; }

/* Exact attribute value */
[type="submit"] { background: #2563eb; }

/* Attribute contains word */
[class~="card"] { border-radius: 8px; }

/* Attribute starts with */
a[href^="https"] { /* external links */ }

/* Attribute ends with */
a[href$=".pdf"]::after { content: " (PDF)"; }

/* Attribute contains substring */
a[href*="github"] { color: #6e40c9; }
"""),
    kc=[
        ("What is the difference between the descendant combinator and the child combinator?","combinators"),
        ("What does li:nth-child(odd) select?","pseudo-classes"),
        ("What is the difference between :is() and :where()?","pseudo-classes"),
        ("How do ::before and ::after work?","pseudo-elements"),
    ],
    assignments=[
        "Rebuild a navigation menu using only combinators and pseudo-classes — no extra classes on the HTML.",
        "Style a form entirely using attribute selectors and pseudo-classes like :focus, :valid, :invalid.",
    ],
    resources=[
        ("MDN — CSS Selectors","https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors"),
        ("CSS Tricks — The CSS :is() Pseudo-Class","https://css-tricks.com/the-css-is-pseudo-class/"),
        ("YouTube — Advanced CSS Selectors (Kevin Powell)","https://www.youtube.com/watch?v=Bcr70LIJcOk"),
    ])

    write("positioning","Positioning",
    intro="CSS positioning lets you break elements out of the normal document flow and place them exactly where you want. Understanding the five position values and how they interact is essential for building tooltips, modals, sticky headers, and complex layouts.",
    overview=[
        "Understand the five position values: static, relative, absolute, fixed, sticky.",
        "Know how top, right, bottom, left work with each position type.",
        "Use z-index to control stacking order.",
        "Know common use cases for each position value.",
    ],
    body="""
<h2 class="lesson-section-title" id="position-values">The Five Position Values</h2>
""" + code("""/* STATIC — default. Element is in normal flow. */
/* top/right/bottom/left have NO effect */
.normal { position: static; }

/* RELATIVE — stays in normal flow, but can be nudged */
/* top/right/bottom/left offset from its own normal position */
.nudged {
  position: relative;
  top: 10px;    /* move 10px DOWN from normal position */
  left: 20px;   /* move 20px RIGHT from normal position */
}

/* ABSOLUTE — removed from normal flow */
/* Positioned relative to nearest NON-STATIC ancestor */
.parent  { position: relative; }   /* establishes a containing block */
.tooltip {
  position: absolute;
  top: 100%;    /* just below the parent */
  left: 0;
  z-index: 10;
}

/* FIXED — removed from flow, positioned relative to VIEWPORT */
/* Stays on screen even when scrolling */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
}

/* STICKY — hybrid of relative and fixed */
/* Behaves relative until it reaches a scroll threshold, then fixed */
.section-header {
  position: sticky;
  top: 64px;   /* sticks when 64px from top of viewport */
}
""") + """
<h2 class="lesson-section-title" id="containing-block">The Containing Block</h2>
<p>When you use <code>position: absolute</code>, the element positions itself relative to its nearest ancestor that has a position other than <code>static</code>. This ancestor is called the <strong>containing block</strong>.</p>
""" + code("""/* The badge is absolutely positioned INSIDE the card */
.card {
  position: relative;  /* makes this the containing block */
  width: 300px;
}

.badge {
  position: absolute;
  top: 12px;
  right: 12px;
  background: #2563eb;
  color: white;
  padding: 4px 8px;
  border-radius: 20px;
}
""") + """
<h2 class="lesson-section-title" id="z-index">Z-Index</h2>
""" + code("""/* z-index controls which element appears on top */
/* Higher value = appears in front */
/* Only works on positioned elements (anything except static) */

.dropdown { position: absolute; z-index: 20; }
.modal    { position: fixed;    z-index: 200; }
.tooltip  { position: absolute; z-index: 50; }

/* Stacking context — a z-index creates a new stacking context */
/* Children cannot escape their parent's stacking context */
"""),
    kc=[
        ("What is the difference between relative and absolute positioning?","position-values"),
        ("What is the containing block for a position: absolute element?","containing-block"),
        ("Why does z-index not work on position: static elements?","z-index"),
        ("When would you use position: sticky?","position-values"),
    ],
    assignments=[
        "Build a card with an absolutely positioned badge in the top-right corner.",
        "Build a sticky navigation bar that stays at the top of the viewport while scrolling.",
        "Build a tooltip that appears on hover using position: absolute.",
    ],
    resources=[
        ("MDN — CSS Positioning","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning"),
        ("CSS Tricks — position","https://css-tricks.com/almanac/properties/p/position/"),
        ("YouTube — CSS Position Explained (Kevin Powell)","https://www.youtube.com/watch?v=jx5jmI0UlXU"),
    ])

    write("css-functions","CSS Functions",
    intro="CSS functions are a powerful feature that allow dynamic values, calculations, and responsive behaviour — all without JavaScript. This lesson covers the most useful ones.",
    overview=[
        "Use calc() for dynamic size calculations.",
        "Use min(), max(), and clamp() for responsive values.",
        "Use var() with CSS custom properties.",
        "Use color functions like rgb(), hsl(), and oklch().",
    ],
    body="""
<h2 class="lesson-section-title" id="calc">calc()</h2>
<p><code>calc()</code> lets you perform mathematical operations with mixed units — something you cannot do with regular CSS values.</p>
""" + code("""/* Mix units freely */
.sidebar {
  width: calc(100% - 280px);   /* full width minus sidebar */
}

.container {
  padding: calc(1rem + 2vw);   /* base padding that grows with viewport */
}

.column {
  width: calc(33.333% - 1rem); /* three columns with gap */
}
""") + """
<h2 class="lesson-section-title" id="min-max-clamp">min(), max(), and clamp()</h2>
""" + code("""/* min() — use the SMALLEST value */
.container {
  width: min(90%, 1200px);
  /* → on large screens: 1200px  */
  /* → on small screens: 90%     */
}

/* max() — use the LARGEST value */
.text {
  font-size: max(1rem, 2vw);
  /* → at least 1rem, but grows with viewport */
}

/* clamp(minimum, preferred, maximum) */
/* The most powerful responsive tool in CSS */
h1 {
  font-size: clamp(1.75rem, 4vw, 3rem);
  /* → never smaller than 1.75rem           */
  /* → ideally 4% of viewport width          */
  /* → never larger than 3rem               */
}

.container {
  padding: clamp(1rem, 5vw, 3rem);
  /* padding that scales smoothly with screen width */
}
""") + """
<h2 class="lesson-section-title" id="color-functions">Color Functions</h2>
""" + code("""/* rgb() and rgba() */
.box { background: rgb(37, 99, 235); }
.box { background: rgba(37, 99, 235, 0.5); }  /* 50% transparent */

/* hsl() — hue, saturation, lightness */
/* More intuitive for creating colour palettes */
.primary  { background: hsl(217, 91%, 60%); }
.lighter  { background: hsl(217, 91%, 75%); }  /* same hue, lighter */
.darker   { background: hsl(217, 91%, 45%); }  /* same hue, darker */

/* Modern: oklch() — perceptually uniform colour space */
.brand { color: oklch(60% 0.2 240); }
"""),
    kc=[
        ("What problem does calc() solve that regular CSS values cannot?","calc"),
        ("What does clamp() do and what are its three arguments?","min-max-clamp"),
        ("Why is hsl() more intuitive than rgb() for building colour palettes?","color-functions"),
    ],
    assignments=[
        "Create a fluid typography system using clamp() for all headings and body text.",
        "Build a full-width layout with a constrained container using min() or calc().",
    ],
    resources=[
        ("MDN — CSS Functions","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Functions"),
        ("MDN — clamp()","https://developer.mozilla.org/en-US/docs/Web/CSS/clamp"),
        ("YouTube — CSS clamp() is Amazing (Kevin Powell)","https://www.youtube.com/watch?v=U9VF-4euyRo"),
    ])

    write("custom-properties","Custom Properties",
    intro="CSS custom properties (also called CSS variables) let you store values in one place and reuse them throughout your stylesheet. They are the foundation of every modern design system and theme.",
    overview=[
        "Declare and use CSS custom properties with var().",
        "Understand scope and inheritance of custom properties.",
        "Use custom properties to build a design token system.",
        "Update custom properties dynamically with JavaScript.",
    ],
    body="""
<h2 class="lesson-section-title" id="declaring">Declaring and Using Custom Properties</h2>
""" + code("""/* Declare on :root to make available everywhere */
:root {
  --color-primary:    #2563eb;
  --color-secondary:  #60a5fa;
  --color-text:       #1e293b;
  --color-bg:         #ffffff;
  --font-size-base:   1rem;
  --spacing-sm:       0.5rem;
  --spacing-md:       1rem;
  --spacing-lg:       2rem;
  --radius:           8px;
  --shadow:           0 4px 6px -1px rgba(0,0,0,0.1);
}

/* Use with var() — always provide a fallback */
.button {
  background: var(--color-primary);
  color: white;
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

h1 { color: var(--color-text, #000); }  /* fallback = #000 */
""") + """
<h2 class="lesson-section-title" id="scope">Scope and Inheritance</h2>
""" + code("""/* Custom properties are inherited — children get parent's values */
:root {
  --color-primary: #2563eb;
}

.dark-theme {
  --color-primary: #93c5fd;  /* override in this scope only */
  --color-bg: #0f172a;
  --color-text: #f1f5f9;
}

/* Elements inside .dark-theme automatically use the overridden values */
.dark-theme .button { background: var(--color-primary); }
""") + """
<h2 class="lesson-section-title" id="dark-mode">Dark Mode with Custom Properties</h2>
""" + code(""":root {
  --bg:      #ffffff;
  --text:    #1e293b;
  --surface: #f8fafc;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg:      #0f172a;
    --text:    #f1f5f9;
    --surface: #1e293b;
  }
}

/* All components automatically update — no duplication */
body       { background: var(--bg); color: var(--text); }
.card      { background: var(--surface); }
""") + """
<h2 class="lesson-section-title" id="js-update">Updating with JavaScript</h2>
""" + code("""// Read a custom property
const root = document.documentElement;
const primary = getComputedStyle(root).getPropertyValue('--color-primary');

// Set a custom property dynamically
root.style.setProperty('--color-primary', '#10b981');

// Theme switcher example
document.querySelector('#theme-toggle').addEventListener('click', () => {
  document.documentElement.classList.toggle('dark-theme');
});
"""),
    kc=[
        ("What is the syntax for declaring a CSS custom property?","declaring"),
        ("On which selector should you declare global custom properties?","declaring"),
        ("How does scope work for custom properties?","scope"),
        ("How do you update a custom property with JavaScript?","js-update"),
    ],
    assignments=[
        "Refactor one of your projects to use custom properties for all colours, font sizes, spacing, and border radii.",
        "Implement a dark mode toggle using custom properties and a class switch on the root element.",
    ],
    resources=[
        ("MDN — Using CSS Custom Properties","https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties"),
        ("CSS Tricks — A Complete Guide to Custom Properties","https://css-tricks.com/a-complete-guide-to-custom-properties/"),
        ("YouTube — CSS Custom Properties (Kevin Powell)","https://www.youtube.com/watch?v=GF8aoDqebsQ"),
    ])

    write("browser-compatibility","Browser Compatibility",
    intro="Modern CSS has excellent browser support, but new features roll out at different times across Chrome, Firefox, Safari, and Edge. This lesson covers how to check compatibility, handle differences, and use progressive enhancement.",
    overview=[
        "Use Can I Use to check feature support.",
        "Understand vendor prefixes and when they are needed.",
        "Write progressive enhancement using @supports.",
        "Know which browsers require special attention today.",
    ],
    body="""
<h2 class="lesson-section-title" id="checking">Checking Compatibility</h2>
<p><a href="https://caniuse.com" target="_blank" rel="noopener">caniuse.com</a> is the definitive resource for checking which browsers support a given CSS or JavaScript feature. Before using any new CSS property in production, search it on Can I Use to understand the support landscape.</p>

<h2 class="lesson-section-title" id="vendor-prefixes">Vendor Prefixes</h2>
<p>Historically, browsers added vendor prefixes to experimental features before standardising them. You still occasionally see these in older codebases:</p>
""" + code("""-webkit- /* Chrome, Safari, newer Opera, Edge */
-moz-    /* Firefox */
-ms-     /* Internet Explorer, old Edge */
-o-      /* Old Opera */

/* Example */
.box {
  -webkit-transform: rotate(45deg);  /* old Safari */
  transform: rotate(45deg);          /* standard */
}
""") + """
<p>Modern properties like Grid, Flexbox, and custom properties no longer need prefixes. Autoprefixer (a PostCSS plugin) can automatically add any needed prefixes during your build process.</p>

<h2 class="lesson-section-title" id="supports">@supports — Feature Detection</h2>
""" + code("""/* Apply styles only if the browser supports a property */
@supports (display: grid) {
  .container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }
}

/* Fallback for browsers without grid support */
.container {
  display: flex;
  flex-wrap: wrap;
}

/* Negative query */
@supports not (container-type: inline-size) {
  /* Fallback when container queries are not supported */
}
""") + """
<h2 class="lesson-section-title" id="today">Browser Support Today</h2>
<p>In 2024, the browser landscape is much simpler than it was five years ago:</p>
<ul>
  <li>IE11 has been officially retired — you no longer need to support it.</li>
  <li>Chrome, Edge, Firefox, and Safari all support Grid, Flexbox, custom properties, and most modern CSS.</li>
  <li>Safari on iOS can lag behind slightly — worth testing on real devices.</li>
  <li>The main strategy now is <strong>progressive enhancement</strong> — build a baseline that works everywhere, then layer on enhancements for modern browsers.</li>
</ul>
""",
    kc=[
        ("What is the best resource for checking CSS browser support?","checking"),
        ("What does @supports do?","supports"),
        ("What is progressive enhancement?","today"),
    ],
    assignments=[
        "Look up three CSS features you have used recently on caniuse.com and check their browser support.",
        "Add an @supports block to a project, providing a flex-based fallback for a grid layout.",
    ],
    resources=[
        ("Can I Use — Browser Compatibility Tables","https://caniuse.com/"),
        ("MDN — @supports","https://developer.mozilla.org/en-US/docs/Web/CSS/@supports"),
        ("YouTube — Browser Compatibility (Kevin Powell)","https://www.youtube.com/watch?v=nFk-sHqDIBs"),
    ])

    write("form-basics","Form Basics",
    intro="Forms are how users interact with your application — logging in, signing up, searching, submitting data. This lesson covers how to build well-structured, accessible HTML forms.",
    overview=[
        "Build a complete HTML form with appropriate input types.",
        "Use label elements correctly for accessibility.",
        "Understand the key form attributes: action, method, name.",
        "Use fieldset and legend to group related inputs.",
    ],
    body="""
<h2 class="lesson-section-title" id="form-structure">Form Structure</h2>
""" + code("""<form action="/submit" method="POST">

  <!-- Text input with associated label -->
  <div class="form-group">
    <label for="email">Email address</label>
    <input
      type="email"
      id="email"
      name="email"
      placeholder="you@example.com"
      autocomplete="email"
      required
    >
  </div>

  <!-- Password input -->
  <div class="form-group">
    <label for="password">Password</label>
    <input
      type="password"
      id="password"
      name="password"
      minlength="8"
      required
    >
  </div>

  <!-- Submit button -->
  <button type="submit">Sign In</button>

</form>
""") + """
<h2 class="lesson-section-title" id="input-types">Input Types</h2>
""" + code("""<input type="text">           <!-- single-line text -->
<input type="email">          <!-- validates email format -->
<input type="password">       <!-- masks characters -->
<input type="number">         <!-- numeric keyboard on mobile -->
<input type="tel">            <!-- phone keyboard on mobile -->
<input type="url">            <!-- validates URL format -->
<input type="date">           <!-- date picker -->
<input type="checkbox">       <!-- boolean option -->
<input type="radio">          <!-- one of many options -->
<input type="range" min="0" max="100"> <!-- slider -->
<input type="file">           <!-- file upload -->
<input type="hidden">         <!-- invisible data field -->
<input type="search">         <!-- search field with clear button -->

<textarea rows="5" cols="40">Multi-line text</textarea>

<select>
  <option value="">-- Select one --</option>
  <option value="js">JavaScript</option>
  <option value="py">Python</option>
</select>
""") + """
<h2 class="lesson-section-title" id="labels-accessibility">Labels and Accessibility</h2>
""" + code("""<!-- Method 1: for/id association (preferred) -->
<label for="username">Username</label>
<input type="text" id="username" name="username">

<!-- Method 2: wrapping label -->
<label>
  Username
  <input type="text" name="username">
</label>

<!-- Never do this — no label association -->
<p>Username</p>
<input type="text" name="username">

<!-- Placeholder is NOT a replacement for a label -->
<!-- It disappears when the user starts typing -->
""") + """
<h2 class="lesson-section-title" id="fieldset">Grouping with Fieldset</h2>
""" + code("""<fieldset>
  <legend>Shipping Address</legend>

  <div class="form-group">
    <label for="street">Street</label>
    <input type="text" id="street" name="street">
  </div>

  <div class="form-group">
    <label for="city">City</label>
    <input type="text" id="city" name="city">
  </div>
</fieldset>

<!-- Radio buttons always belong in a fieldset/legend group -->
<fieldset>
  <legend>Preferred contact method</legend>
  <label><input type="radio" name="contact" value="email"> Email</label>
  <label><input type="radio" name="contact" value="phone"> Phone</label>
</fieldset>
"""),
    kc=[
        ("Why must every input have an associated label?","labels-accessibility"),
        ("What is the difference between the for attribute and wrapping a label?","labels-accessibility"),
        ("When should you use fieldset and legend?","fieldset"),
        ("What input type should you use for email addresses?","input-types"),
    ],
    assignments=[
        "Build a complete registration form with name, email, password, country (select), and terms checkbox — all with proper labels.",
        "Read MDN's 'Your first HTML form' guide — linked below.",
    ],
    resources=[
        ("MDN — Your First HTML Form","https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form"),
        ("MDN — HTML Form Elements","https://developer.mozilla.org/en-US/docs/Learn/Forms/Basic_native_form_controls"),
        ("YouTube — HTML Forms (Web Dev Simplified)","https://www.youtube.com/watch?v=fNcJuPIZ2WE"),
    ])

    write("form-validation","Form Validation",
    intro="Form validation ensures users provide correct, complete data before submission. HTML5 provides powerful built-in validation — no JavaScript required for the basics.",
    overview=[
        "Use HTML5 validation attributes: required, minlength, maxlength, min, max, pattern.",
        "Style valid and invalid states with CSS pseudo-classes.",
        "Understand the constraint validation API.",
        "Know when to use HTML validation versus custom JavaScript validation.",
    ],
    body="""
<h2 class="lesson-section-title" id="html-validation">HTML5 Validation Attributes</h2>
""" + code("""<!-- required — field cannot be empty -->
<input type="text" name="name" required>

<!-- minlength / maxlength — string length constraints -->
<input type="password" name="password" minlength="8" maxlength="64" required>

<!-- min / max — numeric range constraints -->
<input type="number" name="age" min="18" max="120" required>
<input type="date" name="dob" min="1900-01-01" max="2010-12-31">

<!-- pattern — regular expression validation -->
<input
  type="text"
  name="username"
  pattern="[a-zA-Z0-9_]{3,20}"
  title="3-20 characters: letters, numbers, and underscores only"
  required
>

<!-- type validation happens automatically -->
<input type="email" required>  <!-- validates email format -->
<input type="url" required>    <!-- validates URL format -->
""") + """
<h2 class="lesson-section-title" id="css-validation">Styling Validation States</h2>
""" + code("""/* :valid and :invalid pseudo-classes */
input:valid {
  border-color: #10b981;
  outline-color: #10b981;
}

input:invalid {
  border-color: #ef4444;
  outline-color: #ef4444;
}

/* :required and :optional */
input:required { border-left: 3px solid #2563eb; }

/* :user-valid / :user-invalid — only after user has interacted */
/* Prevents showing errors before user has typed anything */
input:user-invalid {
  border-color: #ef4444;
}

/* Focus state should always be visible for accessibility */
input:focus {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}
""") + """
<h2 class="lesson-section-title" id="custom-validation">Custom Validation Messages</h2>
""" + code("""<!-- Custom error message with title attribute -->
<input
  type="email"
  required
  title="Please enter a valid email address like: you@example.com"
>

<!-- Custom JS validation using the Constraint Validation API -->
const emailInput = document.querySelector('#email');

emailInput.addEventListener('input', () => {
  if (emailInput.value.includes('+')) {
    emailInput.setCustomValidity('Plus signs are not allowed in email addresses.');
  } else {
    emailInput.setCustomValidity('');  // empty string = valid
  }
});
"""),
    kc=[
        ("What HTML attribute prevents a form from submitting with an empty field?","html-validation"),
        ("What does the pattern attribute accept?","html-validation"),
        ("What is the difference between :invalid and :user-invalid?","css-validation"),
    ],
    assignments=[
        "Add validation to the registration form from the previous lesson: required fields, password minimum length, and email format.",
        "Style the form validation states using :user-valid and :user-invalid.",
    ],
    resources=[
        ("MDN — Client-Side Form Validation","https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation"),
        ("MDN — Constraint Validation API","https://developer.mozilla.org/en-US/docs/Web/API/Constraint_validation"),
        ("YouTube — Form Validation (Web Dev Simplified)","https://www.youtube.com/watch?v=In0nB0ABaUk"),
    ])

    write("project-sign-up-form","Project: Sign-Up Form",
    intro="Put your form knowledge to work. You will build a complete, styled, and validated sign-up form — the kind found on real applications.",
    overview=[
        "Build a visually polished sign-up form.",
        "Apply custom form styling including focus states.",
        "Implement HTML5 validation with meaningful error indicators.",
        "Ensure the form is accessible and keyboard-navigable.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Fields: full name, username, email, password, confirm password</li>
  <li>All fields validated appropriately (required, minlength, pattern where relevant)</li>
  <li>Custom styling for default, focus, valid, and invalid states</li>
  <li>A show/hide password toggle button</li>
  <li>A terms and conditions checkbox (required before submit)</li>
  <li>Fully keyboard-accessible: every element reachable and operable by Tab</li>
  <li>Responsive: works on mobile and desktop</li>
</ul>

<h2 class="lesson-section-title" id="design-tips">Design Tips</h2>
<ul>
  <li>Use a two-column layout on wide screens, single column on mobile</li>
  <li>Give the form a card-like container with padding and shadow</li>
  <li>Use a brand colour for focus outlines and validation indicators</li>
  <li>Error messages should appear below the relevant field, not as a browser alert</li>
</ul>

<h2 class="lesson-section-title" id="password-toggle">Password Toggle Snippet</h2>
""" + code("""<!-- HTML -->
<div class="input-group">
  <input type="password" id="password" name="password" required>
  <button type="button" id="toggle-password" aria-label="Show password">
    👁
  </button>
</div>

<!-- JavaScript -->
document.querySelector('#toggle-password').addEventListener('click', () => {
  const input = document.querySelector('#password');
  const isPassword = input.type === 'password';
  input.type = isPassword ? 'text' : 'password';
});
""") + """
<h2 class="lesson-section-title" id="workflow">Project Workflow</h2>
""" + code("""mkdir ~/devpath-projects/sign-up-form
cd ~/devpath-projects/sign-up-form
git init
touch index.html styles.css script.js
code .
"""),
    kc=[
        ("What pseudo-classes should you use for form validation states?","requirements"),
        ("What attribute is needed to make a button inside a form NOT submit the form?","password-toggle"),
    ],
    assignments=[
        "Complete the Sign-Up Form meeting all requirements above.",
        "Push to GitHub and publish on GitHub Pages.",
    ],
    resources=[
        ("MDN — Styling Web Forms","https://developer.mozilla.org/en-US/docs/Learn/Forms/Styling_web_forms"),
        ("MDN — Advanced Form Styling","https://developer.mozilla.org/en-US/docs/Learn/Forms/Advanced_form_styling"),
        ("YouTube — Style a Sign Up Form (Traversy Media)","https://www.youtube.com/watch?v=okbByPWS1Xc"),
    ])

    write("introduction-to-grid","Introduction to Grid",
    intro="CSS Grid is a two-dimensional layout system — it handles both rows and columns simultaneously. Where Flexbox excels at one-dimensional layouts, Grid excels at complex two-dimensional ones.",
    overview=[
        "Understand when to use Grid versus Flexbox.",
        "Activate CSS Grid with display: grid.",
        "Define columns and rows with grid-template-columns and grid-template-rows.",
        "Use the fr unit for flexible track sizing.",
    ],
    body="""
<h2 class="lesson-section-title" id="grid-vs-flex">Grid vs. Flexbox</h2>
<p>Flexbox and Grid are complementary tools, not competitors:</p>
<ul>
  <li><strong>Flexbox</strong> — one-dimensional. Items flow in a single row or column. Great for navigation bars, button groups, centering content.</li>
  <li><strong>Grid</strong> — two-dimensional. Items are placed in explicit rows AND columns simultaneously. Great for page layouts, dashboards, card grids, and any layout where you need precise control over both axes.</li>
</ul>

<h2 class="lesson-section-title" id="activating">Activating Grid</h2>
""" + code("""<div class="grid-container">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
  <div class="item">4</div>
  <div class="item">5</div>
  <div class="item">6</div>
</div>
""") + code(""".grid-container {
  display: grid;

  /* Define three equal columns */
  grid-template-columns: 1fr 1fr 1fr;

  /* Shorthand with repeat() */
  grid-template-columns: repeat(3, 1fr);

  /* Mixed sizes */
  grid-template-columns: 250px 1fr 1fr;
  grid-template-columns: 250px 1fr auto;

  /* Gap between cells */
  gap: 1rem;
  column-gap: 1.5rem;  /* separate horizontal and vertical */
  row-gap: 1rem;
}
""") + """
<h2 class="lesson-section-title" id="fr-unit">The fr Unit</h2>
<p>The <code>fr</code> (fraction) unit represents a fraction of the available space in the grid container — similar to flex-grow in Flexbox but applied to grid tracks.</p>
""" + code("""/* Three equal columns sharing all available space */
grid-template-columns: 1fr 1fr 1fr;

/* First column is twice as wide as the others */
grid-template-columns: 2fr 1fr 1fr;

/* Sidebar + main content + another sidebar */
grid-template-columns: 200px 1fr 200px;
/* Fixed sidebar | flexible main | fixed sidebar */

/* Automatic rows */
grid-template-rows: auto;        /* default — sized by content */
grid-auto-rows: minmax(100px, auto); /* each row at least 100px */
"""),
    kc=[
        ("When should you use Grid over Flexbox?","grid-vs-flex"),
        ("What does the fr unit represent?","fr-unit"),
        ("What does repeat(3, 1fr) do?","activating"),
    ],
    assignments=[
        "Build a simple three-column article layout using Grid.",
        "Play CSS Grid Garden until you complete all 28 levels — linked below.",
    ],
    resources=[
        ("CSS Grid Garden — Learn Grid with a game","https://cssgridgarden.com/"),
        ("CSS Tricks — A Complete Guide to Grid","https://css-tricks.com/snippets/css/complete-guide-grid/"),
        ("MDN — CSS Grid Layout","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Grids"),
        ("YouTube — CSS Grid Tutorial (Kevin Powell)","https://www.youtube.com/watch?v=rg7Fvvl3taU"),
    ])

    write("creating-a-grid","Creating a Grid",
    intro="Now that you understand the basics, this lesson goes deeper — implicit vs explicit grids, auto-placement, and controlling row heights.",
    overview=[
        "Understand the difference between explicit and implicit grid tracks.",
        "Use grid-auto-rows and grid-auto-columns.",
        "Use minmax() for flexible minimum and maximum track sizes.",
        "Use auto-fill and auto-fit for responsive grids without media queries.",
    ],
    body="""
<h2 class="lesson-section-title" id="explicit-implicit">Explicit vs. Implicit Grid</h2>
<p>The <strong>explicit grid</strong> is the one you define with <code>grid-template-columns</code> and <code>grid-template-rows</code>. The <strong>implicit grid</strong> is what the browser creates automatically when items overflow your defined tracks.</p>
""" + code(""".grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* explicit: 3 columns */
  /* No rows defined — they are IMPLICIT */

  /* Control implicit row height */
  grid-auto-rows: 200px;              /* fixed height */
  grid-auto-rows: minmax(150px, auto);/* at least 150px, grows with content */
}
""") + """
<h2 class="lesson-section-title" id="minmax">minmax()</h2>
""" + code("""/* minmax(minimum, maximum) — track cannot be smaller than min or larger than max */
.grid {
  grid-template-columns: repeat(3, minmax(200px, 1fr));
  /* each column: at least 200px, expands equally to fill remaining space */

  grid-auto-rows: minmax(120px, auto);
  /* each row: at least 120px tall, grows with content */
}
""") + """
<h2 class="lesson-section-title" id="auto-fill-fit">auto-fill and auto-fit</h2>
<p>These keywords let you create fully responsive grids with zero media queries:</p>
""" + code(""".responsive-grid {
  display: grid;
  gap: 1.5rem;

  /* auto-fill — create as many columns as fit at minimum 250px */
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));

  /* auto-fit — same, but collapses empty tracks */
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

/* Result:
   - Wide screens: many columns
   - Medium screens: fewer columns
   - Small screens: single column
   Zero media queries needed.
*/
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p><code>repeat(auto-fit, minmax(250px, 1fr))</code> is one of the most useful CSS patterns ever written. Add it to your muscle memory — you will use it in almost every project.</p>
</div>
""",
    kc=[
        ("What is the difference between an explicit and implicit grid track?","explicit-implicit"),
        ("What does minmax(200px, 1fr) mean?","minmax"),
        ("What is the difference between auto-fill and auto-fit?","auto-fill-fit"),
    ],
    assignments=[
        "Build a photo gallery that automatically adjusts from 1 to 4 columns based on screen width using auto-fit and minmax — no media queries.",
        "Build a blog card grid where each card has a minimum height set with minmax.",
    ],
    resources=[
        ("MDN — Auto-placement in Grid","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Auto-placement_in_grid_layout"),
        ("CSS Tricks — Auto-Sizing Columns in CSS Grid","https://css-tricks.com/auto-sizing-columns-css-grid-auto-fill-vs-auto-fit/"),
        ("YouTube — Responsive Grid (Kevin Powell)","https://www.youtube.com/watch?v=moBhzSC455o"),
    ])

    write("positioning-grid-elements","Positioning Grid Elements",
    intro="So far grid items have been placed automatically. This lesson covers how to manually position items — spanning multiple rows or columns, and placing items in specific grid cells.",
    overview=[
        "Place items using grid-column and grid-row.",
        "Span items across multiple tracks.",
        "Use named grid lines.",
        "Use grid-area for shorthand placement.",
    ],
    body="""
<h2 class="lesson-section-title" id="line-placement">Line-Based Placement</h2>
<p>Grid lines are numbered starting from 1. You can place items by specifying start and end lines:</p>
""" + code(""".item-a {
  grid-column: 1 / 3;  /* start at line 1, end at line 3 (spans 2 columns) */
  grid-row: 1 / 2;     /* start at row line 1, end at line 2 */
}

/* Shorthand with span keyword */
.item-b {
  grid-column: 2 / span 2;  /* start at line 2, span 2 columns */
  grid-row: span 3;          /* span 3 rows from current position */
}

/* Negative line numbers count from the end */
.full-width {
  grid-column: 1 / -1;  /* span entire row, no matter how many columns */
}
""") + """
<h2 class="lesson-section-title" id="named-lines">Named Grid Lines</h2>
""" + code(""".layout {
  display: grid;
  grid-template-columns:
    [sidebar-start] 250px [sidebar-end main-start] 1fr [main-end];
  grid-template-rows:
    [header-start] 64px [header-end content-start] 1fr [content-end];
}

.header  { grid-column: sidebar-start / main-end; grid-row: header-start; }
.sidebar { grid-column: sidebar-start; grid-row: content-start; }
.main    { grid-column: main-start; grid-row: content-start; }
""") + """
<h2 class="lesson-section-title" id="grid-area">grid-template-areas</h2>
<p>The most readable way to define complex layouts — name the areas and the grid draws itself:</p>
""" + code(""".layout {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-rows: 64px 1fr 48px;
  grid-template-areas:
    "header  header"
    "sidebar main"
    "footer  footer";
  min-height: 100vh;
}

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main    { grid-area: main; }
.footer  { grid-area: footer; }

/* Use a dot for an empty cell */
grid-template-areas:
  "header header header"
  "sidebar main  .     ";
"""),
    kc=[
        ("What does grid-column: 1 / -1 do?","line-placement"),
        ("What is the span keyword used for?","line-placement"),
        ("How do grid-template-areas make layouts more readable?","grid-area"),
    ],
    assignments=[
        "Build a full page layout (header, sidebar, main, footer) using grid-template-areas.",
        "Build a featured articles section where the first article spans two columns.",
    ],
    resources=[
        ("MDN — Line-Based Placement","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Grid_layout_using_line-based_placement"),
        ("MDN — Grid Template Areas","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Grid_template_areas"),
        ("YouTube — Grid Template Areas (Kevin Powell)","https://www.youtube.com/watch?v=v5KzBPUEgGQ"),
    ])

    write("advanced-grid-properties","Advanced Grid Properties",
    intro="This lesson covers the remaining Grid properties that complete your toolkit: alignment within grid cells, the gap shorthand, subgrid, and layering items.",
    overview=[
        "Align items and tracks with justify-items, align-items, justify-content, align-content.",
        "Override alignment on individual items with justify-self and align-self.",
        "Understand the order property for re-ordering items.",
        "Layer items in the same grid cell.",
    ],
    body="""
<h2 class="lesson-section-title" id="alignment">Grid Alignment</h2>
""" + code(""".grid {
  display: grid;
  grid-template-columns: repeat(3, 200px);
  /* The grid tracks are 600px total but the container might be wider */

  /* Align items WITHIN their cell */
  justify-items: start;   /* horizontal within cell (default: stretch) */
  align-items: center;    /* vertical within cell */

  /* Align the GRID ITSELF within the container */
  justify-content: center;      /* horizontal position of the whole grid */
  align-content: space-between; /* vertical position of grid rows */
}

/* Override alignment on a single item */
.featured {
  justify-self: center;
  align-self: end;
}
""") + """
<h2 class="lesson-section-title" id="layering">Layering Items</h2>
<p>Multiple grid items can be placed in the same cell — useful for overlapping text on images or stacked UI effects:</p>
""" + code(""".grid-container {
  display: grid;
  grid-template-columns: 1fr;
}

/* Both items are placed in the same cell */
.background-image {
  grid-column: 1;
  grid-row: 1;
}

.overlay-text {
  grid-column: 1;
  grid-row: 1;
  z-index: 1;
  /* Text sits on top of the image */
}
""") + """
<h2 class="lesson-section-title" id="order">Order</h2>
""" + code("""/* Reorder items visually without changing HTML */
/* Default order is 0. Lower = earlier, higher = later. */
.item-a { order: 2; }  /* moves to the end */
.item-b { order: 1; }
.item-c { order: 0; }  /* appears first (default) */

/* Useful for responsive design — move sidebar below main on mobile */
@media (max-width: 768px) {
  .sidebar { order: 2; }  /* after main on mobile */
  .main    { order: 1; }
}
"""),
    kc=[
        ("What is the difference between justify-items and justify-content in Grid?","alignment"),
        ("How do you place two items in the same grid cell?","layering"),
        ("What does the order property do and why should you be careful with it?","order"),
    ],
    assignments=[
        "Build a dashboard layout that uses grid alignment to position elements precisely within their cells.",
        "Create an image card with overlapping text using grid layering.",
    ],
    resources=[
        ("MDN — Box Alignment in Grid Layout","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Box_alignment_in_grid_layout"),
        ("CSS Tricks — A Complete Guide to Grid","https://css-tricks.com/snippets/css/complete-guide-grid/"),
        ("YouTube — Advanced CSS Grid (Kevin Powell)","https://www.youtube.com/watch?v=N5wpD9Ov_To"),
    ])

    write("using-flexbox-and-grid","Using Flexbox and Grid",
    intro="Flexbox and Grid are not competitors — they are partners. This lesson covers how to combine them effectively, and how to decide which to reach for in any given situation.",
    overview=[
        "Know the decision framework for choosing Grid vs Flexbox.",
        "Combine Grid and Flexbox in the same layout.",
        "Understand common layout patterns that use both.",
    ],
    body="""
<h2 class="lesson-section-title" id="decision">The Decision Framework</h2>
<ul>
  <li><strong>Use Grid when</strong> you need to control layout in two dimensions simultaneously — rows and columns together. Page layouts, dashboards, complex card arrangements.</li>
  <li><strong>Use Flexbox when</strong> you are laying out items in a single direction — a row of buttons, a navigation bar, a stack of cards. Also ideal when you want items to naturally wrap.</li>
  <li><strong>Use both together</strong> — Grid for the overall page structure, Flexbox for the components inside each grid area.</li>
</ul>

<h2 class="lesson-section-title" id="combining">Combining Them in Practice</h2>
""" + code("""/* Grid handles the macro layout */
.page {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "footer";
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}

/* Flexbox handles the header's internal layout */
.header {
  grid-area: header;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;
  height: 64px;
}

/* Grid handles the card section */
.card-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

/* Flexbox handles what is inside each card */
.card {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;  /* push footer to the bottom of the card */
}
""") + """
<h2 class="lesson-section-title" id="common-patterns">Common Layout Patterns</h2>
""" + code("""/* Holy Grail Layout */
.holy-grail {
  display: grid;
  grid-template: auto 1fr auto / 200px 1fr 200px;
  grid-template-areas:
    "header  header  header"
    "nav     main    aside"
    "footer  footer  footer";
  min-height: 100vh;
}

/* Sidebar layout */
.with-sidebar {
  display: grid;
  grid-template-columns: minmax(200px, 25%) 1fr;
  gap: 2rem;
}

/* Pancake stack — full-width sections stacked vertically */
.pancake {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}
"""),
    kc=[
        ("When should you use Grid instead of Flexbox?","decision"),
        ("How do Grid and Flexbox typically work together in a page layout?","combining"),
        ("What is the Holy Grail layout?","common-patterns"),
    ],
    assignments=[
        "Build the Holy Grail layout using Grid for the structure and Flexbox for the internal layout of each section.",
        "Refactor a previous project to deliberately use Grid at the page level and Flexbox at the component level.",
    ],
    resources=[
        ("MDN — Relationship of Grid to Other Layout Methods","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Relationship_of_grid_layout_with_other_layout_methods"),
        ("CSS Tricks — Does CSS Grid Replace Flexbox?","https://css-tricks.com/css-grid-replace-flexbox/"),
        ("YouTube — Grid vs Flexbox (Kevin Powell)","https://www.youtube.com/watch?v=3elGSZSWTbM"),
    ])

    write("project-admin-dashboard","Project: Admin Dashboard",
    intro="The Admin Dashboard project brings together everything from both the Intermediate CSS and Grid sections — positioning, custom properties, advanced selectors, and a complex Grid layout.",
    overview=[
        "Build a complete admin dashboard UI using CSS Grid.",
        "Use Grid for both the page layout and the card grids within it.",
        "Apply custom properties, advanced selectors, and all CSS techniques from this course.",
        "Make the dashboard responsive.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>Sidebar navigation</strong> — fixed-width, full-height, with nav links and active state</li>
  <li><strong>Top header bar</strong> — site name, search input, user avatar</li>
  <li><strong>Main content area</strong> with at least:
    <ul>
      <li>A stats row — four cards showing key numbers</li>
      <li>A recent activity table</li>
      <li>A projects grid — cards with title, description, and progress</li>
    </ul>
  </li>
  <li>Uses CSS Grid for the overall layout and inner grids</li>
  <li>Uses custom properties for the entire colour scheme</li>
  <li>Responsive: sidebar collapses or moves on small screens</li>
</ul>

<h2 class="lesson-section-title" id="layout-structure">Layout Structure</h2>
""" + code("""/* Overall layout — Grid */
.dashboard {
  display: grid;
  grid-template-columns: 260px 1fr;
  grid-template-rows: 64px 1fr;
  grid-template-areas:
    "sidebar header"
    "sidebar main";
  min-height: 100vh;
}

/* Stats row — Flexbox or Grid */
.stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

/* Projects grid */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}
""") + code("""mkdir ~/devpath-projects/admin-dashboard
cd ~/devpath-projects/admin-dashboard
git init
touch index.html styles.css
code .
"""),
    kc=[
        ("What grid-template-areas layout works well for an admin dashboard?","layout-structure"),
        ("How do you make the sidebar full-height?","layout-structure"),
    ],
    assignments=[
        "Build the Admin Dashboard meeting all requirements above.",
        "Push to GitHub and publish on GitHub Pages.",
    ],
    resources=[
        ("CSS Tricks — A Complete Guide to Grid","https://css-tricks.com/snippets/css/complete-guide-grid/"),
        ("YouTube — Build an Admin Dashboard (Traversy Media)","https://www.youtube.com/watch?v=moBhzSC455o"),
        ("MDN — CSS Grid Layout","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout"),
    ])

    write("introduction-to-web-accessibility","Introduction to Web Accessibility",
    intro="Accessibility means building websites that everyone can use — including the roughly 1 in 7 people worldwide who have a disability. This lesson introduces what accessibility means and why it matters.",
    overview=[
        "Understand what web accessibility means and who it benefits.",
        "Know the main categories of disabilities that affect web usage.",
        "Understand assistive technologies like screen readers.",
        "Know the difference between WCAG compliance levels.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-is-a11y">What Is Accessibility?</h2>
<p>Web accessibility (often abbreviated <strong>a11y</strong> — a, 11 letters, y) means building websites and applications that can be used by people with disabilities. This includes people with:</p>
<ul>
  <li><strong>Visual impairments</strong> — blindness, low vision, colour blindness</li>
  <li><strong>Motor impairments</strong> — difficulty using a mouse, tremors, paralysis</li>
  <li><strong>Cognitive disabilities</strong> — dyslexia, ADHD, autism spectrum</li>
  <li><strong>Auditory impairments</strong> — deafness or hard of hearing</li>
</ul>
<p>Accessibility is not just about disabilities. Good accessibility also benefits people using a phone in bright sunlight, people with slow internet connections, elderly users, and people using keyboard-only navigation.</p>

<h2 class="lesson-section-title" id="assistive-tech">Assistive Technologies</h2>
<p>The most important assistive technology for web developers to understand is the <strong>screen reader</strong> — software that reads page content aloud. Popular screen readers include NVDA (free, Windows), VoiceOver (built into macOS and iOS), and TalkBack (built into Android).</p>
<p>Screen readers navigate web pages by reading out HTML structure: headings, landmarks, links, form labels, and alt text. This is exactly why semantic HTML matters so much — a screen reader cannot read a visual layout, only the underlying code.</p>

<h2 class="lesson-section-title" id="wcag">WCAG and Compliance Levels</h2>
<p>The <strong>Web Content Accessibility Guidelines (WCAG)</strong> are the international standard for web accessibility. Published by the W3C, they organise requirements around four principles: <strong>Perceivable, Operable, Understandable, Robust</strong> (POUR).</p>
<p>WCAG has three conformance levels:</p>
<ul>
  <li><strong>A</strong> — Minimum. Failing this excludes some users entirely.</li>
  <li><strong>AA</strong> — The standard target for most organisations. Required by law in many countries.</li>
  <li><strong>AAA</strong> — Highest level. Not required for entire sites but worth aiming for in key areas.</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Good news: most accessibility improvements are also good user experience improvements. A site with clear headings, good colour contrast, and keyboard navigation is a better site for everyone — not just people with disabilities.</p>
</div>
""",
    kc=[
        ("What does a11y stand for?","what-is-a11y"),
        ("What is a screen reader and how does it navigate a page?","assistive-tech"),
        ("What are the three WCAG conformance levels?","wcag"),
    ],
    assignments=[
        "Download and try NVDA (Windows) or use VoiceOver (Mac: Cmd+F5) on one of your own projects. Note what works and what does not.",
        "Read the MDN Accessibility overview linked below.",
    ],
    resources=[
        ("MDN — Accessibility Overview","https://developer.mozilla.org/en-US/docs/Learn/Accessibility/What_is_accessibility"),
        ("WebAIM — Introduction to Web Accessibility","https://webaim.org/intro/"),
        ("YouTube — Web Accessibility Introduction (Google Chrome Developers)","https://www.youtube.com/watch?v=20SHvU2PKsM"),
    ])

    write("wcag","The Web Content Accessibility Guidelines",
    intro="WCAG is the framework that defines what an accessible website looks like. This lesson breaks down the four POUR principles and the most important success criteria you need to implement.",
    overview=[
        "Understand the four POUR principles of WCAG.",
        "Know the key AA-level success criteria you must meet.",
        "Use automated testing tools to check for WCAG issues.",
    ],
    body="""
<h2 class="lesson-section-title" id="pour">The POUR Principles</h2>
<p>All WCAG success criteria fall under four principles:</p>
<ul>
  <li><strong>Perceivable</strong> — Information must be presentable in ways users can perceive. Examples: alt text for images, captions for videos, sufficient colour contrast.</li>
  <li><strong>Operable</strong> — Interface components must be operable. Examples: all functionality available by keyboard, no keyboard traps, sufficient time limits.</li>
  <li><strong>Understandable</strong> — Information and operation must be understandable. Examples: clear language, consistent navigation, helpful error messages.</li>
  <li><strong>Robust</strong> — Content must work with current and future assistive technologies. Examples: valid HTML, correct ARIA usage.</li>
</ul>

<h2 class="lesson-section-title" id="key-criteria">Key AA-Level Success Criteria</h2>
""" + code("""/* 1.4.3 — Colour Contrast (AA) */
/* Text must have a contrast ratio of at least 4.5:1 against background */
/* Large text (18px+ regular, 14px+ bold): at least 3:1 */

/* 2.1.1 — Keyboard Access */
/* All functionality must be available from the keyboard */
/* No keyboard traps */

/* 2.4.3 — Focus Order */
/* Focus must move through the page in a logical order */

/* 2.4.7 — Focus Visible */
/* Any element with keyboard focus must have a visible focus indicator */

/* 3.1.1 — Language of Page */
/* The human language of the page must be identified in the HTML */
<html lang="en">

/* 4.1.2 — Name, Role, Value */
/* UI components must have accessible names and roles */
""") + """
<h2 class="lesson-section-title" id="testing">Automated Testing Tools</h2>
<ul>
  <li><strong>axe DevTools</strong> — Browser extension that audits a page for WCAG violations directly in DevTools.</li>
  <li><strong>Lighthouse</strong> — Built into Chrome DevTools. Run an audit from the Lighthouse tab.</li>
  <li><strong>WAVE</strong> — Another browser extension with visual overlay showing issues on the page.</li>
</ul>
<p>Automated tools catch around 30–40% of accessibility issues. Manual testing with a keyboard and screen reader is still necessary for the rest.</p>
""",
    kc=[
        ("What do the four letters in POUR stand for?","pour"),
        ("What contrast ratio does AA-level WCAG require for normal text?","key-criteria"),
        ("What percentage of accessibility issues can automated tools catch?","testing"),
    ],
    assignments=[
        "Run a Lighthouse accessibility audit on one of your projects. Fix every issue it flags.",
        "Install the axe DevTools extension and audit the same project. Compare the findings.",
    ],
    resources=[
        ("WCAG 2.1 Quick Reference","https://www.w3.org/WAI/WCAG21/quickref/"),
        ("axe DevTools Browser Extension","https://www.deque.com/axe/devtools/"),
        ("YouTube — WCAG Explained (Deque)","https://www.youtube.com/watch?v=MzFr4_JvFdg"),
    ])

    write("accessible-colors","Accessible Colors",
    intro="Colour contrast is one of the most common and most fixable accessibility failures. This lesson covers the contrast requirements and the tools that make meeting them easy.",
    overview=[
        "Understand the WCAG colour contrast requirements.",
        "Use contrast checking tools to verify your colour choices.",
        "Build a colour palette that meets AA requirements.",
        "Consider colour blindness in your designs.",
    ],
    body="""
<h2 class="lesson-section-title" id="contrast-ratios">Contrast Ratios</h2>
<p>Colour contrast is measured as a ratio between the relative luminance of two colours:</p>
<ul>
  <li><strong>AA — Normal text:</strong> minimum 4.5:1</li>
  <li><strong>AA — Large text</strong> (18px regular / 14px bold): minimum 3:1</li>
  <li><strong>AA — UI components</strong> (buttons, inputs, focus indicators): minimum 3:1</li>
  <li><strong>AAA — Normal text:</strong> 7:1 (enhanced, not required everywhere)</li>
</ul>
<p>Pure white (<code>#ffffff</code>) on pure black (<code>#000000</code>) has a contrast ratio of 21:1 — the maximum. A light grey on white might be 1.5:1 — completely inaccessible.</p>

<h2 class="lesson-section-title" id="tools">Contrast Checking Tools</h2>
""" + code("""/* Useful tools for checking contrast */

/* 1. WebAIM Contrast Checker — https://webaim.org/resources/contrastchecker/ */
/* Enter two hex colours, get the ratio and pass/fail for AA and AAA */

/* 2. Colour Contrast Analyser (desktop app) — picks any two colours on screen */

/* 3. browser DevTools — Chrome DevTools shows contrast ratio */
/* when you click on a text colour in the styles pane */

/* 4. CSS: use high-contrast colours by default */
:root {
  --text: #1e293b;       /* dark on white: 15.5:1 — excellent */
  --text-muted: #64748b; /* on white: 4.6:1 — passes AA */
  --text-subtle: #94a3b8;/* on white: 2.9:1 — FAILS AA for small text */
}
""") + """
<h2 class="lesson-section-title" id="color-blindness">Colour Blindness</h2>
<p>About 8% of males and 0.5% of females have some form of colour blindness. The most common is red-green colour blindness (deuteranopia), where red and green appear similar.</p>
<p>Key principles:</p>
<ul>
  <li><strong>Never use colour alone</strong> to convey information. Always add a text label, icon, or pattern.</li>
  <li>For success/error states: use green/red with checkmark/X icons — not colour alone.</li>
  <li>Test with tools like the Firefox Accessibility Inspector's colour blindness simulation.</li>
</ul>
""" + code("""<!-- Bad: colour alone distinguishes required fields -->
<input type="email" style="border-color: red;">  <!-- fails -->

<!-- Good: colour + icon + text -->
<div class="field error">
  <input type="email" aria-describedby="email-error">
  <p id="email-error" class="error-message">
    ⚠ Please enter a valid email address
  </p>
</div>
"""),
    kc=[
        ("What is the minimum contrast ratio for normal text at AA level?","contrast-ratios"),
        ("Why should you never use colour alone to convey information?","color-blindness"),
        ("Name two tools for checking colour contrast.","tools"),
    ],
    assignments=[
        "Check the colour contrast of all text in one of your projects using WebAIM's contrast checker. Fix any failures.",
        "Test your project in Firefox's colour blindness simulation mode.",
    ],
    resources=[
        ("WebAIM — Colour Contrast Checker","https://webaim.org/resources/contrastchecker/"),
        ("MDN — Colour and Colour Contrast","https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG/Perceivable/Color_contrast"),
        ("YouTube — Colour Accessibility (Kevin Powell)","https://www.youtube.com/watch?v=FzXFzk9RsI8"),
    ])

    write("keyboard-navigation","Keyboard Navigation",
    intro="Many users navigate entirely by keyboard — people with motor disabilities, power users, and anyone using a screen reader. Your site must be fully operable without a mouse.",
    overview=[
        "Understand how keyboard navigation works in the browser.",
        "Ensure all interactive elements are keyboard-accessible.",
        "Implement visible, well-designed focus styles.",
        "Manage focus correctly for dynamic content.",
    ],
    body="""
<h2 class="lesson-section-title" id="how-it-works">How Keyboard Navigation Works</h2>
<p>In a browser, keyboard users navigate with:</p>
<ul>
  <li><kbd>Tab</kbd> — move focus forward through interactive elements</li>
  <li><kbd>Shift+Tab</kbd> — move focus backward</li>
  <li><kbd>Enter</kbd> — activate a link or button</li>
  <li><kbd>Space</kbd> — activate a button, checkbox, or select</li>
  <li><kbd>Arrow keys</kbd> — navigate within components (menus, radios, sliders)</li>
  <li><kbd>Escape</kbd> — dismiss modals and menus</li>
</ul>
<p>Interactive HTML elements — <code>&lt;a&gt;</code>, <code>&lt;button&gt;</code>, <code>&lt;input&gt;</code>, <code>&lt;select&gt;</code>, <code>&lt;textarea&gt;</code> — are focusable by default. <code>&lt;div&gt;</code> and <code>&lt;span&gt;</code> are NOT.</p>

<h2 class="lesson-section-title" id="focus-styles">Focus Styles</h2>
""" + code("""/* NEVER do this — it removes the only visual indicator for keyboard users */
*       { outline: none; }          /* terrible */
button:focus { outline: 0; }       /* also terrible */

/* DO this — a clear, branded focus style */
:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 3px;
  border-radius: 3px;
}

/* :focus-visible only shows the focus ring for keyboard navigation */
/* not for mouse clicks — the best of both worlds */
button:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.2);
}
""") + """
<h2 class="lesson-section-title" id="tabindex">tabindex</h2>
""" + code("""<!-- tabindex="0" — adds a non-interactive element to the tab order -->
<div tabindex="0" role="button">Click me</div>

<!-- tabindex="-1" — removes from tab order but can receive focus via JS -->
<!-- Useful for managing focus in modals and dynamic content -->
<div tabindex="-1" id="modal-content">Modal body</div>

<!-- JavaScript: programmatically move focus -->
document.querySelector('#modal-content').focus();

<!-- tabindex > 0 — DO NOT USE — creates unpredictable tab order -->
<button tabindex="3">Avoid this</button>
""") + """
<h2 class="lesson-section-title" id="skip-links">Skip Navigation Links</h2>
""" + code("""<!-- Allows keyboard users to skip repetitive navigation -->
<!-- Placed as the very first element in the body -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<nav>...</nav>
<main id="main-content">...</main>
""") + code(""".skip-link {
  position: absolute;
  top: -100%;      /* off-screen by default */
  left: 0;
  background: #2563eb;
  color: white;
  padding: 0.5rem 1rem;
  z-index: 9999;
  text-decoration: none;
}

.skip-link:focus {
  top: 0;          /* visible when focused by keyboard */
}
"""),
    kc=[
        ("Which HTML elements are keyboard-focusable by default?","how-it-works"),
        ("What is :focus-visible and why is it better than :focus?","focus-styles"),
        ("What does tabindex='-1' do?","tabindex"),
        ("What is a skip link and why is it important?","skip-links"),
    ],
    assignments=[
        "Navigate one of your projects using only the keyboard (Tab, Shift+Tab, Enter, Space). Identify and fix all issues you encounter.",
        "Add a skip link to the top of one of your projects.",
        "Replace any outline: none rules with a proper :focus-visible style.",
    ],
    resources=[
        ("MDN — Keyboard-accessible JavaScript widgets","https://developer.mozilla.org/en-US/docs/Web/Accessibility/Keyboard-navigable_JavaScript_widgets"),
        ("WebAIM — Keyboard Accessibility","https://webaim.org/techniques/keyboard/"),
        ("YouTube — Keyboard Navigation (Google Chrome Developers)","https://www.youtube.com/watch?v=EIkNaBMkxhE"),
    ])

    write("meaningful-text","Meaningful Text",
    intro="The words you use in your HTML — link text, button labels, headings, alt text — are the primary way screen reader users understand your page. This lesson covers how to write text that communicates clearly for everyone.",
    overview=[
        "Write descriptive link text that makes sense out of context.",
        "Write meaningful button labels.",
        "Use headings to create a navigable document structure.",
        "Write good alt text for images in different contexts.",
    ],
    body="""
<h2 class="lesson-section-title" id="link-text">Link Text</h2>
<p>Screen reader users often navigate by pulling up a list of all links on the page. Links need to make sense when read in isolation, out of their surrounding context.</p>
""" + code("""<!-- Bad — meaningless out of context -->
<a href="/pricing">Click here</a>
<a href="/docs">Read more</a>
<a href="/contact">Here</a>

<!-- Good — descriptive on their own -->
<a href="/pricing">View pricing plans</a>
<a href="/docs">Read the documentation</a>
<a href="/contact">Contact our support team</a>

<!-- Multiple "Read more" links on one page — bad -->
<a href="/post-1">Read more</a>
<a href="/post-2">Read more</a>

<!-- Better — use visually-hidden text to distinguish them -->
<a href="/post-1">
  Read more
  <span class="visually-hidden"> about Getting Started with CSS</span>
</a>
""") + """
<h2 class="lesson-section-title" id="buttons">Button Labels</h2>
""" + code("""<!-- Bad — icon-only button with no label -->
<button><svg>...</svg></button>

<!-- Good — icon + visible label -->
<button><svg aria-hidden="true">...</svg> Delete account</button>

<!-- Good — icon-only with aria-label -->
<button aria-label="Delete account">
  <svg aria-hidden="true">...</svg>
</button>

<!-- Good — icon-only with tooltip via title -->
<button title="Close menu">
  <svg aria-hidden="true">...</svg>
</button>
""") + """
<h2 class="lesson-section-title" id="headings">Heading Structure</h2>
<p>Screen reader users navigate between headings like a sighted user scans a page. A logical heading structure is one of the highest-impact accessibility improvements you can make.</p>
""" + code("""<!-- Bad — headings chosen for visual size, not structure -->
<h1>Home</h1>
<h3>Welcome</h3>       <!-- skipped h2 -->
<h1>Our Services</h1>  <!-- second h1 -->

<!-- Good — logical, nested hierarchy -->
<h1>DevPath — Learn Web Development</h1>
  <h2>Foundations Course</h2>
    <h3>Introduction</h3>
    <h3>HTML Basics</h3>
  <h2>Full Stack JavaScript</h2>
    <h3>Intermediate HTML and CSS</h3>
""") + """
<h2 class="lesson-section-title" id="visually-hidden">The Visually-Hidden Pattern</h2>
""" + code("""/* Hide text visually but keep it accessible to screen readers */
/* DO NOT use display:none or visibility:hidden — those hide from everyone */
.visually-hidden {
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
"""),
    kc=[
        ("Why must link text make sense out of context?","link-text"),
        ("How do you make an icon-only button accessible?","buttons"),
        ("What is the visually-hidden pattern and when do you use it?","visually-hidden"),
    ],
    assignments=[
        "Audit all links in one of your projects. Replace any 'click here' or 'read more' text with descriptive labels.",
        "Add aria-label or visually-hidden text to any icon-only buttons in your projects.",
    ],
    resources=[
        ("MDN — Writing CSS for Accessibility","https://developer.mozilla.org/en-US/docs/Learn/Accessibility/CSS_and_JavaScript"),
        ("WebAIM — Links and Hypertext","https://webaim.org/techniques/hypertext/"),
        ("YouTube — Accessible Text (Google Chrome Developers)","https://www.youtube.com/watch?v=e2nkq3h1P68"),
    ])

    write("wai-aria","WAI-ARIA",
    intro="WAI-ARIA (Accessible Rich Internet Applications) is a specification that lets you communicate additional semantic information to assistive technologies — information that HTML alone cannot express.",
    overview=[
            "Understand when to use ARIA and when not to.",
            "Use ARIA roles to define element purpose.",
            "Use ARIA properties and states to convey dynamic information.",
            "Follow the first rule of ARIA.",
    ],
    body="""
<h2 class="lesson-section-title" id="first-rule">The First Rule of ARIA</h2>
<p>The most important rule about ARIA is: <strong>do not use ARIA if you can use native HTML instead.</strong></p>
""" + code("""<!-- Do NOT do this -->
<div role="button" tabindex="0" onclick="submit()">Submit</div>

<!-- DO this — native HTML has all the semantics built in -->
<button type="submit">Submit</button>

<!-- ARIA is for cases where native HTML falls short:
     - Custom interactive widgets (tabs, accordions, carousels)
     - Dynamic content updates
     - Complex relationships between elements              -->
""") + """
<h2 class="lesson-section-title" id="roles">ARIA Roles</h2>
""" + code("""<!-- Landmark roles — help screen reader users navigate page sections -->
<header role="banner">...</header>     <!-- site header -->
<nav role="navigation">...</nav>       <!-- navigation -->
<main role="main">...</main>           <!-- main content -->
<aside role="complementary">...</aside><!-- sidebar -->
<footer role="contentinfo">...</footer><!-- site footer -->

<!-- Note: HTML5 elements like header, nav, main already have implicit roles -->
<!-- The role attributes above are redundant but sometimes useful for clarity -->

<!-- Widget roles — for custom interactive components -->
<div role="tablist">
  <button role="tab" aria-selected="true">Tab 1</button>
  <button role="tab" aria-selected="false">Tab 2</button>
</div>
<div role="tabpanel">Content for tab 1</div>
""") + """
<h2 class="lesson-section-title" id="properties-states">ARIA Properties and States</h2>
""" + code("""<!-- aria-label — provides an accessible name -->
<button aria-label="Close dialog">×</button>

<!-- aria-labelledby — points to an element that labels this one -->
<section aria-labelledby="section-heading">
  <h2 id="section-heading">Recent Projects</h2>
  ...
</section>

<!-- aria-describedby — points to additional description -->
<input
  type="password"
  aria-describedby="password-hint"
>
<p id="password-hint">Password must be at least 8 characters</p>

<!-- aria-hidden — hides from assistive technology -->
<svg aria-hidden="true" focusable="false">...</svg>

<!-- aria-expanded — state of expandable elements -->
<button aria-expanded="false" aria-controls="menu">Menu</button>
<ul id="menu" hidden>...</ul>

<!-- aria-live — announce dynamic content changes -->
<div aria-live="polite" id="status">
  <!-- content updated here is announced by screen readers -->
</div>
"""),
    kc=[
        ("What is the first rule of ARIA?","first-rule"),
        ("What is aria-hidden used for?","properties-states"),
        ("What does aria-live do?","properties-states"),
        ("When should you use role='button' on a div?","first-rule"),
    ],
    assignments=[
        "Add appropriate ARIA attributes to any custom interactive components in your projects.",
        "Read the MDN ARIA guides linked below.",
    ],
    resources=[
        ("MDN — ARIA","https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA"),
        ("WAI-ARIA Authoring Practices","https://www.w3.org/WAI/ARIA/apg/"),
        ("YouTube — ARIA Tutorial (Google Chrome Developers)","https://www.youtube.com/watch?v=g9Qff0b-lHk"),
    ])

    write("introduction-to-responsive-design","Introduction to Responsive Design",
    intro="Responsive design means building websites that look and work well on every screen size — from a 320px mobile phone to a 4K monitor. This lesson introduces the philosophy and core techniques.",
    overview=[
        "Understand what responsive design is and why it matters.",
        "Know the three pillars of responsive design.",
        "Understand the mobile-first approach.",
        "Know the difference between responsive and adaptive design.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-is-responsive">What Is Responsive Design?</h2>
<p>Responsive web design (RWD) is an approach where a website's layout and content fluidly adapt to the size of the device displaying it. The same HTML is served to all devices — CSS handles the presentation differences.</p>
<p>This matters because over 60% of web traffic now comes from mobile devices. A site that only looks good on a desktop is failing the majority of its users.</p>

<h2 class="lesson-section-title" id="three-pillars">The Three Pillars</h2>
<ol>
  <li><strong>Fluid grids</strong> — layouts built with relative units (%, fr) rather than fixed pixels, so they stretch and compress naturally.</li>
  <li><strong>Flexible images</strong> — images that scale within their containers and never overflow them.</li>
  <li><strong>Media queries</strong> — CSS rules that apply only when the viewport matches certain conditions (e.g., screen width is below 768px).</li>
</ol>

<h2 class="lesson-section-title" id="mobile-first">Mobile-First Design</h2>
<p>Mobile-first means writing your base CSS for the smallest screens, then adding media queries to enhance the layout for larger screens. This is the recommended approach because:</p>
<ul>
  <li>It forces you to prioritise content — what is truly essential on a small screen?</li>
  <li>It results in leaner CSS — you start minimal and add, rather than starting large and overriding.</li>
  <li>Performance is better — mobile users only download styles they need.</li>
</ul>
""" + code("""/* Mobile-first: base styles for small screens */
.container {
  padding: 1rem;
}
.card-grid {
  display: grid;
  grid-template-columns: 1fr;   /* single column on mobile */
  gap: 1rem;
}

/* Add more columns as the screen gets wider */
@media (min-width: 640px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  .container {
    padding: 2rem;
  }
}
"""),
    kc=[
        ("What are the three pillars of responsive design?","three-pillars"),
        ("What does mobile-first mean in terms of how you write CSS?","mobile-first"),
        ("Why is mobile-first recommended over desktop-first?","mobile-first"),
    ],
    assignments=[
        "Read Ethan Marcotte's original 'Responsive Web Design' article — linked below.",
        "Identify three websites you use daily. View them at mobile, tablet, and desktop widths. Note what changes between breakpoints.",
    ],
    resources=[
        ("A List Apart — Responsive Web Design (Ethan Marcotte)","https://alistapart.com/article/responsive-web-design/"),
        ("MDN — Responsive Design","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design"),
        ("YouTube — Responsive Design Explained (Kevin Powell)","https://www.youtube.com/watch?v=VQraviuwbzU"),
    ])

    write("natural-responsiveness","Natural Responsiveness",
    intro="Many layout techniques create responsive results automatically without media queries. This lesson covers how to write CSS that is naturally fluid.",
    overview=[
        "Use relative units to create fluid typography and spacing.",
        "Use Flexbox and Grid patterns that respond automatically.",
        "Avoid fixed widths that break layouts.",
    ],
    body="""
<h2 class="lesson-section-title" id="fluid-type">Fluid Typography</h2>
""" + code("""/* clamp() creates fluid type with no media queries */
h1 { font-size: clamp(1.75rem, 4vw, 3rem);   }
h2 { font-size: clamp(1.35rem, 3vw, 2.25rem); }
p  { font-size: clamp(1rem,    1.5vw, 1.125rem); }

/* Fluid spacing */
.section {
  padding: clamp(2rem, 8vw, 6rem) clamp(1rem, 5vw, 3rem);
}

/* Container that never gets too wide */
.container {
  width: min(90%, 1200px);  /* 90% on mobile, max 1200px on large screens */
  margin-inline: auto;       /* centre it */
}
""") + """
<h2 class="lesson-section-title" id="responsive-flex">Naturally Responsive Flexbox</h2>
""" + code("""/* flex-wrap: wrap + flex: 1 1 min-width */
/* Items wrap naturally when they run out of space */
.card-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.card {
  flex: 1 1 280px;  /* items are at least 280px, fill space, wrap as needed */
}

/* Result: 4 columns on wide screens → 2 → 1 as width decreases */
/* Zero media queries needed */
""") + """
<h2 class="lesson-section-title" id="responsive-grid">Naturally Responsive Grid</h2>
""" + code("""/* auto-fit + minmax — the most powerful responsive pattern */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

/* Image galleries */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 0.5rem;
}
""") + """
<h2 class="lesson-section-title" id="avoid-fixed">Avoiding Fixed Widths</h2>
""" + code("""/* Fragile — breaks on small screens */
.card { width: 400px; }

/* Better — flexible with a maximum */
.card {
  width: 100%;
  max-width: 400px;
}

/* Images — always include this */
img {
  display: block;
  max-width: 100%;   /* image never overflows its container */
  height: auto;      /* maintain aspect ratio */
}
"""),
    kc=[
        ("How does clamp() create responsive typography without media queries?","fluid-type"),
        ("What CSS makes a Flexbox layout wrap naturally?","responsive-flex"),
        ("Why should you use max-width instead of width for fixed-size elements?","avoid-fixed"),
    ],
    assignments=[
        "Rebuild a previous project's typography using clamp() for all font sizes.",
        "Refactor a card grid to use auto-fit and minmax — remove any media queries that were only adjusting column counts.",
    ],
    resources=[
        ("MDN — Responsive Images","https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images"),
        ("YouTube — Stop using media queries (Kevin Powell)","https://www.youtube.com/watch?v=OwNyUkJ1WDM"),
        ("CSS Tricks — A Complete Guide to CSS Functions","https://css-tricks.com/complete-guide-to-css-functions/"),
    ])

    write("responsive-images","Responsive Images",
    intro="Images are the largest assets on most web pages. Serving the right image at the right size for each device dramatically improves performance and user experience.",
    overview=[
            "Use the srcset attribute to serve different image resolutions.",
            "Use the sizes attribute to describe image display widths.",
            "Use the picture element for art direction.",
            "Use modern image formats (WebP, AVIF) for better compression.",
    ],
    body="""
<h2 class="lesson-section-title" id="srcset">srcset — Resolution Switching</h2>
""" + code("""<!-- The browser picks the most appropriate image size -->
<img
  src="hero-800.jpg"
  srcset="
    hero-400.jpg  400w,
    hero-800.jpg  800w,
    hero-1200.jpg 1200w,
    hero-1600.jpg 1600w
  "
  alt="A mountainous landscape at sunrise"
>

<!-- w descriptor = actual pixel width of the image file -->
<!-- The browser uses this + sizes to pick the best option -->
""") + """
<h2 class="lesson-section-title" id="sizes">sizes — Telling the Browser the Display Size</h2>
""" + code("""<img
  srcset="hero-400.jpg 400w, hero-800.jpg 800w, hero-1200.jpg 1200w"
  sizes="
    (max-width: 640px)  100vw,
    (max-width: 1024px) 80vw,
    1200px
  "
  src="hero-800.jpg"
  alt="A mountainous landscape"
>

<!-- sizes reads as:
   "On screens ≤640px: image fills 100% of viewport width"
   "On screens ≤1024px: image fills 80% of viewport width"
   "Otherwise: image is 1200px wide"
-->
""") + """
<h2 class="lesson-section-title" id="picture">picture — Art Direction</h2>
""" + code("""<!-- Show a different image crop depending on screen size -->
<picture>
  <!-- Tall crop for mobile portrait screens -->
  <source
    srcset="hero-mobile.jpg"
    media="(max-width: 480px)"
  >

  <!-- Square crop for tablet -->
  <source
    srcset="hero-tablet.jpg"
    media="(max-width: 768px)"
  >

  <!-- Modern format with fallback -->
  <source
    srcset="hero.avif"
    type="image/avif"
  >
  <source
    srcset="hero.webp"
    type="image/webp"
  >

  <!-- Fallback img — always required -->
  <img src="hero.jpg" alt="A mountainous landscape">
</picture>
""") + """
<h2 class="lesson-section-title" id="formats">Modern Image Formats</h2>
<ul>
  <li><strong>WebP</strong> — 25-35% smaller than JPEG/PNG at the same quality. Supported in all modern browsers.</li>
  <li><strong>AVIF</strong> — Even smaller than WebP (30-50% smaller than JPEG). Excellent for photographs. Growing browser support.</li>
  <li><strong>SVG</strong> — For icons and illustrations. Infinitely scalable, tiny file size.</li>
</ul>
""",
    kc=[
        ("What does the w descriptor in srcset represent?","srcset"),
        ("What does the sizes attribute tell the browser?","sizes"),
        ("When would you use the picture element over srcset?","picture"),
    ],
    assignments=[
        "Convert a project's main hero image to use srcset with at least three sizes.",
        "Convert an image to WebP format using Squoosh (linked below) and compare file sizes.",
    ],
    resources=[
        ("MDN — Responsive Images","https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images"),
        ("Squoosh — Image Compression Tool","https://squoosh.app/"),
        ("YouTube — Responsive Images (Kevin Powell)","https://www.youtube.com/watch?v=2QYpkrX2N48"),
    ])

    write("media-queries","Media Queries",
    intro="Media queries are the tool that lets you apply different CSS rules based on the characteristics of the device or viewport. They are the foundation of responsive design when natural responsiveness is not enough.",
    overview=[
            "Write media queries using min-width and max-width.",
            "Use the mobile-first approach with min-width queries.",
            "Query other media features: height, orientation, prefers-color-scheme, prefers-reduced-motion.",
            "Understand modern container queries.",
    ],
    body="""
<h2 class="lesson-section-title" id="syntax">Media Query Syntax</h2>
""" + code("""/* Basic syntax */
@media media-type and (condition) {
  /* CSS rules applied when condition is true */
}

/* Most common: screen width */
@media (min-width: 768px) { ... }  /* mobile-first: adds styles from 768px up */
@media (max-width: 767px) { ... }  /* desktop-first: adds styles below 768px */

/* Multiple conditions */
@media (min-width: 640px) and (max-width: 1023px) { ... }  /* tablet range */

/* Common breakpoints */
/* Mobile:  < 640px  (base styles in mobile-first) */
/* Tablet:   640px+ */
/* Desktop: 1024px+ */
/* Wide:    1280px+ */
""") + """
<h2 class="lesson-section-title" id="mobile-first-queries">Mobile-First with min-width</h2>
""" + code("""/* Base styles: mobile */
.nav {
  display: flex;
  flex-direction: column;
}

.hero-title {
  font-size: 1.75rem;
}

.card-grid {
  grid-template-columns: 1fr;
}

/* Tablet: 640px and up */
@media (min-width: 640px) {
  .hero-title {
    font-size: 2.25rem;
  }
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop: 1024px and up */
@media (min-width: 1024px) {
  .nav {
    flex-direction: row;
  }
  .hero-title {
    font-size: 3rem;
  }
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
""") + """
<h2 class="lesson-section-title" id="user-preferences">User Preference Queries</h2>
""" + code("""/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --bg:   #0f172a;
    --text: #f1f5f9;
  }
}

/* Reduced motion — respect users who have set this in their OS */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* Print styles */
@media print {
  .no-print { display: none; }
  body { font-size: 12pt; color: black; }
}
""") + """
<h2 class="lesson-section-title" id="container-queries">Container Queries</h2>
<p>Media queries respond to the viewport size. Container queries respond to the size of the <em>parent element</em>. This is a newer feature with broad modern browser support:</p>
""" + code("""/* Define a container */
.card-wrapper {
  container-type: inline-size;
  container-name: card;
}

/* Style the card differently based on its OWN container width */
@container card (min-width: 400px) {
  .card {
    display: flex;        /* horizontal layout when card is wide enough */
    flex-direction: row;
  }
  .card-image {
    width: 200px;
  }
}
"""),
    kc=[
        ("What is the difference between min-width and max-width media queries?","syntax"),
        ("Why does mobile-first use min-width instead of max-width?","mobile-first-queries"),
        ("What does prefers-reduced-motion do?","user-preferences"),
        ("How do container queries differ from media queries?","container-queries"),
    ],
    assignments=[
        "Make the Admin Dashboard project fully responsive using media queries. It should work well on mobile, tablet, and desktop.",
        "Add prefers-color-scheme and prefers-reduced-motion queries to a project.",
    ],
    resources=[
        ("MDN — Media Queries","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries"),
        ("MDN — Container Queries","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries"),
        ("YouTube — Media Queries (Kevin Powell)","https://www.youtube.com/watch?v=K24lUqcT0Ms"),
    ])

    write("project-homepage","Project: Homepage",
    intro="The Homepage project is the capstone of this course. You will build a complete, responsive personal homepage that demonstrates every major technique covered — from semantic HTML and CSS Grid to accessibility and responsive images.",
    overview=[
            "Build a complete responsive homepage from scratch.",
            "Apply CSS Grid, Flexbox, custom properties, and all CSS techniques from this course.",
            "Ensure the page is accessible: good contrast, keyboard-navigable, semantic HTML.",
            "Make it fully responsive across mobile, tablet, and desktop.",
            "Publish the finished project on GitHub Pages.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>Header</strong> — logo/name, navigation, skip link, mobile hamburger menu</li>
  <li><strong>Hero section</strong> — responsive heading (clamp), subtext, CTA button, background image with proper alt/decorative handling</li>
  <li><strong>About section</strong> — text + image in a two-column grid layout</li>
  <li><strong>Projects section</strong> — responsive card grid using auto-fit/minmax, each card with an image, title, description, and link</li>
  <li><strong>Skills section</strong> — a visual representation of your skills</li>
  <li><strong>Contact section</strong> — accessible form with validation</li>
  <li><strong>Footer</strong> — links and copyright</li>
</ul>
<p>Content can be real (your actual skills and projects) or placeholder — but the HTML structure and CSS must be complete.</p>

<h2 class="lesson-section-title" id="requirements-checklist">Requirements Checklist</h2>
<ul>
  <li>CSS custom properties for the entire colour scheme</li>
  <li>Modern CSS reset at the top of the stylesheet</li>
  <li>Mobile-first responsive design with at least two breakpoints</li>
  <li>Passes Lighthouse accessibility audit with a score of 90+</li>
  <li>All images have appropriate alt text</li>
  <li>All interactive elements are keyboard-accessible with visible focus styles</li>
  <li>No outline: none anywhere in the CSS</li>
  <li>Colour contrast meets AA standards throughout</li>
</ul>

<h2 class="lesson-section-title" id="workflow">Project Workflow</h2>
""" + code("""mkdir ~/devpath-projects/personal-homepage
cd ~/devpath-projects/personal-homepage
git init
touch index.html styles.css script.js
code .

# Commit structure first
git add .
git commit -m "Add initial HTML structure"

# Commit CSS in sections
git commit -m "Add base styles and custom properties"
git commit -m "Add header and hero section styles"
# etc.

# Publish when done
# GitHub → Settings → Pages → main → / (root) → Save
"""),
    kc=[
        ("What accessibility score should the page achieve on Lighthouse?","requirements-checklist"),
        ("What CSS feature should handle all colour values throughout the stylesheet?","requirements-checklist"),
    ],
    assignments=[
        "Complete the Homepage project meeting all requirements and the checklist.",
        "Run a Lighthouse audit and reach 90+ on Accessibility. Fix everything it flags.",
        "Push to GitHub Pages and share the live URL.",
    ],
    resources=[
        ("MDN — Responsive Design","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design"),
        ("Google Lighthouse Documentation","https://developer.chrome.com/docs/lighthouse/"),
        ("YouTube — Build a Responsive Website (Kevin Powell)","https://www.youtube.com/watch?v=p0bGHP-PXD4"),
    ])

    print("\nAll 33 Intermediate HTML and CSS lessons seeded.")

    os.chdir(BASE)
    subprocess.run(["git","add","-A"], check=True)
    subprocess.run(["git","commit","-m","Seed: Intermediate HTML and CSS — all 33 lessons fully written"], check=True)
    subprocess.run(["git","push"], check=True)
    print("Pushed to GitHub.")

if __name__ == "__main__":
    seed()
