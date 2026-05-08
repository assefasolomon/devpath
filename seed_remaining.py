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
    return ('<nav class="site-nav"><a href="../../index.html" class="nav-logo">'
            + LOGO + ' DevPath</a><ul class="nav-links">'
            '<li><a href="../../index.html">Home</a></li>'
            '<li><a href="../index.html">Foundations</a></li>'
            '<li><a href="../../paths/full-stack-javascript/index.html">Full Stack JS</a></li>'
            '<li><a href="../../paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a></li>'
            '</ul></nav>')

def footer():
    return '<footer class="site-footer"><p>DevPath — A free, open, project-based web development curriculum.</p></footer>'

def sidebar(active):
    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "") + (" active" if sl == active else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'
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
    for sl,ti,*p in [("introduction-to-html-css","Introduction to HTML and CSS"),("elements-and-tags","Elements and Tags"),("html-boilerplate","HTML Boilerplate"),("working-with-text","Working with Text"),("lists","Lists"),("links-and-images","Links and Images"),("commit-messages","Commit Messages"),("project-recipes","Project: Recipes","p")]:
        s += lnk(sl,ti,bool(p))
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">CSS Foundations</div>'
    for sl,ti in [("intro-to-css","Intro to CSS"),("the-cascade","The Cascade"),("inspecting-html-and-css","Inspecting HTML and CSS"),("the-box-model","The Box Model"),("block-and-inline","Block and Inline")]:
        s += lnk(sl,ti)
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">Flexbox</div>'
    for sl,ti,*p in [("introduction-to-flexbox","Introduction to Flexbox"),("growing-and-shrinking","Growing and Shrinking"),("axes","Axes"),("alignment","Alignment"),("project-landing-page","Project: Landing Page","p")]:
        s += lnk(sl,ti,bool(p))
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">JavaScript Basics</div>'
    for sl,ti,*p in [("variables-and-operators","Variables and Operators"),("data-types-and-conditionals","Data Types and Conditionals"),("javascript-developer-tools","JavaScript Developer Tools"),("function-basics","Function Basics"),("problem-solving","Problem Solving"),("understanding-errors","Understanding Errors"),("project-rock-paper-scissors","Project: Rock Paper Scissors","p"),("clean-code","Clean Code"),("installing-nodejs","Installing Node.js"),("arrays-and-loops","Arrays and Loops"),("dom-manipulation-and-events","DOM Manipulation and Events"),("revisiting-rock-paper-scissors","Revisiting Rock Paper Scissors"),("project-etch-a-sketch","Project: Etch-a-Sketch","p"),("object-basics","Object Basics"),("project-calculator","Project: Calculator","p")]:
        s += lnk(sl,ti,bool(p))
    s += '</div><div class="sidebar-section"><div class="sidebar-section-label">Conclusion</div>'
    s += lnk("choose-your-path","Choose Your Path Forward")
    s += '</div></aside>'
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
    p,n = pn(slug)
    pb = f'<a href="{p[1]}" class="btn btn-blue-outline">&#8592; Previous</a>' if p else '<span></span>'
    nb = f'<a href="{n[1]}" class="btn btn-blue">Next &#8594;</a>' if n else '<span></span>'
    return (f'<div class="lesson-nav-bar">'
            f'<div class="lesson-nav-bar-group">{pb}</div>'
            f'<div class="lesson-nav-bar-group"><button class="btn btn-green mark-complete-btn">Mark Completed</button></div>'
            f'<div class="lesson-nav-bar-group">{nb}</div>'
            f'</div>')

def write(slug, title, intro, overview, body, kc, assignments, resources):
    # Skip if already seeded with real content
    path = os.path.join(LESSONS, f"{slug}.html")
    if os.path.exists(path):
        with open(path) as f:
            if "Content not yet seeded" not in f.read():
                print(f"  SKIP (already seeded): {slug}")
                return

    p,n = pn(slug)
    bc  = (f'<nav class="breadcrumb"><a href="../../index.html">Home</a>'
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

    html = (f'<!DOCTYPE html>\n<html lang="en">\n<head>\n'
            f'  <meta charset="UTF-8">\n'
            f'  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            f'  <title>{title} | DevPath</title>\n'
            f'  <link rel="stylesheet" href="../../css/styles.css">\n'
            f'</head>\n<body>\n'
            + nav() + "\n"
            + navbar(slug) + "\n"
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
            + '<script src="../../js/main.js"></script>\n</body>\n</html>')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ {slug}")


def seed():

    # ── join-the-community ──────────────────────────────────
    write("join-the-community","Join the Odin Community",
    intro="Learning alone is hard. Learning with a community is dramatically easier and more enjoyable. This lesson explains how to find and use the developer community around this curriculum.",
    overview=["Understand why a learning community matters.","Know where to ask questions and share progress.","Learn community etiquette that gets you better help faster."],
    body="""
<h2 class="lesson-section-title" id="why-community">Why Community Matters</h2>
<p>When you hit a wall — and you will — having a place to ask questions makes the difference between pushing through and giving up. A good community also exposes you to how other developers think and approach problems, which accelerates your learning far beyond what solo study achieves.</p>
<p>Beyond debugging help, a community gives you accountability, celebrates your wins, and connects you with people who have already walked the path you are on.</p>

<h2 class="lesson-section-title" id="where">Where to Connect</h2>
<ul>
  <li><strong>Discord</strong> — Real-time chat with other learners. Find servers for The Odin Project, freeCodeCamp, and general web development. Ask questions, share projects, help others.</li>
  <li><strong>GitHub</strong> — Follow other learners, star projects that inspire you, and build your own public profile as you complete projects.</li>
  <li><strong>Reddit</strong> — r/learnprogramming and r/webdev are large, active communities for questions and discussion.</li>
  <li><strong>Stack Overflow</strong> — The definitive Q&amp;A site for specific technical questions. Read before posting — your question has probably already been answered.</li>
</ul>

<h2 class="lesson-section-title" id="etiquette">Community Etiquette</h2>
<ul>
  <li><strong>Search before asking.</strong> If your question has been asked before, the existing answer is faster than waiting for a new one.</li>
  <li><strong>Show your work.</strong> Share what you tried and why it did not work. This gets you better help and shows you have put in effort.</li>
  <li><strong>Be specific.</strong> "It does not work" is not a question. "I expected X, got Y, tried Z" is.</li>
  <li><strong>Help others.</strong> Answering questions — even ones where you are not fully sure — is one of the best ways to solidify your own understanding.</li>
  <li><strong>Be kind.</strong> Everyone is at a different point on the same journey.</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Helping someone else debug their code teaches you more than reading about the topic would. As soon as you know enough to help, start helping.</p>
</div>""",
    kc=[("Why does learning in a community accelerate progress?","why-community"),("What makes a question get a good answer in a community?","etiquette")],
    assignments=["Join at least one web development Discord server today.","Introduce yourself in the community — share where you are in the curriculum and what you are hoping to build."],
    resources=[("The Odin Project Discord Community","https://discord.gg/fbFCkYabZB"),("Reddit — r/learnprogramming","https://www.reddit.com/r/learnprogramming/"),("YouTube — How to Use Stack Overflow (Fireship)","https://www.youtube.com/watch?v=E3UPFmEFMD8")])

    # ── installation-overview ───────────────────────────────
    write("installation-overview","Installation Overview",
    intro="Before writing code you need the right tools. This lesson gives you a clear picture of what you will install and why each tool exists — so the Installations lesson feels purposeful rather than mechanical.",
    overview=["Understand the purpose of each tool in the development setup.","Know which installation path applies to your operating system."],
    body="""
<h2 class="lesson-section-title" id="tools">The Tools You Will Install</h2>
<ul>
  <li><strong>VS Code</strong> — Your code editor. Where you write everything.</li>
  <li><strong>Git</strong> — Version control. Tracks every change to your code.</li>
  <li><strong>Node.js</strong> — JavaScript runtime outside the browser. Required by many dev tools.</li>
  <li><strong>Google Chrome</strong> — Primary browser for testing. Best DevTools in the industry.</li>
</ul>

<h2 class="lesson-section-title" id="os-path">Your Operating System Path</h2>
<ul>
  <li><strong>macOS</strong> — Uses Homebrew as a package manager. Straightforward setup.</li>
  <li><strong>Linux (Ubuntu/Debian)</strong> — Uses apt. Generally the smoothest developer experience.</li>
  <li><strong>Windows</strong> — Must use WSL2 (Windows Subsystem for Linux). This gives you a full Linux environment inside Windows — the same tools Mac and Linux developers use.</li>
</ul>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>If you are on Windows, do not skip WSL2. Attempting web development with native Windows tools causes significant compatibility pain. WSL2 solves this cleanly.</p>
</div>""",
    kc=[("What is each tool in the development setup used for?","tools"),("Why do Windows users need WSL2?","os-path")],
    assignments=["If you are on Windows, read the Microsoft WSL installation guide linked below before proceeding.","Confirm you know your operating system version."],
    resources=[("Microsoft — Install WSL","https://learn.microsoft.com/en-us/windows/wsl/install"),("YouTube — WSL2 Setup for Web Dev (Traversy Media)","https://www.youtube.com/watch?v=cgH3nhYBmQs"),("YouTube — Mac Setup for Web Development (Traversy Media)","https://www.youtube.com/watch?v=2qVBfBT0VcE")])

    # ── installations ───────────────────────────────────────
    write("installations","Installations",
    intro="Time to set up your development environment. Follow the steps for your operating system carefully. A good setup now prevents hours of frustration later.",
    overview=["Install VS Code and essential extensions.","Install Git and configure it with your identity.","Install Google Chrome.","Install Node.js via NVM."],
    body="""
<h2 class="lesson-section-title" id="vscode">VS Code</h2>
<p>Download from <a href="https://code.visualstudio.com" target="_blank">code.visualstudio.com</a>. After installing, add these extensions:</p>
<ul>
  <li><strong>Prettier</strong> — auto-formats code on save</li>
  <li><strong>ESLint</strong> — highlights JavaScript errors as you type</li>
  <li><strong>Live Server</strong> — auto-refreshes browser on save</li>
</ul>""" + code("""# Open any project in VS Code from terminal
code .

# Install extensions from terminal
code --install-extension esbenp.prettier-vscode
code --install-extension dbaeumer.vscode-eslint
code --install-extension ritwickdey.LiveServer
""") + """
<h2 class="lesson-section-title" id="git">Git</h2>""" + code("""# Check if already installed
git --version

# Install on Ubuntu/WSL
sudo apt update && sudo apt install git

# Install on macOS
brew install git

# One-time configuration (do this now)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main
""") + """
<h2 class="lesson-section-title" id="node">Node.js via NVM</h2>""" + code("""# Install NVM (Mac/Linux/WSL)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Restart terminal, then:
nvm install --lts
nvm use --lts

# Verify both work
node --version
npm --version
"""),
    kc=[("What command opens a folder in VS Code from the terminal?","vscode"),("What four Git settings should you configure globally?","git"),("Why install Node.js via NVM instead of directly?","node")],
    assignments=["Complete all installations and verify each with its --version command.","Install the three VS Code extensions listed above."],
    resources=[("VS Code — Official Download","https://code.visualstudio.com/"),("NVM — GitHub Repository","https://github.com/nvm-sh/nvm"),("YouTube — VSCode Setup for Web Dev (Traversy Media)","https://www.youtube.com/watch?v=fnPhJHN0jTE")])

    # ── text-editors ────────────────────────────────────────
    write("text-editors","Text Editors",
    intro="VS Code is the industry-standard editor for web development. Learning its shortcuts and features now will make everything that follows significantly faster.",
    overview=["Use the most important VS Code keyboard shortcuts.","Configure VS Code settings for web development.","Use Emmet to write HTML at speed."],
    body="""
<h2 class="lesson-section-title" id="shortcuts">Essential Shortcuts</h2>""" + code("""# Command Palette (find any VS Code command)
Ctrl+Shift+P  /  Cmd+Shift+P

# Quick file open
Ctrl+P  /  Cmd+P

# Toggle integrated terminal
Ctrl+`

# Comment / uncomment selected line(s)
Ctrl+/  /  Cmd+/

# Move line up or down
Alt+Up / Alt+Down

# Duplicate line below
Shift+Alt+Down

# Format entire document
Shift+Alt+F  /  Shift+Option+F

# Multi-cursor: click extra positions
Alt+Click

# Find and replace
Ctrl+H  /  Cmd+H
""") + """
<h2 class="lesson-section-title" id="emmet">Emmet Abbreviations</h2>""" + code("""# Type these then press Tab

!                    → Full HTML5 boilerplate
div.container        → <div class="container"></div>
ul>li*3              → <ul> with 3 <li> items
h1{Hello World}      → <h1>Hello World</h1>
a[href=#]{Click me}  → <a href="#">Click me</a>
""") + """
<h2 class="lesson-section-title" id="settings">Recommended Settings</h2>""" + code("""{
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "editor.wordWrap": "on",
  "editor.fontSize": 15,
  "editor.lineHeight": 1.7,
  "files.autoSave": "onFocusChange"
}
"""),
    kc=[("What shortcut opens the VS Code Command Palette?","shortcuts"),("What does the Emmet abbreviation ul>li*3 expand to?","emmet"),("What does editor.formatOnSave do?","settings")],
    assignments=["Practice every shortcut in the list above at least once.","Add all recommended settings to your User Settings JSON.","Try five Emmet abbreviations in a new HTML file."],
    resources=[("VS Code Tips and Tricks (official)","https://code.visualstudio.com/docs/getstarted/tips-and-tricks"),("Emmet Cheat Sheet","https://docs.emmet.io/cheat-sheet/"),("YouTube — VSCode Tips and Tricks (Fireship)","https://www.youtube.com/watch?v=u21W_tfPVrY")])

    # ── setting-up-git ──────────────────────────────────────
    write("setting-up-git","Setting Up Git",
    intro="Git is installed. Now let us connect it to GitHub and set up SSH keys so you never have to type a password when pushing code.",
    overview=["Configure Git with your identity and editor.","Create and connect a GitHub account.","Set up SSH key authentication."],
    body="""
<h2 class="lesson-section-title" id="config">Git Configuration</h2>""" + code("""git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main
git config --global color.ui auto

# Verify everything is set
git config --list
""") + """
<h2 class="lesson-section-title" id="github-account">GitHub Account</h2>
<p>Create a free account at <a href="https://github.com" target="_blank">github.com</a>. Use the same email address you configured in Git above. Your GitHub profile will become your developer portfolio — choose a professional username.</p>

<h2 class="lesson-section-title" id="ssh">SSH Key Setup</h2>""" + code("""# Step 1: Generate an SSH key
ssh-keygen -t ed25519 -C "you@example.com"
# Press Enter three times to accept all defaults

# Step 2: Display your public key and copy it
cat ~/.ssh/id_ed25519.pub
# Copy the entire output (starts with ssh-ed25519)

# Step 3: Add to GitHub
# Go to: GitHub → Settings → SSH and GPG keys → New SSH key
# Paste your key and click Add SSH key

# Step 4: Test the connection
ssh -T git@github.com
# Expected: "Hi username! You've successfully authenticated."
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Once SSH is set up, always use SSH clone URLs (starting with <code>git@github.com:</code>) rather than HTTPS URLs. This way you never need to enter a password.</p>
</div>""",
    kc=[("What four Git settings should you configure globally?","config"),("What is the benefit of SSH over HTTPS for GitHub?","ssh")],
    assignments=["Complete the SSH key setup and verify with ssh -T git@github.com.","Follow The Odin Project's Setting Up Git guide for step-by-step screenshots — linked below."],
    resources=[("The Odin Project — Setting Up Git","https://www.theodinproject.com/lessons/foundations-setting-up-git"),("GitHub Docs — Generating SSH keys","https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent"),("YouTube — SSH Keys for GitHub (Corey Schafer)","https://www.youtube.com/watch?v=8X4u9sca3Io")])

    # ── introduction-to-html-css ────────────────────────────
    write("introduction-to-html-css","Introduction to HTML and CSS",
    intro="HTML and CSS are the two foundational languages of every website. This lesson gives you a clear picture of what each language does before you start writing either one.",
    overview=["Describe what HTML is responsible for.","Describe what CSS is responsible for.","Understand the relationship between HTML and CSS."],
    body="""
<h2 class="lesson-section-title" id="html-role">What HTML Does</h2>
<p>HTML (HyperText Markup Language) defines the <strong>structure and content</strong> of a web page. It tells the browser what things <em>are</em> — a heading, a paragraph, a list, an image, a link. Think of HTML as a building's skeleton — the load-bearing structure before any decoration.</p>""" + code("""<!DOCTYPE html>
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
<p>CSS (Cascading Style Sheets) controls the <strong>visual presentation</strong> of HTML — colours, fonts, spacing, layout, animations. Using the building analogy: CSS is the paint, furniture, and lighting applied to HTML's skeleton.</p>""" + code("""h1 {
  color: #1d4ed8;
  font-size: 2.5rem;
}

p {
  color: #475569;
  line-height: 1.75;
  max-width: 65ch;
}
""") + """
<h2 class="lesson-section-title" id="together">How They Work Together</h2>
<p>HTML and CSS are deliberately kept in separate files. This separation of concerns keeps code organised — one HTML page can be completely restyled just by swapping its CSS file without touching any HTML.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Mental model: HTML is the noun (what things <em>are</em>), CSS is the adjective (how they <em>look</em>), and JavaScript — coming later — is the verb (what things <em>do</em>).</p>
</div>""",
    kc=[("What is HTML responsible for?","html-role"),("What is CSS responsible for?","css-role"),("Why are HTML and CSS in separate files?","together")],
    assignments=["Read MDN's 'Getting Started with HTML' article linked below.","Read MDN's 'What is CSS?' article linked below."],
    resources=[("MDN — Getting Started with HTML","https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started"),("MDN — What is CSS?","https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS"),("YouTube — HTML and CSS for Beginners (Kevin Powell)","https://www.youtube.com/watch?v=qz0aGYrrlhU")])

    # ── commit-messages ─────────────────────────────────────
    write("commit-messages","Commit Messages",
    intro="A commit message is a permanent label on a snapshot of your code. Writing clear messages is a professional habit that pays off the moment you work with others — or return to your own code months later.",
    overview=["Explain why good commit messages matter.","Follow the seven rules of a great commit message.","Know when to commit and how often."],
    body="""
<h2 class="lesson-section-title" id="why">Why They Matter</h2>""" + code("""# Bad history — tells you nothing
git log --oneline
3f2c1b1 fix
9d8e7f6 stuff
1a2b3c4 wip

# Good history — tells the whole story
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
  <li>Use body to explain <em>what</em> and <em>why</em>, not <em>how</em></li>
</ol>""" + code("""# Subject only (most commits)
git commit -m "Add password strength indicator to signup form"

# Subject + body (when explanation helps)
git commit -m "Fix race condition in auth token refresh

The previous check happened after the request was in flight,
causing 401 errors on slow connections. Now we check and
refresh the token before sending any request.

Closes #142"
""") + """
<h2 class="lesson-section-title" id="when">When to Commit</h2>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>If you cannot describe your commit in one sentence without using "and", it should probably be two separate commits.</p>
</div>""",
    kc=[("What mood should commit subject lines use?","rules"),("What should the body explain — what, why, or how?","rules"),("How do you decide when to make a new commit?","when")],
    assignments=["Read Chris Beams' article 'How to Write a Git Commit Message' linked below.","Review three of your previous commit messages and rewrite them following the seven rules."],
    resources=[("Chris Beams — How to Write a Git Commit Message","https://cbea.ms/git-commit/"),("YouTube — Write Better Commit Messages (Fireship)","https://www.youtube.com/watch?v=Hlp-9cdImSM"),("Conventional Commits Specification","https://www.conventionalcommits.org/")])

    # ── project-recipes ─────────────────────────────────────
    write("project-recipes","Project: Recipes",
    intro="Time to put everything from HTML Foundations into practice. You will build a multi-page recipe website using only HTML — no CSS yet.",
    overview=["Build a multi-page HTML website from scratch.","Use headings, paragraphs, lists, links, and images together.","Connect pages with relative links.","Track and publish with Git and GitHub."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>index.html</strong> — site heading (h1), list of links to each recipe page</li>
  <li><strong>At least three recipe pages</strong>, each with: title (h1), description paragraph, image with alt text, unordered ingredients list, ordered steps list, link back to homepage</li>
  <li>All pages connected with relative links</li>
  <li>Git repo with at least one commit per page, pushed to GitHub</li>
</ul>

<h2 class="lesson-section-title" id="structure">Folder Structure</h2>""" + code("""odin-recipes/
├── index.html
└── recipes/
    ├── lasagne.html
    ├── pancakes.html
    └── chicken-soup.html
""") + """
<h2 class="lesson-section-title" id="workflow">Git Workflow</h2>""" + code("""mkdir ~/devpath-projects/odin-recipes
cd ~/devpath-projects/odin-recipes
git init

# After building each page:
git add .
git commit -m "Add lasagne recipe page"

# When done, push to GitHub:
git remote add origin git@github.com:USERNAME/odin-recipes.git
git branch -M main
git push -u origin main
""") + """
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>Do not add CSS yet. The focus of this project is HTML structure. You will style it in a later project.</p>
</div>""",
    kc=[("What HTML elements are required on each recipe page?","requirements"),("What type of link connects recipe pages back to the homepage?","workflow")],
    assignments=["Complete the project fulfilling all requirements above.","Push the finished project to GitHub and share the link."],
    resources=[("MDN — HTML Element Reference","https://developer.mozilla.org/en-US/docs/Web/HTML/Element"),("YouTube — Build a Simple Multi-Page Website (Kevin Powell)","https://www.youtube.com/watch?v=PlxWf493en4")])

    # ── intro-to-css ────────────────────────────────────────
    write("intro-to-css","Intro to CSS",
    intro="HTML gives your page structure. CSS makes it beautiful. This lesson introduces how CSS rules work and the three ways to attach styles to HTML.",
    overview=["Write a CSS rule with selector, property, and value.","Use element, class, and ID selectors.","Know the three ways to add CSS and why external is always preferred."],
    body="""
<h2 class="lesson-section-title" id="anatomy">Anatomy of a CSS Rule</h2>""" + code("""selector {
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
<h2 class="lesson-section-title" id="selectors">Selectors</h2>""" + code("""/* Element — every h1 */
h1 { color: #1e3a8a; }

/* Class — elements with class="card" */
.card {
  background: #f8fafc;
  border-radius: 8px;
  padding: 1.5rem;
}

/* ID — the unique element with id="hero" */
#hero { background: #1e3a8a; color: white; }

/* Descendant — p inside .card only */
.card p { font-size: 0.9rem; }
""") + """
<h2 class="lesson-section-title" id="three-ways">Three Ways to Add CSS</h2>""" + code("""<!-- 1. INLINE — on the element. Avoid for real projects. -->
<p style="color: red;">Warning</p>

<!-- 2. INTERNAL — style block in head. OK for tiny demos. -->
<style> p { color: navy; } </style>

<!-- 3. EXTERNAL — separate file. Always use this. -->
<link rel="stylesheet" href="styles.css">
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>External stylesheets let you style every page from one file. One change updates the whole site simultaneously.</p>
</div>""",
    kc=[("What are the three parts of a CSS rule?","anatomy"),("What is the difference between a class and an ID selector?","selectors"),("Which of the three methods for adding CSS should you always use for real projects?","three-ways")],
    assignments=["Create styles.css, link it to your Recipes project, and add at least 8 style rules.","Work through the CSS Foundations exercises linked below."],
    resources=[("MDN — CSS First Steps","https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps"),("The Odin Project — CSS Foundations Exercises","https://github.com/TheOdinProject/css-exercises"),("YouTube — CSS Tutorial Zero to Hero (freeCodeCamp)","https://www.youtube.com/watch?v=1Rs2ND1ryYc")])

    # ── the-cascade ─────────────────────────────────────────
    write("the-cascade","The Cascade",
    intro="CSS stands for Cascading Style Sheets. The cascade is the algorithm that decides which rule wins when multiple rules target the same element.",
    overview=["Define specificity and explain how it resolves conflicts.","Understand specificity, inheritance, and source order.","Calculate the specificity weight of any selector."],
    body="""
<h2 class="lesson-section-title" id="cascade">The Three Factors</h2>
<ol>
  <li><strong>Specificity</strong> — how precisely does the selector target the element?</li>
  <li><strong>Source order</strong> — when specificity ties, the later rule wins.</li>
  <li><strong>Inheritance</strong> — some properties pass from parent to child automatically.</li>
</ol>

<h2 class="lesson-section-title" id="specificity">Specificity Weights</h2>""" + code("""/* Element: 0-0-1  (lowest) */
p { color: black; }

/* Class: 0-1-0 */
.intro { color: navy; }

/* ID: 1-0-0 */
#hero { color: gold; }

/* Inline: always wins over selectors */
<p style="color: red;">

/* !important: nuclear option — avoid */
p { color: purple !important; }

/* Combined — class(0-1-0) + element(0-0-1) = 0-1-1 */
.intro p { font-size: 1.1rem; }
""") + """
<h2 class="lesson-section-title" id="inheritance">Inheritance</h2>""" + code("""/* Inherited — children get these automatically */
body {
  font-family: 'Sora', sans-serif;
  color: #334155;
  line-height: 1.75;
}

/* NOT inherited — must be set explicitly on each element */
div {
  border: 1px solid #e2e8f0;
  padding: 1rem;
  margin: 2rem;
}
""") + """
<h2 class="lesson-section-title" id="source-order">Source Order</h2>""" + code("""/* Same specificity — later rule wins */
p { color: red; }
p { color: blue; }
/* Result: blue */
"""),
    kc=[("What three factors does the cascade consider?","cascade"),("Which has higher specificity — class or ID?","specificity"),("Is the CSS color property inherited by children?","inheritance"),("When two rules have equal specificity, which wins?","source-order")],
    assignments=["Open DevTools on any page, inspect an element, and find at least one overridden (strikethrough) rule. Trace why it lost.","Work through the CSS Cascade exercises linked below."],
    resources=[("MDN — Cascade and Inheritance","https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance"),("The Odin Project — CSS Foundations Exercises","https://github.com/TheOdinProject/css-exercises"),("CSS Specificity Calculator","https://specificity.keegan.st/"),("YouTube — CSS Specificity (Kevin Powell)","https://www.youtube.com/watch?v=c0kfcP_nD9E")])

    # ── inspecting-html-and-css ─────────────────────────────
    write("inspecting-html-and-css","Inspecting HTML and CSS",
    intro="Browser DevTools are your most powerful debugging tool as a front-end developer. This lesson shows you how to inspect, test, and diagnose issues in seconds.",
    overview=["Open and navigate browser DevTools.","Inspect elements to see HTML and applied styles.","Edit CSS live in the browser.","Use the box model diagram to debug spacing."],
    body="""
<h2 class="lesson-section-title" id="opening">Opening DevTools</h2>""" + code("""F12                    # All platforms
Cmd + Option + I       # Mac
Right-click → Inspect  # Any element on the page
Ctrl+Shift+C           # Click-to-inspect mode
""") + """
<h2 class="lesson-section-title" id="elements-panel">Elements Panel</h2>
<p>Shows the live DOM — the HTML structure the browser built. Select any element to see every CSS rule applied to it in the Styles pane. Overridden rules appear with a strikethrough.</p>

<h2 class="lesson-section-title" id="live-css">Live CSS Editing</h2>
<ol>
  <li>Select element in Elements panel</li>
  <li>Click any property value in Styles pane and change it</li>
  <li>Press Tab to move to the next property</li>
  <li>Click empty space in a rule to add a new property</li>
  <li>Copy successful values back into your actual CSS file</li>
</ol>
<div class="callout callout-warn">
  <span class="callout-icon">⚠️</span>
  <p>DevTools edits are temporary — they vanish on page reload. Always copy changes back to your stylesheet.</p>
</div>

<h2 class="lesson-section-title" id="box-model-view">Box Model Diagram</h2>
<p>At the bottom of the Styles pane you will find a visual box model diagram. Hover over each area (content, padding, border, margin) to highlight it on the page. This is the fastest way to answer "where is all this extra space coming from?"</p>""",
    kc=[("What keyboard shortcut opens DevTools?","opening"),("What does a strikethrough mean in the Styles pane?","elements-panel"),("How do you test a CSS change without touching files?","live-css"),("Where is the box model diagram in DevTools?","box-model-view")],
    assignments=["Open DevTools on your Recipes project. Inspect the h1 and trace every rule applied to it.","Use live CSS editing to change a background colour and font. Copy the values back into your stylesheet."],
    resources=[("Chrome DevTools — Get started with CSS","https://developer.chrome.com/docs/devtools/css/"),("YouTube — Chrome DevTools Full Tutorial (Traversy Media)","https://www.youtube.com/watch?v=x4q86IjJFag"),("MDN — What are browser developer tools?","https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/What_are_browser_developer_tools")])

    # ── the-box-model ───────────────────────────────────────
    write("the-box-model","The Box Model",
    intro="Every HTML element is a rectangular box. Understanding how boxes are sized and spaced is the single most important concept for CSS layout.",
    overview=["Name the four areas of the CSS box model.","Understand content-box vs border-box sizing.","Use margin, padding, and border correctly."],
    body="""
<h2 class="lesson-section-title" id="four-areas">The Four Areas</h2>""" + code(""".card {
  width: 320px;       /* CONTENT area */
  padding: 24px;      /* PADDING — space between content and border */
  border: 2px solid #e2e8f0;  /* BORDER */
  margin: 32px;       /* MARGIN — space outside, between elements */
}
""") + """
<h2 class="lesson-section-title" id="box-sizing">border-box — The Fix</h2>""" + code("""/* DEFAULT (content-box): actual width = 300+24+24+2+2 = 352px */
.box { width: 300px; padding: 24px; border: 2px solid black; }

/* BETTER (border-box): actual width = exactly 300px */
.box { box-sizing: border-box; width: 300px; padding: 24px; border: 2px solid black; }

/* Add this to EVERY stylesheet you write */
*, *::before, *::after {
  box-sizing: border-box;
}
""") + """
<h2 class="lesson-section-title" id="margin-padding">Margin vs. Padding</h2>""" + code("""/* PADDING — inside the element, background fills this area */
.button {
  padding: 12px 24px;
  background: #2563eb; /* blue fills content + padding */
}

/* MARGIN — outside the element, always transparent */
.section {
  margin: 0 auto;      /* centre a block element */
  margin-bottom: 32px;
}
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Vertical margins between block elements collapse — only the larger value applies, not the sum of both. This surprises almost everyone the first time.</p>
</div>""",
    kc=[("Name the four box model areas from inside to outside.","four-areas"),("What does box-sizing: border-box change?","box-sizing"),("What is the practical difference between margin and padding?","margin-padding")],
    assignments=["Add the universal border-box rule to your stylesheet. Build a card component with explicit padding, border, and margin, and verify dimensions in DevTools.","Work through the CSS Box Model exercises linked below."],
    resources=[("MDN — The Box Model","https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model"),("The Odin Project — CSS Foundations Exercises","https://github.com/TheOdinProject/css-exercises"),("YouTube — The Box Model (Kevin Powell)","https://www.youtube.com/watch?v=rIO5326FgPE")])

    # ── block-and-inline ────────────────────────────────────
    write("block-and-inline","Block and Inline",
    intro="Every HTML element has a default display behaviour. Understanding block versus inline is foundational for understanding why layouts behave the way they do.",
    overview=["Explain the difference between block and inline elements.","Know which common elements are block and which are inline.","Use the display property to change behaviour."],
    body="""
<h2 class="lesson-section-title" id="block">Block Elements</h2>
<p>Block elements start on a new line and take up the full available width. You can freely set width, height, padding, and margin.</p>""" + code("""/* Common block elements */
div, p, h1, h2, h3, h4, h5, h6,
ul, ol, li, section, article,
header, footer, nav, main, form
""") + """
<h2 class="lesson-section-title" id="inline">Inline Elements</h2>
<p>Inline elements flow within text and only take up as much width as their content. Setting width, height, or vertical margin has no effect.</p>""" + code("""/* Common inline elements */
span, a, strong, em, img, input, button, label, code

/* Inline elements flow within surrounding text */
<p>
  Here is a paragraph with <strong>bold text</strong> and
  <a href="#">a link</a> flowing naturally within the sentence.
</p>
""") + """
<h2 class="lesson-section-title" id="display">Changing Display</h2>""" + code("""/* Make inline element behave as block */
span { display: block; }

/* Make block element sit inline */
div { display: inline; }

/* Inline position, block sizing */
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
    kc=[("What is the main difference between block and inline elements?","block"),("Why does setting width have no effect on inline elements?","inline"),("What does display: inline-block give you that inline does not?","display")],
    assignments=["In DevTools, inspect a p (block) and a span (inline). Compare their computed display values.","Work through the Block and Inline exercises linked below."],
    resources=[("MDN — Block and Inline Layout","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flow_layout/Block_and_inline_layout_in_normal_flow"),("The Odin Project — CSS Foundations Exercises","https://github.com/TheOdinProject/css-exercises"),("YouTube — Block vs Inline vs Inline-Block (Web Dev Simplified)","https://www.youtube.com/watch?v=x_i2gga-sYg")])

    # ── introduction-to-flexbox ─────────────────────────────
    write("introduction-to-flexbox","Introduction to Flexbox",
    intro="Flexbox solves layout problems that were previously painful hacks. Vertically centring an element used to be notoriously hard. With Flexbox it is one line.",
    overview=["Activate Flexbox with display: flex.","Understand flex containers and flex items.","Use justify-content and align-items for alignment."],
    body="""
<h2 class="lesson-section-title" id="container-items">Containers and Items</h2>""" + code("""<div class="container">
  <div class="item">One</div>
  <div class="item">Two</div>
  <div class="item">Three</div>
</div>
""") + code(""".container {
  display: flex;  /* all children become flex items, line up in a row */
  gap: 1rem;      /* space between items */
}
""") + """
<h2 class="lesson-section-title" id="axes">Main Axis and Cross Axis</h2>""" + code("""/* Default: main axis = horizontal (left to right) */
.container { display: flex; flex-direction: row; }

/* Switch: main axis = vertical (top to bottom) */
.container { display: flex; flex-direction: column; }
""") + """
<h2 class="lesson-section-title" id="alignment">Alignment</h2>""" + code("""/* justify-content = main axis alignment */
/* align-items    = cross axis alignment */

/* Centre everything — the holy grail */
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
  <p>Play Flexbox Froggy to build intuition for alignment — it covers all Flexbox concepts through a fun puzzle game.</p>
</div>""",
    kc=[("What property activates Flexbox on a container?","container-items"),("What is the difference between main axis and cross axis?","axes"),("Which property aligns items along the main axis?","alignment"),("Which property aligns items along the cross axis?","alignment")],
    assignments=["Build a horizontal nav bar with evenly spaced links using Flexbox.","Centre a div both horizontally and vertically using Flexbox.","Play Flexbox Froggy and complete all 24 levels."],
    resources=[("Flexbox Froggy — Learn Flexbox with a game","https://flexboxfroggy.com/"),("CSS Tricks — Complete Guide to Flexbox","https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),("MDN — Flexbox","https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox"),("YouTube — Flexbox in 20 Minutes (Traversy Media)","https://www.youtube.com/watch?v=JJSoEo8JSnc")])

    # ── growing-and-shrinking ───────────────────────────────
    write("growing-and-shrinking","Growing and Shrinking",
    intro="The real power of Flexbox is making items grow to fill space or shrink to fit. This lesson explains the flex shorthand and its three components.",
    overview=["Understand the flex shorthand property.","Explain flex-grow, flex-shrink, and flex-basis.","Know the most common flex values and what they produce."],
    body="""
<h2 class="lesson-section-title" id="shorthand">The flex Shorthand</h2>""" + code("""/* flex: grow shrink basis */
.item { flex: 1; }          /* flex: 1 1 0  — grow, shrink, start from zero */
.item { flex: 2; }          /* grows twice as fast as flex: 1 */
.item { flex: 0 0 200px; }  /* fixed 200px, never grows or shrinks */
.item { flex: 1 1 auto; }   /* grows and shrinks from natural size */
""") + """
<h2 class="lesson-section-title" id="flex-grow">flex-grow</h2>""" + code(""".container { display: flex; }

.item-a { flex-grow: 1; }  /* 1 share */
.item-b { flex-grow: 2; }  /* 2 shares — twice as wide as item-a */
.item-c { flex-grow: 1; }  /* 1 share */
/* Total: 4 shares. item-b = 50%, item-a and item-c = 25% each */
""") + """
<h2 class="lesson-section-title" id="flex-shrink">flex-shrink</h2>""" + code(""".sidebar {
  flex-shrink: 0;   /* sidebar never shrinks, holds its width */
  width: 250px;
}
.main {
  flex-grow: 1;     /* main takes all remaining space */
  flex-shrink: 1;   /* can shrink if needed */
}
""") + """
<h2 class="lesson-section-title" id="flex-basis">flex-basis</h2>""" + code("""/* Equal-width columns — most common pattern */
.item { flex: 1; }  /* all items share space equally */

/* Cards that wrap responsively */
.card {
  flex: 1 1 280px;  /* grow and shrink, but never below 280px */
}
"""),
    kc=[("What three properties does the flex shorthand combine?","shorthand"),("What does flex-grow: 2 mean compared to flex-grow: 1?","flex-grow"),("What does flex-shrink: 0 do?","flex-shrink"),("What is the difference between flex-basis: auto and flex-basis: 0?","flex-basis")],
    assignments=["Build a two-column layout: fixed sidebar (flex-shrink: 0) and growing main content (flex-grow: 1).","Build a responsive card grid using flex: 1 1 250px and flex-wrap: wrap."],
    resources=[("MDN — Controlling Ratios of Flex Items","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Controlling_ratios_of_flex_items_along_the_main_axis"),("CSS Tricks — Complete Guide to Flexbox","https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),("YouTube — Flexbox Growing and Shrinking (Kevin Powell)","https://www.youtube.com/watch?v=sanRCfIcNaQ")])

    # ── axes ────────────────────────────────────────────────
    write("axes","Axes",
    intro="Everything in Flexbox revolves around two axes. This lesson digs into how changing flex-direction flips those axes and how flex-wrap enables responsive layouts.",
    overview=["Use flex-direction to change the main axis.","Understand how switching axes changes alignment behaviour.","Use flex-wrap to create responsive layouts."],
    body="""
<h2 class="lesson-section-title" id="flex-direction">flex-direction</h2>""" + code(""".container {
  display: flex;
  flex-direction: row;            /* default — left to right */
  flex-direction: row-reverse;    /* right to left */
  flex-direction: column;         /* top to bottom */
  flex-direction: column-reverse; /* bottom to top */
}
""") + """
<h2 class="lesson-section-title" id="axis-flip">How Axes Flip</h2>""" + code("""/* ROW: justify-content = horizontal, align-items = vertical */
.row-container {
  display: flex;
  flex-direction: row;
  justify-content: center;  /* horizontal */
  align-items: center;       /* vertical */
}

/* COLUMN: justify-content = vertical, align-items = horizontal */
.col-container {
  display: flex;
  flex-direction: column;
  justify-content: center;  /* vertical now */
  align-items: center;       /* horizontal now */
}
""") + """
<h2 class="lesson-section-title" id="flex-wrap">flex-wrap</h2>""" + code(""".container {
  display: flex;
  flex-wrap: wrap;   /* items wrap to next line when needed */
  gap: 1rem;
}

/* Responsive cards — zero media queries needed */
.card {
  flex: 1 1 280px;
  /* grows to fill space, wraps when container < 280px */
}
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Remember: justify-content always targets the <em>main axis</em> and align-items always targets the <em>cross axis</em>. The axes flip when flex-direction changes.</p>
</div>""",
    kc=[("When flex-direction is column, which axis does justify-content control?","axis-flip"),("What does flex-wrap: wrap do?","flex-wrap"),("How can you build a responsive card layout with no media queries?","flex-wrap")],
    assignments=["Build a layout and toggle between flex-direction: row and column. Observe how alignment changes.","Build a responsive card grid using flex-wrap: wrap — no media queries allowed."],
    resources=[("MDN — flex-direction","https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction"),("CSS Tricks — Complete Guide to Flexbox","https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),("YouTube — Flexbox Axes (Web Dev Simplified)","https://www.youtube.com/watch?v=3YW65K6LcIA")])

    # ── alignment ───────────────────────────────────────────
    write("alignment","Alignment",
    intro="This lesson covers the complete set of Flexbox alignment tools so you can position elements exactly where you want them with confidence.",
    overview=["Use justify-content, align-items, and align-self.","Use align-content for multi-line containers.","Use the gap property for clean spacing."],
    body="""
<h2 class="lesson-section-title" id="justify">justify-content</h2>""" + code(""".container {
  display: flex;
  justify-content: flex-start;     /* packed to start (default) */
  justify-content: flex-end;       /* packed to end */
  justify-content: center;         /* centred */
  justify-content: space-between;  /* equal gaps between, none at edges */
  justify-content: space-around;   /* equal gaps around each item */
  justify-content: space-evenly;   /* equal gaps everywhere */
}
""") + """
<h2 class="lesson-section-title" id="align-items">align-items</h2>""" + code(""".container {
  display: flex;
  align-items: stretch;     /* items fill cross axis (default) */
  align-items: flex-start;  /* items align to start */
  align-items: flex-end;    /* items align to end */
  align-items: center;      /* items centred on cross axis */
  align-items: baseline;    /* items aligned by text baseline */
}
""") + """
<h2 class="lesson-section-title" id="align-self">align-self</h2>""" + code(""".container { display: flex; align-items: flex-start; }
.special   { align-self: center; }  /* this one item overrides */
""") + """
<h2 class="lesson-section-title" id="gap">gap</h2>""" + code(""".container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;           /* equal gap in all directions */
  gap: 1rem 2rem;      /* row-gap then column-gap */
}
/* gap only adds space BETWEEN items, not at the edges */
"""),
    kc=[("What is the difference between align-items and align-self?","align-self"),("When does align-content have any effect?","align-items"),("Why is gap better than using margins on individual flex items?","gap")],
    assignments=["Build a page header: logo left, nav links right, using only Flexbox alignment.","Build a three-column footer: left text, centred text, right text.","Complete all remaining Flexbox Froggy levels."],
    resources=[("Flexbox Froggy","https://flexboxfroggy.com/"),("CSS Tricks — Complete Guide to Flexbox","https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),("MDN — Aligning Items in Flexbox","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Aligning_items_in_a_flex_container"),("YouTube — Flexbox Alignment (Kevin Powell)","https://www.youtube.com/watch?v=u044iM9xsWU")])

    # ── project-landing-page ────────────────────────────────
    write("project-landing-page","Project: Landing Page",
    intro="You have learned enough HTML and CSS to build something that looks like a real website. In this project you will design and build a full landing page from scratch.",
    overview=["Translate a visual design into working HTML and CSS.","Use Flexbox for all layout.","Apply typography, colour, and spacing for a polished result.","Push the finished project to GitHub Pages."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>Header</strong> — logo/name on left, navigation links on right (Flexbox)</li>
  <li><strong>Hero section</strong> — large heading, subtext, call-to-action button</li>
  <li><strong>Info section</strong> — four cards arranged in a row (Flexbox)</li>
  <li><strong>Quote section</strong> — centred testimonial or inspirational quote</li>
  <li><strong>Footer</strong> — simple centred call to action</li>
</ul>

<h2 class="lesson-section-title" id="tips">Tips for Success</h2>
<ul>
  <li>Build one section at a time. Do not move to the next until the current one looks right.</li>
  <li>Use DevTools constantly to tweak values live before committing them to your CSS.</li>
  <li>Do not aim for pixel perfection — aim for "close enough and moving forward".</li>
</ul>

<h2 class="lesson-section-title" id="github-pages">Publishing on GitHub Pages</h2>""" + code("""# After pushing to GitHub:
# 1. Go to your repo on github.com
# 2. Click Settings → Pages
# 3. Source: Deploy from branch → main → / (root)
# 4. Click Save
# 5. Your site is live at: https://USERNAME.github.io/REPO-NAME/
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>GitHub Pages is free hosting for static HTML/CSS/JS sites. Every project you build from now on can be published and shared this way.</p>
</div>""",
    kc=[("What Flexbox properties centre items both horizontally and vertically?","requirements"),("How do you publish a static site using GitHub Pages?","github-pages")],
    assignments=["Build the landing page meeting all five section requirements.","Push to GitHub and publish on GitHub Pages. Share the live URL."],
    resources=[("The Odin Project — Landing Page Project","https://www.theodinproject.com/lessons/foundations-landing-page"),("CSS Tricks — Complete Guide to Flexbox","https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),("YouTube — Build a Landing Page with HTML and CSS (Kevin Powell)","https://www.youtube.com/watch?v=p0bGHP-PXD4")])

    # ── variables-and-operators ─────────────────────────────
    write("variables-and-operators","Variables and Operators",
    intro="JavaScript is the programming language of the web. This lesson introduces its most fundamental building blocks: variables for storing data and operators for working with it.",
    overview=["Declare variables with let and const.","Understand the difference between let, const, and the older var.","Use arithmetic, comparison, and logical operators."],
    body="""
<h2 class="lesson-section-title" id="variables">Variables</h2>""" + code("""// const — cannot be reassigned (use this by default)
const name = "Alice";
const age = 25;
const isLoggedIn = true;

// let — can be reassigned (use when value needs to change)
let score = 0;
score = score + 10;  // OK
score += 10;         // Shorthand for the same thing

// var — old way, avoid it (confusing scoping rules)
var oldStyle = "avoid this";
""") + """
<h2 class="lesson-section-title" id="arithmetic">Arithmetic Operators</h2>""" + code("""const a = 10;
const b = 3;

console.log(a + b);   // 13  — addition
console.log(a - b);   // 7   — subtraction
console.log(a * b);   // 30  — multiplication
console.log(a / b);   // 3.333... — division
console.log(a % b);   // 1   — remainder (modulo)
console.log(a ** b);  // 1000 — exponentiation (10 to the power of 3)
""") + """
<h2 class="lesson-section-title" id="comparison">Comparison Operators</h2>""" + code("""// Always use === (strict equality) not == (loose equality)
5 === 5      // true
5 === "5"    // false — different types
5 !== 3      // true — strict not equal
10 > 7       // true
10 >= 10     // true
3 < 5        // true
""") + """
<h2 class="lesson-section-title" id="logical">Logical Operators</h2>""" + code("""true && true    // true  — AND: both must be true
true && false   // false
true || false   // true  — OR: at least one must be true
false || false  // false
!true           // false — NOT: inverts the value
!false          // true
"""),
    kc=[("When should you use const vs let?","variables"),("What does the % operator return?","arithmetic"),("What is the difference between == and ===?","comparison")],
    assignments=["Open your browser DevTools console (F12 → Console tab) and experiment with all operators above.","Create a small script that calculates the area and perimeter of a rectangle from width and height variables."],
    resources=[("MDN — JavaScript Variables","https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables"),("javascript.info — Variables","https://javascript.info/variables"),("YouTube — JavaScript Variables (Programming with Mosh)","https://www.youtube.com/watch?v=9emXNzqCKyg")])

    # ── data-types-and-conditionals ─────────────────────────
    write("data-types-and-conditionals","Data Types and Conditionals",
    intro="JavaScript works with different kinds of data. This lesson covers the main data types and how to write code that makes decisions based on conditions.",
    overview=["Identify the eight JavaScript data types.","Write if, else if, and else statements.","Use the ternary operator for concise conditionals.","Understand truthy and falsy values."],
    body="""
<h2 class="lesson-section-title" id="data-types">Data Types</h2>""" + code("""// Primitive types
const name    = "Alice";        // String
const age     = 25;             // Number
const price   = 9.99;           // Number (no separate float type)
const isAdmin = true;           // Boolean
const nothing = null;           // Null — intentional absence of value
let notSet;                     // Undefined — not yet assigned
const id      = Symbol("id");   // Symbol — unique identifier
const big     = 9007199254740991n; // BigInt — very large integers

// Reference type
const user    = { name: "Alice", age: 25 }; // Object
const colors  = ["red", "green", "blue"];    // Array (also an object)
""") + """
<h2 class="lesson-section-title" id="conditionals">Conditionals</h2>""" + code("""const score = 72;

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
<h2 class="lesson-section-title" id="ternary">Ternary Operator</h2>""" + code("""// Shorthand for simple if/else
// condition ? valueIfTrue : valueIfFalse

const age = 20;
const status = age >= 18 ? "adult" : "minor";
console.log(status); // "adult"

// Often used in template literals
const greeting = `Good ${hours < 12 ? "morning" : "afternoon"}!`;
""") + """
<h2 class="lesson-section-title" id="truthy-falsy">Truthy and Falsy</h2>""" + code("""// FALSY values — treated as false in conditions
false, 0, "", null, undefined, NaN

// TRUTHY — everything else
"hello", 1, [], {}, true

// Practical example
const username = "";
if (username) {
  console.log("Hello, " + username);
} else {
  console.log("Please enter a username"); // This runs — "" is falsy
}
"""),
    kc=[("What are the eight JavaScript data types?","data-types"),("What is the difference between null and undefined?","data-types"),("What does the ternary operator do?","ternary"),("Name four falsy values in JavaScript.","truthy-falsy")],
    assignments=["In the browser console, test all data types and log them with typeof to see what JavaScript reports.","Write a grading function that takes a score and returns a letter grade using if/else if."],
    resources=[("MDN — JavaScript Data Types","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures"),("javascript.info — Conditionals","https://javascript.info/ifelse"),("YouTube — JavaScript Data Types (Fireship)","https://www.youtube.com/watch?v=jWliQAmong3A")])

    # ── javascript-developer-tools ──────────────────────────
    write("javascript-developer-tools","JavaScript Developer Tools",
    intro="The browser console and debugger are your most important JavaScript tools. This lesson shows you how to use them to test code, find bugs, and understand what your programs are doing.",
    overview=["Use the browser console to run and test JavaScript.","Use console.log() effectively for debugging.","Set breakpoints and step through code in the debugger.","Read and interpret JavaScript error messages."],
    body="""
<h2 class="lesson-section-title" id="console">The Console</h2>""" + code("""// Open with F12 → Console tab

// Test any JavaScript instantly
2 + 2          // returns 4
"hello".length // returns 5

// Log values to the console
console.log("Hello, World!");
console.log("Score:", score, "Level:", level); // multiple values

// Other console methods
console.error("Something went wrong!"); // red error styling
console.warn("This might be a problem"); // yellow warning
console.table([{name: "Alice"}, {name: "Bob"}]); // table format
console.clear(); // clear the console
""") + """
<h2 class="lesson-section-title" id="errors">Reading Error Messages</h2>""" + code("""// ReferenceError — variable does not exist
console.log(myVariable); // ReferenceError: myVariable is not defined

// TypeError — wrong type or method does not exist
null.toUpperCase(); // TypeError: Cannot read properties of null

// SyntaxError — broken code structure
if (true { }   // SyntaxError: Unexpected token '{'

// Each error tells you: type, message, file name, and line number
// Always read the whole message before searching for answers
""") + """
<h2 class="lesson-section-title" id="debugger">The Debugger</h2>
<ol>
  <li>Open DevTools (F12) → Sources tab</li>
  <li>Click a line number to set a breakpoint (blue dot appears)</li>
  <li>Reload the page — execution pauses at your breakpoint</li>
  <li>Use the controls: Step Over (F10), Step Into (F11), Resume (F8)</li>
  <li>Hover over any variable to see its current value</li>
</ol>""" + code("""// You can also trigger the debugger from code
function calculateTotal(items) {
  debugger; // execution pauses here when DevTools is open
  return items.reduce((sum, item) => sum + item.price, 0);
}
"""),
    kc=[("How do you open the browser console?","console"),("What does a ReferenceError mean?","errors"),("How do you set a breakpoint in the Sources tab?","debugger")],
    assignments=["Open the console and write at least 10 different JavaScript expressions. Use all console methods listed above.","Introduce a deliberate bug into a small script and use the debugger to find it."],
    resources=[("MDN — JavaScript Debugging","https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong"),("Chrome DevTools — Debug JavaScript","https://developer.chrome.com/docs/devtools/javascript/"),("YouTube — How to use the JS Debugger (Fireship)","https://www.youtube.com/watch?v=H0XScE08hy8")])

    # ── function-basics ─────────────────────────────────────
    write("function-basics","Function Basics",
    intro="Functions let you write a block of code once and run it as many times as needed. They are the most important tool for organising JavaScript.",
    overview=["Define functions with the function keyword and with arrow syntax.","Understand parameters, arguments, and return values.","Understand function scope."],
    body="""
<h2 class="lesson-section-title" id="declaring">Declaring Functions</h2>""" + code("""// Function declaration
function greet(name) {
  return "Hello, " + name + "!";
}

const message = greet("Alice");
console.log(message); // "Hello, Alice!"

// Function expression
const double = function(n) {
  return n * 2;
};

// Arrow function (modern, concise)
const square = (n) => n * n;
const add    = (a, b) => a + b;

// Arrow function with multiple lines needs curly braces and return
const calculateArea = (width, height) => {
  const area = width * height;
  return area;
};
""") + """
<h2 class="lesson-section-title" id="params">Parameters and Arguments</h2>""" + code("""// Parameters are the names in the function definition
function add(a, b) {   // a and b are parameters
  return a + b;
}

// Arguments are the actual values passed when calling
add(3, 7);  // 3 and 7 are arguments — result: 10

// Default parameters
function greet(name = "stranger") {
  return "Hello, " + name + "!";
}
greet();          // "Hello, stranger!"
greet("Alice");   // "Hello, Alice!"
""") + """
<h2 class="lesson-section-title" id="scope">Function Scope</h2>""" + code("""const globalVar = "I am everywhere";

function myFunction() {
  const localVar = "I only exist inside this function";
  console.log(globalVar); // Works — can access outer scope
  console.log(localVar);  // Works — in scope
}

myFunction();
console.log(globalVar); // Works
console.log(localVar);  // ReferenceError — localVar is out of scope
"""),
    kc=[("What is the difference between a parameter and an argument?","params"),("What does the return statement do?","declaring"),("Can you access a variable declared inside a function from outside it?","scope")],
    assignments=["Write a function that converts Celsius to Fahrenheit: (C × 9/5) + 32.","Write a function that takes two numbers and returns the larger one without using Math.max.","Rewrite both functions using arrow function syntax."],
    resources=[("MDN — Functions","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions"),("javascript.info — Functions","https://javascript.info/function-basics"),("YouTube — JavaScript Functions (Programming with Mosh)","https://www.youtube.com/watch?v=N8ap4k_1QEQ")])

    # ── problem-solving ─────────────────────────────────────
    write("problem-solving","Problem Solving",
    intro="Writing code is not the hard part of programming — solving problems is. This lesson gives you a repeatable framework for breaking down any problem before writing a single line of code.",
    overview=["Apply a systematic framework to any coding problem.","Use pseudocode to plan solutions before coding.","Break complex problems into smaller, testable pieces."],
    body="""
<h2 class="lesson-section-title" id="framework">The Problem-Solving Framework</h2>
<ol>
  <li><strong>Understand the problem.</strong> Read it multiple times. Restate it in your own words. If you cannot explain it simply, you do not understand it yet.</li>
  <li><strong>Plan the solution.</strong> Write pseudocode — plain English steps. Do not think about syntax yet.</li>
  <li><strong>Divide and conquer.</strong> Break the problem into the smallest possible sub-problems. Solve each one separately.</li>
  <li><strong>Implement.</strong> Now write the code, one sub-problem at a time.</li>
  <li><strong>Test.</strong> Check each piece works. Use console.log to verify values at each step.</li>
</ol>

<h2 class="lesson-section-title" id="pseudocode">Writing Pseudocode</h2>""" + code("""// Problem: Write a function that finds all even numbers
// from 1 to n and returns them in an array.

// PSEUDOCODE (plain English, no syntax):
// 1. Create an empty array to store results
// 2. Loop from 1 to n
// 3. For each number, check if it is divisible by 2
// 4. If yes, add it to the array
// 5. After the loop, return the array

// NOW write the code from the pseudocode:
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
<p>When stuck, explain your code out loud step by step — to a colleague, to yourself, or to a rubber duck on your desk. The act of articulating the problem almost always reveals where your thinking broke down. This technique is used by professional developers daily.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Before Googling, try explaining the problem out loud. "I am trying to do X. I expected Y. Instead I got Z. The part I do not understand is..." — often you will solve it before finishing the sentence.</p>
</div>""",
    kc=[("What are the five steps of the problem-solving framework?","framework"),("What is pseudocode and why write it before coding?","pseudocode"),("What is rubber duck debugging?","rubber-duck")],
    assignments=["Before coding any solution this week, write pseudocode first — no exceptions.","Solve the FizzBuzz problem: print numbers 1–100, replacing multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'."],
    resources=[("javascript.info — Coding Style","https://javascript.info/coding-style"),("YouTube — How to Think Like a Programmer (Coding Tech)","https://www.youtube.com/watch?v=azcrPFhaY9k"),("YouTube — FizzBuzz Explained (Web Dev Simplified)","https://www.youtube.com/watch?v=sxPtMVfmMdo")])

    # ── understanding-errors ────────────────────────────────
    write("understanding-errors","Understanding Errors",
    intro="Errors are not failures — they are the JavaScript engine telling you exactly what went wrong. Learning to read error messages fluently is a superpower that dramatically speeds up debugging.",
    overview=["Read and interpret JavaScript error messages.","Distinguish between the most common error types.","Use the stack trace to find where an error originated."],
    body="""
<h2 class="lesson-section-title" id="anatomy">Anatomy of an Error</h2>""" + code("""// Example error message:
// TypeError: Cannot read properties of null (reading 'textContent')
//     at updateDisplay (app.js:24:15)
//     at init (app.js:42:3)

// It tells you:
// 1. Error TYPE   — TypeError
// 2. What happened — Cannot read properties of null
// 3. What it tried to do — reading 'textContent'
// 4. Stack trace  — which functions called which, with line numbers
""") + """
<h2 class="lesson-section-title" id="common-errors">Common Error Types</h2>""" + code("""// ReferenceError — variable does not exist
console.log(myVar); // ReferenceError: myVar is not defined
// Fix: declare the variable with const or let

// TypeError — wrong type for the operation
null.toUpperCase(); // TypeError: Cannot read properties of null
const num = 42;
num();              // TypeError: num is not a function
// Fix: check the variable is what you think it is

// SyntaxError — broken code structure (often caught before running)
if (true {          // SyntaxError: Unexpected token '{'
function() {}       // SyntaxError: Function statements require a name
// Fix: check your brackets, semicolons, and keywords

// RangeError — value out of allowed range
new Array(-1);      // RangeError: Invalid array length
(1.2345).toFixed(200); // RangeError: toFixed() digits argument must be...
""") + """
<h2 class="lesson-section-title" id="stack-trace">Reading the Stack Trace</h2>""" + code("""// Stack trace shows the call chain that led to the error
// Read it from TOP (where the error happened) to BOTTOM (where it started)

function c() { null.split(""); }  // Error happens here
function b() { c(); }
function a() { b(); }
a();

// Stack trace:
// TypeError: Cannot read properties of null
//   at c (script.js:1:12)   ← where error happened
//   at b (script.js:2:14)
//   at a (script.js:3:14)   ← where it started
"""),
    kc=[("What four pieces of information does an error message contain?","anatomy"),("What causes a ReferenceError?","common-errors"),("How do you read a stack trace?","stack-trace")],
    assignments=["Deliberately trigger each of the four error types in the console and read the message carefully.","Find a bug in a small script using only the error message and stack trace — no random changes allowed."],
    resources=[("MDN — JavaScript Error Reference","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors"),("javascript.info — Error Handling","https://javascript.info/error-handling"),("YouTube — JavaScript Errors Explained (Web Dev Simplified)","https://www.youtube.com/watch?v=cFTFtuEQ-10")])

    # ── project-rock-paper-scissors ─────────────────────────
    write("project-rock-paper-scissors","Project: Rock Paper Scissors",
    intro="Your first JavaScript project. You will build a console-based Rock Paper Scissors game — no UI yet, just logic. This focuses entirely on writing clean JavaScript functions.",
    overview=["Write functions that make decisions with conditionals.","Generate random computer choices.","Determine a winner and track scores.","Run the game from the browser console."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>A function that returns a random computer choice (rock, paper, or scissors)</li>
  <li>A function that compares player and computer choices and returns the round result</li>
  <li>A function that plays five rounds and returns the final score</li>
  <li>Results logged to the console with clear descriptions</li>
</ul>

<h2 class="lesson-section-title" id="getting-started">Getting Started</h2>""" + code("""// Create your project
mkdir ~/devpath-projects/rock-paper-scissors
cd ~/devpath-projects/rock-paper-scissors
git init
touch script.js

// Open in VS Code
code .
""") + code("""// A starting point — build from here

function getComputerChoice() {
  const choices = ["rock", "paper", "scissors"];
  const randomIndex = Math.floor(Math.random() * 3);
  return choices[randomIndex];
}

function playRound(playerChoice, computerChoice) {
  // TODO: compare choices and return "win", "lose", or "draw"
}

function game() {
  // TODO: play 5 rounds, track score, return final result
}

// Test it in the console
console.log(getComputerChoice()); // Should log rock, paper, or scissors
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Commit after completing each function. Small, frequent commits mean if something breaks you can always roll back to the last working state.</p>
</div>""",
    kc=[("How do you generate a random integer between 0 and 2 in JavaScript?","getting-started"),("What functions are needed to build this game?","requirements")],
    assignments=["Complete the Rock Paper Scissors game fulfilling all requirements.","Push to GitHub and publish on GitHub Pages."],
    resources=[("MDN — Math.random()","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random"),("javascript.info — Comparisons","https://javascript.info/comparison"),("YouTube — Rock Paper Scissors in JavaScript (Web Dev Simplified)","https://www.youtube.com/watch?v=1yS-JV4fWqY")])

    # ── clean-code ──────────────────────────────────────────
    write("clean-code","Clean Code",
    intro="Code is written once but read many times. Clean code is code that other developers — and future you — can understand immediately. This lesson covers the habits that make the difference.",
    overview=["Write descriptive, self-documenting variable and function names.","Know when and how to write useful comments.","Keep functions small and focused on one thing.","Format code consistently."],
    body="""
<h2 class="lesson-section-title" id="naming">Naming Things Well</h2>""" + code("""// Bad names — what do these mean?
const d = 7;
const arr = ["Alice", "Bob", "Charlie"];
function calc(x, y) { return x * y; }

// Good names — self-documenting
const daysInWeek = 7;
const userNames  = ["Alice", "Bob", "Charlie"];
function calculateRectangleArea(width, height) { return width * height; }

// Boolean names should read like yes/no questions
const isLoggedIn  = true;
const hasPermission = false;
const canEdit     = user.role === "admin";

// Functions should describe their action
getUserById(id);
validateEmailFormat(email);
renderProductCard(product);
""") + """
<h2 class="lesson-section-title" id="comments">When to Comment</h2>""" + code("""// BAD — comments that just repeat the code
// Add 1 to count
count += 1;

// GOOD — comments that explain WHY, not WHAT
// Offset by 1 because API returns 0-indexed results
const displayIndex = apiIndex + 1;

// GOOD — comments that explain complex logic
// Haversine formula — calculates great-circle distance between two GPS points
const a = Math.sin(dLat/2) ** 2 + Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon/2) ** 2;
""") + """
<h2 class="lesson-section-title" id="functions">Small, Focused Functions</h2>""" + code("""// BAD — one giant function that does everything
function processUserRegistration(data) {
  // validates email... fetches from DB... hashes password...
  // sends welcome email... logs analytics... 80 more lines
}

// GOOD — each function does one thing
function validateRegistrationData(data) { ... }
function checkIfEmailExists(email) { ... }
function hashPassword(password) { ... }
function sendWelcomeEmail(user) { ... }
function trackRegistrationEvent(userId) { ... }

async function registerUser(data) {
  validateRegistrationData(data);
  const exists = await checkIfEmailExists(data.email);
  if (exists) throw new Error("Email already registered");
  const hashedPassword = await hashPassword(data.password);
  const user = await createUser({ ...data, password: hashedPassword });
  sendWelcomeEmail(user);
  trackRegistrationEvent(user.id);
  return user;
}
"""),
    kc=[("What makes a variable name 'good'?","naming"),("When should you write a comment?","comments"),("What is the single responsibility principle for functions?","functions")],
    assignments=["Review your Rock Paper Scissors project and rename any variables or functions that are unclear.","Refactor any function longer than 10 lines into smaller, named sub-functions."],
    resources=[("javascript.info — Coding Style","https://javascript.info/coding-style"),("YouTube — Clean Code (Fireship)","https://www.youtube.com/watch?v=4jFJ3BGKL0E"),("Article — Clean Code JavaScript (ryanmcdermott)","https://github.com/ryanmcdermott/clean-code-javascript")])

    # ── installing-nodejs ───────────────────────────────────
    write("installing-nodejs","Installing Node.js",
    intro="Node.js lets you run JavaScript outside the browser — on your computer or a server. It is also required by most JavaScript development tools, build systems, and package managers.",
    overview=["Understand what Node.js is and why it is needed.","Install Node.js using NVM.","Use npm to install packages.","Run JavaScript files from the terminal."],
    body="""
<h2 class="lesson-section-title" id="what-is-node">What Is Node.js?</h2>
<p>Node.js is a JavaScript runtime built on Chrome's V8 engine. It allows JavaScript to run outside the browser — reading files, making network requests, building servers. It also powers tools like Webpack, Vite, ESLint, and Prettier that you will use throughout this curriculum.</p>

<h2 class="lesson-section-title" id="install">Installing with NVM</h2>""" + code("""# Install NVM (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Restart your terminal, then install the LTS version
nvm install --lts
nvm use --lts

# Verify installation
node --version   # Should show v20.x.x or similar
npm --version    # Should show 10.x.x or similar
""") + """
<h2 class="lesson-section-title" id="running">Running JavaScript Files</h2>""" + code("""# Create a file
echo 'console.log("Hello from Node.js!")' > hello.js

# Run it with Node
node hello.js
# Output: Hello from Node.js!

# Interactive REPL (like the browser console)
node
> 2 + 2
4
> "hello".toUpperCase()
'HELLO'
> .exit   # or Ctrl+C twice to quit
""") + """
<h2 class="lesson-section-title" id="npm">npm Basics</h2>""" + code("""# Initialise a project (creates package.json)
npm init -y

# Install a package
npm install lodash

# Install a dev-only package (not included in production)
npm install --save-dev jest

# Run a script defined in package.json
npm run test
"""),
    kc=[("What is Node.js used for?","what-is-node"),("Why install Node.js with NVM instead of directly?","install"),("What is npm and what is it used for?","npm")],
    assignments=["Install Node.js via NVM and verify with node --version.","Create a hello.js file and run it with node.","Run node in interactive mode and test five JavaScript expressions."],
    resources=[("NVM — GitHub Repository","https://github.com/nvm-sh/nvm"),("Node.js Official Docs","https://nodejs.org/en/docs/"),("YouTube — Node.js Crash Course (Traversy Media)","https://www.youtube.com/watch?v=fBNz5xF-Kx4")])

    # ── arrays-and-loops ────────────────────────────────────
    write("arrays-and-loops","Arrays and Loops",
    intro="Arrays store ordered collections of data. Loops process that data item by item. Together they are one of the most powerful patterns in all of programming.",
    overview=["Create and manipulate arrays.","Use for, while, and for...of loops.","Use essential array methods: forEach, map, filter, and reduce."],
    body="""
<h2 class="lesson-section-title" id="arrays">Arrays</h2>""" + code("""// Create an array
const fruits = ["apple", "banana", "cherry"];
const numbers = [1, 2, 3, 4, 5];
const mixed = [42, "hello", true, null]; // any types

// Access by index (zero-based)
console.log(fruits[0]);  // "apple"
console.log(fruits[2]);  // "cherry"

// Common array operations
fruits.push("date");      // add to end
fruits.pop();             // remove from end
fruits.unshift("avocado"); // add to start
fruits.shift();            // remove from start
console.log(fruits.length); // number of items

// Check if a value exists
console.log(fruits.includes("banana")); // true
console.log(fruits.indexOf("cherry"));  // 2
""") + """
<h2 class="lesson-section-title" id="loops">Loops</h2>""" + code("""// for loop — when you need the index
for (let i = 0; i < fruits.length; i++) {
  console.log(i, fruits[i]);
}

// for...of — cleaner when you just need the value
for (const fruit of fruits) {
  console.log(fruit);
}

// while loop — when you do not know how many iterations
let count = 0;
while (count < 5) {
  console.log(count);
  count++;
}
""") + """
<h2 class="lesson-section-title" id="array-methods">Array Methods</h2>""" + code("""const numbers = [1, 2, 3, 4, 5, 6];

// forEach — do something for each item (no return value)
numbers.forEach(n => console.log(n * 2));

// map — transform each item, return new array
const doubled = numbers.map(n => n * 2);
// [2, 4, 6, 8, 10, 12]

// filter — keep items that pass a test, return new array
const evens = numbers.filter(n => n % 2 === 0);
// [2, 4, 6]

// reduce — combine all items into one value
const sum = numbers.reduce((total, n) => total + n, 0);
// 21

// Chaining methods
const result = numbers
  .filter(n => n % 2 === 0)
  .map(n => n * 10);
// [20, 40, 60]
"""),
    kc=[("How do you access the third item in an array?","arrays"),("What is the difference between for and for...of?","loops"),("What is the difference between map and forEach?","array-methods"),("What does filter return?","array-methods")],
    assignments=["Create an array of 10 numbers and use map, filter, and reduce to: double all values, keep only numbers above 10, and sum the remaining numbers — in a chain.","Solve this: given an array of names, return a new array of names longer than 4 characters, capitalised."],
    resources=[("MDN — Array","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array"),("javascript.info — Arrays","https://javascript.info/array"),("YouTube — JavaScript Arrays (Web Dev Simplified)","https://www.youtube.com/watch?v=7W4pQQ20nJg")])

    # ── dom-manipulation-and-events ─────────────────────────
    write("dom-manipulation-and-events","DOM Manipulation and Events",
    intro="The DOM (Document Object Model) is how JavaScript sees and interacts with your HTML. Events are how you respond to user actions. Together they make pages come alive.",
    overview=["Select HTML elements using JavaScript.","Modify element content, attributes, and styles.","Create and remove elements dynamically.","Add event listeners to respond to user interactions."],
    body="""
<h2 class="lesson-section-title" id="selecting">Selecting Elements</h2>""" + code("""// querySelector — returns the FIRST matching element
const title   = document.querySelector("h1");
const btn     = document.querySelector("#submit-btn");
const card    = document.querySelector(".product-card");

// querySelectorAll — returns ALL matching elements (NodeList)
const allCards  = document.querySelectorAll(".card");
const allLinks  = document.querySelectorAll("nav a");

// Iterate over a NodeList
allCards.forEach(card => console.log(card.textContent));
""") + """
<h2 class="lesson-section-title" id="modifying">Modifying Elements</h2>""" + code("""const title = document.querySelector("h1");

// Change text content (safe — no HTML parsing)
title.textContent = "New Heading";

// Change HTML content (allows HTML tags)
title.innerHTML = "New <em>Heading</em>";

// Change styles
title.style.color = "#2563eb";
title.style.fontSize = "3rem";

// Change CSS classes (preferred over inline styles)
title.classList.add("highlight");
title.classList.remove("hidden");
title.classList.toggle("active");
title.classList.contains("active"); // true/false

// Change attributes
const img = document.querySelector("img");
img.setAttribute("src", "new-photo.jpg");
img.setAttribute("alt", "Updated description");
""") + """
<h2 class="lesson-section-title" id="creating">Creating Elements</h2>""" + code("""// Create a new element
const newCard = document.createElement("div");
newCard.classList.add("card");
newCard.textContent = "I am a new card";

// Add it to the page
document.body.appendChild(newCard);             // at the end of body
document.querySelector(".grid").prepend(newCard); // at the start of .grid

// Remove an element
const oldCard = document.querySelector(".old-card");
oldCard.remove();
""") + """
<h2 class="lesson-section-title" id="events">Events and Event Listeners</h2>""" + code("""const btn = document.querySelector("#my-button");

// addEventListener(eventType, callbackFunction)
btn.addEventListener("click", function(event) {
  console.log("Button clicked!");
  console.log(event.target); // the element that was clicked
});

// Arrow function shorthand
btn.addEventListener("click", (e) => {
  e.preventDefault(); // stop default browser behaviour (e.g. form submit)
  btn.textContent = "Clicked!";
  btn.classList.add("active");
});

// Common event types
// "click"      — mouse click
// "input"      — input field value changes
// "submit"     — form submitted
// "keydown"    — keyboard key pressed
// "mouseover"  — mouse enters element
// "DOMContentLoaded" — HTML fully loaded and parsed
"""),
    kc=[("What does querySelector return if there are multiple matches?","selecting"),("What is the difference between textContent and innerHTML?","modifying"),("How do you attach a function to run when a button is clicked?","events"),("What does event.preventDefault() do?","events")],
    assignments=["Build a page with a button that changes the background colour when clicked.","Build a counter: a displayed number that increases on '+' click and decreases on '-' click, with a reset button."],
    resources=[("MDN — Introduction to the DOM","https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction"),("javascript.info — DOM Tree","https://javascript.info/dom-nodes"),("YouTube — JavaScript DOM Manipulation (Web Dev Simplified)","https://www.youtube.com/watch?v=y17RuWkWdn8")])

    # ── revisiting-rock-paper-scissors ──────────────────────
    write("revisiting-rock-paper-scissors","Revisiting Rock Paper Scissors",
    intro="You built Rock Paper Scissors in the console. Now you will give it a real UI using DOM manipulation — buttons, a score display, and visual round results.",
    overview=["Add HTML buttons for rock, paper, and scissors.","Display round results and running score on the page.","Update the DOM in response to user clicks.","Apply what you know about events and DOM manipulation."],
    body="""
<h2 class="lesson-section-title" id="ui-requirements">UI Requirements</h2>
<ul>
  <li>Three buttons: Rock, Paper, Scissors</li>
  <li>A display area showing the round result ("You win! Paper beats Rock")</li>
  <li>A score display showing player vs computer score</li>
  <li>A Reset button that clears the score and result</li>
</ul>

<h2 class="lesson-section-title" id="structure">Suggested Structure</h2>""" + code("""<!-- HTML -->
<div class="game">
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
""") + code("""// JavaScript — connect the UI to your existing game logic
const buttons = document.querySelectorAll(".choice-btn");
const resultDisplay = document.getElementById("result-display");
const playerScoreEl = document.getElementById("player-score");
const computerScoreEl = document.getElementById("computer-score");

let playerScore = 0;
let computerScore = 0;

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const playerChoice = button.dataset.choice;
    const computerChoice = getComputerChoice();
    const result = playRound(playerChoice, computerChoice);

    if (result === "win") playerScore++;
    if (result === "lose") computerScore++;

    resultDisplay.textContent = `You ${result}! ${playerChoice} vs ${computerChoice}`;
    playerScoreEl.textContent = playerScore;
    computerScoreEl.textContent = computerScore;
  });
});
"""),
    kc=[("How do you read a button's data-choice attribute in JavaScript?","structure"),("What DOM methods do you need to update the score display?","structure")],
    assignments=["Add the full UI to your existing Rock Paper Scissors project.","Push the updated version to GitHub — it should auto-update on GitHub Pages."],
    resources=[("MDN — Using data attributes","https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes"),("javascript.info — DOM Events","https://javascript.info/introduction-browser-events"),("YouTube — Rock Paper Scissors UI (Web Dev Simplified)","https://www.youtube.com/watch?v=1yS-JV4fWqY")])

    # ── project-etch-a-sketch ───────────────────────────────
    write("project-etch-a-sketch","Project: Etch-a-Sketch",
    intro="Build a browser-based drawing pad where hovering over grid squares colours them in. This project combines DOM manipulation, dynamic element creation, and event handling.",
    overview=["Dynamically create a grid of divs using JavaScript.","Use mouseover events to colour grid squares.","Allow the user to set grid size.","Apply flexbox to create the grid layout."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>A 16×16 grid of square divs created by JavaScript (no hard-coding in HTML)</li>
  <li>Hovering over a square darkens it (or colours it)</li>
  <li>A button that asks for a new grid size (1–100) and re-generates the grid</li>
  <li>Grid always fills the same total container size regardless of grid dimensions</li>
</ul>

<h2 class="lesson-section-title" id="getting-started">Getting Started</h2>""" + code("""mkdir ~/devpath-projects/etch-a-sketch
cd ~/devpath-projects/etch-a-sketch
git init
touch index.html styles.css script.js
code .
""") + code("""// Create the grid dynamically
function createGrid(size) {
  const container = document.querySelector("#grid-container");
  container.innerHTML = ""; // clear any existing grid
  container.style.gridTemplateColumns = `repeat(${size}, 1fr)`;

  const totalSquares = size * size;
  for (let i = 0; i < totalSquares; i++) {
    const square = document.createElement("div");
    square.classList.add("grid-square");
    square.addEventListener("mouseover", () => {
      square.style.backgroundColor = "#2563eb";
    });
    container.appendChild(square);
  }
}

createGrid(16); // Start with a 16x16 grid

// Reset button
document.querySelector("#reset-btn").addEventListener("click", () => {
  const size = prompt("Enter grid size (1-100):");
  if (size >= 1 && size <= 100) createGrid(size);
});
""") + code("""/* CSS — grid container */
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
  <p>Stretch goal: instead of a solid colour on hover, progressively darken each square — each hover adds 10% more darkness until it is fully black.</p>
</div>""",
    kc=[("How do you create a 16x16 grid using only JavaScript?","getting-started"),("What event fires when the mouse moves over an element?","requirements")],
    assignments=["Complete the Etch-a-Sketch meeting all requirements.","Add the stretch goal: progressive darkening on hover.","Push to GitHub Pages."],
    resources=[("MDN — Document.createElement","https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement"),("MDN — CSS Grid Layout","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout"),("YouTube — Build Etch a Sketch (Web Dev Simplified)","https://www.youtube.com/watch?v=J8LKHwBCJTk")])

    # ── object-basics ───────────────────────────────────────
    write("object-basics","Object Basics",
    intro="Objects let you group related data and functions together. They are the fundamental building block of JavaScript and the foundation of all object-oriented programming.",
    overview=["Create objects with properties and methods.","Access and modify object properties using dot and bracket notation.","Understand 'this' inside object methods.","Use object destructuring and shorthand syntax."],
    body="""
<h2 class="lesson-section-title" id="creating-objects">Creating Objects</h2>""" + code("""// Object literal — most common way to create an object
const user = {
  name: "Alice",          // property: string
  age: 28,                // property: number
  isAdmin: false,         // property: boolean
  address: {              // nested object
    city: "Addis Ababa",
    country: "Ethiopia"
  },
  greet() {               // method (shorthand syntax)
    return `Hello, I am ${this.name}`;
  }
};

console.log(user.name);          // "Alice"
console.log(user.address.city);  // "Addis Ababa"
console.log(user.greet());       // "Hello, I am Alice"
""") + """
<h2 class="lesson-section-title" id="accessing">Accessing Properties</h2>""" + code("""// Dot notation — use when you know the property name
user.name = "Bob";
console.log(user.age);

// Bracket notation — use when property name is in a variable
const prop = "name";
console.log(user[prop]);  // "Bob"

// Useful for dynamic access
const fields = ["name", "age", "isAdmin"];
fields.forEach(field => console.log(user[field]));

// Check if a property exists
console.log("name" in user);  // true
console.log(user.hasOwnProperty("age")); // true
""") + """
<h2 class="lesson-section-title" id="this">this Keyword</h2>""" + code("""const counter = {
  count: 0,
  increment() {
    this.count++;  // 'this' refers to the counter object
    return this.count;
  },
  reset() {
    this.count = 0;
  }
};

counter.increment(); // 1
counter.increment(); // 2
counter.reset();
counter.increment(); // 1
""") + """
<h2 class="lesson-section-title" id="destructuring">Destructuring and Shorthand</h2>""" + code("""// Destructuring — extract properties into variables
const { name, age, isAdmin } = user;
console.log(name);    // "Bob"

// With rename
const { name: userName } = user;

// Shorthand property names
const x = 10;
const y = 20;
const point = { x, y };  // same as { x: x, y: y }

// Spread operator — copy or merge objects
const updatedUser = { ...user, age: 29 }; // copy with override
"""),
    kc=[("What is the difference between dot notation and bracket notation?","accessing"),("What does 'this' refer to inside an object method?","this"),("What does object destructuring do?","destructuring")],
    assignments=["Create an object representing a book with at least 5 properties and 2 methods. Log each property and call each method.","Write a function that takes an array of user objects and returns only the names of users over age 18."],
    resources=[("MDN — Working with Objects","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects"),("javascript.info — Objects","https://javascript.info/object"),("YouTube — JavaScript Objects (Web Dev Simplified)","https://www.youtube.com/watch?v=sTSLn1Sj3fc")])

    # ── project-calculator ──────────────────────────────────
    write("project-calculator","Project: Calculator",
    intro="The calculator is the capstone of the Foundations course. It brings together everything — HTML, CSS, Flexbox, DOM manipulation, events, and JavaScript logic — in one polished application.",
    overview=["Build a functional calculator with a clean UI.","Handle user input, operator logic, and display updates.","Manage calculator state across multiple button clicks.","Handle edge cases like dividing by zero."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Number buttons 0–9 and a decimal point</li>
  <li>Operator buttons: +, -, ×, ÷</li>
  <li>An equals button that calculates and displays the result</li>
  <li>A clear button (AC) that resets everything</li>
  <li>A display showing the current number or result</li>
  <li>Chaining: after pressing =, the result becomes the first operand of the next calculation</li>
  <li>Edge case: dividing by zero shows an error message</li>
</ul>

<h2 class="lesson-section-title" id="approach">Suggested Approach</h2>""" + code("""// Step 1: Build the HTML structure and style it with CSS first

// Step 2: Write the four math functions
function add(a, b)      { return a + b; }
function subtract(a, b) { return a - b; }
function multiply(a, b) { return a * b; }
function divide(a, b)   {
  if (b === 0) return "Error";
  return a / b;
}

// Step 3: Write operate() to call the right function
function operate(operator, a, b) {
  switch (operator) {
    case "+": return add(a, b);
    case "-": return subtract(a, b);
    case "×": return multiply(a, b);
    case "÷": return divide(a, b);
  }
}

// Step 4: Track state with variables
let firstOperand  = null;
let operator      = null;
let secondOperand = null;
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
  <p>Do not use eval() to calculate the result. It is a security risk and teaches you nothing. Implement operate() yourself.</p>
</div>""",
    kc=[("What four math functions does the calculator need?","approach"),("What state variables does the calculator need to track?","approach"),("How do you handle dividing by zero?","requirements")],
    assignments=["Complete the Calculator meeting all requirements above.","Push to GitHub and publish on GitHub Pages — this is your flagship Foundations project."],
    resources=[("MDN — JavaScript Reference","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference"),("youtube — Build a Calculator (Web Dev Simplified)","https://www.youtube.com/watch?v=j59qQ7YWLxw"),("javascript.info — Events","https://javascript.info/events")])

    # ── choose-your-path ────────────────────────────────────
    write("choose-your-path","Choose Your Path Forward",
    intro="Congratulations — you have completed the Foundations course. Look back at how far you have come and look forward to what comes next. Now it is time to choose your specialisation.",
    overview=["Reflect on what you have built in Foundations.","Understand what each specialisation path covers.","Make an informed choice between Full Stack JavaScript and Full Stack Ruby on Rails."],
    body="""
<h2 class="lesson-section-title" id="what-youve-done">What You Have Accomplished</h2>
<p>When you started, you may not have known what a terminal was. Now you can:</p>
<ul>
  <li>Build multi-page websites with semantic HTML</li>
  <li>Style them with CSS using Flexbox layouts</li>
  <li>Add interactivity with JavaScript and DOM manipulation</li>
  <li>Track your work with Git and publish to GitHub Pages</li>
  <li>Debug effectively using DevTools and error messages</li>
  <li>Think through problems systematically before writing code</li>
</ul>
<p>That is a real foundation. The next phase is where it gets exciting.</p>

<h2 class="lesson-section-title" id="javascript-path">Full Stack JavaScript Path</h2>
<p>This path stays in JavaScript — the language you have been learning. You will go significantly deeper into JavaScript itself, then learn React for sophisticated frontends and Node.js with Express for backend servers. Database: PostgreSQL.</p>
<p><strong>Choose this if:</strong> you enjoy JavaScript, want one language on both frontend and backend, or are excited by the modern web ecosystem (React, Node, APIs).</p>

<h2 class="lesson-section-title" id="rails-path">Full Stack Ruby on Rails Path</h2>
<p>This path introduces Ruby — a language celebrated for its elegant, readable syntax. Then you learn Rails, a backend framework famous for letting you build complete web applications very quickly. You also go deeper into HTML, CSS, and SQL.</p>
<p><strong>Choose this if:</strong> you want to try a new language, are drawn to rapid backend development, or prefer the structured, convention-driven Rails approach.</p>

<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>There is no wrong choice. Both lead to full-stack developer skills. Both are valued in the job market. The most important thing is to pick one and commit — do not switch back and forth.</p>
</div>
<div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap;">
  <a href="../../paths/full-stack-javascript/index.html" class="btn btn-primary">Start Full Stack JavaScript →</a>
  <a href="../../paths/full-stack-ruby-on-rails/index.html" class="btn btn-outline">Start Full Stack Ruby on Rails →</a>
</div>""",
    kc=[("What does the Full Stack JavaScript path use for backend development?","javascript-path"),("What framework does the Ruby on Rails path use?","rails-path"),("What is the most important factor when choosing a path?","rails-path")],
    assignments=["Choose your path and navigate to it — your next lesson is waiting.","Share which path you chose and why in the community."],
    resources=[("Full Stack JavaScript Path","../../paths/full-stack-javascript/index.html"),("Full Stack Ruby on Rails Path","../../paths/full-stack-ruby-on-rails/index.html"),("YouTube — JavaScript vs Ruby on Rails (Traversy Media)","https://www.youtube.com/watch?v=9RMmzLf5A6A")])

    print("\nAll 35 lessons seeded.")

if __name__ == "__main__":
    seed()
