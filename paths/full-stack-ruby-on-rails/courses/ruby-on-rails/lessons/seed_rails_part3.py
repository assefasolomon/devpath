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

    # ------------------------------------------------------------------ #
    # FIX 1: closing ) added after the directory-structure code() block   #
    # ------------------------------------------------------------------ #
    w("rails-intro","Introduction to Ruby on Rails",
    intro="Ruby on Rails is a full-stack web framework built on Ruby that emphasises convention over configuration and the DRY principle. It lets you build complete web applications remarkably quickly.",
    overview=["Understand what Rails is and what it provides.","Know the MVC architecture Rails uses.","Understand convention over configuration.","Know the Rails directory structure."],
    body="""
<h2 class="lesson-section-title" id="what-is-rails">What Is Rails?</h2>
<p>Rails is a full-stack web framework: it handles routing, controllers, views, database interactions, email, background jobs, caching, and testing — all in one package with strong conventions. The same conventions shared by millions of Rails developers means you can read and contribute to any Rails codebase immediately.</p>

<h2 class="lesson-section-title" id="mvc">MVC Architecture</h2>
<ul>
  <li><strong>Model</strong> — represents data and business logic. Talks to the database via Active Record.</li>
  <li><strong>View</strong> — templates that render HTML. ERB by default.</li>
  <li><strong>Controller</strong> — receives requests, calls models, passes data to views.</li>
</ul>

<h2 class="lesson-section-title" id="conventions">Key Conventions</h2>
""" + code("""# Convention: naming things right makes Rails wire everything automatically

# Model:      singular, CamelCase    → User, BlogPost
# Table:      plural, snake_case     → users, blog_posts
# Controller: plural, CamelCase      → UsersController
# Route:      plural, snake_case     → /users, /blog_posts
# View folder:plural, snake_case     → views/users/, views/blog_posts/

# Rails infers all of these from a single name
rails generate scaffold Post title:string body:text published:boolean
# Creates: migration, model, controller, views, routes, tests — all correctly named
""") + """
<h2 class="lesson-section-title" id="directory">Directory Structure</h2>
""" + code("""app/
├── controllers/        ← Controller classes
├── models/             ← ActiveRecord models
├── views/              ← ERB templates
├── helpers/            ← View helper methods
├── assets/             ← CSS, JS, images
config/
├── routes.rb           ← URL routing
├── database.yml        ← Database configuration
db/
├── migrate/            ← Database migrations
├── schema.rb           ← Current schema snapshot
Gemfile                 ← Dependencies
"""),      # <-- FIX 1: was missing this closing ) on the code() call
    kc=[("What does 'convention over configuration' mean in Rails?","conventions"),
        ("What are the three parts of MVC?","mvc"),
        ("What file defines Rails routes?","directory")],
    assignments=["Read the Rails Guides 'Getting Started with Rails' introduction.","Watch the DHH Rails demo to understand the speed of Rails development."],
    resources=[
        ("Rails Guides — Getting Started","https://guides.rubyonrails.org/getting_started.html"),
        ("YouTube — Rails in 20 minutes (GoRails)","https://www.youtube.com/watch?v=TPy4CxNnqZk"),
    ])

    # ------------------------------------------------------------------ #
    # FIX 2: closing ) added after the rails-console code() block        #
    # ------------------------------------------------------------------ #
    w("getting-your-feet-wet","Getting Your Feet Wet",
    intro="The fastest way to understand Rails is to build something. This lesson walks you through creating your first Rails application — a complete blog in under an hour.",
    overview=["Install Rails and create a new application.","Generate a scaffold for a resource.","Run database migrations.","Start the development server.","Understand what the scaffold generated."],
    body="""
<h2 class="lesson-section-title" id="install">Installing Rails</h2>
""" + code("""gem install rails

# Verify
rails --version    # Rails 7.x.x

# Create a new app (with PostgreSQL)
rails new blog --database=postgresql
cd blog

# Set up the database
rails db:create
""") + """
<h2 class="lesson-section-title" id="scaffold">Your First Scaffold</h2>
""" + code("""# Generate a complete CRUD scaffold
rails generate scaffold Post title:string body:text published:boolean

# This creates:
# - db/migrate/TIMESTAMP_create_posts.rb
# - app/models/post.rb
# - app/controllers/posts_controller.rb
# - app/views/posts/ (index, show, new, edit, _form partials)
# - config/routes.rb entry
# - test files

# Run the migration to create the database table
rails db:migrate

# Start the server
rails server
# Visit http://localhost:3000/posts
""") + """
<h2 class="lesson-section-title" id="console">Rails Console</h2>
""" + code("""# The Rails console is like irb but with your entire app loaded
rails console

# Create records
Post.create!(title: "Hello Rails", body: "My first post", published: true)

# Query
Post.all
Post.where(published: true)
Post.find(1)
Post.first

# Update
post = Post.find(1)
post.update(title: "Updated Title")

# Delete
post.destroy
"""),      # <-- FIX 2: was missing this closing ) on the code() call
    kc=[("What does rails generate scaffold create?","scaffold"),
        ("What command runs database migrations?","scaffold"),
        ("What does the Rails console give you access to?","console")],
    assignments=["Create a new Rails app and generate a Post scaffold.","Create, read, update, and delete posts through both the web interface and the Rails console."],
    resources=[
        ("Rails Guides — Getting Started","https://guides.rubyonrails.org/getting_started.html"),
        ("YouTube — Rails Crash Course (Traversy Media)","https://www.youtube.com/watch?v=pPy0GQJLZUM"),
    ])

    w("routing","Routing",
    intro="The Rails router translates incoming HTTP requests into controller actions. Understanding routing deeply is key to building well-structured Rails applications.",
    overview=["Use resources to generate RESTful routes.","Define custom routes.","Use nested routes.","Understand route helpers and path methods.","Use namespace and scope."],
    body="""
<h2 class="lesson-section-title" id="resources">resources Routing</h2>
""" + code("""# config/routes.rb
Rails.application.routes.draw do
  resources :posts
end

# This generates 7 routes:
# GET    /posts          → posts#index
# GET    /posts/new      → posts#new
# POST   /posts          → posts#create
# GET    /posts/:id      → posts#show
# GET    /posts/:id/edit → posts#edit
# PATCH  /posts/:id      → posts#update
# DELETE /posts/:id      → posts#destroy

# Check all routes
rails routes
# or
rails routes --grep posts
""") + """
<h2 class="lesson-section-title" id="nested-routes">Nested Routes</h2>
""" + code("""resources :posts do
  resources :comments   # /posts/:post_id/comments
end

# Generates (among others):
# GET  /posts/:post_id/comments      → comments#index
# POST /posts/:post_id/comments      → comments#create
# GET  /posts/:post_id/comments/:id  → comments#show

# Shallow nesting — avoids deep URLs
resources :posts, shallow: true do
  resources :comments
end
# GET /posts/:post_id/comments       → comments#index
# GET /comments/:id                  → comments#show (not nested)
""") + """
<h2 class="lesson-section-title" id="route-helpers">Route Helpers</h2>
""" + code("""# Rails generates path/url helpers for every route
posts_path                    # /posts
new_post_path                 # /posts/new
post_path(@post)              # /posts/42
edit_post_path(@post)         # /posts/42/edit
post_comments_path(@post)     # /posts/42/comments

# Use in views and controllers
link_to "All Posts", posts_path
redirect_to post_path(@post)
""") + """
<h2 class="lesson-section-title" id="custom-routes">Custom Routes</h2>
""" + code("""# Custom member routes (single resource)
resources :posts do
  member do
    patch :publish    # PATCH /posts/:id/publish
    post  :feature    # POST  /posts/:id/feature
  end
  collection do
    get :search       # GET /posts/search
    get :drafts       # GET /posts/drafts
  end
end

# Root route
root "posts#index"

# Named route
get "/about", to: "pages#about", as: :about
"""),
    kc=[("What seven routes does resources :posts generate?","resources"),
        ("What is shallow nesting?","nested-routes"),
        ("What is the difference between member and collection routes?","custom-routes")],
    assignments=["Run rails routes on your blog app and read every route.","Add nested comments routes to your blog app."],
    resources=[
        ("Rails Guides — Routing","https://guides.rubyonrails.org/routing.html"),
        ("YouTube — Rails Routing (GoRails)","https://www.youtube.com/watch?v=5unPfSkpnGE"),
    ])

    w("controllers","Controllers",
    intro="Controllers are the bridge between routes and everything else — they receive requests, interact with models, and render responses. This lesson covers what every Rails controller does.",
    overview=["Understand what a controller action does.","Access request params.","Use before_action filters.","Render views and redirect.","Use strong parameters."],
    body="""
<h2 class="lesson-section-title" id="controller-actions">Controller Actions</h2>
""" + code("""# app/controllers/posts_controller.rb
class PostsController < ApplicationController
  before_action :set_post, only: [:show, :edit, :update, :destroy]
  before_action :require_login, except: [:index, :show]

  def index
    @posts = Post.published.order(created_at: :desc).page(params[:page])
  end

  def show
    # @post set by before_action
  end

  def new
    @post = Post.new
  end

  def create
    @post = Post.new(post_params)
    if @post.save
      redirect_to @post, notice: "Post created successfully."
    else
      render :new, status: :unprocessable_entity
    end
  end

  def update
    if @post.update(post_params)
      redirect_to @post, notice: "Post updated."
    else
      render :edit, status: :unprocessable_entity
    end
  end

  def destroy
    @post.destroy
    redirect_to posts_path, notice: "Post deleted."
  end

  private

  def set_post
    @post = Post.find(params[:id])
  end

  def post_params
    params.require(:post).permit(:title, :body, :published)
  end
end
""") + """
<h2 class="lesson-section-title" id="strong-params">Strong Parameters</h2>
<p>Strong parameters protect against mass assignment attacks by explicitly listing which parameters are allowed. Never pass <code>params</code> directly to a model.</p>
""" + code("""# DANGEROUS — allows any parameter
Post.new(params[:post])   # never do this

# SAFE — only permitted fields pass through
def post_params
  params.require(:post).permit(:title, :body, :published, tag_ids: [])
end

# For nested attributes
params.require(:user).permit(
  :name, :email,
  address_attributes: [:street, :city, :country]
)
"""),
    kc=[("What does before_action do?","controller-actions"),
        ("What is the create action's response when saving fails?","controller-actions"),
        ("What are strong parameters and why are they needed?","strong-params")],
    assignments=["Add before_action filters to your blog controller for authentication and record finding.","Write strong parameters for a User model with nested address attributes."],
    resources=[
        ("Rails Guides — Action Controller","https://guides.rubyonrails.org/action_controller_overview.html"),
        ("YouTube — Rails Controllers (GoRails)","https://www.youtube.com/watch?v=y8S7BJ5bVno"),
    ])

    w("views","Views",
    intro="Rails views are ERB templates that render HTML. They have access to instance variables set in the controller and can call helper methods. This lesson covers ERB, layouts, partials, and helpers.",
    overview=["Write ERB templates.","Use layouts for shared page structure.","Use partials for reusable view components.","Write and use view helpers.","Use Rails link and form helpers."],
    body="""
<h2 class="lesson-section-title" id="erb">ERB Syntax</h2>
""" + code("""<!-- app/views/posts/show.html.erb -->
<article class="post">
  <h1><%= @post.title %></h1>       <!-- outputs escaped value -->
  <p class="meta">
    Posted by <%= @post.author.name %>
    on <%= @post.created_at.strftime("%B %d, %Y") %>
  </p>

  <div class="body">
    <%= simple_format(@post.body) %>  <!-- converts newlines to <br>/<p> -->
  </div>

  <% if current_user == @post.author %>  <!-- no output -->
    <%= link_to "Edit", edit_post_path(@post), class: "btn" %>
    <%= button_to "Delete", @post, method: :delete, data: { turbo_confirm: "Sure?" } %>
  <% end %>
</article>
""") + """
<h2 class="lesson-section-title" id="layouts-partials">Layouts and Partials</h2>
""" + code("""<!-- app/views/layouts/application.html.erb — shared layout -->
<!DOCTYPE html>
<html>
<head>
  <title><%= content_for?(:title) ? yield(:title) : "MyApp" %></title>
  <%= stylesheet_link_tag "application" %>
  <%= javascript_include_tag "application", defer: true %>
</head>
<body>
  <%= render "shared/navbar" %>
  <main>
    <%= render "shared/flash_messages" %>
    <%= yield %>                    <!-- view content goes here -->
  </main>
  <%= render "shared/footer" %>
</body>
</html>
""") + code("""<!-- Partial: app/views/posts/_post.html.erb -->
<article class="post-card">
  <h2><%= link_to post.title, post_path(post) %></h2>
  <p><%= truncate(post.body, length: 150) %></p>
</article>

<!-- Render the partial -->
<%= render @posts %>               <!-- Rails finds _post.html.erb automatically -->
<%= render "posts/post", post: @post %>   <!-- explicit -->
<%= render partial: "post", collection: @posts, as: :post %>  <!-- collection -->
"""),
    kc=[("What is the difference between <%= %> and <% %> in ERB?","erb"),
        ("What does yield do in a layout?","layouts-partials"),
        ("What is a partial and how do you render one?","layouts-partials")],
    assignments=["Add a shared navigation partial to your blog app.","Create a post card partial and use it on the index page with a collection render."],
    resources=[
        ("Rails Guides — Layouts and Rendering","https://guides.rubyonrails.org/layouts_and_rendering.html"),
        ("YouTube — Rails Views (GoRails)","https://www.youtube.com/watch?v=c-NnvMGvK0E"),
    ])

    w("active-record-basics","Active Record Basics",
    intro="Active Record is Rails' ORM (Object-Relational Mapper). It connects Ruby classes to database tables, letting you write Ruby code instead of SQL for most database operations.",
    overview=["Create and run database migrations.","Define models with validations.","Perform CRUD operations with Active Record methods.","Use callbacks."],
    body="""
<h2 class="lesson-section-title" id="migrations">Migrations</h2>
""" + code("""# Generate a migration
rails generate migration CreatePosts title:string body:text published:boolean

# db/migrate/20240101000000_create_posts.rb
class CreatePosts < ActiveRecord::Migration[7.1]
  def change
    create_table :posts do |t|
      t.string  :title, null: false
      t.text    :body
      t.boolean :published, default: false, null: false
      t.references :user, null: false, foreign_key: true

      t.timestamps  # adds created_at and updated_at
    end

    add_index :posts, [:user_id, :created_at]
  end
end

# Run migration
rails db:migrate

# Rollback last migration
rails db:rollback
""") + """
<h2 class="lesson-section-title" id="validations">Models and Validations</h2>
""" + code("""# app/models/post.rb
class Post < ApplicationRecord
  belongs_to :user
  has_many   :comments, dependent: :destroy

  validates :title, presence: true, length: { minimum: 5, maximum: 200 }
  validates :body,  presence: true
  validates :slug,  uniqueness: true, allow_blank: true

  # Custom validation
  validate :publication_date_cannot_be_in_past

  # Scopes — reusable query fragments
  scope :published, -> { where(published: true) }
  scope :recent,    -> { order(created_at: :desc) }
  scope :by_author, ->(user) { where(user: user) }

  # Callbacks
  before_save :generate_slug
  after_create :notify_subscribers

  private

  def generate_slug
    self.slug = title.parameterize if slug.blank?
  end

  def publication_date_cannot_be_in_past
    if published_at.present? && published_at < Time.current
      errors.add(:published_at, "can't be in the past")
    end
  end
end
"""),
    kc=[("What does t.timestamps add?","migrations"),
        ("What is a scope in Active Record?","validations"),
        ("When does a before_save callback run?","validations")],
    assignments=["Add validations to your blog Post model.","Create a scope that returns only published posts ordered by date.","Write a before_save callback that generates a slug from the title."],
    resources=[
        ("Rails Guides — Active Record Migrations","https://guides.rubyonrails.org/active_record_migrations.html"),
        ("Rails Guides — Active Record Validations","https://guides.rubyonrails.org/active_record_validations.html"),
        ("YouTube — Active Record Basics (GoRails)","https://www.youtube.com/watch?v=RZJBr2gWlS0"),
    ])

    w("active-record-queries","Active Record Queries",
    intro="Active Record provides a powerful query interface that generates efficient SQL. This lesson covers everything from simple finds to complex joins and aggregations.",
    overview=["Use where, order, limit, and offset.","Use joins and includes for associations.","Write aggregation queries.","Understand N+1 queries and how to fix them.","Use explain to analyse query performance."],
    body="""
<h2 class="lesson-section-title" id="basic-queries">Basic Queries</h2>
""" + code("""# Finding records
Post.all
Post.find(1)                          # raises RecordNotFound if missing
Post.find_by(slug: "hello-world")     # returns nil if missing
Post.find_by!(slug: "hello-world")    # raises if missing

# Filtering
Post.where(published: true)
Post.where("created_at > ?", 1.week.ago)
Post.where(user_id: [1, 2, 3])
Post.where.not(published: false)

# Ordering, limiting
Post.order(created_at: :desc).limit(10).offset(20)

# Selecting specific columns
Post.select(:id, :title, :slug)
""") + """
<h2 class="lesson-section-title" id="n-plus-one">N+1 Queries and includes</h2>
""" + code("""# N+1 PROBLEM — queries the DB N+1 times
posts = Post.all
posts.each { |post| puts post.user.name }
# SELECT * FROM posts;
# SELECT * FROM users WHERE id = 1;   (for each post!)
# SELECT * FROM users WHERE id = 2;
# 101 queries for 100 posts

# FIX — use includes to eager-load associations
posts = Post.includes(:user).all
posts.each { |post| puts post.user.name }
# SELECT * FROM posts;
# SELECT * FROM users WHERE id IN (1, 2, 3, ...);
# 2 queries total

# includes with nested associations
Post.includes(comments: :user).where(published: true)

# joins — for filtering on associated data
Post.joins(:user).where(users: { role: :admin })
""") + """
<h2 class="lesson-section-title" id="aggregation">Aggregation</h2>
""" + code("""Post.count
Post.where(published: true).count
Post.average(:word_count).round(1)
Post.maximum(:view_count)
Post.group(:user_id).count    # hash: { user_id => count }
Post.group("DATE(created_at)").count  # posts per day
"""),
    kc=[("What is an N+1 query problem?","n-plus-one"),
        ("What is the difference between joins and includes?","n-plus-one"),
        ("What does find vs find_by return when no record exists?","basic-queries")],
    assignments=["Find all N+1 queries in your blog app using the Bullet gem.","Fix them with includes."],
    resources=[
        ("Rails Guides — Active Record Query Interface","https://guides.rubyonrails.org/active_record_querying.html"),
        ("YouTube — N+1 Queries (GoRails)","https://www.youtube.com/watch?v=AJVQpSEPXlY"),
    ])

    w("active-record-associations","Active Record Associations",
    intro="Associations define the relationships between your models — belongs_to, has_many, has_one, and the powerful has_many :through. Getting associations right makes everything else easier.",
    overview=["Set up belongs_to and has_many associations.","Use has_many :through for many-to-many relationships.","Use has_one.","Understand dependent: :destroy.","Use polymorphic associations."],
    body="""
<h2 class="lesson-section-title" id="basic-associations">Basic Associations</h2>
""" + code("""# One-to-many
class User < ApplicationRecord
  has_many :posts, dependent: :destroy
  has_many :comments
end

class Post < ApplicationRecord
  belongs_to :user  # requires user_id column
  has_many   :comments, dependent: :destroy
end

# Association methods Rails generates
user.posts                   # all posts by this user
user.posts.create(title: "Hello")
user.posts.build(title: "Hello")  # not saved yet
post.user                    # the user who wrote this post
post.build_user(name: "Bob") # builds associated user
""") + """
<h2 class="lesson-section-title" id="has-many-through">has_many :through</h2>
""" + code("""# Many-to-many: posts have many tags through post_tags
class Post < ApplicationRecord
  has_many :post_tags
  has_many :tags, through: :post_tags
end

class Tag < ApplicationRecord
  has_many :post_tags
  has_many :posts, through: :post_tags
end

class PostTag < ApplicationRecord
  belongs_to :post
  belongs_to :tag
end

# Usage
post.tags                    # all tags for this post
post.tags << Tag.find_by(name: "Ruby")
tag.posts                    # all posts with this tag
""") + """
<h2 class="lesson-section-title" id="polymorphic">Polymorphic Associations</h2>
""" + code("""# A Comment can belong to either a Post or a Photo
class Comment < ApplicationRecord
  belongs_to :commentable, polymorphic: true
end

class Post < ApplicationRecord
  has_many :comments, as: :commentable
end

class Photo < ApplicationRecord
  has_many :comments, as: :commentable
end

# Migration
# t.references :commentable, polymorphic: true, null: false
# adds commentable_id and commentable_type columns

# Usage
post.comments
photo.comments
comment.commentable   # returns either a Post or Photo
"""),
    kc=[("What does dependent: :destroy do?","basic-associations"),
        ("What is the difference between build and create on an association?","basic-associations"),
        ("When would you use a polymorphic association?","polymorphic")],
    assignments=["Add tags to your blog using has_many :through.","Make comments polymorphic so they work on both posts and pages."],
    resources=[
        ("Rails Guides — Active Record Associations","https://guides.rubyonrails.org/association_basics.html"),
        ("YouTube — Rails Associations (GoRails)","https://www.youtube.com/watch?v=MVIcqCkAcLQ"),
    ])

    w("project-micro-reddit","Project: Micro-Reddit",
    intro="Build a simplified Reddit clone focusing entirely on the data layer — models, associations, and validations. No views or controllers yet.",
    overview=["Model Users, Posts (Links), and Comments with proper associations.","Add validations to all models.","Test the data layer in the Rails console."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>User: username (unique, 3–20 chars), email (unique), password_digest</li>
  <li>Post: title (required, max 200 chars), url (required, valid URL), user</li>
  <li>Comment: body (required, max 1000 chars), user, post</li>
  <li>A user has_many posts and comments</li>
  <li>A post has_many comments and belongs_to user</li>
  <li>A comment belongs_to both post and user</li>
</ul>
""" + code("""rails new micro-reddit --database=postgresql
cd micro-reddit
rails db:create

# Generate models with associations
rails generate model User username:string email:string password_digest:string
rails generate model Post title:string url:string user:references
rails generate model Comment body:text user:references post:references

rails db:migrate

# Test in console
rails console
user = User.create!(username: "alice", email: "alice@example.com", password_digest: "test")
post = user.posts.create!(title: "Ruby is awesome", url: "https://ruby-lang.org")
comment = post.comments.create!(body: "Totally agree!", user: user)
post.comments.count     # 1
user.posts.first.title  # "Ruby is awesome"
"""),
    kc=[("What foreign keys are needed in the comments table?","requirements"),
        ("How do you create a post associated with a user?","requirements")],
    assignments=["Complete Micro-Reddit meeting all model and validation requirements.","Test all associations thoroughly in the Rails console."],
    resources=[
        ("Rails Guides — Active Record Associations","https://guides.rubyonrails.org/association_basics.html"),
        ("Rails Guides — Active Record Validations","https://guides.rubyonrails.org/active_record_validations.html"),
    ])

    w("forms-and-rails","Forms and Rails",
    intro="Rails provides powerful form helpers that generate HTML forms tied to your models, handle CSRF protection automatically, and make handling form submissions clean and secure.",
    overview=["Use form_with for model-backed forms.","Understand how Rails handles form parameters.","Display validation errors.","Use select, checkboxes, radio buttons, and file uploads."],
    body="""
<h2 class="lesson-section-title" id="form-with">form_with</h2>
""" + code("""<!-- app/views/posts/_form.html.erb -->
<%= form_with model: @post do |form| %>
  <% if @post.errors.any? %>
    <div class="error-messages">
      <h3><%= pluralize(@post.errors.count, "error") %> prevented saving:</h3>
      <ul>
        <% @post.errors.each do |error| %>
          <li><%= error.full_message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div class="field">
    <%= form.label :title %>
    <%= form.text_field :title, class: "form-input" %>
  </div>

  <div class="field">
    <%= form.label :body %>
    <%= form.text_area :body, rows: 8, class: "form-input" %>
  </div>

  <div class="field">
    <%= form.label :published %>
    <%= form.check_box :published %>
  </div>

  <div class="field">
    <%= form.label :category %>
    <%= form.select :category_id, Category.all.collect { |c| [c.name, c.id] }, include_blank: "Select a category" %>
  </div>

  <%= form.submit class: "btn btn-primary" %>
<% end %>
""") + """
<h2 class="lesson-section-title" id="file-uploads">File Uploads with Active Storage</h2>
""" + code("""# Set up Active Storage
rails active_storage:install
rails db:migrate

# Model
class Post < ApplicationRecord
  has_one_attached :cover_image       # single file
  has_many_attached :attachments      # multiple files
end

# Form
<%= form.file_field :cover_image, accept: "image/*" %>

# View
<%= image_tag @post.cover_image if @post.cover_image.attached? %>
"""),
    kc=[("What does form_with model: @post automatically determine?","form-with"),
        ("How does Rails display validation errors in a form?","form-with"),
        ("What Rails feature handles file uploads?","file-uploads")],
    assignments=["Build a complete post creation form with all field types above.","Add file upload support for a cover image using Active Storage."],
    resources=[
        ("Rails Guides — Form Helpers","https://guides.rubyonrails.org/form_helpers.html"),
        ("Rails Guides — Active Storage","https://guides.rubyonrails.org/active_storage_overview.html"),
        ("YouTube — Rails Forms (GoRails)","https://www.youtube.com/watch?v=OPFHQZqJnKY"),
    ])

    w("sessions-cookies-and-flashes","Sessions, Cookies, and Flashes",
    intro="Sessions remember users across requests. Cookies store data in the browser. Flash messages communicate one-time notifications. Together they make web applications feel stateful.",
    overview=["Understand how the HTTP session works in Rails.","Store and read data from the session.","Use cookies for persistent storage.","Use flash messages for one-time notifications."],
    body="""
<h2 class="lesson-section-title" id="sessions">Sessions</h2>
""" + code("""# Sessions are stored server-side (or encrypted cookie)
# Access via the session hash in any controller

# Store data
session[:user_id] = @user.id
session[:cart]    = { items: [], total: 0 }

# Read data
current_user_id = session[:user_id]

# Clear a key
session.delete(:user_id)

# Clear everything (logout)
reset_session

# In ApplicationController — make current_user available everywhere
class ApplicationController < ActionController::Base
  helper_method :current_user, :logged_in?

  def current_user
    @current_user ||= User.find_by(id: session[:user_id])
  end

  def logged_in?
    current_user.present?
  end

  def require_login
    redirect_to login_path, alert: "Please log in." unless logged_in?
  end
end
""") + """
<h2 class="lesson-section-title" id="flash">Flash Messages</h2>
""" + code("""# In controllers — set a flash message
redirect_to @post, notice: "Post created successfully."
redirect_to root_path, alert: "Something went wrong."

# Custom flash key
flash[:success] = "Profile updated!"
flash[:error]   = "Invalid password."

# In layout — display flash messages
<% flash.each do |type, message| %>
  <div class="flash flash-<%= type %>">
    <%= message %>
  </div>
<% end %>

# flash.now — only available in the current action (not after redirect)
flash.now[:error] = "Invalid credentials."
render :login
"""),
    kc=[("What is the difference between session and cookies?","sessions"),
        ("What is the difference between flash and flash.now?","flash"),
        ("What does reset_session do?","sessions")],
    assignments=["Implement a login system that stores the user_id in the session.","Add flash messages to all create, update, and destroy actions."],
    resources=[
        ("Rails Guides — Action Controller — Sessions","https://guides.rubyonrails.org/action_controller_overview.html#session"),
        ("YouTube — Rails Sessions and Cookies (GoRails)","https://www.youtube.com/watch?v=F9xCsLzTy48"),
    ])

    w("authentication","Authentication",
    intro="Rails authentication involves securely storing passwords and managing login state. This lesson covers has_secure_password and building a complete authentication system from scratch before using the Devise gem.",
    overview=["Use has_secure_password with bcrypt.","Build registration and login from scratch.","Use Devise for production authentication.","Implement remember_me functionality."],
    body="""
<h2 class="lesson-section-title" id="has-secure-password">has_secure_password</h2>
""" + code("""# Gemfile
gem 'bcrypt'

# User model
class User < ApplicationRecord
  has_secure_password
  # Automatically adds: password, password_confirmation attributes
  # Hashes password to password_digest before saving
  # Adds authenticate(password) method

  validates :email, presence: true, uniqueness: true
  validates :password, length: { minimum: 8 }, allow_nil: true
end

# Migration needs password_digest column
# t.string :password_digest, null: false
""") + code("""# Registration
def create
  @user = User.new(user_params)
  if @user.save
    session[:user_id] = @user.id
    redirect_to root_path, notice: "Welcome!"
  else
    render :new, status: :unprocessable_entity
  end
end

# Login
def create
  @user = User.find_by(email: params[:email])
  if @user&.authenticate(params[:password])
    session[:user_id] = @user.id
    redirect_to root_path, notice: "Logged in!"
  else
    flash.now[:alert] = "Invalid email or password."
    render :new, status: :unprocessable_entity
  end
end

# Logout
def destroy
  reset_session
  redirect_to root_path, notice: "Logged out."
end
""") + """
<h2 class="lesson-section-title" id="devise">Devise</h2>
""" + code("""# Gemfile
gem 'devise'

# Setup
rails generate devise:install
rails generate devise User
rails db:migrate

# Devise gives you:
# - Registration, login, logout
# - Password reset emails
# - Email confirmation
# - Remember me
# - Account locking

# In controllers
before_action :authenticate_user!   # require login
current_user                        # logged-in user
user_signed_in?                     # boolean
"""),
    kc=[("What does has_secure_password add to a model?","has-secure-password"),
        ("What does authenticate(password) return?","has-secure-password"),
        ("What does Devise provide that a manual implementation does not?","devise")],
    assignments=["Build a complete authentication system from scratch using has_secure_password.","Then add Devise to a separate app and compare the two approaches."],
    resources=[
        ("Rails Docs — has_secure_password","https://api.rubyonrails.org/classes/ActiveModel/SecurePassword/ClassMethods.html"),
        ("Devise — GitHub","https://github.com/heartcombo/devise"),
        ("YouTube — Rails Authentication from Scratch (GoRails)","https://www.youtube.com/watch?v=X2H2OfMjytw"),
    ])

    w("project-members-only","Project: Members Only",
    intro="Build a members-only message board using Rails. Non-members see messages but not who wrote them. Members see author information. Admins can delete messages.",
    overview=["Implement full authentication with has_secure_password.","Show different content based on membership status.","Implement admin-only actions.","Use before_action for authorisation."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Sign up with first name, last name, username, password</li>
  <li>All users see messages but only members see author name and timestamp</li>
  <li>A secret passcode form upgrades a user to member</li>
  <li>Admins can delete any message (set admin flag directly in DB)</li>
  <li>Members can create messages with a title and text</li>
</ul>
""" + code("""rails new members-only --database=postgresql
cd members-only
rails generate model User first_name:string last_name:string \
  username:string password_digest:string membership_status:boolean admin:boolean
rails generate model Message title:string text:text user:references
rails db:create db:migrate
"""),
    kc=[("How do you show/hide content based on membership?","requirements"),
        ("How do you protect the delete action to admins only?","requirements")],
    assignments=["Complete Members Only meeting all requirements.","Deploy to a cloud platform."],
    resources=[
        ("Rails Guides — Action Controller","https://guides.rubyonrails.org/action_controller_overview.html"),
    ])

    w("advanced-forms-and-active-record","Advanced Forms and Active Record",
    intro="Real applications have complex forms: nested attributes, dynamic fields, and multi-step processes. This lesson covers the techniques Rails provides for handling them.",
    overview=["Use accepts_nested_attributes_for.","Build forms with nested models.","Use fields_for for nested forms.","Handle many-to-many form relationships.","Use virtual attributes."],
    body="""
<h2 class="lesson-section-title" id="nested-attributes">Nested Attributes</h2>
""" + code("""# Model — allow creating/editing associated records in the same form
class Post < ApplicationRecord
  has_many :tags, through: :post_tags
  has_many :post_tags

  has_many :comments
  accepts_nested_attributes_for :comments,
    allow_destroy: true,
    reject_if: :all_blank
end

# Controller — permit nested params
def post_params
  params.require(:post).permit(
    :title, :body, :published,
    comments_attributes: [:id, :body, :_destroy]
  )
end
""") + code("""<!-- Form with nested comments -->
<%= form_with model: @post do |form| %>
  <%= form.text_field :title %>

  <h3>Comments</h3>
  <%= form.fields_for :comments do |comment_form| %>
    <div class="nested-comment">
      <%= comment_form.text_area :body %>
      <%= comment_form.check_box :_destroy %>
      <%= comment_form.label :_destroy, "Remove this comment" %>
    </div>
  <% end %>

  <%= link_to_add_association "Add Comment", form, :comments %>
<% end %>
"""),
    kc=[("What does accepts_nested_attributes_for enable?","nested-attributes"),
        ("What does _destroy do in a nested form?","nested-attributes"),
        ("How do you permit nested attributes in strong params?","nested-attributes")],
    assignments=["Add nested tag creation to your post form.","Allow editing user addresses as nested attributes on the user form."],
    resources=[
        ("Rails Guides — Form Helpers — Nested Forms","https://guides.rubyonrails.org/form_helpers.html#building-complex-forms"),
        ("Cocoon Gem — Dynamic Nested Forms","https://github.com/nathanvda/cocoon"),
    ])

    for slug, title, description, extra_code in [
        ("project-private-events","Project: Private Events",
         "Build a private events site where users can create events, invite others, and manage attendance.",
         code("""rails new private-events --database=postgresql
rails generate model User name:string email:string password_digest:string
rails generate model Event title:string description:text creator:references date:datetime location:string
rails generate model Attendance user:references event:references status:string
""")
        ),
        ("project-blog-app","Project: Blog App",
         "Build a full blog application with users, posts, comments, tags, and admin functionality.",
         code("""# Features required:
# - Users can register and log in
# - Authors can create, edit, delete posts (markdown support)
# - Posts have tags (many-to-many)
# - Any user can comment
# - Admin can manage all content
# - Posts have slugs for clean URLs
""")
        ),
        ("project-flight-booker","Project: Flight Booker",
         "Build a multi-step flight booking form — select flights, enter passenger details, confirm booking.",
         code("""# Step 1: Select departure airport, arrival airport, date, passengers
# Step 2: Select from available flights matching criteria
# Step 3: Enter passenger details for each passenger
# Step 4: Booking confirmation

# Models needed:
rails generate model Airport code:string name:string city:string
rails generate model Flight departure_airport:references \
  arrival_airport:references departure_time:datetime duration_minutes:integer price_cents:integer
rails generate model Booking flight:references confirmation_number:string
rails generate model Passenger booking:references name:string email:string
""")
        ),
    ]:
        w(slug, title,
        intro=description + " This project practises everything learned so far in the Rails course.",
        overview=["Design the database schema and associations.","Build complete CRUD for all resources.","Implement authentication and authorisation.","Deploy to a cloud platform."],
        body=f"""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<p>{description}</p>
<ul>
  <li>Full authentication using has_secure_password or Devise</li>
  <li>Authorisation — users can only edit/delete their own records</li>
  <li>Proper validations on all models</li>
  <li>Clean, semantic HTML with a well-styled interface</li>
  <li>Deployed on a free hosting platform (Fly.io or Render)</li>
</ul>
{extra_code}""",
        kc=[("What models and associations does this project require?","requirements"),
            ("How do you authorise users to edit only their own records?","requirements")],
        assignments=[f"Complete {title} meeting all requirements above.","Push to GitHub and deploy publicly."],
        resources=[
            ("Rails Guides — Getting Started","https://guides.rubyonrails.org/getting_started.html"),
            ("Fly.io — Deploy a Rails App","https://fly.io/docs/rails/getting-started/"),
        ])

    w("api-basics","API Basics",
    intro="Rails can serve as both a traditional server-rendered app and a JSON API. This lesson covers how to build a REST API with Rails and how to consume external APIs.",
    overview=["Render JSON responses from controllers.","Use jbuilder or ActiveModelSerializers.","Handle authentication for API endpoints.","Make HTTP requests to external APIs with Faraday."],
    body="""
<h2 class="lesson-section-title" id="json-responses">JSON Responses</h2>
""" + code("""class Api::V1::PostsController < ApplicationController
  before_action :authenticate_api_user!

  def index
    @posts = Post.published.includes(:user).page(params[:page])
    render json: @posts, each_serializer: PostSerializer
  end

  def show
    @post = Post.find(params[:id])
    render json: @post, serializer: PostSerializer
  end

  def create
    @post = current_user.posts.build(post_params)
    if @post.save
      render json: @post, status: :created
    else
      render json: { errors: @post.errors.full_messages }, status: :unprocessable_entity
    end
  end
end
""") + code("""# config/routes.rb
namespace :api do
  namespace :v1 do
    resources :posts, only: [:index, :show, :create, :update, :destroy]
    resources :users, only: [:show, :create]
  end
end
""") + """
<h2 class="lesson-section-title" id="external-apis">Consuming External APIs</h2>
""" + code("""# Gemfile
gem 'faraday'

# app/services/weather_service.rb
class WeatherService
  BASE_URL = "https://api.openweathermap.org/data/2.5"

  def self.current(city)
    response = Faraday.get("#{BASE_URL}/weather") do |req|
      req.params[:q]     = city
      req.params[:appid] = ENV['OPENWEATHER_API_KEY']
      req.params[:units] = 'metric'
    end
    JSON.parse(response.body)
  end
end

# Use in controller
@weather = WeatherService.current("London")
"""),
    kc=[("How do you version a Rails API?","json-responses"),
        ("What does render json: do?","json-responses"),
        ("What does Faraday provide?","external-apis")],
    assignments=["Build a JSON API for your blog with authentication using JWT or token authentication.","Consume a public API in a Rails app using Faraday."],
    resources=[
        ("Rails Guides — Rails API","https://guides.rubyonrails.org/api_app.html"),
        ("Faraday Gem","https://lostisland.github.io/faraday/"),
        ("YouTube — Build a Rails API (GoRails)","https://www.youtube.com/watch?v=QV53FdaZygA"),
    ])

    w("action-mailer","Action Mailer",
    intro="Action Mailer lets your Rails application send emails — welcome emails, password resets, notifications. It uses the same template system as views.",
    overview=["Generate and configure a mailer.","Render HTML and plain-text email templates.","Send emails from controllers.","Test mailers with RSpec.","Use a background job for email delivery."],
    body="""
<h2 class="lesson-section-title" id="setup">Setup</h2>
""" + code("""# Generate a mailer
rails generate mailer UserMailer

# app/mailers/user_mailer.rb
class UserMailer < ApplicationMailer
  default from: 'noreply@myapp.com'

  def welcome_email(user)
    @user = user
    @login_url = login_url
    mail(to: @user.email, subject: 'Welcome to MyApp!')
  end

  def password_reset(user)
    @user  = user
    @token = user.generate_password_token!
    mail(to: @user.email, subject: 'Reset your password')
  end
end
""") + code("""<!-- app/views/user_mailer/welcome_email.html.erb -->
<h1>Welcome, <%= @user.first_name %>!</h1>
<p>Thanks for joining. <%= link_to "Log in here", @login_url %></p>

<!-- app/views/user_mailer/welcome_email.text.erb -->
Welcome, <%= @user.first_name %>!
Log in at: <%= @login_url %>
""") + code("""# Send from a controller or model
UserMailer.welcome_email(@user).deliver_later   # async via ActiveJob
UserMailer.welcome_email(@user).deliver_now     # synchronous

# config/environments/development.rb
config.action_mailer.delivery_method = :letter_opener  # preview in browser
# gem 'letter_opener', group: :development
"""),
    kc=[("What does deliver_later do?","setup"),
        ("Why provide both HTML and text email templates?","setup"),
        ("What gem previews emails in the browser during development?","setup")],
    assignments=["Add a welcome email to your registration flow.","Add a password reset email flow."],
    resources=[
        ("Rails Guides — Action Mailer","https://guides.rubyonrails.org/action_mailer_basics.html"),
        ("YouTube — Action Mailer (GoRails)","https://www.youtube.com/watch?v=bXV7mqEC3b8"),
    ])

    w("advanced-topics","Advanced Topics",
    intro="This lesson covers the advanced Rails features you will encounter in real applications: background jobs, caching, websockets with Action Cable, and service objects.",
    overview=["Use Active Job for background processing.","Implement caching with fragment and low-level caching.","Use service objects to organise complex business logic.","Understand Action Cable for real-time features."],
    body="""
<h2 class="lesson-section-title" id="active-job">Active Job</h2>
""" + code("""# Generate a job
rails generate job ProcessPayment

# app/jobs/process_payment_job.rb
class ProcessPaymentJob < ApplicationJob
  queue_as :default

  def perform(order_id)
    order = Order.find(order_id)
    PaymentService.charge(order)
    OrderMailer.confirmation(order).deliver_now
  end
end

# Enqueue from anywhere
ProcessPaymentJob.perform_later(order.id)
ProcessPaymentJob.set(wait: 5.minutes).perform_later(order.id)
ProcessPaymentJob.set(wait_until: Date.tomorrow.noon).perform_later(order.id)
""") + """
<h2 class="lesson-section-title" id="service-objects">Service Objects</h2>
""" + code("""# Fat models and controllers are a Rails anti-pattern
# Service objects extract complex business logic into single-responsibility classes

# app/services/user_registration_service.rb
class UserRegistrationService
  def initialize(params)
    @params = params
  end

  def call
    User.transaction do
      user = User.create!(@params)
      UserMailer.welcome_email(user).deliver_later
      Segment.track(user_id: user.id, event: "Signed Up")
      user
    end
  rescue ActiveRecord::RecordInvalid => e
    { error: e.message }
  end
end

# Controller stays thin
def create
  result = UserRegistrationService.new(user_params).call
  if result.is_a?(User)
    redirect_to root_path, notice: "Welcome!"
  else
    flash.now[:error] = result[:error]
    render :new
  end
end
"""),
    kc=[("What problem does Active Job solve?","active-job"),
        ("What is a service object and what problem does it solve?","service-objects"),
        ("What does perform_later do differently from perform_now?","active-job")],
    assignments=["Move your email sending to a background job using perform_later.","Extract complex controller logic into a service object."],
    resources=[
        ("Rails Guides — Active Job","https://guides.rubyonrails.org/active_job_basics.html"),
        ("YouTube — Service Objects (GoRails)","https://www.youtube.com/watch?v=z6LkTF2bH0I"),
    ])

    w("the-asset-pipeline","The Asset Pipeline",
    intro="The asset pipeline compiles, minifies, and fingerprints CSS and JavaScript assets for production. Understanding it helps you organise and optimise your front-end assets.",
    overview=["Understand what the asset pipeline does.","Organise CSS and JavaScript in the app/assets directory.","Use the asset helpers in views.","Understand digest fingerprinting for cache busting."],
    body="""
<h2 class="lesson-section-title" id="what-it-does">What the Asset Pipeline Does</h2>
<ul>
  <li><strong>Concatenation</strong> — combines multiple CSS/JS files into one to reduce HTTP requests</li>
  <li><strong>Minification</strong> — removes whitespace, shortens variable names to reduce file size</li>
  <li><strong>Fingerprinting</strong> — adds a content hash to filenames (e.g. <code>application-abc123.css</code>) so browsers cache aggressively but always get new versions when content changes</li>
  <li><strong>Preprocessing</strong> — compiles Sass to CSS, CoffeeScript to JS (if used)</li>
</ul>
""" + code("""# View helpers automatically use fingerprinted paths
<%= stylesheet_link_tag "application" %>
# => <link href="/assets/application-abc123de.css" rel="stylesheet">

<%= javascript_include_tag "application", defer: true %>
# => <script src="/assets/application-xyz456.js" defer="defer"></script>

<%= image_tag "logo.png" %>
# => <img src="/assets/logo-123abc.png">

# In CSS — reference images
background-image: url('<%= asset_path("pattern.png") %>');
"""),
    kc=[("What three things does the asset pipeline do to assets?","what-it-does"),
        ("What is fingerprinting and why does it help with caching?","what-it-does")],
    assignments=["Add a custom CSS file to the asset pipeline and verify it loads in production mode.","Check the fingerprinted file names in the browser's network tab."],
    resources=[
        ("Rails Guides — Asset Pipeline","https://guides.rubyonrails.org/asset_pipeline.html"),
        ("YouTube — Rails Asset Pipeline (GoRails)","https://www.youtube.com/watch?v=n8-E_OHEsCo"),
    ])

    w("css-bundling","CSS Bundling",
    intro="Modern Rails apps use CSS Bundling or Tailwind CSS instead of (or alongside) the traditional asset pipeline. This lesson covers the options available in Rails 7.",
    overview=["Understand the difference between Sprockets, Propshaft, and jsbundling.","Set up Tailwind CSS in a Rails 7 app.","Set up cssbundling-rails with PostCSS.","Understand importmaps for JavaScript."],
    body="""
<h2 class="lesson-section-title" id="rails7-options">Rails 7 CSS Options</h2>
<ul>
  <li><strong>Sprockets (classic)</strong> — the traditional asset pipeline. Still works, widely understood.</li>
  <li><strong>Propshaft</strong> — modern, simpler replacement for Sprockets. No compilation, just fingerprinting.</li>
  <li><strong>cssbundling-rails</strong> — delegates to an external bundler: PostCSS, Tailwind, Bootstrap, Bulma.</li>
  <li><strong>importmap-rails</strong> — uses browser ES modules for JavaScript, no bundler needed.</li>
</ul>
""" + code("""# Create a new Rails 7 app with Tailwind
rails new myapp --css tailwind --database=postgresql

# Or add Tailwind to existing app
bundle add tailwindcss-rails
rails tailwindcss:install

# Start both Rails server and CSS watcher
bin/dev   # runs Procfile.dev (foreman/overmind)
""") + code("""/* app/assets/stylesheets/application.tailwind.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Custom components */
@layer components {
  .btn-primary {
    @apply bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700;
  }
}
"""),
    kc=[("What does bin/dev do?","rails7-options"),
        ("What is importmap-rails?","rails7-options"),
        ("How do you add custom Tailwind components?","rails7-options")],
    assignments=["Create a Rails 7 app with Tailwind CSS and style your blog app with it.","Explore the importmap for JavaScript."],
    resources=[
        ("Tailwind CSS Rails Gem","https://github.com/rails/tailwindcss-rails"),
        ("Rails Guides — Working with JavaScript","https://guides.rubyonrails.org/working_with_javascript_in_rails.html"),
    ])

    w("installing-postgresql","Installing PostgreSQL",
    intro="PostgreSQL is the recommended database for Rails applications in production. This lesson covers installation, configuration, and switching from SQLite to PostgreSQL.",
    overview=["Install PostgreSQL on your operating system.","Configure database.yml for PostgreSQL.","Create development and test databases.","Use Rails with PostgreSQL-specific features."],
    body="""
<h2 class="lesson-section-title" id="install">Installation</h2>
""" + code("""# macOS (Homebrew)
brew install postgresql@16
brew services start postgresql@16

# Ubuntu / WSL
sudo apt install postgresql postgresql-contrib
sudo service postgresql start

# Create a PostgreSQL user
sudo -u postgres createuser --superuser $USER

# Verify
psql --version
psql -c "SELECT version();"
""") + code("""# config/database.yml
default: &default
  adapter: postgresql
  encoding: unicode
  pool: <%= ENV.fetch("RAILS_MAX_THREADS") { 5 } %>

development:
  <<: *default
  database: myapp_development
  username: <%= ENV['DB_USERNAME'] %>
  password: <%= ENV['DB_PASSWORD'] %>

test:
  <<: *default
  database: myapp_test

production:
  <<: *default
  url: <%= ENV['DATABASE_URL'] %>
""") + code("""# Create databases
rails db:create

# Or using psql directly
createdb myapp_development
createdb myapp_test
"""),
    kc=[("How do you configure Rails to use PostgreSQL?","install"),
        ("Where should database credentials go?","install")],
    assignments=["Install PostgreSQL and configure your Rails app to use it.","Run rails db:create and verify the databases were created."],
    resources=[
        ("PostgreSQL Downloads","https://www.postgresql.org/download/"),
        ("Rails Guides — Configuring Databases","https://guides.rubyonrails.org/configuring.html#configuring-a-database"),
    ])

    w("project-odinbook","Project: Odin-Book",
    intro="The Rails capstone. Build a Facebook-like social network using everything you have learned — authentication, associations, Active Storage for photos, Action Mailer for notifications, and real-time features.",
    overview=["Build a complete social networking application in Rails.","Implement OAuth login with OmniAuth.","Use Active Storage for profile and post images.","Implement friend requests, posts, likes, and a news feed."],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li><strong>Authentication</strong> — sign up, log in, log out, and GitHub/Google OAuth login via OmniAuth</li>
  <li><strong>Profiles</strong> — profile photo (Active Storage), bio, timeline of posts</li>
  <li><strong>Posts</strong> — text and image posts; like and unlike posts</li>
  <li><strong>Comments</strong> — comment on posts</li>
  <li><strong>Friends</strong> — send, accept, reject friend requests; unfriend</li>
  <li><strong>News Feed</strong> — posts from friends and self, newest first</li>
  <li><strong>Notifications</strong> — friend request received (Action Mailer or in-app)</li>
  <li>Deployed on Fly.io, Render, or Heroku</li>
</ul>
""" + code("""rails new odin-book --database=postgresql --css tailwind
cd odin-book

# Key gems
gem 'devise'
gem 'omniauth-github'
gem 'omniauth-google-oauth2'
gem 'image_processing'   # for Active Storage variants
gem 'pagy'               # pagination
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Plan your data model before writing code. Draw the ERD. Get associations right first — they are much harder to change later than views or controllers.</p>
</div>""",
    kc=[("What does OmniAuth provide?","requirements"),
        ("How do you query a news feed of friend posts?","requirements")],
    assignments=["Complete Odin-Book meeting all requirements.","Deploy publicly and add the URL to your portfolio."],
    resources=[
        ("Devise — GitHub","https://github.com/heartcombo/devise"),
        ("OmniAuth — GitHub Strategy","https://github.com/omniauth/omniauth-github"),
        ("YouTube — Social Network in Rails (GoRails)","https://www.youtube.com/watch?v=ByGJQpkQUYE"),
    ])

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
