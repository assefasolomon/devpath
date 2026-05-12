#!/usr/bin/env python3
"""Rails Path — Part 2: Ruby on Rails course (24 lessons)"""
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

def write(ldir, course_title, all_lessons, sidebar_html, slug,
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


def seed_ruby_on_rails():
    ldir = os.path.join(RAILS, "ruby-on-rails", "lessons")
    os.makedirs(ldir, exist_ok=True)   # ← FIXED: Ensure directory exists

    ALL = [
        ("rails-intro",                     "Introduction to Ruby on Rails"),
        ("getting-your-feet-wet",            "Getting Your Feet Wet"),
        ("routing",                          "Routing"),
        ("controllers",                      "Controllers"),
        ("views",                            "Views"),
        ("active-record-basics",             "Active Record Basics"),
        ("active-record-queries",            "Active Record Queries"),
        ("active-record-associations",       "Active Record Associations"),
        ("project-micro-reddit",             "Project: Micro-Reddit"),
        ("forms-and-rails",                  "Forms and Rails"),
        ("sessions-cookies-and-flashes",     "Sessions, Cookies, and Flashes"),
        ("authentication",                   "Authentication"),
        ("project-members-only",             "Project: Members Only"),
        ("advanced-forms-and-active-record", "Advanced Forms and Active Record"),
        ("project-private-events",           "Project: Private Events"),
        ("project-blog-app",                 "Project: Blog App"),
        ("project-flight-booker",            "Project: Flight Booker"),
        ("api-basics",                       "API Basics"),
        ("action-mailer",                    "Action Mailer"),
        ("advanced-topics",                  "Advanced Topics"),
        ("the-asset-pipeline",               "The Asset Pipeline"),
        ("css-bundling",                     "CSS Bundling"),
        ("installing-postgresql",            "Installing PostgreSQL"),
        ("project-odinbook",                 "Project: Odin-Book"),
    ]

    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">Ruby on Rails</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">Introduction</div>'
        + lnk("rails-intro","Introduction to Rails")
        + lnk("getting-your-feet-wet","Getting Your Feet Wet")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">MVC Deep Dive</div>'
        + lnk("routing","Routing")
        + lnk("controllers","Controllers")
        + lnk("views","Views")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Active Record</div>'
        + lnk("active-record-basics","Active Record Basics")
        + lnk("active-record-queries","Active Record Queries")
        + lnk("active-record-associations","Active Record Associations")
        + lnk("project-micro-reddit","Project: Micro-Reddit",True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Forms and Auth</div>'
        + lnk("forms-and-rails","Forms and Rails")
        + lnk("sessions-cookies-and-flashes","Sessions, Cookies, Flashes")
        + lnk("authentication","Authentication")
        + lnk("project-members-only","Project: Members Only",True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Advanced</div>'
        + lnk("advanced-forms-and-active-record","Advanced Forms and Active Record")
        + lnk("project-private-events","Project: Private Events",True)
        + lnk("project-blog-app","Project: Blog App",True)
        + lnk("project-flight-booker","Project: Flight Booker",True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">APIs and More</div>'
        + lnk("api-basics","API Basics")
        + lnk("action-mailer","Action Mailer")
        + lnk("advanced-topics","Advanced Topics")
        + lnk("the-asset-pipeline","The Asset Pipeline")
        + lnk("css-bundling","CSS Bundling")
        + lnk("installing-postgresql","Installing PostgreSQL")
        + lnk("project-odinbook","Project: Odin-Book",True)
        + '</div></aside>'
    )

    def w(slug, title, intro, overview, body, kc, assignments, resources):
        write(ldir, "Ruby on Rails", ALL, sidebar, slug, title, intro, overview, body, kc, assignments, resources)

    # ==================== LESSONS ====================

    w("rails-intro","Introduction to Ruby on Rails", ... )   # ← your original content here (unchanged)

    # (All your other w() calls remain exactly the same as in the original file)

    # Just copy-paste all the w() calls from your original script between here:
    # ... paste all individual lessons ...

    # And keep the project loop and the rest of the lessons exactly as they were.

    print(f"  Ruby on Rails: {len(ALL)} lessons done")


def main():
    seed_ruby_on_rails()
    print("\nPart 2 complete. Committing...")
    os.chdir(BASE)
    subprocess.run(["git","add","-A"], check=True)
    subprocess.run(["git","commit","-m","Seed Rails path Part 2: Ruby on Rails (24 lessons)"], check=True)
    subprocess.run(["git","push"], check=True)
    print("Pushed.")


if __name__ == "__main__":
    main()
