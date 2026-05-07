#!/usr/bin/env python3
import os

BASE    = "/home/solomon/devpath"
LESSONS = f"{BASE}/foundations/lessons"

LOGO_SVG = '<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="14" cy="14" r="13" stroke="currentColor" stroke-width="1.8"/><path d="M8 14 L14 7 L20 14 L14 21 Z" fill="currentColor"/></svg>'

def nav(root):
    return f"""<nav class="site-nav">
  <a href="{root}index.html" class="nav-logo">{LOGO_SVG} DevPath</a>
  <ul class="nav-links">
    <li><a href="{root}index.html">Home</a></li>
    <li><a href="{root}foundations/index.html">Foundations</a></li>
    <li><a href="{root}paths/full-stack-javascript/index.html">Full Stack JS</a></li>
    <li><a href="{root}paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a></li>
  </ul>
</nav>"""

def footer():
    return '<footer class="site-footer"><p>DevPath — inspired by <a href="https://www.theodinproject.com" target="_blank">The Odin Project</a>.</p></footer>'

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

SIDEBAR = """<aside class="sidebar">
  <div class="sidebar-course-title">Foundations</div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">Introduction</div>
    <a href="how-this-course-will-work.html" class="sidebar-link">How This Course Will Work</a>
    <a href="introduction-to-web-dev.html" class="sidebar-link">Introduction to Web Development</a>
    <a href="motivation-and-mindset.html" class="sidebar-link">Motivation and Mindset</a>
    <a href="asking-for-help.html" class="sidebar-link">Asking For Help</a>
    <a href="join-the-community.html" class="sidebar-link">Join the Odin Community</a>
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">Prerequisites</div>
    <a href="computer-basics.html" class="sidebar-link">Computer Basics</a>
    <a href="how-does-the-web-work.html" class="sidebar-link">How Does the Web Work?</a>
    <a href="installation-overview.html" class="sidebar-link">Installation Overview</a>
    <a href="installations.html" class="sidebar-link">Installations</a>
    <a href="text-editors.html" class="sidebar-link">Text Editors</a>
    <a href="command-line-basics.html" class="sidebar-link">Command Line Basics</a>
    <a href="setting-up-git.html" class="sidebar-link">Setting Up Git</a>
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">Git Basics</div>
    <a href="introduction-to-git.html" class="sidebar-link">Introduction to Git</a>
    <a href="git-basics.html" class="sidebar-link">Git Basics</a>
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">HTML Foundations</div>
    <a href="introduction-to-html-css.html" class="sidebar-link">Introduction to HTML and CSS</a>
    <a href="elements-and-tags.html" class="sidebar-link">Elements and Tags</a>
    <a href="html-boilerplate.html" class="sidebar-link">HTML Boilerplate</a>
    <a href="working-with-text.html" class="sidebar-link">Working with Text</a>
    <a href="lists.html" class="sidebar-link">Lists</a>
    <a href="links-and-images.html" class="sidebar-link">Links and Images</a>
    <a href="commit-messages.html" class="sidebar-link">Commit Messages</a>
    <a href="project-recipes.html" class="sidebar-link is-project">Project: Recipes</a>
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">CSS Foundations</div>
    <a href="intro-to-css.html" class="sidebar-link">Intro to CSS</a>
    <a href="the-cascade.html" class="sidebar-link">The Cascade</a>
    <a href="inspecting-html-and-css.html" class="sidebar-link">Inspecting HTML and CSS</a>
    <a href="the-box-model.html" class="sidebar-link">The Box Model</a>
    <a href="block-and-inline.html" class="sidebar-link">Block and Inline</a>
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">Flexbox</div>
    <a href="introduction-to-flexbox.html" class="sidebar-link">Introduction to Flexbox</a>
    <a href="growing-and-shrinking.html" class="sidebar-link">Growing and Shrinking</a>
    <a href="axes.html" class="sidebar-link">Axes</a>
    <a href="alignment.html" class="sidebar-link">Alignment</a>
    <a href="project-landing-page.html" class="sidebar-link is-project">Project: Landing Page</a>
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">JavaScript Basics</div>
    <a href="variables-and-operators.html" class="sidebar-link">Variables and Operators</a>
    <a href="data-types-and-conditionals.html" class="sidebar-link">Data Types and Conditionals</a>
    <a href="javascript-developer-tools.html" class="sidebar-link">JavaScript Developer Tools</a>
    <a href="function-basics.html" class="sidebar-link">Function Basics</a>
    <a href="problem-solving.html" class="sidebar-link">Problem Solving</a>
    <a href="understanding-errors.html" class="sidebar-link">Understanding Errors</a>
    <a href="project-rock-paper-scissors.html" class="sidebar-link is-project">Project: Rock Paper Scissors</a>
    <a href="clean-code.html" class="sidebar-link">Clean Code</a>
    <a href="installing-nodejs.html" class="sidebar-link">Installing Node.js</a>
    <a href="arrays-and-loops.html" class="sidebar-link">Arrays and Loops</a>
    <a href="dom-manipulation-and-events.html" class="sidebar-link">DOM Manipulation and Events</a>
    <a href="revisiting-rock-paper-scissors.html" class="sidebar-link">Revisiting Rock Paper Scissors</a>
    <a href="project-etch-a-sketch.html" class="sidebar-link is-project">Project: Etch-a-Sketch</a>
    <a href="object-basics.html" class="sidebar-link">Object Basics</a>
    <a href="project-calculator.html" class="sidebar-link is-project">Project: Calculator</a>
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">Conclusion</div>
    <a href="choose-your-path.html" class="sidebar-link">Choose Your Path Forward</a>
  </div>
</aside>"""

def prev_next(slug):
    idx = next((i for i, l in enumerate(ALL_LESSONS) if l[0] == slug), None)
    prev = (ALL_LESSONS[idx-1][1], f"{ALL_LESSONS[idx-1][0]}.html") if idx and idx > 0 else None
    nxt  = (ALL_LESSONS[idx+1][1], f"{ALL_LESSONS[idx+1][0]}.html") if idx is not None and idx < len(ALL_LESSONS)-1 else None
    return prev, nxt

def write_lesson(slug, title, intro, overview, sections_html, kc_items, assignments, resources):
    prev, nxt = prev_next(slug)
    bc = f'<nav class="breadcrumb"><a href="../../index.html">Home</a> <span class="breadcrumb-sep">/</span> <a href="../index.html">Foundations</a> <span class="breadcrumb-sep">/</span> <span class="breadcrumb-current">{title}</span></nav>'
    overview_li = "".join(f"<li>{i}</li>" for i in overview)
    kc_li       = "".join(f'<li><a href="#{k[1]}" data-target="{k[1]}">{k[0]}</a></li>' for k in kc_items)
    assign_li   = "".join(f"<li>{a}</li>" for a in assignments)
    res_li      = "".join(f'<li><a href="{r[1]}" target="_blank" rel="noopener">{r[0]}</a></li>' for r in resources)
    prev_html   = f'<a href="{prev[1]}" class="pagination-link prev"><span class="pagination-label">← Previous</span><span class="pagination-title">{prev[0]}</span></a>' if prev else "<span></span>"
    next_html   = f'<a href="{nxt[1]}" class="pagination-link next"><span class="pagination-label">Next →</span><span class="pagination-title">{nxt[0]}</span></a>' if nxt else "<span></span>"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | DevPath</title>
  <link rel="stylesheet" href="../../css/styles.css">
</head>
<body>
{nav("../../")}
<div class="page-header">
  <div class="page-header-inner">
    {bc}
    <h1>{title}</h1>
  </div>
</div>
<div class="lesson-layout">
  {SIDEBAR}
  <main>
    <div class="lesson-body">
      <div class="block-intro"><p>{intro}</p></div>
      <div class="block-overview">
        <div class="block-overview-label">Lesson Overview</div>
        <ul>{overview_li}</ul>
      </div>
      {sections_html}
      <div class="block-kc">
        <div class="block-kc-label">Knowledge Check</div>
        <p class="kc-note">Click any question to jump to the part of this lesson that answers it.</p>
        <ol>{kc_li}</ol>
      </div>
      <div class="block-assignments">
        <div class="block-assignments-label">Assignments</div>
        <ol>{assign_li}</ol>
      </div>
      <div class="block-resources">
        <div class="block-resources-label">Additional Resources</div>
        <ul>{res_li}</ul>
      </div>
    </div>
    <div class="lesson-pagination">{prev_html}{next_html}</div>
  </main>
</div>
{footer()}
<script src="../../js/main.js"></script>
</body>
</html>"""

    path = os.path.join(LESSONS, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  seeded: {slug}.html")


def seed():

    # ------------------------------------------------------------------
    # 15. COMMIT MESSAGES
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "commit-messages",
        title = "Commit Messages",
        intro = "A Git commit message is a short note explaining what a change does and why. Writing good commit messages is a professional habit that pays off the moment you work with other people — or return to your own code three months later.",
        overview = [
            "Explain why good commit messages matter.",
            "Follow the seven rules of a great commit message.",
            "Know when to commit and how often.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="why">Why Commit Messages Matter</h2>
<p>Your commit history is a log of every decision you made while building something. A well-maintained log lets you — and your teammates — understand <em>why</em> any line of code exists, not just what it does. When something breaks, good commit messages let you quickly identify the change that caused it.</p>
<p>Compare these two commit histories:</p>
<pre><code># Bad — tells you nothing
git log --oneline
a3f2c1b fix
9d8e7f6 stuff
3b2a1c0 changes
1f0e9d8 wip

# Good — tells the whole story
git log --oneline
a3f2c1b Fix nav links breaking on mobile viewports
9d8e7f6 Add form validation to the contact page
3b2a1c0 Refactor hero section to use Flexbox
1f0e9d8 Add initial HTML boilerplate and folder structure</code></pre>

<h2 class="lesson-section-title" id="rules">The Seven Rules</h2>
<p>The widely accepted standard for commit messages comes from Chris Beams' influential article. The seven rules are:</p>
<ol>
  <li><strong>Separate subject from body with a blank line.</strong></li>
  <li><strong>Limit the subject line to 50 characters.</strong></li>
  <li><strong>Capitalise the subject line.</strong></li>
  <li><strong>Do not end the subject line with a period.</strong></li>
  <li><strong>Use the imperative mood in the subject line</strong> — "Fix bug" not "Fixed bug" or "Fixes bug".</li>
  <li><strong>Wrap the body at 72 characters.</strong></li>
  <li><strong>Use the body to explain what and why, not how.</strong></li>
</ol>
<pre><code># A well-formed commit message
Add password strength indicator to signup form

Users were submitting weak passwords that caused account security
issues. This commit adds a real-time strength meter that scores
password complexity and shows visual feedback as the user types.

Resolves #47</code></pre>

<h2 class="lesson-section-title" id="when">When to Commit</h2>
<p>Commit early and often. Each commit should represent one logical unit of work — one feature, one bug fix, one refactor. Small focused commits are far easier to understand, review, and revert than large ones that mix many unrelated changes.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>A useful test: can you describe your commit in one short imperative sentence? If you find yourself writing "and" multiple times — "Fix login and update styles and add new page" — that should probably be three separate commits.</p>
</div>
""",
        kc_items = [
            ("What mood should commit message subject lines be written in?", "rules"),
            ("What should you explain in the commit body — the what, the why, or the how?", "rules"),
            ("What is a good rule of thumb for deciding when to make a commit?", "when"),
        ],
        assignments = [
            "Read Chris Beams' article 'How to Write a Git Commit Message' (linked below). It is the definitive reference on this topic.",
            "Go back through your previous projects and look at your commit messages. Rewrite three of them in your notes following the seven rules.",
        ],
        resources = [
            ("The Odin Project — Commit Messages", "https://www.theodinproject.com/lessons/foundations-commit-messages"),
            ("Chris Beams — How to Write a Git Commit Message", "https://cbea.ms/git-commit/"),
            ("YouTube — Write Better Git Commit Messages (Fireship)", "https://www.youtube.com/watch?v=Hlp-9cdImSM"),
        ],
    )

    # ------------------------------------------------------------------
    # 16. PROJECT: RECIPES
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "project-recipes",
        title = "Project: Recipes",
        intro = "It is time to put everything you have learned about HTML into practice. You are going to build a simple recipe website — multiple pages, linked together, using only the HTML elements covered so far.",
        overview = [
            "Build a multi-page HTML website from scratch.",
            "Use headings, paragraphs, lists, links, and images together.",
            "Connect pages to each other using relative links.",
            "Push the finished project to GitHub.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="brief">Project Brief</h2>
<p>You are going to build a recipe website. It will not look beautiful yet — that is what CSS is for in the next section. The goal right now is to practise structuring content with HTML and connecting multiple pages together.</p>
<p>Do not let the plain appearance discourage you. Professional developers build the structure first, then layer on the visual design. This is the right way to work.</p>

<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>An <code>index.html</code> homepage that:
    <ul>
      <li>Has a main heading with your site name.</li>
      <li>Contains a list of links to each individual recipe page.</li>
    </ul>
  </li>
  <li>At least three individual recipe pages, each containing:
    <ul>
      <li>A title (<code>h1</code>) and a short description paragraph.</li>
      <li>An image of the dish with descriptive alt text.</li>
      <li>An unordered list of ingredients.</li>
      <li>An ordered list of preparation steps.</li>
      <li>A link back to the homepage.</li>
    </ul>
  </li>
  <li>All pages linked to each other using relative links.</li>
  <li>The project tracked with Git, pushed to a GitHub repository.</li>
</ul>

<h2 class="lesson-section-title" id="structure">Suggested Folder Structure</h2>
<pre><code>odin-recipes/
├── index.html
└── recipes/
    ├── lasagne.html
    ├── pancakes.html
    └── chicken-soup.html</code></pre>

<h2 class="lesson-section-title" id="steps">Getting Started</h2>
<ol>
  <li>Create the project folder and initialise Git:
  <pre><code>mkdir ~/devpath-projects/odin-recipes
cd ~/devpath-projects/odin-recipes
git init</code></pre>
  </li>
  <li>Create <code>index.html</code> with the boilerplate, add your heading and list of recipe links.</li>
  <li>Create the <code>recipes/</code> subfolder and add each recipe file.</li>
  <li>Commit after completing each page:
  <pre><code>git add .
git commit -m "Add lasagne recipe page"</code></pre>
  </li>
  <li>Create a new GitHub repository and push when done.</li>
</ol>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Resist the urge to add CSS yet. The purpose of this project is HTML structure. Keeping CSS out of scope keeps you focused on the thing you are actually practising.</p>
</div>
""",
        kc_items = [
            ("What HTML elements are needed to build a basic recipe page?", "requirements"),
            ("What type of link connects your recipe pages back to the homepage?", "requirements"),
        ],
        assignments = [
            "Complete the Recipes project following all requirements above.",
            "Push your finished project to GitHub. Your repository URL is now something you can share — congratulations on your first published project.",
        ],
        resources = [
            ("The Odin Project — Recipes Project", "https://www.theodinproject.com/lessons/foundations-recipes"),
            ("MDN — HTML Element Reference", "https://developer.mozilla.org/en-US/docs/Web/HTML/Element"),
            ("YouTube — Build a Simple Website With HTML (Kevin Powell)", "https://www.youtube.com/watch?v=PlxWf493en4"),
        ],
    )

    # ------------------------------------------------------------------
    # 17. INTRO TO CSS
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "intro-to-css",
        title = "Intro to CSS",
        intro = "Your HTML pages look plain right now. CSS is what transforms them into visually polished websites. This lesson introduces how CSS works, how to write rules, and the different ways you can apply styles.",
        overview = [
            "Describe what CSS does and what it controls.",
            "Write a CSS rule with a selector, property, and value.",
            "Know the three ways to add CSS: inline, internal, and external.",
            "Understand why external stylesheets are the right approach for real projects.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="what-css-does">What CSS Does</h2>
<p>CSS stands for <strong>Cascading Style Sheets</strong>. While HTML defines the structure and meaning of your content, CSS defines how it <em>looks</em>: colours, fonts, spacing, layout, animations — everything visual.</p>
<p>CSS works by targeting HTML elements with <strong>selectors</strong> and applying <strong>declarations</strong> to them. A declaration is a property-value pair:</p>
<pre><code>p {
  color: #333333;
  font-size: 18px;
  line-height: 1.6;
}</code></pre>
<p>This says: "For every <code>&lt;p&gt;</code> element, set the text colour to dark grey, font size to 18px, and line height to 1.6 times the font size."</p>

<h2 class="lesson-section-title" id="anatomy">Anatomy of a CSS Rule</h2>
<pre><code>selector {
  property: value;
  property: value;
}</code></pre>
<ul>
  <li><strong>Selector</strong> — targets which HTML elements to style. Can be an element name, class, ID, or more complex patterns.</li>
  <li><strong>Declaration block</strong> — the curly braces and everything inside them.</li>
  <li><strong>Property</strong> — the aspect of the element you want to change (colour, size, spacing, etc.).</li>
  <li><strong>Value</strong> — the setting you want for that property.</li>
</ul>

<h2 class="lesson-section-title" id="selectors">Basic Selectors</h2>
<pre><code>/* Element selector — targets all h1 elements */
h1 {
  color: navy;
}

/* Class selector — targets any element with class="highlight" */
.highlight {
  background-color: yellow;
}

/* ID selector — targets the ONE element with id="hero" */
#hero {
  font-size: 3rem;
}

/* Descendant selector — targets p elements inside a .card */
.card p {
  font-size: 0.9rem;
}</code></pre>

<h2 class="lesson-section-title" id="three-ways">Three Ways to Add CSS</h2>
<p><strong>1. Inline styles</strong> — applied directly on a single element with the <code>style</code> attribute. Highest specificity. Avoid for anything beyond quick tests:</p>
<pre><code>&lt;p style="color: red; font-weight: bold;"&gt;Warning text.&lt;/p&gt;</code></pre>
<p><strong>2. Internal styles</strong> — a <code>&lt;style&gt;</code> block inside the <code>&lt;head&gt;</code>. Fine for single-page demos, impractical for real sites:</p>
<pre><code>&lt;head&gt;
  &lt;style&gt;
    p { color: navy; }
  &lt;/style&gt;
&lt;/head&gt;</code></pre>
<p><strong>3. External stylesheet</strong> — a separate <code>.css</code> file linked in the <code>&lt;head&gt;</code>. The correct approach for every real project:</p>
<pre><code>&lt;head&gt;
  &lt;link rel="stylesheet" href="styles.css"&gt;
&lt;/head&gt;</code></pre>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Always use external stylesheets. They keep your HTML clean, let you reuse the same styles across every page, and make maintenance far easier. One CSS change updates every page simultaneously.</p>
</div>
""",
        kc_items = [
            ("What are the three parts of a CSS rule?", "anatomy"),
            ("What is the difference between a class selector and an ID selector?", "selectors"),
            ("What are the three ways to add CSS and which is preferred?", "three-ways"),
        ],
        assignments = [
            "Create a <code>styles.css</code> file and link it to your Recipes project. Add at least 8 style rules — colours, font sizes, background colours, spacing.",
            "Experiment with all three selector types: element, class, and ID.",
            "Work through The Odin Project's CSS Foundations exercises linked below.",
        ],
        resources = [
            ("The Odin Project — Intro to CSS", "https://www.theodinproject.com/lessons/foundations-intro-to-css"),
            ("MDN — CSS First Steps", "https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps"),
            ("YouTube — CSS Tutorial — Zero to Hero (freeCodeCamp)", "https://www.youtube.com/watch?v=1Rs2ND1ryYc"),
            ("YouTube — CSS in 100 Seconds (Fireship)", "https://www.youtube.com/watch?v=OEV8gMkCHXQ"),
        ],
    )

    # ------------------------------------------------------------------
    # 18. THE CASCADE
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "the-cascade",
        title = "The Cascade",
        intro = "CSS stands for Cascading Style Sheets. That word — cascading — is the key. When multiple CSS rules could apply to the same element, the cascade is the algorithm that decides which one wins.",
        overview = [
            "Define specificity and explain how it resolves conflicts between CSS rules.",
            "Understand the roles of specificity, inheritance, and source order in the cascade.",
            "Calculate the specificity of a given selector.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="what-cascade">What Is the Cascade?</h2>
<p>The cascade is the set of rules CSS uses when two or more declarations compete to style the same element. It considers three factors in order of priority:</p>
<ol>
  <li><strong>Specificity</strong> — how precisely does the selector target the element?</li>
  <li><strong>Source order</strong> — when specificity is equal, the rule that appears <em>later</em> in the stylesheet wins.</li>
  <li><strong>Inheritance</strong> — some properties pass down from parent elements to their children automatically.</li>
</ol>

<h2 class="lesson-section-title" id="specificity">Specificity</h2>
<p>Specificity is calculated as a three-number score. From lowest to highest weight:</p>
<ul>
  <li><strong>Element selectors</strong> (<code>p</code>, <code>h1</code>, <code>div</code>) — score: 0,0,1</li>
  <li><strong>Class selectors</strong> (<code>.card</code>, <code>.nav-link</code>) — score: 0,1,0</li>
  <li><strong>ID selectors</strong> (<code>#hero</code>, <code>#main-nav</code>) — score: 1,0,0</li>
  <li><strong>Inline styles</strong> — score: 1,0,0,0 (always beats everything above)</li>
  <li><strong><code>!important</code></strong> — overrides everything. Use sparingly; it makes debugging very painful.</li>
</ul>
<pre><code>/* Specificity 0,0,1 — element */
p {
  color: black;
}

/* Specificity 0,1,0 — class — wins over element */
.intro {
  color: navy;
}

/* Specificity 1,0,0 — ID — wins over class */
#hero-text {
  color: gold;
}

/* Combined: 0,1,1 — class + element */
.intro p {
  font-size: 1.1rem;
}</code></pre>

<h2 class="lesson-section-title" id="inheritance">Inheritance</h2>
<p>Some CSS properties are <strong>inherited</strong> — child elements automatically receive them from their parent unless they override the value. Properties like <code>color</code>, <code>font-family</code>, <code>font-size</code>, and <code>line-height</code> are inherited.</p>
<p>Properties like <code>border</code>, <code>padding</code>, <code>margin</code>, <code>background</code>, and <code>width</code> are <strong>not</strong> inherited — each element must set them explicitly.</p>
<pre><code>/* Set on body, inherited by all text elements */
body {
  font-family: 'Segoe UI', sans-serif;
  color: #333;
  line-height: 1.7;
}

/* p elements inherit font-family, color, and line-height from body */
/* but they do NOT inherit border or padding */</code></pre>

<h2 class="lesson-section-title" id="source-order">Source Order</h2>
<p>When two rules have identical specificity, the one that appears later in the stylesheet wins:</p>
<pre><code>p { color: red; }
p { color: blue; }
/* Result: blue, because it comes later */</code></pre>
""",
        kc_items = [
            ("What three factors does the cascade consider when resolving conflicts?", "what-cascade"),
            ("Which has higher specificity: a class selector or an ID selector?", "specificity"),
            ("Is the CSS <code>color</code> property inherited by child elements?", "inheritance"),
            ("When two rules have the same specificity, which one wins?", "source-order"),
        ],
        assignments = [
            "Open DevTools on any website, select an element, and look at the 'Computed' tab. Notice which styles are crossed out (overridden) and which are active. Trace the specificity.",
            "Work through The Odin Project's Cascade exercises.",
        ],
        resources = [
            ("The Odin Project — The Cascade", "https://www.theodinproject.com/lessons/foundations-the-cascade"),
            ("MDN — Cascade and Inheritance", "https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance"),
            ("CSS Specificity Calculator (Keegan Street)", "https://specificity.keegan.st/"),
            ("YouTube — CSS Specificity Explained (Kevin Powell)", "https://www.youtube.com/watch?v=c0kfcP_nD9E"),
        ],
    )

    # ------------------------------------------------------------------
    # 19. INSPECTING HTML AND CSS
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "inspecting-html-and-css",
        title = "Inspecting HTML and CSS",
        intro = "Browser developer tools are your most powerful debugging tool as a front-end developer. This lesson shows you how to use them to inspect elements, test CSS changes live, and understand exactly what is happening on any page.",
        overview = [
            "Open and navigate the browser DevTools.",
            "Inspect any element on a page to see its HTML and applied styles.",
            "Edit CSS live in the browser to test changes.",
            "Use the box model diagram in DevTools.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="opening">Opening DevTools</h2>
<p>Every major browser has built-in developer tools. You can open them in multiple ways:</p>
<ul>
  <li><strong>Keyboard shortcut:</strong> <code>F12</code> (Windows/Linux) or <code>Cmd+Option+I</code> (Mac)</li>
  <li><strong>Right-click:</strong> Right-click any element on a page and choose <strong>Inspect</strong>.</li>
  <li><strong>Menu:</strong> Browser menu → More Tools → Developer Tools.</li>
</ul>
<p>Chrome DevTools is the industry standard and is what this lesson focuses on. Firefox DevTools are equally capable and slightly more friendly to CSS developers.</p>

<h2 class="lesson-section-title" id="elements-panel">The Elements Panel</h2>
<p>The <strong>Elements</strong> panel (called <strong>Inspector</strong> in Firefox) shows you the live DOM — the HTML structure the browser has built from your code. It is not necessarily identical to your source file, because JavaScript can modify the DOM dynamically.</p>
<p>In the Elements panel you can:</p>
<ul>
  <li>Click any element to select it and see its HTML.</li>
  <li>See the <strong>Styles</strong> pane on the right showing every CSS rule applied to the selected element, with their source files and line numbers.</li>
  <li>See strikethrough rules that have been overridden by higher-specificity declarations.</li>
</ul>

<h2 class="lesson-section-title" id="live-editing">Live CSS Editing</h2>
<p>You can edit CSS directly in DevTools and see changes instantly — without touching your actual files. This is invaluable for experimenting:</p>
<ol>
  <li>Select an element in the Elements panel.</li>
  <li>In the Styles pane, click on any property value and change it.</li>
  <li>Press Tab to move to the next property.</li>
  <li>Click on an empty space in a rule to add a new property.</li>
</ol>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Changes made in DevTools are temporary — they disappear on page refresh. When you find something that works, copy it back into your actual CSS file.</p>
</div>

<h2 class="lesson-section-title" id="box-model">The Box Model Diagram</h2>
<p>At the bottom of the Styles pane (or in the Computed tab) you will find a visual diagram of the selected element's box model — showing its content size, padding, border, and margin as nested rectangles. Hovering over each section highlights it on the page.</p>
<p>This is the fastest way to debug spacing problems: "why is there all this space here?" — open DevTools, select the element, and the box model diagram shows you exactly where the space is coming from.</p>
""",
        kc_items = [
            ("What keyboard shortcut opens DevTools?", "opening"),
            ("What does a strikethrough on a CSS rule in the Styles pane mean?", "elements-panel"),
            ("How do you test a CSS change without touching your files?", "live-editing"),
            ("Where in DevTools can you see a visual diagram of padding, border, and margin?", "box-model"),
        ],
        assignments = [
            "Open DevTools on your Recipes project. Inspect your <code>h1</code> element and see every CSS rule applied to it.",
            "Use live editing to change the background colour and font size of an element. When you find values you like, copy them into your stylesheet.",
            "Watch The Odin Project's DevTools video linked below.",
        ],
        resources = [
            ("The Odin Project — Inspecting HTML and CSS", "https://www.theodinproject.com/lessons/foundations-inspecting-html-and-css"),
            ("Chrome DevTools — Get Started with Viewing and Changing CSS", "https://developer.chrome.com/docs/devtools/css/"),
            ("YouTube — Chrome DevTools Full Tutorial (Traversy Media)", "https://www.youtube.com/watch?v=x4q86IjJFag"),
        ],
    )

    # ------------------------------------------------------------------
    # 20. THE BOX MODEL
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "the-box-model",
        title = "The Box Model",
        intro = "Every single HTML element — every paragraph, heading, image, div — is a rectangular box. Understanding how these boxes are sized and spaced is the foundation of all CSS layout.",
        overview = [
            "Name and describe the four areas of the CSS box model.",
            "Understand the difference between <code>content-box</code> and <code>border-box</code> sizing.",
            "Use margin and padding to control spacing.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="four-areas">The Four Areas</h2>
<p>Every element's box has four nested areas, from innermost to outermost:</p>
<ul>
  <li><strong>Content</strong> — the actual text or image inside the element. Its size is controlled by <code>width</code> and <code>height</code>.</li>
  <li><strong>Padding</strong> — transparent space between the content and the border. Backgrounds extend into the padding area.</li>
  <li><strong>Border</strong> — a line around the padding. Can be visible or set to none.</li>
  <li><strong>Margin</strong> — transparent space outside the border. Separates this element from its neighbours. Backgrounds do NOT extend into margin.</li>
</ul>
<pre><code>.card {
  width: 300px;
  padding: 20px;           /* space inside, around the content */
  border: 2px solid #ccc;  /* visible line around the padding */
  margin: 30px;            /* space outside, between this and other elements */
}</code></pre>

<h2 class="lesson-section-title" id="box-sizing">The box-sizing Problem</h2>
<p>By default, CSS uses <code>box-sizing: content-box</code>. This means the <code>width</code> property only sets the width of the <em>content area</em>. Padding and border are added on top, making the actual rendered element wider than you specified.</p>
<pre><code>/* content-box (default): actual width = 300 + 20 + 20 + 2 + 2 = 344px */
.box {
  box-sizing: content-box; /* default */
  width: 300px;
  padding: 20px;
  border: 2px solid black;
}

/* border-box: actual width stays at exactly 300px */
.box {
  box-sizing: border-box;
  width: 300px;
  padding: 20px;  /* padding is subtracted from the 300px */
  border: 2px solid black;
}</code></pre>
<p><code>border-box</code> is almost always what you want. Add this rule to the top of every stylesheet you write:</p>
<pre><code>*,
*::before,
*::after {
  box-sizing: border-box;
}</code></pre>

<h2 class="lesson-section-title" id="margin-padding">Margin vs. Padding</h2>
<p>A common source of confusion. The rule of thumb:</p>
<ul>
  <li>Use <strong>padding</strong> for space <em>inside</em> an element — between its content and its edge. Background colour fills this space.</li>
  <li>Use <strong>margin</strong> for space <em>outside</em> an element — between it and other elements. Always transparent.</li>
</ul>
<pre><code>/* Shorthand: top right bottom left (clockwise) */
padding: 10px 20px 10px 20px;

/* Shorthand: vertical horizontal */
padding: 10px 20px;

/* Shorthand: all four sides */
padding: 16px;

/* Individual sides */
margin-top: 24px;
margin-bottom: 8px;</code></pre>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Vertical margins between adjacent block elements <em>collapse</em> — only the larger margin applies, not the sum of both. This catches a lot of beginners off guard. DevTools is your friend for investigating collapsed margins.</p>
</div>
""",
        kc_items = [
            ("Name the four areas of the box model from inside to outside.", "four-areas"),
            ("What does <code>box-sizing: border-box</code> change?", "box-sizing"),
            ("What is the difference between margin and padding?", "margin-padding"),
            ("What is margin collapse?", "margin-padding"),
        ],
        assignments = [
            "Add <code>box-sizing: border-box</code> to your project stylesheet. Build a simple card component with explicit padding, border, and margin, and verify the dimensions using DevTools.",
            "Work through The Odin Project's Box Model exercises.",
        ],
        resources = [
            ("The Odin Project — The Box Model", "https://www.theodinproject.com/lessons/foundations-the-box-model"),
            ("MDN — The Box Model", "https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model"),
            ("YouTube — The Box Model (Kevin Powell)", "https://www.youtube.com/watch?v=rIO5326FgPE"),
            ("CSS Tricks — The CSS Box Model", "https://css-tricks.com/the-css-box-model/"),
        ],
    )

    # ------------------------------------------------------------------
    # 21. BLOCK AND INLINE
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "block-and-inline",
        title = "Block and Inline",
        intro = "Every HTML element has a default display behaviour. Understanding the difference between block and inline elements explains why some elements stack vertically and others flow side by side in text.",
        overview = [
            "Explain the difference between block and inline display.",
            "Know which common HTML elements are block-level and which are inline.",
            "Use the <code>display</code> property to change an element's behaviour.",
            "Understand <code>inline-block</code> and when it is useful.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="block">Block Elements</h2>
<p>A <strong>block-level element</strong> always starts on a new line and takes up the full width available — pushing everything above and below it onto their own lines. You can set <code>width</code>, <code>height</code>, <code>margin</code>, and <code>padding</code> on block elements freely.</p>
<p>Common block elements: <code>&lt;div&gt;</code>, <code>&lt;p&gt;</code>, <code>&lt;h1&gt;</code>–<code>&lt;h6&gt;</code>, <code>&lt;ul&gt;</code>, <code>&lt;ol&gt;</code>, <code>&lt;li&gt;</code>, <code>&lt;section&gt;</code>, <code>&lt;article&gt;</code>, <code>&lt;header&gt;</code>, <code>&lt;footer&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;main&gt;</code>.</p>

<h2 class="lesson-section-title" id="inline">Inline Elements</h2>
<p>An <strong>inline element</strong> flows within the surrounding text and only takes up as much width as its content requires. It does not start on a new line. Setting <code>width</code> and <code>height</code> has no effect on inline elements. Top and bottom margins also have no effect.</p>
<p>Common inline elements: <code>&lt;span&gt;</code>, <code>&lt;a&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;em&gt;</code>, <code>&lt;img&gt;</code>, <code>&lt;input&gt;</code>, <code>&lt;button&gt;</code>, <code>&lt;label&gt;</code>.</p>
<pre><code>&lt;p&gt;
  This is a paragraph with &lt;strong&gt;bold text&lt;/strong&gt; and a
  &lt;a href="#"&gt;link&lt;/a&gt; flowing inline within the sentence.
&lt;/p&gt;</code></pre>

<h2 class="lesson-section-title" id="display">Changing Display with CSS</h2>
<p>The <code>display</code> property lets you override an element's default behaviour:</p>
<pre><code>/* Make a normally-inline span behave like a block */
span {
  display: block;
}

/* Make a normally-block div behave like inline */
div {
  display: inline;
}

/* The best of both worlds */
.nav-item {
  display: inline-block;
  width: 100px;
  padding: 8px 16px;
}

/* Remove an element from the page entirely */
.hidden {
  display: none;
}</code></pre>

<h2 class="lesson-section-title" id="inline-block">Inline-Block</h2>
<p><code>inline-block</code> sits inline with other elements (does not force a new line) but respects <code>width</code>, <code>height</code>, and vertical <code>margin</code> like a block element. It was commonly used for navigation menus before Flexbox made that unnecessary — but you will still encounter it.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>In modern CSS, Flexbox and Grid have largely replaced the need to manually fiddle with block, inline, and inline-block for layout purposes. But understanding these concepts is essential for knowing <em>why</em> Flexbox behaves the way it does.</p>
</div>
""",
        kc_items = [
            ("What is the main visual difference between block and inline elements?", "block"),
            ("Why does setting <code>width</code> have no effect on an inline element?", "inline"),
            ("What does <code>display: inline-block</code> give you that plain <code>inline</code> does not?", "inline-block"),
        ],
        assignments = [
            "In your project, use DevTools to inspect a <code>&lt;p&gt;</code> (block) and a <code>&lt;span&gt;</code> (inline). Notice the difference in their computed display values.",
            "Create a small demo: a <code>&lt;div&gt;</code> with <code>display: inline-block</code> and a set width and height. Confirm it respects those dimensions unlike a plain inline element.",
        ],
        resources = [
            ("The Odin Project — Block and Inline", "https://www.theodinproject.com/lessons/foundations-block-and-inline"),
            ("MDN — Block and Inline Layout in Normal Flow", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flow_layout/Block_and_inline_layout_in_normal_flow"),
            ("YouTube — Block vs Inline vs Inline-Block (Web Dev Simplified)", "https://www.youtube.com/watch?v=x_i2gga-sYg"),
        ],
    )

    # ------------------------------------------------------------------
    # 22. INTRODUCTION TO FLEXBOX
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "introduction-to-flexbox",
        title = "Introduction to Flexbox",
        intro = "Flexbox is a CSS layout system that makes it dramatically easier to align and distribute elements. Before it existed, centering things vertically required elaborate hacks. Now it takes one line. This lesson introduces the core concepts.",
        overview = [
            "Activate Flexbox on a container with <code>display: flex</code>.",
            "Understand flex containers and flex items.",
            "Describe the main axis and cross axis.",
            "Apply basic alignment with <code>justify-content</code> and <code>align-items</code>.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="what-flexbox">What Is Flexbox?</h2>
<p>The Flexible Box Layout Module (Flexbox) is a one-dimensional layout system — it handles elements in either a row or a column at a time. It was designed to solve the layout problems that <code>float</code> and <code>inline-block</code> hacks could not solve cleanly.</p>
<p>Flexbox makes these previously difficult tasks trivial:</p>
<ul>
  <li>Vertically centring an element inside its parent.</li>
  <li>Distributing equal space between items.</li>
  <li>Making items grow to fill available space.</li>
  <li>Reordering items without changing the HTML.</li>
</ul>

<h2 class="lesson-section-title" id="container-items">Containers and Items</h2>
<p>Flexbox works on a parent-child relationship. Apply <code>display: flex</code> to the <strong>parent</strong> and it becomes a <strong>flex container</strong>. Every direct child immediately becomes a <strong>flex item</strong> and starts obeying flex rules.</p>
<pre><code>&lt;div class="container"&gt;
  &lt;div class="item"&gt;One&lt;/div&gt;
  &lt;div class="item"&gt;Two&lt;/div&gt;
  &lt;div class="item"&gt;Three&lt;/div&gt;
&lt;/div&gt;</code></pre>
<pre><code>.container {
  display: flex;
  gap: 1rem;   /* space between flex items */
}
/* The three .item divs are now flex items — they line up in a row */</code></pre>
<p>That is it. Just adding <code>display: flex</code> to the parent makes all its children line up in a row.</p>

<h2 class="lesson-section-title" id="axes">Main Axis and Cross Axis</h2>
<p>Flexbox works along two perpendicular axes:</p>
<ul>
  <li>The <strong>main axis</strong> is the direction flex items flow. By default it is horizontal (left to right). Changed with <code>flex-direction</code>.</li>
  <li>The <strong>cross axis</strong> is perpendicular to the main axis. If the main axis is horizontal, the cross axis is vertical.</li>
</ul>
<pre><code>/* Default: items flow left to right (main axis = horizontal) */
.container { flex-direction: row; }

/* Items flow top to bottom (main axis = vertical) */
.container { flex-direction: column; }</code></pre>

<h2 class="lesson-section-title" id="alignment">Basic Alignment</h2>
<pre><code>.container {
  display: flex;
  justify-content: center;       /* align along the MAIN axis */
  align-items: center;           /* align along the CROSS axis */
  gap: 1rem;
  height: 300px;
}
/* Result: items are perfectly centred both horizontally and vertically */</code></pre>
<p>Common values for <code>justify-content</code>:</p>
<ul>
  <li><code>flex-start</code> — pack items to the start (default)</li>
  <li><code>flex-end</code> — pack items to the end</li>
  <li><code>center</code> — centre items</li>
  <li><code>space-between</code> — equal gaps between items, none at edges</li>
  <li><code>space-around</code> — equal gaps around each item</li>
  <li><code>space-evenly</code> — equal gaps between items and edges</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Play Flexbox Froggy (linked below) to build intuition for these alignment properties through a fun game. It covers everything in this lesson and the next three.</p>
</div>
""",
        kc_items = [
            ("What CSS property turns an element into a flex container?", "container-items"),
            ("What is the difference between the main axis and cross axis?", "axes"),
            ("Which property aligns flex items along the main axis?", "alignment"),
            ("Which property aligns flex items along the cross axis?", "alignment"),
        ],
        assignments = [
            "Build a horizontal navigation bar using Flexbox with links evenly spaced.",
            "Centre a single div both horizontally and vertically inside a full-height container using Flexbox.",
            "Play Flexbox Froggy (linked below) — complete all 24 levels.",
        ],
        resources = [
            ("The Odin Project — Introduction to Flexbox", "https://www.theodinproject.com/lessons/foundations-introduction-to-flexbox"),
            ("CSS Tricks — A Complete Guide to Flexbox", "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),
            ("Flexbox Froggy — Learn Flexbox with a game", "https://flexboxfroggy.com/"),
            ("YouTube — Flexbox CSS In 20 Minutes (Traversy Media)", "https://www.youtube.com/watch?v=JJSoEo8JSnc"),
        ],
    )

    # ------------------------------------------------------------------
    # 23. GROWING AND SHRINKING
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "growing-and-shrinking",
        title = "Growing and Shrinking",
        intro = "The real power of Flexbox comes from its ability to make items grow to fill available space or shrink to fit. This lesson digs into the flex property and how it controls item sizing.",
        overview = [
            "Understand the <code>flex</code> shorthand property.",
            "Explain what <code>flex-grow</code>, <code>flex-shrink</code>, and <code>flex-basis</code> each control.",
            "Know the most common <code>flex</code> values and what they produce.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="flex-shorthand">The flex Shorthand</h2>
<p>The <code>flex</code> property is a shorthand for three separate properties: <code>flex-grow</code>, <code>flex-shrink</code>, and <code>flex-basis</code>. It is set on flex <em>items</em> (the children), not on the container.</p>
<pre><code>.item {
  flex: 1;          /* shorthand for flex: 1 1 0 */
  flex: 2;          /* grows twice as fast as flex: 1 items */
  flex: 0 0 200px;  /* does not grow, does not shrink, always 200px */
  flex: 1 1 auto;   /* grows and shrinks, starts from natural size */
}</code></pre>

<h2 class="lesson-section-title" id="flex-grow">flex-grow</h2>
<p><code>flex-grow</code> controls how much an item expands to fill available space. The value is a unitless ratio.</p>
<pre><code>.container { display: flex; }

.item-a { flex-grow: 1; }   /* gets 1 share of free space */
.item-b { flex-grow: 2; }   /* gets 2 shares — twice as much as item-a */
.item-c { flex-grow: 1; }   /* gets 1 share */
/* Total: 4 shares. item-b gets 50%, item-a and item-c each get 25% */</code></pre>
<p>Setting <code>flex-grow: 0</code> (the default) means the item will not grow beyond its natural size.</p>

<h2 class="lesson-section-title" id="flex-shrink">flex-shrink</h2>
<p><code>flex-shrink</code> controls how much an item shrinks when the container is too small. A value of <code>1</code> (the default) means all items shrink proportionally. A value of <code>0</code> means the item refuses to shrink.</p>
<pre><code>.sidebar {
  flex-shrink: 0;    /* sidebar keeps its width even when space is tight */
  width: 250px;
}
.main-content {
  flex-grow: 1;      /* takes all remaining space */
  flex-shrink: 1;    /* will shrink if needed */
}</code></pre>

<h2 class="lesson-section-title" id="flex-basis">flex-basis</h2>
<p><code>flex-basis</code> sets the initial size of a flex item before the remaining space is distributed. It works like <code>width</code> for row-direction flex, or <code>height</code> for column-direction.</p>
<pre><code>/* All items start at 200px, then grow/shrink from there */
.item {
  flex: 1 1 200px;
}

/* The most common pattern — equal-width columns */
.item {
  flex: 1;   /* equivalent to flex: 1 1 0 — start from zero and grow equally */
}</code></pre>
""",
        kc_items = [
            ("What three properties does the <code>flex</code> shorthand combine?", "flex-shorthand"),
            ("What does a <code>flex-grow</code> value of 2 mean compared to a value of 1?", "flex-grow"),
            ("What does <code>flex-shrink: 0</code> do?", "flex-shrink"),
            ("What is <code>flex-basis</code> and what is the difference between <code>flex-basis: auto</code> and <code>flex-basis: 0</code>?", "flex-basis"),
        ],
        assignments = [
            "Build a two-column layout: a fixed-width sidebar (<code>flex-shrink: 0</code>) and a main content area that fills the remaining space (<code>flex-grow: 1</code>).",
            "Experiment with three items given <code>flex-grow</code> values of 1, 2, and 3. Verify they take up proportional shares of the container.",
        ],
        resources = [
            ("The Odin Project — Growing and Shrinking", "https://www.theodinproject.com/lessons/foundations-growing-and-shrinking"),
            ("MDN — Controlling Ratios of Flex Items Along the Main Axis", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Controlling_ratios_of_flex_items_along_the_main_axis"),
            ("YouTube — Flexbox Growing and Shrinking (Kevin Powell)", "https://www.youtube.com/watch?v=sanRCfIcNaQ"),
        ],
    )

    # ------------------------------------------------------------------
    # 24. AXES
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "axes",
        title = "Axes",
        intro = "Everything in Flexbox revolves around the main axis and cross axis. This lesson takes a deeper look at how changing the flex direction flips these axes and completely changes how alignment properties behave.",
        overview = [
            "Use <code>flex-direction</code> to change the main axis.",
            "Understand how switching axes changes the behaviour of <code>justify-content</code> and <code>align-items</code>.",
            "Use <code>flex-wrap</code> to handle items that overflow.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="flex-direction">flex-direction</h2>
<p><code>flex-direction</code> sets which axis flex items flow along — the main axis. The four values:</p>
<pre><code>.container {
  display: flex;
  flex-direction: row;           /* default: left to right */
  flex-direction: row-reverse;   /* right to left */
  flex-direction: column;        /* top to bottom */
  flex-direction: column-reverse;/* bottom to top */
}</code></pre>
<p>When you switch to <code>column</code>, the main axis is now vertical. This means <code>justify-content</code> controls vertical alignment and <code>align-items</code> controls horizontal alignment — the opposite of row direction.</p>

<h2 class="lesson-section-title" id="axis-alignment">Alignment and the Active Axis</h2>
<pre><code>/* ROW direction (default) */
.row-container {
  display: flex;
  flex-direction: row;
  justify-content: center;  /* horizontal — along the main axis */
  align-items: center;       /* vertical — along the cross axis */
}

/* COLUMN direction */
.col-container {
  display: flex;
  flex-direction: column;
  justify-content: center;  /* vertical — main axis is now vertical */
  align-items: center;       /* horizontal — cross axis is now horizontal */
}</code></pre>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>The key insight: <code>justify-content</code> always aligns along the <em>main axis</em> and <code>align-items</code> always aligns along the <em>cross axis</em>. The axis directions change when you change <code>flex-direction</code>.</p>
</div>

<h2 class="lesson-section-title" id="flex-wrap">flex-wrap</h2>
<p>By default, flex items will squeeze into a single line even if they overflow the container. <code>flex-wrap</code> lets them wrap onto multiple lines:</p>
<pre><code>.container {
  display: flex;
  flex-wrap: wrap;        /* items wrap to the next line when needed */
  flex-wrap: nowrap;      /* default: single line, items may overflow */
  flex-wrap: wrap-reverse;/* wraps upward instead of downward */
  gap: 1rem;              /* gap applies between both rows and columns */
}</code></pre>
<p>A common responsive pattern: a set of cards that are <code>flex: 1 1 280px</code> inside a <code>flex-wrap: wrap</code> container. On wide screens they form multiple columns. On narrow screens they stack. Zero media queries needed.</p>
<pre><code>.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}
.card {
  flex: 1 1 280px;  /* grow and shrink, but never narrower than 280px */
}</code></pre>
""",
        kc_items = [
            ("When <code>flex-direction</code> is <code>column</code>, which axis does <code>justify-content</code> control?", "axis-alignment"),
            ("What does <code>flex-wrap: wrap</code> do?", "flex-wrap"),
            ("What is a simple responsive card layout pattern using Flexbox?", "flex-wrap"),
        ],
        assignments = [
            "Build a layout that works in both row and column direction by toggling <code>flex-direction</code>. Observe how the alignment properties behave differently.",
            "Build a responsive card grid using <code>flex-wrap: wrap</code> and <code>flex: 1 1 250px</code>. Resize your browser and watch it adapt.",
        ],
        resources = [
            ("The Odin Project — Axes", "https://www.theodinproject.com/lessons/foundations-axes"),
            ("MDN — Flexbox Direction", "https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction"),
            ("YouTube — Flexbox Axes Explained (Web Dev Simplified)", "https://www.youtube.com/watch?v=3YW65K6LcIA"),
        ],
    )

    # ------------------------------------------------------------------
    # 25. ALIGNMENT
    # ------------------------------------------------------------------
    write_lesson(
        slug  = "alignment",
        title = "Alignment",
        intro = "This lesson covers the complete set of Flexbox alignment tools. By the end you will be able to position elements exactly where you want them with confidence.",
        overview = [
            "Use <code>justify-content</code>, <code>align-items</code>, and <code>align-self</code> precisely.",
            "Use <code>align-content</code> to control multi-line flex containers.",
            "Use the <code>gap</code> property for clean spacing between items.",
        ],
        sections_html = """
<h2 class="lesson-section-title" id="justify-content">justify-content</h2>
<p>Aligns all flex items along the <strong>main axis</strong> as a group:</p>
<pre><code>.container {
  display: flex;
  justify-content: flex-start;    /* packed to start (default) */
  justify-content: flex-end;      /* packed to end */
  justify-content: center;        /* centred */
  justify-content: space-between; /* equal gaps between, none at edges */
  justify-content: space-around;  /* equal gaps around each item */
  justify-content: space-evenly;  /* equal gaps everywhere */
}</code></pre>

<h2 class="lesson-section-title" id="align-items">align-items</h2>
<p>Aligns all flex items along the <strong>cross axis</strong>:</p>
<pre><code>.container {
  display: flex;
  align-items: stretch;      /* items stretch to fill cross axis (default) */
  align-items: flex-start;   /* items align to the start of cross axis */
  align-items: flex-end;     /* items align to the end */
  align-items: center;       /* items centred on cross axis */
  align-items: baseline;     /* items aligned by their text baseline */
}</code></pre>

<h2 class="lesson-section-title" id="align-self">align-self</h2>
<p><code>align-self</code> is set on an individual flex <em>item</em> to override the container's <code>align-items</code> value for that one item:</p>
<pre><code>.container {
  display: flex;
  align-items: flex-start;  /* most items align to the top */
}
.special-item {
  align-self: center;        /* this one item is vertically centred */
}</code></pre>

<h2 class="lesson-section-title" id="align-content">align-content</h2>
<p><code>align-content</code> only applies to multi-line flex containers (<code>flex-wrap: wrap</code>). It controls how the <em>rows themselves</em> are aligned along the cross axis:</p>
<pre><code>.container {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;    /* rows packed to top */
  align-content: center;        /* rows centred vertically */
  align-content: space-between; /* equal vertical gaps between rows */
}</code></pre>

<h2 class="lesson-section-title" id="gap">gap</h2>
<p>The <code>gap</code> property sets consistent spacing between flex items. Much cleaner than using margin on individual items:</p>
<pre><code>.container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;           /* same gap in both directions */
  gap: 1rem 2rem;      /* row-gap column-gap */
  row-gap: 1rem;
  column-gap: 2rem;
}</code></pre>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Using <code>gap</code> instead of margins on items avoids the problem of unwanted space on the outer edges of your layout. It only adds space <em>between</em> items, not around them.</p>
</div>
""",
        kc_items = [
            ("What is the difference between <code>align-items</code> and <code>align-self</code>?", "align-self"),
            ("When does <code>align-content</code> have any effect?", "align-content"),
            ("Why is <code>gap</code> preferable to using margins on flex items?", "gap"),
        ],
        assignments = [
            "Build a complete page header with a logo on the left and navigation links on the right, using only Flexbox alignment.",
            "Build a footer with three columns: left text, centred text, and right text — using Flexbox.",
            "Complete all remaining Flexbox Froggy levels if you have not done so already.",
        ],
        resources = [
            ("The Odin Project — Alignment", "https://www.theodinproject.com/lessons/foundations-alignment"),
            ("CSS Tricks — A Complete Guide to Flexbox", "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),
            ("MDN — Aligning Items in a Flex Container", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Aligning_items_in_a_flex_container"),
            ("YouTube — Flexbox Alignment Deep Dive (Kevin Powell)", "https://www.youtube.com/watch?v=u044iM9xsWU"),
        ],
    )

    print("\nDone — seeded lessons 15 through 25.")

if __name__ == "__main__":
    seed()
