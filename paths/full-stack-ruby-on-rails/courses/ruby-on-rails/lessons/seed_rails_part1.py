#!/usr/bin/env python3
"""Rails Path — Part 1: Ruby (26 lessons) + Databases (3 lessons)"""
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
    """Escape and wrap a code snippet in a styled block."""
    esc = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<div class="code-block"><pre><code>{esc}</code></pre></div>'


def write(ldir, course_title, all_lessons, sidebar_html, slug,
          title, intro, overview, body, kc, assignments, resources):
    idx = next((i for i, l in enumerate(all_lessons) if l[0] == slug), None)
    p   = (all_lessons[idx - 1][1], all_lessons[idx - 1][0] + ".html") if idx and idx > 0 else None
    n   = (all_lessons[idx + 1][1], all_lessons[idx + 1][0] + ".html") if idx is not None and idx < len(all_lessons) - 1 else None
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


# ══════════════════════════════════════════════════════
#  RUBY COURSE
# ══════════════════════════════════════════════════════

def seed_ruby():
    ldir = os.path.join(RAILS, "ruby", "lessons")
    ALL = [
        ("ruby-intro",                  "Introduction"),
        ("basic-ruby",                  "Basic Ruby"),
        ("sub-strings",                 "Project: Sub Strings"),
        ("stock-picker",                "Project: Stock Picker"),
        ("bubble-sort",                 "Project: Bubble Sort"),
        ("object-oriented-programming", "Object Oriented Programming"),
        ("files-and-serialization",     "Files and Serialization"),
        ("project-event-manager",       "Project: Event Manager"),
        ("project-hangman",             "Project: Hangman"),
        ("pattern-matching",            "Pattern Matching"),
        ("blocks",                      "Blocks"),
        ("project-custom-enumerables",  "Project: Custom Enumerables"),
        ("a-bit-of-computer-science",   "A Bit of Computer Science"),
        ("project-recursion",           "Project: Recursion"),
        ("linked-lists",                "Linked Lists"),
        ("project-linked-lists",        "Project: Linked Lists"),
        ("hash-map",                    "Hash Map"),
        ("project-hashmap",             "Project: HashMap"),
        ("binary-search-trees",         "Binary Search Trees"),
        ("project-binary-search-trees", "Project: Binary Search Trees"),
        ("knights-travails",            "Project: Knights Travails"),
        ("introduction-to-rspec",       "Introduction to RSpec"),
        ("project-caesar-cipher",       "Project: Caesar Cipher"),
        ("project-mastermind",          "Project: Mastermind"),
        ("project-tic-tac-toe",         "Project: Tic Tac Toe"),
        ("project-connect-four",        "Project: Connect Four"),
    ]

    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">Ruby</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">Introduction</div>'
        + lnk("ruby-intro", "Introduction")
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Basic Ruby</div>'
        + lnk("basic-ruby", "Basic Ruby")
        + lnk("sub-strings", "Project: Sub Strings", True)
        + lnk("stock-picker", "Project: Stock Picker", True)
        + lnk("bubble-sort", "Project: Bubble Sort", True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Intermediate Ruby</div>'
        + lnk("object-oriented-programming", "Object Oriented Programming")
        + lnk("files-and-serialization", "Files and Serialization")
        + lnk("project-event-manager", "Project: Event Manager", True)
        + lnk("project-hangman", "Project: Hangman", True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Advanced Ruby</div>'
        + lnk("pattern-matching", "Pattern Matching")
        + lnk("blocks", "Blocks")
        + lnk("project-custom-enumerables", "Project: Custom Enumerables", True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Computer Science</div>'
        + lnk("a-bit-of-computer-science", "A Bit of Computer Science")
        + lnk("project-recursion", "Project: Recursion", True)
        + lnk("linked-lists", "Linked Lists")
        + lnk("project-linked-lists", "Project: Linked Lists", True)
        + lnk("hash-map", "Hash Map")
        + lnk("project-hashmap", "Project: HashMap", True)
        + lnk("binary-search-trees", "Binary Search Trees")
        + lnk("project-binary-search-trees", "Project: Binary Search Trees", True)
        + lnk("knights-travails", "Project: Knights Travails", True)
        + '</div><div class="sidebar-section"><div class="sidebar-section-label">Testing with RSpec</div>'
        + lnk("introduction-to-rspec", "Introduction to RSpec")
        + lnk("project-caesar-cipher", "Project: Caesar Cipher", True)
        + lnk("project-mastermind", "Project: Mastermind", True)
        + lnk("project-tic-tac-toe", "Project: Tic Tac Toe", True)
        + lnk("project-connect-four", "Project: Connect Four", True)
        + '</div></aside>'
    )

    def w(slug, title, intro, overview, body, kc, assignments, resources):
        write(ldir, "Ruby", ALL, sidebar, slug, title, intro, overview, body, kc, assignments, resources)

    # ── ruby-intro ────────────────────────────────────────
    w("ruby-intro", "Introduction",
      intro="Ruby is an elegant, expressive programming language designed for developer happiness. Created by Yukihiro Matsumoto in 1995, Ruby powers the Rails web framework and is celebrated for code that reads like natural English.",
      overview=[
          "Understand what Ruby is and why it was created.",
          "Know how Ruby differs from JavaScript.",
          "Install Ruby and run your first Ruby program.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="what-is-ruby">What Is Ruby?</h2>'
          "<p>Ruby is a dynamically typed, object-oriented language built around the principle of least surprise — code should behave the way you expect. Everything in Ruby is an object, including numbers, strings, and even nil.</p>"
          "<p>Ruby's main claim to fame in web development is <strong>Ruby on Rails</strong>, a framework that pioneered conventions like convention-over-configuration and the MVC pattern — ideas that influenced nearly every web framework that followed.</p>"
          '<h2 class="lesson-section-title" id="install">Installing Ruby</h2>'
          + code("""\
# Install rbenv (Ruby version manager — like nvm for Node)
# macOS / Linux / WSL
brew install rbenv ruby-build   # macOS
sudo apt install rbenv          # Ubuntu/WSL
# Install Ruby
rbenv install 3.3.0
rbenv global 3.3.0
# Verify
ruby --version    # ruby 3.3.0
irb               # Interactive Ruby shell (like node REPL)
""")
          + '<h2 class="lesson-section-title" id="first-program">Your First Ruby Program</h2>'
          + code("""\
# hello.rb
puts "Hello, World!"
puts 2 + 3
puts "Ruby".upcase
puts [1, 2, 3].sum
# Run it
# ruby hello.rb
""")
          + '<h2 class="lesson-section-title" id="ruby-vs-js">Ruby vs. JavaScript</h2>'
          + code("""\
# JavaScript           # Ruby equivalent
const x = 5;           x = 5
let name = "Alice"     name = "Alice"
console.log(name)      puts name
// comment             # comment
arr.forEach(...)       arr.each { |item| ... }
arr.map(...)           arr.map { |item| ... }
arr.filter(...)        arr.select { |item| ... }
null                   nil
true / false           true / false
""")
      ),
      kc=[
          ("What principle guided Ruby's design?", "what-is-ruby"),
          ("What is the Ruby equivalent of console.log?", "first-program"),
          ("What is rbenv used for?", "install"),
      ],
      assignments=[
          "Install Ruby with rbenv and verify with ruby --version.",
          "Open irb and experiment with basic expressions.",
      ],
      resources=[
          ("Ruby Official Documentation", "https://ruby-doc.org/"),
          ("rbenv — GitHub", "https://github.com/rbenv/rbenv"),
          ("YouTube — Ruby Programming Language (freeCodeCamp)", "https://www.youtube.com/watch?v=t_ispmWmdjY"),
      ])

    # ── basic-ruby ────────────────────────────────────────
    w("basic-ruby", "Basic Ruby",
      intro="Ruby's syntax is clean and readable. This lesson covers the fundamentals — variables, data types, conditionals, loops, and methods — the building blocks of every Ruby program.",
      overview=[
          "Use Ruby's core data types: String, Integer, Float, Boolean, nil, Symbol, Array, Hash.",
          "Write conditionals with if, unless, and case.",
          "Loop with each, times, while, and until.",
          "Define and call methods.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="data-types">Data Types</h2>'
          + code("""\
# Strings
name = "Alice"
greeting = 'Hello, World!'
interpolated = "Hello, #{name}!"   # string interpolation — use double quotes
# Numbers
age     = 28          # Integer
price   = 9.99        # Float
big_num = 1_000_000   # underscores for readability
# Booleans and nil
logged_in = true
value     = nil       # Ruby's null
# Symbols — immutable, lightweight identifiers
status = :active
role   = :admin
# Arrays
fruits  = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed   = [1, "hello", :symbol, nil]
# Hashes (like JS objects)
user = { name: "Alice", age: 28, role: :admin }
user[:name]     # => "Alice"
user[:email]    # => nil (no error for missing key)
""")
          + '<h2 class="lesson-section-title" id="conditionals">Conditionals</h2>'
          + code("""\
# if / elsif / else
if score >= 90
  puts "A grade"
elsif score >= 80
  puts "B grade"
else
  puts "Below B"
end
# unless — opposite of if
unless logged_in
  redirect_to login_path
end
# One-line conditionals
puts "Welcome!" if logged_in
puts "Please log in" unless logged_in
# Ternary
label = score >= 60 ? "Pass" : "Fail"
# case / when
case role
when :admin
  puts "Full access"
when :member
  puts "Limited access"
else
  puts "No access"
end
""")
          + '<h2 class="lesson-section-title" id="loops">Loops and Iteration</h2>'
          + code("""\
# .each — most common loop in Ruby
[1, 2, 3].each do |num|
  puts num * 2
end
# One-line block syntax
[1, 2, 3].each { |num| puts num }
# .times
5.times { |i| puts "Iteration #{i}" }
# .upto / .downto
1.upto(5)   { |i| puts i }
5.downto(1) { |i| puts i }
# while / until
count = 0
while count < 5
  puts count
  count += 1
end
""")
          + '<h2 class="lesson-section-title" id="methods">Methods</h2>'
          + code("""\
# Define a method
def greet(name, greeting = "Hello")
  "#{greeting}, #{name}!"    # last expression is returned automatically
end
puts greet("Alice")          # "Hello, Alice!"
puts greet("Bob", "Hi")      # "Hi, Bob!"
# Methods with a block parameter
def repeat(n)
  n.times { yield }          # yield calls the block
end
repeat(3) { puts "Hello!" }  # prints Hello! three times
# Useful built-in methods
"hello".upcase               # "HELLO"
"WORLD".downcase             # "world"
"  spaces  ".strip           # "spaces"
"hello world".split          # ["hello", "world"]
[1,2,3].include?(2)          # true
[3,1,2].sort                 # [1,2,3]
[1,2,3].reverse              # [3,2,1]
{ a: 1 }.keys                # [:a]
{ a: 1 }.values              # [1]
""")
      ),
      kc=[
          ("What is a Ruby Symbol and how does it differ from a String?", "data-types"),
          ("What does unless mean?", "conditionals"),
          ("What does the last expression in a Ruby method do?", "methods"),
      ],
      assignments=[
          "In irb, experiment with all data types and built-in methods listed above.",
          "Write a method that takes an array of numbers and returns their average.",
      ],
      resources=[
          ("Ruby Docs — Core API", "https://ruby-doc.org/core/"),
          ("Learn Ruby the Hard Way", "https://learnrubythehardway.org/"),
          ("YouTube — Ruby Basics (Traversy Media)", "https://www.youtube.com/watch?v=t_ispmWmdjY"),
      ])

    # ── sub-strings ───────────────────────────────────────
    w("sub-strings", "Project: Sub Strings",
      intro="Your first Ruby project. Check whether a word contains any dictionary substrings. A small but complete problem that practices string manipulation and hash usage.",
      overview=[
          "Iterate over an array of dictionary words.",
          "Check string containment with String#include?.",
          "Return a hash of matched words and their count.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="requirements">Requirements</h2>'
          "<p>Write a method <code>substrings</code> that takes a word and an array of valid substrings, and returns a hash listing each substring found (case-insensitive) and how many times it appears.</p>"
          + code("""\
dictionary = ["below", "down", "go", "going", "horn", "how", "howdy",
             "it", "i", "low", "own", "part", "partner", "sit"]
substrings("below", dictionary)
# => { "below" => 1, "low" => 1 }
substrings("Howdy partner, sit down! How's it going?", dictionary)
# => { "down" => 1, "go" => 1, "going" => 1, "how" => 2,
#      "howdy" => 1, "it" => 2, "i" => 3, "own" => 1,
#      "part" => 1, "partner" => 1, "sit" => 1 }
""")
          + code("""\
# Starting point
def substrings(string, dictionary)
  result = {}
  # your code here
  result
end
""")
      ),
      kc=[
          ("How do you check if a string contains a substring in Ruby?", "requirements"),
          ("How do you increment a hash value with a default of 0?", "requirements"),
      ],
      assignments=[
          "Complete the substrings method.",
          "Write tests for edge cases: empty string, no matches, case sensitivity.",
      ],
      resources=[
          ("Ruby Docs — String#include?", "https://ruby-doc.org/core/String.html#method-i-include-3F"),
          ("Ruby Docs — Hash#fetch", "https://ruby-doc.org/core/Hash.html"),
      ])

    # ── stock-picker ──────────────────────────────────────
    w("stock-picker", "Project: Stock Picker",
      intro="Find the best day to buy and the best day to sell stocks from an array of prices. A classic algorithm problem in Ruby.",
      overview=[
          "Iterate over an array with indices.",
          "Find a maximum value while tracking context.",
          "Return a pair of indices.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="requirements">Requirements</h2>'
          "<p>Write a method <code>stock_picker</code> that takes an array of daily stock prices and returns a pair of indices representing the best buy day and best sell day. The buy day must come before the sell day.</p>"
          + code("""\
stock_picker([17, 3, 6, 9, 15, 8, 6, 1, 10])
# => [1, 4]  (buy on day 1 at price 3, sell on day 4 at price 15)
# Max profit = 15 - 3 = 12
""")
          + code("""\
def stock_picker(prices)
  best_buy  = 0
  best_sell = 1
  max_profit = prices[1] - prices[0]
  # your logic here
  [best_buy, best_sell]
end
""")
      ),
      kc=[
          ("Why must the buy day index be less than the sell day index?", "requirements"),
          ("What is the time complexity of a brute force solution?", "requirements"),
      ],
      assignments=[
          "Complete stock_picker.",
          "Add an edge case check: what if all prices decline?",
      ],
      resources=[
          ("Ruby Docs — Array#each_with_index", "https://ruby-doc.org/core/Array.html#method-i-each_with_index"),
      ])

    # ── bubble-sort ───────────────────────────────────────
    w("bubble-sort", "Project: Bubble Sort",
      intro="Implement bubble sort — a foundational sorting algorithm that teaches iteration, comparisons, and in-place array manipulation.",
      overview=[
          "Understand how bubble sort works.",
          "Implement the sorting algorithm in Ruby.",
          "Analyse its O(n²) time complexity.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="how-it-works">How Bubble Sort Works</h2>'
          "<p>Bubble sort repeatedly steps through the array, compares adjacent elements, and swaps them if they are in the wrong order. The largest unsorted element \"bubbles\" to its correct position each pass.</p>"
          + code("""\
# Target:
bubble_sort([4, 3, 78, 2, 0, 2])
# => [0, 2, 2, 3, 4, 78]
# Do not use Ruby's built-in sort method — implement it manually
def bubble_sort(array)
  # your implementation here
end
""")
          + code("""\
# Hint: track whether any swap occurred
# If a full pass completes with no swaps, the array is sorted
n = array.length
loop do
  swapped = false
  (n - 1).times do |i|
    if array[i] > array[i + 1]
      array[i], array[i + 1] = array[i + 1], array[i]  # Ruby swap
      swapped = true
    end
  end
  break unless swapped
end
""")
      ),
      kc=[
          ("What is the time complexity of bubble sort?", "how-it-works"),
          ("What Ruby syntax performs an in-place swap?", "how-it-works"),
      ],
      assignments=[
          "Implement bubble_sort without using Ruby's sort.",
          "Verify it works on arrays of strings and mixed types.",
      ],
      resources=[
          ("YouTube — Bubble Sort Algorithm (CS Dojo)", "https://www.youtube.com/watch?v=xli_FI7CuzA"),
      ])

    # ── object-oriented-programming ───────────────────────
    w("object-oriented-programming", "Object Oriented Programming",
      intro="Ruby is a fully object-oriented language — everything is an object. This lesson covers classes, inheritance, modules, and Ruby's unique approach to OOP.",
      overview=[
          "Define classes with instance variables and methods.",
          "Use initialize as the constructor.",
          "Implement inheritance with < and super.",
          "Use modules for mixins and namespacing.",
          "Understand attr_accessor, attr_reader, attr_writer.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="classes">Classes</h2>'
          + code("""\
class Person
  attr_accessor :name, :age     # creates getter and setter methods
  attr_reader   :id             # read-only
  @@count = 0                   # class variable — shared by all instances
  def initialize(name, age)
    @name = name                # instance variable
    @age  = age
    @@count += 1
    @id = @@count
  end
  def introduce
    "Hi, I'm #{@name} and I'm #{@age} years old."
  end
  def self.count              # class method
    @@count
  end
end
alice = Person.new("Alice", 28)
bob   = Person.new("Bob",   32)
alice.name           # "Alice"
alice.name = "Alicia"# setter
alice.introduce      # "Hi, I'm Alicia and I'm 28 years old."
Person.count         # 2
""")
          + '<h2 class="lesson-section-title" id="inheritance">Inheritance</h2>'
          + code("""\
class Animal
  attr_reader :name
  def initialize(name)
    @name = name
  end
  def speak
    raise NotImplementedError, "#{self.class} must implement speak"
  end
  def to_s
    "#{self.class.name} named #{@name}"
  end
end
class Dog < Animal
  def speak
    "Woof!"
  end
end
class Cat < Animal
  def speak
    "Meow!"
  end
end
# Polymorphism
[Dog.new("Rex"), Cat.new("Luna")].each do |animal|
  puts "#{animal.name} says #{animal.speak}"
end
""")
          + '<h2 class="lesson-section-title" id="modules">Modules and Mixins</h2>'
          + code("""\
# Modules as mixins — share behaviour across unrelated classes
module Greetable
  def greet
    "Hello, I'm #{name}"       # uses the including class's 'name' method
  end
end
module Farewell
  def farewell
    "Goodbye from #{name}!"
  end
end
class User
  include Greetable
  include Farewell
  attr_reader :name
  def initialize(name)
    @name = name
  end
end
User.new("Alice").greet     # "Hello, I'm Alice"
User.new("Bob").farewell    # "Goodbye from Bob!"
""")
      ),
      kc=[
          ("What does attr_accessor do?", "classes"),
          ("What is the difference between a class method and an instance method?", "classes"),
          ("What is a mixin in Ruby?", "modules"),
      ],
      assignments=[
          "Build a Vehicle class hierarchy: Vehicle base, Car and Motorcycle subclasses, each with different fuel_type and speed.",
          "Add a Describable module that adds a describe method used by all vehicle types.",
      ],
      resources=[
          ("Ruby Docs — Classes and Modules", "https://ruby-doc.org/core/"),
          ("YouTube — Ruby OOP (Traversy Media)", "https://www.youtube.com/watch?v=t_ispmWmdjY"),
      ])

    # ── files-and-serialization ───────────────────────────
    w("files-and-serialization", "Files and Serialization",
      intro="Ruby has excellent built-in support for reading and writing files, and several ways to serialize data — CSV, JSON, and YAML. This lesson covers all three.",
      overview=[
          "Read and write files with File and IO.",
          "Serialize data with JSON and YAML.",
          "Read and write CSV files.",
          "Use Psych for YAML serialization.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="file-io">File I/O</h2>'
          + code("""\
# Write a file
File.write("output.txt", "Hello, World!")
# Read entire file
content = File.read("input.txt")
# Read line by line (memory-efficient for large files)
File.foreach("data.txt") do |line|
  puts line.chomp  # chomp removes trailing newline
end
# Open/close pattern (auto-closes)
File.open("log.txt", "a") do |file|
  file.puts "#{Time.now} — event logged"
end
""")
          + '<h2 class="lesson-section-title" id="json-yaml">JSON and YAML</h2>'
          + code("""\
require 'json'
require 'yaml'
# JSON
data = { name: "Alice", scores: [95, 87, 92] }
json_string = JSON.generate(data)
# or
json_string = data.to_json
# Write to file
File.write("data.json", JSON.pretty_generate(data))
# Read and parse
parsed = JSON.parse(File.read("data.json"))
parsed["name"]   # "Alice" (keys become strings after parsing)
# YAML — more human-readable
yaml_string = data.to_yaml
File.write("data.yml", yaml_string)
loaded = YAML.load_file("data.yml")
loaded[:name]    # "Alice" (symbols preserved)
""")
      ),
      kc=[
          ("What does chomp do?", "file-io"),
          ("What is the difference between JSON and YAML for data serialization?", "json-yaml"),
          ("What does File.open with a block guarantee?", "file-io"),
      ],
      assignments=[
          "Build a program that reads a CSV of student scores, calculates each student's average, and writes the results to a new CSV.",
          "Serialize and deserialize a Ruby hash to both JSON and YAML.",
      ],
      resources=[
          ("Ruby Docs — File", "https://ruby-doc.org/core/File.html"),
          ("Ruby Docs — JSON", "https://ruby-doc.org/stdlib/libdoc/json/rdoc/JSON.html"),
      ])

    # ── project-event-manager ─────────────────────────────
    w("project-event-manager", "Project: Event Manager",
      intro="Process a real-world CSV file of event registrations, look up congressional representatives by zip code, and send personalised form letters. A practical introduction to file I/O and APIs in Ruby.",
      overview=[
          "Parse CSV data with the csv library.",
          "Clean and validate real-world data.",
          "Make API requests with the Google Civic Information API.",
          "Generate personalised output files.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="requirements">Requirements</h2>'
          "<ul>"
          "<li>Read a CSV file of event attendees (name, phone, zip code, date)</li>"
          "<li>Clean phone numbers: strip non-digits, handle wrong-length numbers</li>"
          "<li>Look up each attendee's congressional representative using the Google Civic API</li>"
          "<li>Generate a personalised letter for each attendee using an ERB template</li>"
          "<li>Write each letter to its own output file</li>"
          "</ul>"
          + code("""\
require 'csv'
require 'erb'
contents = CSV.open(
  'event_attendees.csv',
  headers: true,
  header_converters: :symbol
)
contents.each do |row|
  name    = row[:first_name]
  zipcode = row[:zipcode].to_s.rjust(5, "0")  # pad to 5 digits
  puts "#{name} — #{zipcode}"
end
""")
      ),
      kc=[
          ("What does header_converters: :symbol do?", "requirements"),
          ("What does rjust(5, '0') do to a zip code?", "requirements"),
      ],
      assignments=[
          "Complete the Event Manager following the requirements.",
          "Generate at least one personalised letter and verify it looks correct.",
      ],
      resources=[
          ("Ruby Docs — CSV", "https://ruby-doc.org/stdlib/libdoc/csv/rdoc/CSV.html"),
          ("Ruby Docs — ERB", "https://ruby-doc.org/stdlib/libdoc/erb/rdoc/ERB.html"),
      ])

    # ── project-hangman ───────────────────────────────────
    w("project-hangman", "Project: Hangman",
      intro="Build a command-line Hangman game that reads a dictionary file, allows letter guessing, and supports saving and loading game state using serialization.",
      overview=[
          "Build an interactive command-line game.",
          "Read words from a file and pick one randomly.",
          "Save and load game state with Marshal or YAML.",
          "Track guesses and wrong attempts.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="requirements">Requirements</h2>'
          "<ul>"
          "<li>Load a dictionary of words and pick a random word with 5–12 characters</li>"
          "<li>Display the word as underscores, revealing letters as they are guessed</li>"
          "<li>Allow the player to save the game mid-round (type 'save')</li>"
          "<li>Allow loading a saved game at the start</li>"
          "<li>Maximum 8 wrong guesses before game over</li>"
          "</ul>"
          + code("""\
# Saving with YAML
def save_game
  File.write("saved_game.yml", self.to_yaml)
  puts "Game saved!"
end
def self.load_game
  return nil unless File.exist?("saved_game.yml")
  YAML.load_file("saved_game.yml")
end
""")
          + code("""\
mkdir ~/devpath-projects/ruby/hangman
cd ~/devpath-projects/ruby/hangman
# Download google-10000-english-no-swears.txt as your dictionary
touch hangman.rb
""")
      ),
      kc=[
          ("How do you serialize and deserialize a Ruby object with YAML?", "requirements"),
          ("What does Marshal do differently from YAML?", "requirements"),
      ],
      assignments=[
          "Complete Hangman meeting all requirements.",
          "Push to GitHub.",
      ],
      resources=[
          ("Ruby Docs — YAML", "https://ruby-doc.org/stdlib/libdoc/yaml/rdoc/YAML.html"),
          ("Google 10000 English Words", "https://github.com/first20hours/google-10000-english"),
      ])

    # ── pattern-matching ──────────────────────────────────
    w("pattern-matching", "Pattern Matching",
      intro="Ruby 3.x introduced powerful pattern matching — a concise way to match data structures and extract values. It goes far beyond what a simple case/when can do.",
      overview=[
          "Use case/in for pattern matching.",
          "Match arrays, hashes, and nested structures.",
          "Use guard clauses with if in patterns.",
          "Use find patterns and pin operators.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="basic-patterns">Basic Pattern Matching</h2>'
          + code("""\
# case/in instead of case/when
response = { status: 200, body: { user: { name: "Alice", role: :admin } } }
case response
in { status: 200, body: { user: { name: String => name, role: :admin } } }
  puts "Admin user: #{name}"
in { status: 200, body: { user: { name: String => name } } }
  puts "Regular user: #{name}"
in { status: 404 }
  puts "Not found"
in { status: (500..) }
  puts "Server error"
end
# => "Admin user: Alice"
""")
          + '<h2 class="lesson-section-title" id="array-patterns">Array Patterns</h2>'
          + code("""\
case [1, 2, 3]
in [Integer => first, *rest]
  puts "First: #{first}, rest: #{rest}"
  # => "First: 1, rest: [2, 3]"
end
# Find pattern — find subsequence anywhere in array
case [1, 2, "hello", 3, 4]
in [*, String => s, *]
  puts "Found string: #{s}"   # "Found string: hello"
end
""")
          + '<h2 class="lesson-section-title" id="pin-operator">Pin Operator</h2>'
          + code("""\
expected = 42
case { value: 42 }
in { value: ^expected }   # ^ pins to existing variable
  puts "Got the expected value"
end
""")
      ),
      kc=[
          ("How does case/in differ from case/when?", "basic-patterns"),
          ("What does the pin operator ^ do?", "pin-operator"),
          ("What is a find pattern used for?", "array-patterns"),
      ],
      assignments=[
          "Refactor a previous project's case/when statements to use case/in where appropriate.",
          "Write a method that uses pattern matching to parse API responses with different structures.",
      ],
      resources=[
          ("Ruby Docs — Pattern Matching", "https://docs.ruby-lang.org/en/master/syntax/pattern_matching_rdoc.html"),
          ("YouTube — Ruby Pattern Matching", "https://www.youtube.com/watch?v=AyxBBqo79Ak"),
      ])

    # ── blocks ────────────────────────────────────────────
    w("blocks", "Blocks",
      intro="Blocks are Ruby's anonymous functions — they are everywhere in Ruby code. Understanding blocks, Procs, and lambdas is essential for writing idiomatic Ruby.",
      overview=[
          "Understand what a block is and how yield works.",
          "Convert blocks to Procs with &block.",
          "Understand the difference between Procs and Lambdas.",
          "Use closures in Ruby.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="blocks-yield">Blocks and yield</h2>'
          + code("""\
# A block is code passed to a method between do..end or { }
[1, 2, 3].each do |n|
  puts n * 2
end
# Passing a block to your own method
def greet
  puts "Before greeting"
  yield("Alice") if block_given?
  puts "After greeting"
end
greet { |name| puts "Hello, #{name}!" }
# => Before greeting
# => Hello, Alice!
# => After greeting
""")
          + '<h2 class="lesson-section-title" id="procs-lambdas">Procs and Lambdas</h2>'
          + code("""\
# Proc — block saved as an object
double = Proc.new { |n| n * 2 }
double.call(5)    # => 10
double.(5)        # => 10 (shorthand)
# Lambda — stricter Proc
square = lambda { |n| n ** 2 }
square = ->(n) { n ** 2 }   # stabby lambda syntax
square.call(4)    # => 16
# Key differences:
# 1. Lambda checks argument count strictly — Proc does not
# 2. return in a Lambda returns from the lambda
#    return in a Proc returns from the ENCLOSING method
# Convert method to block with &
[1, 2, 3].map(&method(:puts))   # calls puts on each element
# Store block parameter
def run_later(&block)
  @saved_block = block
end
run_later { puts "Running!" }
@saved_block.call   # => "Running!"
""")
      ),
      kc=[
          ("What does yield do?", "blocks-yield"),
          ("What is the difference between a Proc and a Lambda?", "procs-lambdas"),
          ("What does block_given? check?", "blocks-yield"),
      ],
      assignments=[
          "Write a method that takes a block and calls it three times with different arguments.",
          "Reimplement Ruby's map method using yield.",
      ],
      resources=[
          ("Ruby Docs — Proc", "https://ruby-doc.org/core/Proc.html"),
          ("YouTube — Ruby Blocks, Procs and Lambdas", "https://www.youtube.com/watch?v=LL0DGc5pg7A"),
      ])

    # ── project-custom-enumerables ────────────────────────
    w("project-custom-enumerables", "Project: Custom Enumerables",
      intro="Implement your own versions of Ruby's Enumerable methods. This deepens your understanding of blocks, iteration, and how Ruby's most-used library works under the hood.",
      overview=[
          "Implement my_each, my_map, my_select, my_all?, my_any?, my_count, my_flatten, my_zip.",
          "Use yield and blocks throughout.",
          "Match the behaviour of Ruby's built-in Enumerable methods.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="requirements">Requirements</h2>'
          "<p>Extend the Enumerable module with custom implementations. Each method must accept a block and behave identically to the built-in version.</p>"
          + code("""\
module Enumerable
  def my_each
    # your implementation — yield each element
  end
  def my_map
    result = []
    my_each { |el| result << yield(el) }
    result
  end
  def my_select
    result = []
    my_each { |el| result << el if yield(el) }
    result
  end
  def my_all?
    my_each { |el| return false unless yield(el) }
    true
  end
  def my_any?
    my_each { |el| return true if yield(el) }
    false
  end
end
# Test
[1, 2, 3, 4, 5].my_map    { |n| n * 2 }    # => [2, 4, 6, 8, 10]
[1, 2, 3, 4, 5].my_select { |n| n.even? }  # => [2, 4]
[1, 2, 3].my_all?          { |n| n > 0 }   # => true
""")
      ),
      kc=[
          ("How does my_each use yield?", "requirements"),
          ("Why does my_all? return false early?", "requirements"),
      ],
      assignments=[
          "Implement all eight methods listed above.",
          "Write RSpec tests verifying your methods match Ruby's built-in behaviour.",
      ],
      resources=[
          ("Ruby Docs — Enumerable", "https://ruby-doc.org/core/Enumerable.html"),
      ])

    # ── Computer Science lessons (shared template) ────────
    cs_lessons = [
        ("a-bit-of-computer-science", "A Bit of Computer Science",
         "This lesson introduces computer science fundamentals in the context of Ruby — recursion, data structures, and algorithm analysis."),
        ("project-recursion", "Project: Recursion",
         "Implement classic recursive algorithms in Ruby: Fibonacci, merge sort, and flatten."),
        ("linked-lists", "Linked Lists",
         "Build a LinkedList class in Ruby using nodes and pointers."),
        ("project-linked-lists", "Project: Linked Lists",
         "Build a complete tested LinkedList implementation in Ruby."),
        ("hash-map", "Hash Map",
         "Implement a HashMap from scratch in Ruby."),
        ("project-hashmap", "Project: HashMap",
         "Build a complete HashMap with collision handling in Ruby."),
        ("binary-search-trees", "Binary Search Trees",
         "Implement a Binary Search Tree in Ruby."),
        ("project-binary-search-trees", "Project: Binary Search Trees",
         "Build a complete, balanced BST implementation in Ruby."),
        ("knights-travails", "Project: Knights Travails",
         "Find the shortest path for a chess knight using BFS in Ruby."),
    ]
    for slug, title, lang_note in cs_lessons:
        w(slug, title,
          intro=lang_note + " The concepts are identical to the JavaScript versions — only the syntax changes.",
          overview=[
              f"Implement {title} in Ruby.",
              "Apply Ruby idioms: blocks, Enumerable methods, and clean OOP.",
              "Write RSpec tests for your implementation.",
          ],
          body=(
              f'<h2 class="lesson-section-title" id="overview">Ruby Implementation</h2>'
              f"<p>The concepts for {title} are covered in depth in the Full Stack JavaScript path. This lesson focuses on implementing the same structures and algorithms using Ruby's syntax and idioms.</p>"
              + code("""\
# Ruby syntax reminders for implementing data structures
# Class with initialize
class Node
  attr_accessor :value, :next_node
  def initialize(value)
    @value = value
    @next_node = nil
  end
end
# Comparable mixin — adds <, >, ==, between?
class TreeNode
  include Comparable
  attr_accessor :value, :left, :right
  def <=>(other)
    value <=> other.value
  end
end
# Recursion in Ruby
def factorial(n)
  return 1 if n <= 1
  n * factorial(n - 1)
end
# BFS with a queue
def bfs(root)
  queue = [root]
  until queue.empty?
    node = queue.shift
    yield node
    queue << node.left  if node.left
    queue << node.right if node.right
  end
end
""")
          ),
          kc=[
              (f"How do you implement {title} in Ruby?", "overview"),
              ("What Ruby idiom replaces manual iteration in most cases?", "overview"),
          ],
          assignments=[
              f"Implement {title} in Ruby following the same requirements as the JavaScript version.",
              "Write RSpec tests covering normal cases and edge cases.",
          ],
          resources=[
              ("Ruby Docs — Comparable", "https://ruby-doc.org/core/Comparable.html"),
              ("YouTube — Data Structures in Ruby", "https://www.youtube.com/watch?v=t_ispmWmdjY"),
          ])

    # ── introduction-to-rspec ─────────────────────────────
    w("introduction-to-rspec", "Introduction to RSpec",
      intro="RSpec is Ruby's behaviour-driven testing framework. Its readable syntax lets you write tests that describe what your code should do in plain English.",
      overview=[
          "Install and configure RSpec.",
          "Write describe, context, and it blocks.",
          "Use expect with matchers.",
          "Use before and let for setup.",
          "Practise TDD with RSpec.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="setup">Setup</h2>'
          + code("""\
# Install
gem install rspec
# Or in a project (Gemfile)
gem 'rspec', group: :development
bundle install
rspec --init   # creates .rspec and spec/ directory
""")
          + '<h2 class="lesson-section-title" id="writing-tests">Writing Tests</h2>'
          + code("""\
# spec/calculator_spec.rb
require_relative '../calculator'
RSpec.describe Calculator do
  describe '#add' do
    it 'adds two positive numbers' do
      calc = Calculator.new
      expect(calc.add(2, 3)).to eq(5)
    end
    it 'handles negative numbers' do
      calc = Calculator.new
      expect(calc.add(-1, -2)).to eq(-3)
    end
  end
  describe '#divide' do
    it 'raises an error when dividing by zero' do
      calc = Calculator.new
      expect { calc.divide(10, 0) }.to raise_error(ArgumentError)
    end
  end
end
""")
          + '<h2 class="lesson-section-title" id="matchers">Common Matchers</h2>'
          + code("""\
expect(result).to eq(5)             # equality
expect(result).to be > 3            # comparison
expect(result).to be_nil            # nil check
expect(result).to be_truthy         # truthy
expect(array).to include(3)         # inclusion
expect(array).to have_attributes(name: "Alice")
expect { code }.to raise_error      # exception
expect { code }.to change { count }.by(1)
# DRY setup with let and before
RSpec.describe User do
  let(:user) { User.new("Alice", 28) }  # lazy — only created when used
  before(:each) do                       # runs before every example
    @db = TestDatabase.new
  end
end
""")
          + code("""\
# Run tests
rspec                         # all tests
rspec spec/calculator_spec.rb # one file
rspec --format documentation  # verbose output
""")
      ),
      kc=[
          ("What is the structure of an RSpec test?", "writing-tests"),
          ("What is the difference between let and before?", "matchers"),
          ("What matcher checks that code raises an exception?", "matchers"),
      ],
      assignments=[
          "Write RSpec tests for your bubble sort implementation.",
          "Write RSpec tests for your LinkedList class.",
      ],
      resources=[
          ("RSpec Documentation", "https://rspec.info/documentation/"),
          ("YouTube — RSpec Tutorial (Traversy Media)", "https://www.youtube.com/watch?v=71eKcNxwxVY"),
      ])

    # ── Final project lessons (shared template) ───────────
    final_projects = [
        ("project-caesar-cipher", "Project: Caesar Cipher",
         "Implement a Caesar cipher that encodes and decodes messages by shifting letters. Test with RSpec."),
        ("project-mastermind", "Project: Mastermind",
         "Build a command-line Mastermind game with computer code generation, player guessing, and hint display."),
        ("project-tic-tac-toe", "Project: Tic Tac Toe",
         "Build a two-player command-line Tic Tac Toe game with win detection and draw detection."),
        ("project-connect-four", "Project: Connect Four",
         "Build a command-line Connect Four game with a 6x7 board, win detection for rows, columns, and diagonals."),
    ]
    for slug, title, description in final_projects:
        dir_name = slug.replace("project-", "").replace("-", "_")
        w(slug, title,
          intro=description + " This project practices OOP, file organisation, and RSpec testing.",
          overview=[
              "Design the game using OOP principles.",
              "Separate game logic from display logic.",
              "Write comprehensive RSpec tests.",
              "Handle all edge cases and invalid input.",
          ],
          body=(
              '<h2 class="lesson-section-title" id="requirements">Requirements</h2>'
              f"<p>{description}</p>"
              "<ul>"
              "<li>Clean object-oriented design with separate classes for game logic and display</li>"
              "<li>All game logic covered by RSpec tests</li>"
              "<li>Handles invalid input gracefully</li>"
              "<li>Clear, readable code following Ruby conventions</li>"
              "</ul>"
              + code(f"""\
mkdir ~/devpath-projects/ruby/{slug.replace('project-', '')}
cd ~/devpath-projects/ruby/{slug.replace('project-', '')}
git init
rspec --init
touch lib/{dir_name}.rb
""")
          ),
          kc=[
              ("What classes does this game need?", "requirements"),
              ("What RSpec tests cover win detection?", "requirements"),
          ],
          assignments=[
              f"Complete {title} meeting all requirements.",
              "Achieve full test coverage for game logic.",
              "Push to GitHub.",
          ],
          resources=[
              ("RSpec Documentation", "https://rspec.info/documentation/"),
              ("Ruby Style Guide", "https://rubystyle.guide/"),
          ])

    print(f"  Ruby: {len(ALL)} lessons done")


# ══════════════════════════════════════════════════════
#  DATABASES COURSE
# ══════════════════════════════════════════════════════

def seed_databases():
    ldir = os.path.join(RAILS, "databases", "lessons")
    ALL = [
        ("databases-intro",       "Introduction to Databases"),
        ("databases-and-sql",     "Databases and SQL"),
        ("project-sql-exercises", "Project: SQL Exercises"),
    ]

    def lnk(sl, ti):
        return f'<a href="{sl}.html" class="sidebar-link">{ti}</a>\n'

    sidebar = (
        '<aside class="sidebar"><div class="sidebar-course-title">Databases</div>'
        '<div class="sidebar-section"><div class="sidebar-section-label">SQL</div>'
        + lnk("databases-intro", "Introduction to Databases")
        + lnk("databases-and-sql", "Databases and SQL")
        + lnk("project-sql-exercises", "Project: SQL Exercises")
        + '</div></aside>'
    )

    def w(slug, title, intro, overview, body, kc, assignments, resources):
        write(ldir, "Databases", ALL, sidebar, slug, title, intro, overview, body, kc, assignments, resources)

    # ── databases-intro ───────────────────────────────────
    w("databases-intro", "Introduction to Databases",
      intro="Before building Rails applications with databases, you need to understand what relational databases are, how they organise data, and why they are the backbone of almost every web application.",
      overview=[
          "Understand what a relational database is.",
          "Know the difference between SQL and NoSQL.",
          "Understand tables, rows, columns, primary keys, and foreign keys.",
          "Understand database relationships: one-to-one, one-to-many, many-to-many.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="what-is-rdb">Relational Databases</h2>'
          "<p>A relational database stores data in <strong>tables</strong> — structured grids of rows and columns. Tables can be related to each other through <strong>foreign keys</strong>, allowing complex data to be stored efficiently without duplication.</p>"
          '<h2 class="lesson-section-title" id="relationships">Database Relationships</h2>'
          + code("""\
-- One-to-many: a user has many posts
-- users table              posts table
-- id | name                id | title | user_id
-- 1  | Alice               1  | Hello | 1
-- 2  | Bob                 2  | World | 1
--                          3  | Ruby! | 2
-- Many-to-many: posts have many tags, tags have many posts
-- Requires a join table
-- posts_tags
-- post_id | tag_id
-- 1       | 1
-- 1       | 2
-- 2       | 1
""")
          + '<h2 class="lesson-section-title" id="keys">Primary and Foreign Keys</h2>'
          + code("""\
-- Primary key: unique identifier for each row
CREATE TABLE users (
  id         SERIAL PRIMARY KEY,
  name       VARCHAR(100) NOT NULL,
  email      VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
-- Foreign key: references the primary key of another table
CREATE TABLE posts (
  id         SERIAL PRIMARY KEY,
  title      VARCHAR(200) NOT NULL,
  body       TEXT,
  user_id    INTEGER REFERENCES users(id) ON DELETE CASCADE
);
""")
      ),
      kc=[
          ("What is a primary key?", "keys"),
          ("What is a foreign key?", "keys"),
          ("What are the three types of database relationships?", "relationships"),
      ],
      assignments=[
          "Design a database schema for a blog with users, posts, comments, and tags.",
          "Draw an entity-relationship diagram (ERD) for your schema.",
      ],
      resources=[
          ("MDN — Introduction to Databases", "https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Website_security"),
          ("YouTube — Database Design (Caleb Curry)", "https://www.youtube.com/watch?v=ztHopE5Wnpc"),
      ])

    # ── databases-and-sql ─────────────────────────────────
    w("databases-and-sql", "Databases and SQL",
      intro="SQL is the language of relational databases. This lesson covers the queries you will use constantly in Rails applications, and how to connect PostgreSQL to a Ruby program.",
      overview=[
          "Write SELECT, INSERT, UPDATE, DELETE queries.",
          "Use WHERE, JOIN, ORDER BY, GROUP BY, and HAVING.",
          "Aggregate data with COUNT, SUM, AVG, MIN, MAX.",
          "Connect to PostgreSQL from Ruby with the pg gem.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="core-queries">Core SQL Queries</h2>'
          + code("""\
-- SELECT with filtering and sorting
SELECT * FROM users WHERE active = true ORDER BY name ASC;
SELECT name, email FROM users WHERE created_at > '2024-01-01';
-- JOINs
SELECT users.name, posts.title
FROM posts
INNER JOIN users ON posts.user_id = users.id
WHERE posts.published = true;
-- Aggregation
SELECT users.name, COUNT(posts.id) AS post_count
FROM users
LEFT JOIN posts ON posts.user_id = users.id
GROUP BY users.id, users.name
HAVING COUNT(posts.id) > 3
ORDER BY post_count DESC;
-- INSERT
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
-- UPDATE
UPDATE users SET name = 'Alicia' WHERE id = 1;
-- DELETE
DELETE FROM posts WHERE published = false AND created_at < NOW() - INTERVAL '30 days';
""")
          + '<h2 class="lesson-section-title" id="ruby-pg">PostgreSQL in Ruby</h2>'
          + code("""\
# gem install pg
require 'pg'
conn = PG.connect(dbname: 'myapp_development')
# Safe parameterised query — prevents SQL injection
result = conn.exec_params(
  'SELECT * FROM users WHERE email = $1',
  ['alice@example.com']
)
result.each do |row|
  puts row['name']
end
conn.close
""")
      ),
      kc=[
          ("What is the difference between INNER JOIN and LEFT JOIN?", "core-queries"),
          ("What does GROUP BY do?", "core-queries"),
          ("Why use parameterised queries?", "ruby-pg"),
      ],
      assignments=[
          "Install PostgreSQL. Create a database and practice all queries above.",
          "Connect to PostgreSQL from a Ruby script and run a SELECT query.",
      ],
      resources=[
          ("PostgreSQL Tutorial", "https://www.postgresqltutorial.com/"),
          ("SQLZoo", "https://sqlzoo.net/"),
          ("YouTube — SQL Tutorial (freeCodeCamp)", "https://www.youtube.com/watch?v=qw--VYLpxG4"),
      ])

    # ── project-sql-exercises ─────────────────────────────
    w("project-sql-exercises", "Project: SQL Exercises",
      intro="Practice makes perfect with SQL. This project guides you through a series of increasingly complex queries on a provided database schema.",
      overview=[
          "Write queries covering all major SQL clauses.",
          "Use JOINs across multiple tables.",
          "Write subqueries and CTEs.",
          "Optimise slow queries with EXPLAIN.",
      ],
      body=(
          '<h2 class="lesson-section-title" id="schema">Practice Schema</h2>'
          + code("""\
-- Set up this schema and populate it with seed data
CREATE TABLE students (id SERIAL PRIMARY KEY, name VARCHAR(100), grade INTEGER);
CREATE TABLE courses  (id SERIAL PRIMARY KEY, title VARCHAR(200), credits INTEGER);
CREATE TABLE enrollments (
  student_id INTEGER REFERENCES students(id),
  course_id  INTEGER REFERENCES courses(id),
  grade      CHAR(1),
  PRIMARY KEY (student_id, course_id)
);
""")
          + '<h2 class="lesson-section-title" id="exercises">Exercises</h2>'
          "<ol>"
          "<li>List all students enrolled in more than 2 courses</li>"
          "<li>Find the average grade per course</li>"
          "<li>List students who have not enrolled in any course</li>"
          "<li>Find the most popular course by enrollment count</li>"
          "<li>List students with a GPA above the class average</li>"
          "<li>Find courses with no failing students (grade != 'F')</li>"
          "<li>Rank students by total credits earned</li>"
          "</ol>"
          + code("""\
-- Example: Exercise 3 — students with no enrollments
SELECT students.name
FROM students
LEFT JOIN enrollments ON students.id = enrollments.student_id
WHERE enrollments.student_id IS NULL;
""")
      ),
      kc=[
          ("How do you find rows with no matching join?", "exercises"),
          ("What is a CTE and when is it useful?", "exercises"),
      ],
      assignments=[
          "Complete all seven exercises.",
          "Add EXPLAIN ANALYZE to one query and interpret the output.",
      ],
      resources=[
          ("SQLZoo — Interactive Exercises", "https://sqlzoo.net/"),
          ("PGExercises", "https://pgexercises.com/"),
      ])

    print(f"  Databases: {len(ALL)} lessons done")


def main():
    seed_ruby()
    seed_databases()
    print("\nPart 1 complete. Committing...")
    os.chdir(BASE)
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", "Seed Rails path Part 1: Ruby (26) + Databases (3)"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Pushed.")


if __name__ == "__main__":
    main()
