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
# INTERMEDIATE HTML AND CSS
# ══════════════════════════════════════════════════════
def seed_intermediate_html_css():
    ldir = os.path.join(RAILS, "intermediate-html-css", "lessons")
    os.makedirs(ldir, exist_ok=True)   # ← FIXED

    ALL = [ ... ]  # (your original ALL list unchanged)

    sections = [ ... ]  # (your original sections list unchanged)

    sidebar = css_html_sidebar("Intermediate HTML and CSS", sections)

    SHARED = { ... }   # (your original SHARED dict unchanged)

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
# ADVANCED HTML AND CSS
# ══════════════════════════════════════════════════════
def seed_advanced_html_css():
    ldir = os.path.join(RAILS, "advanced-html-css", "lessons")
    os.makedirs(ldir, exist_ok=True)   # ← FIXED

    ALL = [ ... ]  # unchanged

    sections = [ ... ]  # unchanged
    sidebar = css_html_sidebar("Advanced HTML and CSS", sections)

    CONTENT = { ... }  # your original CONTENT dict

    for slug, title in ALL:
        if slug in CONTENT:
            title, intro, ov = CONTENT[slug]
            body = f"""
<h2 class="lesson-section-title" id="overview">{title} in Rails</h2>
<p>This lesson covers {title} as it applies to Ruby on Rails applications — specifically how to use these techniques in ERB templates, Rails Stimulus controllers, and Tailwind CSS.</p>
""" + code("""# Example Stimulus usage
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  connect() {
    this.element.classList.add('fade-in')
  }
}
""")
        else:
            intro = f"This lesson covers {title} in the context of advanced Rails front-end development."
            ov = [f"Apply {title} in Rails ERB templates.","Use with Stimulus and Turbo."]
            body = f"""
<h2 class="lesson-section-title" id="overview">{title} in Rails</h2>
<p>The same CSS concepts apply in Rails. Focus on integrating them with ERB, Stimulus, and Turbo.</p>
"""

        write(ldir, "Advanced HTML and CSS", "advanced-html-css",
              ALL, sidebar, slug, title, intro, ov, body,
              [(f"How does {title} integrate with Rails Turbo/Stimulus?","overview")],
              [f"Apply {title} techniques to your Rails project.",
               "Respect prefers-reduced-motion."],
              [("MDN — CSS Reference","https://developer.mozilla.org/en-US/docs/Web/CSS"),
               ("Hotwire","https://hotwired.dev/"),
               ("Kevin Powell","https://www.youtube.com/@KevinPowell")])

    print(f"  Advanced HTML/CSS (Rails): {len(ALL)} lessons done")


# ══════════════════════════════════════════════════════
# GETTING HIRED
# ══════════════════════════════════════════════════════
def seed_getting_hired():
    ldir = os.path.join(RAILS, "getting-hired", "lessons")
    os.makedirs(ldir, exist_ok=True)   # ← FIXED

    ALL = [ ... ]  # unchanged

    sidebar = ...  # your original sidebar

    CONTENT = { ... }  # your original CONTENT

    for slug, _ in ALL:
        if slug in CONTENT:
            title, intro, ov = CONTENT[slug]
        else:
            title = next((t for s,t in ALL if s == slug), slug)
            intro = f"This lesson covers {title} for Rails developers."
            ov = ["Apply strategies to Rails job search.", "Leverage Ruby community."]

        body = f"""
<h2 class="lesson-section-title" id="overview">Rails Job Search Context</h2>
<p>The job search advice in this lesson applies universally, with a strong Ruby on Rails focus.</p>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Rails companies value solid Ruby/Rails fundamentals, testing, and understanding of conventions.</p>
</div>
"""

        write(ldir, "Getting Hired", "getting-hired",
              ALL, sidebar, slug, title, intro, ov, body,
              [(f"How does {title} differ for Rails vs JavaScript jobs?","overview")],
              [f"Complete the {title} action items.","Join Ruby community channels."],
              [("Ruby on Rails Link Slack","https://www.rubyonrails.link/"),
               ("RubyConf","https://rubyconf.org/"),
               ("Levels.fyi","https://www.levels.fyi/")])

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
