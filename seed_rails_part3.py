#!/usr/bin/env python3
"""Rails Path — Part 3: Intermediate HTML/CSS (31) + Advanced HTML/CSS (13) + Getting Hired (15)"""
import os, subprocess

BASE  = os.path.expanduser("~/devpath")
RAILS = os.path.join(BASE, "paths", "full-stack-ruby-on-rails", "courses")
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
    esc = s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f'<div class="code-block"><pre><code>{esc}</code></pre></div>'

def write(ldir, course_title, course_path_name, all_lessons, sidebar_html, slug,
          title, intro, overview, body, kc, assignments, resources):
    idx = next((i for i,l in enumerate(all_lessons) if l[0]==slug), None)
    p   = (all_lessons[idx-1][1], all_lessons[idx-1][0]+".html") if idx and idx>0 else None
    n   = (all_lessons[idx+1][1], all_lessons[idx+1][0]+".html") if idx is not None and idx<len(all_lessons)-1 else None
    pb  = f'<a href="{p[1]}" class="btn btn-blue-outline">&#8592; Previous</a>' if p else '<span></span>'
    nb  = f'<a href="{n[1]}" class="btn btn-blue">Next &#8594;</a>' if n else '<span></span>'
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
    ph   = f'<a href="{p[1]}" class="pagination-link prev"><span class="pagination-label">&#8592; Previous</span><span class="pagination-title">{p[0]}</span></a>' if p else "<span></span>"
    nh   = f'<a href="{n[1]}" class="pagination-link next"><span class="pagination-label">Next &#8594;</span><span class="pagination-title">{n[0]}</span></a>' if n else "<span></span>"
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


# Helper to build a shared CSS/HTML sidebar
def css_html_sidebar(course_title, lessons_by_section):
    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'
    s = f'<aside class="sidebar"><div class="sidebar-course-title">{course_title}</div>'
    for label, items in lessons_by_section:
        s += f'<div class="sidebar-section"><div class="sidebar-section-label">{label}</div>'
        for sl, ti, proj in items:
            s += lnk(sl, ti, proj)
        s += '</div>'
    s += '</aside>'
    return s


# ══════════════════════════════════════════════════════
# INTERMEDIATE HTML AND CSS (Rails path — same content,
# different breadcrumb/sidebar context)
# ══════════════════════════════════════════════════════
def seed_intermediate_html_css():
    ldir = os.path.join(RAILS, "intermediate-html-css", "lessons")

    ALL = [
        ("int-intro",                          "Introduction"),
        ("emmet",                              "Emmet"),
        ("svg",                                "SVG"),
        ("tables",                             "Tables"),
        ("default-styles",                     "Default Styles"),
        ("css-units",                          "CSS Units"),
        ("more-text-styles",                   "More Text Styles"),
        ("more-css-properties",                "More CSS Properties"),
        ("advanced-selectors",                 "Advanced Selectors"),
        ("positioning",                        "Positioning"),
        ("css-functions",                      "CSS Functions"),
        ("custom-properties",                  "Custom Properties"),
        ("browser-compatibility",              "Browser Compatibility"),
        ("form-basics",                        "Form Basics"),
        ("form-validation",                    "Form Validation"),
        ("project-sign-up-form",               "Project: Sign-Up Form"),
        ("introduction-to-grid",               "Introduction to Grid"),
        ("creating-a-grid",                    "Creating a Grid"),
        ("positioning-grid-elements",          "Positioning Grid Elements"),
        ("advanced-grid-properties",           "Advanced Grid Properties"),
        ("using-flexbox-and-grid",             "Using Flexbox and Grid"),
        ("project-admin-dashboard",            "Project: Admin Dashboard"),
        ("intro-to-accessibility",             "Introduction to Web Accessibility"),
        ("wcag",                               "The Web Content Accessibility Guidelines"),
        ("accessible-colors",                  "Accessible Colors"),
        ("keyboard-navigation",                "Keyboard Navigation"),
        ("meaningful-text",                    "Meaningful Text"),
        ("wai-aria",                           "WAI-ARIA"),
        ("intro-to-responsive-design",         "Introduction to Responsive Design"),
        ("natural-responsiveness",             "Natural Responsiveness"),
        ("responsive-images",                  "Responsive Images"),
        ("media-queries",                      "Media Queries"),
        ("project-homepage",                   "Project: Homepage"),
    ]

    sections = [
        ("Introduction",   [("int-intro","Introduction",False)]),
        ("Intermediate HTML",[("emmet","Emmet",False),("svg","SVG",False),("tables","Tables",False)]),
        ("Intermediate CSS",[
            ("default-styles","Default Styles",False),("css-units","CSS Units",False),
            ("more-text-styles","More Text Styles",False),("more-css-properties","More CSS Properties",False),
            ("advanced-selectors","Advanced Selectors",False),("positioning","Positioning",False),
            ("css-functions","CSS Functions",False),("custom-properties","Custom Properties",False),
            ("browser-compatibility","Browser Compatibility",False),
        ]),
        ("Forms",[
            ("form-basics","Form Basics",False),("form-validation","Form Validation",False),
            ("project-sign-up-form","Project: Sign-Up Form",True),
        ]),
        ("Grid",[
            ("introduction-to-grid","Introduction to Grid",False),("creating-a-grid","Creating a Grid",False),
            ("positioning-grid-elements","Positioning Grid Elements",False),
            ("advanced-grid-properties","Advanced Grid Properties",False),
            ("using-flexbox-and-grid","Using Flexbox and Grid",False),
            ("project-admin-dashboard","Project: Admin Dashboard",True),
        ]),
        ("Accessibility",[
            ("intro-to-accessibility","Introduction to Accessibility",False),
            ("wcag","WCAG",False),("accessible-colors","Accessible Colors",False),
            ("keyboard-navigation","Keyboard Navigation",False),
            ("meaningful-text","Meaningful Text",False),("wai-aria","WAI-ARIA",False),
        ]),
        ("Responsive Design",[
            ("intro-to-responsive-design","Introduction to Responsive Design",False),
            ("natural-responsiveness","Natural Responsiveness",False),
            ("responsive-images","Responsive Images",False),
            ("media-queries","Media Queries",False),
            ("project-homepage","Project: Homepage",True),
        ]),
    ]

    sidebar = css_html_sidebar("Intermediate HTML and CSS", sections)

    # Lesson content — same topics as the JS path version, shared knowledge
    SHARED = {
        "int-intro": ("Introduction",
            "This course deepens your HTML and CSS knowledge — the same skills apply whether you are building JavaScript or Rails frontends. Every lesson here directly supports your Rails views.",
            ["Understand what this course covers.","Know the order of topics and how they build."]),
        "emmet": ("Emmet",
            "Emmet expands abbreviations into full HTML instantly in VS Code — a major productivity boost for writing Rails ERB templates.",
            ["Use Emmet abbreviations for HTML structure.","Chain, nest, and multiply elements.","Use Emmet inside .erb files."]),
        "svg": ("SVG",
            "SVG graphics are resolution-independent and can be embedded directly in Rails ERB templates or used as asset files.",
            ["Understand what SVG is and its advantages.","Embed SVG in ERB templates.","Style SVG with CSS."]),
        "tables": ("Tables",
            "HTML tables display tabular data. Rails developers frequently generate tables from ActiveRecord collections.",
            ["Build accessible HTML tables.","Use colspan and rowspan.","Render ActiveRecord collections as tables in ERB."]),
        "default-styles": ("Default Styles",
            "Browser default styles affect every Rails view. A CSS reset prevents cross-browser inconsistencies.",
            ["Understand user agent stylesheets.","Apply a modern CSS reset.","Know the difference between reset and normalise."]),
        "css-units": ("CSS Units",
            "Choosing the right CSS unit — rem, em, px, vw, vh — directly affects how responsive your Rails views are.",
            ["Use relative units for accessible, responsive layouts.","Know when to use each unit type.","Apply rem for font sizes and spacing."]),
        "more-text-styles": ("More Text Styles",
            "Typography is a core part of every Rails view. This lesson covers font properties, web fonts, and text effects.",
            ["Control fonts with font-family, weight, and line-height.","Load Google Fonts in a Rails layout.","Apply letter-spacing and text-transform."]),
        "more-css-properties": ("More CSS Properties",
            "Overflow, opacity, filters, z-index — properties that appear constantly in real Rails applications.",
            ["Control overflow behaviour.","Use opacity and visibility.","Apply CSS filters and cursor styles."]),
        "advanced-selectors": ("Advanced Selectors",
            "Advanced selectors let you target elements precisely in complex Rails views without adding extra classes.",
            ["Use combinators and pseudo-classes.","Use pseudo-elements ::before and ::after.","Use attribute selectors."]),
        "positioning": ("Positioning",
            "CSS positioning is essential for tooltips, modals, sticky headers, and overlays in Rails views.",
            ["Use static, relative, absolute, fixed, and sticky positioning.","Understand the containing block.","Use z-index correctly."]),
        "css-functions": ("CSS Functions",
            "calc(), clamp(), min(), and max() create fluid, responsive layouts without media queries.",
            ["Use calc() for dynamic calculations.","Use clamp() for fluid typography.","Use CSS color functions."]),
        "custom-properties": ("Custom Properties",
            "CSS custom properties are the foundation of themeable Rails applications with dark mode support.",
            ["Declare and consume CSS custom properties.","Build a design token system.","Implement dark mode with @media and class toggle."]),
        "browser-compatibility": ("Browser Compatibility",
            "Rails views must work across all modern browsers. This lesson covers @supports, vendor prefixes, and testing strategies.",
            ["Use caniuse.com to check feature support.","Write @supports queries.","Understand progressive enhancement."]),
        "form-basics": ("Form Basics",
            "HTML forms are the foundation of Rails form helpers. Understanding native form elements makes using form_with much more effective.",
            ["Build forms with input types, labels, and fieldsets.","Understand form accessibility requirements.","Connect HTML forms to the HTML5 constraint validation API."]),
        "form-validation": ("Form Validation",
            "HTML5 validation and CSS :valid/:invalid states work alongside Rails model validations for a layered approach.",
            ["Use HTML5 validation attributes.","Style valid and invalid states with CSS pseudo-classes.","Understand when to use client vs server validation."]),
        "project-sign-up-form": ("Project: Sign-Up Form",
            "Build a polished, accessible, validated sign-up form in plain HTML and CSS — before connecting it to a Rails backend.",
            ["Build a complete multi-field sign-up form.","Apply custom CSS validation styles.","Ensure full keyboard accessibility."]),
        "introduction-to-grid": ("Introduction to Grid",
            "CSS Grid handles two-dimensional layout. It pairs perfectly with Rails partial-based component architecture.",
            ["Activate CSS Grid and define columns.","Use the fr unit.","Understand auto-placement."]),
        "creating-a-grid": ("Creating a Grid",
            "Implicit vs explicit grids, auto-fill and auto-fit — patterns for responsive Rails view layouts.",
            ["Understand explicit and implicit grids.","Use minmax() for flexible tracks.","Use auto-fit for responsive grids."]),
        "positioning-grid-elements": ("Positioning Grid Elements",
            "Manually place grid items to create complex layouts for Rails dashboards and admin interfaces.",
            ["Use grid-column and grid-row for placement.","Use grid-template-areas.","Layer items in grid cells."]),
        "advanced-grid-properties": ("Advanced Grid Properties",
            "Grid alignment, layering, and ordering — advanced techniques for polished Rails views.",
            ["Align items and tracks.","Layer overlapping grid items.","Use the order property."]),
        "using-flexbox-and-grid": ("Using Flexbox and Grid",
            "The best Rails views use Grid for page structure and Flexbox for components inside each section.",
            ["Know when to choose Grid vs Flexbox.","Combine both in a single layout.","Implement the Holy Grail layout."]),
        "project-admin-dashboard": ("Project: Admin Dashboard",
            "Build a full admin dashboard UI — the kind you will eventually connect to a Rails backend.",
            ["Build a complete admin layout with Grid.","Create responsive stats cards and data tables.","Make it fully responsive."]),
        "intro-to-accessibility": ("Introduction to Web Accessibility",
            "Accessibility is a legal requirement in many countries and a core quality of professional Rails applications.",
            ["Understand what accessibility means.","Know the major categories of disability.","Understand WCAG conformance levels."]),
        "wcag": ("The Web Content Accessibility Guidelines",
            "WCAG defines the standards every Rails application should meet.",
            ["Understand the four POUR principles.","Know key AA-level success criteria.","Use automated testing tools."]),
        "accessible-colors": ("Accessible Colors",
            "Colour contrast failures are the most common accessibility issue. Every Rails stylesheet should be checked.",
            ["Understand contrast ratio requirements.","Use contrast checking tools.","Design colour-blind-safe interfaces."]),
        "keyboard-navigation": ("Keyboard Navigation",
            "Rails forms and interactive elements must be keyboard-accessible. This lesson covers focus management and skip links.",
            ["Understand how keyboard navigation works.","Implement visible focus styles.","Add skip links to Rails layouts."]),
        "meaningful-text": ("Meaningful Text",
            "Link text, button labels, and alt text in Rails views must communicate clearly without visual context.",
            ["Write descriptive link text.","Label buttons accessibly.","Use the visually-hidden pattern."]),
        "wai-aria": ("WAI-ARIA",
            "Rails Stimulus controllers and Turbo-driven interfaces require ARIA attributes to communicate state changes to assistive technology.",
            ["Know when to use ARIA.","Apply ARIA roles and states.","Follow the first rule of ARIA."]),
        "intro-to-responsive-design": ("Introduction to Responsive Design",
            "Every Rails application must work on mobile. This lesson introduces the philosophy and core techniques.",
            ["Understand the three pillars of responsive design.","Know the mobile-first approach.","Understand responsive vs adaptive."]),
        "natural-responsiveness": ("Natural Responsiveness",
            "Many Rails layouts become responsive naturally using relative units and modern CSS without media queries.",
            ["Use clamp() for fluid typography.","Use auto-fit for responsive grids.","Avoid fixed widths."]),
        "responsive-images": ("Responsive Images",
            "Images are the heaviest assets in Rails views. srcset and the picture element serve the right size for every device.",
            ["Use srcset for resolution switching.","Use the sizes attribute.","Use picture for art direction."]),
        "media-queries": ("Media Queries",
            "Media queries let Rails stylesheets adapt to viewport size, user preferences, and device capabilities.",
            ["Write mobile-first min-width queries.","Use prefers-color-scheme and prefers-reduced-motion.","Understand container queries."]),
        "project-homepage": ("Project: Homepage",
            "Build a complete responsive homepage — the same kind you will later power with Rails data.",
            ["Build a full responsive homepage using Grid and Flexbox.","Apply accessibility and responsive design principles.","Achieve 90+ Lighthouse scores."]),
    }

    def w(slug):
        title, intro, ov = SHARED[slug]
        body = f"""
<h2 class="lesson-section-title" id="overview">About This Lesson</h2>
<p>This lesson covers the same material as the identical lesson in the Full Stack JavaScript path. The concepts are exactly the same — HTML and CSS are not language-specific. The only difference is context: you will apply these skills in Ruby on Rails ERB templates rather than React components.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>If you completed the Full Stack JavaScript path first, this is a review. Focus on how these techniques apply inside ERB templates and Rails layouts.</p>
</div>
<h2 class="lesson-section-title" id="rails-context">Rails Context</h2>
<p>In Rails, all CSS and HTML knowledge applies directly. Your stylesheets live in <code>app/assets/stylesheets/</code> or are managed by Tailwind/cssbundling. Your HTML lives in ERB templates in <code>app/views/</code>. Everything you learn in this lesson is used daily in Rails development.</p>
"""
        write(ldir, "Intermediate HTML and CSS", "intermediate-html-css",
              ALL, sidebar, slug, title, intro, ov, body,
              [(f"How does {title} apply to Rails ERB templates?","rails-context"),
               (f"What is the most important concept in {title}?","overview")],
              [f"Complete the {title} exercises.",
               "Apply this technique to one of your Rails views."],
              [("MDN Web Docs","https://developer.mozilla.org/en-US/"),
               ("CSS Tricks","https://css-tricks.com/"),
               ("YouTube — Kevin Powell CSS Channel","https://www.youtube.com/@KevinPowell")])

    for slug, _ in ALL:
        w(slug)

    print(f"  Intermediate HTML/CSS (Rails): {len(ALL)} lessons done")


# ══════════════════════════════════════════════════════
# ADVANCED HTML AND CSS (Rails path)
# ══════════════════════════════════════════════════════
def seed_advanced_html_css():
    ldir = os.path.join(RAILS, "advanced-html-css", "lessons")

    ALL = [
        ("transforms",          "Transforms"),
        ("transitions",         "Transitions"),
        ("keyframes",           "Keyframes"),
        ("accessibility-adv",   "Introduction to Accessibility"),
        ("wcag-adv",            "The Web Content Accessibility Guidelines"),
        ("accessible-colors-adv","Accessible Colors"),
        ("keyboard-nav-adv",    "Keyboard Navigation"),
        ("meaningful-text-adv", "Meaningful Text"),
        ("wai-aria-adv",        "WAI-ARIA"),
        ("natural-resp-adv",    "Natural Responsiveness"),
        ("responsive-images-adv","Responsive Images"),
        ("media-queries-adv",   "Media Queries"),
        ("project-homepage-adv","Project: Homepage"),
    ]

    sections = [
        ("Animation", [("transforms","Transforms",False),("transitions","Transitions",False),("keyframes","Keyframes",False)]),
        ("Accessibility", [
            ("accessibility-adv","Introduction to Accessibility",False),
            ("wcag-adv","WCAG",False),("accessible-colors-adv","Accessible Colors",False),
            ("keyboard-nav-adv","Keyboard Navigation",False),
            ("meaningful-text-adv","Meaningful Text",False),("wai-aria-adv","WAI-ARIA",False),
        ]),
        ("Responsive Design", [
            ("natural-resp-adv","Natural Responsiveness",False),
            ("responsive-images-adv","Responsive Images",False),
            ("media-queries-adv","Media Queries",False),
            ("project-homepage-adv","Project: Homepage",True),
        ]),
    ]
    sidebar = css_html_sidebar("Advanced HTML and CSS", sections)

    CONTENT = {
        "transforms": ("Transforms",
            "CSS transforms let you move, rotate, scale, and skew elements without affecting document flow — essential for polished Rails UI interactions.",
            ["Use 2D and 3D CSS transforms.","Chain transforms.","Control pivot with transform-origin."]),
        "transitions": ("Transitions",
            "CSS transitions animate property changes smoothly — on hover, focus, or class toggling from Rails Stimulus controllers.",
            ["Write transition declarations.","Choose appropriate easing functions.","Know which properties animate performantly."]),
        "keyframes": ("Keyframes",
            "CSS animations with @keyframes create multi-step animations — page loaders, attention effects, entrance animations.",
            ["Define animations with @keyframes.","Apply animations with the animation property.","Respect prefers-reduced-motion."]),
    }

    for slug, title in ALL:
        if slug in CONTENT:
            title, intro, ov = CONTENT[slug]
            body = f"""
<h2 class="lesson-section-title" id="overview">{title} in Rails</h2>
<p>This lesson covers {title} as it applies to Ruby on Rails applications — specifically how to use these techniques in ERB templates, Rails Stimulus controllers, and Tailwind CSS.</p>
""" + code("""# In a Rails view — add animation classes with Stimulus
# app/javascript/controllers/animate_controller.js
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  connect() {
    this.element.classList.add('fade-in')
  }
}
""")
        else:
            intro = f"This lesson covers {title} in the context of advanced Rails front-end development — animations, accessibility, and responsive design."
            ov = [f"Apply {title} in Rails ERB templates.","Use with Stimulus and Turbo for dynamic effects."]
            body = f"""
<h2 class="lesson-section-title" id="overview">{title} in Rails</h2>
<p>The same CSS and HTML concepts from the Full Stack JavaScript path apply here. Rails uses ERB templates but the front-end layer is identical. Focus on how to apply these techniques in a server-rendered context.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Rails 7 with Turbo and Stimulus gives you reactive front-end behaviour without writing a full JavaScript framework. These CSS techniques work seamlessly with that stack.</p>
</div>
"""
        write(ldir, "Advanced HTML and CSS", "advanced-html-css",
              ALL, sidebar, slug, title, intro, ov, body,
              [(f"How does {title} integrate with Rails Turbo/Stimulus?","overview")],
              [f"Apply {title} techniques to your Rails portfolio project.",
               "Ensure all animations respect prefers-reduced-motion."],
              [("MDN — CSS Reference","https://developer.mozilla.org/en-US/docs/Web/CSS"),
               ("Hotwire (Turbo + Stimulus)","https://hotwired.dev/"),
               ("YouTube — Kevin Powell","https://www.youtube.com/@KevinPowell")])

    print(f"  Advanced HTML/CSS (Rails): {len(ALL)} lessons done")


# ══════════════════════════════════════════════════════
# GETTING HIRED (Rails path — identical to JS path)
# ══════════════════════════════════════════════════════
def seed_getting_hired():
    ldir = os.path.join(RAILS, "getting-hired", "lessons")

    ALL = [
        ("introduction",              "Introduction to Getting Hired"),
        ("how-to-get-hired",          "How to Get Hired as a Web Developer"),
        ("strategy",                  "Strategy"),
        ("it-starts-with-you",        "It Starts with You"),
        ("what-companies-want",       "What Do Companies Want?"),
        ("what-you-can-do",           "What Can You Do to Prepare?"),
        ("building-your-portfolio",   "Building Your Portfolio"),
        ("collecting-leads",          "Collecting Leads"),
        ("qualifying-leads",          "Qualifying Leads"),
        ("reaching-out",              "Reaching Out"),
        ("preparing-for-interviews",  "Preparing for Interviews"),
        ("the-first-interview",       "The First Interview"),
        ("the-technical-interview",   "The Technical Interview"),
        ("after-the-interview",       "After the Interview"),
        ("handling-offers",           "Handling Offers and Negotiations"),
    ]

    def lnk(sl, ti):
        return f'<a href="{sl}.html" class="sidebar-link">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">Getting Hired</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">Preparing</div>'
        + lnk("introduction","Introduction")
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
        + lnk("handling-offers","Offers and Negotiations")
        + '</div></aside>'
    )

    CONTENT = {
        "introduction": ("Introduction to Getting Hired",
            "You have spent months building real Rails skills. Now translate them into your first developer job. This course covers every step.",
            ["Understand the job search process for Rails developers.","Know how to position your Rails skills.","Set realistic timeline expectations."]),
        "how-to-get-hired": ("How to Get Hired as a Web Developer",
            "Understanding how companies hire Rails developers gives you a significant advantage. The Rails ecosystem is smaller and more community-driven than the JS ecosystem.",
            ["Understand how Rails companies hire.","Know which companies use Rails.","Understand the Rails job market."]),
        "strategy": ("Strategy",
            "A targeted job search focusing on Rails companies is far more effective than applying everywhere.",
            ["Build a targeted Rails company list.","Use a job search tracker.","Set daily job search targets."]),
        "it-starts-with-you": ("It Starts with You",
            "Knowing what kind of Rails developer you want to be — API-only, full-stack, frontend-heavy — sharpens every application you send.",
            ["Define your target Rails role.","Craft your developer story highlighting Ruby/Rails.","Identify your genuine strengths."]),
        "what-companies-want": ("What Do Companies Want?",
            "Rails companies hiring juniors value Ruby fundamentals, Rails conventions, and strong CS problem-solving.",
            ["Know the Rails technical bar for juniors.","Understand soft skills in Rails team culture.","Know Rails-specific red flags."]),
        "what-you-can-do": ("What Can You Do to Prepare?",
            "Polish your GitHub with Rails projects, set up a strong LinkedIn, and craft a resume that highlights your Ruby/Rails experience.",
            ["Polish your GitHub profile with Rails projects.","Write a Rails-focused resume.","Set up LinkedIn for Rails opportunities."]),
        "building-your-portfolio": ("Building Your Portfolio",
            "Your portfolio for Rails jobs should include deployed Rails applications, not just frontend projects.",
            ["Include deployed Rails applications.","Write compelling Rails project descriptions.","Build a Rails-powered portfolio site."]),
        "collecting-leads": ("Collecting Leads",
            "Rails jobs are often found through community channels — RubyConf, regional Ruby groups, and Rails-specific job boards.",
            ["Use Ruby/Rails specific job boards.","Leverage the Ruby community.","Set up targeted job alerts."]),
        "qualifying-leads": ("Qualifying Leads",
            "Evaluate Rails job postings critically — version of Rails, team size, testing culture, and deployment practices matter.",
            ["Evaluate Rails job postings.","Check a company's tech stack.","Identify Rails-specific green and red flags."]),
        "reaching-out": ("Reaching Out",
            "The Ruby community is welcoming. Attend meetups, contribute to gems, and engage on Ruby forums to build genuine connections.",
            ["Connect with Rails developers on LinkedIn.","Attend Ruby/Rails meetups.","Ask for informational interviews."]),
        "preparing-for-interviews": ("Preparing for Interviews",
            "Rails technical interviews combine Ruby fundamentals, Rails-specific knowledge, and general web development understanding.",
            ["Practise Ruby algorithms on LeetCode/HackerRank.","Know Rails interview topics: ActiveRecord, routing, MVC.","Prepare your Rails project walkthroughs."]),
        "the-first-interview": ("The First Interview",
            "Recruiter screens for Rails roles focus on Ruby experience, familiarity with Rails conventions, and communication skills.",
            ["Handle Rails recruiter screens.","Answer salary questions for Rails roles.","Demonstrate Rails knowledge concisely."]),
        "the-technical-interview": ("The Technical Interview",
            "Rails technical interviews often involve live coding in Ruby, code review of Rails code, and architectural questions.",
            ["Prepare for Ruby live coding challenges.","Handle Rails code review exercises.","Answer Rails architecture questions."]),
        "after-the-interview": ("After the Interview",
            "Follow up professionally, evaluate the company's Rails codebase maturity, and handle rejection constructively.",
            ["Send thank-you emails after Rails interviews.","Evaluate a company's Rails tech decisions.","Handle rejection and keep your pipeline full."]),
        "handling-offers": ("Handling Offers and Negotiations",
            "Rails developer compensation varies by company size and location. Research Rails-specific salary data before negotiating.",
            ["Research Rails developer salaries.","Evaluate Rails-specific compensation components.","Negotiate professionally."]),
    }

    for slug, _ in ALL:
        if slug in CONTENT:
            title, intro, ov = CONTENT[slug]
        else:
            title = next(t for s,t in ALL if s==slug)
            intro = f"This lesson covers {title} for developers seeking Ruby on Rails positions."
            ov = [f"Apply {title} strategies to your Rails job search.",
                  "Leverage the Ruby community for opportunities."]
        body = f"""
<h2 class="lesson-section-title" id="overview">Rails Job Search Context</h2>
<p>The job search advice in this lesson applies universally, with a Ruby on Rails focus. The Rails job market is smaller than the JavaScript ecosystem but tends to be more community-driven — local Ruby groups, RailsConf, and RubyConf are particularly valuable.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Rails companies tend to value pragmatism, convention, and solid Ruby knowledge over framework-hopping. Emphasise your understanding of Rails conventions, testing practices, and database design.</p>
</div>
<h2 class="lesson-section-title" id="rails-specific">Rails-Specific Advice</h2>
<ul>
  <li>Know your Rails version — Rails 7 Hotwire/Turbo is the current standard</li>
  <li>Understand the difference between Rails as API vs full-stack</li>
  <li>Be comfortable with RSpec and Minitest — Rails teams care about testing</li>
  <li>Know ActiveRecord well — it comes up in almost every Rails interview</li>
  <li>Join the Ruby community: Ruby on Rails Link Slack, local Ruby groups</li>
</ul>
"""
        write(ldir, "Getting Hired", "getting-hired",
              ALL, sidebar, slug, title, intro, ov, body,
              [(f"How does {title} differ for Rails vs JavaScript jobs?","rails-specific"),
               ("What Rails community resources help with job searching?","overview")],
              [f"Complete the {title} action items for your Rails job search.",
               "Join the Ruby on Rails Link Slack community."],
              [("Ruby on Rails Link Slack","https://www.rubyonrails.link/"),
               ("RubyConf — Conference for Ruby developers","https://rubyconf.org/"),
               ("Levels.fyi — Tech Salary Data","https://www.levels.fyi/")])

    print(f"  Getting Hired (Rails): {len(ALL)} lessons done")


def main():
    seed_intermediate_html_css()
    seed_advanced_html_css()
    seed_getting_hired()
    print("\nPart 3 complete. Committing...")
    os.chdir(BASE)
    subprocess.run(["git","add","-A"], check=True)
    subprocess.run(["git","commit","-m","Seed Rails path Part 3: Intermediate HTML/CSS + Advanced HTML/CSS + Getting Hired"], check=True)
    subprocess.run(["git","push"], check=True)
    print("Pushed. Full Stack Ruby on Rails path complete.")

if __name__ == "__main__":
    main()
