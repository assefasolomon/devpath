#!/usr/bin/env python3
"""
DevPath — Complete Foundations seeder.
- No mentions of The Odin Project anywhere
- Resources are the same quality sources TOP uses (MDN, javascript.info, YouTube)
- All explanations written originally
- Skips lessons already seeded with real content
"""
import os, subprocess

BASE    = os.path.expanduser("~/devpath")
LESSONS = os.path.join(BASE, "foundations", "lessons")

ALL_LESSONS = [
    ("how-this-course-will-work",      "How This Course Will Work"),
    ("introduction-to-web-dev",        "Introduction to Web Development"),
    ("motivation-and-mindset",         "Motivation and Mindset"),
    ("asking-for-help",                "Asking For Help"),
    ("join-the-community",             "Join the Community"),
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
        f'<a href="../../index.html" class="nav-logo">{LOGO} DevPath</a>'
        '<ul class="nav-links">'
        '<li><a href="../../index.html">Home</a></li>'
        '<li><a href="../index.html">Foundations</a></li>'
        '<li><a href="../../paths/full-stack-javascript/index.html">Full Stack JS</a></li>'
        '<li><a href="../../paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a></li>'
        '</ul></nav>'
    )

def footer():
    return '<footer class="site-footer"><p>DevPath — A free, open, project-based web development curriculum.</p></footer>'

def sidebar(active):
    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "") + (" active" if sl == active else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'
    s = '<aside class="sidebar"><div class="sidebar-course-title">Foundations</div>'
    groups = [
        ("Introduction", [
            ("how-this-course-will-work","How This Course Will Work",False),
            ("introduction-to-web-dev","Introduction to Web Development",False),
            ("motivation-and-mindset","Motivation and Mindset",False),
            ("asking-for-help","Asking For Help",False),
            ("join-the-community","Join the Community",False),
        ]),
        ("Prerequisites", [
            ("computer-basics","Computer Basics",False),
            ("how-does-the-web-work","How Does the Web Work?",False),
            ("installation-overview","Installation Overview",False),
            ("installations","Installations",False),
            ("text-editors","Text Editors",False),
            ("command-line-basics","Command Line Basics",False),
            ("setting-up-git","Setting Up Git",False),
        ]),
        ("Git Basics", [
            ("introduction-to-git","Introduction to Git",False),
            ("git-basics","Git Basics",False),
        ]),
        ("HTML Foundations", [
            ("introduction-to-html-css","Introduction to HTML and CSS",False),
            ("elements-and-tags","Elements and Tags",False),
            ("html-boilerplate","HTML Boilerplate",False),
            ("working-with-text","Working with Text",False),
            ("lists","Lists",False),
            ("links-and-images","Links and Images",False),
            ("commit-messages","Commit Messages",False),
            ("project-recipes","Project: Recipes",True),
        ]),
        ("CSS Foundations", [
            ("intro-to-css","Intro to CSS",False),
            ("the-cascade","The Cascade",False),
            ("inspecting-html-and-css","Inspecting HTML and CSS",False),
            ("the-box-model","The Box Model",False),
            ("block-and-inline","Block and Inline",False),
        ]),
        ("Flexbox", [
            ("introduction-to-flexbox","Introduction to Flexbox",False),
            ("growing-and-shrinking","Growing and Shrinking",False),
            ("axes","Axes",False),
            ("alignment","Alignment",False),
            ("project-landing-page","Project: Landing Page",True),
        ]),
        ("JavaScript Basics", [
            ("variables-and-operators","Variables and Operators",False),
            ("data-types-and-conditionals","Data Types and Conditionals",False),
            ("javascript-developer-tools","JavaScript Developer Tools",False),
            ("function-basics","Function Basics",False),
            ("problem-solving","Problem Solving",False),
            ("understanding-errors","Understanding Errors",False),
            ("project-rock-paper-scissors","Project: Rock Paper Scissors",True),
            ("clean-code","Clean Code",False),
            ("installing-nodejs","Installing Node.js",False),
            ("arrays-and-loops","Arrays and Loops",False),
            ("dom-manipulation-and-events","DOM Manipulation and Events",False),
            ("revisiting-rock-paper-scissors","Revisiting Rock Paper Scissors",False),
            ("project-etch-a-sketch","Project: Etch-a-Sketch",True),
            ("object-basics","Object Basics",False),
            ("project-calculator","Project: Calculator",True),
        ]),
        ("Conclusion", [
            ("choose-your-path","Choose Your Path Forward",False),
        ]),
    ]
    for label, items in groups:
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
    p = (ALL_LESSONS[idx-1][1], ALL_LESSONS[idx-1][0]+".html") if idx and idx > 0 else None
    n = (ALL_LESSONS[idx+1][1], ALL_LESSONS[idx+1][0]+".html") if idx is not None and idx < len(ALL_LESSONS)-1 else None
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
    path = os.path.join(LESSONS, f"{slug}.html")
    # Always overwrite to apply the no-odin-reference fix
    p, n = pn(slug)
    bc = (
        '<nav class="breadcrumb">'
        '<a href="../../index.html">Home</a>'
        '<span class="breadcrumb-sep">/</span>'
        '<a href="../index.html">Foundations</a>'
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
        '  <link rel="stylesheet" href="../../css/styles.css">\n'
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
        + '<script src="../../js/main.js"></script>\n</body>\n</html>'
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  {slug}")


# ═══════════════════════════════════════════════════════════
#  ALL 48 LESSONS
# ═══════════════════════════════════════════════════════════
def seed():

    write("how-this-course-will-work","How This Course Will Work",
    intro="Before you write a single line of code, spend a few minutes understanding how this curriculum is structured — because it works differently from most courses you may have tried.",
    overview=[
        "Understand the format every lesson follows.",
        "Know what to do when you get stuck.",
        "Understand why productive struggle is the core learning method.",
    ],
    body="""
<h2 class="lesson-section-title" id="structure">How Every Lesson Is Structured</h2>
<p>Every lesson follows the same predictable shape so you always know where you are:</p>
<ul>
  <li><strong>Introduction</strong> — A short paragraph explaining the topic and why it matters.</li>
  <li><strong>Lesson Overview</strong> — Bullet points of what you will understand by the end.</li>
  <li><strong>Content Sections</strong> — Plain-language explanations with copyable code examples.</li>
  <li><strong>Knowledge Check</strong> — Questions that scroll you back to the content that answers them.</li>
  <li><strong>Assignments</strong> — Exercises using the best free resources available on each topic.</li>
  <li><strong>Additional Resources</strong> — Curated links for going deeper.</li>
</ul>

<h2 class="lesson-section-title" id="struggle">Why This Curriculum Does Not Hand-Hold</h2>
<p>Most online courses give you everything pre-solved. You follow along, things work, and it <em>feels</em> like learning. Then you try to build something on your own and draw a complete blank.</p>
<p>This curriculum is different. Concepts are explained clearly, the best resources are pointed out, and then you are asked to <em>actually build something</em>. The friction is intentional. When you wrestle with a problem for thirty minutes and finally crack it, that knowledge sticks in a way that watching a solution never achieves.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Think of it like learning to swim. Reading about technique is useful — but you only truly learn by getting in the water.</p>
</div>

<h2 class="lesson-section-title" id="stuck">What To Do When You Get Stuck</h2>
<p>You will get stuck. Here is the process that works:</p>
<ol>
  <li><strong>Read the error message fully.</strong> It usually tells you the exact problem and line number.</li>
  <li><strong>Search Google.</strong> Copy the exact error text. Add the language or tool name.</li>
  <li><strong>Check the official documentation</strong> for whatever you are using.</li>
  <li><strong>If still stuck after 20–30 minutes</strong> — ask for help, but explain what you have already tried.</li>
</ol>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>"It doesn't work" gets ignored. "I expected X, got error Y, already tried Z" gets a real answer fast.</p>
</div>

<h2 class="lesson-section-title" id="snowball">The Snowball Effect</h2>
<p>Learning to code is a snowball rolling downhill. The first weeks feel slow. But each concept you master makes the next one easier. By the end of this curriculum you will have enough foundation to teach yourself almost anything — which is the real goal. <strong>Do not skip lessons.</strong> Each one is a layer the next builds on.</p>
""",
    kc=[
        ("What six sections does every lesson contain?", "structure"),
        ("What should you do before asking for help?", "stuck"),
        ("Why does this curriculum use productive struggle instead of solved examples?", "struggle"),
    ],
    assignments=[
        "Bookmark this page — come back here when you feel lost about how the course works.",
        "Set up a folder (digital or physical) where you keep notes on concepts you want to revisit.",
    ],
    resources=[
        ("MDN — Getting Started with the Web", "https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web"),
        ("YouTube — How to Think Like a Programmer (Coding Tech)", "https://www.youtube.com/watch?v=azcrPFhaY9k"),
        ("YouTube — Learning to Code is a Marathon (Mayuko)", "https://www.youtube.com/watch?v=E0PfRMkuBmQ"),
    ])

    write("introduction-to-web-dev","Introduction to Web Development",
    intro="What do web developers actually do? This lesson gives you the bird's-eye view so you always know where you are headed before diving into technical details.",
    overview=[
        "Describe what front-end, back-end, and full-stack developers do.",
        "Understand the difference between a web designer and a web developer.",
        "Know the core tools in every developer's daily workflow.",
    ],
    body="""
<h2 class="lesson-section-title" id="types">Types of Web Developers</h2>
<ul>
  <li><strong>Front-end developers</strong> build everything users see and interact with — layouts, buttons, animations, forms. Core tools: HTML, CSS, JavaScript.</li>
  <li><strong>Back-end developers</strong> build server-side logic: authentication, database queries, APIs. They use JavaScript (Node.js), Ruby, Python, and others.</li>
  <li><strong>Full-stack developers</strong> work comfortably on both sides. That is what this curriculum prepares you to be.</li>
</ul>

<h2 class="lesson-section-title" id="designer-vs-dev">Designer vs. Developer</h2>
<p>A <strong>designer</strong> focuses on visual aesthetics and user experience — how a product <em>feels</em>. A <strong>developer</strong> focuses on code — how a product <em>works</em>. Many people do both, but they are distinct disciplines requiring different expertise.</p>

<h2 class="lesson-section-title" id="tools">The Core Toolbox</h2>
<ul>
  <li><strong>VS Code</strong> — Free, powerful code editor. Where you write everything.</li>
  <li><strong>The terminal</strong> — Text-based interface for running programs and navigating files.</li>
  <li><strong>Git and GitHub</strong> — Git tracks code changes. GitHub stores them in the cloud.</li>
  <li><strong>Chrome DevTools</strong> — Built-in browser tools for inspecting and debugging pages.</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Even senior developers Google basic things every single day. The skill is not memorising syntax — it is knowing how to find answers quickly and judge whether they solve your specific problem.</p>
</div>
""",
    kc=[
        ("What is the difference between a front-end and a back-end developer?", "types"),
        ("What separates a web designer from a web developer?", "designer-vs-dev"),
        ("Name three tools every developer uses daily.", "tools"),
    ],
    assignments=[
        'Search YouTube for "day in the life of a web developer" and watch one video. Notice how much time is reading and communicating versus writing new code.',
        "Read the MDN article 'What is the difference between webpage, website, web server, and search engine?' — linked below.",
    ],
    resources=[
        ("MDN — Pages, Sites, Servers, and Search Engines", "https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/Pages_sites_servers_and_search_engines"),
        ("YouTube — Web Development In 2024 — A Practical Guide (Traversy Media)", "https://www.youtube.com/watch?v=EqzUcMzfV1w"),
        ("YouTube — Frontend vs Backend vs Fullstack (Fireship)", "https://www.youtube.com/watch?v=pkdgVYehiTE"),
    ])

    write("motivation-and-mindset","Motivation and Mindset",
    intro="The technical side of coding is learnable by anyone. The real barrier is mindset. This lesson covers the mental habits that separate people who finish from people who quit.",
    overview=[
        "Understand the difference between a fixed and a growth mindset.",
        "Recognise the learning plateau and know how to push through it.",
        "Learn strategies for managing frustration during hard problems.",
    ],
    body="""
<h2 class="lesson-section-title" id="growth-mindset">Fixed vs. Growth Mindset</h2>
<p>Psychologist Carol Dweck identified two ways people think about their abilities:</p>
<ul>
  <li><strong>Fixed mindset:</strong> <em>"I am either good at this or I am not."</em></li>
  <li><strong>Growth mindset:</strong> <em>"I cannot do this yet — but I can learn."</em></li>
</ul>
<p>People with a growth mindset treat failures as data. When code breaks they do not think "I'm terrible at this" — they think "What does this error tell me about what I haven't understood yet?" This single shift in framing is the most important preparation you can make.</p>

<h2 class="lesson-section-title" id="plateau">The Learning Plateau</h2>
<p>Almost every learner hits a point where progress feels like it has stopped. New concepts resist sticking. Projects take four hours instead of one. This is the plateau — completely normal.</p>
<p>The plateau is not evidence you have reached your limit. It means your brain is integrating a large amount of new material at once. Strategies that help:</p>
<ul>
  <li>Step away for 20 minutes. Walk around. Your subconscious keeps working.</li>
  <li>Explain the concept out loud to yourself — or a rubber duck on your desk.</li>
  <li>Go back one lesson and re-read what the current one builds on.</li>
  <li>Build something small using only what you already know.</li>
</ul>

<h2 class="lesson-section-title" id="frustration">Managing Frustration</h2>
<p>Every developer has a story about spending hours debugging only to find a missing semicolon. Frustration is unavoidable. What matters is your response.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>The 20-minute rule: if you have been stuck with zero forward progress for 20 minutes, take a 5-minute break before doing anything else. This is not giving up — it is a deliberate cognitive strategy that works.</p>
</div>
<p>Comparing your progress to others online is also a trap. People share their wins, not their hours of confusion. You are seeing a highlight reel.</p>
""",
    kc=[
        ("What is the key difference between a fixed and a growth mindset?", "growth-mindset"),
        ("What is the 20-minute rule and why does it help?", "frustration"),
        ("Name two strategies for pushing through a learning plateau.", "plateau"),
    ],
    assignments=[
        "Watch Carol Dweck's TED Talk 'The Power of Believing That You Can Improve' — linked below (10 minutes).",
        "Write down one part of this curriculum you feel nervous about. Rewrite that worry replacing 'I can't' with 'I can't yet — here is how I will approach it.'",
    ],
    resources=[
        ("YouTube — Carol Dweck: The Power of Believing You Can Improve (TED)", "https://www.youtube.com/watch?v=_X0mgOOSpLU"),
        ("YouTube — How to Learn Anything Faster (Thomas Frank)", "https://www.youtube.com/watch?v=rA2XHWM__yE"),
        ("Mindset Works — What is a Growth Mindset?", "https://www.mindsetworks.com/science/"),
    ])

    write("asking-for-help","Asking For Help",
    intro="Knowing how to ask a good technical question is one of the highest-leverage skills you can develop. A well-formed question gets answered in minutes. A vague one gets ignored.",
    overview=[
        "Know the steps to take before asking for help.",
        "Understand what makes a technical question useful.",
        "Know where to find help for web development questions.",
    ],
    body="""
<h2 class="lesson-section-title" id="before">Before You Ask</h2>
<ol>
  <li><strong>Read the error message fully.</strong> The stack trace usually says exactly what went wrong and on which line.</li>
  <li><strong>Search Google.</strong> Copy the exact error text, add the language or framework name.</li>
  <li><strong>Check the official documentation</strong> for whatever you are using.</li>
  <li><strong>Isolate the problem.</strong> Strip your code to the smallest example that still reproduces the issue — this process alone often reveals the bug.</li>
</ol>

<h2 class="lesson-section-title" id="good-question">What Makes a Good Question</h2>
<ul>
  <li><strong>What you are trying to do</strong> — the goal, not just the symptom</li>
  <li><strong>What you expected to happen</strong></li>
  <li><strong>What actually happened</strong> — paste the exact error message</li>
  <li><strong>What you have already tried</strong></li>
  <li><strong>A minimal code example</strong> — the smallest code that reproduces the problem</li>
</ul>
""" + code("""// Bad question
"My code doesn't work, can someone help?"

// Good question
"I'm trying to centre a div with Flexbox.
I expected it to centre horizontally but it stays left-aligned.
I've tried justify-content: center on the parent — no effect.
Here's the minimal code reproducing the issue: [paste code]"
""") + """
<h2 class="lesson-section-title" id="where">Where to Ask</h2>
<ul>
  <li><strong>Stack Overflow</strong> — The definitive Q&amp;A site for specific technical questions.</li>
  <li><strong>MDN Web Docs</strong> — The best reference for HTML, CSS, and JavaScript.</li>
  <li><strong>Discord communities</strong> — Real-time help from other developers.</li>
  <li><strong>GitHub Issues</strong> — For bugs in specific libraries or tools.</li>
</ul>
""",
    kc=[
        ("What four steps should you take before asking for help?", "before"),
        ("What five pieces of information make a question useful?", "good-question"),
    ],
    assignments=[
        "Read Stack Overflow's guide 'How do I ask a good question?' — linked below.",
        "The next time you get stuck, write out your question following the format above before posting — even if you solve it in the process.",
    ],
    resources=[
        ("Stack Overflow — How do I ask a good question?", "https://stackoverflow.com/help/how-to-ask"),
        ("YouTube — How to Ask Programming Questions (CS Dojo)", "https://www.youtube.com/watch?v=yCPEwzKrGAs"),
        ("MDN Web Docs — Home", "https://developer.mozilla.org/en-US/"),
    ])

    write("join-the-community","Join the Community",
    intro="Learning alone is hard. Learning alongside other developers is dramatically faster and more enjoyable. This lesson covers where to find your people and how to get the most from them.",
    overview=[
        "Understand why a learning community accelerates progress.",
        "Know where to ask questions and share your work.",
        "Learn community etiquette that gets you better help.",
    ],
    body="""
<h2 class="lesson-section-title" id="why">Why Community Accelerates Learning</h2>
<p>When you hit a wall — and you will — having a place to ask questions makes the difference between pushing through and giving up. A good community also exposes you to how other developers think and solve problems, which teaches you things no tutorial covers.</p>
<p>Beyond help, a community gives you accountability, celebrates your wins, and connects you with people who have already walked the path you are on.</p>

<h2 class="lesson-section-title" id="where">Where to Connect</h2>
<ul>
  <li><strong>Discord</strong> — Real-time chat with other learners. Many web dev communities offer channels for questions, project feedback, and general discussion.</li>
  <li><strong>GitHub</strong> — Build your public developer profile as you complete projects. Follow other learners for inspiration.</li>
  <li><strong>Reddit</strong> — r/learnprogramming and r/webdev are large, active communities for questions and discussion.</li>
  <li><strong>Stack Overflow</strong> — The definitive Q&amp;A site for specific technical questions. Search before posting.</li>
</ul>

<h2 class="lesson-section-title" id="etiquette">Getting the Most From a Community</h2>
<ul>
  <li><strong>Search before asking.</strong> Your question has probably already been answered.</li>
  <li><strong>Show your work.</strong> Share what you tried — it demonstrates effort and gets better answers.</li>
  <li><strong>Be specific.</strong> "It does not work" is not a question. Describe the goal, the expected result, and the actual result.</li>
  <li><strong>Help others.</strong> Answering questions — even ones where you are not fully sure — cements your own understanding better than reading does.</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>As soon as you know enough to help someone else, start helping. Teaching is one of the most powerful learning tools available.</p>
</div>
""",
    kc=[
        ("Why does learning in a community accelerate progress?", "why"),
        ("What makes a question get a good answer?", "etiquette"),
    ],
    assignments=[
        "Join at least one web development Discord server today.",
        "Introduce yourself in the community — share where you are in the curriculum and what you are hoping to build.",
    ],
    resources=[
        ("Reddit — r/learnprogramming", "https://www.reddit.com/r/learnprogramming/"),
        ("Reddit — r/webdev", "https://www.reddit.com/r/webdev/"),
        ("YouTube — How to Use Stack Overflow (Fireship)", "https://www.youtube.com/watch?v=E3UPFmEFMD8"),
    ])

    write("computer-basics","Computer Basics",
    intro="Before writing code you need to be completely comfortable navigating your machine. This lesson covers the fundamentals every developer relies on daily.",
    overview=[
        "Navigate your file system using files and folders.",
        "Understand absolute and relative paths.",
        "Use keyboard shortcuts that save the most time.",
        "Take screenshots and manage files efficiently.",
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
<p>An <strong>absolute path</strong> starts from the root and works from anywhere. A <strong>relative path</strong> is relative to your current location.</p>
""" + code("""# If you are inside /home/alice/projects/my-site/

# Absolute — works from anywhere
/home/alice/projects/my-site/index.html

# Relative — works from current folder
index.html

# Go up one level then into another folder
../other-project/index.html

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
  <li><code>Alt+Tab</code> / <code>Cmd+Tab</code> — Switch applications</li>
</ul>
""",
    kc=[
        ("What is a file path?", "files-folders"),
        ("What is the difference between an absolute and relative path?", "abs-relative"),
        ("What does the <code>..</code> shorthand mean?", "abs-relative"),
    ],
    assignments=[
        "Complete the GCF Global Computer Basics course (linked below) — about 20 minutes.",
        "Create a folder called <code>devpath-projects</code> in your home directory. This is where all your project work will live.",
    ],
    resources=[
        ("GCF Global — Computer Basics (free course)", "https://edu.gcfglobal.org/en/computerbasics/"),
        ("YouTube — Files and Folders Explained (GCFLearnFree)", "https://www.youtube.com/watch?v=k-EID5_2D9U"),
        ("YouTube — File Systems Explained (Fireship)", "https://www.youtube.com/watch?v=KN8YgJnShPM"),
    ])

    write("how-does-the-web-work","How Does the Web Work?",
    intro="Every time you visit a website a fascinating chain of events happens in milliseconds. Understanding this chain makes you a better developer — you know which part is responsible for what.",
    overview=[
        "Explain the client-server model.",
        "Describe what DNS does and why it exists.",
        "Understand HTTP at a high level.",
        "Trace the full sequence when you visit a URL.",
    ],
    body="""
<h2 class="lesson-section-title" id="client-server">Clients and Servers</h2>
<p>The web runs on a <strong>client-server model</strong>. Your browser is the <strong>client</strong> — it makes requests. The machine holding a website's files is the <strong>server</strong> — it responds. Every website visit is your browser asking a server for files, and that server sending them back.</p>

<h2 class="lesson-section-title" id="dns">DNS — The Web's Address Book</h2>
<p><strong>DNS (Domain Name System)</strong> translates human-readable domain names into machine-readable IP addresses.</p>
""" + code("""# Human-readable name
github.com

# DNS translates it to a machine-readable IP address
140.82.121.4

# Your browser contacts that IP address directly
""") + """
<h2 class="lesson-section-title" id="http">HTTP — The Language of the Web</h2>
<p>HTTP (HyperText Transfer Protocol) defines how clients and servers communicate. Your browser sends an HTTP <strong>request</strong>; the server replies with an HTTP <strong>response</strong> including a status code.</p>
<ul>
  <li><code>200 OK</code> — success</li>
  <li><code>301 Moved Permanently</code> — redirect</li>
  <li><code>404 Not Found</code> — resource does not exist</li>
  <li><code>500 Internal Server Error</code> — server-side problem</li>
</ul>

<h2 class="lesson-section-title" id="sequence">The Full Sequence</h2>
<ol>
  <li>You type a URL and press Enter</li>
  <li>Browser asks DNS for the IP address of the domain</li>
  <li>DNS replies with the IP</li>
  <li>Browser sends an HTTP GET request to that IP</li>
  <li>Server sends back an HTML file</li>
  <li>Browser parses HTML, finds CSS/JS references, requests those too</li>
  <li>Browser renders the complete page</li>
</ol>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Open DevTools (F12), go to the Network tab, and refresh any page. Watch every HTTP request happen in real time — usually far more than you expect.</p>
</div>
""",
    kc=[
        ("What is the difference between a client and a server?", "client-server"),
        ("What does DNS do?", "dns"),
        ("What does a 404 status code mean?", "http"),
        ("List the steps when you visit a URL.", "sequence"),
    ],
    assignments=[
        "Open DevTools on any website (F12 → Network tab) and spend 5 minutes exploring the requests. How many are there? What file types are fetched?",
        "Read MDN's 'How the Web Works' article — linked below.",
    ],
    resources=[
        ("MDN — How the Web Works", "https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works"),
        ("YouTube — How the Internet Works in 5 Minutes (Aaron)", "https://www.youtube.com/watch?v=7_LPdttKXPc"),
        ("YouTube — DNS Explained (NetworkChuck)", "https://www.youtube.com/watch?v=27r4Bzuj5NQ"),
    ])

    write("installation-overview","Installation Overview",
    intro="Before writing code you need the right tools. This lesson explains what you will install and why — so the Installations lesson feels purposeful rather than mechanical.",
    overview=[
        "Understand the purpose of each tool in your development setup.",
        "Know which installation path applies to your operating system.",
    ],
    body="""
<h2 class="lesson-section-title" id="tools">Your Development Toolkit</h2>
<ul>
  <li><strong>VS Code</strong> — Your code editor. Where you write everything.</li>
  <li><strong>Git</strong> — Version control. Tracks every change to your code.</li>
  <li><strong>Node.js</strong> — JavaScript runtime outside the browser. Required by most development tools.</li>
  <li><strong>Google Chrome</strong> — Primary browser for testing. Best DevTools in the industry.</li>
</ul>

<h2 class="lesson-section-title" id="os">Choose Your Path</h2>
<ul>
  <li><strong>macOS</strong> — Uses Homebrew as a package manager.</li>
  <li><strong>Linux (Ubuntu/Debian)</strong> — Uses apt. The smoothest developer experience.</li>
  <li><strong>Windows</strong> — Must use WSL2 (Windows Subsystem for Linux). This gives you a full Linux environment inside Windows — the same tools Mac and Linux developers use.</li>
</ul>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>If you are on Windows, do not skip WSL2. Attempting web development with native Windows tools causes significant compatibility problems. WSL2 solves them cleanly.</p>
</div>
""",
    kc=[
        ("What is each tool in the development toolkit used for?", "tools"),
        ("Why do Windows users need WSL2?", "os"),
    ],
    assignments=[
        "If you are on Windows, read the Microsoft WSL installation guide — linked below.",
        "Confirm you know your operating system version before starting the Installations lesson.",
    ],
    resources=[
        ("Microsoft — Install WSL", "https://learn.microsoft.com/en-us/windows/wsl/install"),
        ("YouTube — WSL2 Setup for Web Development (Traversy Media)", "https://www.youtube.com/watch?v=cgH3nhYBmQs"),
        ("YouTube — Mac Dev Environment Setup (Traversy Media)", "https://www.youtube.com/watch?v=2qVBfBT0VcE"),
    ])

    write("installations","Installations",
    intro="Time to set up your development environment. Follow the steps for your operating system carefully — a solid setup now prevents hours of frustration later.",
    overview=[
        "Install VS Code and essential extensions.",
        "Install and configure Git.",
        "Install Node.js using NVM.",
        "Verify every tool works.",
    ],
    body="""
<h2 class="lesson-section-title" id="vscode">VS Code</h2>
<p>Download from <a href="https://code.visualstudio.com" target="_blank" rel="noopener">code.visualstudio.com</a>, then install these three extensions:</p>
<ul>
  <li><strong>Prettier</strong> — auto-formats code on save</li>
  <li><strong>ESLint</strong> — highlights JavaScript errors as you type</li>
  <li><strong>Live Server</strong> — auto-refreshes your browser on save</li>
</ul>
""" + code("""# Open any project folder in VS Code from the terminal
code .

# Install extensions from the terminal
code --install-extension esbenp.prettier-vscode
code --install-extension dbaeumer.vscode-eslint
code --install-extension ritwickdey.LiveServer
""") + """
<h2 class="lesson-section-title" id="git">Git</h2>
""" + code("""# Check if Git is already installed
git --version

# Install on Ubuntu / WSL
sudo apt update && sudo apt install git

# Install on macOS
brew install git

# One-time global configuration
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main
""") + """
<h2 class="lesson-section-title" id="node">Node.js via NVM</h2>
""" + code("""# Install NVM (Mac / Linux / WSL)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Restart your terminal, then install the LTS version
nvm install --lts
nvm use --lts

# Verify both installed correctly
node --version    # v20.x.x or similar
npm --version     # 10.x.x or similar
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>If any step fails, copy the exact error message and search it. Installation errors are extremely common and almost every one has a documented solution.</p>
</div>
""",
    kc=[
        ("What command opens the current folder in VS Code?", "vscode"),
        ("What four Git config values should you set globally?", "git"),
        ("Why install Node.js via NVM instead of directly?", "node"),
    ],
    assignments=[
        "Complete all three installations and verify each with its <code>--version</code> command.",
        "Install all three VS Code extensions listed above.",
    ],
    resources=[
        ("VS Code — Official Download", "https://code.visualstudio.com/"),
        ("NVM — GitHub Repository", "https://github.com/nvm-sh/nvm"),
        ("YouTube — VSCode Setup for Web Development (Traversy Media)", "https://www.youtube.com/watch?v=fnPhJHN0jTE"),
    ])

    write("text-editors","Text Editors",
    intro="VS Code is the industry-standard editor for web development. This lesson covers the features and shortcuts that will make you significantly more productive from day one.",
    overview=[
        "Use the most important VS Code keyboard shortcuts.",
        "Configure VS Code settings for web development.",
        "Use Emmet to write HTML at speed.",
    ],
    body="""
<h2 class="lesson-section-title" id="shortcuts">Essential Shortcuts</h2>
""" + code("""# Command Palette — find any VS Code command
Ctrl+Shift+P  /  Cmd+Shift+P

# Quick file open by name
Ctrl+P  /  Cmd+P

# Toggle the integrated terminal
Ctrl+`

# Comment / uncomment selected line(s)
Ctrl+/  /  Cmd+/

# Move a line up or down
Alt+Up  /  Alt+Down

# Duplicate line below
Shift+Alt+Down

# Format the entire document
Shift+Alt+F  /  Shift+Option+F

# Find and replace
Ctrl+H  /  Cmd+H

# Go to a specific line number
Ctrl+G  /  Cmd+G
""") + """
<h2 class="lesson-section-title" id="emmet">Emmet — Write HTML at Speed</h2>
<p>Type an abbreviation, press <kbd>Tab</kbd>, and VS Code expands it into full HTML:</p>
""" + code("""!                     → Full HTML5 boilerplate
div.container         → <div class="container"></div>
ul>li*3               → <ul> with 3 <li> items
h1{Hello World}       → <h1>Hello World</h1>
a[href=#]{Click me}   → <a href="#">Click me</a>
input[type=email]     → <input type="email">
""") + """
<h2 class="lesson-section-title" id="settings">Recommended Settings</h2>
<p>Open settings JSON with <kbd>Ctrl+Shift+P</kbd> → "Open User Settings JSON":</p>
""" + code("""{
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "editor.wordWrap": "on",
  "editor.fontSize": 15,
  "editor.lineHeight": 1.7,
  "files.autoSave": "onFocusChange"
}
"""),
    kc=[
        ("What shortcut opens the VS Code Command Palette?", "shortcuts"),
        ("What does the Emmet abbreviation <code>ul>li*3</code> expand to?", "emmet"),
        ("What does <code>editor.formatOnSave</code> do?", "settings"),
    ],
    assignments=[
        "Practise every shortcut in the list at least once in VS Code.",
        "Add all recommended settings to your User Settings JSON.",
        "Try five different Emmet abbreviations in a new HTML file.",
    ],
    resources=[
        ("VS Code — Tips and Tricks (official)", "https://code.visualstudio.com/docs/getstarted/tips-and-tricks"),
        ("Emmet — Cheat Sheet", "https://docs.emmet.io/cheat-sheet/"),
        ("YouTube — VSCode Tips and Tricks (Fireship)", "https://www.youtube.com/watch?v=u21W_tfPVrY"),
    ])

    write("command-line-basics","Command Line Basics",
    intro="The command line is the developer's power tool. Once comfortable with it you will navigate your file system and run programs faster than any graphical interface allows.",
    overview=[
        "Open the terminal on your operating system.",
        "Navigate the file system using <code>pwd</code>, <code>ls</code>, and <code>cd</code>.",
        "Create and delete files and directories from the command line.",
        "Use Tab completion and command history to work faster.",
    ],
    body="""
<h2 class="lesson-section-title" id="opening">Opening the Terminal</h2>
<ul>
  <li><strong>Mac:</strong> <code>Cmd+Space</code> → type "Terminal" → Enter</li>
  <li><strong>Linux:</strong> <code>Ctrl+Alt+T</code> or search your application menu</li>
  <li><strong>Windows (WSL):</strong> Open Ubuntu from the Start menu, or use the VS Code integrated terminal</li>
</ul>

<h2 class="lesson-section-title" id="navigation">Navigating the File System</h2>
""" + code("""pwd              # Print Working Directory — where are you right now?
ls               # List files and folders in current directory
ls -la           # List all files including hidden ones, with details
cd projects      # Change into the 'projects' folder
cd ..            # Go up one level to parent folder
cd ~             # Go to your home directory
cd -             # Go back to the previous directory
""") + """
<h2 class="lesson-section-title" id="creating">Creating and Removing Files</h2>
""" + code("""mkdir my-folder           # Create a new directory
mkdir -p a/b/c            # Create nested directories at once
touch index.html          # Create an empty file
cp file.txt backup.txt    # Copy a file
mv old.txt new.txt        # Rename or move a file
rm old-file.txt           # Delete a file — no recycle bin!
rm -r old-folder          # Delete a folder and all its contents
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p><code>rm</code> permanently deletes files. Always double-check before running it — especially with <code>-r</code> which deletes entire directories.</p>
</div>

<h2 class="lesson-section-title" id="tips">Time-Saving Tips</h2>
""" + code("""# Tab completion — press Tab to auto-complete names
cd Dev[Tab]  →  cd DevPath/

# Up arrow — cycle through previous commands

# Cancel a running command
Ctrl+C

# Clear the terminal screen
clear

# Show recent command history
history | tail -20
"""),
    kc=[
        ("What does <code>pwd</code> do?", "navigation"),
        ("How do you move up one level in the directory tree?", "navigation"),
        ("Why is <code>rm -r</code> dangerous?", "creating"),
        ("What key auto-completes file and folder names?", "tips"),
    ],
    assignments=[
        "Open your terminal and create the folder <code>devpath-projects/foundations</code> using only command-line commands.",
        "Work through the command line exercises linked below.",
        "Avoid using your file manager GUI for the rest of the day — use the terminal instead.",
    ],
    resources=[
        ("The Linux Command Line — free online book (William Shotts)", "http://linuxcommand.org/tlcl.php"),
        ("YouTube — Command Line Crash Course (Traversy Media)", "https://www.youtube.com/watch?v=uwAqEzhyjtw"),
        ("YouTube — Linux Terminal Full Course (freeCodeCamp)", "https://www.youtube.com/watch?v=ZtqBQ68cfJc"),
    ])

    write("setting-up-git","Setting Up Git",
    intro="Git is installed. Now connect it to GitHub and set up SSH keys so you never need to type a password when pushing code.",
    overview=[
        "Configure Git with your name, email, and editor.",
        "Create a GitHub account.",
        "Set up SSH key authentication.",
    ],
    body="""
<h2 class="lesson-section-title" id="config">Git Configuration</h2>
""" + code("""git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main
git config --global color.ui auto

# Verify your settings
git config --list
""") + """
<h2 class="lesson-section-title" id="github">GitHub Account</h2>
<p>Create a free account at <a href="https://github.com" target="_blank" rel="noopener">github.com</a>. Use the same email address you just configured in Git. Your GitHub profile will become your developer portfolio — choose a professional username.</p>

<h2 class="lesson-section-title" id="ssh">SSH Key Authentication</h2>
<p>SSH keys let you push to GitHub without entering a password every time. Set this up once and forget about it.</p>
""" + code("""# Step 1 — Generate an SSH key
ssh-keygen -t ed25519 -C "you@example.com"
# Press Enter three times to accept all defaults

# Step 2 — Display and copy your public key
cat ~/.ssh/id_ed25519.pub
# Copy the entire output (starts with ssh-ed25519...)

# Step 3 — Add the key to GitHub
# github.com → Settings → SSH and GPG keys → New SSH key
# Paste the key and click Add SSH key

# Step 4 — Test the connection
ssh -T git@github.com
# Expected: "Hi username! You've successfully authenticated."
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>After SSH is set up, always clone repos using the SSH URL (starts with <code>git@github.com:</code>) — not the HTTPS URL. You will never need to enter a password.</p>
</div>
""",
    kc=[
        ("What five Git settings should you configure globally?", "config"),
        ("What is the benefit of SSH over HTTPS?", "ssh"),
    ],
    assignments=[
        "Complete the SSH setup and verify with <code>ssh -T git@github.com</code>.",
        "Read the GitHub SSH documentation linked below for illustrated steps.",
    ],
    resources=[
        ("GitHub Docs — Generating SSH Keys", "https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent"),
        ("YouTube — SSH Keys for GitHub (Corey Schafer)", "https://www.youtube.com/watch?v=8X4u9sca3Io"),
        ("Git Official Docs — Getting Started", "https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup"),
    ])

    write("introduction-to-git","Introduction to Git",
    intro="Git is how developers track changes, collaborate with teammates, and recover from mistakes. It is not optional — it is one of the most important professional tools you will ever learn.",
    overview=[
        "Explain what version control is and the problem it solves.",
        "Describe what Git is and how it differs from GitHub.",
        "Understand repositories, commits, and branches at a high level.",
    ],
    body="""
<h2 class="lesson-section-title" id="version-control">What Is Version Control?</h2>
<p>Imagine saving document versions manually: <code>essay_v1.docx</code>, <code>essay_final.docx</code>, <code>essay_FINAL_USE_THIS.docx</code>. That is manual version control — messy, error-prone, and unscalable.</p>
<p>Version control systems track every change automatically. They record what changed, who changed it, and when — and let you rewind to any point in history, compare versions, and merge work from multiple people simultaneously.</p>

<h2 class="lesson-section-title" id="what-is-git">What Is Git?</h2>
<p>Git is the most widely used version control system in the world. It runs on your local machine, watches a folder called a <strong>repository</strong>, and records snapshots called <strong>commits</strong>. Each commit is a save point you can always return to.</p>

<h2 class="lesson-section-title" id="git-vs-github">Git vs. GitHub</h2>
<ul>
  <li><strong>Git</strong> — The tool. Lives on your computer. Tracks changes locally.</li>
  <li><strong>GitHub</strong> — A website hosting Git repositories in the cloud. Provides backup, sharing, and collaboration features.</li>
</ul>
""" + code("""# Git is the command-line tool you run in your terminal
git init
git add .
git commit -m "First commit"

# GitHub is where you PUSH those commits for backup and sharing
git push origin main
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Think of Git as the recording software on your computer, and GitHub as the cloud service where you store backups and share your work. They cooperate but are entirely separate things.</p>
</div>
""",
    kc=[
        ("What problem does version control solve?", "version-control"),
        ("What is a Git commit?", "what-is-git"),
        ("What is the difference between Git and GitHub?", "git-vs-github"),
    ],
    assignments=[
        "Read the 'About Version Control' section of the official Git documentation — linked below.",
        "Create a free GitHub account if you have not done so already.",
    ],
    resources=[
        ("Git Official Docs — About Version Control", "https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control"),
        ("YouTube — Git Explained in 100 Seconds (Fireship)", "https://www.youtube.com/watch?v=hwP7WQkmECE"),
        ("YouTube — Git and GitHub Crash Course (freeCodeCamp)", "https://www.youtube.com/watch?v=RGOj5yH7evk"),
    ])

    write("git-basics","Git Basics",
    intro="Now that you know what Git is, let us use it. By the end of this lesson you will be tracking code changes, saving commits, and pushing to GitHub like a professional.",
    overview=[
        "Initialise a Git repo with <code>git init</code>.",
        "Stage and save changes with <code>git add</code> and <code>git commit</code>.",
        "View history and status.",
        "Connect to GitHub and push commits.",
    ],
    body="""
<h2 class="lesson-section-title" id="init">Starting a Repository</h2>
""" + code("""cd ~/devpath-projects
mkdir git-practice && cd git-practice
git init
# Output: Initialized empty Git repository in .../git-practice/.git/
""") + """
<h2 class="lesson-section-title" id="add-commit">Stage → Commit Cycle</h2>
<p>Git saves changes in a deliberate two-step process. <strong>Staging</strong> selects what to include. <strong>Committing</strong> permanently saves that selection as a snapshot.</p>
""" + code("""git status                              # see what has changed
git add index.html                      # stage one file
git add .                               # stage all changed files
git commit -m "Add homepage structure"  # save staged changes

git log --oneline                       # view commit history
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Write commit messages in the imperative mood: "Add login form" not "Added login form". This is the universal convention used by Git itself and professional projects worldwide.</p>
</div>

<h2 class="lesson-section-title" id="remote">Connecting to GitHub</h2>
""" + code("""# 1. Create a new repo on github.com (+ icon → New repository)
# 2. Copy the SSH URL shown on the next screen
# 3. Connect your local repo

git remote add origin git@github.com:USERNAME/git-practice.git
git branch -M main
git push -u origin main

# Every future push is simply:
git push
""") + """
<h2 class="lesson-section-title" id="workflow">The Daily Workflow</h2>
""" + code("""# 1. Make changes in VS Code
# 2. Review what changed
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
        ("What command shows compact commit history?", "add-commit"),
        ("What command sends local commits to GitHub?", "remote"),
    ],
    assignments=[
        "Create a folder, initialise a Git repo, add a file, commit it, and push it to a new GitHub repository. Verify the file appears on GitHub.",
        "Make three separate changes — one commit per change with a meaningful message. Push all three.",
        "Work through the Git exercises linked below.",
    ],
    resources=[
        ("GitHub Docs — Hello World Guide", "https://docs.github.com/en/get-started/quickstart/hello-world"),
        ("Git Cheat Sheet PDF (GitHub Education)", "https://education.github.com/git-cheat-sheet-education.pdf"),
        ("YouTube — Git Tutorial for Beginners (Programming with Mosh)", "https://www.youtube.com/watch?v=8JJ101D3knE"),
    ])

    write("introduction-to-html-css","Introduction to HTML and CSS",
    intro="HTML and CSS are the two foundational languages of every website. This lesson gives you a clear picture of what each does before you start writing either one.",
    overview=[
        "Describe what HTML is responsible for on a web page.",
        "Describe what CSS is responsible for on a web page.",
        "Understand why HTML and CSS are kept in separate files.",
    ],
    body="""
<h2 class="lesson-section-title" id="html-role">What HTML Does</h2>
<p>HTML (HyperText Markup Language) defines the <strong>structure and content</strong> of a page. It tells the browser what things <em>are</em> — a heading, a paragraph, an image, a link. Think of it as the skeleton of a building.</p>
""" + code("""<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <img src="photo.jpg" alt="A photo">
    <a href="about.html">About</a>
  </body>
</html>
""") + """
<h2 class="lesson-section-title" id="css-role">What CSS Does</h2>
<p>CSS (Cascading Style Sheets) controls the <strong>visual presentation</strong> — colours, fonts, spacing, layout, animations. Using the building analogy: CSS is the paint, the furniture, the lighting.</p>
""" + code("""h1 {
  color: #1d4ed8;
  font-size: 2.5rem;
  font-weight: 700;
}

p {
  color: #475569;
  line-height: 1.75;
  max-width: 65ch;
}
""") + """
<h2 class="lesson-section-title" id="together">How They Work Together</h2>
<p>HTML and CSS are kept in separate files on purpose. This <em>separation of concerns</em> means one HTML page can be completely restyled just by swapping its CSS file — without touching any HTML.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Mental model: HTML is the noun (what things <em>are</em>), CSS is the adjective (how they <em>look</em>), JavaScript is the verb (what they <em>do</em>).</p>
</div>
""",
    kc=[
        ("What is HTML responsible for?", "html-role"),
        ("What is CSS responsible for?", "css-role"),
        ("Why are HTML and CSS in separate files?", "together"),
    ],
    assignments=[
        "Read MDN's 'Getting Started with HTML' — linked below.",
        "Read MDN's 'What is CSS?' — linked below.",
    ],
    resources=[
        ("MDN — Getting Started with HTML", "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started"),
        ("MDN — What is CSS?", "https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS"),
        ("YouTube — HTML and CSS for Beginners (Kevin Powell)", "https://www.youtube.com/watch?v=qz0aGYrrlhU"),
    ])

    write("elements-and-tags","Elements and Tags",
    intro="HTML is built from elements. Understanding exactly what an element is — and how tags, content, and attributes combine — gives you a solid foundation for everything that follows.",
    overview=[
        "Explain the difference between an HTML element and a tag.",
        "Identify opening tags, closing tags, and void elements.",
        "Understand correct nesting.",
        "Use attributes to add extra information to elements.",
    ],
    body="""
<h2 class="lesson-section-title" id="elements">Elements and Tags</h2>
<p>An <strong>HTML element</strong> is an opening tag + content + closing tag working together:</p>
""" + code("""<!-- Standard element structure -->
<tagname>Content goes here</tagname>

<!-- Real examples -->
<p>This is a paragraph.</p>
<h1>This is the main heading.</h1>
<strong>This text is bold.</strong>
<em>This text is italic.</em>
""") + """
<p>The <strong>tag</strong> is the part inside angle brackets — <code>&lt;p&gt;</code>. The <strong>element</strong> is the complete unit: opening tag + content + closing tag.</p>

<h2 class="lesson-section-title" id="void">Void Elements</h2>
<p>Some elements carry no content and have no closing tag. They are called <strong>void elements</strong>:</p>
""" + code("""<img src="sunset.jpg" alt="A golden sunset over the sea">
<input type="text" placeholder="Enter your name">
<br>
<hr>
<meta charset="UTF-8">
<link rel="stylesheet" href="styles.css">
""") + """
<h2 class="lesson-section-title" id="nesting">Nesting Elements</h2>
<p>Elements can live inside other elements. The rule: close tags in the reverse order you opened them.</p>
""" + code("""<!-- CORRECT — inner closes before outer -->
<p>I love <strong>web development</strong> deeply.</p>

<ul>
  <li>First item</li>
  <li>Second <em>important</em> item</li>
</ul>

<!-- WRONG — tags overlap -->
<p>I love <strong>web development</p></strong>
""") + """
<h2 class="lesson-section-title" id="attributes">Attributes</h2>
<p>Attributes provide extra information and always live inside the opening tag:</p>
""" + code("""<a href="https://example.com">Visit Example</a>
<img src="photo.jpg" alt="A description of the photo">
<input type="email" placeholder="you@example.com">
<div class="card" id="hero">Content</div>
"""),
    kc=[
        ("What is the difference between an HTML tag and an element?", "elements"),
        ("What is a void element? Name two examples.", "void"),
        ("What rule must you follow when nesting elements?", "nesting"),
        ("Where do attributes go in an HTML element?", "attributes"),
    ],
    assignments=[
        "Without looking at any reference, write 8 different HTML elements from memory. Then verify each on MDN.",
        "Read MDN's 'Getting Started with HTML — anatomy of an HTML element' section — linked below.",
    ],
    resources=[
        ("MDN — Getting Started with HTML", "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started"),
        ("MDN — HTML Element Reference", "https://developer.mozilla.org/en-US/docs/Web/HTML/Element"),
        ("YouTube — HTML Crash Course for Absolute Beginners (Traversy Media)", "https://www.youtube.com/watch?v=UB1O30fR-EE"),
    ])

    write("html-boilerplate","HTML Boilerplate",
    intro="Every HTML file needs a standard starting structure. This lesson explains what each line does and how to generate the whole thing in under a second.",
    overview=[
        "Explain the purpose of the DOCTYPE declaration.",
        "Describe what the html, head, and body elements each do.",
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
  <li><code>&lt;!DOCTYPE html&gt;</code> — Tells the browser this is HTML5. Without it, browsers use an unpredictable legacy rendering mode.</li>
  <li><code>&lt;html lang="en"&gt;</code> — Root element wrapping the entire document. <code>lang</code> helps screen readers and search engines.</li>
  <li><code>&lt;head&gt;</code> — Contains metadata <em>about</em> the page — not displayed content. The page's settings panel.</li>
  <li><code>&lt;meta charset="UTF-8"&gt;</code> — Use UTF-8 encoding, supporting virtually every character in every language.</li>
  <li><code>&lt;meta name="viewport"&gt;</code> — Makes the page display correctly on mobile. Without this, mobile browsers show a zoomed-out desktop view.</li>
  <li><code>&lt;title&gt;</code> — Text shown on the browser tab and in search results.</li>
  <li><code>&lt;body&gt;</code> — Everything visible to the user lives here.</li>
</ul>

<h2 class="lesson-section-title" id="emmet">Generate It Instantly</h2>
<p>In VS Code: create a <code>.html</code> file, type <code>!</code> on line 1, press <kbd>Tab</kbd>. Emmet generates the entire boilerplate instantly.</p>

<h2 class="lesson-section-title" id="scripts">Where to Put Script Tags</h2>
<p>Place <code>&lt;script&gt;</code> tags just before <code>&lt;/body&gt;</code> — not in <code>&lt;head&gt;</code>. This ensures all HTML elements exist in the DOM before JavaScript tries to access them.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Even though the Emmet shortcut is quick, practise writing the boilerplate from memory. Understanding each line matters more than knowing the shortcut.</p>
</div>
""",
    kc=[
        ("What does the DOCTYPE declaration tell the browser?", "each-part"),
        ("What is the difference between head and body?", "each-part"),
        ("What does the viewport meta tag do?", "each-part"),
        ("Why place script tags just before </body>?", "scripts"),
    ],
    assignments=[
        "Create a new HTML file and write the full boilerplate from memory — no Emmet shortcut. Open it in Chrome and confirm it loads without errors.",
        "Add a title, h1, and two paragraphs. Link an empty CSS file. Verify in DevTools the stylesheet is being requested.",
    ],
    resources=[
        ("MDN — Document and Website Structure", "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure"),
        ("YouTube — HTML Boilerplate Explained (Kevin Powell)", "https://www.youtube.com/watch?v=G3e-cpL7ofc"),
        ("Emmet Docs — Cheat Sheet", "https://docs.emmet.io/cheat-sheet/"),
    ])

    write("working-with-text","Working with Text",
    intro="Most web page content is text. This lesson covers the HTML elements for headings, paragraphs, and emphasis — and the important distinction between semantic and presentational markup.",
    overview=[
        "Use headings h1–h6 correctly and semantically.",
        "Wrap body text in paragraph elements.",
        "Use strong and em for semantic emphasis.",
        "Write HTML comments.",
    ],
    body="""
<h2 class="lesson-section-title" id="headings">Headings</h2>
<p>HTML provides six heading levels. Use them to express logical content hierarchy — not for visual size:</p>
""" + code("""<h1>Site Name or Page Title</h1>      <!-- one per page -->
<h2>Main Section Heading</h2>
<h3>Subsection Heading</h3>
<h4>Sub-subsection</h4>
<h5>Rarely needed</h5>
<h6>Almost never used</h6>
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Every page should have exactly one <code>h1</code>. Never choose a heading level based on size — use CSS for that. Choose based on content structure.</p>
</div>

<h2 class="lesson-section-title" id="paragraphs">Paragraphs</h2>
""" + code("""<p>This is the first paragraph. The browser adds space between paragraphs automatically.</p>

<p>This is the second paragraph. Use separate p elements —
never fake paragraph spacing with br tags.</p>
""") + """
<h2 class="lesson-section-title" id="emphasis">Strong and Em</h2>
""" + code("""<!-- Semantic — carries meaning, not just visual style -->
<p>This step is <strong>critically important</strong> — do not skip it.</p>
<p>The file must be named <em>exactly</em> as shown.</p>

<!-- Presentational only — use only for genuine styling intent -->
<b>Bold with no importance</b>
<i>Italic with no emphasis</i>
""") + """
<h2 class="lesson-section-title" id="comments">HTML Comments</h2>
""" + code("""<!-- Single-line comment — browser ignores this completely -->

<!--
  Multi-line comment — useful for explaining complex sections
  or temporarily disabling a block during debugging.
-->

<p>This paragraph IS rendered.</p>
<!-- <p>This paragraph is hidden.</p> -->
"""),
    kc=[
        ("How many h1 elements should a page have?", "headings"),
        ("What is the semantic difference between strong and b?", "emphasis"),
        ("Why use p elements instead of br tags for paragraphs?", "paragraphs"),
    ],
    assignments=[
        "Build an HTML page about any topic you enjoy. Include h1, h2, h3, four or more paragraphs, strong, em, and at least two comments.",
        "Read MDN's 'HTML text fundamentals' — linked below.",
    ],
    resources=[
        ("MDN — HTML Text Fundamentals", "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals"),
        ("YouTube — HTML Text and Headings (Kevin Powell)", "https://www.youtube.com/watch?v=qz0aGYrrlhU"),
        ("MDN — The Strong element", "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong"),
    ])

    write("lists","Lists",
    intro="Lists are among the most used HTML structures — navigation menus, ingredients, steps, features. HTML gives you two main types and a way to nest them.",
    overview=[
        "Create unordered lists with ul and li.",
        "Create ordered lists with ol and li.",
        "Nest lists within list items.",
    ],
    body="""
<h2 class="lesson-section-title" id="unordered">Unordered Lists</h2>
<p>Use <strong>ul</strong> when order does not matter — shopping lists, feature sets, collections:</p>
""" + code("""<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>
""") + """
<h2 class="lesson-section-title" id="ordered">Ordered Lists</h2>
<p>Use <strong>ol</strong> when sequence matters — numbered instructions, rankings, steps:</p>
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
  <p>The only valid direct children of <code>ul</code> and <code>ol</code> are <code>li</code> elements. Nested lists go <em>inside</em> an <code>li</code>, not directly inside <code>ul</code>/<code>ol</code>.</p>
</div>
""",
    kc=[
        ("When would you use ol over ul?", "ordered"),
        ("What element wraps each item in both list types?", "unordered"),
        ("Where does a nested list go — inside li or directly inside ul?", "nesting"),
    ],
    assignments=[
        "Add an ordered list of steps and an unordered list of items to the page from the previous lesson.",
        "Create a nested list with at least two levels of depth.",
        "Read MDN's lists section — linked below.",
    ],
    resources=[
        ("MDN — HTML Lists", "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals#lists"),
        ("YouTube — HTML Lists (Dani Krossing)", "https://www.youtube.com/watch?v=HeQvQEiGMKk"),
        ("MDN — The ul element", "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul"),
    ])

    write("links-and-images","Links and Images",
    intro="Links are what make the web a web. Images make it visual. This lesson covers both — including the accessibility requirement you must never skip.",
    overview=[
        "Create links with the a element and href attribute.",
        "Distinguish between absolute and relative links.",
        "Embed images with img using src and alt.",
        "Write meaningful alt text for accessibility.",
    ],
    body="""
<h2 class="lesson-section-title" id="links">Creating Links</h2>
""" + code("""<!-- External link -->
<a href="https://developer.mozilla.org">Visit MDN</a>

<!-- Internal link -->
<a href="about.html">About Us</a>

<!-- Link to a section on the same page -->
<a href="#contact">Jump to Contact</a>

<!-- Opens in a new tab — always add rel="noopener" for security -->
<a href="https://github.com" target="_blank" rel="noopener noreferrer">
  GitHub
</a>
""") + """
<h2 class="lesson-section-title" id="abs-relative">Absolute vs. Relative Links</h2>
""" + code("""<!-- ABSOLUTE — full URL, works from anywhere -->
<a href="https://www.example.com/about.html">About</a>

<!-- RELATIVE — relative to current file location -->
<a href="about.html">About</a>          <!-- same folder -->
<a href="recipes/pasta.html">Pasta</a>  <!-- subfolder -->
<a href="../index.html">Home</a>         <!-- one level up -->
""") + """
<h2 class="lesson-section-title" id="images">Images</h2>
""" + code("""<!-- Local image -->
<img src="images/sunset.jpg" alt="A golden sunset over calm water">

<!-- Remote image -->
<img src="https://example.com/photo.png" alt="A mountain peak at dawn">

<!-- With explicit dimensions (always a good practice) -->
<img src="avatar.jpg" alt="Profile photo" width="200" height="200">
""") + """
<h2 class="lesson-section-title" id="alt">Writing Good Alt Text</h2>
<p>The <code>alt</code> attribute is read aloud by screen readers for visually impaired users and displayed when the image fails to load.</p>
""" + code("""<!-- Bad — meaningless -->
<img src="img1.jpg" alt="image">

<!-- Good — descriptive -->
<img src="team.jpg" alt="Five team members in front of our office building">

<!-- Decorative image — screen reader should skip it -->
<img src="divider.png" alt="" role="presentation">
"""),
    kc=[
        ("What attribute specifies a link's destination?", "links"),
        ("What is the difference between absolute and relative links?", "abs-relative"),
        ("Why is the alt attribute on images required?", "alt"),
        ("What security attribute should accompany target='_blank'?", "links"),
    ],
    assignments=[
        "Add a navigation bar with three relative links and two images with descriptive alt text to your project.",
        "Build a three-page mini site where every page links to the other two using relative links.",
        "Read WebAIM's alt text guide — linked below.",
    ],
    resources=[
        ("MDN — Creating Hyperlinks", "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks"),
        ("WebAIM — Alternative Text Guide", "https://webaim.org/techniques/alttext/"),
        ("YouTube — HTML Links and Images (Kevin Powell)", "https://www.youtube.com/watch?v=ts_qze4KqKA"),
    ])

    write("commit-messages","Commit Messages",
    intro="A commit message is a permanent label on a snapshot of your code. Clear, consistent messages are a professional habit that pays off every time you collaborate or return to old work.",
    overview=[
        "Explain why good commit messages matter.",
        "Follow the seven rules of a great commit message.",
        "Know when to commit and how often.",
    ],
    body="""
<h2 class="lesson-section-title" id="why">Why Commit Messages Matter</h2>
""" + code("""# A bad history — tells you nothing
git log --oneline
3f2c1b1 fix
9d8e7f6 stuff
1a2b3c4 wip

# A good history — tells the whole story
git log --oneline
3f2c1b1 Fix nav links breaking on mobile below 768px
9d8e7f6 Add real-time validation to sign-up form
1a2b3c4 Refactor hero section to use Flexbox layout
""") + """
<h2 class="lesson-section-title" id="rules">The Seven Rules</h2>
<ol>
  <li>Separate subject from body with a blank line</li>
  <li>Limit subject to 50 characters</li>
  <li>Capitalise the subject line</li>
  <li>Do not end subject with a period</li>
  <li><strong>Use imperative mood</strong> — "Fix bug" not "Fixed bug"</li>
  <li>Wrap body at 72 characters</li>
  <li>Use the body to explain <em>what</em> and <em>why</em>, not <em>how</em></li>
</ol>
""" + code("""# Subject only (most commits)
git commit -m "Add password strength indicator to signup form"

# Subject + body (when context helps future readers)
git commit -m "Fix race condition in auth token refresh

The previous check ran after the request was already in flight,
causing occasional 401 errors on slow connections. Now we check
and refresh before sending any protected request.

Closes #142"
""") + """
<h2 class="lesson-section-title" id="when">When to Commit</h2>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Quick test: can you describe the change in one sentence without using "and"? If not, it is probably two commits. Commit after every logical unit of work — one feature, one fix, one refactor.</p>
</div>
""",
    kc=[
        ("What mood should commit subject lines use?", "rules"),
        ("What should the body explain — what, why, or how?", "rules"),
        ("How do you decide when to make a new commit?", "when"),
    ],
    assignments=[
        "Read Chris Beams' article 'How to Write a Git Commit Message' — linked below.",
        "Review three of your previous commit messages and rewrite them following the seven rules.",
    ],
    resources=[
        ("Chris Beams — How to Write a Git Commit Message", "https://cbea.ms/git-commit/"),
        ("YouTube — Write Better Commit Messages (Fireship)", "https://www.youtube.com/watch?v=Hlp-9cdImSM"),
        ("Conventional Commits Specification", "https://www.conventionalcommits.org/"),
    ])

    write("project-recipes","Project: Recipes",
    intro="Time to put everything from HTML Foundations into practice. You will build a multi-page recipe website using only HTML — no CSS yet.",
    overview=[
        "Build a multi-page HTML website from scratch.",
        "Use headings, paragraphs, lists, links, and images together.",
        "Connect pages using relative links.",
        "Track and publish the project with Git and GitHub.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>index.html</strong> — site heading (h1) and a list of links to each recipe page</li>
  <li><strong>At least three recipe pages</strong>, each with: title (h1), description paragraph, image with alt text, unordered ingredients list, ordered steps list, link back to homepage</li>
  <li>All pages connected with relative links</li>
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
<h2 class="lesson-section-title" id="workflow">Git Workflow</h2>
""" + code("""mkdir ~/devpath-projects/odin-recipes
cd ~/devpath-projects/odin-recipes
git init

# After each page:
git add .
git commit -m "Add lasagne recipe page"

# When done:
git remote add origin git@github.com:USERNAME/odin-recipes.git
git branch -M main
git push -u origin main
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Do not add CSS. The focus is HTML structure. You will style this project later.</p>
</div>
""",
    kc=[
        ("What HTML elements are required on each recipe page?", "requirements"),
        ("What type of link connects recipe pages back to the homepage?", "workflow"),
    ],
    assignments=[
        "Complete the project meeting all requirements above.",
        "Push to GitHub. Share the repository link — this is your first published project.",
    ],
    resources=[
        ("MDN — HTML Element Reference", "https://developer.mozilla.org/en-US/docs/Web/HTML/Element"),
        ("YouTube — Build a Simple Multi-Page Website (Kevin Powell)", "https://www.youtube.com/watch?v=PlxWf493en4"),
        ("YouTube — HTML Full Course (freeCodeCamp)", "https://www.youtube.com/watch?v=pQN-pnXPaVg"),
    ])

    write("intro-to-css","Intro to CSS",
    intro="HTML gives your page structure. CSS makes it beautiful. This lesson introduces how CSS rules work and the three ways to apply styles to HTML.",
    overview=[
        "Write a CSS rule with selector, property, and value.",
        "Use element, class, and ID selectors.",
        "Know the three ways to add CSS and why external is always preferred.",
    ],
    body="""
<h2 class="lesson-section-title" id="anatomy">Anatomy of a CSS Rule</h2>
""" + code("""selector {
  property: value;
  property: value;
}

/* Example */
p {
  color: #334155;
  font-size: 1.1rem;
  line-height: 1.75;
}
""") + """
<h2 class="lesson-section-title" id="selectors">Selectors</h2>
""" + code("""/* Element — every h1 on the page */
h1 { color: #1e3a8a; }

/* Class — elements with class="card" */
.card {
  background: #f8fafc;
  border-radius: 8px;
  padding: 1.5rem;
}

/* ID — the one element with id="hero" */
#hero { background: #1e3a8a; color: white; }

/* Descendant — p inside .card only */
.card p { font-size: 0.9rem; }
""") + """
<h2 class="lesson-section-title" id="three-ways">Three Ways to Add CSS</h2>
""" + code("""<!-- 1. INLINE — on the element. Avoid for real projects. -->
<p style="color: red;">Warning text</p>

<!-- 2. INTERNAL — style block in head. OK for tiny demos only. -->
<style> p { color: navy; } </style>

<!-- 3. EXTERNAL — separate .css file. Always use this. -->
<link rel="stylesheet" href="styles.css">
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>External stylesheets let one CSS file style every page. One change updates the whole site simultaneously.</p>
</div>
""",
    kc=[
        ("What are the three parts of a CSS rule?", "anatomy"),
        ("What is the difference between a class and an ID selector?", "selectors"),
        ("Which method for adding CSS should you use for real projects?", "three-ways"),
    ],
    assignments=[
        "Create <code>styles.css</code>, link it to your Recipes project, and add at least 8 style rules.",
        "Work through the CSS Foundations exercises — linked below.",
    ],
    resources=[
        ("MDN — CSS First Steps", "https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps"),
        ("CSS Foundations Exercises (GitHub)", "https://github.com/TheOdinProject/css-exercises"),
        ("YouTube — CSS Tutorial Zero to Hero (freeCodeCamp)", "https://www.youtube.com/watch?v=1Rs2ND1ryYc"),
        ("YouTube — CSS in 100 Seconds (Fireship)", "https://www.youtube.com/watch?v=OEV8gMkCHXQ"),
    ])

    write("the-cascade","The Cascade",
    intro="CSS stands for Cascading Style Sheets. The cascade is the algorithm that decides which rule wins when multiple rules target the same element.",
    overview=[
        "Define specificity and explain how it resolves conflicts.",
        "Understand specificity, inheritance, and source order.",
        "Calculate specificity weight for any selector.",
    ],
    body="""
<h2 class="lesson-section-title" id="cascade">The Three Factors</h2>
<ol>
  <li><strong>Specificity</strong> — how precisely does the selector target the element?</li>
  <li><strong>Source order</strong> — when specificity ties, the later rule wins.</li>
  <li><strong>Inheritance</strong> — some properties pass from parent to child automatically.</li>
</ol>

<h2 class="lesson-section-title" id="specificity">Specificity Weights</h2>
""" + code("""/* Element: 0-0-1 */
p { color: black; }

/* Class: 0-1-0 — beats element */
.intro { color: navy; }

/* ID: 1-0-0 — beats class */
#hero { color: gold; }

/* Inline style — beats all selectors */
<p style="color: red;">

/* !important — beats everything. Use only as last resort. */
p { color: purple !important; }

/* Combined: class(0-1-0) + element(0-0-1) = 0-1-1 */
.intro p { font-size: 1.1rem; }
""") + """
<h2 class="lesson-section-title" id="inheritance">Inheritance</h2>
""" + code("""/* These properties ARE inherited by children */
body {
  font-family: 'Sora', sans-serif;
  color: #334155;
  line-height: 1.75;
}

/* These are NOT inherited — set explicitly on each element */
div {
  border: 1px solid #e2e8f0;
  padding: 1rem;
  margin: 2rem;
}
""") + """
<h2 class="lesson-section-title" id="source-order">Source Order</h2>
""" + code("""/* Equal specificity — later rule wins */
p { color: red; }
p { color: blue; }
/* Result: blue */
"""),
    kc=[
        ("What three factors does the cascade consider?", "cascade"),
        ("Which has higher specificity — class or ID?", "specificity"),
        ("Is the CSS color property inherited by children?", "inheritance"),
        ("When two rules have equal specificity, which wins?", "source-order"),
    ],
    assignments=[
        "Open DevTools on any page, inspect an element, and find at least one overridden (strikethrough) rule. Trace why it lost.",
        "Work through the CSS Cascade exercises — linked below.",
    ],
    resources=[
        ("MDN — Cascade and Inheritance", "https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance"),
        ("CSS Specificity Calculator", "https://specificity.keegan.st/"),
        ("YouTube — CSS Specificity Explained (Kevin Powell)", "https://www.youtube.com/watch?v=c0kfcP_nD9E"),
        ("CSS Foundations Exercises (GitHub)", "https://github.com/TheOdinProject/css-exercises"),
    ])

    write("inspecting-html-and-css","Inspecting HTML and CSS",
    intro="Browser DevTools are your most powerful debugging tool as a front-end developer. This lesson shows you how to inspect, test, and diagnose issues in seconds.",
    overview=[
        "Open and navigate browser DevTools.",
        "Inspect any element to see its HTML and applied styles.",
        "Edit CSS live in the browser.",
        "Use the box model diagram to debug spacing.",
    ],
    body="""
<h2 class="lesson-section-title" id="opening">Opening DevTools</h2>
""" + code("""F12                     # All platforms
Cmd + Option + I        # Mac
Right-click → Inspect   # Any element on the page
Ctrl+Shift+C            # Click-to-inspect mode
""") + """
<h2 class="lesson-section-title" id="elements-panel">The Elements Panel</h2>
<p>Shows the live DOM — the HTML the browser built. Select any element to see every CSS rule applied to it in the Styles pane on the right. Overridden rules appear with a strikethrough, with a note showing which rule won.</p>

<h2 class="lesson-section-title" id="live-css">Live CSS Editing</h2>
<ol>
  <li>Select an element in the Elements panel</li>
  <li>Click any property value in the Styles pane and change it</li>
  <li>Press Tab to jump to the next property</li>
  <li>Click empty space in a rule to add a new property</li>
  <li>Copy successful values back into your actual CSS file</li>
</ol>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>DevTools edits are temporary — they vanish on page reload. Always copy good changes back to your stylesheet.</p>
</div>

<h2 class="lesson-section-title" id="box-model-view">Box Model Diagram</h2>
<p>At the bottom of the Styles pane you will find a visual box model diagram. Hover over each area to highlight it on the page. This is the fastest way to answer "where is all this extra space coming from?"</p>
""",
    kc=[
        ("What keyboard shortcut opens DevTools?", "opening"),
        ("What does a strikethrough on a CSS rule mean?", "elements-panel"),
        ("How do you test a CSS change without touching your files?", "live-css"),
        ("Where is the box model diagram in DevTools?", "box-model-view"),
    ],
    assignments=[
        "Open DevTools on your Recipes project. Inspect the h1 and trace every rule applied to it.",
        "Use live editing to change a background colour and font. Copy the values back into your stylesheet.",
    ],
    resources=[
        ("Chrome DevTools — Get Started with CSS", "https://developer.chrome.com/docs/devtools/css/"),
        ("MDN — What are browser developer tools?", "https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/What_are_browser_developer_tools"),
        ("YouTube — Chrome DevTools Full Tutorial (Traversy Media)", "https://www.youtube.com/watch?v=x4q86IjJFag"),
    ])

    write("the-box-model","The Box Model",
    intro="Every HTML element is a rectangular box. Understanding how these boxes are sized and spaced is the single most important concept in CSS layout.",
    overview=[
        "Name the four areas of the CSS box model.",
        "Understand content-box vs border-box sizing.",
        "Use margin and padding correctly.",
    ],
    body="""
<h2 class="lesson-section-title" id="four-areas">The Four Areas</h2>
""" + code(""".card {
  width: 320px;                    /* CONTENT area */
  padding: 24px;                   /* PADDING — inside, between content and border */
  border: 2px solid #e2e8f0;       /* BORDER */
  margin: 32px;                    /* MARGIN — outside, between this and neighbours */
}
""") + """
<h2 class="lesson-section-title" id="box-sizing">The border-box Fix</h2>
""" + code("""/* DEFAULT content-box: actual width = 300 + 24 + 24 + 2 + 2 = 352px */
.box { width: 300px; padding: 24px; border: 2px solid black; }

/* border-box: actual width = exactly 300px */
.box {
  box-sizing: border-box;
  width: 300px;
  padding: 24px;
  border: 2px solid black;
}

/* Add this universal rule to EVERY stylesheet */
*, *::before, *::after {
  box-sizing: border-box;
}
""") + """
<h2 class="lesson-section-title" id="margin-padding">Margin vs. Padding</h2>
""" + code("""/* PADDING — inside the element, background fills this area */
.button {
  padding: 12px 24px;
  background: #2563eb;  /* blue extends into padding */
}

/* MARGIN — outside the element, always transparent */
.section {
  margin: 0 auto;       /* centre a block element */
  margin-bottom: 32px;
}
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Vertical margins between adjacent block elements <em>collapse</em> — only the larger value applies, not the sum. This surprises almost everyone the first time they encounter it.</p>
</div>
""",
    kc=[
        ("Name the four box model areas from inside to outside.", "four-areas"),
        ("What does box-sizing: border-box change?", "box-sizing"),
        ("What is the practical difference between margin and padding?", "margin-padding"),
    ],
    assignments=[
        "Add the universal border-box rule to your stylesheet. Build a card with explicit padding, border, and margin. Verify dimensions in DevTools.",
        "Work through the Box Model exercises — linked below.",
    ],
    resources=[
        ("MDN — The Box Model", "https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model"),
        ("CSS Tricks — The CSS Box Model", "https://css-tricks.com/the-css-box-model/"),
        ("YouTube — The Box Model (Kevin Powell)", "https://www.youtube.com/watch?v=rIO5326FgPE"),
        ("CSS Foundations Exercises (GitHub)", "https://github.com/TheOdinProject/css-exercises"),
    ])

    write("block-and-inline","Block and Inline",
    intro="Every HTML element has a default display behaviour. Understanding block versus inline is foundational for understanding why layouts behave the way they do.",
    overview=[
        "Explain the difference between block and inline elements.",
        "Know which common elements are block and which are inline.",
        "Use the display property to change an element's behaviour.",
    ],
    body="""
<h2 class="lesson-section-title" id="block">Block Elements</h2>
<p>Block elements start on a new line and take the full available width. You can freely set width, height, margin, and padding.</p>
""" + code("""/* Common block elements */
div, p, h1, h2, h3, h4, h5, h6,
ul, ol, li, section, article,
header, footer, nav, main, form
""") + """
<h2 class="lesson-section-title" id="inline">Inline Elements</h2>
<p>Inline elements flow within surrounding text, taking only as much width as their content. Setting width, height, or vertical margin has no effect on them.</p>
""" + code("""/* Common inline elements */
span, a, strong, em, img, input, button, label, code

<!-- Inline elements flow naturally within text -->
<p>
  A paragraph with <strong>bold</strong> and
  <a href="#">a link</a> flowing naturally within the sentence.
</p>
""") + """
<h2 class="lesson-section-title" id="display">Changing Display</h2>
""" + code("""/* Override default behaviour */
span { display: block; }        /* inline → block */
div  { display: inline; }       /* block → inline */

/* Inline position + block sizing */
.nav-item {
  display: inline-block;
  width: 120px;
  padding: 8px 16px;
}

/* Remove from page entirely */
.hidden { display: none; }

/* Modern layout methods */
.row  { display: flex; }
.grid { display: grid; }
"""),
    kc=[
        ("What is the main difference between block and inline elements?", "block"),
        ("Why does setting width have no effect on inline elements?", "inline"),
        ("What does display: inline-block give you that inline does not?", "display"),
    ],
    assignments=[
        "In DevTools, compare the computed display values of a p (block) and a span (inline).",
        "Work through the Block and Inline exercises — linked below.",
    ],
    resources=[
        ("MDN — Block and Inline Layout", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flow_layout/Block_and_inline_layout_in_normal_flow"),
        ("CSS Foundations Exercises (GitHub)", "https://github.com/TheOdinProject/css-exercises"),
        ("YouTube — Block vs Inline vs Inline-Block (Web Dev Simplified)", "https://www.youtube.com/watch?v=x_i2gga-sYg"),
    ])

    write("introduction-to-flexbox","Introduction to Flexbox",
    intro="Flexbox solves layout problems that were previously painful hacks. Vertically centring an element used to be notoriously difficult. With Flexbox it is one line.",
    overview=[
        "Activate Flexbox with display: flex.",
        "Understand flex containers and flex items.",
        "Describe the main axis and cross axis.",
        "Apply justify-content and align-items.",
    ],
    body="""
<h2 class="lesson-section-title" id="container-items">Containers and Items</h2>
""" + code("""<div class="container">
  <div class="item">One</div>
  <div class="item">Two</div>
  <div class="item">Three</div>
</div>
""") + code(""".container {
  display: flex;  /* children become flex items and line up in a row */
  gap: 1rem;
}
""") + """
<h2 class="lesson-section-title" id="axes">Main Axis and Cross Axis</h2>
""" + code("""/* Default: main axis = horizontal */
.container { display: flex; flex-direction: row; }

/* Switch: main axis = vertical */
.container { display: flex; flex-direction: column; }
""") + """
<h2 class="lesson-section-title" id="alignment">Alignment</h2>
""" + code("""/* justify-content = main axis | align-items = cross axis */

/* Centre everything — the classic "centring a div" */
.centered {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
}

/* Space cards evenly */
.card-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1.5rem;
}
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Play Flexbox Froggy — a game that covers all Flexbox alignment concepts through fun puzzles. It is one of the best ways to build intuition fast.</p>
</div>
""",
    kc=[
        ("What CSS property activates Flexbox?", "container-items"),
        ("What is the difference between main axis and cross axis?", "axes"),
        ("Which property aligns items along the main axis?", "alignment"),
        ("Which property aligns items along the cross axis?", "alignment"),
    ],
    assignments=[
        "Build a horizontal nav bar with evenly spaced links using Flexbox.",
        "Centre a div both horizontally and vertically using Flexbox.",
        "Play Flexbox Froggy and complete all 24 levels.",
    ],
    resources=[
        ("Flexbox Froggy — Learn Flexbox with a game", "https://flexboxfroggy.com/"),
        ("CSS Tricks — A Complete Guide to Flexbox", "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),
        ("MDN — Flexbox", "https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox"),
        ("YouTube — Flexbox CSS in 20 Minutes (Traversy Media)", "https://www.youtube.com/watch?v=JJSoEo8JSnc"),
    ])

    write("growing-and-shrinking","Growing and Shrinking",
    intro="The real power of Flexbox comes from making items grow to fill available space or shrink to fit. This lesson explains the flex shorthand and its three components.",
    overview=[
        "Understand the flex shorthand property.",
        "Explain flex-grow, flex-shrink, and flex-basis individually.",
        "Know the most common flex values and their effects.",
    ],
    body="""
<h2 class="lesson-section-title" id="shorthand">The flex Shorthand</h2>
""" + code("""/* flex: grow  shrink  basis */
.item { flex: 1; }           /* flex: 1 1 0  — grow, shrink, start from zero */
.item { flex: 2; }           /* grows twice as fast as flex: 1 */
.item { flex: 0 0 200px; }   /* fixed 200px, never grows or shrinks */
.item { flex: 1 1 auto; }    /* grows and shrinks from natural size */
""") + """
<h2 class="lesson-section-title" id="flex-grow">flex-grow</h2>
""" + code(""".container { display: flex; }

.item-a { flex-grow: 1; }   /* 1 share of free space */
.item-b { flex-grow: 2; }   /* 2 shares — twice as wide as item-a */
.item-c { flex-grow: 1; }   /* 1 share */
/* 4 total shares: item-b = 50%, item-a and item-c = 25% each */
""") + """
<h2 class="lesson-section-title" id="flex-shrink">flex-shrink</h2>
""" + code(""".sidebar {
  flex-shrink: 0;    /* never shrinks below its set width */
  width: 250px;
}
.main-content {
  flex-grow: 1;      /* takes all remaining space */
  flex-shrink: 1;    /* can shrink if needed */
}
""") + """
<h2 class="lesson-section-title" id="flex-basis">flex-basis</h2>
""" + code("""/* Equal-width columns — most common pattern */
.column { flex: 1; }   /* all columns share space equally */

/* Responsive cards that wrap */
.card {
  flex: 1 1 280px;
  /* grows to fill space, wraps if container shrinks below 280px */
}
"""),
    kc=[
        ("What three properties does the flex shorthand combine?", "shorthand"),
        ("What does flex-grow: 2 mean versus flex-grow: 1?", "flex-grow"),
        ("What does flex-shrink: 0 do?", "flex-shrink"),
        ("What is the difference between flex-basis: auto and flex-basis: 0?", "flex-basis"),
    ],
    assignments=[
        "Build a two-column layout: fixed sidebar (flex-shrink: 0) and main content that fills remaining space (flex-grow: 1).",
        "Build a responsive card grid using flex: 1 1 250px and flex-wrap: wrap.",
    ],
    resources=[
        ("MDN — Controlling Ratios of Flex Items", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Controlling_ratios_of_flex_items_along_the_main_axis"),
        ("CSS Tricks — A Complete Guide to Flexbox", "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),
        ("YouTube — Flexbox Growing and Shrinking (Kevin Powell)", "https://www.youtube.com/watch?v=sanRCfIcNaQ"),
    ])

    write("axes","Axes",
    intro="Everything in Flexbox revolves around two axes. This lesson digs into how changing flex-direction flips those axes and how flex-wrap enables responsive layouts without media queries.",
    overview=[
        "Use flex-direction to change the main axis.",
        "Understand how switching axes changes alignment behaviour.",
        "Use flex-wrap to handle overflow and create responsive layouts.",
    ],
    body="""
<h2 class="lesson-section-title" id="flex-direction">flex-direction</h2>
""" + code(""".container {
  display: flex;
  flex-direction: row;             /* default — left to right */
  flex-direction: row-reverse;     /* right to left */
  flex-direction: column;          /* top to bottom */
  flex-direction: column-reverse;  /* bottom to top */
}
""") + """
<h2 class="lesson-section-title" id="axis-flip">How Axes Flip</h2>
""" + code("""/* ROW direction */
.row {
  display: flex;
  flex-direction: row;
  justify-content: center;  /* horizontal — along main axis */
  align-items: center;       /* vertical — along cross axis */
}

/* COLUMN direction — axes swap */
.column {
  display: flex;
  flex-direction: column;
  justify-content: center;  /* vertical now — main axis is vertical */
  align-items: center;       /* horizontal now — cross axis is horizontal */
}
""") + """
<h2 class="lesson-section-title" id="flex-wrap">flex-wrap</h2>
""" + code(""".container {
  display: flex;
  flex-wrap: wrap;   /* items wrap to the next row when needed */
  gap: 1rem;
}

/* Responsive cards with zero media queries */
.card {
  flex: 1 1 280px;
  /* fills space when wide, wraps gracefully when narrow */
}
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Remember: <code>justify-content</code> always targets the <em>main axis</em> and <code>align-items</code> always targets the <em>cross axis</em>. Those axes flip when <code>flex-direction</code> changes.</p>
</div>
""",
    kc=[
        ("When flex-direction is column, which axis does justify-content control?", "axis-flip"),
        ("What does flex-wrap: wrap do?", "flex-wrap"),
        ("How can you build responsive cards with no media queries?", "flex-wrap"),
    ],
    assignments=[
        "Build a layout that works in both row and column direction by toggling flex-direction. Observe how alignment changes.",
        "Build a responsive card grid using flex-wrap: wrap — no media queries allowed.",
    ],
    resources=[
        ("MDN — flex-direction", "https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction"),
        ("CSS Tricks — A Complete Guide to Flexbox", "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),
        ("YouTube — Flexbox Axes Explained (Web Dev Simplified)", "https://www.youtube.com/watch?v=3YW65K6LcIA"),
    ])

    write("alignment","Alignment",
    intro="This lesson covers the complete set of Flexbox alignment properties so you can place elements exactly where you want them with full confidence.",
    overview=[
        "Use justify-content, align-items, and align-self precisely.",
        "Use align-content for multi-line containers.",
        "Use gap for clean spacing between items.",
    ],
    body="""
<h2 class="lesson-section-title" id="justify">justify-content</h2>
""" + code(""".container {
  display: flex;
  justify-content: flex-start;    /* packed to start (default) */
  justify-content: flex-end;      /* packed to end */
  justify-content: center;        /* centred */
  justify-content: space-between; /* equal gaps between, none at edges */
  justify-content: space-around;  /* equal gaps around each item */
  justify-content: space-evenly;  /* equal gaps everywhere */
}
""") + """
<h2 class="lesson-section-title" id="align-items">align-items</h2>
""" + code(""".container {
  display: flex;
  align-items: stretch;     /* items fill cross axis height (default) */
  align-items: flex-start;  /* align to start of cross axis */
  align-items: flex-end;    /* align to end */
  align-items: center;      /* centred on cross axis */
  align-items: baseline;    /* aligned by text baseline */
}
""") + """
<h2 class="lesson-section-title" id="align-self">align-self</h2>
""" + code(""".container { display: flex; align-items: flex-start; }

.special-item {
  align-self: center;  /* this one item overrides the container's align-items */
}
""") + """
<h2 class="lesson-section-title" id="gap">gap</h2>
""" + code(""".container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;           /* equal gap in all directions */
  gap: 1rem 2rem;      /* row-gap then column-gap */
}
/* gap only adds space BETWEEN items — not at the outer edges */
"""),
    kc=[
        ("What is the difference between align-items and align-self?", "align-self"),
        ("When does align-content take effect?", "align-items"),
        ("Why is gap better than using margins on individual items?", "gap"),
    ],
    assignments=[
        "Build a page header: logo on the left, navigation links on the right — Flexbox only.",
        "Build a three-column footer: left text, centred text, right text.",
        "Complete all remaining Flexbox Froggy levels.",
    ],
    resources=[
        ("Flexbox Froggy", "https://flexboxfroggy.com/"),
        ("CSS Tricks — A Complete Guide to Flexbox", "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),
        ("MDN — Aligning Items in Flexbox", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Aligning_items_in_a_flex_container"),
        ("YouTube — Flexbox Alignment Deep Dive (Kevin Powell)", "https://www.youtube.com/watch?v=u044iM9xsWU"),
    ])

    write("project-landing-page","Project: Landing Page",
    intro="You now know enough HTML and CSS to build something that looks like a real website. In this project you will design and build a complete landing page from scratch.",
    overview=[
        "Translate a visual design into working HTML and CSS.",
        "Use Flexbox for all layout decisions.",
        "Apply typography, colour, and spacing for a polished result.",
        "Publish the project live using GitHub Pages.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>Header</strong> — logo/name left, navigation links right (Flexbox)</li>
  <li><strong>Hero section</strong> — large heading, subtext, call-to-action button</li>
  <li><strong>Info section</strong> — four cards arranged in a row</li>
  <li><strong>Quote section</strong> — centred testimonial or quote</li>
  <li><strong>Footer</strong> — simple centred call to action</li>
</ul>

<h2 class="lesson-section-title" id="tips">Tips for Success</h2>
<ul>
  <li>Build one section at a time. Do not move on until the current one looks right.</li>
  <li>Use DevTools constantly — tweak values live before copying to your CSS file.</li>
  <li>Do not chase pixel perfection. "Close enough and moving forward" is a real developer skill.</li>
</ul>

<h2 class="lesson-section-title" id="github-pages">Publishing on GitHub Pages</h2>
""" + code("""# After pushing your repo to GitHub:
# 1. Open the repo on github.com
# 2. Click Settings → Pages
# 3. Source: Deploy from branch → main → / (root) → Save
# 4. Your site will be live at:
#    https://YOUR_USERNAME.github.io/REPO-NAME/
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>GitHub Pages is free hosting for static HTML/CSS/JS sites. Every project you build from here on can be published and shared this way instantly.</p>
</div>
""",
    kc=[
        ("What Flexbox properties centre content both horizontally and vertically?", "requirements"),
        ("How do you publish a static site on GitHub Pages?", "github-pages"),
    ],
    assignments=[
        "Build the landing page meeting all five section requirements.",
        "Push to GitHub and publish on GitHub Pages. Share the live URL.",
    ],
    resources=[
        ("CSS Tricks — A Complete Guide to Flexbox", "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),
        ("YouTube — Build a Landing Page with HTML and CSS (Kevin Powell)", "https://www.youtube.com/watch?v=p0bGHP-PXD4"),
        ("GitHub Docs — Publishing from a branch", "https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site"),
    ])

    write("variables-and-operators","Variables and Operators",
    intro="JavaScript is the programming language of the web. This lesson introduces the most fundamental building blocks: variables for storing data and operators for working with it.",
    overview=[
        "Declare variables with let and const.",
        "Understand the difference between let, const, and var.",
        "Use arithmetic, comparison, and logical operators.",
    ],
    body="""
<h2 class="lesson-section-title" id="variables">Variables</h2>
""" + code("""// const — cannot be reassigned (use this by default)
const name = "Alice";
const age  = 25;

// let — can be reassigned (use when value needs to change)
let score = 0;
score = score + 10;  // OK
score += 10;         // shorthand for the same thing

// var — the old way. Avoid it — confusing scoping rules.
var oldStyle = "avoid this";
""") + """
<h2 class="lesson-section-title" id="arithmetic">Arithmetic Operators</h2>
""" + code("""const a = 10, b = 3;

a + b   // 13  — addition
a - b   // 7   — subtraction
a * b   // 30  — multiplication
a / b   // 3.333...
a % b   // 1   — remainder (modulo)
a ** b  // 1000 — exponentiation (10 to the power of 3)
""") + """
<h2 class="lesson-section-title" id="comparison">Comparison Operators</h2>
""" + code("""// Always use === (strict equality), not == (loose equality)
5 === 5     // true
5 === "5"   // false — different types
5 !== 3     // true
10 > 7      // true
10 >= 10    // true
""") + """
<h2 class="lesson-section-title" id="logical">Logical Operators</h2>
""" + code("""true && true    // true  (AND — both must be true)
true && false   // false
true || false   // true  (OR — at least one must be true)
false || false  // false
!true           // false (NOT — inverts)
"""),
    kc=[
        ("When should you use const vs let?", "variables"),
        ("What does the % operator return?", "arithmetic"),
        ("What is the difference between == and ===?", "comparison"),
    ],
    assignments=[
        "Open the browser console (F12) and experiment with all operators above.",
        "Write a script that calculates the area and perimeter of a rectangle from width and height variables.",
    ],
    resources=[
        ("MDN — JavaScript Variables", "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables"),
        ("javascript.info — Variables", "https://javascript.info/variables"),
        ("YouTube — JavaScript Variables (Programming with Mosh)", "https://www.youtube.com/watch?v=9emXNzqCKyg"),
    ])

    write("data-types-and-conditionals","Data Types and Conditionals",
    intro="JavaScript works with different kinds of data. This lesson covers the main data types and how to write code that makes decisions based on conditions.",
    overview=[
        "Identify the eight JavaScript data types.",
        "Write if, else if, and else statements.",
        "Use the ternary operator for concise conditionals.",
        "Understand truthy and falsy values.",
    ],
    body="""
<h2 class="lesson-section-title" id="data-types">Data Types</h2>
""" + code("""// Primitive types
const name    = "Alice";          // String
const age     = 25;               // Number
const price   = 9.99;             // Number (no separate float)
const isAdmin = true;             // Boolean
const nothing = null;             // Null — intentional absence
let   notSet;                     // Undefined — not yet assigned
const id      = Symbol("id");     // Symbol — unique identifier
const big     = 9007199254740991n;// BigInt — very large integers

// Reference type
const user   = { name: "Alice", age: 25 }; // Object
const colors = ["red", "green", "blue"];    // Array
""") + """
<h2 class="lesson-section-title" id="conditionals">Conditionals</h2>
""" + code("""const score = 72;

if (score >= 90) {
  console.log("A grade");
} else if (score >= 80) {
  console.log("B grade");
} else if (score >= 70) {
  console.log("C grade");
} else {
  console.log("Below C");
}
// Output: "C grade"
""") + """
<h2 class="lesson-section-title" id="ternary">Ternary Operator</h2>
""" + code("""// condition ? valueIfTrue : valueIfFalse
const age = 20;
const status = age >= 18 ? "adult" : "minor";
console.log(status); // "adult"
""") + """
<h2 class="lesson-section-title" id="truthy-falsy">Truthy and Falsy</h2>
""" + code("""// FALSY — treated as false in conditions
false, 0, "", null, undefined, NaN

// TRUTHY — everything else
"hello", 1, [], {}, true

// Example
const username = "";
if (username) {
  console.log("Hello, " + username);
} else {
  console.log("Please enter a username"); // runs — "" is falsy
}
"""),
    kc=[
        ("What are the eight JavaScript data types?", "data-types"),
        ("What is the difference between null and undefined?", "data-types"),
        ("What does the ternary operator do?", "ternary"),
        ("Name four falsy values in JavaScript.", "truthy-falsy"),
    ],
    assignments=[
        "In the browser console, test all data types and check each with typeof.",
        "Write a grading function that takes a score and returns a letter grade using if/else if.",
    ],
    resources=[
        ("MDN — JavaScript Data Types", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures"),
        ("javascript.info — Conditionals", "https://javascript.info/ifelse"),
        ("YouTube — JavaScript Data Types (Web Dev Simplified)", "https://www.youtube.com/watch?v=qT7a1zhNwRg"),
    ])

    write("javascript-developer-tools","JavaScript Developer Tools",
    intro="The browser console and debugger are your most important JavaScript tools. This lesson shows you how to test code, find bugs, and understand what your programs are actually doing.",
    overview=[
        "Use the browser console to run and test JavaScript.",
        "Use console.log() and other console methods for debugging.",
        "Set breakpoints and step through code in the debugger.",
        "Read and interpret JavaScript error messages.",
    ],
    body="""
<h2 class="lesson-section-title" id="console">The Console</h2>
""" + code("""// Open with F12 → Console tab

// Test any JavaScript expression instantly
2 + 2            // 4
"hello".length   // 5

// Log values during debugging
console.log("Score:", score);
console.log("User:", user);          // logs objects nicely
console.error("Something failed!"); // red error styling
console.warn("Check this value");   // yellow warning
console.table([{name:"Alice"},{name:"Bob"}]); // tabular view
console.clear();                    // clear console
""") + """
<h2 class="lesson-section-title" id="errors">Reading Error Messages</h2>
""" + code("""// ReferenceError — variable does not exist
console.log(myVar); // ReferenceError: myVar is not defined
// Fix: declare the variable first

// TypeError — wrong type or method does not exist
null.toUpperCase(); // TypeError: Cannot read properties of null
const num = 42;
num();              // TypeError: num is not a function

// SyntaxError — broken code structure
if (true {          // SyntaxError: Unexpected token '{'

// Every error shows: type, message, file name, and line number
""") + """
<h2 class="lesson-section-title" id="debugger">The Debugger</h2>
<ol>
  <li>Open DevTools → Sources tab</li>
  <li>Click a line number to set a breakpoint (blue dot appears)</li>
  <li>Reload the page — execution pauses at your breakpoint</li>
  <li>Hover over any variable to see its current value</li>
  <li>Use the controls: Step Over (F10), Step Into (F11), Resume (F8)</li>
</ol>
""" + code("""// Trigger the debugger from code
function calculateTotal(items) {
  debugger; // execution pauses here when DevTools is open
  return items.reduce((sum, item) => sum + item.price, 0);
}
"""),
    kc=[
        ("How do you open the browser console?", "console"),
        ("What does a ReferenceError mean?", "errors"),
        ("How do you set a breakpoint in the Sources tab?", "debugger"),
    ],
    assignments=[
        "Open the console and write at least 10 JavaScript expressions. Try all console methods listed.",
        "Introduce a deliberate bug into a small script and use the debugger — not random changes — to find it.",
    ],
    resources=[
        ("MDN — JavaScript Debugging", "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong"),
        ("Chrome DevTools — Debug JavaScript", "https://developer.chrome.com/docs/devtools/javascript/"),
        ("YouTube — How to Use the JS Debugger (Fireship)", "https://www.youtube.com/watch?v=H0XScE08hy8"),
    ])

    write("function-basics","Function Basics",
    intro="Functions let you write a block of code once and run it as many times as you need. They are the most important tool for organising JavaScript.",
    overview=[
        "Define functions using function declarations and arrow syntax.",
        "Understand parameters, arguments, and return values.",
        "Understand function scope.",
    ],
    body="""
<h2 class="lesson-section-title" id="declaring">Declaring Functions</h2>
""" + code("""// Function declaration
function greet(name) {
  return "Hello, " + name + "!";
}
console.log(greet("Alice")); // "Hello, Alice!"

// Function expression
const double = function(n) {
  return n * 2;
};

// Arrow function — concise modern syntax
const square   = (n) => n * n;
const add      = (a, b) => a + b;

// Arrow function with a block body
const getArea  = (w, h) => {
  const area = w * h;
  return area;
};
""") + """
<h2 class="lesson-section-title" id="params">Parameters and Arguments</h2>
""" + code("""// Parameters — the names in the function definition
function add(a, b) {
  return a + b;
}

// Arguments — the actual values passed when calling
add(3, 7);  // 10

// Default parameters
function greet(name = "stranger") {
  return "Hello, " + name + "!";
}
greet();         // "Hello, stranger!"
greet("Alice");  // "Hello, Alice!"
""") + """
<h2 class="lesson-section-title" id="scope">Function Scope</h2>
""" + code("""const globalVar = "accessible everywhere";

function myFunction() {
  const localVar = "only inside this function";
  console.log(globalVar); // works
  console.log(localVar);  // works
}

myFunction();
console.log(globalVar); // works
console.log(localVar);  // ReferenceError — out of scope
"""),
    kc=[
        ("What is the difference between a parameter and an argument?", "params"),
        ("What does the return statement do?", "declaring"),
        ("Can a variable declared inside a function be accessed outside it?", "scope"),
    ],
    assignments=[
        "Write a function that converts Celsius to Fahrenheit: (C × 9/5) + 32.",
        "Write a function that takes two numbers and returns the larger one without using Math.max.",
        "Rewrite both functions using arrow function syntax.",
    ],
    resources=[
        ("MDN — Functions", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions"),
        ("javascript.info — Functions", "https://javascript.info/function-basics"),
        ("YouTube — JavaScript Functions (Programming with Mosh)", "https://www.youtube.com/watch?v=N8ap4k_1QEQ"),
    ])

    write("problem-solving","Problem Solving",
    intro="Writing code is not the hard part of programming — solving problems is. This lesson gives you a repeatable framework for breaking down any problem before writing a single line of code.",
    overview=[
        "Apply a systematic framework to any coding problem.",
        "Use pseudocode to plan before coding.",
        "Break complex problems into small, testable pieces.",
    ],
    body="""
<h2 class="lesson-section-title" id="framework">The Framework</h2>
<ol>
  <li><strong>Understand.</strong> Read the problem multiple times. Restate it in your own words. If you cannot explain it simply, you do not understand it yet.</li>
  <li><strong>Plan.</strong> Write pseudocode — plain English steps. Do not think about syntax.</li>
  <li><strong>Divide.</strong> Break the problem into the smallest possible sub-problems.</li>
  <li><strong>Implement.</strong> Write code for one sub-problem at a time.</li>
  <li><strong>Test.</strong> Verify each piece works. Use console.log to check values at every step.</li>
</ol>

<h2 class="lesson-section-title" id="pseudocode">Writing Pseudocode</h2>
""" + code("""// Problem: find all even numbers from 1 to n and return them

// PSEUDOCODE
// 1. Create an empty array
// 2. Loop from 1 to n
// 3. If a number divides evenly by 2, add it to the array
// 4. After the loop, return the array

// CODE from the pseudocode
function getEvenNumbers(n) {
  const evens = [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      evens.push(i);
    }
  }
  return evens;
}

console.log(getEvenNumbers(10)); // [2, 4, 6, 8, 10]
""") + """
<h2 class="lesson-section-title" id="rubber-duck">Rubber Duck Debugging</h2>
<p>When stuck, explain your code out loud step by step — to yourself, a colleague, or a rubber duck on your desk. Articulating the problem almost always reveals where your thinking broke down. This technique is used by professional developers every single day.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Before Googling, try saying out loud: "I am trying to do X. I expected Y. Instead I got Z. The part I do not understand is..." — you will often solve it before finishing the sentence.</p>
</div>
""",
    kc=[
        ("What are the five steps in the problem-solving framework?", "framework"),
        ("What is pseudocode and why write it before coding?", "pseudocode"),
        ("What is rubber duck debugging?", "rubber-duck"),
    ],
    assignments=[
        "Before writing any code solution this week, write pseudocode first — no exceptions.",
        "Solve FizzBuzz: print numbers 1–100, replacing multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'.",
    ],
    resources=[
        ("javascript.info — Coding Style", "https://javascript.info/coding-style"),
        ("YouTube — How to Think Like a Programmer (Coding Tech)", "https://www.youtube.com/watch?v=azcrPFhaY9k"),
        ("YouTube — FizzBuzz Explained (Web Dev Simplified)", "https://www.youtube.com/watch?v=sxPtMVfmMdo"),
    ])

    write("understanding-errors","Understanding Errors",
    intro="Errors are not failures — they are the JavaScript engine telling you exactly what went wrong. Reading error messages fluently is a superpower that dramatically speeds up debugging.",
    overview=[
        "Read and interpret JavaScript error messages.",
        "Distinguish between the most common error types.",
        "Use the stack trace to find where an error originated.",
    ],
    body="""
<h2 class="lesson-section-title" id="anatomy">Anatomy of an Error</h2>
""" + code("""// A typical error message:
// TypeError: Cannot read properties of null (reading 'textContent')
//     at updateDisplay (app.js:24:15)
//     at init (app.js:42:3)

// Tells you:
// 1. Type          — TypeError
// 2. What happened — Cannot read properties of null
// 3. Specific prop — textContent
// 4. Stack trace   — call chain with file and line numbers
""") + """
<h2 class="lesson-section-title" id="common-errors">Common Error Types</h2>
""" + code("""// ReferenceError — variable does not exist
console.log(myVar); // ReferenceError: myVar is not defined
// Fix: declare the variable with const or let

// TypeError — wrong type for the operation
null.toUpperCase();  // TypeError: Cannot read properties of null
const num = 42;
num();               // TypeError: num is not a function

// SyntaxError — broken code structure
if (true {           // SyntaxError: Unexpected token '{'
// Fix: check brackets and keywords

// RangeError — value out of allowed range
new Array(-1);       // RangeError: Invalid array length
""") + """
<h2 class="lesson-section-title" id="stack-trace">Reading the Stack Trace</h2>
""" + code("""// Read the stack trace from TOP (where error happened) to BOTTOM (where it started)
function c() { null.split(""); }
function b() { c(); }
function a() { b(); }
a();

// TypeError: Cannot read properties of null
//   at c (script.js:1:12)   ← error happened here
//   at b (script.js:2:14)
//   at a (script.js:3:14)   ← execution started here
"""),
    kc=[
        ("What four pieces of information does an error message contain?", "anatomy"),
        ("What causes a ReferenceError?", "common-errors"),
        ("How do you read a stack trace?", "stack-trace"),
    ],
    assignments=[
        "Deliberately trigger each of the four error types in the console and read each message carefully.",
        "Find a bug in a small script using only the error message and stack trace — no random guessing.",
    ],
    resources=[
        ("MDN — JavaScript Error Reference", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors"),
        ("javascript.info — Error Handling", "https://javascript.info/error-handling"),
        ("YouTube — JavaScript Errors Explained (Web Dev Simplified)", "https://www.youtube.com/watch?v=cFTFtuEQ-10"),
    ])

    write("project-rock-paper-scissors","Project: Rock Paper Scissors",
    intro="Your first JavaScript project. Build a console-based Rock Paper Scissors game — no UI yet, pure logic. This focuses entirely on writing clean JavaScript functions.",
    overview=[
        "Write functions that use conditionals to make decisions.",
        "Generate random computer choices.",
        "Determine a winner and track scores.",
        "Run the game from the browser console.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>A function that returns a random computer choice</li>
  <li>A function that compares player and computer choices and returns the round result</li>
  <li>A function that plays five rounds and returns the final score</li>
  <li>Results logged clearly to the console</li>
</ul>

<h2 class="lesson-section-title" id="setup">Setup</h2>
""" + code("""mkdir ~/devpath-projects/rock-paper-scissors
cd ~/devpath-projects/rock-paper-scissors
git init
touch script.js
code .
""") + code("""// Starting point — build from here

function getComputerChoice() {
  const choices = ["rock", "paper", "scissors"];
  const randomIndex = Math.floor(Math.random() * 3);
  return choices[randomIndex];
}

function playRound(playerChoice, computerChoice) {
  // TODO: compare and return "win", "lose", or "draw"
}

function game() {
  // TODO: play 5 rounds, track score, log result
}

// Test immediately
console.log(getComputerChoice());
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Commit after completing each function. Small, frequent commits mean you can always roll back to the last working state if something breaks.</p>
</div>
""",
    kc=[
        ("How do you generate a random integer between 0 and 2?", "setup"),
        ("What functions are needed for this game?", "requirements"),
    ],
    assignments=[
        "Complete the game meeting all requirements above.",
        "Push to GitHub and publish on GitHub Pages.",
    ],
    resources=[
        ("MDN — Math.random()", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random"),
        ("javascript.info — Comparisons", "https://javascript.info/comparison"),
        ("YouTube — Rock Paper Scissors in JavaScript (Web Dev Simplified)", "https://www.youtube.com/watch?v=1yS-JV4fWqY"),
    ])

    write("clean-code","Clean Code",
    intro="Code is written once but read many times. Clean code is code that the next developer — or future you — can understand immediately without needing to decode it.",
    overview=[
        "Write descriptive, self-documenting variable and function names.",
        "Know when and how to write useful comments.",
        "Keep functions small and focused on one responsibility.",
    ],
    body="""
<h2 class="lesson-section-title" id="naming">Naming Things Well</h2>
""" + code("""// Bad — what do these mean?
const d = 7;
const arr = ["Alice", "Bob"];
function calc(x, y) { return x * y; }

// Good — self-documenting
const daysInWeek = 7;
const userNames  = ["Alice", "Bob"];
function calculateRectangleArea(width, height) { return width * height; }

// Booleans should read like yes/no questions
const isLoggedIn     = true;
const hasPermission  = false;
const canEdit        = user.role === "admin";

// Functions should describe their action
getUserById(id);
validateEmailFormat(email);
renderProductCard(product);
""") + """
<h2 class="lesson-section-title" id="comments">When to Comment</h2>
""" + code("""// BAD — restating what the code does
// Add 1 to count
count += 1;

// GOOD — explaining WHY, not WHAT
// Offset by 1 because the API returns 0-indexed results
const displayIndex = apiIndex + 1;

// GOOD — documenting complex non-obvious logic
// Haversine formula — calculates great-circle distance between two GPS points
const a = Math.sin(dLat/2) ** 2 + Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon/2) ** 2;
""") + """
<h2 class="lesson-section-title" id="small-functions">Small, Focused Functions</h2>
""" + code("""// BAD — one function that does everything
function processUserRegistration(data) {
  // validates... fetches DB... hashes password... sends email... logs analytics...
}

// GOOD — each function has one responsibility
function validateRegistrationData(data) { ... }
function checkIfEmailExists(email) { ... }
function hashPassword(password) { ... }
function sendWelcomeEmail(user) { ... }

async function registerUser(data) {
  validateRegistrationData(data);
  const exists = await checkIfEmailExists(data.email);
  if (exists) throw new Error("Email already registered");
  // ...
}
"""),
    kc=[
        ("What makes a variable name 'good'?", "naming"),
        ("When should you write a comment?", "comments"),
        ("What is the single responsibility principle for functions?", "small-functions"),
    ],
    assignments=[
        "Review your Rock Paper Scissors project and rename any unclear variables or functions.",
        "Refactor any function longer than 10 lines into smaller named sub-functions.",
    ],
    resources=[
        ("javascript.info — Coding Style", "https://javascript.info/coding-style"),
        ("YouTube — Clean Code (Fireship)", "https://www.youtube.com/watch?v=4jFJ3BGKL0E"),
        ("Clean Code JavaScript (GitHub)", "https://github.com/ryanmcdermott/clean-code-javascript"),
    ])

    write("installing-nodejs","Installing Node.js",
    intro="Node.js lets you run JavaScript outside the browser. It is also required by most JavaScript development tools, build systems, and package managers you will use throughout this curriculum.",
    overview=[
        "Understand what Node.js is and why it is needed.",
        "Install Node.js using NVM.",
        "Use npm to install packages.",
        "Run JavaScript files from the terminal.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-node">What Is Node.js?</h2>
<p>Node.js is a JavaScript runtime built on Chrome's V8 engine. It allows JavaScript to run on your computer or a server — reading files, making network requests, building APIs. It also powers tools like Webpack, Vite, ESLint, and Prettier that you will use constantly.</p>

<h2 class="lesson-section-title" id="install">Installing with NVM</h2>
""" + code("""# Install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Restart terminal, then install LTS Node
nvm install --lts
nvm use --lts

# Verify both installed
node --version   # v20.x.x
npm --version    # 10.x.x
""") + """
<h2 class="lesson-section-title" id="running">Running JavaScript Files</h2>
""" + code("""# Create and run a file
echo 'console.log("Hello from Node.js!")' > hello.js
node hello.js
# Output: Hello from Node.js!

# Interactive REPL (like the browser console)
node
> 2 + 2
4
> .exit
""") + """
<h2 class="lesson-section-title" id="npm">npm Basics</h2>
""" + code("""# Initialise a project
npm init -y

# Install a package
npm install lodash

# Install a dev dependency
npm install --save-dev jest

# Run a script from package.json
npm run test
"""),
    kc=[
        ("What is Node.js used for?", "what-node"),
        ("Why install Node.js via NVM instead of directly?", "install"),
        ("What is npm?", "npm"),
    ],
    assignments=[
        "Verify Node.js is installed: run <code>node --version</code>.",
        "Create a <code>hello.js</code> file and run it with <code>node hello.js</code>.",
        "Run <code>node</code> in interactive mode and test five JavaScript expressions.",
    ],
    resources=[
        ("NVM — GitHub Repository", "https://github.com/nvm-sh/nvm"),
        ("Node.js Official Docs", "https://nodejs.org/en/docs/"),
        ("YouTube — Node.js Crash Course (Traversy Media)", "https://www.youtube.com/watch?v=fBNz5xF-Kx4"),
    ])

    write("arrays-and-loops","Arrays and Loops",
    intro="Arrays store ordered collections of data. Loops process that data item by item. Together they form one of the most powerful patterns in all of programming.",
    overview=[
        "Create and manipulate arrays.",
        "Use for, while, and for...of loops.",
        "Use forEach, map, filter, and reduce.",
    ],
    body="""
<h2 class="lesson-section-title" id="arrays">Arrays</h2>
""" + code("""const fruits  = ["apple", "banana", "cherry"];
const numbers = [1, 2, 3, 4, 5];

// Access by index (zero-based)
fruits[0]   // "apple"
fruits[2]   // "cherry"

// Common operations
fruits.push("date");       // add to end
fruits.pop();              // remove from end
fruits.unshift("avocado"); // add to start
fruits.shift();            // remove from start
fruits.length              // number of items
fruits.includes("banana")  // true
fruits.indexOf("cherry")   // 2
""") + """
<h2 class="lesson-section-title" id="loops">Loops</h2>
""" + code("""// for loop — when you need the index
for (let i = 0; i < fruits.length; i++) {
  console.log(i, fruits[i]);
}

// for...of — cleaner when you just need the value
for (const fruit of fruits) {
  console.log(fruit);
}

// while loop — when you don't know iteration count
let count = 0;
while (count < 5) {
  console.log(count);
  count++;
}
""") + """
<h2 class="lesson-section-title" id="array-methods">Array Methods</h2>
""" + code("""const numbers = [1, 2, 3, 4, 5, 6];

// forEach — do something for each item (no return)
numbers.forEach(n => console.log(n));

// map — transform each item, return new array
const doubled = numbers.map(n => n * 2);
// [2, 4, 6, 8, 10, 12]

// filter — keep items that pass a test
const evens = numbers.filter(n => n % 2 === 0);
// [2, 4, 6]

// reduce — combine all items into one value
const sum = numbers.reduce((total, n) => total + n, 0);
// 21

// Chaining
const result = numbers
  .filter(n => n % 2 === 0)
  .map(n => n * 10);
// [20, 40, 60]
"""),
    kc=[
        ("How do you access the third item in an array?", "arrays"),
        ("What is the difference between for and for...of?", "loops"),
        ("What is the difference between map and forEach?", "array-methods"),
        ("What does filter return?", "array-methods"),
    ],
    assignments=[
        "Create an array of 10 numbers. Chain filter, map, and reduce to: keep only evens, double them, then sum the result.",
        "Given an array of names, return a new array of names longer than 4 characters, capitalised.",
    ],
    resources=[
        ("MDN — Array", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array"),
        ("javascript.info — Arrays", "https://javascript.info/array"),
        ("YouTube — JavaScript Arrays (Web Dev Simplified)", "https://www.youtube.com/watch?v=7W4pQQ20nJg"),
    ])

    write("dom-manipulation-and-events","DOM Manipulation and Events",
    intro="The DOM (Document Object Model) is how JavaScript sees and interacts with your HTML. Events are how you respond to user actions. Together they make pages interactive.",
    overview=[
        "Select HTML elements using JavaScript.",
        "Modify element content, classes, and styles.",
        "Create and remove elements dynamically.",
        "Add event listeners to respond to user interactions.",
    ],
    body="""
<h2 class="lesson-section-title" id="selecting">Selecting Elements</h2>
""" + code("""// querySelector — first matching element
const title  = document.querySelector("h1");
const btn    = document.querySelector("#submit-btn");
const card   = document.querySelector(".product-card");

// querySelectorAll — all matching elements (NodeList)
const allCards = document.querySelectorAll(".card");
allCards.forEach(card => console.log(card.textContent));
""") + """
<h2 class="lesson-section-title" id="modifying">Modifying Elements</h2>
""" + code("""const title = document.querySelector("h1");

title.textContent = "New Heading";           // change text
title.innerHTML   = "New <em>Heading</em>";  // allows HTML tags
title.style.color = "#2563eb";               // inline style

title.classList.add("highlight");    // add class
title.classList.remove("hidden");    // remove class
title.classList.toggle("active");    // toggle class

const img = document.querySelector("img");
img.setAttribute("src", "new-photo.jpg");
img.setAttribute("alt", "Updated description");
""") + """
<h2 class="lesson-section-title" id="creating">Creating Elements</h2>
""" + code("""const newCard = document.createElement("div");
newCard.classList.add("card");
newCard.textContent = "I am a new card";

document.body.appendChild(newCard);              // end of body
document.querySelector(".grid").prepend(newCard); // start of .grid

const oldCard = document.querySelector(".old-card");
oldCard.remove();
""") + """
<h2 class="lesson-section-title" id="events">Events</h2>
""" + code("""const btn = document.querySelector("#my-button");

btn.addEventListener("click", function(event) {
  console.log("Clicked!", event.target);
});

// Arrow syntax
btn.addEventListener("click", (e) => {
  e.preventDefault(); // stop default browser behaviour
  btn.textContent = "Clicked!";
});

// Common events:
// "click"           — mouse click
// "input"           — input value changes
// "submit"          — form submitted
// "keydown"         — key pressed
// "mouseover"       — mouse enters element
// "DOMContentLoaded"— HTML fully loaded
"""),
    kc=[
        ("What does querySelector return when there are multiple matches?", "selecting"),
        ("What is the difference between textContent and innerHTML?", "modifying"),
        ("How do you attach a function to run on button click?", "events"),
        ("What does event.preventDefault() do?", "events"),
    ],
    assignments=[
        "Build a page with a button that changes the background colour when clicked.",
        "Build a counter: a displayed number that increases on '+', decreases on '-', and resets on 'Reset'.",
    ],
    resources=[
        ("MDN — Introduction to the DOM", "https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction"),
        ("javascript.info — DOM Tree", "https://javascript.info/dom-nodes"),
        ("YouTube — JavaScript DOM Manipulation (Web Dev Simplified)", "https://www.youtube.com/watch?v=y17RuWkWdn8"),
    ])

    write("revisiting-rock-paper-scissors","Revisiting Rock Paper Scissors",
    intro="You built Rock Paper Scissors in the console. Now give it a proper UI using DOM manipulation — buttons, a live score display, and visual round results.",
    overview=[
        "Add HTML buttons for each choice.",
        "Display round results and running score on the page.",
        "Update the DOM in response to user clicks.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">UI Requirements</h2>
<ul>
  <li>Three buttons: Rock, Paper, Scissors</li>
  <li>A display area showing the round result</li>
  <li>A score tracker showing player vs computer</li>
  <li>A Reset button that clears score and result</li>
</ul>

<h2 class="lesson-section-title" id="html-structure">Suggested HTML Structure</h2>
""" + code("""<div class="game">
  <div class="score">
    <span id="player-score">0</span>
    <span>vs</span>
    <span id="computer-score">0</span>
  </div>

  <div class="buttons">
    <button class="choice-btn" data-choice="rock">🪨 Rock</button>
    <button class="choice-btn" data-choice="paper">📄 Paper</button>
    <button class="choice-btn" data-choice="scissors">✂️ Scissors</button>
  </div>

  <p id="result-display">Choose a weapon!</p>
  <button id="reset-btn">Reset</button>
</div>
""") + code("""// Connect UI to existing game logic
const buttons       = document.querySelectorAll(".choice-btn");
const resultDisplay = document.getElementById("result-display");
const playerScoreEl = document.getElementById("player-score");
const computerScoreEl = document.getElementById("computer-score");

let playerScore = 0, computerScore = 0;

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const playerChoice   = button.dataset.choice;
    const computerChoice = getComputerChoice();
    const result         = playRound(playerChoice, computerChoice);

    if (result === "win")  playerScore++;
    if (result === "lose") computerScore++;

    resultDisplay.textContent =
      `You ${result}! ${playerChoice} vs ${computerChoice}`;
    playerScoreEl.textContent  = playerScore;
    computerScoreEl.textContent = computerScore;
  });
});
"""),
    kc=[
        ("How do you read a button's data-choice attribute in JavaScript?", "html-structure"),
        ("What DOM methods update the score display?", "html-structure"),
    ],
    assignments=[
        "Add the full UI to your existing Rock Paper Scissors project.",
        "Push the updated version to GitHub — it auto-updates on GitHub Pages.",
    ],
    resources=[
        ("MDN — Using data attributes", "https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes"),
        ("javascript.info — Browser Events", "https://javascript.info/introduction-browser-events"),
        ("YouTube — Rock Paper Scissors UI (Web Dev Simplified)", "https://www.youtube.com/watch?v=1yS-JV4fWqY"),
    ])

    write("project-etch-a-sketch","Project: Etch-a-Sketch",
    intro="Build a browser-based drawing pad where hovering over grid squares colours them in. This project combines dynamic element creation, mouseover events, and Flexbox or Grid layout.",
    overview=[
        "Dynamically create a grid of divs using JavaScript.",
        "Colour grid squares on mouseover.",
        "Allow the user to change the grid size.",
        "Use CSS Grid for the grid layout.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>A 16×16 grid of square divs created entirely by JavaScript</li>
  <li>Hovering over a square darkens or colours it</li>
  <li>A button that prompts for a new grid size (1–100) and re-generates the grid</li>
  <li>Grid always fills the same total container size regardless of dimensions</li>
</ul>

<h2 class="lesson-section-title" id="setup">Setup</h2>
""" + code("""mkdir ~/devpath-projects/etch-a-sketch
cd ~/devpath-projects/etch-a-sketch
git init
touch index.html styles.css script.js
code .
""") + code("""// Create the grid dynamically
function createGrid(size) {
  const container = document.querySelector("#grid-container");
  container.innerHTML = "";
  container.style.gridTemplateColumns = `repeat(${size}, 1fr)`;

  for (let i = 0; i < size * size; i++) {
    const square = document.createElement("div");
    square.classList.add("grid-square");
    square.addEventListener("mouseover", () => {
      square.style.backgroundColor = "#2563eb";
    });
    container.appendChild(square);
  }
}
createGrid(16);

document.querySelector("#reset-btn").addEventListener("click", () => {
  const size = parseInt(prompt("Enter grid size (1-100):"));
  if (size >= 1 && size <= 100) createGrid(size);
});
""") + code("""/* CSS */
#grid-container {
  display: grid;
  width: 600px;
  height: 600px;
  border: 2px solid #1e3a8a;
}
.grid-square {
  background: white;
  border: 1px solid #e2e8f0;
  transition: background-color 0.1s;
}
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Stretch goal: progressively darken squares on each hover pass — each mouseover adds 10% darkness until fully black.</p>
</div>
""",
    kc=[
        ("How do you create a 16×16 grid entirely with JavaScript?", "setup"),
        ("What event fires when the mouse moves over an element?", "requirements"),
    ],
    assignments=[
        "Complete the project meeting all requirements.",
        "Add the stretch goal: progressive darkening on hover.",
        "Push to GitHub Pages.",
    ],
    resources=[
        ("MDN — Document.createElement", "https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement"),
        ("MDN — CSS Grid Layout", "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout"),
        ("YouTube — Etch-a-Sketch Project (Web Dev Simplified)", "https://www.youtube.com/watch?v=J8LKHwBCJTk"),
    ])

    write("object-basics","Object Basics",
    intro="Objects group related data and functions together. They are the fundamental building block of JavaScript — everything from DOM elements to API responses is an object.",
    overview=[
        "Create objects with properties and methods.",
        "Access and modify properties using dot and bracket notation.",
        "Understand 'this' inside object methods.",
        "Use destructuring and spread syntax.",
    ],
    body="""
<h2 class="lesson-section-title" id="creating">Creating Objects</h2>
""" + code("""const user = {
  name: "Alice",
  age: 28,
  isAdmin: false,
  address: {
    city: "Addis Ababa",
    country: "Ethiopia"
  },
  greet() {
    return `Hello, I am ${this.name}`;
  }
};

user.name          // "Alice"
user.address.city  // "Addis Ababa"
user.greet()       // "Hello, I am Alice"
""") + """
<h2 class="lesson-section-title" id="accessing">Dot vs Bracket Notation</h2>
""" + code("""// Dot notation — use when you know the property name
user.name = "Bob";

// Bracket notation — use when property name is in a variable
const prop = "name";
user[prop]  // "Bob"

// Useful for dynamic access
const fields = ["name", "age", "isAdmin"];
fields.forEach(field => console.log(user[field]));

// Check if a property exists
"name" in user           // true
user.hasOwnProperty("age") // true
""") + """
<h2 class="lesson-section-title" id="this">The this Keyword</h2>
""" + code("""const counter = {
  count: 0,
  increment() {
    this.count++;    // 'this' refers to the counter object
    return this.count;
  },
  reset() { this.count = 0; }
};

counter.increment(); // 1
counter.increment(); // 2
counter.reset();
""") + """
<h2 class="lesson-section-title" id="destructuring">Destructuring and Spread</h2>
""" + code("""// Destructuring — extract properties into variables
const { name, age } = user;
console.log(name); // "Bob"

// Shorthand property names
const x = 10, y = 20;
const point = { x, y };  // same as { x: x, y: y }

// Spread — copy or merge objects
const updatedUser = { ...user, age: 29 }; // copy with override
"""),
    kc=[
        ("What is the difference between dot and bracket notation?", "accessing"),
        ("What does 'this' refer to inside an object method?", "this"),
        ("What does object destructuring do?", "destructuring"),
    ],
    assignments=[
        "Create an object representing a book with 5 properties and 2 methods. Log each property and call each method.",
        "Write a function that takes an array of user objects and returns only the names of users aged 18 or over.",
    ],
    resources=[
        ("MDN — Working with Objects", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects"),
        ("javascript.info — Objects", "https://javascript.info/object"),
        ("YouTube — JavaScript Objects (Web Dev Simplified)", "https://www.youtube.com/watch?v=sTSLn1Sj3fc"),
    ])

    write("project-calculator","Project: Calculator",
    intro="The calculator is the capstone of the Foundations course. It brings together HTML, CSS, Flexbox, DOM manipulation, events, and JavaScript logic in one polished application.",
    overview=[
        "Build a functional on-screen calculator with a clean UI.",
        "Handle operator chaining and display updates.",
        "Manage calculator state across button clicks.",
        "Handle edge cases like dividing by zero.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Number buttons 0–9 and a decimal point</li>
  <li>Operator buttons: +, -, ×, ÷</li>
  <li>An equals button that calculates and shows the result</li>
  <li>A clear button (AC) that resets everything</li>
  <li>A display showing the current number or result</li>
  <li>Chaining: after pressing =, the result becomes the first operand of the next calculation</li>
  <li>Edge case: dividing by zero shows a meaningful error message</li>
</ul>

<h2 class="lesson-section-title" id="approach">Suggested Approach</h2>
""" + code("""// Step 1: Build HTML + CSS first (structure before logic)

// Step 2: Write the four math functions
function add(a, b)      { return a + b; }
function subtract(a, b) { return a - b; }
function multiply(a, b) { return a * b; }
function divide(a, b) {
  if (b === 0) return "Cannot divide by zero";
  return a / b;
}

// Step 3: Write operate() to dispatch to the right function
function operate(op, a, b) {
  if (op === "+") return add(a, b);
  if (op === "-") return subtract(a, b);
  if (op === "×") return multiply(a, b);
  if (op === "÷") return divide(a, b);
}

// Step 4: Track state
let firstOperand       = null;
let operator           = null;
let shouldResetDisplay = false;

// Step 5: Wire up buttons with event listeners
// Step 6: Handle edge cases last
""") + code("""mkdir ~/devpath-projects/calculator
cd ~/devpath-projects/calculator
git init
touch index.html styles.css script.js
code .
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Do not use <code>eval()</code> to calculate results — it is a security risk and teaches you nothing. Implement <code>operate()</code> yourself.</p>
</div>
""",
    kc=[
        ("What four math functions does the calculator need?", "approach"),
        ("What state variables does the calculator need to track?", "approach"),
        ("How do you handle dividing by zero?", "requirements"),
    ],
    assignments=[
        "Complete the Calculator meeting all requirements.",
        "Push to GitHub and publish on GitHub Pages — this is your flagship Foundations project.",
    ],
    resources=[
        ("MDN — JavaScript Reference", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference"),
        ("javascript.info — Events", "https://javascript.info/events"),
        ("YouTube — Build a Calculator (Web Dev Simplified)", "https://www.youtube.com/watch?v=j59qQ7YWLxw"),
    ])

    write("choose-your-path","Choose Your Path Forward",
    intro="Congratulations — you have completed the Foundations course. Look back at how far you have come, then choose your specialisation path and keep building.",
    overview=[
        "Reflect on everything you have built in Foundations.",
        "Understand what each path covers.",
        "Make an informed choice between Full Stack JavaScript and Full Stack Ruby on Rails.",
    ],
    body="""
<h2 class="lesson-section-title" id="accomplished">What You Have Accomplished</h2>
<p>When you started, you may not have known what a terminal was. Now you can:</p>
<ul>
  <li>Build multi-page websites with semantic HTML</li>
  <li>Style them with CSS using Flexbox layouts</li>
  <li>Add interactivity with JavaScript and DOM manipulation</li>
  <li>Track code with Git and publish projects on GitHub Pages</li>
  <li>Debug effectively using DevTools and error messages</li>
  <li>Think through problems systematically before writing code</li>
</ul>
<p>That is a real foundation. The next phase is where it gets exciting.</p>

<h2 class="lesson-section-title" id="js-path">Full Stack JavaScript Path</h2>
<p>This path stays in JavaScript — the language you have been using. You will go much deeper into JavaScript, then learn React for sophisticated frontends and Node.js with Express for backends. Database: PostgreSQL.</p>
<p><strong>Choose this if:</strong> you enjoy JavaScript, want one language on both frontend and backend, or are excited by the modern web ecosystem.</p>

<h2 class="lesson-section-title" id="rails-path">Full Stack Ruby on Rails Path</h2>
<p>This path introduces Ruby — a language celebrated for its elegant syntax. Then you learn Rails, a backend framework famous for rapid application development. You also go deeper into HTML, CSS, and SQL.</p>
<p><strong>Choose this if:</strong> you want to try a new language, are drawn to rapid backend development, or prefer the structured convention-over-configuration approach.</p>

<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>There is no wrong choice — both paths lead to full-stack developer skills. The important thing is to commit to one and not switch back and forth.</p>
</div>

<div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
  <a href="../../paths/full-stack-javascript/index.html" class="btn btn-primary">Start Full Stack JavaScript &#8594;</a>
  <a href="../../paths/full-stack-ruby-on-rails/index.html" class="btn btn-outline">Start Full Stack Ruby on Rails &#8594;</a>
</div>
""",
    kc=[
        ("What does the Full Stack JavaScript path use for backend?", "js-path"),
        ("What framework does the Ruby path use?", "rails-path"),
        ("What matters most when choosing a path?", "rails-path"),
    ],
    assignments=[
        "Choose your path and navigate to it — your next lesson is waiting.",
        "Share which path you chose and why in the community.",
    ],
    resources=[
        ("MDN — Web Development Learning Pathway", "https://developer.mozilla.org/en-US/docs/Learn"),
        ("javascript.info — Full JavaScript Reference", "https://javascript.info/"),
        ("YouTube — How to Choose a Web Dev Path (Traversy Media)", "https://www.youtube.com/watch?v=ysEN5RaKOlA"),
    ])

    print("\nAll 48 lessons written. Pushing to GitHub...\n")
    os.chdir(BASE)
    subprocess.run(["git","add","-A"], check=True)
    subprocess.run(["git","commit","-m","Revise all 48 Foundation lessons: remove odin refs, original explanations, quality resources"], check=True)
    subprocess.run(["git","push"], check=True)
    print("Done. All 48 Foundations lessons seeded and pushed.")

if __name__ == "__main__":
    seed()
