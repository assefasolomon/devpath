#!/usr/bin/env python3
import os, subprocess

BASE    = os.path.expanduser("~/devpath")
LESSONS = os.path.join(BASE, "foundations", "lessons")

ALL_LESSONS = [
    ("how-this-course-will-work",      "How This Course Will Work"),
    ("introduction-to-web-dev",        "Introduction to Web Development"),
    ("motivation-and-mindset",         "Motivation and Mindset"),
    ("asking-for-help",                "Asking For Help"),
    ("join-the-community",             "Join the Odin Community"),
    ("computer-basics",                "Computer Basics"),
    ("how-does-the-web-work",          "How Does the Web Work?"),
    ("installation-overview",          "Installation Overview"),
    ("installations",                  "Installations"),
    ("text-editors",                   "Text Editors"),
    ("command-line-basics",            "Command Line Basics"),
    ("setting-up-git",                 "Setting Up Git"),
    ("introduction-to-git",            "Introduction to Git"),
    ("git-basics",                     "Git Basics"),
    ("introduction-to-html-css",       "Introduction to HTML and CSS"),
    ("elements-and-tags",              "Elements and Tags"),
    ("html-boilerplate",               "HTML Boilerplate"),
    ("working-with-text",              "Working with Text"),
    ("lists",                          "Lists"),
    ("links-and-images",               "Links and Images"),
    ("commit-messages",                "Commit Messages"),
    ("project-recipes",                "Project: Recipes"),
    ("intro-to-css",                   "Intro to CSS"),
    ("the-cascade",                    "The Cascade"),
    ("inspecting-html-and-css",        "Inspecting HTML and CSS"),
    ("the-box-model",                  "The Box Model"),
    ("block-and-inline",               "Block and Inline"),
    ("introduction-to-flexbox",        "Introduction to Flexbox"),
    ("growing-and-shrinking",          "Growing and Shrinking"),
    ("axes",                           "Axes"),
    ("alignment",                      "Alignment"),
    ("project-landing-page",           "Project: Landing Page"),
    ("variables-and-operators",        "Variables and Operators"),
    ("data-types-and-conditionals",    "Data Types and Conditionals"),
    ("javascript-developer-tools",     "JavaScript Developer Tools"),
    ("function-basics",                "Function Basics"),
    ("problem-solving",                "Problem Solving"),
    ("understanding-errors",           "Understanding Errors"),
    ("project-rock-paper-scissors",    "Project: Rock Paper Scissors"),
    ("clean-code",                     "Clean Code"),
    ("installing-nodejs",              "Installing Node.js"),
    ("arrays-and-loops",               "Arrays and Loops"),
    ("dom-manipulation-and-events",    "DOM Manipulation and Events"),
    ("revisiting-rock-paper-scissors", "Revisiting Rock Paper Scissors"),
    ("project-etch-a-sketch",          "Project: Etch-a-Sketch"),
    ("object-basics",                  "Object Basics"),
    ("project-calculator",             "Project: Calculator"),
    ("choose-your-path",               "Choose Your Path Forward"),
]

LOGO = '<svg viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="13" stroke="currentColor" stroke-width="1.8"/><path d="M8 14 L14 7 L20 14 L14 21 Z" fill="currentColor"/></svg>'

def nav():
    return (
        '<nav class="site-nav">'
        '<a href="../../index.html" class="nav-logo">' + LOGO + ' DevPath</a>'
        '<ul class="nav-links">'
        '<li><a href="../../index.html">Home</a></li>'
        '<li><a href="../index.html">Foundations</a></li>'
        '<li><a href="../../paths/full-stack-javascript/index.html">Full Stack JS</a></li>'
        '<li><a href="../../paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a></li>'
        '</ul></nav>'
    )

def footer():
    return '<footer class="site-footer"><p>DevPath — A free, open, project-based web development curriculum.</p></footer>'

def sidebar(active_slug):
    def lnk(slug, title, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "") + (" active" if slug == active_slug else "")
        return f'<a href="{slug}.html" class="{cls}">{title}</a>\n'
    s = '<aside class="sidebar"><div class="sidebar-course-title">Foundations</div>'
    s += '<div class="sidebar-section"><div class="sidebar-section-label">Introduction</div>'
    for sl,ti in [("how-this-course-will-work","How This Course Will Work"),("introduction-to-web-dev","Introduction to Web Development"),("motivation-and-mindset","Motivation and Mindset"),("asking-for-help","Asking For Help"),("join-the-community","Join the Community")]:
        s += lnk(sl,ti)
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">Prerequisites</div>'
    for sl,ti in [("computer-basics","Computer Basics"),("how-does-the-web-work","How Does the Web Work?"),("installation-overview","Installation Overview"),("installations","Installations"),("text-editors","Text Editors"),("command-line-basics","Command Line Basics"),("setting-up-git","Setting Up Git")]:
        s += lnk(sl,ti)
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">Git Basics</div>'
    for sl,ti in [("introduction-to-git","Introduction to Git"),("git-basics","Git Basics")]:
        s += lnk(sl,ti)
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">HTML Foundations</div>'
    for sl,ti,*p in [("introduction-to-html-css","Introduction to HTML and CSS"),("elements-and-tags","Elements and Tags"),("html-boilerplate","HTML Boilerplate"),("working-with-text","Working with Text"),("lists","Lists"),("links-and-images","Links and Images"),("commit-messages","Commit Messages"),("project-recipes","Project: Recipes","proj")]:
        s += lnk(sl,ti,bool(p))
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">CSS Foundations</div>'
    for sl,ti in [("intro-to-css","Intro to CSS"),("the-cascade","The Cascade"),("inspecting-html-and-css","Inspecting HTML and CSS"),("the-box-model","The Box Model"),("block-and-inline","Block and Inline")]:
        s += lnk(sl,ti)
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">Flexbox</div>'
    for sl,ti,*p in [("introduction-to-flexbox","Introduction to Flexbox"),("growing-and-shrinking","Growing and Shrinking"),("axes","Axes"),("alignment","Alignment"),("project-landing-page","Project: Landing Page","proj")]:
        s += lnk(sl,ti,bool(p))
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">JavaScript Basics</div>'
    for sl,ti,*p in [("variables-and-operators","Variables and Operators"),("data-types-and-conditionals","Data Types and Conditionals"),("javascript-developer-tools","JavaScript Developer Tools"),("function-basics","Function Basics"),("problem-solving","Problem Solving"),("understanding-errors","Understanding Errors"),("project-rock-paper-scissors","Project: Rock Paper Scissors","proj"),("clean-code","Clean Code"),("installing-nodejs","Installing Node.js"),("arrays-and-loops","Arrays and Loops"),("dom-manipulation-and-events","DOM Manipulation and Events"),("revisiting-rock-paper-scissors","Revisiting Rock Paper Scissors"),("project-etch-a-sketch","Project: Etch-a-Sketch","proj"),("object-basics","Object Basics"),("project-calculator","Project: Calculator","proj")]:
        s += lnk(sl,ti,bool(p))
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">Conclusion</div>'
    s += lnk("choose-your-path","Choose Your Path Forward")
    s += '</div></aside>'
    return s

def code(snippet):
    esc = snippet.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f'<div class="code-block"><pre><code>{esc}</code></pre></div>'

def prev_next(slug):
    idx = next((i for i,l in enumerate(ALL_LESSONS) if l[0]==slug), None)
    p = (ALL_LESSONS[idx-1][1], ALL_LESSONS[idx-1][0]+".html") if idx and idx>0 else None
    n = (ALL_LESSONS[idx+1][1], ALL_LESSONS[idx+1][0]+".html") if idx is not None and idx<len(ALL_LESSONS)-1 else None
    return p,n

def nav_bar(slug):
    p,n = prev_next(slug)
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
    p,n = prev_next(slug)
    bc = (f'<nav class="breadcrumb">'
          f'<a href="../../index.html">Home</a>'
          f'<span class="breadcrumb-sep">/</span>'
          f'<a href="../index.html">Foundations</a>'
          f'<span class="breadcrumb-sep">/</span>'
          f'<span class="breadcrumb-current">{title}</span></nav>')
    ov   = "".join(f"<li>{i}</li>" for i in overview)
    kcli = "".join(f'<li><a href="#{k[1]}" data-target="{k[1]}">{k[0]}</a></li>' for k in kc)
    asli = "".join(f"<li>{a}</li>" for a in assignments)
    rsli = "".join(f'<li><a href="{r[1]}" target="_blank" rel="noopener">{r[0]}</a></li>' for r in resources)
    ph   = f'<a href="{p[1]}" class="pagination-link prev"><span class="pagination-label">&#8592; Previous</span><span class="pagination-title">{p[0]}</span></a>' if p else "<span></span>"
    nh   = f'<a href="{n[1]}" class="pagination-link next"><span class="pagination-label">Next &#8594;</span><span class="pagination-title">{n[0]}</span></a>' if n else "<span></span>"

    html = (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "  <meta charset=\"UTF-8\">\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        f"  <title>{title} | DevPath</title>\n"
        "  <link rel=\"stylesheet\" href=\"../../css/styles.css\">\n"
        "</head>\n<body>\n"
        + nav() + "\n"
        + nav_bar(slug) + "\n"
        + f'<div class="page-header"><div class="page-header-inner">{bc}<h1>{title}</h1></div></div>\n'
        + f'<div class="lesson-layout">{sidebar(slug)}<main><div class="lesson-body">\n'
        + f'<div class="block-intro"><p>{intro}</p></div>\n'
        + f'<div class="block-overview"><div class="block-overview-label">Lesson Overview</div><ul>{ov}</ul></div>\n'
        + body
        + f'\n<div class="block-kc"><div class="block-kc-label">Knowledge Check</div>'
        + f'<p class="kc-note">Click any question to jump to the section that answers it.</p>'
        + f'<ol>{kcli}</ol></div>\n'
        + f'<div class="block-assignments"><div class="block-assignments-label">Assignments</div><ol>{asli}</ol></div>\n'
        + f'<div class="block-resources"><div class="block-resources-label">Additional Resources</div><ul>{rsli}</ul></div>\n'
        + f'</div><div class="lesson-pagination">{ph}{nh}</div></main></div>\n'
        + footer() + "\n"
        + '<script src="../../js/main.js"></script>\n</body>\n</html>'
    )
    with open(os.path.join(LESSONS, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  {slug}")


# ════════════════════════════════════════════════════════════
#  LESSONS 14 → 27
# ════════════════════════════════════════════════════════════

def seed():

    # 14 ── Introduction to HTML and CSS ─────────────────────
    write("introduction-to-html-css","Introduction to HTML and CSS",
    intro="HTML and CSS are the two foundational languages of the web. Every website you have ever visited is built on them. This lesson gives you a clear picture of what each language does and how they work together.",
    overview=[
        "Describe what HTML is responsible for on a web page.",
        "Describe what CSS is responsible for on a web page.",
        "Understand the relationship between HTML and CSS.",
    ],
    body="""
<h2 class="lesson-section-title" id="html-role">What HTML Does</h2>
<p><strong>HTML (HyperText Markup Language)</strong> defines the <em>structure</em> and <em>content</em> of a web page. It tells the browser what things <em>are</em> — this is a heading, this is a paragraph, this is an image, this is a navigation menu.</p>
<p>Think of HTML as the skeleton of a building. It establishes the load-bearing structure without any visual decoration.</p>
""" + code("""<!DOCTYPE html>
<html lang="en">
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Welcome to My Site</h1>
    <p>This is a paragraph of text.</p>
    <img src="photo.jpg" alt="A photo">
  </body>
</html>
""") + """
<h2 class="lesson-section-title" id="css-role">What CSS Does</h2>
<p><strong>CSS (Cascading Style Sheets)</strong> controls the <em>visual presentation</em> of HTML — colours, fonts, spacing, layout, animations. It answers the question: "How should this look?"</p>
<p>Using the building analogy: CSS is the paint, the furniture, the lighting. The structure is already there from HTML — CSS makes it beautiful.</p>
""" + code("""/* CSS targets HTML elements and applies visual styles */
h1 {
  color: #1d4ed8;
  font-size: 2.5rem;
  font-weight: 700;
}

p {
  color: #475569;
  line-height: 1.75;
  max-width: 65ch;
}

img {
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
""") + """
<h2 class="lesson-section-title" id="together">How They Work Together</h2>
<p>HTML and CSS are separate languages kept in separate files on purpose. This separation of concerns keeps your code organised and maintainable. One HTML page can be completely restyled just by swapping its CSS file — without touching a single line of HTML.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>A useful mental model: HTML is the noun (what things <em>are</em>) and CSS is the adjective (how they <em>look</em>). JavaScript — which you will learn later — is the verb (what things <em>do</em>).</p>
</div>
""",
    kc=[
        ("What is HTML responsible for on a web page?","html-role"),
        ("What is CSS responsible for on a web page?","css-role"),
        ("Why are HTML and CSS kept in separate files?","together"),
    ],
    assignments=[
        "Read the MDN article 'Getting Started with HTML' linked below.",
        "Read the MDN article 'What is CSS?' linked below.",
    ],
    resources=[
        ("MDN — Getting Started with HTML","https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started"),
        ("MDN — What is CSS?","https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS"),
        ("YouTube — HTML and CSS for Beginners (Kevin Powell)","https://www.youtube.com/watch?v=qz0aGYrrlhU"),
    ])

    # 15 ── Elements and Tags ─────────────────────────────────
    write("elements-and-tags","Elements and Tags",
    intro="HTML is built from elements. Understanding exactly what an element is — and how tags, content, and attributes work together — gives you a solid foundation for everything that follows.",
    overview=[
        "Explain the difference between an HTML element and an HTML tag.",
        "Identify opening tags, closing tags, and self-closing (void) elements.",
        "Understand how elements nest correctly inside one another.",
    ],
    body="""
<h2 class="lesson-section-title" id="elements">Elements and Tags</h2>
<p>An <strong>HTML element</strong> is made up of an opening tag, content, and a closing tag working together:</p>
""" + code("""<!-- Structure of a standard HTML element -->
<tagname>Content goes here</tagname>

<!-- Real examples -->
<p>This is a paragraph.</p>
<h1>This is a top-level heading.</h1>
<strong>This text is bold.</strong>
<em>This text is italic.</em>
""") + """
<p>The <strong>tag</strong> is just the part inside the angle brackets — <code>&lt;p&gt;</code> or <code>&lt;/p&gt;</code>. The <strong>element</strong> is the complete unit: opening tag + content + closing tag.</p>

<h2 class="lesson-section-title" id="void">Void Elements</h2>
<p>Some elements have no content and no closing tag. These are called <strong>void elements</strong> or self-closing elements:</p>
""" + code("""<!-- Void elements — no closing tag needed -->
<img src="sunset.jpg" alt="A golden sunset">
<input type="text" placeholder="Enter your name">
<br>
<hr>
<meta charset="UTF-8">
<link rel="stylesheet" href="styles.css">
""") + """
<h2 class="lesson-section-title" id="nesting">Nesting Elements</h2>
<p>Elements can contain other elements. The rule is strict: close tags in the reverse order you opened them — like removing stacked rings.</p>
""" + code("""<!-- CORRECT — inner closes before outer -->
<p>I love <strong>web development</strong> deeply.</p>

<ul>
  <li>First item</li>
  <li>Second <em>important</em> item</li>
</ul>

<!-- WRONG — tags overlap instead of nest -->
<p>I love <strong>web development</p></strong>
""") + """
<h2 class="lesson-section-title" id="attributes">Attributes</h2>
<p>Attributes give extra information to an element. They always live inside the opening tag:</p>
""" + code("""<!-- attribute="value" syntax -->
<a href="https://example.com">Visit Example</a>
<img src="photo.jpg" alt="Description of photo">
<input type="email" placeholder="you@example.com">
<div class="card" id="hero">Content</div>
"""),
    kc=[
        ("What is the difference between an HTML tag and an HTML element?","elements"),
        ("What is a void element? Name two examples.","void"),
        ("What rule must you follow when nesting HTML elements?","nesting"),
        ("Where do attributes go in an HTML element?","attributes"),
    ],
    assignments=[
        "Without looking at any reference, write 8 different HTML elements from memory. Then verify each one on MDN.",
        "Read MDN's 'Getting started with HTML' article, focusing on the 'Anatomy of an HTML element' section (linked below).",
    ],
    resources=[
        ("MDN — Getting Started with HTML","https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started"),
        ("YouTube — HTML Crash Course for Absolute Beginners (Traversy Media)","https://www.youtube.com/watch?v=UB1O30fR-EE"),
        ("MDN — HTML Element Reference","https://developer.mozilla.org/en-US/docs/Web/HTML/Element"),
    ])

    # 16 ── HTML Boilerplate ──────────────────────────────────
    write("html-boilerplate","HTML Boilerplate",
    intro="Every HTML file needs a standard starting structure. This lesson explains what each line of the boilerplate does and how to generate the whole thing in under a second.",
    overview=[
        "Explain the purpose of the DOCTYPE declaration.",
        "Describe what the <code>html</code>, <code>head</code>, and <code>body</code> elements each do.",
        "Write a valid HTML5 boilerplate from memory.",
        "Use the VS Code Emmet shortcut to generate it instantly.",
    ],
    body="""
<h2 class="lesson-section-title" id="boilerplate">The Standard Boilerplate</h2>
""" + code("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title Here</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>

    <!-- All visible content goes here -->

    <script src="script.js"></script>
  </body>
</html>
""") + """
<h2 class="lesson-section-title" id="each-part">What Each Line Does</h2>
<ul>
  <li><code>&lt;!DOCTYPE html&gt;</code> — Tells the browser this is an HTML5 document. Without it, browsers use an unpredictable compatibility mode.</li>
  <li><code>&lt;html lang="en"&gt;</code> — Root element wrapping everything. <code>lang</code> helps screen readers and search engines.</li>
  <li><code>&lt;head&gt;</code> — Contains metadata <em>about</em> the page — not displayed content. Think of it as the page's settings.</li>
  <li><code>&lt;meta charset="UTF-8"&gt;</code> — Use UTF-8 encoding, which supports virtually every character in every language.</li>
  <li><code>&lt;meta name="viewport"&gt;</code> — Makes the page display correctly on mobile devices. Essential.</li>
  <li><code>&lt;title&gt;</code> — Text shown on the browser tab and in search results.</li>
  <li><code>&lt;body&gt;</code> — Everything the user sees lives here.</li>
</ul>

<h2 class="lesson-section-title" id="emmet">Generate It in One Keystroke</h2>
<p>In VS Code, create a new <code>.html</code> file, type <code>!</code> on line 1, and press <code>Tab</code>. Emmet generates the complete boilerplate instantly.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Even though the shortcut is quick, make sure you can write the boilerplate from memory. Understanding each line matters far more than knowing the shortcut.</p>
</div>

<h2 class="lesson-section-title" id="where-scripts">Where to Put Scripts</h2>
<p>Place <code>&lt;script&gt;</code> tags just before <code>&lt;/body&gt;</code>, not in <code>&lt;head&gt;</code>. This ensures the HTML elements exist in the DOM before your JavaScript tries to access them.</p>
""",
    kc=[
        ("What does DOCTYPE tell the browser?","each-part"),
        ("What is the difference between head and body?","each-part"),
        ("What does the viewport meta tag do?","each-part"),
        ("Where should script tags be placed and why?","where-scripts"),
    ],
    assignments=[
        "Create a new HTML file and write the full boilerplate from memory — without using the Emmet shortcut. Open it in Chrome and confirm it loads without errors.",
        "Add a title, h1, and two paragraphs. Link a CSS file (even an empty one). Open DevTools and confirm the stylesheet is being requested.",
    ],
    resources=[
        ("MDN — Document and Website Structure","https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure"),
        ("YouTube — HTML Boilerplate Explained (Kevin Powell)","https://www.youtube.com/watch?v=G3e-cpL7ofc"),
        ("Emmet Docs — Cheat Sheet","https://docs.emmet.io/cheat-sheet/"),
    ])

    # 17 ── Working with Text ─────────────────────────────────
    write("working-with-text","Working with Text",
    intro="Most of what lives on a web page is text. This lesson covers the HTML elements for headings, paragraphs, and emphasis — and the important distinction between semantic and presentational markup.",
    overview=[
        "Use headings h1 through h6 with correct hierarchy.",
        "Wrap body text in paragraph elements.",
        "Use strong and em for semantic emphasis.",
        "Write HTML comments.",
    ],
    body="""
<h2 class="lesson-section-title" id="headings">Headings</h2>
<p>HTML provides six levels of headings. Use them to create a logical content hierarchy — not for visual size:</p>
""" + code("""<h1>Site Name or Page Title</h1>      <!-- One per page -->
<h2>Main Section Heading</h2>
<h3>Subsection Heading</h3>
<h4>Sub-subsection</h4>
<h5>Rarely needed</h5>
<h6>Almost never used</h6>
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Every page should have exactly one <code>h1</code>. Never choose a heading level based on how big you want text to look — use CSS for that. Choose heading levels based on the logical structure of your content.</p>
</div>

<h2 class="lesson-section-title" id="paragraphs">Paragraphs</h2>
""" + code("""<p>This is the first paragraph. The browser automatically adds
space between paragraphs.</p>

<p>This is the second paragraph. Notice each one is its own element —
do not use br tags to fake paragraph spacing.</p>
""") + """
<h2 class="lesson-section-title" id="emphasis">Strong and Em</h2>
<p>HTML distinguishes between <em>semantic</em> importance and <em>visual</em> styling:</p>
""" + code("""<!-- Semantic — carries meaning, not just visual style -->
<p>This step is <strong>critically important</strong> — do not skip it.</p>
<p>The file must be named <em>exactly</em> as shown.</p>

<!-- Presentational only — avoid for content, use for genuine styling -->
<b>Bold without importance</b>
<i>Italic without emphasis</i>
""") + """
<h2 class="lesson-section-title" id="comments">HTML Comments</h2>
""" + code("""<!-- Single line comment — browser ignores this -->

<!--
  Multi-line comment.
  Great for explaining complex sections or temporarily
  disabling a block of HTML during debugging.
-->

<p>This paragraph is visible.</p>
<!-- <p>This paragraph is commented out and hidden.</p> -->
"""),
    kc=[
        ("How many h1 elements should a page have?","headings"),
        ("What is the semantic difference between strong and b?","emphasis"),
        ("Why should you avoid using br tags to separate paragraphs?","paragraphs"),
    ],
    assignments=[
        "Build an HTML page about any topic you enjoy. Use h1, h2, h3, at least four paragraphs, strong, em, and at least two comments.",
        "Read MDN's 'HTML text fundamentals' article linked below.",
    ],
    resources=[
        ("MDN — HTML Text Fundamentals","https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals"),
        ("YouTube — HTML Text and Headings (Kevin Powell)","https://www.youtube.com/watch?v=qz0aGYrrlhU"),
    ])

    # 18 ── Lists ─────────────────────────────────────────────
    write("lists","Lists",
    intro="Lists are one of the most used HTML structures — navigation menus, ingredients, steps, features. HTML gives you two main types and a way to nest them.",
    overview=[
        "Create unordered lists with ul and li.",
        "Create ordered lists with ol and li.",
        "Nest lists within list items.",
    ],
    body="""
<h2 class="lesson-section-title" id="unordered">Unordered Lists</h2>
<p>Use a <strong>ul</strong> when item order does not matter — shopping lists, features, collections:</p>
""" + code("""<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>
""") + """
<h2 class="lesson-section-title" id="ordered">Ordered Lists</h2>
<p>Use an <strong>ol</strong> when sequence matters — numbered instructions, rankings, steps:</p>
""" + code("""<ol>
  <li>Preheat the oven to 200°C.</li>
  <li>Mix the dry ingredients in a large bowl.</li>
  <li>Add wet ingredients and stir until just combined.</li>
  <li>Bake for 25 minutes until golden.</li>
</ol>
""") + """
<h2 class="lesson-section-title" id="nesting">Nesting Lists</h2>
""" + code("""<ul>
  <li>Front-end
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
  </li>
  <li>Back-end
    <ul>
      <li>Node.js</li>
      <li>Databases</li>
    </ul>
  </li>
</ul>
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>The only valid direct children of <code>ul</code> and <code>ol</code> are <code>li</code> elements. Put nested lists <em>inside</em> an <code>li</code>, not directly inside <code>ul</code>/<code>ol</code>.</p>
</div>
""",
    kc=[
        ("When would you choose ol over ul?","ordered"),
        ("What element wraps each item in both list types?","unordered"),
        ("Where does a nested list go — inside li or directly inside ul?","nesting"),
    ],
    assignments=[
        "Add an ordered list of steps and an unordered list of ingredients to the page from the previous lesson.",
        "Create a nested list with at least two levels of depth.",
        "Read MDN's lists article linked below.",
    ],
    resources=[
        ("MDN — HTML Lists","https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals#lists"),
        ("YouTube — HTML Lists Tutorial (Dani Krossing)","https://www.youtube.com/watch?v=HeQvQEiGMKk"),
    ])

    # 19 ── Links and Images ──────────────────────────────────
    write("links-and-images","Links and Images",
    intro="Links are what make the web a web. Images make it visual. This lesson covers both — including the accessibility requirement you must never skip.",
    overview=[
        "Create links with the a element and href attribute.",
        "Understand the difference between absolute and relative links.",
        "Embed images with img using src and alt attributes.",
        "Write meaningful alt text for accessibility.",
    ],
    body="""
<h2 class="lesson-section-title" id="links">Creating Links</h2>
""" + code("""<!-- External link -->
<a href="https://developer.mozilla.org">Visit MDN</a>

<!-- Internal link to another page in your site -->
<a href="about.html">About Us</a>

<!-- Link to a section on the same page -->
<a href="#contact">Jump to Contact</a>

<!-- Opens in a new tab (always add rel="noopener" for security) -->
<a href="https://github.com" target="_blank" rel="noopener noreferrer">
  GitHub
</a>
""") + """
<h2 class="lesson-section-title" id="abs-relative">Absolute vs. Relative Links</h2>
""" + code("""<!-- ABSOLUTE — full URL, works from anywhere -->
<a href="https://www.example.com/about.html">About</a>

<!-- RELATIVE — relative to current file location -->

<!-- Same folder -->
<a href="about.html">About</a>

<!-- Inside a subfolder -->
<a href="recipes/pasta.html">Pasta</a>

<!-- Up one level then into another folder -->
<a href="../index.html">Home</a>
""") + """
<h2 class="lesson-section-title" id="images">Images</h2>
""" + code("""<!-- Local image -->
<img src="images/sunset.jpg" alt="A golden sunset over calm water">

<!-- Remote image -->
<img src="https://example.com/photo.png" alt="A mountain peak at dawn">

<!-- Set dimensions (always good practice) -->
<img src="avatar.jpg" alt="Profile photo" width="200" height="200">
""") + """
<h2 class="lesson-section-title" id="alt">Writing Good Alt Text</h2>
<p>The <code>alt</code> attribute is read aloud by screen readers for visually impaired users. It is also displayed when the image fails to load.</p>
""" + code("""<!-- Bad — meaningless -->
<img src="img1.jpg" alt="image">
<img src="img1.jpg" alt="">  <!-- blank is OK only for decorative images -->

<!-- Good — describes what is shown -->
<img src="team.jpg" alt="Five team members standing in front of our office">
<img src="logo.svg" alt="DevPath logo">

<!-- Decorative image — screen reader skips it -->
<img src="divider.png" alt="" role="presentation">
"""),
    kc=[
        ("What attribute specifies a link's destination?","links"),
        ("What is the difference between an absolute and relative link?","abs-relative"),
        ("Why is the alt attribute on images required?","alt"),
        ("What security attribute should accompany target='_blank'?","links"),
    ],
    assignments=[
        "Add a navigation bar with three relative links and at least two images with descriptive alt text to your project.",
        "Build a three-page mini site where every page links to the other two using relative links.",
        "Read WebAIM's alt text guide linked below.",
    ],
    resources=[
        ("MDN — Creating Hyperlinks","https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks"),
        ("WebAIM — Alternative Text Guide","https://webaim.org/techniques/alttext/"),
        ("YouTube — HTML Links and Images (Kevin Powell)","https://www.youtube.com/watch?v=ts_qze4KqKA"),
    ])

    # 20 ── Commit Messages ───────────────────────────────────
    write("commit-messages","Commit Messages",
    intro="A commit message is a permanent label attached to a snapshot of your code. Writing clear, consistent messages is a professional habit that pays dividends the moment you work in a team — or return to your own code six months later.",
    overview=[
        "Explain why good commit messages matter.",
        "Follow the seven rules of a great commit message.",
        "Know when to commit and how often.",
    ],
    body="""
<h2 class="lesson-section-title" id="why">Why They Matter</h2>
<p>Your commit history is a log of every decision you made while building something. A well-written log lets you — and your team — answer the question "why does this code exist?" without reading the code itself.</p>
""" + code("""# A bad commit history — tells you nothing
git log --oneline
3f2c1b1 fix
9d8e7f6 stuff
1a2b3c4 wip
0z9y8x7 changes

# A good commit history — tells the whole story
git log --oneline
3f2c1b1 Fix nav links breaking below 768px
9d8e7f6 Add real-time form validation to sign-up page
1a2b3c4 Refactor hero section layout to use Flexbox
0z9y8x7 Add initial project structure and HTML boilerplate
""") + """
<h2 class="lesson-section-title" id="rules">The Seven Rules</h2>
<ol>
  <li>Separate subject from body with a blank line.</li>
  <li>Limit the subject line to 50 characters.</li>
  <li>Capitalise the subject line.</li>
  <li>Do not end the subject line with a period.</li>
  <li><strong>Use the imperative mood</strong> — "Fix bug" not "Fixed bug".</li>
  <li>Wrap the body at 72 characters.</li>
  <li>Use the body to explain <em>what</em> and <em>why</em>, not <em>how</em>.</li>
</ol>
""" + code("""# Subject only (most common for small changes)
git commit -m "Add password strength indicator to signup form"

# Subject + body (for changes that need explanation)
git commit -m "Fix race condition in auth token refresh

The previous implementation checked token expiry after the
request was already in flight, causing occasional 401 errors
on slow connections. Now we check and refresh before sending.

Closes #142"
""") + """
<h2 class="lesson-section-title" id="when">When to Commit</h2>
<p>Commit after each logical unit of work — one feature, one bug fix, one refactor. Small focused commits are far easier to review and revert than large ones mixing many changes.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>A useful test: can you describe the change in a single short sentence without using "and"? If you need "and", it is probably two separate commits.</p>
</div>
""",
    kc=[
        ("What mood should commit message subject lines use?","rules"),
        ("What should the commit body explain — what, why, or how?","rules"),
        ("When is it time to make a new commit?","when"),
    ],
    assignments=[
        "Read Chris Beams' article 'How to Write a Git Commit Message' linked below — it is the definitive reference.",
        "Review three of your previous commit messages. Rewrite them in your notes following the seven rules.",
    ],
    resources=[
        ("Chris Beams — How to Write a Git Commit Message","https://cbea.ms/git-commit/"),
        ("YouTube — Write Better Commit Messages (Fireship)","https://www.youtube.com/watch?v=Hlp-9cdImSM"),
        ("Conventional Commits Specification","https://www.conventionalcommits.org/"),
    ])

    # 21 ── Project: Recipes ──────────────────────────────────
    write("project-recipes","Project: Recipes",
    intro="Time to put everything from the HTML Foundations section into practice. You will build a multi-page recipe website — structured with HTML only, no CSS yet.",
    overview=[
        "Build a multi-page HTML website from scratch.",
        "Use headings, paragraphs, lists, links, and images together.",
        "Connect pages using relative links.",
        "Track and publish the project with Git and GitHub.",
    ],
    body="""
<h2 class="lesson-section-title" id="brief">Project Brief</h2>
<p>Build a recipe website. It will look plain — that is intentional. The goal is practising HTML structure, not visual design. You will style it in a later project.</p>

<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>index.html</strong> homepage with:
    <ul>
      <li>A site heading (h1)</li>
      <li>A list of links to each recipe page</li>
    </ul>
  </li>
  <li><strong>At least three recipe pages</strong>, each with:
    <ul>
      <li>Recipe title (h1) and description paragraph</li>
      <li>An image with descriptive alt text</li>
      <li>An unordered list of ingredients</li>
      <li>An ordered list of steps</li>
      <li>A link back to the homepage</li>
    </ul>
  </li>
  <li>All pages linked together with relative links</li>
  <li>Git repo with at least one commit per page, pushed to GitHub</li>
</ul>

<h2 class="lesson-section-title" id="structure">Folder Structure</h2>
""" + code("""odin-recipes/
├── index.html
└── recipes/
    ├── lasagne.html
    ├── pancakes.html
    └── chicken-soup.html
""") + """
<h2 class="lesson-section-title" id="steps">Step by Step</h2>
""" + code("""# 1. Create the project and initialise Git
mkdir ~/devpath-projects/odin-recipes
cd ~/devpath-projects/odin-recipes
git init

# 2. Build index.html with your recipe links
# 3. Create the recipes/ folder
mkdir recipes

# 4. Build each recipe page
# 5. Commit after each page
git add .
git commit -m "Add lasagne recipe page"

# 6. Push to GitHub when done
git remote add origin git@github.com:USERNAME/odin-recipes.git
git branch -M main
git push -u origin main
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Do not add CSS yet. The purpose of this project is HTML structure. Adding CSS now splits your focus and obscures whether your HTML is correct.</p>
</div>
""",
    kc=[
        ("What HTML elements are needed on each recipe page?","requirements"),
        ("What type of links connect recipe pages back to the homepage?","requirements"),
    ],
    assignments=[
        "Complete the Recipes project fulfilling all requirements above.",
        "Push the finished project to GitHub. Share the repository link — this is your first published project.",
    ],
    resources=[
        ("MDN — HTML Element Reference","https://developer.mozilla.org/en-US/docs/Web/HTML/Element"),
        ("YouTube — Build a Simple Multi-Page Website (Kevin Powell)","https://www.youtube.com/watch?v=PlxWf493en4"),
    ])

    # 22 ── Intro to CSS ──────────────────────────────────────
    write("intro-to-css","Intro to CSS",
    intro="HTML gives your page structure. CSS gives it style. This lesson introduces how CSS works, how to write rules, and the three ways to attach styles to your HTML.",
    overview=[
        "Write a CSS rule with selector, property, and value.",
        "Use element, class, and ID selectors.",
        "Know the three ways to add CSS and why external stylesheets are the right approach.",
    ],
    body="""
<h2 class="lesson-section-title" id="anatomy">Anatomy of a CSS Rule</h2>
""" + code("""selector {
  property: value;
  property: value;
}

/* Real example */
p {
  color: #334155;
  font-size: 1.1rem;
  line-height: 1.75;
}
""") + """
<ul>
  <li><strong>Selector</strong> — targets which HTML elements to style</li>
  <li><strong>Property</strong> — the aspect you are changing (color, size, spacing…)</li>
  <li><strong>Value</strong> — the setting for that property</li>
</ul>

<h2 class="lesson-section-title" id="selectors">Basic Selectors</h2>
""" + code("""/* Element selector — every h1 on the page */
h1 {
  font-size: 2.5rem;
  color: #1e3a8a;
}

/* Class selector — any element with class="card" */
.card {
  background: #f8fafc;
  border-radius: 8px;
  padding: 1.5rem;
}

/* ID selector — the ONE element with id="hero" */
#hero {
  background: linear-gradient(135deg, #1e3a8a, #2563eb);
  color: white;
}

/* Combining: p elements that are inside a .card */
.card p {
  font-size: 0.9rem;
  color: #64748b;
}
""") + """
<h2 class="lesson-section-title" id="three-ways">Three Ways to Add CSS</h2>
""" + code("""<!-- 1. INLINE — directly on the element. Avoid for real projects. -->
<p style="color: red; font-weight: bold;">Warning text</p>

<!-- 2. INTERNAL — style block in the head. OK for tiny demos. -->
<head>
  <style>
    p { color: navy; }
  </style>
</head>

<!-- 3. EXTERNAL — separate .css file. Always use this for real work. -->
<head>
  <link rel="stylesheet" href="styles.css">
</head>
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>External stylesheets keep HTML clean, let you share styles across every page, and mean one CSS change updates the whole site simultaneously. Always use external stylesheets for real projects.</p>
</div>
""",
    kc=[
        ("What are the three parts of a CSS rule?","anatomy"),
        ("What is the difference between a class and an ID selector?","selectors"),
        ("What are the three ways to add CSS and which is preferred?","three-ways"),
    ],
    assignments=[
        "Create a styles.css file and link it to your Recipes project. Add at least 8 style rules covering colour, font size, background, and spacing.",
        "Work through The Odin Project's CSS Foundations exercises linked below.",
    ],
    resources=[
        ("MDN — CSS First Steps","https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps"),
        ("The Odin Project — CSS Foundations exercises","https://github.com/TheOdinProject/css-exercises"),
        ("YouTube — CSS Tutorial Zero to Hero (freeCodeCamp)","https://www.youtube.com/watch?v=1Rs2ND1ryYc"),
        ("YouTube — CSS in 100 Seconds (Fireship)","https://www.youtube.com/watch?v=OEV8gMkCHXQ"),
    ])

    # 23 ── The Cascade ───────────────────────────────────────
    write("the-cascade","The Cascade",
    intro="CSS stands for Cascading Style Sheets. That word — cascading — is the key. When multiple rules target the same element, the cascade determines which one wins.",
    overview=[
        "Define specificity and explain how it resolves conflicts.",
        "Understand the roles of specificity, inheritance, and source order.",
        "Calculate the specificity weight of any selector.",
    ],
    body="""
<h2 class="lesson-section-title" id="cascade">What Is the Cascade?</h2>
<p>The cascade evaluates three factors in order of priority:</p>
<ol>
  <li><strong>Specificity</strong> — how precisely does the selector target the element?</li>
  <li><strong>Source order</strong> — when specificity ties, the later rule wins.</li>
  <li><strong>Inheritance</strong> — some properties pass down from parent to child automatically.</li>
</ol>

<h2 class="lesson-section-title" id="specificity">Specificity</h2>
""" + code("""/* Specificity weights (low → high) */

/* Element: 0-0-1 */
p { color: black; }

/* Class: 0-1-0  — wins over element */
.intro { color: navy; }

/* ID: 1-0-0  — wins over class */
#hero-text { color: gold; }

/* Inline style: wins over all selectors */
<p style="color: red;">

/* !important: nuclear option — avoid it */
p { color: purple !important; }

/* Combined: class(0-1-0) + element(0-0-1) = 0-1-1 */
.intro p { font-size: 1.1rem; }
""") + """
<h2 class="lesson-section-title" id="inheritance">Inheritance</h2>
""" + code("""/* These properties ARE inherited by children */
body {
  font-family: 'Sora', sans-serif;  /* every element inherits this */
  color: #334155;                    /* every text element inherits this */
  line-height: 1.75;
}

/* These properties are NOT inherited */
div {
  border: 1px solid #e2e8f0;  /* children do NOT get a border */
  padding: 1rem;               /* children do NOT get padding */
  width: 400px;                /* children do NOT inherit width */
}
""") + """
<h2 class="lesson-section-title" id="source-order">Source Order</h2>
""" + code("""/* When specificity is equal, later wins */
p { color: red; }
p { color: blue; }
/* Result: blue — it appears later */

/* Order in HTML also matters for linked stylesheets */
<link rel="stylesheet" href="base.css">      <!-- loaded first -->
<link rel="stylesheet" href="overrides.css"> <!-- wins on ties -->
"""),
    kc=[
        ("What three factors does the cascade consider?","cascade"),
        ("Which has higher specificity — a class or an ID?","specificity"),
        ("Is the CSS color property inherited by child elements?","inheritance"),
        ("When two rules have identical specificity, which wins?","source-order"),
    ],
    assignments=[
        "Open DevTools on any website. Inspect an element and look at the Styles pane. Find at least one overridden (strikethrough) rule and trace why it lost.",
        "Work through The Odin Project's CSS Cascade exercises linked below.",
    ],
    resources=[
        ("MDN — Cascade and Inheritance","https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance"),
        ("The Odin Project — CSS Foundations exercises","https://github.com/TheOdinProject/css-exercises"),
        ("CSS Specificity Calculator","https://specificity.keegan.st/"),
        ("YouTube — CSS Specificity Explained (Kevin Powell)","https://www.youtube.com/watch?v=c0kfcP_nD9E"),
    ])

    # 24 ── Inspecting HTML and CSS ───────────────────────────
    write("inspecting-html-and-css","Inspecting HTML and CSS",
    intro="Browser DevTools are your most powerful debugging tool. This lesson shows you how to inspect elements, test CSS changes live, and diagnose spacing problems in seconds.",
    overview=[
        "Open and navigate browser DevTools.",
        "Inspect any element to see its HTML and applied styles.",
        "Edit CSS live in the browser to test changes.",
        "Use the box model diagram to debug spacing.",
    ],
    body="""
<h2 class="lesson-section-title" id="opening">Opening DevTools</h2>
""" + code("""# Keyboard shortcut (all platforms)
F12

# Mac alternative
Cmd + Option + I

# Right-click method
Right-click any element → Inspect

# Find specific element
Ctrl+Shift+C  /  Cmd+Shift+C
Then click any element on the page
""") + """
<h2 class="lesson-section-title" id="elements-panel">The Elements Panel</h2>
<p>The Elements panel shows the live DOM — the HTML structure the browser built from your code. Select any element to see:</p>
<ul>
  <li>Its HTML in the tree on the left</li>
  <li>Every CSS rule applied to it in the Styles pane on the right</li>
  <li>Overridden rules shown with a strikethrough</li>
  <li>Which file and line number each rule comes from</li>
</ul>

<h2 class="lesson-section-title" id="live-css">Live CSS Editing</h2>
<p>Edit CSS directly in DevTools to test changes without touching your files:</p>
<ol>
  <li>Select an element in the Elements panel</li>
  <li>Click any property value in the Styles pane and change it</li>
  <li>Press Tab to jump to the next property</li>
  <li>Click any blank space in a rule to add a new property</li>
  <li>When satisfied, copy the values back into your actual CSS file</li>
</ol>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>DevTools changes are temporary — they vanish on page reload. Always copy successful changes back to your stylesheet.</p>
</div>

<h2 class="lesson-section-title" id="box-model-diagram">The Box Model Diagram</h2>
<p>At the bottom of the Styles pane (or in the Computed tab) you will find a visual diagram of the selected element's box model. Hover over each area to highlight it on the page. This is the fastest way to answer "where is all this space coming from?"</p>
""",
    kc=[
        ("What keyboard shortcut opens DevTools?","opening"),
        ("What does a strikethrough on a CSS rule mean in DevTools?","elements-panel"),
        ("How do you test a CSS change without touching your files?","live-css"),
        ("Where in DevTools can you see the box model diagram?","box-model-diagram"),
    ],
    assignments=[
        "Open DevTools on your Recipes project. Inspect the h1 and identify every CSS rule applied to it.",
        "Use live editing to change the background colour and font of an element. Copy the values you like back into your stylesheet.",
        "Watch the Chrome DevTools intro video linked below.",
    ],
    resources=[
        ("Chrome DevTools — Get started with CSS","https://developer.chrome.com/docs/devtools/css/"),
        ("YouTube — Chrome DevTools Full Tutorial (Traversy Media)","https://www.youtube.com/watch?v=x4q86IjJFag"),
        ("MDN — What are browser developer tools?","https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/What_are_browser_developer_tools"),
    ])

    # 25 ── The Box Model ─────────────────────────────────────
    write("the-box-model","The Box Model",
    intro="Every HTML element is a rectangular box. Understanding how these boxes are sized and spaced is the single most important concept for CSS layout.",
    overview=[
        "Name the four areas of the CSS box model.",
        "Understand the difference between content-box and border-box sizing.",
        "Use margin, padding, and border effectively.",
    ],
    body="""
<h2 class="lesson-section-title" id="four-areas">The Four Areas</h2>
<p>From inside out, every element's box has four layers:</p>
""" + code(""".card {
  /* CONTENT — width and height control this area */
  width: 320px;
  height: auto;

  /* PADDING — space between content and border */
  padding: 24px;

  /* BORDER — line around the padding */
  border: 2px solid #e2e8f0;

  /* MARGIN — space outside the border, between elements */
  margin: 32px;
}
""") + """
<h2 class="lesson-section-title" id="box-sizing">The box-sizing Problem and Fix</h2>
""" + code("""/* DEFAULT: content-box — width only applies to content */
/* Actual rendered width = 300 + 24 + 24 + 2 + 2 = 352px */
.box {
  box-sizing: content-box;
  width: 300px;
  padding: 24px;
  border: 2px solid black;
}

/* BETTER: border-box — width includes padding and border */
/* Actual rendered width = exactly 300px */
.box {
  box-sizing: border-box;
  width: 300px;
  padding: 24px;
  border: 2px solid black;
}

/* Add this to EVERY stylesheet you write */
*,
*::before,
*::after {
  box-sizing: border-box;
}
""") + """
<h2 class="lesson-section-title" id="margin-padding">Margin vs. Padding</h2>
""" + code("""/* PADDING — inside the element, background fills this area */
.button {
  padding: 12px 24px;       /* top/bottom  left/right */
  padding: 12px 24px 12px 24px; /* top right bottom left */
  background: #2563eb;      /* blue extends into padding */
}

/* MARGIN — outside the element, always transparent */
.card {
  margin: 0 auto;           /* centre block element horizontally */
  margin-top: 32px;
  margin-bottom: 16px;
}
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Vertical margins between adjacent block elements collapse — only the larger value applies, not the sum. Use DevTools to investigate when spacing behaves unexpectedly.</p>
</div>
""",
    kc=[
        ("Name the four box model areas from inside to outside.","four-areas"),
        ("What does box-sizing border-box change?","box-sizing"),
        ("What is the practical difference between margin and padding?","margin-padding"),
    ],
    assignments=[
        "Add the universal border-box rule to your stylesheet. Build a card component with explicit padding, border, and margin, and verify dimensions in DevTools.",
        "Work through The Odin Project's Box Model exercises linked below.",
    ],
    resources=[
        ("MDN — The Box Model","https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model"),
        ("The Odin Project — CSS Foundations exercises","https://github.com/TheOdinProject/css-exercises"),
        ("YouTube — The Box Model (Kevin Powell)","https://www.youtube.com/watch?v=rIO5326FgPE"),
        ("CSS Tricks — The CSS Box Model","https://css-tricks.com/the-css-box-model/"),
    ])

    # 26 ── Block and Inline ──────────────────────────────────
    write("block-and-inline","Block and Inline",
    intro="Every HTML element has a default display behaviour. Understanding block versus inline is foundational for understanding why layouts behave the way they do.",
    overview=[
        "Explain the difference between block and inline elements.",
        "Know which common HTML elements are block-level and which are inline.",
        "Use the display property to change an element's behaviour.",
        "Understand inline-block and when it is useful.",
    ],
    body="""
<h2 class="lesson-section-title" id="block">Block Elements</h2>
<p>Block elements start on a new line and take up the full available width. You can freely set width, height, padding, and margin on them.</p>
""" + code("""/* Common block elements */
div, p, h1, h2, h3, h4, h5, h6,
ul, ol, li, section, article,
header, footer, nav, main, form
""") + """
<h2 class="lesson-section-title" id="inline">Inline Elements</h2>
<p>Inline elements flow within text and only take up as much width as their content. Setting width, height, or vertical margins has no effect.</p>
""" + code("""/* Common inline elements */
span, a, strong, em, img,
input, button, label, code

<!-- Inline elements flow within the surrounding text -->
<p>
  Here is a paragraph with <strong>bold</strong> and
  <a href="#">a link</a> flowing naturally within the text.
</p>
""") + """
<h2 class="lesson-section-title" id="display">Changing Display</h2>
""" + code("""/* Override default display behaviour */

/* Make inline span behave like a block */
span { display: block; }

/* Make block div behave inline */
div { display: inline; }

/* Best of both worlds — inline position, block sizing */
.nav-item {
  display: inline-block;
  width: 120px;
  padding: 8px 16px;
  text-align: center;
}

/* Remove from page entirely */
.hidden { display: none; }

/* Modern layouts use flex and grid instead */
.container { display: flex; }
.grid      { display: grid; }
"""),
    kc=[
        ("What is the main visual difference between block and inline?","block"),
        ("Why does setting width have no effect on an inline element?","inline"),
        ("What does display inline-block give you that plain inline does not?","display"),
    ],
    assignments=[
        "In DevTools, inspect a p (block) and a span (inline). Notice the computed display values and how they affect layout.",
        "Work through The Odin Project's Block and Inline exercises linked below.",
    ],
    resources=[
        ("MDN — Block and Inline Layout in Normal Flow","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flow_layout/Block_and_inline_layout_in_normal_flow"),
        ("The Odin Project — CSS Foundations exercises","https://github.com/TheOdinProject/css-exercises"),
        ("YouTube — Block vs Inline vs Inline-Block (Web Dev Simplified)","https://www.youtube.com/watch?v=x_i2gga-sYg"),
    ])

    # 27 ── Introduction to Flexbox ───────────────────────────
    write("introduction-to-flexbox","Introduction to Flexbox",
    intro="Flexbox is a CSS layout system that solves alignment problems that were previously hacks. Centering vertically used to be notoriously hard. With Flexbox it takes one line.",
    overview=[
        "Activate Flexbox with display flex.",
        "Understand flex containers and flex items.",
        "Describe the main axis and cross axis.",
        "Apply justify-content and align-items for alignment.",
    ],
    body="""
<h2 class="lesson-section-title" id="container-items">Containers and Items</h2>
""" + code("""<!-- HTML: parent and children -->
<div class="container">
  <div class="item">One</div>
  <div class="item">Two</div>
  <div class="item">Three</div>
</div>
""") + code("""/* CSS: make the parent a flex container */
.container {
  display: flex;
  gap: 1rem;
}
/* All three .item divs are now flex items */
/* They line up in a row automatically */
""") + """
<h2 class="lesson-section-title" id="axes">Main Axis and Cross Axis</h2>
""" + code("""/* Default: main axis is horizontal (left → right) */
.container {
  display: flex;
  flex-direction: row; /* default */
}

/* Switch: main axis becomes vertical (top → bottom) */
.container {
  display: flex;
  flex-direction: column;
}
""") + """
<h2 class="lesson-section-title" id="alignment">Alignment Properties</h2>
""" + code("""/* justify-content — aligns along the MAIN axis */
/* align-items    — aligns along the CROSS axis */

/* Centre items both horizontally and vertically */
.centered-box {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
}

/* Space cards evenly with items at the top */
.card-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1.5rem;
}

/* Stack items vertically, centered */
.stack {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Play Flexbox Froggy (linked below) to build intuition for alignment through a game. It covers all alignment concepts from this and the next three lessons.</p>
</div>
""",
    kc=[
        ("What CSS property activates Flexbox on a container?","container-items"),
        ("What is the difference between the main axis and cross axis?","axes"),
        ("Which property aligns items along the main axis?","alignment"),
        ("Which property aligns items along the cross axis?","alignment"),
    ],
    assignments=[
        "Build a horizontal navigation bar with links spaced evenly using Flexbox.",
        "Create a card that is perfectly centered both horizontally and vertically using Flexbox.",
        "Play Flexbox Froggy and complete all 24 levels.",
    ],
    resources=[
        ("Flexbox Froggy — Learn Flexbox with a game","https://flexboxfroggy.com/"),
        ("CSS Tricks — A Complete Guide to Flexbox","https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),
        ("MDN — Flexbox","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox"),
        ("YouTube — Flexbox CSS in 20 Minutes (Traversy Media)","https://www.youtube.com/watch?v=JJSoEo8JSnc"),
    ])

    print("\nAll lessons written. Committing to GitHub...\n")
    os.chdir(BASE)
    subprocess.run(["git","add","-A"], check=True)
    subprocess.run(["git","commit","-m","Seed Foundations lessons 14-27 with full content and copy buttons"], check=True)
    subprocess.run(["git","push"], check=True)
    print("Pushed to GitHub.")

if __name__ == "__main__":
    seed()
