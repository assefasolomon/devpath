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
    return """<nav class="site-nav">
  <a href="../../index.html" class="nav-logo">""" + LOGO + """ DevPath</a>
  <ul class="nav-links">
    <li><a href="../../index.html">Home</a></li>
    <li><a href="../index.html">Foundations</a></li>
    <li><a href="../../paths/full-stack-javascript/index.html">Full Stack JS</a></li>
    <li><a href="../../paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a></li>
  </ul>
</nav>"""

def footer():
    return '<footer class="site-footer"><p>DevPath — A free, open, project-based web development curriculum.</p></footer>'

def sidebar(active_slug):
    def link(slug, title, is_project=False):
        cls = "sidebar-link"
        if is_project: cls += " is-project"
        if slug == active_slug: cls += " active"
        return f'<a href="{slug}.html" class="{cls}">{title}</a>'

    return """<aside class="sidebar">
  <div class="sidebar-course-title">Foundations</div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">Introduction</div>
    """ + link("how-this-course-will-work","How This Course Will Work") + """
    """ + link("introduction-to-web-dev","Introduction to Web Development") + """
    """ + link("motivation-and-mindset","Motivation and Mindset") + """
    """ + link("asking-for-help","Asking For Help") + """
    """ + link("join-the-community","Join the Community") + """
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">Prerequisites</div>
    """ + link("computer-basics","Computer Basics") + """
    """ + link("how-does-the-web-work","How Does the Web Work?") + """
    """ + link("installation-overview","Installation Overview") + """
    """ + link("installations","Installations") + """
    """ + link("text-editors","Text Editors") + """
    """ + link("command-line-basics","Command Line Basics") + """
    """ + link("setting-up-git","Setting Up Git") + """
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">Git Basics</div>
    """ + link("introduction-to-git","Introduction to Git") + """
    """ + link("git-basics","Git Basics") + """
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">HTML Foundations</div>
    """ + link("introduction-to-html-css","Introduction to HTML and CSS") + """
    """ + link("elements-and-tags","Elements and Tags") + """
    """ + link("html-boilerplate","HTML Boilerplate") + """
    """ + link("working-with-text","Working with Text") + """
    """ + link("lists","Lists") + """
    """ + link("links-and-images","Links and Images") + """
    """ + link("commit-messages","Commit Messages") + """
    """ + link("project-recipes","Project: Recipes",True) + """
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">CSS Foundations</div>
    """ + link("intro-to-css","Intro to CSS") + """
    """ + link("the-cascade","The Cascade") + """
    """ + link("inspecting-html-and-css","Inspecting HTML and CSS") + """
    """ + link("the-box-model","The Box Model") + """
    """ + link("block-and-inline","Block and Inline") + """
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">Flexbox</div>
    """ + link("introduction-to-flexbox","Introduction to Flexbox") + """
    """ + link("growing-and-shrinking","Growing and Shrinking") + """
    """ + link("axes","Axes") + """
    """ + link("alignment","Alignment") + """
    """ + link("project-landing-page","Project: Landing Page",True) + """
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">JavaScript Basics</div>
    """ + link("variables-and-operators","Variables and Operators") + """
    """ + link("data-types-and-conditionals","Data Types and Conditionals") + """
    """ + link("javascript-developer-tools","JavaScript Developer Tools") + """
    """ + link("function-basics","Function Basics") + """
    """ + link("problem-solving","Problem Solving") + """
    """ + link("understanding-errors","Understanding Errors") + """
    """ + link("project-rock-paper-scissors","Project: Rock Paper Scissors",True) + """
    """ + link("clean-code","Clean Code") + """
    """ + link("installing-nodejs","Installing Node.js") + """
    """ + link("arrays-and-loops","Arrays and Loops") + """
    """ + link("dom-manipulation-and-events","DOM Manipulation and Events") + """
    """ + link("revisiting-rock-paper-scissors","Revisiting Rock Paper Scissors") + """
    """ + link("project-etch-a-sketch","Project: Etch-a-Sketch",True) + """
    """ + link("object-basics","Object Basics") + """
    """ + link("project-calculator","Project: Calculator",True) + """
  </div>
  <div class="sidebar-section">
    <div class="sidebar-section-label">Conclusion</div>
    """ + link("choose-your-path","Choose Your Path Forward") + """
  </div>
</aside>"""

def code(snippet):
    """Wrap a code snippet in a copyable code block."""
    escaped = snippet.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f'<div class="code-block"><pre><code>{escaped}</code></pre></div>'

def prev_next(slug):
    idx = next((i for i,l in enumerate(ALL_LESSONS) if l[0]==slug), None)
    p = (ALL_LESSONS[idx-1][1], ALL_LESSONS[idx-1][0]+".html") if idx and idx>0 else None
    n = (ALL_LESSONS[idx+1][1], ALL_LESSONS[idx+1][0]+".html") if idx is not None and idx<len(ALL_LESSONS)-1 else None
    return p, n

def lesson_nav_bar(slug):
    prev, nxt = prev_next(slug)
    prev_btn = f'<a href="{prev[1]}" class="btn btn-blue-outline">← Previous</a>' if prev else '<span></span>'
    next_btn = f'<a href="{nxt[1]}" class="btn btn-blue">Next →</a>' if nxt else '<span></span>'
    return f"""<div class="lesson-nav-bar">
  <div class="lesson-nav-bar-group">{prev_btn}</div>
  <div class="lesson-nav-bar-group">
    <button class="btn btn-green mark-complete-btn">Mark Completed</button>
  </div>
  <div class="lesson-nav-bar-group">{next_btn}</div>
</div>"""

def write(slug, title, intro, overview, body, kc, assignments, resources):
    prev, nxt = prev_next(slug)
    bc = f'<nav class="breadcrumb"><a href="../../index.html">Home</a><span class="breadcrumb-sep">/</span><a href="../index.html">Foundations</a><span class="breadcrumb-sep">/</span><span class="breadcrumb-current">{title}</span></nav>'
    ov = "".join(f"<li>{i}</li>" for i in overview)
    kc_li = "".join(f'<li><a href="#{k[1]}" data-target="{k[1]}">{k[0]}</a></li>' for k in kc)
    as_li = "".join(f"<li>{a}</li>" for a in assignments)
    rs_li = "".join(f'<li><a href="{r[1]}" target="_blank" rel="noopener">{r[0]}</a></li>' for r in resources)
    prev_btn = f'<a href="{prev[1]}" class="pagination-link prev"><span class="pagination-label">← Previous</span><span class="pagination-title">{prev[0]}</span></a>' if prev else "<span></span>"
    next_btn = f'<a href="{nxt[1]}" class="pagination-link next"><span class="pagination-label">Next →</span><span class="pagination-title">{nxt[0]}</span></a>' if nxt else "<span></span>"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | DevPath</title>
  <link rel="stylesheet" href="../../css/styles.css">
</head>
<body>
{nav()}
{lesson_nav_bar(slug)}
<div class="page-header">
  <div class="page-header-inner">{bc}<h1>{title}</h1></div>
</div>
<div class="lesson-layout">
  {sidebar(slug)}
  <main>
    <div class="lesson-body">
      <div class="block-intro"><p>{intro}</p></div>
      <div class="block-overview">
        <div class="block-overview-label">Lesson Overview</div>
        <ul>{ov}</ul>
      </div>
      {body}
      <div class="block-kc">
        <div class="block-kc-label">Knowledge Check</div>
        <p class="kc-note">Click any question to jump to the part of this lesson that answers it.</p>
        <ol>{kc_li}</ol>
      </div>
      <div class="block-assignments">
        <div class="block-assignments-label">Assignments</div>
        <ol>{as_li}</ol>
      </div>
      <div class="block-resources">
        <div class="block-resources-label">Additional Resources</div>
        <ul>{rs_li}</ul>
      </div>
    </div>
    <div class="lesson-pagination">{prev_btn}{next_btn}</div>
  </main>
</div>
{footer()}
<script src="../../js/main.js"></script>
</body>
</html>"""
    with open(os.path.join(LESSONS, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  {slug}")


# ═══════════════════════════════════════════════════════════
#  LESSONS
# ═══════════════════════════════════════════════════════════

def seed():

    # ── 1 ──────────────────────────────────────────────────
    write("how-this-course-will-work", "How This Course Will Work",
    intro="Before you write a single line of code, spend a few minutes understanding how this curriculum is structured — because it works differently from most courses you may have tried.",
    overview=[
        "Understand the format every lesson in this curriculum follows.",
        "Know what to do when you get stuck.",
        "Understand why this curriculum values productive struggle over passive watching.",
    ],
    body="""
<h2 class="lesson-section-title" id="structure">How Every Lesson Is Structured</h2>
<p>Every lesson follows the same predictable shape so you always know what to expect:</p>
<ul>
  <li><strong>Introduction</strong> — A short paragraph explaining the topic and why it matters.</li>
  <li><strong>Lesson Overview</strong> — A bullet list of what you will understand by the end.</li>
  <li><strong>Content Sections</strong> — Plain-language explanations with copyable code examples.</li>
  <li><strong>Knowledge Check</strong> — Questions that scroll you back to the content that answers them.</li>
  <li><strong>Assignments</strong> — Exercises drawn from the best free resources on each topic.</li>
  <li><strong>Additional Resources</strong> — Curated links for going deeper.</li>
</ul>

<h2 class="lesson-section-title" id="struggle">Why We Do Not Hand-Hold</h2>
<p>Most online courses give you everything pre-solved. You follow along, things work, and it feels like learning. Then you try building something independently and draw a complete blank.</p>
<p>This curriculum is different. We explain concepts clearly, point you to the best resources, and then ask you to <em>actually build something</em>. The friction is intentional. When you wrestle with a problem for thirty minutes and finally crack it, that knowledge sticks in a way that watching a solution never achieves.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Think of learning to code like learning to swim. Reading about technique is useful background, but you only really learn by getting in the water.</p>
</div>

<h2 class="lesson-section-title" id="stuck">What To Do When You Get Stuck</h2>
<p>You will get stuck — that is guaranteed. Here is the process that works:</p>
<ol>
  <li>Read the error message carefully. It usually tells you the exact problem and line number.</li>
  <li>Search the specific error on Google. Copy the exact error text and paste it in.</li>
  <li>Check the official documentation for whatever tool you are using.</li>
  <li>If you are still stuck after 20–30 minutes with no progress, ask for help in the community — but explain what you have already tried.</li>
</ol>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>"It doesn't work" gets no response. "I expected X, got error Y, already tried Z" gets a real answer fast.</p>
</div>

<h2 class="lesson-section-title" id="snowball">The Snowball Effect</h2>
<p>Learning to code is a snowball rolling downhill. The first few weeks feel slow. But each concept you master makes the next one easier to understand. By the end of this curriculum, you will have enough foundation to teach yourself almost anything — which is the real goal.</p>
<p><strong>Do not skip lessons.</strong> Each one is a layer. Skip one and you will feel its absence later.</p>
""",
    kc=[
        ("What six sections does every lesson contain?", "structure"),
        ("What should you do before asking the community for help?", "stuck"),
        ("Why does this curriculum use productive struggle instead of solved examples?", "struggle"),
    ],
    assignments=[
        "Bookmark this page and come back here if you ever feel lost about how the course works.",
        "Set up a folder on your computer — digital or physical — where you keep notes on concepts you want to revisit.",
    ],
    resources=[
        ("MDN — Getting Started with the Web", "https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web"),
        ("YouTube — How to Think Like a Programmer (Coding Tech)", "https://www.youtube.com/watch?v=azcrPFhaY9k"),
        ("YouTube — Learning to Code is a Marathon, Not a Sprint (Mayuko)", "https://www.youtube.com/watch?v=E0PfRMkuBmQ"),
    ])

    # ── 2 ──────────────────────────────────────────────────
    write("introduction-to-web-dev", "Introduction to Web Development",
    intro="What do web developers actually do? This lesson gives you the big picture before you dive into technical details — so you always know where you are headed.",
    overview=[
        "Describe what front-end, back-end, and full-stack developers do.",
        "Understand the difference between a web designer and a web developer.",
        "Know the core tools that appear in every developer's workflow.",
    ],
    body="""
<h2 class="lesson-section-title" id="types">Types of Web Developers</h2>
<p>Web development broadly splits into three roles:</p>
<ul>
  <li><strong>Front-end developers</strong> build everything users see and interact with — layouts, buttons, animations, forms. Their primary tools are HTML, CSS, and JavaScript.</li>
  <li><strong>Back-end developers</strong> build server-side logic: user authentication, database queries, business rules, and APIs. They might use JavaScript (Node.js), Ruby, Python, or many others.</li>
  <li><strong>Full-stack developers</strong> work comfortably on both sides. That is what this curriculum prepares you to be.</li>
</ul>

<h2 class="lesson-section-title" id="designer-vs-dev">Designer vs. Developer</h2>
<p>These roles are often confused but are genuinely different skills. A <strong>designer</strong> focuses on visual aesthetics and user experience — how a product <em>feels</em>. A <strong>developer</strong> focuses on code — how a product <em>works</em>. Many people do both, but they are distinct disciplines.</p>

<h2 class="lesson-section-title" id="tools">The Core Toolbox</h2>
<p>You need no expensive software to become a developer. Here is what this curriculum uses:</p>
<ul>
  <li><strong>VS Code</strong> — A free, powerful text editor for writing code.</li>
  <li><strong>The terminal</strong> — A text-based interface for running programs and navigating files.</li>
  <li><strong>Git and GitHub</strong> — Git tracks every change to your code. GitHub stores it in the cloud.</li>
  <li><strong>A web browser with DevTools</strong> — Chrome or Firefox both have excellent built-in developer tools.</li>
</ul>

<h2 class="lesson-section-title" id="day">A Realistic Day</h2>
<p>A typical developer day involves reading existing code, writing new features, debugging broken ones, reviewing colleagues' work, and reading documentation. Communication takes up far more time than people expect — clear commit messages, well-described tickets, and thoughtful code comments are real professional skills.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Even senior developers Google basic things every single day. The skill is not memorising syntax — it is knowing how to find answers quickly and judge whether they solve your specific problem.</p>
</div>
""",
    kc=[
        ("What is the difference between a front-end and a back-end developer?", "types"),
        ("What is the difference between a web designer and a web developer?", "designer-vs-dev"),
        ("Name three tools every developer uses daily.", "tools"),
    ],
    assignments=[
        'Search YouTube for "day in the life of a web developer" and watch one video. Pay attention to how much time is spent reading code versus writing it.',
        "Read the MDN article linked below: 'What is the difference between webpage, website, web server, and search engine?'",
    ],
    resources=[
        ("MDN — Pages, Sites, Servers, and Search Engines", "https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/Pages_sites_servers_and_search_engines"),
        ("YouTube — Web Development In 2024 — A Practical Guide (Traversy Media)", "https://www.youtube.com/watch?v=EqzUcMzfV1w"),
        ("YouTube — Frontend vs Backend vs Fullstack (Fireship)", "https://www.youtube.com/watch?v=pkdgVYehiTE"),
    ])

    # ── 3 ──────────────────────────────────────────────────
    write("motivation-and-mindset", "Motivation and Mindset",
    intro="The technical side of coding is learnable by anyone. The real barrier is mindset. This lesson covers the mental habits that separate people who finish from people who quit.",
    overview=[
        "Understand the difference between a fixed and a growth mindset.",
        "Recognise the learning plateau and know how to push through it.",
        "Learn practical strategies for managing frustration.",
    ],
    body="""
<h2 class="lesson-section-title" id="growth-mindset">Fixed vs. Growth Mindset</h2>
<p>Psychologist Carol Dweck identified two ways people think about their abilities:</p>
<ul>
  <li>A <strong>fixed mindset</strong> says: <em>"I am either good at this or I am not."</em></li>
  <li>A <strong>growth mindset</strong> says: <em>"I cannot do this yet — but I can learn."</em></li>
</ul>
<p>People with a growth mindset treat failures as data. When their code breaks, they do not think "I am terrible at this." They think "What does this error tell me about what I have not understood yet?"</p>
<p>This single shift in framing is the most important preparation you can make before you start coding.</p>

<h2 class="lesson-section-title" id="plateau">The Learning Plateau</h2>
<p>Almost every learner hits a point where progress feels like it has stopped. New concepts resist sticking. Projects take four hours instead of one. This is the plateau — and it is completely normal.</p>
<p>The plateau is not evidence you have reached your limit. It is evidence your brain is integrating a large amount of new material simultaneously. Strategies that help:</p>
<ul>
  <li>Step away for 20 minutes. Walk around. Your subconscious keeps working when your conscious mind rests.</li>
  <li>Explain the concept out loud to yourself — or to a rubber duck on your desk.</li>
  <li>Go back one lesson and re-read the concept the current one builds on.</li>
  <li>Build something small using only what you currently know.</li>
</ul>

<h2 class="lesson-section-title" id="frustration">Managing Frustration</h2>
<p>Every developer has a story about spending hours debugging only to find a missing semicolon. Frustration is unavoidable. What matters is your response to it.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>The 20-minute rule: if you have been stuck on the same problem for 20 minutes with zero forward progress, take a five-minute break before doing anything else. This is not giving up — it is a deliberate cognitive strategy.</p>
</div>
<p>Also: comparing your progress to others online is a trap. People share their wins, not their hours of confusion. You are seeing a highlight reel, not the full story.</p>
""",
    kc=[
        ("What is the key difference between a fixed and a growth mindset?", "growth-mindset"),
        ("What is the 20-minute rule and why does it help?", "frustration"),
        ("Name two strategies for pushing through a learning plateau.", "plateau"),
    ],
    assignments=[
        "Watch Carol Dweck's TED Talk 'The Power of Believing That You Can Improve' (10 minutes). Link in Additional Resources.",
        "Write down one part of this curriculum you feel nervous about. Rewrite that worry using growth-mindset language — replace 'I can't' with 'I can't yet, and here is how I will approach it.'",
    ],
    resources=[
        ("YouTube — Carol Dweck: The Power of Believing That You Can Improve (TED)", "https://www.youtube.com/watch?v=_X0mgOOSpLU"),
        ("YouTube — How to Learn Anything Faster (Thomas Frank)", "https://www.youtube.com/watch?v=rA2XHWM__yE"),
        ("Article — What is a Growth Mindset? (Mindset Works)", "https://www.mindsetworks.com/science/"),
    ])

    # ── 4 ──────────────────────────────────────────────────
    write("asking-for-help", "Asking For Help",
    intro="Knowing how to ask a good technical question is one of the highest-leverage skills you can develop. A well-formed question gets answered in minutes. A vague one gets ignored or leads nowhere.",
    overview=[
        "Know the steps to take before asking for help.",
        "Understand what information makes a technical question useful.",
        "Know where to find help for web development questions.",
    ],
    body="""
<h2 class="lesson-section-title" id="before">Before You Ask</h2>
<p>Before posting anywhere, work through this checklist:</p>
<ol>
  <li><strong>Read the error message fully.</strong> The stack trace usually tells you exactly what went wrong and on which line.</li>
  <li><strong>Search Google.</strong> Copy the exact error text. Add the language or tool name. Someone has almost certainly had this problem before.</li>
  <li><strong>Check the documentation.</strong> MDN for HTML/CSS/JavaScript. Official docs for everything else.</li>
  <li><strong>Isolate the problem.</strong> Strip your code to the smallest example that still reproduces the issue. This process alone often reveals the bug.</li>
</ol>
<p>If you have done all of the above and are still stuck after 20–30 minutes, asking for help is exactly the right move.</p>

<h2 class="lesson-section-title" id="good-question">What Makes a Good Question</h2>
<p>A good technical question gives the helper everything they need without making them dig for it. Always include:</p>
<ul>
  <li><strong>What you are trying to do</strong> — the goal, not just the symptom.</li>
  <li><strong>What you expected to happen.</strong></li>
  <li><strong>What actually happened</strong> — paste the exact error message.</li>
  <li><strong>What you have already tried.</strong></li>
  <li><strong>A minimal code example</strong> — the smallest code that reproduces the problem.</li>
</ul>
""" + code("""<!-- Bad question -->
"My code doesn't work, can someone help?"

<!-- Good question -->
"I am trying to centre a div horizontally with Flexbox.
I expected it to centre but it stays left-aligned.
I have tried justify-content: center on the parent — no effect.
Here is my code: [paste minimal example]"
""") + """
<h2 class="lesson-section-title" id="where">Where to Ask</h2>
<ul>
  <li><strong>Stack Overflow</strong> — For general programming questions. Read their guide on asking good questions first.</li>
  <li><strong>MDN Web Docs</strong> — The definitive reference for HTML, CSS, and JavaScript.</li>
  <li><strong>Discord communities</strong> — Many web dev communities offer real-time help.</li>
  <li><strong>GitHub Issues</strong> — For bugs in specific libraries or tools.</li>
</ul>
""",
    kc=[
        ("What four steps should you take before asking for help?", "before"),
        ("What five pieces of information make a technical question useful?", "good-question"),
    ],
    assignments=[
        "Read Stack Overflow's official guide 'How do I ask a good question?' — linked in Additional Resources.",
        "The next time you get stuck, write out your question following the format above before posting it — even if you solve it yourself in the process.",
    ],
    resources=[
        ("Stack Overflow — How do I ask a good question?", "https://stackoverflow.com/help/how-to-ask"),
        ("YouTube — How to Ask Programming Questions (CS Dojo)", "https://www.youtube.com/watch?v=yCPEwzKrGAs"),
        ("MDN — Web Documentation (reference for all HTML/CSS/JS)", "https://developer.mozilla.org/en-US/"),
    ])

    # ── 5 ──────────────────────────────────────────────────
    write("computer-basics", "Computer Basics",
    intro="Before writing code you need to be completely comfortable navigating your machine. This lesson covers the fundamentals every developer relies on daily.",
    overview=[
        "Navigate your file system using files and folders.",
        "Understand absolute and relative file paths.",
        "Take screenshots and manage files efficiently.",
        "Use the keyboard shortcuts that save the most time.",
    ],
    body="""
<h2 class="lesson-section-title" id="files-folders">Files, Folders, and Paths</h2>
<p>Your computer organises everything in a tree of <strong>files</strong> and <strong>folders</strong>. A file path describes exactly where a file lives in that tree.</p>
""" + code("""# Mac / Linux — forward slashes
/home/alice/projects/my-site/index.html

# Windows — backslashes
C:\\Users\\Alice\\projects\\my-site\\index.html
""") + """
<h2 class="lesson-section-title" id="abs-relative">Absolute vs. Relative Paths</h2>
<p>An <strong>absolute path</strong> starts from the root of the file system and works from anywhere. A <strong>relative path</strong> is relative to your current location.</p>
""" + code("""# If you are inside /home/alice/projects/my-site/

# Absolute — works from anywhere
/home/alice/projects/my-site/index.html

# Relative — works from current folder
index.html

# Go up one level then into another folder
../other-site/index.html

# Special shortcuts
.   = current directory
..  = parent directory
""") + """
<h2 class="lesson-section-title" id="shortcuts">Essential Keyboard Shortcuts</h2>
<ul>
  <li><code>Ctrl+C</code> / <code>Cmd+C</code> — Copy</li>
  <li><code>Ctrl+V</code> / <code>Cmd+V</code> — Paste</li>
  <li><code>Ctrl+Z</code> / <code>Cmd+Z</code> — Undo</li>
  <li><code>Ctrl+S</code> / <code>Cmd+S</code> — Save</li>
  <li><code>Ctrl+F</code> / <code>Cmd+F</code> — Find in document</li>
  <li><code>Alt+Tab</code> / <code>Cmd+Tab</code> — Switch apps</li>
</ul>
""",
    kc=[
        ("What is a file path?", "files-folders"),
        ("What is the difference between an absolute and a relative path?", "abs-relative"),
        ("What does the <code>..</code> shorthand mean in a file path?", "abs-relative"),
    ],
    assignments=[
        "Complete the Computer Basics course on GCF Global (linked below) — it takes about 20 minutes.",
        "Create a folder called <code>devpath-projects</code> in your home directory. This is where all your project work will live throughout this curriculum.",
    ],
    resources=[
        ("GCF Global — Computer Basics (free course)", "https://edu.gcfglobal.org/en/computerbasics/"),
        ("YouTube — Computer Basics: Understanding Files and Folders (GCFLearnFree)", "https://www.youtube.com/watch?v=k-EID5_2D9U"),
        ("YouTube — File System and Paths Explained (CS Dojo)", "https://www.youtube.com/watch?v=uwAqEzhyjtw"),
    ])

    # ── 6 ──────────────────────────────────────────────────
    write("how-does-the-web-work", "How Does the Web Work?",
    intro="Every time you visit a website, a fascinating chain of events happens in milliseconds. Understanding this chain makes you a better developer — you know which part is responsible for what.",
    overview=[
        "Explain the client-server model.",
        "Describe what DNS does and why it exists.",
        "Understand HTTP at a high level.",
        "Trace the full sequence when you visit a URL.",
    ],
    body="""
<h2 class="lesson-section-title" id="client-server">Clients and Servers</h2>
<p>The web runs on a <strong>client-server model</strong>. Your browser is the <strong>client</strong> — it makes requests. The machine holding a website's files is the <strong>server</strong> — it responds.</p>
<p>Every website visit involves your browser sending a request to a server, and that server sending back files (HTML, CSS, JavaScript, images) that your browser assembles into what you see.</p>

<h2 class="lesson-section-title" id="dns">DNS — The Web's Address Book</h2>
<p>When you type <code>github.com</code>, how does your computer know which server to contact? It uses <strong>DNS (Domain Name System)</strong> — a distributed database that translates domain names into IP addresses.</p>
""" + code("""# Human-readable domain name
github.com

# Gets translated by DNS into a machine-readable IP address
140.82.121.4

# Your browser then contacts THAT IP address directly
""") + """
<h2 class="lesson-section-title" id="http">HTTP — The Language of the Web</h2>
<p><strong>HTTP</strong> (HyperText Transfer Protocol) is the format for communication between clients and servers. Your browser sends an HTTP <strong>request</strong>; the server responds with an HTTP <strong>response</strong> that includes a status code.</p>
<ul>
  <li><code>200 OK</code> — Success. Here is your content.</li>
  <li><code>301 Moved Permanently</code> — This URL has moved. Go here instead.</li>
  <li><code>404 Not Found</code> — The server could not find what you asked for.</li>
  <li><code>500 Internal Server Error</code> — Something went wrong on the server.</li>
</ul>

<h2 class="lesson-section-title" id="sequence">The Full Sequence</h2>
<p>When you visit <code>https://example.com</code>:</p>
<ol>
  <li>You press Enter.</li>
  <li>Your browser asks DNS: "What is the IP for example.com?"</li>
  <li>DNS replies with an IP address.</li>
  <li>Your browser sends an HTTP GET request to that IP.</li>
  <li>The server sends back an HTML file.</li>
  <li>Your browser parses the HTML, finds CSS and JS references, and fetches those too.</li>
  <li>Your browser renders the complete page.</li>
</ol>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Press F12, go to the Network tab, and refresh any page. Watch every single HTTP request happen in real time. There are usually far more than you expect.</p>
</div>
""",
    kc=[
        ("What is the difference between a client and a server?", "client-server"),
        ("What does DNS do?", "dns"),
        ("What does an HTTP 404 status code mean?", "http"),
        ("List the sequence of events when you visit a URL.", "sequence"),
    ],
    assignments=[
        "Open DevTools (F12 → Network tab), refresh any website and spend 5 minutes exploring the requests. How many are there? What file types are being fetched?",
        "Read MDN's 'How the Web Works' article linked below.",
    ],
    resources=[
        ("MDN — How the Web Works", "https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works"),
        ("YouTube — How the Internet Works in 5 Minutes (Aaron)", "https://www.youtube.com/watch?v=7_LPdttKXPc"),
        ("YouTube — DNS Explained (NetworkChuck)", "https://www.youtube.com/watch?v=27r4Bzuj5NQ"),
    ])

    # ── 7 ──────────────────────────────────────────────────
    write("installation-overview", "Installation Overview",
    intro="Before writing any code you need the right tools set up on your machine. This lesson explains what you will be installing and why each tool exists.",
    overview=[
        "Understand the purpose of each tool in your development setup.",
        "Know which installation path applies to your operating system.",
    ],
    body="""
<h2 class="lesson-section-title" id="tools">The Tools You Will Install</h2>
<p>This curriculum uses a specific set of tools that professional developers use daily. Here is what each one is for:</p>
<ul>
  <li><strong>VS Code</strong> — Your code editor. Where you write all your HTML, CSS, JavaScript, and more.</li>
  <li><strong>Git</strong> — Version control. Tracks every change to your code so you can go back in time.</li>
  <li><strong>Node.js</strong> — JavaScript runtime that lets you run JavaScript outside the browser. Required for many development tools.</li>
  <li><strong>Google Chrome</strong> — Your primary browser for testing. Its DevTools are the industry standard.</li>
</ul>

<h2 class="lesson-section-title" id="os">Choose Your Operating System Path</h2>
<p>Installation steps differ across operating systems. The next lesson — Installations — will give you exact steps for your system. Use the path that matches your machine:</p>
<ul>
  <li><strong>macOS</strong> — Uses Homebrew as a package manager.</li>
  <li><strong>Linux (Ubuntu/Debian)</strong> — Uses apt. Generally the smoothest developer setup.</li>
  <li><strong>Windows</strong> — Uses WSL2 (Windows Subsystem for Linux) to provide a Linux environment. This is the recommended path for Windows users — it gives you the same tools as Linux/Mac developers.</li>
</ul>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>If you are on Windows, do not skip WSL. Trying to use native Windows tools for web development causes significant pain. WSL gives you a proper Linux environment inside Windows.</p>
</div>
""",
    kc=[
        ("What is VS Code used for?", "tools"),
        ("Why do Windows users need WSL?", "os"),
    ],
    assignments=[
        "Read the official WSL installation guide linked below if you are on Windows.",
        "Make sure you know your operating system version before starting the Installations lesson.",
    ],
    resources=[
        ("Microsoft — Install WSL (Windows Subsystem for Linux)", "https://learn.microsoft.com/en-us/windows/wsl/install"),
        ("YouTube — WSL2 Setup for Web Development (Traversy Media)", "https://www.youtube.com/watch?v=cgH3nhYBmQs"),
        ("YouTube — How to Set Up Your Mac for Development (Traversy Media)", "https://www.youtube.com/watch?v=2qVBfBT0VcE"),
    ])

    # ── 8 ──────────────────────────────────────────────────
    write("installations", "Installations",
    intro="Time to set up your development environment. Follow the steps for your operating system carefully — a good setup now prevents hours of frustration later.",
    overview=[
        "Install VS Code and essential extensions.",
        "Install Git and configure it with your name and email.",
        "Install Google Chrome.",
        "Install Node.js via a version manager.",
    ],
    body="""
<h2 class="lesson-section-title" id="vscode">VS Code</h2>
<p>Download and install VS Code from <a href="https://code.visualstudio.com" target="_blank">code.visualstudio.com</a>. After installing, open it and install these essential extensions:</p>
<ul>
  <li><strong>Prettier</strong> — Formats your code automatically on save.</li>
  <li><strong>ESLint</strong> — Highlights JavaScript errors as you type.</li>
  <li><strong>Live Server</strong> — Opens your HTML file in the browser and auto-refreshes on save.</li>
</ul>
<p>To open any project folder in VS Code from the terminal, use:</p>
""" + code("""# Open current folder in VS Code
code .

# Open a specific folder
code ~/devpath-projects/my-project
""") + """
<h2 class="lesson-section-title" id="git-install">Git</h2>
<p>Check if Git is already installed:</p>
""" + code("""git --version
# Should output something like: git version 2.42.0
""") + """
<p>If not installed:</p>
""" + code("""# macOS (using Homebrew)
brew install git

# Ubuntu / Debian / WSL
sudo apt update && sudo apt install git

# Windows — download from git-scm.com
""") + """
<p>Configure Git with your identity (do this once):</p>
""" + code("""git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main
""") + """
<h2 class="lesson-section-title" id="node">Node.js via NVM</h2>
<p>Install Node.js using NVM (Node Version Manager) so you can switch versions easily:</p>
""" + code("""# Install NVM (Mac / Linux / WSL)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Reload your terminal, then install the LTS version of Node
nvm install --lts
nvm use --lts

# Verify
node --version
npm --version
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>If any step fails, copy the exact error and search it. Installation issues are extremely common and almost every one has a Stack Overflow answer.</p>
</div>
""",
    kc=[
        ("What command opens the current folder in VS Code?", "vscode"),
        ("What three Git config settings should you set globally?", "git-install"),
        ("Why install Node.js via NVM instead of directly?", "node"),
    ],
    assignments=[
        "Complete all four installations above. Verify each one works by running its <code>--version</code> command.",
        "Install the three VS Code extensions listed above.",
    ],
    resources=[
        ("VS Code — Official Download", "https://code.visualstudio.com/"),
        ("NVM — GitHub Repository", "https://github.com/nvm-sh/nvm"),
        ("YouTube — VSCode Setup for Web Development (Traversy Media)", "https://www.youtube.com/watch?v=fnPhJHN0jTE"),
    ])

    # ── 9 ──────────────────────────────────────────────────
    write("text-editors", "Text Editors",
    intro="VS Code is the industry-standard text editor for web development. This lesson covers the features and shortcuts that will make you significantly more productive.",
    overview=[
        "Use the most important VS Code keyboard shortcuts.",
        "Configure VS Code settings for web development.",
        "Understand what extensions are and which ones matter most.",
    ],
    body="""
<h2 class="lesson-section-title" id="shortcuts">Essential VS Code Shortcuts</h2>
<p>Learning these shortcuts pays back immediately:</p>
""" + code("""# Open Command Palette (find any command)
Ctrl+Shift+P  /  Cmd+Shift+P

# Open file quickly by name
Ctrl+P  /  Cmd+P

# Toggle the integrated terminal
Ctrl+`  /  Ctrl+`

# Multi-cursor: click additional lines while holding Alt
Alt+Click

# Move a line up or down
Alt+Up / Alt+Down

# Duplicate a line
Shift+Alt+Down

# Comment / uncomment a line
Ctrl+/  /  Cmd+/

# Format the entire document
Shift+Alt+F  /  Shift+Option+F

# Go to a specific line number
Ctrl+G  /  Cmd+G
""") + """
<h2 class="lesson-section-title" id="emmet">Emmet — HTML Shortcuts</h2>
<p>VS Code includes Emmet, which expands short abbreviations into full HTML. Type the abbreviation and press Tab:</p>
""" + code("""! + Tab
→ Full HTML5 boilerplate

div.container + Tab
→ <div class="container"></div>

ul>li*3 + Tab
→ <ul>
    <li></li>
    <li></li>
    <li></li>
  </ul>

h1{Hello World} + Tab
→ <h1>Hello World</h1>
""") + """
<h2 class="lesson-section-title" id="settings">Recommended Settings</h2>
<p>Open VS Code settings (<code>Ctrl+,</code>), then open the JSON settings (<code>Ctrl+Shift+P</code> → "Open User Settings JSON") and add:</p>
""" + code("""{
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "editor.wordWrap": "on",
  "editor.fontSize": 15,
  "editor.lineHeight": 1.7,
  "files.autoSave": "onFocusChange",
  "emmet.includeLanguages": { "javascript": "javascriptreact" }
}
"""),
    kc=[
        ("What shortcut opens the VS Code Command Palette?", "shortcuts"),
        ("What does the Emmet abbreviation <code>ul>li*3</code> expand to?", "emmet"),
        ("What does <code>editor.formatOnSave: true</code> do?", "settings"),
    ],
    assignments=[
        "Open VS Code and practise each shortcut in the list above at least once.",
        "Open your User Settings JSON and add all the recommended settings.",
        "Try five different Emmet abbreviations in a new HTML file.",
    ],
    resources=[
        ("VS Code — Tips and Tricks (official)", "https://code.visualstudio.com/docs/getstarted/tips-and-tricks"),
        ("YouTube — VSCode Tips and Tricks (Fireship)", "https://www.youtube.com/watch?v=u21W_tfPVrY"),
        ("Emmet — Cheat Sheet", "https://docs.emmet.io/cheat-sheet/"),
    ])

    # ── 10 ─────────────────────────────────────────────────
    write("command-line-basics", "Command Line Basics",
    intro="The command line is the developer's power tool. Once comfortable with it, you will move through your file system and run programs faster than any graphical interface allows.",
    overview=[
        "Open the terminal on your operating system.",
        "Navigate the file system using <code>pwd</code>, <code>ls</code>, and <code>cd</code>.",
        "Create and delete files and directories from the command line.",
        "Use time-saving terminal features like Tab completion and command history.",
    ],
    body="""
<h2 class="lesson-section-title" id="opening">Opening the Terminal</h2>
<ul>
  <li><strong>Mac:</strong> <code>Cmd+Space</code> → type "Terminal" → Enter</li>
  <li><strong>Linux:</strong> <code>Ctrl+Alt+T</code> or search your application menu</li>
  <li><strong>Windows:</strong> Open WSL from the Start menu, or use the integrated terminal in VS Code</li>
</ul>

<h2 class="lesson-section-title" id="navigation">Navigating the File System</h2>
""" + code("""pwd              # Print Working Directory — where are you right now?
ls               # List files and folders here
ls -la           # List all files (including hidden) with details
cd projects      # Change into the 'projects' folder
cd ..            # Go up one level to the parent folder
cd ~             # Go to your home directory (shortcut for /home/username)
cd /             # Go to the root of the file system
cd -             # Go back to the previous directory
""") + """
<h2 class="lesson-section-title" id="creating">Creating and Removing Files</h2>
""" + code("""mkdir my-folder          # Create a new directory
mkdir -p a/b/c           # Create nested directories in one command
touch index.html         # Create an empty file
cp file.txt backup.txt   # Copy a file
mv old-name.txt new-name.txt  # Rename or move a file
rm old-file.txt          # Delete a file (no recycle bin!)
rm -r old-folder         # Delete a folder and all contents (careful!)
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p><code>rm</code> permanently deletes files — they do not go to a recycle bin. Always double-check before running it, especially with the <code>-r</code> flag.</p>
</div>

<h2 class="lesson-section-title" id="tips">Time-Saving Tips</h2>
""" + code("""# Tab completion — press Tab to auto-complete file/folder names
cd Dev[Tab]   →  cd DevPath/

# Command history — press Up arrow to repeat previous commands

# Cancel a running command
Ctrl+C

# Clear the terminal screen
clear

# Show the last 10 commands you ran
history | tail -10
"""),
    kc=[
        ("What does <code>pwd</code> do?", "navigation"),
        ("How do you move up one level in the directory tree?", "navigation"),
        ("Why is <code>rm -r</code> dangerous?", "creating"),
        ("What key auto-completes file and folder names?", "tips"),
    ],
    assignments=[
        "Open your terminal, navigate to your home directory and create the folder <code>devpath-projects/foundations</code> using the command line only.",
        "Work through The Odin Project's Command Line Basics exercises (linked below).",
        "Practice until navigating with <code>cd</code>, <code>ls</code>, and <code>pwd</code> feels natural — avoid using the file manager GUI for the rest of the day.",
    ],
    resources=[
        ("The Odin Project — Command Line Basics exercises", "https://www.theodinproject.com/lessons/foundations-command-line-basics"),
        ("The Linux Command Line — free online book (William Shotts)", "http://linuxcommand.org/tlcl.php"),
        ("YouTube — Command Line Crash Course (Traversy Media)", "https://www.youtube.com/watch?v=uwAqEzhyjtw"),
        ("YouTube — Linux Terminal Full Course (freeCodeCamp)", "https://www.youtube.com/watch?v=ZtqBQ68cfJc"),
    ])

    # ── 11 ─────────────────────────────────────────────────
    write("setting-up-git", "Setting Up Git",
    intro="Git is already installed from the Installations lesson. This lesson covers connecting Git to GitHub and the one-time configuration that sets you up correctly for every project.",
    overview=[
        "Configure Git with your name, email, and preferred editor.",
        "Create and connect a GitHub account.",
        "Set up SSH key authentication so you never type your password again.",
    ],
    body="""
<h2 class="lesson-section-title" id="config">Git Configuration</h2>
<p>These settings attach your identity to every commit you make. Run them once:</p>
""" + code("""git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main
git config --global color.ui auto

# Verify your settings
git config --list
""") + """
<h2 class="lesson-section-title" id="github">Connecting to GitHub</h2>
<p>Create a free account at <a href="https://github.com" target="_blank">github.com</a> if you have not already. Use the same email address you configured in Git above.</p>

<h2 class="lesson-section-title" id="ssh">SSH Key Authentication</h2>
<p>SSH keys let you push to GitHub without entering a password every time. Set them up once and forget about it:</p>
""" + code("""# 1. Generate an SSH key
ssh-keygen -t ed25519 -C "you@example.com"
# Press Enter three times to accept defaults

# 2. Copy the public key to your clipboard
cat ~/.ssh/id_ed25519.pub
# Copy the output (starts with "ssh-ed25519 ...")

# 3. Add the key to GitHub:
#    GitHub → Settings → SSH and GPG keys → New SSH key
#    Paste your key and save

# 4. Test the connection
ssh -T git@github.com
# You should see: "Hi username! You've successfully authenticated."
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Once SSH is set up, always clone repositories using the SSH URL (starts with <code>git@github.com:</code>) rather than the HTTPS URL.</p>
</div>
""",
    kc=[
        ("What four Git settings should you configure globally?", "config"),
        ("What is the benefit of SSH key authentication over HTTPS?", "ssh"),
    ],
    assignments=[
        "Complete the SSH key setup above and verify it works with <code>ssh -T git@github.com</code>.",
        "Follow The Odin Project's Setting Up Git guide linked below for step-by-step screenshots.",
    ],
    resources=[
        ("The Odin Project — Setting Up Git", "https://www.theodinproject.com/lessons/foundations-setting-up-git"),
        ("GitHub Docs — Generating a new SSH key", "https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent"),
        ("YouTube — How to Setup SSH Keys for GitHub (Corey Schafer)", "https://www.youtube.com/watch?v=8X4u9sca3Io"),
    ])

    # ── 12 ─────────────────────────────────────────────────
    write("introduction-to-git", "Introduction to Git",
    intro="Git is how developers track changes, collaborate with teammates, and recover from mistakes. It is not optional — it is one of the most important tools you will ever learn.",
    overview=[
        "Explain what version control is and the problem it solves.",
        "Describe what Git is and how it differs from GitHub.",
        "Understand repositories, commits, and branches at a high level.",
    ],
    body="""
<h2 class="lesson-section-title" id="version-control">What Is Version Control?</h2>
<p>Imagine saving versions of a document manually: <code>essay_v1.docx</code>, <code>essay_final.docx</code>, <code>essay_FINAL_USE_THIS.docx</code>. That is manual version control and it is a mess.</p>
<p>Version control systems track every change to your files automatically. They record what changed, who changed it, and when — and let you rewind to any point in history.</p>

<h2 class="lesson-section-title" id="what-is-git">What Is Git?</h2>
<p><strong>Git</strong> is the most widely used version control system in the world, created by Linus Torvalds in 2005. It runs on your local machine, watches a folder called a <strong>repository</strong>, and records snapshots called <strong>commits</strong>.</p>

<h2 class="lesson-section-title" id="git-vs-github">Git vs. GitHub</h2>
<ul>
  <li><strong>Git</strong> — The tool. Lives on your computer. Tracks changes locally.</li>
  <li><strong>GitHub</strong> — A website that hosts Git repositories in the cloud for backup, sharing, and collaboration.</li>
</ul>
""" + code("""# Git is the tool you run in your terminal
git init
git add .
git commit -m "First commit"

# GitHub is the website where you store and share your repos
# You PUSH your local commits to GitHub
git push origin main
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Think of Git as the recording software on your computer and GitHub as the cloud backup service. They work together but are completely separate things.</p>
</div>

<h2 class="lesson-section-title" id="concepts">Key Concepts</h2>
<ul>
  <li><strong>Repository (repo)</strong> — A folder tracked by Git, containing your files plus a hidden <code>.git</code> folder.</li>
  <li><strong>Commit</strong> — A saved snapshot of your files. Like a save point in a video game.</li>
  <li><strong>Branch</strong> — A parallel version of your repo for developing features without affecting the main codebase.</li>
  <li><strong>Remote</strong> — A copy of your repo hosted elsewhere, typically on GitHub.</li>
</ul>
""",
    kc=[
        ("What problem does version control solve?", "version-control"),
        ("What is a Git commit?", "what-is-git"),
        ("What is the difference between Git and GitHub?", "git-vs-github"),
    ],
    assignments=[
        "Read the 'About Version Control' section of the official Git documentation linked below.",
        "Create a free GitHub account at github.com if you have not already done so.",
    ],
    resources=[
        ("Git Official Docs — About Version Control", "https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control"),
        ("YouTube — Git Explained in 100 Seconds (Fireship)", "https://www.youtube.com/watch?v=hwP7WQkmECE"),
        ("YouTube — Git and GitHub Crash Course (freeCodeCamp)", "https://www.youtube.com/watch?v=RGOj5yH7evk"),
    ])

    # ── 13 ─────────────────────────────────────────────────
    write("git-basics", "Git Basics",
    intro="Now that you know what Git is, let us use it. By the end of this lesson you will be tracking code changes, saving commits, and pushing to GitHub like a professional.",
    overview=[
        "Initialise a Git repo with <code>git init</code>.",
        "Stage and commit changes with <code>git add</code> and <code>git commit</code>.",
        "View history and status with <code>git log</code> and <code>git status</code>.",
        "Connect a local repo to GitHub and push commits.",
    ],
    body="""
<h2 class="lesson-section-title" id="init">Starting a Repository</h2>
""" + code("""cd ~/devpath-projects
mkdir git-practice && cd git-practice
git init
# Output: Initialized empty Git repository in .../git-practice/.git/
""") + """
<h2 class="lesson-section-title" id="add-commit">The Stage → Commit Cycle</h2>
<p>Git uses a deliberate two-step process. <strong>Staging</strong> is selecting what to include. <strong>Committing</strong> is saving that selection as a snapshot.</p>
""" + code("""# Check the current state of your repo
git status

# Stage a specific file
git add index.html

# Stage everything that has changed
git add .

# Commit what is staged with a descriptive message
git commit -m "Add homepage HTML structure"

# View your commit history
git log --oneline
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Write commit messages in the imperative mood: "Add login form" not "Added login form". This matches the convention used by Git itself.</p>
</div>

<h2 class="lesson-section-title" id="remote">Connecting to GitHub</h2>
""" + code("""# 1. Create a new repo on GitHub (github.com → + → New repository)
# 2. Copy the SSH URL: git@github.com:username/repo-name.git
# 3. Connect your local repo to it

git remote add origin git@github.com:username/git-practice.git
git branch -M main
git push -u origin main

# From now on, just:
git push
""") + """
<h2 class="lesson-section-title" id="workflow">The Daily Workflow</h2>
""" + code("""# 1. Make changes in VS Code
# 2. Check what changed
git status

# 3. Stage changes
git add .

# 4. Commit with a clear message
git commit -m "Describe what changed and why"

# 5. Push to GitHub
git push
"""),
    kc=[
        ("What command initialises a new Git repository?", "init"),
        ("What is the difference between <code>git add</code> and <code>git commit</code>?", "add-commit"),
        ("What command shows a compact history of all commits?", "add-commit"),
        ("What command sends local commits to GitHub?", "remote"),
    ],
    assignments=[
        "Create a new folder, initialise a Git repo, add a file, commit it, and push it to a new GitHub repository. Verify the file appears on GitHub.",
        "Make three separate changes to that file — one commit per change — each with a meaningful message. Push all three.",
        "Work through The Odin Project's Git Basics exercises linked below.",
    ],
    resources=[
        ("The Odin Project — Git Basics", "https://www.theodinproject.com/lessons/foundations-git-basics"),
        ("GitHub Docs — Hello World guide", "https://docs.github.com/en/get-started/quickstart/hello-world"),
        ("Git Cheat Sheet PDF (GitHub Education)", "https://education.github.com/git-cheat-sheet-education.pdf"),
        ("YouTube — Git Tutorial for Beginners (Programming with Mosh)", "https://www.youtube.com/watch?v=8JJ101D3knE"),
    ])

    print("\nAll lessons seeded. Committing to GitHub...\n")

    # ── Git commit ──────────────────────────────────────────
    os.chdir(BASE)
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", "Seed Foundations lessons 1-13 with full content"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("\nPushed to GitHub successfully.")

if __name__ == "__main__":
    seed()
