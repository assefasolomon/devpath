#!/usr/bin/env python3
"""Seed: Advanced HTML/CSS, React, NodeJS, Getting Hired — Full Stack JS path"""
import os, subprocess

BASE = os.path.expanduser("~/devpath")
JS   = os.path.join(BASE, "paths", "full-stack-javascript", "courses")

LOGO = '<svg viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="13" stroke="currentColor" stroke-width="1.8"/><path d="M8 14 L14 7 L20 14 L14 21 Z" fill="currentColor"/></svg>'

def nav(root):
    return (
        '<nav class="site-nav">'
        f'<a href="{root}index.html" class="nav-logo">{LOGO} DevPath</a>'
        '<ul class="nav-links">'
        f'<li><a href="{root}index.html">Home</a></li>'
        f'<li><a href="{root}foundations/index.html">Foundations</a></li>'
        f'<li><a href="{root}paths/full-stack-javascript/index.html">Full Stack JS</a></li>'
        f'<li><a href="{root}paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a></li>'
        '</ul></nav>'
    )

def footer():
    return '<footer class="site-footer"><p>DevPath — A free, open, project-based web development curriculum.</p></footer>'

def code(snippet):
    esc = snippet.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f'<div class="code-block"><pre><code>{esc}</code></pre></div>'


# ── Generic lesson writer ────────────────────────────────────────────────────
def write_lesson(ldir, root, course_title, all_lessons, sidebar_html,
                 slug, title, intro, overview, body, kc, assignments, resources):
    idx  = next((i for i,l in enumerate(all_lessons) if l[0]==slug), None)
    p    = (all_lessons[idx-1][1], all_lessons[idx-1][0]+".html") if idx and idx>0 else None
    n    = (all_lessons[idx+1][1], all_lessons[idx+1][0]+".html") if idx is not None and idx<len(all_lessons)-1 else None

    pb   = f'<a href="{p[1]}" class="btn btn-blue-outline">&#8592; Previous</a>' if p else '<span></span>'
    nb   = f'<a href="{n[1]}" class="btn btn-blue">Next &#8594;</a>' if n else '<span></span>'
    navb = (f'<div class="lesson-nav-bar">'
            f'<div class="lesson-nav-bar-group">{pb}</div>'
            f'<div class="lesson-nav-bar-group"><button class="btn btn-green mark-complete-btn">Mark Completed</button></div>'
            f'<div class="lesson-nav-bar-group">{nb}</div>'
            f'</div>')

    bc   = (f'<nav class="breadcrumb">'
            f'<a href="{root}index.html">Home</a><span class="breadcrumb-sep">/</span>'
            f'<a href="{root}paths/full-stack-javascript/index.html">Full Stack JS</a><span class="breadcrumb-sep">/</span>'
            f'<a href="../index.html">{course_title}</a><span class="breadcrumb-sep">/</span>'
            f'<span class="breadcrumb-current">{title}</span></nav>')

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
        f'  <link rel="stylesheet" href="{root}css/styles.css">\n'
        '</head>\n<body>\n'
        + nav(root) + '\n'
        + navb + '\n'
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
        + f'<script src="{root}js/main.js"></script>\n</body>\n</html>'
    )
    # ✅ FIX 3: create output directory if it doesn't exist
    os.makedirs(ldir, exist_ok=True)
    with open(os.path.join(ldir, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  {slug}")


# ════════════════════════════════════════════════════════════════════════════
#  1. ADVANCED HTML AND CSS
# ════════════════════════════════════════════════════════════════════════════
def seed_advanced_html_css():
    ldir = os.path.join(JS, "advanced-html-css", "lessons")
    root = "../../../../../"
    course_title = "Advanced HTML and CSS"

    ALL = [
        ("transforms",                             "Transforms"),
        ("transitions",                            "Transitions"),
        ("keyframes",                              "Keyframes"),
        ("accessibility-intro",                    "Introduction to Accessibility"),
        ("the-web-content-accessibility-guidelines-adv", "The Web Content Accessibility Guidelines"),
        ("accessible-colors-adv",                  "Accessible Colors"),
        ("keyboard-navigation-adv",                "Keyboard Navigation"),
        ("meaningful-text-adv",                    "Meaningful Text"),
        ("wai-aria-adv",                           "WAI-ARIA"),
        ("natural-responsiveness-adv",             "Natural Responsiveness"),
        ("responsive-images-adv",                  "Responsive Images"),
        ("media-queries-adv",                      "Media Queries"),
        ("project-homepage-adv",                   "Project: Homepage"),
    ]

    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">Advanced HTML and CSS</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">Animation</div>'
        + lnk("transforms","Transforms") + lnk("transitions","Transitions") + lnk("keyframes","Keyframes")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Accessibility</div>'
        + lnk("accessibility-intro","Introduction to Accessibility")
        + lnk("the-web-content-accessibility-guidelines-adv","WCAG")
        + lnk("accessible-colors-adv","Accessible Colors")
        + lnk("keyboard-navigation-adv","Keyboard Navigation")
        + lnk("meaningful-text-adv","Meaningful Text")
        + lnk("wai-aria-adv","WAI-ARIA")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Responsive Design</div>'
        + lnk("natural-responsiveness-adv","Natural Responsiveness")
        + lnk("responsive-images-adv","Responsive Images")
        + lnk("media-queries-adv","Media Queries")
        + lnk("project-homepage-adv","Project: Homepage",True)
        + '</div></aside>'
    )

    def w(slug, title, intro, overview, body, kc, assignments, resources):
        write_lesson(ldir, root, course_title, ALL, sidebar,
                     slug, title, intro, overview, body, kc, assignments, resources)

    w("transforms","Transforms",
    intro="CSS transforms let you visually move, rotate, scale, and skew elements without affecting layout. They are the foundation of smooth, performant animations.",
    overview=["Use translate, rotate, scale, and skew transforms.","Chain multiple transforms together.","Understand the difference between 2D and 3D transforms.","Use transform-origin to control the pivot point."],
    body="""
<h2 class="lesson-section-title" id="basic-transforms">Basic 2D Transforms</h2>
""" + code(""".card {
  /* translate — move without affecting layout */
  transform: translateX(20px);
  transform: translateY(-10px);
  transform: translate(20px, -10px);  /* shorthand */

  /* rotate — clockwise in degrees */
  transform: rotate(45deg);
  transform: rotate(-90deg);

  /* scale — 1 = normal, 2 = double size, 0.5 = half */
  transform: scale(1.1);       /* uniform scale */
  transform: scaleX(2);        /* horizontal only */
  transform: scale(1.2, 0.8);  /* x then y */

  /* skew — shear the element */
  transform: skew(10deg, 5deg);
}
""") + """
<h2 class="lesson-section-title" id="chaining">Chaining Transforms</h2>
""" + code("""/* Chain multiple transforms — applied right to left */
.element {
  transform: translateX(100px) rotate(45deg) scale(1.5);
  /* First scales, then rotates, then translates */
}

/* Order matters! */
.a { transform: rotate(45deg) translateX(100px); }
/* moves 100px along the ROTATED axis */

.b { transform: translateX(100px) rotate(45deg); }
/* moves 100px horizontally THEN rotates */
""") + """
<h2 class="lesson-section-title" id="transform-origin">transform-origin</h2>
""" + code(""".card {
  transform-origin: center;        /* default — rotate from centre */
  transform-origin: top left;      /* rotate from top-left corner */
  transform-origin: 50% 0;         /* rotate from top centre */
  transform-origin: 100px 50px;    /* specific coordinates */
}

/* Classic hover flip card */
.card:hover {
  transform-origin: left center;
  transform: rotateY(180deg);
}
""") + """
<h2 class="lesson-section-title" id="3d-transforms">3D Transforms</h2>
""" + code(""".scene {
  perspective: 800px;   /* parent must set perspective for 3D */
}

.card {
  transform: rotateY(45deg);
  transform: rotateX(20deg);
  transform: translateZ(50px);      /* move toward/away from viewer */
  transform: rotate3d(1, 1, 0, 45deg);
}

/* Flip card effect */
.card-inner {
  transform-style: preserve-3d;    /* children exist in 3D space */
  transition: transform 0.6s;
}
.card:hover .card-inner {
  transform: rotateY(180deg);
}
.card-back {
  transform: rotateY(180deg);      /* pre-flipped, hidden by default */
  backface-visibility: hidden;     /* hide the back when facing away */
}
"""),
    kc=[("What is the difference between translate and margin/position for moving elements?","basic-transforms"),
        ("Does the order of chained transforms matter?","chaining"),
        ("What does perspective do in 3D transforms?","3d-transforms")],
    assignments=["Build a card that flips on hover using 3D CSS transforms.","Build an icon button that rotates 90 degrees and scales slightly on hover."],
    resources=[
        ("MDN — CSS Transforms","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transforms/Using_CSS_transforms"),
        ("CSS Tricks — Transform","https://css-tricks.com/almanac/properties/t/transform/"),
        ("YouTube — CSS Transforms (Kevin Powell)","https://www.youtube.com/watch?v=rzD-cPhq02E"),
    ])

    w("transitions","Transitions",
    intro="CSS transitions animate property changes smoothly. When a property value changes — on hover, focus, or class toggle — transitions make the change happen gradually over time.",
    overview=["Apply transitions with the transition shorthand.","Control timing with duration, delay, and easing functions.","Know which properties can and cannot be transitioned.","Use transitions for accessible, performant animations."],
    body="""
<h2 class="lesson-section-title" id="transition-syntax">Transition Syntax</h2>
""" + code(""".button {
  background: #2563eb;
  transform: scale(1);
  transition: background 0.2s ease,
              transform 0.2s ease;
}

.button:hover {
  background: #1d4ed8;
  transform: scale(1.05);
}

/* Shorthand: property duration timing-function delay */
.card {
  transition: all 0.3s ease-in-out;
  /* or be specific — better performance */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
""") + """
<h2 class="lesson-section-title" id="easing">Easing Functions</h2>
""" + code(""".element {
  transition-timing-function: ease;           /* default — slow start, fast middle, slow end */
  transition-timing-function: linear;         /* constant speed */
  transition-timing-function: ease-in;        /* slow start */
  transition-timing-function: ease-out;       /* slow end — most natural for exits */
  transition-timing-function: ease-in-out;    /* slow start and end */
  transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1); /* custom — springy */
}
""") + """
<h2 class="lesson-section-title" id="what-transitions">What Can Be Transitioned</h2>
""" + code("""/* YES — numeric values that can be interpolated */
opacity, transform, width, height, color,
background-color, border-color, box-shadow, padding, margin

/* NO — cannot be transitioned (binary changes) */
display: none → block   /* use opacity + visibility instead */
visibility: hidden → visible

/* Performant transitions — GPU-accelerated */
/* Only animate these for smooth 60fps */
transform, opacity

/* Avoid animating — triggers layout recalculation */
width, height, top, left, margin, padding
"""),
    kc=[("What does transition: all do and why should you avoid it in production?","transition-syntax"),
        ("What two CSS properties animate most performantly?","what-transitions"),
        ("What easing function feels most natural for an element leaving the screen?","easing")],
    assignments=["Add transitions to the buttons, links, and cards in your projects.","Replace any JavaScript-based show/hide with CSS opacity + visibility transitions."],
    resources=[
        ("MDN — Using CSS Transitions","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions"),
        ("CSS Tricks — Transition","https://css-tricks.com/almanac/properties/t/transition/"),
        ("YouTube — CSS Transitions (Kevin Powell)","https://www.youtube.com/watch?v=Nloq6uzF8RQ"),
    ])

    w("keyframes","Keyframes",
    intro="While transitions animate between two states, CSS animations with @keyframes let you define complex multi-step animations that run automatically — no user interaction required.",
    overview=["Define animations with @keyframes.","Apply animations with the animation property.","Control direction, iteration, and fill-mode.","Use animation events in JavaScript."],
    body="""
<h2 class="lesson-section-title" id="keyframes-syntax">@keyframes Syntax</h2>
""" + code("""/* Define the animation */
@keyframes fadeInUp {
  from {                       /* 0% */
    opacity: 0;
    transform: translateY(20px);
  }
  to {                         /* 100% */
    opacity: 1;
    transform: translateY(0);
  }
}

/* Multi-step animation */
@keyframes pulse {
  0%   { transform: scale(1); }
  50%  { transform: scale(1.05); }
  100% { transform: scale(1); }
}

@keyframes loadingBar {
  0%   { width: 0%; }
  30%  { width: 50%; }
  80%  { width: 80%; }
  100% { width: 100%; }
}
""") + """
<h2 class="lesson-section-title" id="animation-property">The animation Property</h2>
""" + code(""".card {
  /* name | duration | timing | delay | iterations | direction | fill-mode */
  animation: fadeInUp 0.5s ease-out 0s 1 normal forwards;

  /* Shorthand */
  animation: fadeInUp 0.5s ease-out forwards;
}

.spinner {
  animation: spin 1s linear infinite;  /* loops forever */
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

/* Multiple animations */
.hero {
  animation:
    fadeInUp 0.6s ease-out forwards,
    pulse 2s ease-in-out 0.6s infinite;
}
""") + """
<h2 class="lesson-section-title" id="fill-mode">fill-mode and direction</h2>
""" + code(""".element {
  animation-fill-mode: none;       /* default — resets to original after */
  animation-fill-mode: forwards;   /* keeps final keyframe state */
  animation-fill-mode: backwards;  /* applies first keyframe before starting */
  animation-fill-mode: both;       /* both forwards and backwards */

  animation-direction: normal;     /* 0% → 100% */
  animation-direction: reverse;    /* 100% → 0% */
  animation-direction: alternate;  /* 0%→100%, 100%→0%, 0%→100%... */
}
""") + """
<h2 class="lesson-section-title" id="reduced-motion">Respecting Reduced Motion</h2>
""" + code("""/* Always add this — some users experience motion sickness */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
"""),
    kc=[("What is the difference between a transition and a keyframe animation?","keyframes-syntax"),
        ("What does animation-fill-mode: forwards do?","fill-mode"),
        ("Why should you always include a prefers-reduced-motion media query?","reduced-motion")],
    assignments=["Build a page entrance animation: elements fade and slide in sequentially with staggered delays.","Add a loading spinner animation to your Weather App."],
    resources=[
        ("MDN — Using CSS Animations","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations"),
        ("CSS Tricks — Animation","https://css-tricks.com/almanac/properties/a/animation/"),
        ("YouTube — CSS Animations (Kevin Powell)","https://www.youtube.com/watch?v=YszONjKpgg4"),
    ])

    # Accessibility lessons
    for slug, title in [
        ("accessibility-intro","Introduction to Accessibility"),
        ("the-web-content-accessibility-guidelines-adv","The Web Content Accessibility Guidelines"),
        ("accessible-colors-adv","Accessible Colors"),
        ("keyboard-navigation-adv","Keyboard Navigation"),
        ("meaningful-text-adv","Meaningful Text"),
        ("wai-aria-adv","WAI-ARIA"),
    ]:
        w(slug, title,
        intro=f"This lesson covers {title} in the context of advanced, JavaScript-driven web applications — where accessibility challenges are more complex than static HTML pages.",
        overview=[f"Apply {title} principles to dynamic, JavaScript-driven interfaces.","Handle focus management in SPAs and dynamic content.","Test with real assistive technology."],
        body=f"""
<h2 class="lesson-section-title" id="overview">Advanced Context</h2>
<p>You covered {title} in the Intermediate HTML and CSS course. At this level, the same principles apply but the implementation is more complex — JavaScript dynamically adds and removes content, routes change without page loads, and components manage their own state.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Revisit the Intermediate HTML and CSS accessibility lessons if any concepts feel unclear. This lesson builds directly on them.</p>
</div>
<h2 class="lesson-section-title" id="spa-challenges">SPA-Specific Challenges</h2>
<ul>
  <li><strong>Focus management</strong> — when a route changes, move focus to the new page heading</li>
  <li><strong>Live regions</strong> — use aria-live to announce dynamic updates to screen readers</li>
  <li><strong>Loading states</strong> — announce when content is loading and when it has arrived</li>
  <li><strong>Modals</strong> — trap focus inside open modals, restore it when they close</li>
</ul>
""" + code("""// Focus management on route change (React example)
useEffect(() => {
  document.querySelector('h1')?.focus();
}, [location.pathname]);

// Announce dynamic content to screen readers
const [status, setStatus] = useState('');

// In your JSX:
// <div aria-live="polite" aria-atomic="true" className="visually-hidden">
//   {status}
// </div>

// When data loads:
setStatus('Search results loaded: 12 items found');
"""),
        # ✅ FIX 1: closed code() with ) above — kc/assignments/resources now go to w()
        kc=[(f"What makes {title} more complex in JavaScript-driven applications?","spa-challenges"),
            ("How do you manage focus when a route changes in a SPA?","spa-challenges")],
        assignments=[f"Audit one of your JavaScript projects for {title} issues using axe DevTools.","Fix every issue the audit reveals."],
        resources=[
            ("MDN — Accessibility","https://developer.mozilla.org/en-US/docs/Web/Accessibility"),
            ("WebAIM — Web Accessibility In Mind","https://webaim.org/"),
            ("YouTube — Accessibility in JavaScript Apps (Google Chrome Developers)","https://www.youtube.com/watch?v=HtTyRajRuyY"),
        ])

    # Responsive lessons
    for slug, title in [
        ("natural-responsiveness-adv","Natural Responsiveness"),
        ("responsive-images-adv","Responsive Images"),
        ("media-queries-adv","Media Queries"),
    ]:
        w(slug, title,
        intro=f"This lesson revisits {title} with a focus on advanced techniques — container queries, fluid type systems, and performance optimisation for images.",
        overview=[f"Apply advanced {title} techniques to complex layouts.","Use container queries for component-level responsiveness.","Optimise images for Core Web Vitals."],
        body="""
<h2 class="lesson-section-title" id="advanced">Advanced Techniques</h2>
<p>You covered the fundamentals in Intermediate HTML and CSS. This lesson focuses on the advanced patterns used in production applications.</p>
""" + code("""/* Container queries — component responds to its own container, not viewport */
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}

/* Fluid type scale — no media queries needed */
:root {
  --step-0: clamp(1rem,     1vw + 0.75rem,  1.125rem);
  --step-1: clamp(1.25rem,  1.5vw + 0.875rem, 1.5rem);
  --step-2: clamp(1.563rem, 2vw + 1rem,     2rem);
  --step-3: clamp(1.953rem, 2.5vw + 1.25rem, 2.5rem);
  --step-4: clamp(2.441rem, 3vw + 1.5rem,   3.5rem);
}

p  { font-size: var(--step-0); }
h3 { font-size: var(--step-2); }
h1 { font-size: var(--step-4); }
"""),
        # ✅ FIX 2: closed code() with ) above — kc/assignments/resources now go to w()
        kc=[(f"What advantage do container queries have over viewport media queries?","advanced"),
            ("What is a fluid type scale?","advanced")],
        assignments=[f"Apply container queries to a card component so it changes layout based on its container width, not the viewport.",
                     "Set up a fluid type scale using clamp() for your Homepage project."],
        resources=[
            ("MDN — Container Queries","https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries"),
            ("YouTube — Container Queries (Kevin Powell)","https://www.youtube.com/watch?v=OV8MVmtgMEI"),
        ])

    w("project-homepage-adv","Project: Homepage",
    intro="The Advanced HTML and CSS capstone. You will build a polished, fully accessible, animated, and responsive personal homepage — demonstrating every technique from this course.",
    overview=["Build a complete animated responsive homepage.","Apply CSS transforms, transitions, and keyframe animations.","Achieve 95+ on Lighthouse accessibility audit.","Use container queries and a fluid type scale."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>All requirements from the Intermediate HTML and CSS Homepage project, plus:</li>
  <li>Entrance animations using keyframes and @keyframes</li>
  <li>Smooth hover transitions on all interactive elements</li>
  <li>At least one 3D CSS transform effect</li>
  <li>Container queries on at least one component</li>
  <li>Fluid typography using clamp()</li>
  <li>prefers-reduced-motion media query disabling all animations</li>
  <li>Lighthouse Accessibility score of 95+</li>
  <li>Lighthouse Performance score of 90+</li>
</ul>
""" + code("""mkdir ~/devpath-projects/advanced-homepage
cd ~/devpath-projects/advanced-homepage
git init
touch index.html styles.css script.js
code .
"""),
    kc=[("What animation-specific requirements does this project add?","requirements"),
        ("What Lighthouse scores must you achieve?","requirements")],
    assignments=["Complete the Advanced Homepage meeting all requirements.","Push to GitHub Pages. Run Lighthouse and fix everything below target scores."],
    resources=[
        ("Google Lighthouse Documentation","https://developer.chrome.com/docs/lighthouse/"),
        ("CSS Tricks — Complete Guide to Custom Properties","https://css-tricks.com/a-complete-guide-to-custom-properties/"),
        ("YouTube — Advanced CSS Homepage (Kevin Powell)","https://www.youtube.com/watch?v=p0bGHP-PXD4"),
    ])

    print(f"  Advanced HTML and CSS: {len(ALL)} lessons done")


# ════════════════════════════════════════════════════════════════════════════
#  2. REACT
# ════════════════════════════════════════════════════════════════════════════
def seed_react():
    ldir = os.path.join(JS, "react", "lessons")
    root = "../../../../../"
    course_title = "React"

    ALL = [
        ("react-intro",                        "Introduction to React"),
        ("getting-started-with-react",         "Getting Started with React"),
        ("state-and-props",                    "State and Props"),
        ("rendering-techniques",               "Rendering Techniques"),
        ("handling-inputs-and-rendering-lists","Handling Inputs and Rendering Lists"),
        ("project-cv-application",             "Project: CV Application"),
        ("passing-data-between-components",    "Passing Data Between Components"),
        ("project-memory-card",                "Project: Memory Card"),
        ("more-on-state",                      "More on State"),
        ("refs-and-memoization",               "Refs and Memoization"),
        ("project-shopping-cart",              "Project: Shopping Cart"),
        ("introduction-to-react-hooks",        "Introduction to React Hooks"),
        ("useeffect",                          "useEffect"),
        ("custom-hooks",                       "Custom Hooks"),
        ("class-components",                   "Class Components"),
        ("react-router",                       "React Router"),
        ("fetching-data-in-react",             "Fetching Data in React"),
        ("introduction-to-state-management",   "Introduction to State Management"),
        ("managing-state-with-the-context-api","Managing State with the Context API"),
        ("project-where-in-the-world",         "Project: Where in the World?"),
        ("introduction-to-react-testing",      "Introduction to React Testing"),
        ("mocking-callbacks-and-components",   "Mocking Callbacks and Components"),
        ("project-battleship-react",           "Project: Battleship (React)"),
    ]

    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">React</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">Introduction to React</div>'
        + lnk("react-intro","Introduction to React")
        + lnk("getting-started-with-react","Getting Started with React")
        + lnk("state-and-props","State and Props")
        + lnk("rendering-techniques","Rendering Techniques")
        + lnk("handling-inputs-and-rendering-lists","Handling Inputs and Lists")
        + lnk("project-cv-application","Project: CV Application",True)
        + lnk("passing-data-between-components","Passing Data Between Components")
        + lnk("project-memory-card","Project: Memory Card",True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Getting Deeper</div>'
        + lnk("more-on-state","More on State")
        + lnk("refs-and-memoization","Refs and Memoization")
        + lnk("project-shopping-cart","Project: Shopping Cart",True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Hooks</div>'
        + lnk("introduction-to-react-hooks","Introduction to React Hooks")
        + lnk("useeffect","useEffect")
        + lnk("custom-hooks","Custom Hooks")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Class Components</div>'
        + lnk("class-components","Class Components")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">React Ecosystem</div>'
        + lnk("react-router","React Router")
        + lnk("fetching-data-in-react","Fetching Data in React")
        + lnk("introduction-to-state-management","Introduction to State Management")
        + lnk("managing-state-with-the-context-api","Managing State with Context API")
        + lnk("project-where-in-the-world","Project: Where in the World?",True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Testing React</div>'
        + lnk("introduction-to-react-testing","Introduction to React Testing")
        + lnk("mocking-callbacks-and-components","Mocking Callbacks and Components")
        + lnk("project-battleship-react","Project: Battleship (React)",True)
        + '</div></aside>'
    )

    def w(slug, title, intro, overview, body, kc, assignments, resources):
        write_lesson(ldir, root, course_title, ALL, sidebar,
                     slug, title, intro, overview, body, kc, assignments, resources)

    w("react-intro","Introduction to React",
    intro="React is a JavaScript library for building user interfaces through reusable components. Created by Facebook in 2013, it is now the most widely used frontend library in the world. This lesson explains what React is and why it was created.",
    overview=["Understand what React is and the problem it solves.","Know the difference between a library and a framework.","Understand the component model.","Know React's key concepts: JSX, virtual DOM, and one-way data flow."],
    body="""
<h2 class="lesson-section-title" id="what-is-react">What Is React?</h2>
<p>React is a <strong>JavaScript library</strong> for building user interfaces. It is not a full framework — it handles the view layer only. You add routing, state management, and data fetching separately (or use a framework like Next.js built on top of React).</p>
<p>React was created to solve a specific problem: as web UIs became more complex, keeping the DOM in sync with application state became incredibly error-prone. React introduced a model where you describe what the UI <em>should look like</em> for a given state, and React efficiently handles updating the DOM to match.</p>

<h2 class="lesson-section-title" id="virtual-dom">The Virtual DOM</h2>
<p>Instead of manipulating the real DOM directly (which is slow), React maintains a <strong>virtual DOM</strong> — an in-memory JavaScript representation of the actual DOM. When state changes, React:</p>
<ol>
  <li>Creates a new virtual DOM tree representing the new state</li>
  <li>Compares it with the previous virtual DOM (this is called "diffing")</li>
  <li>Calculates the minimum set of real DOM changes needed</li>
  <li>Applies only those changes</li>
</ol>
<p>This process — called <strong>reconciliation</strong> — makes React fast.</p>

<h2 class="lesson-section-title" id="components">The Component Model</h2>
<p>React applications are built from <strong>components</strong> — reusable, self-contained pieces of UI. Each component manages its own state and renders its own HTML. Complex UIs are built by composing simple components together.</p>
""" + code("""// A simple React component
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}

// Used like an HTML tag
<Greeting name="Alice" />
<Greeting name="Bob" />
""") + """
<h2 class="lesson-section-title" id="jsx">JSX</h2>
<p>JSX is a syntax extension that lets you write HTML-like markup inside JavaScript. It is not required to use React, but virtually everyone does because it makes component code much more readable.</p>
""" + code("""// JSX — looks like HTML, but it is JavaScript
const element = <h1 className="title">Hello, World!</h1>;

// Compiles to:
const element = React.createElement('h1', { className: 'title' }, 'Hello, World!');

// JSX rules:
// - Use className instead of class (class is a reserved JS word)
// - All tags must be closed: <img /> not <img>
// - Return a single root element (or use a Fragment <>...)
// - JavaScript expressions go in curly braces {expression}
"""),
    kc=[("What specific problem did React solve?","what-is-react"),
        ("What is the virtual DOM and why does React use it?","virtual-dom"),
        ("What is JSX?","jsx")],
    assignments=["Read the official React documentation's 'Quick Start' guide — linked below.","Watch the React 'Thinking in React' article to understand the component model."],
    resources=[
        ("React Official Docs — Quick Start","https://react.dev/learn"),
        ("React — Thinking in React","https://react.dev/learn/thinking-in-react"),
        ("YouTube — React in 100 Seconds (Fireship)","https://www.youtube.com/watch?v=Tn6-PIqc4UM"),
    ])

    w("getting-started-with-react","Getting Started with React",
    intro="Time to write your first React code. This lesson covers setting up a React project with Vite, understanding the file structure, and writing your first components.",
    overview=["Create a React project with Vite.","Understand the project structure.","Write functional components that return JSX.","Render a component to the DOM."],
    body="""
<h2 class="lesson-section-title" id="create-project">Creating a React Project</h2>
""" + code("""# Create a new React project with Vite (recommended)
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev

# Project structure
my-app/
├── public/
│   └── vite.svg
├── src/
│   ├── assets/
│   ├── App.jsx          ← main app component
│   ├── App.css
│   ├── main.jsx         ← entry point — renders App into the DOM
│   └── index.css
├── index.html           ← HTML shell
├── vite.config.js
└── package.json
""") + """
<h2 class="lesson-section-title" id="entry-point">The Entry Point</h2>
""" + code("""// src/main.jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// index.html has: <div id="root"></div>
// React mounts your entire app inside that div
""") + """
<h2 class="lesson-section-title" id="your-first-component">Your First Component</h2>
""" + code("""// src/components/Greeting.jsx

// A functional component — just a function that returns JSX
function Greeting({ name, age }) {
  const isAdult = age >= 18;

  return (
    <div className="greeting">
      <h1>Hello, {name}!</h1>
      <p>You are {age} years old.</p>
      {isAdult && <p>You can vote!</p>}
    </div>
  );
}

export default Greeting;
""") + code("""// Use it in App.jsx
import Greeting from './components/Greeting';

function App() {
  return (
    <main>
      <Greeting name="Alice" age={28} />
      <Greeting name="Bob"   age={16} />
    </main>
  );
}

export default App;
"""),
    kc=[("What command creates a new React project with Vite?","create-project"),
        ("What file renders the React app into the HTML page?","entry-point"),
        ("What must every React component return?","your-first-component")],
    assignments=["Create a new React project with Vite. Replace the default App.jsx with your own component that displays your name and a short bio.","Install the React Developer Tools browser extension."],
    resources=[
        ("React — Installation","https://react.dev/learn/installation"),
        ("Vite — Getting Started","https://vitejs.dev/guide/"),
        ("YouTube — React Crash Course (Traversy Media)","https://www.youtube.com/watch?v=w7ejDZ8SWv8"),
    ])

    w("state-and-props","State and Props",
    intro="Props and state are the two core mechanisms for managing data in React. Props pass data down from parent to child. State is private data that a component manages itself and that triggers re-renders when it changes.",
    overview=["Pass data to components using props.","Create and update local state with useState.","Understand the difference between props and state.","Lift state up when multiple components need the same data."],
    body="""
<h2 class="lesson-section-title" id="props">Props</h2>
<p>Props (short for properties) are how you pass data from a parent component to a child. They are read-only — a component must never modify its own props.</p>
""" + code("""// Parent passes props
function App() {
  return (
    <ProductCard
      name="Wireless Headphones"
      price={79.99}
      inStock={true}
      image="/headphones.jpg"
    />
  );
}

// Child receives them as an object parameter
function ProductCard({ name, price, inStock, image }) {
  return (
    <div className="card">
      <img src={image} alt={name} />
      <h2>{name}</h2>
      <p>${price.toFixed(2)}</p>
      {!inStock && <span className="badge">Out of Stock</span>}
    </div>
  );
}

// Default props
function Button({ label = "Click me", variant = "primary" }) {
  return <button className={variant}>{label}</button>;
}
""") + """
<h2 class="lesson-section-title" id="state">useState Hook</h2>
""" + code("""import { useState } from 'react';

function Counter() {
  // [currentValue, setterFunction] = useState(initialValue)
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
""") + """
<h2 class="lesson-section-title" id="lifting-state">Lifting State Up</h2>
<p>When two sibling components need to share state, move the state to their closest common parent and pass it down as props.</p>
""" + code("""function App() {
  // State lives in the parent — shared by both children
  const [count, setCount] = useState(0);

  return (
    <div>
      <Display count={count} />
      <Controls onIncrement={() => setCount(c => c + 1)}
                onDecrement={() => setCount(c => c - 1)} />
    </div>
  );
}

function Display({ count }) {
  return <p>Current count: {count}</p>;
}

function Controls({ onIncrement, onDecrement }) {
  return (
    <div>
      <button onClick={onIncrement}>+</button>
      <button onClick={onDecrement}>-</button>
    </div>
  );
}
"""),
    kc=[("What is the difference between props and state?","props"),
        ("What does useState return?","state"),
        ("What does 'lifting state up' mean?","lifting-state")],
    assignments=["Build a temperature converter component that shows both Celsius and Fahrenheit, keeping them in sync.","Build a shopping cart where the cart count in the header stays in sync with the list of items."],
    resources=[
        ("React — State: A Component's Memory","https://react.dev/learn/state-a-components-memory"),
        ("React — Sharing State Between Components","https://react.dev/learn/sharing-state-between-components"),
        ("YouTube — React State and Props (Web Dev Simplified)","https://www.youtube.com/watch?v=IYvD9oBCuJI"),
    ])

    w("rendering-techniques","Rendering Techniques",
    intro="React gives you several patterns for conditionally showing content and rendering lists of items. This lesson covers the patterns you will use in every React application.",
    overview=["Conditionally render elements with && and ternary operators.","Render lists of items with Array.map().","Add keys to list items.","Handle empty states and loading states."],
    body="""
<h2 class="lesson-section-title" id="conditional">Conditional Rendering</h2>
""" + code("""function UserProfile({ user, isLoading }) {
  // Short-circuit: render second part only if first is truthy
  return (
    <div>
      {isLoading && <Spinner />}

      {!isLoading && user && (
        <div>
          <h1>{user.name}</h1>
          <p>{user.bio}</p>
        </div>
      )}

      {!isLoading && !user && <p>User not found.</p>}
    </div>
  );
}

// Ternary — either/or
function StatusBadge({ isOnline }) {
  return (
    <span className={isOnline ? 'badge-green' : 'badge-grey'}>
      {isOnline ? 'Online' : 'Offline'}
    </span>
  );
}
""") + """
<h2 class="lesson-section-title" id="lists">Rendering Lists</h2>
""" + code("""const products = [
  { id: 1, name: "Laptop",   price: 999 },
  { id: 2, name: "Phone",    price: 599 },
  { id: 3, name: "Headphones", price: 79 },
];

function ProductList() {
  return (
    <ul>
      {products.map(product => (
        <ProductItem key={product.id} product={product} />
      ))}
    </ul>
  );
}

function ProductItem({ product }) {
  return (
    <li>
      {product.name} — ${product.price}
    </li>
  );
}
""") + """
<h2 class="lesson-section-title" id="keys">Keys</h2>
<p>Keys help React identify which items have changed, been added, or removed. They must be unique among siblings and stable (do not use array index as a key unless the list never reorders).</p>
""" + code("""// Good — using a unique, stable ID
{items.map(item => <Item key={item.id} {...item} />)}

// Acceptable — if list never reorders and items have no IDs
{items.map((item, index) => <Item key={index} {...item} />)}

// BAD — random key changes every render
{items.map(item => <Item key={Math.random()} {...item} />)}
"""),
    kc=[("What does the && operator do in JSX?","conditional"),
        ("What function is used to render a list of components?","lists"),
        ("Why can't you use array index as a key if the list reorders?","keys")],
    assignments=["Build a filterable product list: a text input that filters displayed products as you type.","Add a loading state and an empty state message to the product list."],
    resources=[
        ("React — Conditional Rendering","https://react.dev/learn/conditional-rendering"),
        ("React — Rendering Lists","https://react.dev/learn/rendering-lists"),
        ("YouTube — React Lists and Keys (Web Dev Simplified)","https://www.youtube.com/watch?v=-Ls48dd-vJE"),
    ])

    w("handling-inputs-and-rendering-lists","Handling Inputs and Rendering Lists",
    intro="Controlled components are React's pattern for form inputs where React state is the single source of truth. This lesson covers controlled inputs, form submission, and more complex list rendering.",
    overview=["Build controlled form inputs.","Handle form submission in React.","Manage lists in state (add, remove, update items)."],
    body="""
<h2 class="lesson-section-title" id="controlled-inputs">Controlled Inputs</h2>
<p>In a <strong>controlled component</strong>, the input's value is driven by React state. Every keystroke calls setState, which updates the state, which updates the input — React is always in control.</p>
""" + code("""function SearchBar() {
  const [query, setQuery] = useState('');

  return (
    <div>
      <input
        type="text"
        value={query}             /* controlled by state */
        onChange={e => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <p>You typed: {query}</p>
    </div>
  );
}
""") + """
<h2 class="lesson-section-title" id="form-submission">Form Submission</h2>
""" + code("""function AddTodoForm({ onAdd }) {
  const [title, setTitle]       = useState('');
  const [priority, setPriority] = useState('medium');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim()) return;   // validation
    onAdd({ title, priority, id: Date.now() });
    setTitle('');                // reset form
    setPriority('medium');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={title}
        onChange={e => setTitle(e.target.value)}
        placeholder="New todo..."
        required
      />
      <select value={priority} onChange={e => setPriority(e.target.value)}>
        <option value="high">High</option>
        <option value="medium">Medium</option>
        <option value="low">Low</option>
      </select>
      <button type="submit">Add Todo</button>
    </form>
  );
}
""") + """
<h2 class="lesson-section-title" id="list-state">Managing Lists in State</h2>
""" + code("""function TodoApp() {
  const [todos, setTodos] = useState([]);

  const addTodo = (todo) => {
    setTodos(prev => [...prev, todo]);        // add — never mutate state directly
  };

  const removeTodo = (id) => {
    setTodos(prev => prev.filter(t => t.id !== id));
  };

  const toggleTodo = (id) => {
    setTodos(prev =>
      prev.map(t => t.id === id ? { ...t, done: !t.done } : t)
    );
  };

  return (
    <div>
      <AddTodoForm onAdd={addTodo} />
      {todos.map(todo => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onRemove={removeTodo}
          onToggle={toggleTodo}
        />
      ))}
    </div>
  );
}
"""),
    kc=[("What makes an input 'controlled' in React?","controlled-inputs"),
        ("Why must you never mutate state arrays directly?","list-state"),
        ("How do you update one item in a state array?","list-state")],
    assignments=["Build the Todo App above with full add, remove, and toggle functionality.","Add a filter to show all/active/completed todos."],
    resources=[
        ("React — Reacting to Input with State","https://react.dev/learn/reacting-to-input-with-state"),
        ("React — Updating Arrays in State","https://react.dev/learn/updating-arrays-in-state"),
        ("YouTube — React Forms (Web Dev Simplified)","https://www.youtube.com/watch?v=SdzMgAjH37Q"),
    ])

    w("project-cv-application","Project: CV Application",
    intro="Build a CV (resume) builder where users fill in their information and see a formatted CV preview update in real time. This is the first substantial React project.",
    overview=["Manage complex form state across multiple sections.","Render a live preview that updates as the user types.","Toggle between edit and preview modes.","Organise components thoughtfully."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Three sections: General Info (name, email, phone), Education, and Experience</li>
  <li>Each section has an edit form and a display component</li>
  <li>A live preview panel that updates in real time as the user types</li>
  <li>Add and remove multiple education/experience entries</li>
  <li>A button to toggle between "Edit" and "Preview" mode</li>
  <li>Clean, professional CV layout in the preview</li>
</ul>
""" + code("""// Component structure
App
├── EditSection
│   ├── GeneralInfoForm
│   ├── EducationForm (multiple entries)
│   └── ExperienceForm (multiple entries)
└── PreviewSection
    ├── PersonalInfo
    ├── EducationList
    └── ExperienceList
""") + code("""// App.jsx — state management
function App() {
  const [cvData, setCvData] = useState({
    general: { name: '', email: '', phone: '' },
    education: [],
    experience: [],
  });

  const updateGeneral = (field, value) => {
    setCvData(prev => ({
      ...prev,
      general: { ...prev.general, [field]: value },
    }));
  };

  return (
    <div className="cv-builder">
      <EditSection cvData={cvData} onUpdate={updateGeneral} />
      <PreviewSection cvData={cvData} />
    </div>
  );
}
"""),
    # ✅ FIX 4: closed code() with ) above — kc/assignments/resources now go to w()
    kc=[("How do you update a nested property in a state object?","requirements"),
        ("What is the benefit of keeping all CV data in the top-level App component?","requirements")],
    assignments=["Complete the CV Application meeting all requirements.","Push to GitHub Pages."],
    resources=[
        ("React — Updating Objects in State","https://react.dev/learn/updating-objects-in-state"),
        ("YouTube — React CV Builder (Web Dev Simplified)","https://www.youtube.com/watch?v=E3XaDpff9Bc"),
    ])

    w("passing-data-between-components","Passing Data Between Components",
    intro="As React apps grow, passing data between components efficiently becomes critical. This lesson covers prop drilling, component composition, and the patterns used to avoid unnecessary complexity.",
    overview=["Understand prop drilling and when it becomes a problem.","Use component composition to share data without props.","Pass components as children and as props.","Use the children prop pattern."],
    body="""
<h2 class="lesson-section-title" id="prop-drilling">Prop Drilling</h2>
<p><strong>Prop drilling</strong> is when you pass props through several intermediate components that do not use the data themselves — only to get it to a deeply nested component that does.</p>
""" + code("""// Problem: theme must pass through every level
function App() {
  const [theme, setTheme] = useState('dark');
  return <Layout theme={theme} />;
}

function Layout({ theme }) {
  return <Sidebar theme={theme} />;  // Layout doesn't use theme
}

function Sidebar({ theme }) {
  return <Button theme={theme} />;  // Sidebar doesn't use theme either
}

function Button({ theme }) {
  return <button className={theme}>Click</button>;  // finally used here
}
""") + """
<h2 class="lesson-section-title" id="children">The children Prop</h2>
<p>Every React component automatically receives a <code>children</code> prop — whatever is rendered between its opening and closing tags.</p>
""" + code("""// A Card container that wraps any content
function Card({ title, children }) {
  return (
    <div className="card">
      {title && <h2 className="card-title">{title}</h2>}
      <div className="card-body">
        {children}   {/* whatever is between <Card>...</Card> */}
      </div>
    </div>
  );
}

// Usage — pass anything as children
<Card title="Welcome">
  <p>This is the card content.</p>
  <button>Click me</button>
</Card>

<Card>
  <img src="photo.jpg" alt="Photo" />
</Card>
""") + """
<h2 class="lesson-section-title" id="composition">Component Composition</h2>
""" + code("""// Instead of prop drilling, compose at the top level
function App() {
  const [theme, setTheme] = useState('dark');

  // Create the Button here where we have access to theme
  const ThemedButton = <Button className={theme}>Click</Button>;

  return (
    <Layout>
      <Sidebar>
        {ThemedButton}   {/* pass as children, no prop drilling */}
      </Sidebar>
    </Layout>
  );
}
"""),
    kc=[("What is prop drilling and what problem does it cause?","prop-drilling"),
        ("What is the children prop?","children"),
        ("How does component composition reduce prop drilling?","composition")],
    assignments=["Refactor your CV Application to use the children prop for layout components.","Build a generic Modal component that accepts content as children."],
    resources=[
        ("React — Passing Props to a Component","https://react.dev/learn/passing-props-to-a-component"),
        ("React — Passing JSX as Children","https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children"),
        ("YouTube — React Component Composition (Web Dev Simplified)","https://www.youtube.com/watch?v=23JuApjxE0A"),
    ])

    w("project-memory-card","Project: Memory Card",
    intro="Build a memory card game where clicking each card reveals an image and clicking the same card twice ends the game. This project heavily exercises state management and component interaction.",
    overview=["Manage game state across multiple components.","Shuffle an array randomly.","Track which cards have been clicked in this round.","Display the current score and best score."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Display a grid of cards, each showing an image (fetch from a public API like PokéAPI)</li>
  <li>Cards shuffle after every click</li>
  <li>Clicking a card that has not been clicked this round increments the score</li>
  <li>Clicking a card that has already been clicked this round ends the round — score resets</li>
  <li>Track and display the best score across rounds</li>
  <li>Win condition: click every card once without repeating</li>
</ul>
""" + code("""// Core game logic
function App() {
  const [cards, setCards] = useState([]);
  const [clicked, setClicked] = useState(new Set());
  const [score, setScore] = useState(0);
  const [bestScore, setBestScore] = useState(0);

  const handleCardClick = (id) => {
    if (clicked.has(id)) {
      // Already clicked — game over
      setBestScore(prev => Math.max(prev, score));
      setClicked(new Set());
      setScore(0);
    } else {
      // New click — increment score
      const newClicked = new Set(clicked).add(id);
      setClicked(newClicked);
      setScore(newClicked.size);

      // Win condition
      if (newClicked.size === cards.length) {
        setBestScore(cards.length);
        setClicked(new Set());
        setScore(0);
      }
    }

    // Shuffle cards after every click
    setCards(prev => [...prev].sort(() => Math.random() - 0.5));
  };

  return (
    <div>
      <ScoreBoard score={score} bestScore={bestScore} />
      <CardGrid cards={cards} onCardClick={handleCardClick} />
    </div>
  );
}
"""),
    kc=[("Why use a Set to track clicked cards?","requirements"),
        ("When exactly does the game reset the score?","requirements")],
    assignments=["Complete the Memory Card game meeting all requirements.","Fetch card images from the PokéAPI or similar.","Push to GitHub Pages."],
    resources=[
        ("PokéAPI — Free Pokémon API","https://pokeapi.co/"),
        ("React — State: A Component's Memory","https://react.dev/learn/state-a-components-memory"),
        ("YouTube — Memory Card Game React (Web Dev Simplified)","https://www.youtube.com/watch?v=62B3PN6IDQs"),
    ])

    w("more-on-state","More on State",
    intro="State management in React has nuances. This lesson covers state batching, the state queue, updating state based on previous state, and managing complex state objects.",
    overview=["Understand state batching.","Use the functional form of setState for updates based on previous state.","Manage complex state objects and arrays correctly.","Understand when re-renders happen."],
    body="""
<h2 class="lesson-section-title" id="functional-updates">Functional State Updates</h2>
<p>When new state depends on the previous state, always use the functional form of setState. React may batch multiple state updates, and the functional form guarantees you always have the latest state.</p>
""" + code("""// WRONG — stale state in rapid updates
function Counter() {
  const [count, setCount] = useState(0);

  const addThree = () => {
    setCount(count + 1);  // all three read the same 'count' value
    setCount(count + 1);
    setCount(count + 1);
    // Result: count increases by 1, not 3
  };
}

// CORRECT — always based on most recent state
function Counter() {
  const [count, setCount] = useState(0);

  const addThree = () => {
    setCount(prev => prev + 1);  // prev is guaranteed to be latest
    setCount(prev => prev + 1);
    setCount(prev => prev + 1);
    // Result: count increases by 3
  };
}
""") + """
<h2 class="lesson-section-title" id="complex-state">Complex State Objects</h2>
""" + code("""// NEVER mutate state directly
const [user, setUser] = useState({ name: 'Alice', age: 28, address: { city: 'London' } });

// WRONG — direct mutation
user.name = 'Bob';            // React won't re-render!
user.address.city = 'Paris';  // also wrong

// CORRECT — spread to create new objects
setUser(prev => ({ ...prev, name: 'Bob' }));

// Nested update — spread at each level
setUser(prev => ({
  ...prev,
  address: { ...prev.address, city: 'Paris' }
}));
""") + """
<h2 class="lesson-section-title" id="batching">State Batching</h2>
""" + code("""// React 18 batches ALL state updates, including those in async functions
async function handleClick() {
  setCount(c => c + 1);
  setFlag(f => !f);
  setName('Alice');
  // React batches all three — only ONE re-render, not three
}
"""),
    kc=[("When should you use the functional form of setState?","functional-updates"),
        ("Why must you never mutate state objects directly?","complex-state"),
        ("What is state batching and how does it help performance?","batching")],
    assignments=["Identify any direct state mutations in your previous React projects and fix them.","Build a multi-step form where state is a single object with fields for each step."],
    resources=[
        ("React — Queueing a Series of State Updates","https://react.dev/learn/queueing-a-series-of-state-updates"),
        ("React — Updating Objects in State","https://react.dev/learn/updating-objects-in-state"),
        ("YouTube — React State Batching (Jack Herrington)","https://www.youtube.com/watch?v=M_JYFMM5Kz8"),
    ])

    w("refs-and-memoization","Refs and Memoization",
    intro="Refs give you a way to access DOM elements directly or persist values without triggering re-renders. Memoization optimises performance by preventing unnecessary recalculations and re-renders.",
    overview=["Use useRef to access DOM elements.","Use useRef to persist values across renders without causing re-renders.","Use useMemo to memoize expensive calculations.","Use useCallback to memoize functions.","Use React.memo to prevent child component re-renders."],
    body="""
<h2 class="lesson-section-title" id="useref">useRef</h2>
""" + code("""import { useRef, useEffect } from 'react';

function TextInput() {
  const inputRef = useRef(null);

  // Focus the input when the component mounts
  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return <input ref={inputRef} type="text" />;
}

// useRef for values that persist but don't trigger re-renders
function Timer() {
  const [seconds, setSeconds] = useState(0);
  const intervalRef = useRef(null);

  const start = () => {
    intervalRef.current = setInterval(() => {
      setSeconds(s => s + 1);
    }, 1000);
  };

  const stop = () => {
    clearInterval(intervalRef.current);
  };

  return (
    <div>
      <p>{seconds}s</p>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
    </div>
  );
}
""") + """
<h2 class="lesson-section-title" id="memoization">useMemo and useCallback</h2>
""" + code("""import { useMemo, useCallback } from 'react';

function ExpensiveComponent({ items, onSelect }) {
  // useMemo — only recalculates when 'items' changes
  const expensiveValue = useMemo(() => {
    return items.reduce((sum, item) => sum + item.price, 0);
  }, [items]);  // dependency array

  // useCallback — only recreates the function when 'onSelect' changes
  // Prevents child from re-rendering when parent renders
  const handleClick = useCallback((id) => {
    onSelect(id);
  }, [onSelect]);

  return (
    <div>
      <p>Total: ${expensiveValue}</p>
      {items.map(item => (
        <Item key={item.id} item={item} onClick={handleClick} />
      ))}
    </div>
  );
}

// React.memo — skip re-render if props haven't changed
const Item = React.memo(function Item({ item, onClick }) {
  return <div onClick={() => onClick(item.id)}>{item.name}</div>;
});
"""),
    kc=[("What does useRef return and what are its two main uses?","useref"),
        ("What problem does useMemo solve?","memoization"),
        ("When should you use React.memo?","memoization")],
    assignments=["Add a useRef to auto-focus the search input in your filterable list.","Add useMemo to a component that does an expensive calculation (like sorting or filtering a large list)."],
    resources=[
        ("React — useRef","https://react.dev/reference/react/useRef"),
        ("React — useMemo","https://react.dev/reference/react/useMemo"),
        ("YouTube — React useMemo and useCallback (Web Dev Simplified)","https://www.youtube.com/watch?v=_AyFP5s69N4"),
    ])

    w("project-shopping-cart","Project: Shopping Cart",
    intro="Build a shopping cart application with a product listing page and a cart page. This is the most complex React project so far and requires careful state management.",
    overview=["Manage cart state across multiple pages.","Add, remove, and update item quantities.","Calculate totals dynamically.","Implement a cart count indicator in the navigation."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>A shop page listing at least 6 products fetched from a mock API</li>
  <li>Each product has an "Add to Cart" button and a quantity input</li>
  <li>A cart page showing all added items, quantities, and a total</li>
  <li>A cart icon in the navigation showing the total item count</li>
  <li>Ability to update quantity or remove items from the cart</li>
  <li>Cart state persists when navigating between pages (requires React Router)</li>
</ul>
""" + code("""// Cart state management
function App() {
  const [cart, setCart] = useState([]);

  const addToCart = (product, quantity = 1) => {
    setCart(prev => {
      const existing = prev.find(item => item.id === product.id);
      if (existing) {
        return prev.map(item =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + quantity }
            : item
        );
      }
      return [...prev, { ...product, quantity }];
    });
  };

  const removeFromCart = (id) => {
    setCart(prev => prev.filter(item => item.id !== id));
  };

  const updateQuantity = (id, quantity) => {
    if (quantity <= 0) { removeFromCart(id); return; }
    setCart(prev =>
      prev.map(item => item.id === id ? { ...item, quantity } : item)
    );
  };

  const cartTotal = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const cartCount = cart.reduce((sum, item) => sum + item.quantity, 0);

  return (
    <Router>
      <Nav cartCount={cartCount} />
      <Routes>
        <Route path="/" element={<ShopPage onAddToCart={addToCart} />} />
        <Route path="/cart" element={
          <CartPage cart={cart} onUpdate={updateQuantity} total={cartTotal} />
        } />
      </Routes>
    </Router>
  );
}
"""),
    kc=[("Where should the cart state live and why?","requirements"),
        ("How do you update the quantity of an existing cart item?","requirements")],
    assignments=["Complete the Shopping Cart meeting all requirements.","Push to GitHub Pages."],
    resources=[
        ("React Router — Getting Started","https://reactrouter.com/en/main/start/tutorial"),
        ("YouTube — React Shopping Cart (Web Dev Simplified)","https://www.youtube.com/watch?v=lATafp15HWA"),
    ])

    w("introduction-to-react-hooks","Introduction to React Hooks",
    intro="Hooks are functions that let you use React features — state, lifecycle, context — inside functional components. This lesson gives you the conceptual foundation before diving into individual hooks.",
    overview=["Understand what hooks are and why they were introduced.","Know the rules of hooks.","Survey the built-in hooks and their purposes."],
    body="""
<h2 class="lesson-section-title" id="what-are-hooks">What Are Hooks?</h2>
<p>Hooks were introduced in React 16.8 to let functional components use state and lifecycle features that previously required class components. They are regular JavaScript functions that follow naming conventions (always start with <code>use</code>).</p>
<p>Before hooks, you needed class components for state and lifecycle methods. Now functional components can do everything, and hooks make the code more reusable and composable.</p>

<h2 class="lesson-section-title" id="rules">Rules of Hooks</h2>
<ul>
  <li><strong>Only call hooks at the top level</strong> — never inside loops, conditions, or nested functions. React relies on call order to match hooks to their state.</li>
  <li><strong>Only call hooks from React functions</strong> — functional components or custom hooks. Not regular JavaScript functions.</li>
</ul>
""" + code("""// WRONG — conditional hook call
function Component({ showCount }) {
  if (showCount) {
    const [count, setCount] = useState(0); // ERROR: inside condition
  }
}

// CORRECT — always call the hook, use the condition inside
function Component({ showCount }) {
  const [count, setCount] = useState(0);
  return showCount ? <p>{count}</p> : null;
}
""") + """
<h2 class="lesson-section-title" id="built-in-hooks">Built-In Hooks Overview</h2>
<ul>
  <li><code>useState</code> — local component state</li>
  <li><code>useEffect</code> — side effects (data fetching, subscriptions, DOM manipulation)</li>
  <li><code>useContext</code> — consume Context values</li>
  <li><code>useRef</code> — mutable reference, DOM access</li>
  <li><code>useMemo</code> — memoize expensive calculations</li>
  <li><code>useCallback</code> — memoize functions</li>
  <li><code>useReducer</code> — complex state with a reducer function</li>
  <li><code>useId</code> — generate unique IDs for accessibility</li>
</ul>
""",
    kc=[("What are the two rules of hooks?","rules"),
        ("What problem did hooks solve?","what-are-hooks"),
        ("What is useReducer used for?","built-in-hooks")],
    assignments=["Read the React documentation's 'Built-in React Hooks' reference — linked below.","Identify which hooks you have already used and which ones you have not encountered yet."],
    resources=[
        ("React — Hooks Reference","https://react.dev/reference/react"),
        ("React — Rules of Hooks","https://react.dev/reference/rules/rules-of-hooks"),
        ("YouTube — React Hooks Explained (Fireship)","https://www.youtube.com/watch?v=TNhaISOUy6Q"),
    ])

    w("useeffect","useEffect",
    intro="useEffect is the hook for running side effects in React — data fetching, subscriptions, DOM manipulation, and anything that reaches outside the component. Understanding it deeply is essential for real applications.",
    overview=["Understand what a side effect is in React.","Use useEffect with and without a dependency array.","Clean up effects to prevent memory leaks.","Fetch data with useEffect."],
    body="""
<h2 class="lesson-section-title" id="what-are-effects">What Are Effects?</h2>
<p>A <strong>side effect</strong> is anything that affects something outside the component — fetching data, setting up subscriptions, manipulating the DOM, setting timers. React renders are pure — effects run after rendering is complete.</p>

<h2 class="lesson-section-title" id="syntax">useEffect Syntax</h2>
""" + code("""import { useEffect, useState } from 'react';

function Component() {
  // Runs after EVERY render
  useEffect(() => {
    document.title = 'Updated!';
  });

  // Runs only ONCE — on mount (empty dependency array)
  useEffect(() => {
    console.log('Component mounted');
  }, []);

  // Runs when 'userId' changes
  const [userId, setUserId] = useState(1);
  useEffect(() => {
    fetchUser(userId).then(user => setUser(user));
  }, [userId]);  // re-runs whenever userId changes

  // Cleanup — returned function runs before next effect or on unmount
  useEffect(() => {
    const interval = setInterval(() => tick(), 1000);
    return () => clearInterval(interval);  // cleanup!
  }, []);
}
""") + """
<h2 class="lesson-section-title" id="data-fetching">Data Fetching Pattern</h2>
""" + code("""function UserProfile({ userId }) {
  const [user, setUser]       = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(null);

  useEffect(() => {
    let cancelled = false;  // prevent setting state on unmounted component

    setLoading(true);
    setError(null);

    fetch(`/api/users/${userId}`)
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch');
        return res.json();
      })
      .then(data => {
        if (!cancelled) {
          setUser(data);
          setLoading(false);
        }
      })
      .catch(err => {
        if (!cancelled) {
          setError(err.message);
          setLoading(false);
        }
      });

    return () => { cancelled = true; };  // cleanup on unmount or userId change
  }, [userId]);

  if (loading) return <Spinner />;
  if (error)   return <ErrorMessage message={error} />;
  return <UserCard user={user} />;
}
"""),
    kc=[("What is a side effect in React?","what-are-effects"),
        ("What does an empty dependency array [] mean?","syntax"),
        ("What is the cleanup function and when does it run?","syntax"),
        ("Why set a 'cancelled' flag in the fetch effect?","data-fetching")],
    assignments=["Add data fetching with useEffect to your Weather App (React version).","Add proper cleanup to any effects that set up subscriptions or intervals."],
    resources=[
        ("React — useEffect","https://react.dev/reference/react/useEffect"),
        ("React — You Might Not Need an Effect","https://react.dev/learn/you-might-not-need-an-effect"),
        ("YouTube — useEffect Explained (Web Dev Simplified)","https://www.youtube.com/watch?v=0ZJgIjIuY7U"),
    ])

    w("custom-hooks","Custom Hooks",
    intro="Custom hooks let you extract component logic into reusable functions. Any time you find yourself duplicating stateful logic across components, a custom hook is the answer.",
    overview=["Understand when to create a custom hook.","Extract stateful logic into a custom hook.","Build common utility hooks: useFetch, useLocalStorage, useDebounce."],
    body="""
<h2 class="lesson-section-title" id="when-to-create">When to Create a Custom Hook</h2>
<p>Custom hooks solve two problems: code duplication and overly complex components. If you find yourself copying the same useState + useEffect pattern into multiple components, extract it into a custom hook.</p>

<h2 class="lesson-section-title" id="examples">Building Custom Hooks</h2>
""" + code("""// useFetch — reusable data fetching
function useFetch(url) {
  const [data, setData]       = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);

    fetch(url)
      .then(res => res.json())
      .then(data  => { if (!cancelled) { setData(data); setLoading(false); } })
      .catch(err  => { if (!cancelled) { setError(err); setLoading(false); } });

    return () => { cancelled = true; };
  }, [url]);

  return { data, loading, error };
}

// Usage — clean and reusable
function UserProfile({ userId }) {
  const { data: user, loading, error } = useFetch(`/api/users/${userId}`);
  if (loading) return <Spinner />;
  if (error) return <p>Error: {error.message}</p>;
  return <UserCard user={user} />;
}
""") + code("""// useLocalStorage — persist state to localStorage
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const stored = localStorage.getItem(key);
      return stored ? JSON.parse(stored) : initialValue;
    } catch {
      return initialValue;
    }
  });

  const setStoredValue = (newValue) => {
    setValue(newValue);
    localStorage.setItem(key, JSON.stringify(newValue));
  };

  return [value, setStoredValue];
}

// useDebounce — delay a value update
function useDebounce(value, delay = 500) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debounced;
}
"""),
    kc=[("What naming convention must custom hooks follow?","when-to-create"),
        ("What does useFetch return?","examples"),
        ("What does useDebounce do?","examples")],
    assignments=["Extract the data-fetching logic from your Weather App into a useFetch custom hook.","Build a useLocalStorage hook and use it to persist the todo list."],
    resources=[
        ("React — Reusing Logic with Custom Hooks","https://react.dev/learn/reusing-logic-with-custom-hooks"),
        ("YouTube — Custom React Hooks (Web Dev Simplified)","https://www.youtube.com/watch?v=6ThXsUwLWvc"),
    ])

    w("class-components","Class Components",
    intro="Before hooks, React components that needed state were written as classes. You will encounter class components in older codebases. This lesson covers their syntax and how they compare to modern functional components.",
    overview=["Write class components with state.","Use lifecycle methods: componentDidMount, componentDidUpdate, componentWillUnmount.","Compare class and functional component patterns."],
    body="""
<h2 class="lesson-section-title" id="class-syntax">Class Component Syntax</h2>
""" + code("""import { Component } from 'react';

class Counter extends Component {
  constructor(props) {
    super(props);  // always required
    this.state = {
      count: 0,
    };
  }

  increment = () => {
    this.setState(prev => ({ count: prev.count + 1 }));
  };

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.increment}>+</button>
      </div>
    );
  }
}

export default Counter;
""") + """
<h2 class="lesson-section-title" id="lifecycle">Lifecycle Methods</h2>
""" + code("""class UserProfile extends Component {
  state = { user: null, loading: true };

  // Equivalent to useEffect(() => { ... }, []) — runs after first render
  componentDidMount() {
    fetch(`/api/users/${this.props.userId}`)
      .then(res => res.json())
      .then(user => this.setState({ user, loading: false }));
  }

  // Equivalent to useEffect(() => { ... }, [props.userId])
  componentDidUpdate(prevProps) {
    if (prevProps.userId !== this.props.userId) {
      this.fetchUser(this.props.userId);
    }
  }

  // Equivalent to useEffect cleanup — runs before unmount
  componentWillUnmount() {
    // cancel subscriptions, clear intervals etc.
  }

  render() {
    const { user, loading } = this.state;
    if (loading) return <p>Loading...</p>;
    return <div>{user.name}</div>;
  }
}
"""),
    kc=[("What is the equivalent of componentDidMount in functional components?","lifecycle"),
        ("How do you update state in a class component?","class-syntax"),
        ("Should you write new code using class components?","class-syntax")],
    assignments=["Convert one of your functional components to a class component for practice.","Read the React documentation on class components — linked below."],
    resources=[
        ("React — Component (class API reference)","https://react.dev/reference/react/Component"),
        ("YouTube — React Class Components (Web Dev Simplified)","https://www.youtube.com/watch?v=oNSPqgSRbBk"),
    ])

    w("react-router","React Router",
    intro="React Router is the standard library for navigation in React applications. It lets you create multiple 'pages' in a single-page app, with URL-based routing that works with the browser's back/forward buttons.",
    overview=["Set up React Router v6.","Create routes with Route and Routes.","Navigate between routes with Link and useNavigate.","Use URL parameters and query strings.","Create nested routes."],
    body="""
<h2 class="lesson-section-title" id="setup">Setup</h2>
""" + code("""npm install react-router-dom
""") + code("""// main.jsx — wrap app in BrowserRouter
import { BrowserRouter } from 'react-router-dom';

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
""") + """
<h2 class="lesson-section-title" id="routes">Defining Routes</h2>
""" + code("""// App.jsx
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import About from './pages/About';
import UserProfile from './pages/UserProfile';
import NotFound from './pages/NotFound';

function App() {
  return (
    <>
      <Nav />
      <Routes>
        <Route path="/"           element={<Home />} />
        <Route path="/about"      element={<About />} />
        <Route path="/users/:id"  element={<UserProfile />} />  {/* URL param */}
        <Route path="*"           element={<NotFound />} />     {/* catch-all */}
      </Routes>
    </>
  );
}
""") + """
<h2 class="lesson-section-title" id="navigation">Navigation and URL Params</h2>
""" + code("""import { Link, NavLink, useNavigate, useParams } from 'react-router-dom';

// Link — declarative navigation
function Nav() {
  return (
    <nav>
      <Link to="/">Home</Link>
      {/* NavLink adds 'active' class when route matches */}
      <NavLink to="/about" className={({ isActive }) => isActive ? 'active' : ''}>
        About
      </NavLink>
    </nav>
  );
}

// useNavigate — programmatic navigation
function LoginForm() {
  const navigate = useNavigate();

  const handleLogin = async () => {
    await login();
    navigate('/dashboard');        // redirect after login
    navigate(-1);                  // go back
    navigate('/dashboard', { replace: true }); // replace history entry
  };
}

// useParams — read URL parameters
function UserProfile() {
  const { id } = useParams();  // from path="/users/:id"
  const { data: user } = useFetch(`/api/users/${id}`);
  return <div>{user?.name}</div>;
}
"""),
    kc=[("What is the difference between Link and NavLink?","navigation"),
        ("How do you read a URL parameter like :id?","navigation"),
        ("What does navigate(-1) do?","navigation")],
    assignments=["Add React Router to your Shopping Cart project.","Create a product detail page at /products/:id that fetches and displays a single product."],
    resources=[
        ("React Router — Tutorial","https://reactrouter.com/en/main/start/tutorial"),
        ("YouTube — React Router v6 (Web Dev Simplified)","https://www.youtube.com/watch?v=Ul3y1LXxzdU"),
    ])

    w("fetching-data-in-react","Fetching Data in React",
    intro="Most React applications fetch data from APIs. This lesson covers the full data-fetching lifecycle — loading states, error handling, caching, and the modern approach using TanStack Query.",
    overview=["Fetch data with useEffect and the custom useFetch hook.","Handle loading, error, and success states.","Understand the limitations of manual data fetching.","Use TanStack Query for production-grade data fetching."],
    body="""
<h2 class="lesson-section-title" id="manual-fetching">Manual Fetching Review</h2>
""" + code("""// The pattern you already know
function PostList() {
  const { data: posts, loading, error } = useFetch('/api/posts');

  return (
    <div>
      {loading && <Spinner />}
      {error   && <ErrorBanner message={error.message} />}
      {posts   && posts.map(post => <PostCard key={post.id} post={post} />)}
    </div>
  );
}
""") + """
<h2 class="lesson-section-title" id="limitations">Limitations of Manual Fetching</h2>
<p>Manual useEffect fetching has real-world problems:</p>
<ul>
  <li>No caching — re-fetches every time the component mounts</li>
  <li>No automatic refetching when data goes stale</li>
  <li>No deduplication — two components fetching the same URL make two requests</li>
  <li>Complex code for pagination and infinite scroll</li>
</ul>

<h2 class="lesson-section-title" id="tanstack-query">TanStack Query</h2>
""" + code("""npm install @tanstack/react-query
""") + code("""// main.jsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
const queryClient = new QueryClient();

<QueryClientProvider client={queryClient}>
  <App />
</QueryClientProvider>
""") + code("""// Component — much simpler than manual useEffect
import { useQuery } from '@tanstack/react-query';

function PostList() {
  const { data, isLoading, isError, error } = useQuery({
    queryKey: ['posts'],          // unique cache key
    queryFn: () => fetch('/api/posts').then(r => r.json()),
    staleTime: 5 * 60 * 1000,    // consider data fresh for 5 minutes
  });

  if (isLoading) return <Spinner />;
  if (isError)   return <p>Error: {error.message}</p>;
  return <div>{data.map(post => <PostCard key={post.id} post={post} />)}</div>;
}
"""),
    kc=[("What are the limitations of manual useEffect data fetching?","limitations"),
        ("What does queryKey do in TanStack Query?","tanstack-query"),
        ("What does staleTime control?","tanstack-query")],
    assignments=["Refactor your Weather App to use TanStack Query instead of useEffect for data fetching.","Observe the caching behaviour — search for the same city twice and notice it does not re-fetch."],
    resources=[
        ("TanStack Query — Quick Start","https://tanstack.com/query/latest/docs/framework/react/quick-start"),
        ("YouTube — TanStack Query (Web Dev Simplified)","https://www.youtube.com/watch?v=r8Dg0KVnfMA"),
    ])

    w("introduction-to-state-management","Introduction to State Management",
    intro="As React apps grow, passing state through props becomes unwieldy. This lesson introduces the problem of global state management and surveys the solutions available.",
    overview=["Understand when global state management is needed.","Know the difference between server state and client state.","Survey the main state management options: Context API, Zustand, Redux Toolkit."],
    body="""
<h2 class="lesson-section-title" id="the-problem">The Global State Problem</h2>
<p>Prop drilling becomes a problem when many components at different levels need the same data. The classic examples: the currently logged-in user, the active theme, and cart data need to be accessible throughout the app.</p>

<h2 class="lesson-section-title" id="server-vs-client">Server State vs. Client State</h2>
<ul>
  <li><strong>Server state</strong> — data that lives on a server and must be fetched, cached, and synchronised. Examples: posts, users, products. Best managed with TanStack Query.</li>
  <li><strong>Client state</strong> — data that lives only in the browser. Examples: UI state (modal open/closed), current user preferences, cart items. Managed with useState, Context, or a state manager.</li>
</ul>
<p>Many apps that seem to need a state manager actually only need TanStack Query for server state and local state for UI. Reach for a state manager only when you genuinely have complex client state.</p>

<h2 class="lesson-section-title" id="options">State Management Options</h2>
<ul>
  <li><strong>Context API</strong> — built into React. Good for infrequently changing global values (theme, auth, locale). Not performant for frequently changing state.</li>
  <li><strong>Zustand</strong> — lightweight, simple API, performant. Good for most apps that need a state manager.</li>
  <li><strong>Redux Toolkit</strong> — the modern, opinionated way to use Redux. More boilerplate than Zustand but standard in large teams.</li>
  <li><strong>Jotai / Recoil</strong> — atomic state management. Each atom is independent state, components subscribe to only what they need.</li>
</ul>
""",
    kc=[("What is the difference between server state and client state?","server-vs-client"),
        ("When should you reach for a global state manager?","the-problem"),
        ("What is Zustand and when would you choose it over Redux?","options")],
    assignments=["Identify the global state in your Shopping Cart project.","Read the Zustand documentation quick start — linked below."],
    resources=[
        ("Zustand — Documentation","https://zustand-demo.pmnd.rs/"),
        ("Redux Toolkit — Quick Start","https://redux-toolkit.js.org/introduction/getting-started"),
        ("YouTube — React State Management (Fireship)","https://www.youtube.com/watch?v=_ngCLZ5Iz-0"),
    ])

    w("managing-state-with-the-context-api","Managing State with the Context API",
    intro="The React Context API lets you share state across any component in the tree without prop drilling. This lesson covers how to create, provide, and consume Context effectively.",
    overview=["Create a Context with createContext.","Provide context values with a Provider component.","Consume context with useContext.","Build a custom context hook.","Understand Context's performance limitations."],
    body="""
<h2 class="lesson-section-title" id="creating-context">Creating and Providing Context</h2>
""" + code("""// ThemeContext.jsx
import { createContext, useContext, useState } from 'react';

// 1. Create the context
const ThemeContext = createContext(null);

// 2. Create a Provider component
export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// 3. Create a custom hook for easy consumption
export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used inside ThemeProvider');
  }
  return context;
}
""") + code("""// main.jsx — wrap the app
<ThemeProvider>
  <App />
</ThemeProvider>

// Any component — consume the context
function Header() {
  const { theme, toggleTheme } = useTheme();
  return (
    <header className={theme}>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </header>
  );
}
""") + """
<h2 class="lesson-section-title" id="performance">Context Performance</h2>
<p>Every time the context value changes, ALL components consuming that context re-render. For frequently changing state (like animation values or typing input), this can cause performance problems.</p>
<p>Solutions: split context by update frequency, use useMemo to stabilise the context value, or use a dedicated state manager like Zustand instead.</p>
""",
    kc=[("What does createContext return?","creating-context"),
        ("Why throw an error in the custom hook if context is null?","creating-context"),
        ("What is the performance caveat of Context?","performance")],
    assignments=["Add a ThemeContext to one of your React projects with a light/dark toggle.","Add an AuthContext that provides the current user and login/logout functions."],
    resources=[
        ("React — useContext","https://react.dev/reference/react/useContext"),
        ("React — Passing Data Deeply with Context","https://react.dev/learn/passing-data-deeply-with-context"),
        ("YouTube — React Context API (Web Dev Simplified)","https://www.youtube.com/watch?v=5LrDIWkK_Bc"),
    ])

    w("project-where-in-the-world","Project: Where in the World?",
    intro="Build a countries information app that fetches data from the REST Countries API, includes filtering and searching, and uses React Router for country detail pages.",
    overview=["Fetch and display data from the REST Countries API.","Implement search and filter functionality.","Use React Router for country detail pages.","Implement a light/dark mode toggle with Context."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Homepage showing all countries as cards (flag, name, population, region, capital)</li>
  <li>Search input that filters countries by name in real time</li>
  <li>A region filter dropdown (Africa, Americas, Asia, Europe, Oceania)</li>
  <li>Clicking a country navigates to a detail page showing all info</li>
  <li>Detail page has "Border Countries" links to neighbouring countries</li>
  <li>A light/dark mode toggle that persists preference</li>
  <li>Fully responsive layout</li>
</ul>
""" + code("""// API
const BASE = 'https://restcountries.com/v3.1';

// All countries
fetch(`${BASE}/all?fields=name,flags,population,region,capital,cca3`)

// Countries by region
fetch(`${BASE}/region/europe?fields=name,flags,population,region,capital`)

// Single country by code
fetch(`${BASE}/alpha/${code}`)
""") + code("""mkdir ~/devpath-projects/where-in-the-world
cd ~/devpath-projects/where-in-the-world
npm create vite@latest . -- --template react
npm install react-router-dom @tanstack/react-query
npm run dev
"""),
    kc=[("What API is used and what endpoint fetches all countries?","requirements"),
        ("How do you keep the theme preference across page refreshes?","requirements")],
    assignments=["Complete the Where in the World? project meeting all requirements.","Push to GitHub Pages."],
    resources=[
        ("REST Countries API Documentation","https://restcountries.com/"),
        ("YouTube — Where in the World? React Project (Frontend Mentor)","https://www.youtube.com/watch?v=v5e7Xv1Bh_M"),
    ])

    w("introduction-to-react-testing","Introduction to React Testing",
    intro="Testing React components requires tools beyond Jest alone. React Testing Library (RTL) is the standard — it tests components the way users interact with them, not implementation details.",
    overview=["Install and configure React Testing Library.","Render components and query elements.","Simulate user interactions.","Understand the testing philosophy: test behaviour, not implementation."],
    body="""
<h2 class="lesson-section-title" id="setup">Setup</h2>
""" + code("""npm install --save-dev @testing-library/react @testing-library/user-event @testing-library/jest-dom vitest jsdom

# vitest.config.js
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: './src/setupTests.js',
  },
});
""") + """
<h2 class="lesson-section-title" id="writing-tests">Writing RTL Tests</h2>
""" + code("""// Greeting.test.jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Greeting from './Greeting';

describe('Greeting', () => {
  it('renders the name correctly', () => {
    render(<Greeting name="Alice" />);
    expect(screen.getByText('Hello, Alice!')).toBeInTheDocument();
  });

  it('shows the button', () => {
    render(<Greeting name="Alice" />);
    expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument();
  });

  it('increments count on button click', async () => {
    const user = userEvent.setup();
    render(<Greeting name="Alice" />);

    const button = screen.getByRole('button');
    await user.click(button);

    expect(screen.getByText('Clicked 1 time')).toBeInTheDocument();
  });
});
""") + """
<h2 class="lesson-section-title" id="queries">Query Methods</h2>
""" + code("""// Preferred queries (in order of preference)
screen.getByRole('button', { name: /submit/i })  // most accessible-aware
screen.getByLabelText('Email')                    // for form inputs
screen.getByPlaceholderText('Enter email')
screen.getByText('Hello')
screen.getByDisplayValue('current value')

// When the element might not exist
screen.queryByText('Error message')  // returns null if not found
await screen.findByText('Loaded!')   // waits for async element
"""),
    kc=[("What is the testing philosophy of React Testing Library?","writing-tests"),
        ("What is the preferred query method and why?","queries"),
        ("What is the difference between getBy, queryBy, and findBy?","queries")],
    assignments=["Write tests for your Counter component.","Write tests for your filterable product list — test that filtering works correctly."],
    resources=[
        ("React Testing Library Docs","https://testing-library.com/docs/react-testing-library/intro/"),
        ("YouTube — React Testing Library (Web Dev Simplified)","https://www.youtube.com/watch?v=7dTTFW7yACQ"),
    ])

    w("mocking-callbacks-and-components","Mocking Callbacks and Components",
    intro="When testing a component that depends on callbacks or child components, mocking lets you isolate the unit you are testing and verify interactions precisely.",
    overview=["Mock callback props with jest.fn().","Test that callbacks are called with correct arguments.","Mock entire modules for complex dependencies.","Test components that make API calls."],
    body="""
<h2 class="lesson-section-title" id="mocking-callbacks">Mocking Callbacks</h2>
""" + code("""// Component under test
function DeleteButton({ onDelete, itemName }) {
  return (
    <button onClick={() => onDelete(itemName)}>
      Delete {itemName}
    </button>
  );
}

// Test — verify callback is called correctly
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('calls onDelete with item name when clicked', async () => {
  const mockOnDelete = vi.fn();  // Vitest mock (or jest.fn() with Jest)
  const user = userEvent.setup();

  render(<DeleteButton onDelete={mockOnDelete} itemName="Widget" />);

  await user.click(screen.getByRole('button'));

  expect(mockOnDelete).toHaveBeenCalledTimes(1);
  expect(mockOnDelete).toHaveBeenCalledWith('Widget');
});
""") + """
<h2 class="lesson-section-title" id="mocking-api">Mocking API Calls</h2>
""" + code("""// Mock fetch for components that call the API
beforeEach(() => {
  global.fetch = vi.fn().mockResolvedValue({
    ok: true,
    json: () => Promise.resolve([
      { id: 1, title: 'Test Post' },
    ]),
  });
});

afterEach(() => {
  vi.restoreAllMocks();
});

test('renders posts from API', async () => {
  render(<PostList />);

  expect(screen.getByText('Loading...')).toBeInTheDocument();

  const post = await screen.findByText('Test Post');  // waits for async
  expect(post).toBeInTheDocument();

  expect(fetch).toHaveBeenCalledWith('/api/posts');
});
"""),
    kc=[("What does vi.fn() create?","mocking-callbacks"),
        ("How do you test that a callback was called with specific arguments?","mocking-callbacks"),
        ("Why mock fetch instead of making real API calls in tests?","mocking-api")],
    assignments=["Write tests for your Shopping Cart's add-to-cart functionality using mocked callbacks.","Write a test for your Weather App that mocks the fetch call."],
    resources=[
        ("Vitest — Mocking","https://vitest.dev/guide/mocking.html"),
        ("Testing Library — Async Queries","https://testing-library.com/docs/dom-testing-library/api-async/"),
        ("YouTube — Mocking in React Tests (Web Dev Simplified)","https://www.youtube.com/watch?v=v77fjkKQTH0"),
    ])

    w("project-battleship-react","Project: Battleship (React)",
    intro="Port your vanilla JavaScript Battleship game to React. This project demonstrates how to translate existing game logic into a React component architecture while keeping logic separate from presentation.",
    overview=["Refactor game logic into pure functions or classes.","Represent game state as React state.","Build the board and ship-placement UI with React components.","Write tests for components using React Testing Library."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>All the same gameplay requirements as the original Battleship project</li>
  <li>Game logic (Ship, Gameboard, Player) stays as pure classes/functions — no React in the logic layer</li>
  <li>React components handle display and user interaction only</li>
  <li>State represents the complete game state; components derive their display from it</li>
  <li>React Testing Library tests for key UI interactions</li>
  <li>Drag-and-drop or click-to-place ship placement</li>
</ul>
""" + code("""// Architecture: game logic is React-free
// src/game/Ship.js       ← pure class, no React
// src/game/Gameboard.js  ← pure class, no React
// src/game/Player.js     ← pure class, no React

// src/components/Board.jsx      ← renders a gameboard
// src/components/Cell.jsx       ← single board cell
// src/components/ShipPlacer.jsx ← ship placement UI
// src/App.jsx                   ← top-level game state

// App.jsx
function App() {
  const [gameState, setGameState] = useState(() => ({
    playerBoard: new Gameboard(),
    computerBoard: new Gameboard(),
    currentTurn: 'player',
    gameOver: false,
    winner: null,
  }));

  const handleAttack = (row, col) => {
    setGameState(prev => {
      const newState = { ...prev };
      newState.computerBoard.receiveAttack(row, col);
      // check win condition, switch turns...
      return newState;
    });
  };
}
"""),
    kc=[("Why keep game logic in pure classes separate from React?","requirements"),
        ("How does React state represent the gameboard?","requirements")],
    assignments=["Complete the React Battleship meeting all requirements.","Write at least 10 RTL tests for UI components.","Push to GitHub Pages."],
    resources=[
        ("React Testing Library Docs","https://testing-library.com/docs/react-testing-library/intro/"),
        ("YouTube — Battleship in React","https://www.youtube.com/watch?v=4VkC4QoGTBc"),
    ])

    print(f"  React: {len(ALL)} lessons done")


# ════════════════════════════════════════════════════════════════════════════
#  3. NODEJS
# ════════════════════════════════════════════════════════════════════════════
def seed_nodejs():
    ldir = os.path.join(JS, "nodejs", "lessons")
    root = "../../../../../"
    course_title = "NodeJS"

    ALL = [
        ("introduction-to-nodejs",       "Introduction to NodeJS"),
        ("getting-started",              "Getting Started"),
        ("debugging-node",               "Debugging Node"),
        ("introduction-to-express",      "Introduction to Express"),
        ("express-routes-and-controllers","Express Routes and Controllers"),
        ("express-views",                "Express Views"),
        ("project-mini-message-board",   "Project: Mini Message Board"),
        ("introduction-to-mongodb",      "Introduction to MongoDB"),
        ("mongoose-primer",              "Mongoose Primer"),
        ("project-inventory-application","Project: Inventory Application"),
        ("authentication-basics",        "Authentication Basics"),
        ("security-configuration",       "Security Configuration"),
        ("project-members-only",         "Project: Members Only"),
        ("apis",                         "APIs"),
        ("api-security-and-authentication","API Security and Authentication"),
        ("project-blog-api",             "Project: Blog API"),
        ("testing-express",              "Testing Express"),
        ("sql-basics",                   "SQL Basics"),
        ("databases-and-sql",            "Databases and SQL"),
        ("knex-js",                      "Knex.js"),
        ("project-file-uploader",        "Project: File Uploader"),
        ("project-odinbook",             "Project: Odin-Book"),
    ]

    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">NodeJS</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">Introduction to NodeJS</div>'
        + lnk("introduction-to-nodejs","Introduction to NodeJS")
        + lnk("getting-started","Getting Started")
        + lnk("debugging-node","Debugging Node")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Express and Mongoose</div>'
        + lnk("introduction-to-express","Introduction to Express")
        + lnk("express-routes-and-controllers","Express Routes and Controllers")
        + lnk("express-views","Express Views")
        + lnk("project-mini-message-board","Project: Mini Message Board",True)
        + lnk("introduction-to-mongodb","Introduction to MongoDB")
        + lnk("mongoose-primer","Mongoose Primer")
        + lnk("project-inventory-application","Project: Inventory Application",True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Authentication</div>'
        + lnk("authentication-basics","Authentication Basics")
        + lnk("security-configuration","Security Configuration")
        + lnk("project-members-only","Project: Members Only",True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">APIs</div>'
        + lnk("apis","APIs")
        + lnk("api-security-and-authentication","API Security and Authentication")
        + lnk("project-blog-api","Project: Blog API",True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Testing Express</div>'
        + lnk("testing-express","Testing Express")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">SQL and PostgreSQL</div>'
        + lnk("sql-basics","SQL Basics")
        + lnk("databases-and-sql","Databases and SQL")
        + lnk("knex-js","Knex.js")
        + lnk("project-file-uploader","Project: File Uploader",True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Finishing the Full Stack</div>'
        + lnk("project-odinbook","Project: Odin-Book",True)
        + '</div></aside>'
    )

    def w(slug, title, intro, overview, body, kc, assignments, resources):
        write_lesson(ldir, root, course_title, ALL, sidebar,
                     slug, title, intro, overview, body, kc, assignments, resources)

    w("introduction-to-nodejs","Introduction to NodeJS",
    intro="Node.js lets JavaScript run on the server. This opens up a world of possibilities — file systems, databases, HTTP servers, real-time communication — all using the language you already know.",
    overview=["Understand what Node.js is and what it enables.","Know the difference between browser JavaScript and Node.js.","Understand the Node.js event loop model.","Know the Node.js module system (CommonJS and ESM)."],
    body="""
<h2 class="lesson-section-title" id="what-is-node">What Is Node.js?</h2>
<p>Node.js is a runtime environment that executes JavaScript outside the browser using Chrome's V8 engine. It is designed for building fast, scalable network applications using an event-driven, non-blocking I/O model.</p>
<p>Node.js powers: web servers, REST APIs, real-time apps (chat, gaming), command-line tools, build tooling (Webpack, Vite, ESLint), and serverless functions.</p>

<h2 class="lesson-section-title" id="browser-vs-node">Browser vs. Node.js</h2>
<ul>
  <li><strong>Browser</strong> — has DOM, window, document, fetch, localStorage. No file system access.</li>
  <li><strong>Node.js</strong> — no DOM, no window. Has file system, network, process, os modules. Has global instead of window.</li>
</ul>
""" + code("""// Node.js has access to things the browser does not
const fs   = require('fs');          // file system
const path = require('path');        // file paths
const os   = require('os');          // operating system info
const http = require('http');        // HTTP server

// And lacks browser things
typeof window;    // undefined in Node
typeof document;  // undefined in Node
""") + """
<h2 class="lesson-section-title" id="modules">Node Modules</h2>
""" + code("""// CommonJS (original Node.js module system)
const express = require('express');
module.exports = { myFunction };

// ESM (modern — add "type": "module" to package.json)
import express from 'express';
export function myFunction() {}
"""),
    kc=[("What makes Node.js different from browser JavaScript?","browser-vs-node"),
        ("What is the difference between CommonJS and ESM in Node?","modules"),
        ("Name three things Node.js is used for.","what-is-node")],
    assignments=["Install Node.js if not done. Verify with node --version.","Create a Node.js script that reads a file and logs its contents."],
    resources=[
        ("Node.js Official Documentation","https://nodejs.org/en/docs/"),
        ("YouTube — Node.js Crash Course (Traversy Media)","https://www.youtube.com/watch?v=fBNz5xF-Kx4"),
    ])

    w("getting-started","Getting Started",
    intro="This lesson gets you writing Node.js code immediately — a basic HTTP server, reading files, and using npm to manage dependencies.",
    overview=["Create a basic HTTP server with the http module.","Read and write files with the fs module.","Use npm to install and manage packages.","Understand package.json and node_modules."],
    body="""
<h2 class="lesson-section-title" id="http-server">Your First HTTP Server</h2>
""" + code("""// server.js
const http = require('http');

const server = http.createServer((req, res) => {
  console.log(`${req.method} ${req.url}`);

  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('<h1>Hello from Node.js!</h1>');
});

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000');
});
""") + code("""# Run it
node server.js
# Open http://localhost:3000 in your browser
""") + """
<h2 class="lesson-section-title" id="file-system">File System Operations</h2>
""" + code("""const fs = require('fs').promises;  // promise-based API

// Read a file
const content = await fs.readFile('./data.txt', 'utf-8');
console.log(content);

// Write a file
await fs.writeFile('./output.txt', 'Hello, World!');

// Append to a file
await fs.appendFile('./log.txt', `${new Date().toISOString()} — event\\n`);

// Check if file exists
try {
  await fs.access('./file.txt');
  console.log('File exists');
} catch {
  console.log('File does not exist');
}
""") + """
<h2 class="lesson-section-title" id="npm">npm Basics</h2>
""" + code("""# Initialise a project
npm init -y

# Install a package (saved to dependencies)
npm install express

# Install a dev dependency
npm install --save-dev nodemon

# package.json scripts
{
  "scripts": {
    "start": "node server.js",
    "dev":   "nodemon server.js"  // restarts on file changes
  }
}

npm run dev
"""),
    kc=[("What does http.createServer return?","http-server"),
        ("What is the difference between dependencies and devDependencies?","npm"),
        ("What does nodemon do?","npm")],
    assignments=["Build a Node.js server that serves different HTML responses based on the URL path.","Add nodemon to your project so the server restarts automatically on changes."],
    resources=[
        ("Node.js — Getting Started Guide","https://nodejs.org/en/learn/getting-started/introduction-to-nodejs"),
        ("YouTube — Node.js File System Module (Traversy Media)","https://www.youtube.com/watch?v=xHLd36QoS4k"),
    ])

    w("debugging-node","Debugging Node",
    intro="Debugging server-side code requires different tools than the browser. This lesson covers the built-in Node.js debugger, VS Code debugging, and effective logging strategies.",
    overview=["Use console.log effectively for server-side debugging.","Set up VS Code's built-in Node.js debugger.","Use the --inspect flag to connect Chrome DevTools to Node.","Use a logger library like Morgan for HTTP request logging."],
    body="""
<h2 class="lesson-section-title" id="console-logging">Effective console.log</h2>
""" + code("""// Label your logs
console.log('[Auth] User logged in:', user.id);
console.log('[DB] Query took:', duration, 'ms');
console.error('[Server] Fatal error:', error);

// Log objects clearly
console.log('User:', JSON.stringify(user, null, 2));

// console.table for arrays of objects
console.table(users.map(u => ({ id: u.id, name: u.name })));

// Measure timing
console.time('database-query');
await db.query('SELECT * FROM users');
console.timeEnd('database-query');
""") + """
<h2 class="lesson-section-title" id="vscode-debugger">VS Code Debugger</h2>
""" + code("""// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Launch Server",
      "program": "${workspaceFolder}/server.js",
      "restart": true,
      "runtimeExecutable": "nodemon",
      "console": "integratedTerminal"
    }
  ]
}
// Press F5 in VS Code to start debugging
// Set breakpoints by clicking to the left of line numbers
""") + """
<h2 class="lesson-section-title" id="morgan">HTTP Request Logging with Morgan</h2>
""" + code("""npm install morgan
""") + code("""const express = require('express');
const morgan  = require('morgan');

const app = express();
app.use(morgan('dev'));  // logs: GET /users 200 15ms

// Log to a file
const fs   = require('fs');
const path = require('path');
const accessLog = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' });
app.use(morgan('combined', { stream: accessLog }));
"""),
    kc=[("How do you connect the Chrome DevTools debugger to a running Node.js process?","vscode-debugger"),
        ("What does morgan log?","morgan"),
        ("What is the --inspect flag used for?","vscode-debugger")],
    assignments=["Add VS Code debug configuration to your Node.js project and set at least one breakpoint.","Add Morgan to your Express server and observe the request logs."],
    resources=[
        ("Node.js — Debugging Guide","https://nodejs.org/en/learn/getting-started/debugging"),
        ("Morgan npm package","https://www.npmjs.com/package/morgan"),
        ("YouTube — Node.js Debugging in VS Code (Microsoft)","https://www.youtube.com/watch?v=2oFKNL7vYV8"),
    ])

    w("introduction-to-express","Introduction to Express",
    intro="Express is a minimal and flexible Node.js web framework. It simplifies the creation of web servers with routing, middleware, and request/response helpers.",
    overview=["Create an Express server.","Define routes for different HTTP methods and paths.","Use middleware with app.use().","Send responses: HTML, JSON, status codes."],
    body="""
<h2 class="lesson-section-title" id="express-basics">Express Basics</h2>
""" + code("""npm install express
""") + code("""const express = require('express');
const app     = express();

// Parse JSON request bodies
app.use(express.json());

// Parse URL-encoded form bodies
app.use(express.urlencoded({ extended: true }));

// Serve static files from 'public' folder
app.use(express.static('public'));

// Route handlers
app.get('/', (req, res) => {
  res.send('<h1>Hello, Express!</h1>');
});

app.get('/api/users', (req, res) => {
  res.status(200).json({ users: [] });
});

app.post('/api/users', (req, res) => {
  const { name, email } = req.body;
  // create user...
  res.status(201).json({ message: 'User created', name, email });
});

// 404 handler — placed after all routes
app.use((req, res) => {
  res.status(404).json({ error: 'Not found' });
});

// Error handler — four parameters
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal server error' });
});

app.listen(3000, () => console.log('Server running on port 3000'));
""") + """
<h2 class="lesson-section-title" id="route-params">Route Parameters and Query Strings</h2>
""" + code("""// URL parameter — /users/42
app.get('/users/:id', (req, res) => {
  const { id } = req.params;  // '42' (always a string)
  res.json({ userId: id });
});

// Query string — /search?q=hello&limit=10
app.get('/search', (req, res) => {
  const { q, limit = 10 } = req.query;
  res.json({ query: q, limit: parseInt(limit) });
});
"""),
    kc=[("What does app.use() do?","express-basics"),
        ("What is the difference between req.params and req.query?","route-params"),
        ("What does the error handler middleware's four parameters mean?","express-basics")],
    assignments=["Build an Express server with at least 5 routes covering GET and POST.","Add a 404 handler and a global error handler."],
    resources=[
        ("Express.js — Getting Started","https://expressjs.com/en/starter/hello-world.html"),
        ("YouTube — Express.js Crash Course (Traversy Media)","https://www.youtube.com/watch?v=L72fhGm1tfE"),
    ])

    w("express-routes-and-controllers","Express Routes and Controllers",
    intro="As Express apps grow, keeping all route handlers in one file becomes unmanageable. This lesson covers how to organise routes and controllers into separate files.",
    overview=["Use express.Router() to create modular route files.","Separate route definitions from controller logic.","Mount routers on the main app.","Use async error handling middleware."],
    body="""
<h2 class="lesson-section-title" id="router">express.Router()</h2>
""" + code("""// routes/users.js
const router = require('express').Router();
const userController = require('../controllers/userController');

router.get('/',    userController.getAllUsers);
router.get('/:id', userController.getUserById);
router.post('/',   userController.createUser);
router.put('/:id', userController.updateUser);
router.delete('/:id', userController.deleteUser);

module.exports = router;
""") + code("""// controllers/userController.js
const users = [];  // replace with DB later

exports.getAllUsers = (req, res) => {
  res.json(users);
};

exports.getUserById = (req, res) => {
  const user = users.find(u => u.id === req.params.id);
  if (!user) return res.status(404).json({ error: 'User not found' });
  res.json(user);
};

exports.createUser = (req, res) => {
  const user = { id: Date.now().toString(), ...req.body };
  users.push(user);
  res.status(201).json(user);
};
""") + code("""// app.js — mount the router
const userRouter = require('./routes/users');
app.use('/api/users', userRouter);

// GET /api/users      → getAllUsers
// GET /api/users/:id  → getUserById
// POST /api/users     → createUser
""") + """
<h2 class="lesson-section-title" id="async-errors">Async Error Handling</h2>
""" + code("""// Without async error handling — unhandled promise rejections
app.get('/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id); // could throw!
  res.json(user);
});

// With error handling — wrap async handlers
const asyncHandler = fn => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

app.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await User.findById(req.params.id);
  if (!user) return res.status(404).json({ error: 'Not found' });
  res.json(user);
}));

// Or install: npm install express-async-errors
require('express-async-errors');  // patches Express to handle async errors
"""),
    kc=[("What does express.Router() create?","router"),
        ("What is the benefit of separating controllers from routes?","router"),
        ("Why do async route handlers need special error handling?","async-errors")],
    assignments=["Refactor your Express server to use separate router and controller files.","Add asyncHandler to all async route handlers."],
    resources=[
        ("Express.js — Router","https://expressjs.com/en/4x/api.html#router"),
        ("YouTube — Express Router and Controllers (Traversy Media)","https://www.youtube.com/watch?v=lY6icfhap2o"),
    ])

    w("express-views","Express Views",
    intro="Server-side rendering generates HTML on the server and sends it to the browser. Express supports multiple template engines. This lesson covers EJS — the most straightforward option.",
    overview=["Set up EJS as a view engine.","Render templates with res.render().","Pass data from routes to views.","Use EJS partials for reusable HTML fragments."],
    body="""
<h2 class="lesson-section-title" id="ejs-setup">Setting Up EJS</h2>
""" + code("""npm install ejs
""") + code("""// app.js
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Directory structure
views/
├── partials/
│   ├── header.ejs
│   └── footer.ejs
├── index.ejs
├── users.ejs
└── user-detail.ejs
""") + """
<h2 class="lesson-section-title" id="templates">EJS Template Syntax</h2>
""" + code("""<!-- views/index.ejs -->
<!DOCTYPE html>
<html>
<head>
  <title><%= pageTitle %></title>  <!-- output escaped value -->
</head>
<body>
  <%- include('partials/header') %>  <!-- include partial -->

  <h1><%= heading %></h1>

  <% if (users.length === 0) { %>  <!-- JS code block -->
    <p>No users found.</p>
  <% } else { %>
    <ul>
      <% users.forEach(user => { %>
        <li>
          <a href="/users/<%= user.id %>"><%= user.name %></a>
        </li>
      <% }) %>
    </ul>
  <% } %>

  <%- include('partials/footer') %>
</body>
</html>
""") + code("""// Route — pass data to the view
app.get('/', async (req, res) => {
  const users = await User.find();
  res.render('index', {
    pageTitle: 'Home',
    heading: 'All Users',
    users,
  });
});
"""),
    kc=[("What is the difference between <%= %> and <%- %> in EJS?","templates"),
        ("How do you pass data from a route to an EJS view?","templates"),
        ("What are EJS partials used for?","ejs-setup")],
    assignments=["Build an Express app with EJS views showing a list of items and a detail page.","Create a header and footer partial and include them in all pages."],
    resources=[
        ("EJS — Official Documentation","https://ejs.co/"),
        ("YouTube — EJS Template Engine (Traversy Media)","https://www.youtube.com/watch?v=Ik0KzjfNWYk"),
    ])

    w("project-mini-message-board","Project: Mini Message Board",
    intro="Build a simple message board where users can view and post messages. This is your first full Express project combining routing, views, and in-memory data storage.",
    overview=["Build a full Express application with GET and POST routes.","Display messages on a page rendered with EJS.","Handle form submission and add messages to the list.","Use redirects after form submission."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>An index page listing all messages (author, text, timestamp)</li>
  <li>A "New Message" form page with author and message fields</li>
  <li>Submitting the form adds the message and redirects to the index</li>
  <li>Clicking a message title shows a detail page for that message</li>
  <li>Messages stored in a module-level array (no database yet)</li>
</ul>
""" + code("""// app.js — route structure
app.get('/',         messageController.index);       // show all messages
app.get('/new',      messageController.newForm);     // show form
app.post('/new',     messageController.createMessage);// handle form submit
app.get('/:id',      messageController.showMessage); // single message
""") + code("""// controllers/messageController.js
const messages = [];

exports.index = (req, res) => {
  res.render('index', { messages });
};

exports.newForm = (req, res) => {
  res.render('new-message');
};

exports.createMessage = (req, res) => {
  const { author, text } = req.body;
  messages.push({ id: Date.now(), author, text, createdAt: new Date() });
  res.redirect('/');  // POST → redirect → GET (PRG pattern)
};
""") + code("""mkdir ~/devpath-projects/mini-message-board
cd ~/devpath-projects/mini-message-board
npm init -y
npm install express ejs
"""),
    kc=[("What is the POST → Redirect → GET pattern and why use it?","requirements"),
        ("Where does Express get the submitted form data?","requirements")],
    assignments=["Complete the Mini Message Board meeting all requirements.","Push to GitHub."],
    resources=[
        ("Express.js — Routing","https://expressjs.com/en/guide/routing.html"),
        ("YouTube — Express Mini Message Board","https://www.youtube.com/watch?v=LM75CVngL8E"),
    ])

    w("introduction-to-mongodb","Introduction to MongoDB",
    intro="MongoDB is a document-oriented NoSQL database. Instead of tables and rows, it stores data as flexible JSON-like documents. This makes it natural to use with JavaScript applications.",
    overview=["Understand what MongoDB is and when to use it.","Know the difference between SQL and NoSQL databases.","Understand MongoDB's data model: databases, collections, documents.","Perform basic CRUD operations with the MongoDB shell."],
    body="""
<h2 class="lesson-section-title" id="what-is-mongodb">What Is MongoDB?</h2>
<p>MongoDB stores data as BSON documents (Binary JSON) in collections, rather than rows in tables. This flexible schema means documents in the same collection can have different fields — great for evolving data structures.</p>

<h2 class="lesson-section-title" id="sql-vs-nosql">SQL vs. NoSQL</h2>
<ul>
  <li><strong>SQL (relational)</strong> — structured tables with fixed schemas, relationships via foreign keys, strong consistency. Great for complex queries and transactions.</li>
  <li><strong>NoSQL (document)</strong> — flexible documents, horizontal scaling, great for hierarchical data and rapid iteration. Less suited for complex joins.</li>
</ul>

<h2 class="lesson-section-title" id="crud">Basic MongoDB Operations</h2>
""" + code("""// MongoDB shell / Compass

// Insert
db.users.insertOne({ name: "Alice", email: "alice@example.com", age: 28 })
db.users.insertMany([...])

// Find
db.users.find()                        // all documents
db.users.find({ age: { $gt: 25 } })    // filtered
db.users.findOne({ email: "alice@example.com" })

// Update
db.users.updateOne(
  { email: "alice@example.com" },       // filter
  { $set: { age: 29 } }                 // update operator
)

// Delete
db.users.deleteOne({ email: "alice@example.com" })
db.users.deleteMany({ age: { $lt: 18 } })
"""),
    kc=[("What is the MongoDB equivalent of a SQL table?","what-is-mongodb"),
        ("What is a MongoDB document?","what-is-mongodb"),
        ("When would you choose SQL over MongoDB?","sql-vs-nosql")],
    assignments=["Install MongoDB locally or create a free Atlas cluster.","Create a database, insert 5 documents, and practise all four CRUD operations in the shell."],
    resources=[
        ("MongoDB — Getting Started","https://www.mongodb.com/docs/manual/tutorial/getting-started/"),
        ("MongoDB Atlas — Free Tier","https://www.mongodb.com/cloud/atlas/register"),
        ("YouTube — MongoDB Crash Course (Traversy Media)","https://www.youtube.com/watch?v=-56x56UppqQ"),
    ])

    w("mongoose-primer","Mongoose Primer",
    intro="Mongoose is an Object Document Mapper (ODM) for MongoDB and Node.js. It provides schema-based validation, type casting, and a clean API for interacting with MongoDB from Express applications.",
    overview=["Connect to MongoDB with Mongoose.","Define schemas and models.","Perform CRUD operations with Mongoose methods.","Validate data with Mongoose validators."],
    body="""
<h2 class="lesson-section-title" id="setup">Setup and Connection</h2>
""" + code("""npm install mongoose
""") + code("""// db.js
const mongoose = require('mongoose');

mongoose.connect(process.env.MONGODB_URI)
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('Connection error:', err));
""") + """
<h2 class="lesson-section-title" id="schemas-models">Schemas and Models</h2>
""" + code("""// models/User.js
const { Schema, model } = require('mongoose');

const userSchema = new Schema({
  name: {
    type: String,
    required: [true, 'Name is required'],
    trim: true,
    minlength: 2,
    maxlength: 50,
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    match: [/^\\S+@\\S+\\.\\S+$/, 'Invalid email format'],
  },
  age: {
    type: Number,
    min: 0,
    max: 150,
  },
  role: {
    type: String,
    enum: ['user', 'admin', 'moderator'],
    default: 'user',
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
});

module.exports = model('User', userSchema);
""") + """
<h2 class="lesson-section-title" id="crud-mongoose">CRUD with Mongoose</h2>
""" + code("""const User = require('./models/User');

// Create
const user = await User.create({ name: 'Alice', email: 'alice@example.com' });

// Read
const allUsers  = await User.find();
const oneUser   = await User.findById(id);
const byEmail   = await User.findOne({ email: 'alice@example.com' });
const filtered  = await User.find({ role: 'admin' }).sort({ name: 1 }).limit(10);

// Update
const updated = await User.findByIdAndUpdate(
  id,
  { $set: { name: 'Alicia' } },
  { new: true, runValidators: true }  // return updated doc, run validators
);

// Delete
await User.findByIdAndDelete(id);
"""),
    kc=[("What is a Mongoose schema?","schemas-models"),
        ("What does { new: true } do in findByIdAndUpdate?","crud-mongoose"),
        ("How do you add validation to a Mongoose schema field?","schemas-models")],
    assignments=["Define a Post schema with title, content, author (ref to User), and createdAt.","Build a controller with full CRUD operations for your Post model."],
    resources=[
        ("Mongoose — Getting Started","https://mongoosejs.com/docs/index.html"),
        ("YouTube — Mongoose Crash Course (Traversy Media)","https://www.youtube.com/watch?v=DZBGEVgL2eE"),
    ])

    w("project-inventory-application","Project: Inventory Application",
    intro="Build a full inventory management application using Express, Mongoose, and EJS. This is your first full-stack application with a real database.",
    overview=["Model categories and items with Mongoose.","Build full CRUD for both categories and items.","Implement form validation.","Deploy to a cloud platform."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Categories with: name and description</li>
  <li>Items with: name, description, category (ref), price, stock count, image URL</li>
  <li>Full CRUD for categories and items (Create, Read, Update, Delete)</li>
  <li>Category pages list all items in that category</li>
  <li>Form validation — no empty required fields</li>
  <li>Deployed to Fly.io, Railway, or Render (free tiers available)</li>
</ul>
""" + code("""// Project structure
inventory-app/
├── app.js
├── routes/
│   ├── categoryRoutes.js
│   └── itemRoutes.js
├── controllers/
│   ├── categoryController.js
│   └── itemController.js
├── models/
│   ├── Category.js
│   └── Item.js
├── views/
│   ├── partials/
│   ├── category/
│   └── item/
└── public/
""") + code("""mkdir ~/devpath-projects/inventory-application
cd ~/devpath-projects/inventory-application
npm init -y
npm install express mongoose ejs dotenv
"""),
    kc=[("What Mongoose relationship type connects Item to Category?","requirements"),
        ("What is the PRG pattern and why does it matter for form submission?","requirements")],
    assignments=["Complete the Inventory Application meeting all requirements.","Deploy to a free cloud platform and share the live URL."],
    resources=[
        ("Mongoose — Populate (references between documents)","https://mongoosejs.com/docs/populate.html"),
        ("Fly.io — Getting Started","https://fly.io/docs/getting-started/"),
        ("YouTube — Express MongoDB CRUD App (Traversy Media)","https://www.youtube.com/watch?v=-0exw-9YJBo"),
    ])

    w("authentication-basics","Authentication Basics",
    intro="Authentication verifies who a user is. This lesson covers the core concepts: hashing passwords, sessions, and the Passport.js authentication middleware.",
    overview=["Understand why passwords must be hashed, never stored plain.","Hash passwords with bcrypt.","Implement session-based authentication.","Use Passport.js with the local strategy."],
    body="""
<h2 class="lesson-section-title" id="password-hashing">Password Hashing with bcrypt</h2>
""" + code("""npm install bcryptjs
""") + code("""const bcrypt = require('bcryptjs');

// Registration — hash before saving
const saltRounds = 10;  // higher = slower = more secure
const hashedPassword = await bcrypt.hash(plainTextPassword, saltRounds);
await User.create({ email, password: hashedPassword });

// Login — compare plain text against stored hash
const isMatch = await bcrypt.compare(enteredPassword, user.password);
if (!isMatch) return res.status(401).json({ error: 'Invalid credentials' });
""") + """
<h2 class="lesson-section-title" id="sessions">Sessions</h2>
""" + code("""npm install express-session connect-mongo
""") + code("""const session = require('express-session');
const MongoStore = require('connect-mongo');

app.use(session({
  secret: process.env.SESSION_SECRET,  // from .env file
  resave: false,
  saveUninitialized: false,
  store: MongoStore.create({ mongoUrl: process.env.MONGODB_URI }),
  cookie: {
    maxAge: 7 * 24 * 60 * 60 * 1000,  // 7 days in ms
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
  },
}));
""") + """
<h2 class="lesson-section-title" id="passport">Passport.js Local Strategy</h2>
""" + code("""npm install passport passport-local
""") + code("""const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;

passport.use(new LocalStrategy(
  { usernameField: 'email' },
  async (email, password, done) => {
    try {
      const user = await User.findOne({ email });
      if (!user) return done(null, false, { message: 'User not found' });
      const isMatch = await bcrypt.compare(password, user.password);
      if (!isMatch) return done(null, false, { message: 'Wrong password' });
      return done(null, user);
    } catch (err) {
      return done(err);
    }
  }
));

passport.serializeUser((user, done) => done(null, user.id));
passport.deserializeUser(async (id, done) => {
  try {
    const user = await User.findById(id);
    done(null, user);
  } catch (err) { done(err); }
});

app.use(passport.initialize());
app.use(passport.session());

// Login route
app.post('/login', passport.authenticate('local', {
  successRedirect: '/dashboard',
  failureRedirect: '/login',
  failureFlash: true,
}));

// Logout
app.post('/logout', (req, res) => {
  req.logout(() => res.redirect('/'));
});

// Protect routes
function requireAuth(req, res, next) {
  if (req.isAuthenticated()) return next();
  res.redirect('/login');
}
app.get('/dashboard', requireAuth, (req, res) => {
  res.render('dashboard', { user: req.user });
});
"""),
    kc=[("Why must passwords be hashed before storing?","password-hashing"),
        ("What does bcrypt.compare() return?","password-hashing"),
        ("What does req.isAuthenticated() check?","passport")],
    assignments=["Add user registration and login to your Inventory Application using Passport.js.","Protect the create/edit/delete routes so only logged-in users can access them."],
    resources=[
        ("Passport.js Documentation","https://www.passportjs.org/docs/"),
        ("bcryptjs npm package","https://www.npmjs.com/package/bcryptjs"),
        ("YouTube — Node.js Authentication (Traversy Media)","https://www.youtube.com/watch?v=6FOq4cUdH8k"),
    ])

    w("security-configuration","Security Configuration",
    intro="A web application that ignores security is a liability. This lesson covers the essential security measures every Express application needs: environment variables, CORS, rate limiting, and security headers.",
    overview=["Use environment variables for secrets with dotenv.","Set security headers with Helmet.","Implement rate limiting to prevent abuse.","Configure CORS correctly.","Prevent common vulnerabilities: XSS, CSRF, injection."],
    body="""
<h2 class="lesson-section-title" id="env-vars">Environment Variables</h2>
""" + code("""npm install dotenv
""") + code("""// .env — NEVER commit this file to Git
MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/mydb
SESSION_SECRET=a-very-long-random-string-here
JWT_SECRET=another-random-string
PORT=3000
NODE_ENV=development

// .gitignore
.env
node_modules/
""") + code("""// Load at the top of your entry file
require('dotenv').config();

// Access anywhere
const port = process.env.PORT || 3000;
const mongoUri = process.env.MONGODB_URI;
""") + """
<h2 class="lesson-section-title" id="helmet">Helmet — Security Headers</h2>
""" + code("""npm install helmet
""") + code("""const helmet = require('helmet');
app.use(helmet());

// Helmet sets these headers automatically:
// X-Content-Type-Options: nosniff
// X-Frame-Options: DENY
// X-XSS-Protection: 1; mode=block
// Content-Security-Policy: ...
// Referrer-Policy: no-referrer
// Strict-Transport-Security: max-age=15552000; includeSubDomains
""") + """
<h2 class="lesson-section-title" id="rate-limiting">Rate Limiting</h2>
""" + code("""npm install express-rate-limit
""") + code("""const rateLimit = require('express-rate-limit');

// Apply to all requests
app.use(rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minutes
  max: 100,                   // limit each IP to 100 requests per window
  message: 'Too many requests, please try again later.',
}));

// Stricter limit for auth routes
const authLimiter = rateLimit({
  windowMs: 60 * 60 * 1000,  // 1 hour
  max: 10,                    // 10 login attempts per hour
});
app.use('/login', authLimiter);
app.use('/register', authLimiter);
"""),
    kc=[("Why should .env never be committed to Git?","env-vars"),
        ("What does Helmet do?","helmet"),
        ("What does rate limiting prevent?","rate-limiting")],
    assignments=["Add dotenv, Helmet, and rate limiting to your Express application.","Verify your .env file is in .gitignore."],
    resources=[
        ("Helmet.js Documentation","https://helmetjs.github.io/"),
        ("express-rate-limit Documentation","https://www.npmjs.com/package/express-rate-limit"),
        ("YouTube — Node.js Security Best Practices (Traversy Media)","https://www.youtube.com/watch?v=zvtUsagkFkc"),
    ])

    w("project-members-only","Project: Members Only",
    intro="Build a members-only message board. Non-members can see messages but not who wrote them. Members can see author information. Admins can delete messages.",
    overview=["Implement registration with membership upgrade.","Show different content to different user roles.","Implement admin-only delete functionality.","Use Passport.js for complete authentication flow."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Users can sign up with name, username, and password</li>
  <li>Signed-up users can see a form to create messages</li>
  <li>All users can see messages, but only members see the author and timestamp</li>
  <li>A secret passcode page upgrades a user to member status</li>
  <li>Admin users (set in the database) can see a delete button on every message</li>
  <li>Bonus: add a confirm dialog before deleting</li>
</ul>
""" + code("""// User model
const userSchema = new Schema({
  name:       { type: String, required: true },
  username:   { type: String, required: true, unique: true },
  password:   { type: String, required: true },
  membership: { type: Boolean, default: false },
  isAdmin:    { type: Boolean, default: false },
});

// Message model
const messageSchema = new Schema({
  title:     { type: String, required: true },
  text:      { type: String, required: true },
  author:    { type: Schema.Types.ObjectId, ref: 'User', required: true },
  createdAt: { type: Date, default: Date.now },
});
"""),
    kc=[("How does the app show different content to members vs non-members?","requirements"),
        ("How do you upgrade a user to admin status?","requirements")],
    assignments=["Complete the Members Only project meeting all requirements.","Push to GitHub and deploy."],
    resources=[
        ("Passport.js — Local Strategy","https://www.passportjs.org/concepts/authentication/strategies/"),
        ("YouTube — Members Only Node.js App","https://www.youtube.com/watch?v=6FOq4cUdH8k"),
    ])

    w("apis","APIs",
    intro="REST APIs let your backend serve data to any client — a React frontend, a mobile app, or a third-party service. This lesson covers designing and building RESTful APIs with Express.",
    overview=["Understand REST principles.","Design RESTful routes.","Return appropriate HTTP status codes.","Build a complete CRUD API."],
    body="""
<h2 class="lesson-section-title" id="rest-principles">REST Principles</h2>
<p>REST (Representational State Transfer) is an architectural style for APIs. Key conventions:</p>
<ul>
  <li>Resources are nouns in the URL: <code>/users</code>, <code>/posts</code>, not <code>/getUsers</code></li>
  <li>HTTP verbs define the action: GET (read), POST (create), PUT/PATCH (update), DELETE (delete)</li>
  <li>Stateless — each request contains all information needed</li>
  <li>Return appropriate status codes</li>
</ul>
""" + code("""// RESTful route conventions
GET    /api/posts          → list all posts
GET    /api/posts/:id      → get one post
POST   /api/posts          → create a post
PUT    /api/posts/:id      → replace a post completely
PATCH  /api/posts/:id      → partially update a post
DELETE /api/posts/:id      → delete a post

// Status codes
200 OK            → successful GET, PUT, PATCH
201 Created       → successful POST
204 No Content    → successful DELETE (no body)
400 Bad Request   → invalid request data
401 Unauthorized  → not authenticated
403 Forbidden     → authenticated but not authorised
404 Not Found     → resource doesn't exist
422 Unprocessable → validation errors
500 Internal Error→ server error
""") + """
<h2 class="lesson-section-title" id="building-api">Building a REST API</h2>
""" + code("""// routes/posts.js
router.get('/', asyncHandler(async (req, res) => {
  const { page = 1, limit = 20, sort = '-createdAt' } = req.query;
  const posts = await Post.find()
    .populate('author', 'name')  // include author name
    .sort(sort)
    .skip((page - 1) * limit)
    .limit(parseInt(limit));
  const total = await Post.countDocuments();
  res.json({ posts, total, page: parseInt(page), pages: Math.ceil(total/limit) });
}));

router.post('/', requireAuth, asyncHandler(async (req, res) => {
  const { title, content } = req.body;
  if (!title || !content) {
    return res.status(400).json({ error: 'Title and content are required' });
  }
  const post = await Post.create({ title, content, author: req.user.id });
  res.status(201).json(post);
}));
"""),
    kc=[("What HTTP verb should you use to partially update a resource?","rest-principles"),
        ("What status code should a successful POST return?","rest-principles"),
        ("What does .populate() do in Mongoose?","building-api")],
    assignments=["Build a complete REST API for a blog with posts and comments.","Test all endpoints using a REST client like Thunder Client (VS Code extension)."],
    resources=[
        ("MDN — HTTP Request Methods","https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods"),
        ("REST API Design Best Practices","https://restfulapi.net/"),
        ("YouTube — REST API with Node.js (Traversy Media)","https://www.youtube.com/watch?v=mjZh1y6LMp4"),
    ])

    w("api-security-and-authentication","API Security and Authentication",
    intro="REST APIs cannot use session cookies the same way server-rendered apps do. JSON Web Tokens (JWT) are the standard for stateless API authentication.",
    overview=["Understand why JWTs are used for APIs.","Generate and verify JWTs.","Protect API routes with JWT middleware.","Implement refresh tokens for long-lived sessions."],
    body="""
<h2 class="lesson-section-title" id="jwt">JSON Web Tokens</h2>
<p>A JWT is a compact, URL-safe token containing signed claims. Because the server signs the token with a secret, it can verify the token's authenticity without storing session data — making APIs stateless and scalable.</p>
""" + code("""npm install jsonwebtoken
""") + code("""const jwt = require('jsonwebtoken');

// Generate a token on login
const token = jwt.sign(
  { userId: user._id, role: user.role },  // payload
  process.env.JWT_SECRET,                  // secret
  { expiresIn: '15m' }                     // short expiry for access tokens
);
res.json({ token });

// Verify middleware
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1]; // "Bearer TOKEN"

  if (!token) return res.status(401).json({ error: 'Access token required' });

  jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
    if (err) return res.status(403).json({ error: 'Invalid or expired token' });
    req.user = decoded;
    next();
  });
}

// Protect routes
app.get('/api/profile', authenticateToken, (req, res) => {
  res.json({ userId: req.user.userId });
});
""") + """
<h2 class="lesson-section-title" id="refresh-tokens">Refresh Tokens</h2>
""" + code("""// Access token — short lived (15 minutes)
const accessToken  = jwt.sign({ userId }, process.env.JWT_SECRET, { expiresIn: '15m' });

// Refresh token — long lived (7 days), stored securely
const refreshToken = jwt.sign({ userId }, process.env.REFRESH_SECRET, { expiresIn: '7d' });
// Store refresh token in httpOnly cookie or database

// Client sends refresh token when access token expires
app.post('/api/refresh', (req, res) => {
  const { refreshToken } = req.cookies;
  jwt.verify(refreshToken, process.env.REFRESH_SECRET, (err, decoded) => {
    if (err) return res.status(403).json({ error: 'Invalid refresh token' });
    const newAccessToken = jwt.sign({ userId: decoded.userId }, process.env.JWT_SECRET, { expiresIn: '15m' });
    res.json({ accessToken: newAccessToken });
  });
});
"""),
    kc=[("Why use JWTs instead of sessions for APIs?","jwt"),
        ("Where does the client send the JWT in requests?","jwt"),
        ("Why are access tokens short-lived?","refresh-tokens")],
    assignments=["Refactor your Blog API to use JWT authentication.","Implement a refresh token endpoint."],
    resources=[
        ("jwt.io — JWT Debugger and Documentation","https://jwt.io/"),
        ("YouTube — JWT Authentication (Web Dev Simplified)","https://www.youtube.com/watch?v=mbsmsi7l3r4"),
    ])

    w("project-blog-api","Project: Blog API",
    intro="Build a complete RESTful Blog API with JWT authentication. A separate React frontend will consume it. This is your first true full-stack API project.",
    overview=["Build a full CRUD API for blog posts and comments.","Implement JWT authentication for protected routes.","Handle authorisation — users can only edit their own posts.","Write API documentation."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>Auth routes:</strong> POST /auth/register, POST /auth/login, POST /auth/refresh</li>
  <li><strong>Post routes:</strong> Full CRUD. Only the author can update/delete their posts.</li>
  <li><strong>Comment routes:</strong> GET comments for a post, POST a comment (authenticated), DELETE (author only)</li>
  <li><strong>Admin routes:</strong> Admins can publish/unpublish any post</li>
  <li>Pagination on list endpoints</li>
  <li>A separate React frontend that reads posts (no auth required for reading)</li>
  <li>A second React frontend (admin panel) for creating and managing posts</li>
</ul>
""" + code("""// API endpoints
POST   /api/auth/register
POST   /api/auth/login
GET    /api/posts                 → public, paginated
GET    /api/posts/:id             → public
POST   /api/posts                 → authenticated
PUT    /api/posts/:id             → author only
DELETE /api/posts/:id             → author only
PATCH  /api/posts/:id/publish     → admin only
GET    /api/posts/:id/comments    → public
POST   /api/posts/:id/comments    → authenticated
DELETE /api/posts/:id/comments/:cid → author only
"""),
    kc=[("How do you ensure only a post's author can delete it?","requirements"),
        ("Why create two separate React frontends?","requirements")],
    assignments=["Complete the Blog API and both React frontends.","Deploy all three: the API, the public blog, and the admin panel."],
    resources=[
        ("Express.js — API Documentation","https://expressjs.com/en/4x/api.html"),
        ("YouTube — MERN Stack Blog API (Traversy Media)","https://www.youtube.com/watch?v=7CqJlxBYj-M"),
    ])

    w("testing-express","Testing Express",
    intro="Testing Express APIs requires sending HTTP requests and asserting on responses. Supertest is the standard library for this — it works alongside Jest or Vitest.",
    overview=["Set up Supertest with Jest for API testing.","Write integration tests for Express routes.","Use an in-memory database for testing.","Test authentication flows."],
    body="""
<h2 class="lesson-section-title" id="setup">Setup</h2>
""" + code("""npm install --save-dev jest supertest @shelf/jest-mongodb
""") + code("""// app.js — export the app without calling listen
const express = require('express');
const app = express();
// ... routes, middleware ...
module.exports = app;  // don't call app.listen here

// server.js — entry point
const app = require('./app');
app.listen(process.env.PORT || 3000);
""") + """
<h2 class="lesson-section-title" id="writing-tests">Writing API Tests</h2>
""" + code("""// routes/users.test.js
const request = require('supertest');
const app     = require('../app');
const User    = require('../models/User');

describe('POST /api/users', () => {
  it('creates a new user and returns 201', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ name: 'Alice', email: 'alice@test.com', password: 'password123' });

    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('id');
    expect(response.body.email).toBe('alice@test.com');
  });

  it('returns 400 when email is missing', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ name: 'Alice' });

    expect(response.status).toBe(400);
    expect(response.body.error).toMatch(/email/i);
  });
});

describe('GET /api/users/:id', () => {
  it('returns 404 for non-existent user', async () => {
    const fakeId = '507f1f77bcf86cd799439011';  // valid ObjectId format
    const response = await request(app).get(`/api/users/${fakeId}`);
    expect(response.status).toBe(404);
  });
});
"""),
    kc=[("Why export the app without calling listen?","setup"),
        ("What does supertest's request(app) give you?","writing-tests"),
        ("What is an in-memory database and why use it for testing?","setup")],
    assignments=["Write integration tests for your Blog API covering all CRUD routes.","Test authentication: protected routes return 401 without a token."],
    resources=[
        ("Supertest — GitHub Repository","https://github.com/ladjs/supertest"),
        ("YouTube — Node.js API Testing (Traversy Media)","https://www.youtube.com/watch?v=mMDObVCmqoM"),
    ])

    w("sql-basics","SQL Basics",
    intro="SQL (Structured Query Language) is the universal language of relational databases. This lesson covers the core SQL commands you need to store, retrieve, and manipulate data.",
    overview=["Understand relational database concepts: tables, rows, columns, primary keys.","Write SELECT queries with WHERE, ORDER BY, and LIMIT.","Join tables with INNER JOIN and LEFT JOIN.","Insert, update, and delete data."],
    body="""
<h2 class="lesson-section-title" id="select">SELECT Queries</h2>
""" + code("""-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT name, email, created_at FROM users;

-- Filter with WHERE
SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE role = 'admin' AND active = true;
SELECT * FROM users WHERE name LIKE 'Al%';  -- starts with 'Al'

-- Sort results
SELECT * FROM users ORDER BY created_at DESC;
SELECT * FROM users ORDER BY name ASC;

-- Limit and offset (pagination)
SELECT * FROM posts ORDER BY created_at DESC LIMIT 10 OFFSET 20;
-- page 3 of 10-per-page results
""") + """
<h2 class="lesson-section-title" id="joins">Joins</h2>
""" + code("""-- Tables: users(id, name), posts(id, title, user_id)

-- INNER JOIN — only rows that match in both tables
SELECT users.name, posts.title
FROM posts
INNER JOIN users ON posts.user_id = users.id;

-- LEFT JOIN — all posts, even if user is deleted
SELECT posts.title, users.name
FROM posts
LEFT JOIN users ON posts.user_id = users.id;

-- Multiple joins
SELECT posts.title, users.name, categories.name AS category
FROM posts
JOIN users      ON posts.user_id     = users.id
JOIN categories ON posts.category_id = categories.id
WHERE posts.published = true
ORDER BY posts.created_at DESC;
""") + """
<h2 class="lesson-section-title" id="mutations">INSERT, UPDATE, DELETE</h2>
""" + code("""-- Insert
INSERT INTO users (name, email, password_hash)
VALUES ('Alice', 'alice@example.com', '$2a$10$...');

-- Update
UPDATE users SET name = 'Alicia' WHERE id = 42;

-- Delete
DELETE FROM users WHERE id = 42;
DELETE FROM posts WHERE created_at < NOW() - INTERVAL '1 year';
"""),
    kc=[("What is the difference between INNER JOIN and LEFT JOIN?","joins"),
        ("How do you paginate results in SQL?","select"),
        ("What does LIKE 'Al%' match?","select")],
    assignments=["Install PostgreSQL locally. Create a database and practise all queries above.","Write a query that joins users and posts to show each user's post count."],
    resources=[
        ("PostgreSQL — Tutorial","https://www.postgresqltutorial.com/"),
        ("SQLZoo — Interactive SQL Tutorial","https://sqlzoo.net/"),
        ("YouTube — SQL Crash Course (Traversy Media)","https://www.youtube.com/watch?v=OqjJjpjDRLc"),
    ])

    w("databases-and-sql","Databases and SQL",
    intro="This lesson goes deeper into relational database design — normalisation, indexes, transactions, and how PostgreSQL fits into a Node.js application.",
    overview=["Understand database normalisation.","Use indexes to speed up queries.","Use transactions for atomic operations.","Connect PostgreSQL to a Node.js application."],
    body="""
<h2 class="lesson-section-title" id="normalisation">Database Normalisation</h2>
<p>Normalisation is the process of organising a database to reduce redundancy. The goal is to store each piece of data in exactly one place.</p>
""" + code("""-- UNNORMALISED — repeats user info in every order
orders (id, product, user_name, user_email, user_address)

-- NORMALISED — user data lives once in users table
users  (id, name, email, address)
orders (id, product, user_id)  -- user_id is a foreign key to users.id
""") + """
<h2 class="lesson-section-title" id="indexes">Indexes</h2>
""" + code("""-- Indexes speed up queries on frequently-searched columns
-- Without index: full table scan — O(n)
-- With index:    B-tree lookup — O(log n)

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_posts_user_id ON posts(user_id);

-- Unique constraint creates an index automatically
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);

-- Check if a query uses an index
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'alice@example.com';
""") + """
<h2 class="lesson-section-title" id="node-postgres">PostgreSQL in Node.js</h2>
""" + code("""npm install pg
""") + code("""const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

// Query with parameterised values (prevents SQL injection)
const result = await pool.query(
  'SELECT * FROM users WHERE email = $1',
  [email]  // $1 is replaced with this value — safely
);
const user = result.rows[0];

// Insert and get the created row back
const { rows } = await pool.query(
  'INSERT INTO users (name, email) VALUES ($1, $2) RETURNING *',
  [name, email]
);
const newUser = rows[0];
"""),
    kc=[("What is database normalisation and why does it matter?","normalisation"),
        ("What does an index do for query performance?","indexes"),
        ("Why must you use parameterised queries instead of string concatenation?","node-postgres")],
    assignments=["Design a normalised schema for a blog with users, posts, comments, and tags.","Add indexes to the columns you query most frequently."],
    resources=[
        ("PostgreSQL — Documentation","https://www.postgresql.org/docs/"),
        ("node-postgres (pg) Documentation","https://node-postgres.com/"),
        ("YouTube — PostgreSQL Tutorial (freeCodeCamp)","https://www.youtube.com/watch?v=qw--VYLpxG4"),
    ])

    w("knex-js","Knex.js",
    intro="Knex.js is a SQL query builder for Node.js. It provides a clean JavaScript API for building SQL queries, running migrations, and seeding databases — while keeping you close to SQL.",
    overview=["Set up Knex.js with PostgreSQL.","Write queries using the Knex query builder API.","Run database migrations.","Seed the database with initial data."],
    body="""
<h2 class="lesson-section-title" id="setup">Setup</h2>
""" + code("""npm install knex pg
npx knex init  # creates knexfile.js
""") + code("""// knexfile.js
module.exports = {
  development: {
    client: 'pg',
    connection: process.env.DATABASE_URL,
    migrations: { directory: './db/migrations' },
    seeds:      { directory: './db/seeds' },
  },
};
""") + """
<h2 class="lesson-section-title" id="queries">Knex Query Builder</h2>
""" + code("""const db = require('./db');  // Knex instance

// SELECT
const users = await db('users').select('*');
const user  = await db('users').where({ id }).first();

// INSERT
const [id] = await db('users')
  .insert({ name, email })
  .returning('id');

// UPDATE
await db('users').where({ id }).update({ name: 'Alicia' });

// DELETE
await db('users').where({ id }).delete();

// JOIN
const posts = await db('posts')
  .join('users', 'posts.user_id', 'users.id')
  .select('posts.*', 'users.name as author_name');
""") + """
<h2 class="lesson-section-title" id="migrations">Migrations</h2>
""" + code("""# Create a migration file
npx knex migrate:make create_users_table

# Run migrations
npx knex migrate:latest

# Roll back
npx knex migrate:rollback
""") + code("""// db/migrations/20240101_create_users_table.js
exports.up = async (knex) => {
  await knex.schema.createTable('users', (table) => {
    table.increments('id').primary();
    table.string('name', 100).notNullable();
    table.string('email', 255).notNullable().unique();
    table.string('password_hash').notNullable();
    table.timestamps(true, true);  // created_at, updated_at
  });
};

exports.down = async (knex) => {
  await knex.schema.dropTable('users');
};
"""),
    kc=[("What does a database migration do?","migrations"),
        ("How do you prevent SQL injection with Knex?","queries"),
        ("What does the down function in a migration do?","migrations")],
    assignments=["Set up Knex in your project. Create migrations for your schema.","Run the migrations and seed the database with test data."],
    resources=[
        ("Knex.js Documentation","https://knexjs.org/"),
        ("YouTube — Knex.js Tutorial (Traversy Media)","https://www.youtube.com/watch?v=qlvdpfqhRpk"),
    ])

    w("project-file-uploader","Project: File Uploader",
    intro="Build a file upload service using Express, Multer, and cloud storage. Users can upload files, view their uploads, and share files with others.",
    overview=["Handle file uploads with Multer.","Store files in Supabase Storage or Cloudinary.","Build a file management interface.","Implement access control for files."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>User registration and login (Passport.js)</li>
  <li>Upload files (images, PDFs, documents — max 10MB)</li>
  <li>Files are stored in Supabase Storage or Cloudinary (not on the server)</li>
  <li>A dashboard showing the user's uploaded files</li>
  <li>Shareable links for each file</li>
  <li>Folders — users can organise files into named folders</li>
  <li>File metadata stored in PostgreSQL (name, size, type, url, owner)</li>
</ul>
""" + code("""npm install multer @supabase/supabase-js
""") + code("""const multer   = require('multer');
const { createClient } = require('@supabase/supabase-js');

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_KEY
);

// Store in memory, upload to cloud
const upload = multer({ storage: multer.memoryStorage(), limits: { fileSize: 10 * 1024 * 1024 } });

app.post('/upload', requireAuth, upload.single('file'), async (req, res) => {
  const { data, error } = await supabase.storage
    .from('user-files')
    .upload(`${req.user.id}/${Date.now()}-${req.file.originalname}`, req.file.buffer, {
      contentType: req.file.mimetype,
    });

  if (error) return res.status(500).json({ error: error.message });

  const { data: { publicUrl } } = supabase.storage
    .from('user-files')
    .getPublicUrl(data.path);

  // Save metadata to PostgreSQL
  await db('files').insert({
    name: req.file.originalname,
    size: req.file.size,
    type: req.file.mimetype,
    url:  publicUrl,
    owner_id: req.user.id,
  });

  res.redirect('/dashboard');
});
"""),
    kc=[("Why store files in cloud storage rather than on the server?","requirements"),
        ("What does multer.memoryStorage() do?","requirements")],
    assignments=["Complete the File Uploader meeting all requirements.","Deploy to a cloud platform."],
    resources=[
        ("Multer — File Upload Middleware","https://www.npmjs.com/package/multer"),
        ("Supabase — Storage Documentation","https://supabase.com/docs/guides/storage"),
        ("YouTube — File Uploads with Node.js (Web Dev Simplified)","https://www.youtube.com/watch?v=EVOFt8Its6I"),
    ])

    w("project-odinbook","Project: Odin-Book",
    intro="The capstone of the NodeJS course. Build a Facebook-like social network with user profiles, friend requests, and a news feed. This is a full-stack project using everything you have learned.",
    overview=["Build a complete social networking application.","Implement friend requests and friendships.","Build a news feed of friend activity.","Deploy the full-stack application."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>Authentication</strong> — sign up, log in, log out. Optional: social login (GitHub/Google OAuth)</li>
  <li><strong>Profiles</strong> — each user has a profile with photo, bio, and their posts</li>
  <li><strong>Posts</strong> — create, read, delete posts. Posts can include an image.</li>
  <li><strong>Likes</strong> — like and unlike posts</li>
  <li><strong>Comments</strong> — comment on posts</li>
  <li><strong>Friends</strong> — send, accept, reject, and cancel friend requests. Unfriend.</li>
  <li><strong>News Feed</strong> — shows posts from the user and their friends, newest first</li>
  <li><strong>Notifications</strong> — friend request received, post liked</li>
</ul>

<h2 class="lesson-section-title" id="architecture">Suggested Architecture</h2>
""" + code("""# Tech stack options

# Option A: Full Stack (Express + EJS or Express + React)
Backend:  Express + PostgreSQL (Knex) or MongoDB (Mongoose)
Frontend: React SPA consuming the REST API

# Option B: Server-rendered
Backend:  Express + EJS + PostgreSQL
Frontend: EJS templates + vanilla JS for interactive parts
""") + code("""mkdir ~/devpath-projects/odinbook
cd ~/devpath-projects/odinbook
git init
# Set up your chosen stack
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>This is a large project. Plan before you code. Write user stories, design the database schema, and sketch the component/page structure before writing any code. Scope to the core features first.</p>
</div>""",
    kc=[("What are the minimum features the social network must have?","requirements"),
        ("What is a news feed and how do you build it with SQL or MongoDB?","architecture")],
    assignments=["Complete Odin-Book meeting all requirements.","Deploy the full application publicly.","Add the live URL to your GitHub profile and resume."],
    resources=[
        ("Passport.js — OAuth Strategies","https://www.passportjs.org/concepts/authentication/strategies/"),
        ("YouTube — Social Media App (Traversy Media)","https://www.youtube.com/watch?v=ByGJQzlzxQg"),
        ("MDN — WebSockets (for real-time notifications)","https://developer.mozilla.org/en-US/docs/Web/API/WebSocket"),
    ])

    print(f"  NodeJS: {len(ALL)} lessons done")


# ════════════════════════════════════════════════════════════════════════════
#  4. GETTING HIRED
# ════════════════════════════════════════════════════════════════════════════
def seed_getting_hired():
    ldir = os.path.join(JS, "getting-hired", "lessons")
    root = "../../../../../"
    course_title = "Getting Hired"

    ALL = [
        ("introduction-to-getting-hired", "Introduction to Getting Hired"),
        ("how-to-get-hired",              "How to Get Hired as a Web Developer"),
        ("strategy",                      "Strategy"),
        ("it-starts-with-you",            "It Starts with You"),
        ("what-companies-want",           "What Do Companies Want?"),
        ("what-you-can-do",               "What Can You Do to Prepare?"),
        ("building-your-portfolio",       "Building Your Portfolio"),
        ("collecting-leads",              "Collecting Leads"),
        ("qualifying-leads",              "Qualifying Leads"),
        ("reaching-out",                  "Reaching Out"),
        ("preparing-for-interviews",      "Preparing for Interviews"),
        ("the-first-interview",           "The First Interview"),
        ("the-technical-interview",       "The Technical Interview"),
        ("after-the-interview",           "After the Interview"),
        ("handling-offers-and-negotiations","Handling Offers and Negotiations"),
    ]

    def lnk(sl, ti):
        cls = "sidebar-link"
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">Getting Hired</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">Preparing</div>'
        + lnk("introduction-to-getting-hired","Introduction")
        + lnk("how-to-get-hired","How to Get Hired")
        + lnk("strategy","Strategy")
        + lnk("it-starts-with-you","It Starts with You")
        + lnk("what-companies-want","What Companies Want")
        + lnk("what-you-can-do","What You Can Do")
        + lnk("building-your-portfolio","Building Your Portfolio")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Applying</div>'
        + lnk("collecting-leads","Collecting Leads")
        + lnk("qualifying-leads","Qualifying Leads")
        + lnk("reaching-out","Reaching Out")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Interviewing</div>'
        + lnk("preparing-for-interviews","Preparing for Interviews")
        + lnk("the-first-interview","The First Interview")
        + lnk("the-technical-interview","The Technical Interview")
        + lnk("after-the-interview","After the Interview")
        + lnk("handling-offers-and-negotiations","Offers and Negotiations")
        + '</div></aside>'
    )

    def w(slug, title, intro, overview, body, kc, assignments, resources):
        write_lesson(ldir, root, course_title, ALL, sidebar,
                     slug, title, intro, overview, body, kc, assignments, resources)

    w("introduction-to-getting-hired","Introduction to Getting Hired",
    intro="You have spent months building real skills and real projects. Now it is time to translate that into your first developer job. This course walks you through every step of the process — from crafting your portfolio to negotiating your offer.",
    overview=["Understand the job search process for entry-level developers.","Know what makes a developer portfolio compelling.","Understand the different stages of the interview process."],
    body="""
<h2 class="lesson-section-title" id="the-journey">The Journey Ahead</h2>
<p>Getting your first developer job is a job in itself. The average job search takes 3–6 months. You will send dozens of applications, go through multiple interview rounds, and face rejection — this is normal and not a reflection of your ability.</p>
<p>What sets successful job seekers apart is not talent — it is systematic effort, preparation, and persistence. This course gives you a framework for all three.</p>

<h2 class="lesson-section-title" id="what-this-covers">What This Course Covers</h2>
<ul>
  <li><strong>Preparation</strong> — understanding what companies want, building a portfolio, crafting your resume</li>
  <li><strong>The search</strong> — finding opportunities, qualifying them, and reaching out effectively</li>
  <li><strong>Interviews</strong> — technical screens, coding challenges, system design, and behavioural interviews</li>
  <li><strong>Offers</strong> — evaluating and negotiating job offers</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Start your job search before you feel "ready." Most developers start applying when they are about 80% through a curriculum. Waiting until you feel 100% ready means waiting forever.</p>
</div>""",
    kc=[("How long does the average entry-level developer job search take?","the-journey"),
        ("What are the four stages covered in this course?","what-this-covers")],
    assignments=["Set a target start date for actively applying. Write it down.","Read Eric Feng's article on the developer job search — linked below."],
    resources=[
        ("Hacker News — Who is Hiring? (monthly thread)","https://hn.algolia.com/?q=who+is+hiring"),
        ("YouTube — How to Get Your First Developer Job (Traversy Media)","https://www.youtube.com/watch?v=gKjGh6NTDtA"),
    ])

    w("how-to-get-hired","How to Get Hired as a Web Developer",
    intro="The developer job market has clear patterns. Understanding how hiring actually works — from the recruiter's perspective — dramatically improves your odds.",
    overview=["Understand how companies hire developers.","Know the typical interview pipeline.","Understand the difference between applying cold vs. warm referrals.","Know which companies are good targets for junior developers."],
    body="""
<h2 class="lesson-section-title" id="how-hiring-works">How Hiring Actually Works</h2>
<p>Most job postings receive hundreds of applications. Recruiters typically spend 6–10 seconds scanning a resume before deciding to keep or discard it. To get through this filter:</p>
<ul>
  <li>Your resume must contain the keywords from the job description</li>
  <li>Your GitHub profile must show recent, consistent activity</li>
  <li>Your portfolio projects must be deployed and impressive</li>
  <li>A referral from an employee skips the resume filter entirely</li>
</ul>

<h2 class="lesson-section-title" id="pipeline">The Typical Interview Pipeline</h2>
<ol>
  <li><strong>Resume screen</strong> — recruiter reviews your application (6–10 seconds)</li>
  <li><strong>Recruiter screen</strong> — 15–30 minute phone call. Cultural fit, logistics, salary range.</li>
  <li><strong>Technical screen</strong> — 30–60 minutes. Live coding on a platform like HackerRank or a take-home assignment.</li>
  <li><strong>Technical interview(s)</strong> — 45–90 minutes each. Data structures, algorithms, system design, code review.</li>
  <li><strong>Final round</strong> — multiple interviews in one day, often including a hiring manager interview.</li>
  <li><strong>Offer</strong> — verbal offer, written offer, negotiation.</li>
</ol>

<h2 class="lesson-section-title" id="good-targets">Good Targets for Junior Developers</h2>
<ul>
  <li>Small-to-medium companies (20–200 employees) — less competition, more responsibility, faster learning</li>
  <li>Companies that use your specific tech stack (React, Node, Rails, etc.)</li>
  <li>Companies with an explicit junior hiring programme</li>
  <li>Bootcamp hiring partners and companies that regularly hire career changers</li>
</ul>""",
    kc=[("What skips the resume filter?","how-hiring-works"),
        ("What are the six stages of a typical interview pipeline?","pipeline"),
        ("Why are small companies often better for junior developers?","good-targets")],
    assignments=["Research 10 companies in your city or that hire remotely that use your tech stack.","Find a person at each company on LinkedIn and note their name."],
    resources=[
        ("Glassdoor — Company Reviews","https://www.glassdoor.com/"),
        ("LinkedIn Jobs","https://www.linkedin.com/jobs/"),
        ("YouTube — How Tech Companies Hire (TechLead)","https://www.youtube.com/watch?v=NW1ND3gI0GI"),
    ])

    w("strategy","Strategy",
    intro="A strategic job search is not about sending as many applications as possible. It is about targeting the right companies and building genuine relationships — so most of your opportunities come from people, not job boards.",
    overview=["Understand the difference between spray-and-pray vs targeted job searching.","Build a tracking system for your job search.","Prioritise networking over cold applications.","Set realistic daily targets."],
    body="""
<h2 class="lesson-section-title" id="targeted-vs-spray">Targeted vs. Spray-and-Pray</h2>
<p><strong>Spray-and-pray</strong> means sending identical applications to dozens of job boards. It feels productive but has a very low success rate — you are competing with hundreds of people for generic roles.</p>
<p><strong>Targeted</strong> means identifying 20–30 specific companies you genuinely want to work for, researching them deeply, and pursuing them through multiple channels simultaneously: tailored applications, LinkedIn outreach, attending their meetups, and referrals through your network.</p>

<h2 class="lesson-section-title" id="tracking">Build a Job Search Tracker</h2>
<p>Track every opportunity in a spreadsheet or Notion database:</p>
<ul>
  <li>Company name and URL</li>
  <li>Role and job posting link</li>
  <li>Date applied</li>
  <li>Status: applied / screening / technical / final / offer / rejected</li>
  <li>Contact person (if any)</li>
  <li>Notes from each interaction</li>
  <li>Next action and due date</li>
</ul>

<h2 class="lesson-section-title" id="daily-targets">Daily Targets</h2>
<p>Treat the job search like a job: dedicate 4–6 hours per day. A reasonable daily target:</p>
<ul>
  <li>2 quality tailored applications</li>
  <li>3 LinkedIn connection requests with personalised notes</li>
  <li>1 follow-up message to a previous contact</li>
  <li>30 minutes of technical interview preparation</li>
</ul>""",
    kc=[("What is the difference between spray-and-pray and targeted job searching?","targeted-vs-spray"),
        ("What fields should your job search tracker include?","tracking"),
        ("What are reasonable daily job search targets?","daily-targets")],
    assignments=["Build a job search tracker in a spreadsheet or Notion.","Identify your top 20 target companies and add them to the tracker."],
    resources=[
        ("Notion — Job Search Tracker Template","https://www.notion.so/templates/job-search"),
        ("YouTube — Job Search Strategy for Developers (Traversy Media)","https://www.youtube.com/watch?v=gKjGh6NTDtA"),
    ])

    w("it-starts-with-you","It Starts with You",
    intro="Before you apply anywhere, you need clarity on what you want. Companies can tell when an applicant has no clear direction — and it kills your chances. This lesson helps you define your target role and story.",
    overview=["Clarify what kind of developer role you want.","Craft your developer story.","Know your answers to 'Tell me about yourself' and 'Why are you interested in this role?'","Identify your genuine strengths."],
    body="""
<h2 class="lesson-section-title" id="what-you-want">Know What You Want</h2>
<p>Answer these questions before applying to anything:</p>
<ul>
  <li>Frontend, backend, or full-stack? What tech stack?</li>
  <li>What industry interests you? FinTech? EdTech? SaaS? Agency work?</li>
  <li>Remote, hybrid, or in-office? What city if not remote?</li>
  <li>What size company? Startup or enterprise?</li>
  <li>What do you want to be doing in 2 years?</li>
</ul>

<h2 class="lesson-section-title" id="your-story">Your Developer Story</h2>
<p>Every developer has a story: how they got started, what they have built, and where they are headed. Your story must be authentic, concise, and compelling. Practice saying it out loud until it takes under 2 minutes and sounds natural.</p>
""" + code("""// Story structure
// 1. Who you were before (briefly)
// 2. What sparked your interest in development
// 3. How you learned (what you built)
// 4. What you are looking for now

// Example:
"I spent 5 years in customer support, which gave me a deep understanding
of user needs. Two years ago I started learning to code to build solutions
to problems I was seeing daily. I've built a full-stack recipe app, a weather
dashboard using the OpenWeather API, and a task manager with real-time
updates. I'm looking for a junior full-stack role where I can keep growing
and contribute to a product I believe in."
"""),
    kc=[("Why do you need to know what you want before applying?","what-you-want"),
        ("What is the structure of a good developer story?","your-story")],
    assignments=["Write your developer story following the structure above.","Practice saying it out loud until it flows naturally in under 2 minutes."],
    resources=[
        ("YouTube — Tell Me About Yourself — Developer (TechLead)","https://www.youtube.com/watch?v=I78xhKIxrQE"),
        ("YouTube — Developer Story (Kevin Powell)","https://www.youtube.com/watch?v=bLWXpGFdR8E"),
    ])

    w("what-companies-want","What Do Companies Want?",
    intro="Companies hiring junior developers are not just evaluating your technical skills. They are assessing your ability to learn, your communication, your attitude, and your potential. This lesson covers exactly what they are looking for.",
    overview=["Understand the technical bar for junior developer roles.","Know what 'soft skills' companies actually care about.","Understand the cultural fit evaluation.","Know what red flags to avoid."],
    body="""
<h2 class="lesson-section-title" id="technical-bar">The Technical Bar for Juniors</h2>
<p>Companies hiring juniors do not expect senior-level expertise. They expect:</p>
<ul>
  <li>Solid fundamentals: HTML/CSS, JavaScript, one backend language or framework</li>
  <li>Understanding of version control with Git</li>
  <li>Ability to read and understand existing code</li>
  <li>Problem-solving skills — you can work through a problem systematically even if you do not know the answer immediately</li>
  <li>2–3 portfolio projects that demonstrate you can build real things</li>
</ul>

<h2 class="lesson-section-title" id="soft-skills">What "Soft Skills" Actually Means</h2>
<p>Soft skills is a vague term for real, measurable behaviours:</p>
<ul>
  <li><strong>Communication</strong> — can you explain a technical problem clearly to a non-technical person? Can you ask good questions?</li>
  <li><strong>Coachability</strong> — do you accept feedback graciously and act on it?</li>
  <li><strong>Initiative</strong> — do you proactively look for what needs doing, or only do what you are told?</li>
  <li><strong>Reliability</strong> — do you do what you say you will do, when you say you will do it?</li>
  <li><strong>Curiosity</strong> — do you genuinely enjoy learning new things?</li>
</ul>

<h2 class="lesson-section-title" id="red-flags">Red Flags to Avoid</h2>
<ul>
  <li>Speaking negatively about previous employers or colleagues</li>
  <li>Not being able to explain your own portfolio projects</li>
  <li>Claiming expertise you do not have</li>
  <li>Showing no interest in the company or the role</li>
  <li>Being defensive when given feedback on your code</li>
</ul>""",
    kc=[("What technical skills do companies expect from junior developers?","technical-bar"),
        ("What does 'coachability' mean in a hiring context?","soft-skills"),
        ("What is the biggest red flag in a portfolio presentation?","red-flags")],
    assignments=["For each soft skill listed, write one concrete example from your own experience that demonstrates it.","Prepare for 'Tell me about a challenge you faced and how you overcame it.'"],
    resources=[
        ("YouTube — What Junior Developers Are Expected to Know (Traversy Media)","https://www.youtube.com/watch?v=ysEN5RaKOlA"),
        ("YouTube — Developer Soft Skills (Web Dev Cody)","https://www.youtube.com/watch?v=aw-TfRmDpOY"),
    ])

    w("what-you-can-do","What Can You Do to Prepare?",
    intro="The most effective job search preparation happens before you start applying. This lesson covers the concrete actions that make the biggest difference.",
    overview=["Polish your GitHub profile.","Set up a strong LinkedIn presence.","Write a compelling developer resume.","Prepare your portfolio for review."],
    body="""
<h2 class="lesson-section-title" id="github">GitHub Profile</h2>
<p>Your GitHub is your professional portfolio. Every hiring manager will look at it. Make sure:</p>
<ul>
  <li>Profile photo, name, location, bio, and website are filled in</li>
  <li>Your pinned repositories are your best 6 projects</li>
  <li>Each repository has a descriptive README with screenshots, a live demo link, and setup instructions</li>
  <li>Your contribution graph shows consistent recent activity</li>
  <li>No repositories named "test" or "untitled" are pinned</li>
</ul>

<h2 class="lesson-section-title" id="resume">The Developer Resume</h2>
<p>A developer resume should be one page, ATS-friendly (text-based, no complex tables), and lead with impact:</p>
<ul>
  <li><strong>Header</strong> — name, email, phone, LinkedIn URL, GitHub URL, portfolio URL</li>
  <li><strong>Skills</strong> — list languages, frameworks, and tools. Be honest about proficiency.</li>
  <li><strong>Projects</strong> — 3–4 projects with a brief description and what technologies were used</li>
  <li><strong>Experience</strong> — even non-tech experience showing responsibility and communication</li>
  <li><strong>Education</strong> — at the bottom; self-taught is fine, list relevant courses</li>
</ul>
""" + code("""// Resume project description format:
// [Project name] | [tech stack] | [live link] | [GitHub link]
// - What the project does (user value)
// - What you built specifically
// - Any notable metrics (10,000 users, 99.9% uptime, etc.)

// Example:
// WeatherNow | React, OpenWeather API | [live] | [github]
// - Real-time weather app showing 5-day forecast for any city
// - Implemented custom useFetch hook reducing code duplication by 40%
// - Responsive across all screen sizes with 95+ Lighthouse score
"""),
    kc=[("What must every pinned GitHub repository include?","github"),
        ("What is the correct order of sections on a developer resume?","resume")],
    assignments=["Polish your GitHub profile following all recommendations above.","Write or update your resume using the format described."],
    resources=[
        ("Resume.io — Developer Resume Builder","https://resume.io/"),
        ("YouTube — Developer Resume Tips (Traversy Media)","https://www.youtube.com/watch?v=gKjGh6NTDtA"),
        ("GitHub — Creating a Profile README","https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme"),
    ])

    w("building-your-portfolio","Building Your Portfolio",
    intro="Your portfolio is your most powerful job search tool. This lesson covers what makes a portfolio impressive, how to present your projects, and common portfolio mistakes to avoid.",
    overview=["Know what makes a portfolio project impressive to employers.","Build a personal portfolio website.","Write compelling project case studies.","Include the right projects in the right order."],
    body="""
<h2 class="lesson-section-title" id="impressive-projects">What Makes a Project Impressive</h2>
<p>Employers do not care about todo list number 47. They care about:</p>
<ul>
  <li><strong>Real utility</strong> — does it solve a genuine problem?</li>
  <li><strong>Technical complexity</strong> — does it demonstrate the skills relevant to the role?</li>
  <li><strong>Finish quality</strong> — is it polished? Does it have edge case handling?</li>
  <li><strong>Live demo</strong> — deployed and working on the day of the interview</li>
  <li><strong>Clean code</strong> — readable, organised, commented where necessary</li>
</ul>

<h2 class="lesson-section-title" id="portfolio-site">Your Portfolio Website</h2>
<p>Your portfolio site does not need to be fancy — but it must be fast, mobile-friendly, and tell your story clearly. Essential pages:</p>
<ul>
  <li><strong>Home</strong> — your name, a one-line description, and a call to action</li>
  <li><strong>Projects</strong> — your best 3–4 projects with screenshots, descriptions, and links</li>
  <li><strong>About</strong> — your story, skills, and what you are looking for</li>
  <li><strong>Contact</strong> — email or a contact form</li>
</ul>

<h2 class="lesson-section-title" id="what-to-include">Which Projects to Include</h2>
<p>Quality over quantity. Three great projects beat ten mediocre ones. For each project:</p>
<ul>
  <li>A live deployed version that actually works</li>
  <li>A GitHub repository with a professional README</li>
  <li>A 2–3 sentence description of the problem it solves and how</li>
  <li>A list of the main technologies used</li>
  <li>Screenshots or a demo GIF</li>
</ul>""",
    kc=[("What four qualities make a portfolio project impressive?","impressive-projects"),
        ("What pages must a portfolio website have?","portfolio-site"),
        ("How many projects should a portfolio include?","what-to-include")],
    assignments=["Deploy your portfolio website and share the URL.","Write a project description for each of your three best projects following the format above."],
    resources=[
        ("YouTube — Build a Developer Portfolio (Kevin Powell)","https://www.youtube.com/watch?v=u-RLu_8kwA0"),
        ("YouTube — Best Developer Portfolios (Traversy Media)","https://www.youtube.com/watch?v=GazHne5M3Yg"),
    ])

    w("collecting-leads","Collecting Leads",
    intro="A lead is any company or person that might lead to a job. This lesson covers systematic ways to find high-quality job leads beyond the obvious job boards.",
    overview=["Use LinkedIn effectively to find opportunities.","Leverage your network for referrals.","Use GitHub, Meetups, and Twitter/X to find opportunities.","Set up job alerts to automate discovery."],
    body="""
<h2 class="lesson-section-title" id="linkedin">LinkedIn Strategy</h2>
<ul>
  <li>Complete your profile 100% — LinkedIn ranks incomplete profiles lower</li>
  <li>Use the "Open to Work" feature (visible to recruiters only if you choose)</li>
  <li>Follow and engage with companies you are interested in</li>
  <li>Connect with developers at target companies — a genuine connection opens doors</li>
  <li>Use "Jobs" with filters: entry-level, your tech stack, location/remote</li>
  <li>Set up job alerts for specific searches</li>
</ul>

<h2 class="lesson-section-title" id="beyond-job-boards">Beyond Job Boards</h2>
<ul>
  <li><strong>Hacker News "Who's Hiring"</strong> — monthly thread, often high quality startups</li>
  <li><strong>AngelList / Wellfound</strong> — startup jobs, often junior-friendly</li>
  <li><strong>GitHub Jobs</strong> — companies that are active on GitHub</li>
  <li><strong>Tech Twitter/X</strong> — developers post about open roles regularly</li>
  <li><strong>Local meetups</strong> — attending meetups often leads to referrals before jobs are posted</li>
  <li><strong>Company blogs</strong> — companies hiring often announce it on their engineering blog</li>
</ul>

<h2 class="lesson-section-title" id="networking">Making Networking Feel Natural</h2>
<p>Networking does not mean asking strangers for jobs. It means building genuine relationships with people who do the kind of work you want to do. Attend meetups. Contribute to open source. Help others in communities. Ask for advice, not jobs — people are far more willing to give advice than employment.</p>""",
    kc=[("Name three lead sources beyond job boards.","beyond-job-boards"),
        ("What does successful networking feel like?","networking")],
    assignments=["Set up job alerts on LinkedIn and HackerNews.","Attend one local or virtual tech meetup this month."],
    resources=[
        ("Wellfound (formerly AngelList) — Startup Jobs","https://wellfound.com/jobs"),
        ("Hacker News — Who is Hiring?","https://hn.algolia.com/?q=who+is+hiring"),
        ("YouTube — How to Network as a Developer (Traversy Media)","https://www.youtube.com/watch?v=iP4Kl6Oa7YE"),
    ])

    w("qualifying-leads","Qualifying Leads",
    intro="Not every job posting is worth applying to. Qualifying leads — quickly assessing whether a role is a realistic fit — saves you enormous time and energy.",
    overview=["Evaluate whether a role is a realistic target.","Assess company culture and stability.","Identify green flags and red flags in job postings.","Prioritise your application effort."],
    body="""
<h2 class="lesson-section-title" id="realistic-fit">Is This a Realistic Target?</h2>
<p>Ask honestly:</p>
<ul>
  <li>Do I meet at least 70% of the stated requirements? (Apply if yes — requirements are a wish list, not a checklist)</li>
  <li>Does the tech stack overlap with what I know?</li>
  <li>Is this truly a junior/entry-level role, or is it "junior" with 5 years of experience required?</li>
  <li>Is the company reachable — can I speak to someone there?</li>
</ul>

<h2 class="lesson-section-title" id="green-red-flags">Green Flags and Red Flags</h2>
<p><strong>Green flags:</strong></p>
<ul>
  <li>The posting mentions mentorship, pairing, or growth paths</li>
  <li>The company has positive Glassdoor reviews specifically about engineering culture</li>
  <li>The job description uses realistic, specific language</li>
  <li>You can find happy engineers from this company on LinkedIn</li>
</ul>
<p><strong>Red flags:</strong></p>
<ul>
  <li>"Junior" role requiring 3+ years of experience</li>
  <li>Asks for every trendy technology simultaneously</li>
  <li>Glassdoor mentions poor work-life balance, no mentorship, or high turnover</li>
  <li>Job posting has been up for 6+ months (often means the bar is unrealistically high)</li>
</ul>""",
    kc=[("What percentage of stated requirements do you need to meet before applying?","realistic-fit"),
        ("Name three red flags in a job posting.","green-red-flags")],
    assignments=["Run your top 20 target companies through the qualifying checklist.","Check Glassdoor reviews for your top 5 companies."],
    resources=[
        ("Glassdoor — Company Reviews","https://www.glassdoor.com/"),
        ("YouTube — How to Read Job Descriptions (CS Dojo)","https://www.youtube.com/watch?v=yCPEwzKrGAs"),
    ])

    w("reaching-out","Reaching Out",
    intro="A warm introduction is worth 100 cold applications. This lesson covers how to reach out to developers at target companies, ask for informational interviews, and get referred.",
    overview=["Write effective LinkedIn outreach messages.","Request informational interviews.","Ask for referrals without making it awkward.","Follow up appropriately."],
    body="""
<h2 class="lesson-section-title" id="linkedin-outreach">LinkedIn Outreach</h2>
<p>The goal of initial outreach is not to ask for a job — it is to start a conversation. Keep your first message short, specific, and with a single clear ask:</p>
""" + code("""// Template — connection request note (300 character limit)
"Hi [Name], I've been following [Company]'s engineering blog — the post on
your migration to microservices was fascinating. I'm a junior dev looking to
break in and would love to connect."

// Template — follow-up message after connecting
"Hi [Name], thanks for connecting! I'm genuinely interested in [Company]
— I've used [their product] and love how [specific feature] works. Would you
be open to a 15-minute call to share your experience there? No pressure
if you're busy."
""") + """
<h2 class="lesson-section-title" id="informational-interviews">Informational Interviews</h2>
<p>An informational interview is a short conversation (15–30 minutes) where you ask a developer questions about their role, company, and career path. You are not asking for a job — you are gathering information and building a relationship. Most developers are happy to help someone who is genuinely curious and respectful of their time.</p>

<h2 class="lesson-section-title" id="follow-up">Follow-Up</h2>
<p>Always send a thank-you message within 24 hours of any conversation. Keep your network warm — check in occasionally, share something relevant to their interests, congratulate them on career milestones. Relationships require maintenance.</p>""",
    kc=[("What is the goal of initial outreach to developers?","linkedin-outreach"),
        ("What is an informational interview?","informational-interviews"),
        ("When should you send a follow-up thank-you?","follow-up")],
    assignments=["Send 5 LinkedIn connection requests to developers at target companies with personalised notes.","Request one informational interview this week."],
    resources=[
        ("YouTube — LinkedIn Outreach for Developers (Traversy Media)","https://www.youtube.com/watch?v=iP4Kl6Oa7YE"),
        ("YouTube — Informational Interviews (Harvard Business Review)","https://www.youtube.com/watch?v=vVFY2-PygEE"),
    ])

    w("preparing-for-interviews","Preparing for Interviews",
    intro="Technical interviews are a specific skill that requires specific preparation. This lesson covers how to practise effectively and what to expect at each stage.",
    overview=["Practise technical problems on interview platforms.","Prepare your answers to common behavioural questions.","Know how to talk about your projects under pressure.","Prepare questions to ask the interviewer."],
    body="""
<h2 class="lesson-section-title" id="technical-prep">Technical Preparation</h2>
<p>Practise on the platforms interviewers actually use:</p>
<ul>
  <li><strong>LeetCode</strong> — start with Easy problems. 30 minutes per day builds the habit.</li>
  <li><strong>HackerRank</strong> — many companies use this for screening challenges</li>
  <li><strong>Codewars</strong> — good for building language fluency</li>
</ul>
<p>Focus on: arrays, strings, hash maps, basic sorting, and tree traversal. These cover the majority of junior interview questions.</p>

<h2 class="lesson-section-title" id="behavioural">Behavioural Questions</h2>
<p>Use the STAR format: <strong>S</strong>ituation, <strong>T</strong>ask, <strong>A</strong>ction, <strong>R</strong>esult.</p>
<p>Prepare 3–4 stories that cover: a challenge you overcame, a time you received critical feedback, a time you disagreed with someone, and a time you took initiative.</p>

<h2 class="lesson-section-title" id="questions-to-ask">Questions to Ask the Interviewer</h2>
<p>Always come with questions. "I don't have any questions" signals low interest. Good questions:</p>
<ul>
  <li>What does a typical first week look like for someone in this role?</li>
  <li>How does the team handle code reviews?</li>
  <li>What is the biggest challenge the engineering team is currently facing?</li>
  <li>What do you enjoy most about working here?</li>
  <li>How do you measure success for this role in the first 90 days?</li>
</ul>""",
    kc=[("What is the STAR format for behavioural questions?","behavioural"),
        ("What data structures should junior developers focus on?","technical-prep"),
        ("Why should you always prepare questions to ask the interviewer?","questions-to-ask")],
    assignments=["Solve 3 LeetCode Easy problems in your strongest language.","Write out your answers to the four behavioural scenarios listed above using the STAR format."],
    resources=[
        ("LeetCode","https://leetcode.com/"),
        ("YouTube — How to Prepare for Technical Interviews (TechLead)","https://www.youtube.com/watch?v=qp_PPWRHDGM"),
        ("YouTube — STAR Method for Behavioural Interviews","https://www.youtube.com/watch?v=8QfSnuL8Ny8"),
    ])

    w("the-first-interview","The First Interview",
    intro="The recruiter screen is usually the first live conversation. It is shorter and less technical than later stages, but failing here ends your candidacy. This lesson covers how to ace it.",
    overview=["Know what a recruiter screen covers.","Answer 'Tell me about yourself' in under 2 minutes.","Handle questions about salary and experience gracefully.","Demonstrate genuine interest in the company."],
    body="""
<h2 class="lesson-section-title" id="what-to-expect">What the Recruiter Is Assessing</h2>
<p>Recruiters are not engineers. They are assessing:</p>
<ul>
  <li>Can you communicate clearly?</li>
  <li>Do you seem professional and enthusiastic?</li>
  <li>Do your experience and skills roughly match the role?</li>
  <li>Are your salary expectations in range?</li>
  <li>Would an engineer enjoy talking to you for an hour?</li>
</ul>

<h2 class="lesson-section-title" id="salary">Handling Salary Questions</h2>
<p>Research the market rate for the role in your location before any interview. Use Glassdoor, Levels.fyi, or LinkedIn Salary. When asked about expectations:</p>
""" + code("""// Good response — shows you've done research, gives a range
"Based on my research for similar junior full-stack roles in [city/remote],
I'm targeting something in the $X–$Y range. That said, I'm most interested
in finding the right fit, so I'm open to discussing what the band looks like
for this role."
""") + """
<h2 class="lesson-section-title" id="close-the-interview">Closing the Interview</h2>
<p>Always close with: "What are the next steps and what is the timeline?" This shows you are organised and interested. If they say they will follow up, ask when — and follow up yourself if they miss that date.</p>""",
    kc=[("What are the five things a recruiter is assessing?","what-to-expect"),
        ("How should you respond to a salary question?","salary"),
        ("What should you always ask at the end of a recruiter screen?","close-the-interview")],
    assignments=["Practice saying 'Tell me about yourself' out loud until it sounds natural.","Research market salaries for junior developer roles in your target location."],
    resources=[
        ("Levels.fyi — Tech Salary Data","https://www.levels.fyi/"),
        ("YouTube — Recruiter Phone Screen Tips (TechLead)","https://www.youtube.com/watch?v=bG7Hm2O-MNg"),
    ])

    w("the-technical-interview","The Technical Interview",
    intro="The technical interview is where most candidates are eliminated. This lesson covers the different formats, the thought process that impresses interviewers, and how to recover when you are stuck.",
    overview=["Know the formats: live coding, take-home, pair programming.","Think out loud throughout the interview.","Clarify requirements before coding.","Handle being stuck gracefully."],
    body="""
<h2 class="lesson-section-title" id="formats">Interview Formats</h2>
<ul>
  <li><strong>Live coding</strong> — solve a problem on a shared platform (CoderPad, HackerRank) while the interviewer watches. Most common format.</li>
  <li><strong>Take-home assignment</strong> — build something over 24–72 hours. Treat it like production code: tests, README, clean commits.</li>
  <li><strong>Pair programming</strong> — work on a real codebase task alongside a developer. They observe your process, not just the result.</li>
  <li><strong>Code review</strong> — given buggy or poorly written code, identify issues and suggest improvements.</li>
</ul>

<h2 class="lesson-section-title" id="process">The Live Coding Process</h2>
<ol>
  <li><strong>Clarify</strong> — ask questions before writing anything. What are the input types? Edge cases? Constraints?</li>
  <li><strong>Plan</strong> — explain your approach in plain English before coding. "I'm going to iterate through the array and use a hash map to track..."</li>
  <li><strong>Code</strong> — implement it. Talk through what you are doing as you go.</li>
  <li><strong>Test</strong> — walk through examples by hand. Check edge cases.</li>
  <li><strong>Discuss</strong> — talk about time and space complexity. Suggest optimisations.</li>
</ol>

<h2 class="lesson-section-title" id="when-stuck">When You Get Stuck</h2>
<p>Getting stuck is not automatically a failure. <strong>What you do when stuck matters more than not getting stuck.</strong></p>
<ul>
  <li>"Let me think through this out loud..."</li>
  <li>"I know I can solve this with a brute force approach first and then optimise..."</li>
  <li>"I'm not sure about [specific part] — could I ask a clarifying question?"</li>
</ul>""",
    kc=[("What are the four technical interview formats?","formats"),
        ("What five steps should you follow in a live coding interview?","process"),
        ("What should you do when you get stuck?","when-stuck")],
    assignments=["Do one timed LeetCode problem today without looking at hints first.","Practice the five-step process on a problem, narrating each step out loud."],
    resources=[
        ("LeetCode","https://leetcode.com/"),
        ("YouTube — How to Solve Coding Interview Problems (CS Dojo)","https://www.youtube.com/watch?v=GBuHSRDGZBY"),
        ("YouTube — Live Coding Interview Tips (TechLead)","https://www.youtube.com/watch?v=q_fhvGNClCo"),
    ])

    w("after-the-interview","After the Interview",
    intro="What you do after the interview affects your outcome more than most people realise. This lesson covers follow-up, evaluating companies during the process, and handling rejection constructively.",
    overview=["Send a thank-you email within 24 hours.","Evaluate companies as they evaluate you.","Handle rejection professionally.","Keep your pipeline full throughout the process."],
    body="""
<h2 class="lesson-section-title" id="thank-you">The Thank-You Email</h2>
<p>Send a brief thank-you email within 24 hours of any interview. It reinforces your interest and keeps you top-of-mind. Keep it short:</p>
""" + code("""Subject: Thank you — [Your Name] / [Role]

Hi [Name],

Thank you for taking the time to speak with me today. I really enjoyed
learning about [specific thing discussed] — it confirmed my interest in
the role and the team.

I'm excited about the possibility of contributing to [specific project
or challenge they mentioned].

Looking forward to next steps!

[Your name]
""") + """
<h2 class="lesson-section-title" id="evaluating-companies">Evaluating Companies</h2>
<p>You are interviewing them as much as they are interviewing you. Red flags during the interview process:</p>
<ul>
  <li>Disorganised process — interviews rescheduled multiple times</li>
  <li>Disrespect for your time — interviews running 30+ minutes over without acknowledgement</li>
  <li>Inconsistent information — different people tell you different things about the role</li>
  <li>No clear answer to "What does success look like in 90 days?"</li>
  <li>Dismissive or condescending interviewers</li>
</ul>

<h2 class="lesson-section-title" id="rejection">Handling Rejection</h2>
<p>You will be rejected. Many times. Rejection is not a verdict on your worth — it is information about fit, timing, and circumstances that are mostly outside your control. The right response:</p>
<ul>
  <li>Thank the recruiter and ask for feedback (rarely given, occasionally valuable)</li>
  <li>Reflect briefly on what you could improve</li>
  <li>Keep your pipeline full so no single rejection derails you</li>
  <li>Give yourself 24 hours to feel disappointed, then move on</li>
</ul>""",
    kc=[("What should a thank-you email include?","thank-you"),
        ("Name three red flags during the interview process.","evaluating-companies"),
        ("What is the productive response to receiving a rejection?","rejection")],
    assignments=["Write a template thank-you email you can customise after each interview.","If you have been rejected recently, send a professional thank-you and request for feedback."],
    resources=[
        ("YouTube — Thank You Email After Interview","https://www.youtube.com/watch?v=NN8k6hH6vI0"),
        ("YouTube — How to Handle Rejection (CS Dojo)","https://www.youtube.com/watch?v=yCPEwzKrGAs"),
    ])

    w("handling-offers-and-negotiations","Handling Offers and Negotiations",
    intro="Receiving a job offer is exciting — and the moment many people make costly mistakes by accepting immediately or negotiating poorly. This lesson gives you the knowledge to evaluate and negotiate confidently.",
    overview=["Know how to evaluate a complete compensation package.","Understand that negotiation is expected and professional.","Use the right language to negotiate without risking the offer.","Evaluate equity and benefits alongside base salary."],
    body="""
<h2 class="lesson-section-title" id="evaluating-offer">Evaluating the Full Package</h2>
<p>Salary is only one component. Evaluate the complete package:</p>
<ul>
  <li><strong>Base salary</strong> — compare to market rate (Glassdoor, Levels.fyi, LinkedIn Salary)</li>
  <li><strong>Equity</strong> — stock options or RSUs; understand the vesting schedule and cliff</li>
  <li><strong>Bonus</strong> — signing bonus and annual performance bonus</li>
  <li><strong>Benefits</strong> — health insurance (value this: a good plan is worth $5–15k/year), dental, vision, 401k match</li>
  <li><strong>Remote/hybrid</strong> — commuting costs and time are real compensation components</li>
  <li><strong>PTO and culture</strong> — unlimited PTO that is never used is worth less than 15 days that is encouraged</li>
  <li><strong>Growth</strong> — will you learn and advance here?</li>
</ul>

<h2 class="lesson-section-title" id="negotiation">Negotiating Professionally</h2>
<p>Negotiation is expected — offers are not final until you have negotiated. A professional negotiation never risks the offer. Use this language:</p>
""" + code("""// Express enthusiasm first — always
"Thank you so much for the offer. I'm genuinely excited about this opportunity
and the team. I'd like to take a day to review the full package."

// Counter-offer — specific, based on research
"Based on my research for this type of role in [location] and considering my
[specific skills/experience], I was hoping we could get to [specific number].
Is there any flexibility there?"

// If they cannot move on salary
"I understand. Is there flexibility on [signing bonus / extra PTO / remote days]?"

// After negotiating
"Thank you — I'm happy to accept. I'm looking forward to getting started."
"""),
    kc=[("What components make up a total compensation package?","evaluating-offer"),
        ("Does negotiating risk the offer?","negotiation"),
        ("What should you always say before making a counter-offer?","negotiation")],
    assignments=["Research the market salary for your target role at target companies using Glassdoor and Levels.fyi.","Practice the negotiation script above with a friend or in the mirror."],
    resources=[
        ("Levels.fyi — Tech Compensation Data","https://www.levels.fyi/"),
        ("YouTube — How to Negotiate a Job Offer (TechLead)","https://www.youtube.com/watch?v=v4BpF4hlANs"),
        ("Glassdoor — Know Your Worth Salary Calculator","https://www.glassdoor.com/salaries/index.htm"),
    ])

    print(f"  Getting Hired: {len(ALL)} lessons done")


# ════════════════════════════════════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════════════════════════════════════
def main():
    seed_advanced_html_css()
    seed_react()
    seed_nodejs()
    seed_getting_hired()

    print("\nAll 73 lessons seeded. Committing to GitHub...")
    os.chdir(BASE)
    subprocess.run(["git","add","-A"], check=True)
    subprocess.run(["git","commit","-m",
        "Seed: Advanced HTML/CSS, React, NodeJS, Getting Hired — all 73 lessons"], check=True)
    subprocess.run(["git","push"], check=True)
    print("Pushed to GitHub. Full Stack JavaScript path complete.")

if __name__ == "__main__":
    main()
