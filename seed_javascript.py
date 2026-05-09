#!/usr/bin/env python3
"""Seed: JavaScript course — Full Stack JavaScript path"""
import os, subprocess

BASE   = os.path.expanduser("~/devpath")
COURSE = os.path.join(BASE, "paths", "full-stack-javascript", "courses", "javascript")
LDIR   = os.path.join(COURSE, "lessons")
ROOT   = "../../../../../"

ALL_LESSONS = [
    ("javascript-intro",                         "Introduction"),
    ("a-quick-review",                           "A Quick Review"),
    ("organizing-js-intro",                      "Organizing Your JavaScript Code Introduction"),
    ("objects-and-constructors",                 "Objects and Object Constructors"),
    ("project-library",                          "Project: Library"),
    ("factory-functions-and-the-module-pattern", "Factory Functions and the Module Pattern"),
    ("classes",                                  "Classes"),
    ("es6-modules",                              "ES6 Modules"),
    ("webpack",                                  "Webpack"),
    ("project-restaurant-page",                  "Project: Restaurant Page"),
    ("oop-principles",                           "OOP Principles"),
    ("project-todo-list",                        "Project: Todo List"),
    ("linting",                                  "Linting"),
    ("dynamic-user-interface-interactions",      "Dynamic User Interface Interactions"),
    ("form-validation-with-javascript",          "Form Validation with JavaScript"),
    ("what-is-es6",                              "What is ES6?"),
    ("json",                                     "JSON"),
    ("asynchronous-code",                        "Asynchronous Code"),
    ("working-with-apis",                        "Working with APIs"),
    ("async-and-await",                          "Async and Await"),
    ("project-weather-app",                      "Project: Weather App"),
    ("testing-basics",                           "Testing Basics"),
    ("more-testing",                             "More Testing"),
    ("project-battleship",                       "Project: Battleship"),
    ("a-deeper-look-at-git",                     "A Deeper Look at Git"),
    ("working-with-remotes",                     "Working with Remotes"),
    ("using-git-in-the-real-world",              "Using Git in the Real World"),
    ("project-javascript-final",                 "Project: JavaScript Final Project"),
    ("recursion",                                "Recursion"),
    ("project-fibonacci",                        "Project: Fibonacci"),
    ("time-complexity",                          "Time Complexity"),
    ("space-complexity",                         "Space Complexity"),
    ("common-data-structures",                   "Common Data Structures and Algorithms"),
    ("linked-lists",                             "Linked Lists"),
    ("project-linked-lists",                     "Project: Linked Lists"),
    ("hash-map",                                 "Hash Map"),
    ("project-hashmap",                          "Project: HashMap"),
    ("binary-search-trees",                      "Binary Search Trees"),
    ("project-binary-search-trees",              "Project: Binary Search Trees"),
    ("knights-travails",                         "Project: Knights Travails"),
]

LOGO = '<svg viewBox="0 0 28 28" fill="none"><circle cx="14" cy="14" r="13" stroke="currentColor" stroke-width="1.8"/><path d="M8 14 L14 7 L20 14 L14 21 Z" fill="currentColor"/></svg>'

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

def sidebar(active):
    def lnk(sl, ti, proj=False):
        cls = "sidebar-link" + (" is-project" if proj else "") + (" active" if sl == active else "")
        return f'<a href="{sl}.html" class="{cls}">{ti}</a>\n'
    sections = [
        ("Introduction", [
            ("javascript-intro","Introduction",False),
            ("a-quick-review","A Quick Review",False),
        ]),
        ("Organizing Your Code", [
            ("organizing-js-intro","Organizing Your JS Code Intro",False),
            ("objects-and-constructors","Objects and Object Constructors",False),
            ("project-library","Project: Library",True),
            ("factory-functions-and-the-module-pattern","Factory Functions and Module Pattern",False),
            ("classes","Classes",False),
            ("es6-modules","ES6 Modules",False),
            ("webpack","Webpack",False),
            ("project-restaurant-page","Project: Restaurant Page",True),
            ("oop-principles","OOP Principles",False),
            ("project-todo-list","Project: Todo List",True),
        ]),
        ("JavaScript in the Real World", [
            ("linting","Linting",False),
            ("dynamic-user-interface-interactions","Dynamic UI Interactions",False),
            ("form-validation-with-javascript","Form Validation with JS",False),
            ("what-is-es6","What is ES6?",False),
        ]),
        ("Async JavaScript and APIs", [
            ("json","JSON",False),
            ("asynchronous-code","Asynchronous Code",False),
            ("working-with-apis","Working with APIs",False),
            ("async-and-await","Async and Await",False),
            ("project-weather-app","Project: Weather App",True),
        ]),
        ("Testing JavaScript", [
            ("testing-basics","Testing Basics",False),
            ("more-testing","More Testing",False),
            ("project-battleship","Project: Battleship",True),
        ]),
        ("Intermediate Git", [
            ("a-deeper-look-at-git","A Deeper Look at Git",False),
            ("working-with-remotes","Working with Remotes",False),
            ("using-git-in-the-real-world","Using Git in the Real World",False),
        ]),
        ("Finishing Up with JavaScript", [
            ("project-javascript-final","Project: JavaScript Final",True),
        ]),
        ("Computer Science", [
            ("recursion","Recursion",False),
            ("project-fibonacci","Project: Fibonacci",True),
            ("time-complexity","Time Complexity",False),
            ("space-complexity","Space Complexity",False),
            ("common-data-structures","Common Data Structures",False),
            ("linked-lists","Linked Lists",False),
            ("project-linked-lists","Project: Linked Lists",True),
            ("hash-map","Hash Map",False),
            ("project-hashmap","Project: HashMap",True),
            ("binary-search-trees","Binary Search Trees",False),
            ("project-binary-search-trees","Project: Binary Search Trees",True),
            ("knights-travails","Project: Knights Travails",True),
        ]),
    ]
    s = '<aside class="sidebar"><div class="sidebar-course-title">JavaScript</div>'
    for label, items in sections:
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
    p = (ALL_LESSONS[idx-1][1], ALL_LESSONS[idx-1][0]+".html") if idx and idx>0 else None
    n = (ALL_LESSONS[idx+1][1], ALL_LESSONS[idx+1][0]+".html") if idx is not None and idx<len(ALL_LESSONS)-1 else None
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
    p, n = pn(slug)
    bc = (
        '<nav class="breadcrumb">'
        f'<a href="{ROOT}index.html">Home</a>'
        '<span class="breadcrumb-sep">/</span>'
        f'<a href="{ROOT}paths/full-stack-javascript/index.html">Full Stack JS</a>'
        '<span class="breadcrumb-sep">/</span>'
        '<a href="../index.html">JavaScript</a>'
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
        f'  <link rel="stylesheet" href="{ROOT}css/styles.css">\n'
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
        + f'<script src="{ROOT}js/main.js"></script>\n</body>\n</html>'
    )
    with open(os.path.join(LDIR, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓  {slug}")


# ═══════════════════════════════════════════════════════════
#  LESSONS
# ═══════════════════════════════════════════════════════════
def seed():

    write("javascript-intro","Introduction",
    intro="Welcome to the JavaScript course. You already know JavaScript basics from Foundations. This course takes you much deeper — professional code organisation, asynchronous programming, testing, and computer science fundamentals. By the end you will be writing production-quality JavaScript.",
    overview=[
        "Understand what this course covers and how the sections connect.",
        "Know the prerequisites expected from Foundations.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-you-need">What You Need From Foundations</h2>
<p>This course assumes you can already:</p>
<ul>
  <li>Write JavaScript functions, use arrays and objects, and work with loops and conditionals</li>
  <li>Manipulate the DOM and handle events</li>
  <li>Use Git and push projects to GitHub</li>
  <li>Build multi-page HTML/CSS sites with Flexbox</li>
</ul>
<p>If any of those feel shaky, revisit the relevant Foundations lessons before continuing.</p>

<h2 class="lesson-section-title" id="what-youll-learn">What This Course Covers</h2>
<ul>
  <li><strong>Organising JavaScript Code</strong> — Objects, constructors, factory functions, classes, modules, and Webpack. How to structure real applications.</li>
  <li><strong>JavaScript in the Real World</strong> — Linting, dynamic UI patterns, and form validation.</li>
  <li><strong>Asynchronous JavaScript and APIs</strong> — Promises, fetch, async/await, and JSON. How to talk to external services.</li>
  <li><strong>Testing</strong> — Unit testing with Jest. Writing testable code and test-driven development.</li>
  <li><strong>Intermediate Git</strong> — Branching, rebasing, and collaborative workflows.</li>
  <li><strong>Computer Science Fundamentals</strong> — Recursion, time and space complexity, linked lists, hash maps, and binary search trees.</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>The projects in this course are significantly more complex than those in Foundations. Budget more time, commit more frequently, and use the debugging skills you built earlier.</p>
</div>""",
    kc=[("What JavaScript topics from Foundations are assumed in this course?","what-you-need"),
        ("What are the six topic areas this course covers?","what-youll-learn")],
    assignments=[
        "Review your Foundations JavaScript projects. If any concepts feel unclear, revisit those lessons before moving on.",
        "Make sure Node.js and npm are installed: run <code>node --version</code> and <code>npm --version</code>.",
    ],
    resources=[
        ("javascript.info — The Modern JavaScript Tutorial","https://javascript.info/"),
        ("MDN — JavaScript Guide","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"),
    ])

    write("a-quick-review",  "A Quick Review",
    intro="Before diving into new material, this lesson consolidates the JavaScript fundamentals from Foundations — variables, functions, arrays, objects, and the DOM — so everything that follows has a solid base.",
    overview=[
        "Solidify understanding of variables, scope, and closures.",
        "Review array and object manipulation.",
        "Review DOM manipulation and event handling.",
        "Understand the difference between value and reference types.",
    ],
    body="""
<h2 class="lesson-section-title" id="scope-closures">Scope and Closures</h2>
<p>Understanding scope is essential before tackling modules and classes. Every function creates its own scope. A <strong>closure</strong> is a function that retains access to variables from its outer scope even after that outer function has returned.</p>
""" + code("""function makeCounter() {
  let count = 0;          // 'count' lives in makeCounter's scope

  return function () {    // this inner function is a closure
    count++;              // it retains access to 'count'
    return count;
  };
}

const counter = makeCounter();
counter(); // 1
counter(); // 2
counter(); // 3
// count is inaccessible from outside — encapsulated
""") + """
<h2 class="lesson-section-title" id="value-vs-reference">Value vs. Reference</h2>
<p>Primitives (numbers, strings, booleans) are copied by <strong>value</strong>. Objects and arrays are copied by <strong>reference</strong> — both variables point to the same data in memory.</p>
""" + code("""// PRIMITIVES — copied by value
let a = 5;
let b = a;
b = 10;
console.log(a); // 5 — unchanged

// OBJECTS — copied by reference
const obj1 = { name: "Alice" };
const obj2 = obj1;           // obj2 points to the SAME object
obj2.name = "Bob";
console.log(obj1.name); // "Bob" — obj1 was also changed!

// To copy an object without reference
const obj3 = { ...obj1 };    // shallow copy with spread
const obj4 = structuredClone(obj1); // deep copy
""") + """
<h2 class="lesson-section-title" id="array-methods-review">Array Methods Review</h2>
""" + code("""const students = [
  { name: "Alice", grade: 92 },
  { name: "Bob",   grade: 74 },
  { name: "Carol", grade: 88 },
];

// map — transform each item
const names = students.map(s => s.name);
// ["Alice", "Bob", "Carol"]

// filter — keep items that pass
const passing = students.filter(s => s.grade >= 80);
// [Alice(92), Carol(88)]

// reduce — combine into one value
const average = students.reduce((sum, s) => sum + s.grade, 0) / students.length;
// 84.67

// find — first match
const topStudent = students.find(s => s.grade > 90);
// { name: "Alice", grade: 92 }

// some / every
students.some(s => s.grade < 60);   // false
students.every(s => s.grade >= 70); // true
"""),
    kc=[("What is a closure and why is it useful?","scope-closures"),
        ("What is the difference between copying by value and copying by reference?","value-vs-reference"),
        ("What does Array.find() return?","array-methods-review")],
    assignments=[
        "Without looking at any reference, write a function that takes an array of numbers and returns: the sum, the average, the maximum, and the minimum — all using reduce, no loops.",
        "Write a function using closures that creates a private counter with increment, decrement, and reset methods.",
    ],
    resources=[
        ("javascript.info — Closures","https://javascript.info/closure"),
        ("MDN — Array methods","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array"),
        ("YouTube — JavaScript Closures (Fireship)","https://www.youtube.com/watch?v=vKJpN5FAeF4"),
    ])

    write("organizing-js-intro","Organizing Your JavaScript Code Introduction",
    intro="As applications grow, dumping all your code in a single script.js file becomes unmanageable. This lesson introduces the problem of code organisation and the patterns JavaScript provides to solve it.",
    overview=[
        "Understand why code organisation matters.",
        "Know the main approaches: plain objects, constructors, classes, modules.",
        "Understand the concept of encapsulation.",
    ],
    body="""
<h2 class="lesson-section-title" id="the-problem">The Problem with Unorganised Code</h2>
<p>A script file with 1000 lines of unstructured code has several serious problems:</p>
<ul>
  <li><strong>Name collisions</strong> — variables with the same name overwrite each other</li>
  <li><strong>Global pollution</strong> — everything is accessible everywhere, making bugs hard to trace</li>
  <li><strong>No reusability</strong> — copy-pasting code instead of reusing it</li>
  <li><strong>Hard to test</strong> — intertwined code cannot be tested in isolation</li>
</ul>

<h2 class="lesson-section-title" id="approaches">Approaches to Organisation</h2>
<p>JavaScript offers several patterns for organising code, from simple to sophisticated:</p>
<ol>
  <li><strong>Plain objects</strong> — group related data and functions together in an object literal</li>
  <li><strong>Object constructors / factory functions</strong> — create multiple instances of the same object shape</li>
  <li><strong>ES6 Classes</strong> — syntactic sugar over prototypes, familiar to developers from other languages</li>
  <li><strong>ES6 Modules</strong> — split code across multiple files, each with its own scope</li>
</ol>

<h2 class="lesson-section-title" id="encapsulation">Encapsulation</h2>
<p><strong>Encapsulation</strong> means keeping internal implementation details private, exposing only what is needed. This prevents other parts of your code from accidentally depending on internal details that might change.</p>
""" + code("""// Without encapsulation — everything exposed
let playerHP = 100;
let playerMaxHP = 100;
function healPlayer(amount) { playerHP = Math.min(playerHP + amount, playerMaxHP); }

// With encapsulation — internal state is protected
function createPlayer(name) {
  let hp = 100;           // private — not directly accessible
  const maxHp = 100;      // private

  return {
    name,
    getHP() { return hp; },
    heal(amount) {
      hp = Math.min(hp + amount, maxHp);
      console.log(`${name} healed to ${hp} HP`);
    },
    takeDamage(amount) {
      hp = Math.max(0, hp - amount);
    },
  };
}

const player = createPlayer("Lena");
player.heal(30);
console.log(player.getHP()); // 100
// player.hp is undefined — encapsulated
"""),
    kc=[("What problems does unorganised JavaScript cause?","the-problem"),
        ("What is encapsulation?","encapsulation"),
        ("Name four approaches to organising JavaScript code.","approaches")],
    assignments=[
        "Read javascript.info's 'Objects — the basics' chapter if you need a refresher.",
        "Take one of your previous projects and identify all the global variables. Refactor them into a single object.",
    ],
    resources=[
        ("javascript.info — Objects","https://javascript.info/object"),
        ("MDN — Object-oriented programming","https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_programming"),
        ("YouTube — JavaScript Object Oriented Programming (Traversy Media)","https://www.youtube.com/watch?v=vDJpGbbZj6s"),
    ])

    write("objects-and-constructors","Objects and Object Constructors",
    intro="You know how to create a single object with an object literal. But what if you need to create many objects with the same shape? Object constructors and prototypes are the traditional JavaScript answer.",
    overview=[
        "Create objects using constructor functions.",
        "Understand the prototype chain.",
        "Use Object.create() to set prototypes explicitly.",
        "Know what the new keyword does step by step.",
    ],
    body="""
<h2 class="lesson-section-title" id="constructors">Constructor Functions</h2>
<p>A constructor function is a regular function called with the <code>new</code> keyword. By convention, constructor functions are capitalised.</p>
""" + code("""function Player(name, level) {
  this.name  = name;
  this.level = level;
  this.hp    = 100;
}

// Add methods to the prototype — shared by ALL instances
// Much more memory-efficient than adding methods inside the constructor
Player.prototype.greet = function () {
  return `Hi, I'm ${this.name}, level ${this.level}`;
};

Player.prototype.levelUp = function () {
  this.level++;
  console.log(`${this.name} reached level ${this.level}!`);
};

const player1 = new Player("Alice", 5);
const player2 = new Player("Bob", 3);

player1.greet();    // "Hi, I'm Alice, level 5"
player2.levelUp();  // "Bob reached level 4!"

// Both instances share the same greet and levelUp functions
// they are not duplicated in memory
""") + """
<h2 class="lesson-section-title" id="new-keyword">What new Does</h2>
<p>When you call a constructor with <code>new</code>, four things happen automatically:</p>
""" + code("""// What 'new Player("Alice", 5)' does behind the scenes:

// 1. Creates a new empty object
const obj = {};

// 2. Sets the new object's prototype to Player.prototype
Object.setPrototypeOf(obj, Player.prototype);

// 3. Calls the constructor with 'this' pointing to the new object
Player.call(obj, "Alice", 5);

// 4. Returns the new object (unless the constructor returns an object explicitly)
return obj;
""") + """
<h2 class="lesson-section-title" id="prototype-chain">The Prototype Chain</h2>
<p>Every JavaScript object has an internal link to a <strong>prototype</strong>. When you access a property, JavaScript first looks on the object itself, then walks up the prototype chain until it finds it or reaches null.</p>
""" + code("""const player1 = new Player("Alice", 5);

// Property lookup order:
// 1. Does player1 have its own 'greet' property? No.
// 2. Does Player.prototype have 'greet'? Yes → use it.
player1.greet();

// Checking the chain
console.log(player1.__proto__ === Player.prototype);          // true
console.log(Player.prototype.__proto__ === Object.prototype); // true
console.log(Object.prototype.__proto__);                      // null — end of chain

// instanceof checks the prototype chain
player1 instanceof Player; // true
player1 instanceof Object; // true (everything is ultimately an Object)
"""),
    kc=[("What does the new keyword do in four steps?","new-keyword"),
        ("Why add methods to the prototype instead of inside the constructor?","constructors"),
        ("How does JavaScript look up a property using the prototype chain?","prototype-chain")],
    assignments=[
        "Build a Book constructor function with title, author, and pages properties. Add a method to the prototype that logs a summary. Create at least three book instances.",
        "Read MDN's 'Object prototypes' article — linked below.",
    ],
    resources=[
        ("MDN — Object Prototypes","https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes"),
        ("javascript.info — Prototypes","https://javascript.info/prototype-inheritance"),
        ("YouTube — Prototypes in JavaScript (Fireship)","https://www.youtube.com/watch?v=wstwjQ1yqWQ"),
    ])

    write("project-library","Project: Library",
    intro="Your first organised JavaScript project. You will build a personal library app that stores books and tracks reading status — using the object and constructor knowledge from the previous lesson.",
    overview=[
        "Store a collection of Book objects in an array.",
        "Add and remove books from the library.",
        "Toggle read status on each book.",
        "Display the library as cards in the DOM.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>A <code>Book</code> constructor/class with: title, author, pages, read (boolean)</li>
  <li>A <code>myLibrary</code> array that stores all books</li>
  <li>An <code>addBookToLibrary()</code> function</li>
  <li>A UI that displays each book as a card showing all its info</li>
  <li>A "New Book" button that opens a form (dialog or section) to add a book</li>
  <li>Each card has a button to toggle the read status</li>
  <li>Each card has a button to remove the book from the library</li>
  <li>The display updates whenever the library changes</li>
</ul>

<h2 class="lesson-section-title" id="approach">Suggested Approach</h2>
""" + code("""// 1. Define the Book constructor
function Book(title, author, pages, read) {
  this.title  = title;
  this.author = author;
  this.pages  = pages;
  this.read   = read;
}

Book.prototype.toggleRead = function () {
  this.read = !this.read;
};

Book.prototype.info = function () {
  return `${this.title} by ${this.author}, ${this.pages} pages, ${this.read ? "already read" : "not read yet"}`;
};

// 2. Store books
const myLibrary = [];

function addBookToLibrary(title, author, pages, read) {
  const book = new Book(title, author, pages, read);
  myLibrary.push(book);
}

// 3. Render the library
function displayLibrary() {
  const grid = document.querySelector("#book-grid");
  grid.innerHTML = "";  // clear before re-rendering

  myLibrary.forEach((book, index) => {
    const card = document.createElement("div");
    card.classList.add("book-card");
    card.innerHTML = `
      <h3>${book.title}</h3>
      <p>${book.author}</p>
      <p>${book.pages} pages</p>
      <button data-index="${index}" class="toggle-btn">
        ${book.read ? "Read" : "Not Read"}
      </button>
      <button data-index="${index}" class="remove-btn">Remove</button>
    `;
    grid.appendChild(card);
  });
}
""") + code("""mkdir ~/devpath-projects/library
cd ~/devpath-projects/library
git init
touch index.html styles.css script.js
code .
"""),
    kc=[("What data does each Book object need?","requirements"),
        ("Why clear the grid innerHTML before re-rendering?","approach")],
    assignments=["Complete the Library project meeting all requirements.","Push to GitHub and deploy on GitHub Pages."],
    resources=[
        ("MDN — Document.createElement","https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement"),
        ("javascript.info — Constructor and new","https://javascript.info/constructor-new"),
        ("YouTube — Build a Library App (Web Dev Simplified)","https://www.youtube.com/watch?v=eiC58R16hb8"),
    ])

    write("factory-functions-and-the-module-pattern","Factory Functions and the Module Pattern",
    intro="Factory functions are an alternative to constructors for creating objects. The Module Pattern uses closures to create private scope — a powerful technique for writing encapsulated, reusable code.",
    overview=[
        "Write factory functions that return objects.",
        "Understand the advantages of factory functions over constructors.",
        "Use the Module Pattern to create private scope.",
        "Use IIFEs to create modules in legacy code.",
    ],
    body="""
<h2 class="lesson-section-title" id="factory-functions">Factory Functions</h2>
<p>A factory function is any function that returns a new object. No <code>new</code> keyword, no <code>this</code>, no prototype wrangling.</p>
""" + code("""// Factory function
function createPlayer(name, level) {
  // Private state — not exposed on the returned object
  let hp = 100;

  // Public interface — what callers can access
  return {
    name,
    level,
    getHP()      { return hp; },
    takeDamage(n){ hp = Math.max(0, hp - n); },
    heal(n)      { hp = Math.min(100, hp + n); },
    toString()   { return `${name} (lvl ${level}) — ${hp}HP`; },
  };
}

const p1 = createPlayer("Alice", 5);
const p2 = createPlayer("Bob",   3);

p1.takeDamage(30);
console.log(p1.getHP()); // 70
console.log(p2.getHP()); // 100 — independent

// hp is private — this returns undefined
console.log(p1.hp); // undefined
""") + """
<h2 class="lesson-section-title" id="factory-vs-constructor">Factory vs. Constructor</h2>
<ul>
  <li>Factory functions do not require <code>new</code> — calling without it does not silently break things</li>
  <li>Factory functions easily achieve private state via closures</li>
  <li>Constructors use prototypes — methods are shared in memory (more efficient for thousands of instances)</li>
  <li>Factory functions copy methods into every instance (fine for most applications)</li>
</ul>

<h2 class="lesson-section-title" id="module-pattern">The Module Pattern</h2>
<p>The Module Pattern uses an IIFE (Immediately Invoked Function Expression) to create a private scope and return a public API. Used extensively in pre-ES6 code and still valuable today.</p>
""" + code("""// IIFE — runs immediately, creates its own scope
const ShoppingCart = (function () {
  // Private state
  const items = [];
  let discount = 0;

  // Private function
  function calculateTotal() {
    return items.reduce((sum, item) => sum + item.price, 0) * (1 - discount);
  }

  // Public API — returned object
  return {
    addItem(item)   { items.push(item); },
    removeItem(id)  { items.splice(items.findIndex(i => i.id === id), 1); },
    setDiscount(pct){ discount = pct / 100; },
    getTotal()      { return calculateTotal(); },
    getItems()      { return [...items]; },  // return a copy
  };
})();

ShoppingCart.addItem({ id: 1, name: "Book", price: 20 });
ShoppingCart.setDiscount(10);
ShoppingCart.getTotal(); // 18
// ShoppingCart.items is undefined — private!
"""),
    kc=[("What is a factory function?","factory-functions"),
        ("What advantage do factory functions have over constructors for privacy?","factory-vs-constructor"),
        ("What is an IIFE and how does it create private scope?","module-pattern")],
    assignments=[
        "Refactor your Library project to use a factory function for Book instead of a constructor.",
        "Build a BankAccount module using the Module Pattern with private balance and methods: deposit, withdraw, getBalance.",
    ],
    resources=[
        ("javascript.info — Factory Functions","https://javascript.info/constructor-new"),
        ("MDN — Closures","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures"),
        ("YouTube — Factory Functions (Fireship)","https://www.youtube.com/watch?v=ImwrezYhw4w"),
    ])

    write("classes","Classes",
    intro="ES6 Classes provide a cleaner syntax for creating objects and managing inheritance. They are syntactic sugar over JavaScript's prototype system — the same mechanics, with more familiar syntax.",
    overview=[
        "Define classes with the class keyword.",
        "Use constructors, methods, and static methods.",
        "Extend classes with inheritance using extends and super.",
        "Use private class fields.",
    ],
    body="""
<h2 class="lesson-section-title" id="class-syntax">Class Syntax</h2>
""" + code("""class Player {
  // Private field — declared at the top (modern syntax)
  #hp = 100;

  constructor(name, level) {
    this.name  = name;
    this.level = level;
  }

  // Instance method — available on all instances
  greet() {
    return `Hi, I'm ${this.name}, level ${this.level}`;
  }

  getHP()       { return this.#hp; }
  takeDamage(n) { this.#hp = Math.max(0, this.#hp - n); }
  heal(n)       { this.#hp = Math.min(100, this.#hp + n); }

  // Static method — called on the class, not an instance
  static create(name) {
    return new Player(name, 1);  // convenience factory
  }
}

const p1 = new Player("Alice", 5);
p1.greet();          // "Hi, I'm Alice, level 5"
p1.getHP();          // 100
p1.takeDamage(30);
p1.getHP();          // 70

const p2 = Player.create("Bob");  // level 1
""") + """
<h2 class="lesson-section-title" id="inheritance">Inheritance with extends</h2>
""" + code("""class Mage extends Player {
  constructor(name, level, spellPower) {
    super(name, level);   // MUST call super() first
    this.spellPower = spellPower;
  }

  castSpell(target) {
    const damage = this.spellPower * 2;
    target.takeDamage(damage);
    return `${this.name} casts a spell for ${damage} damage!`;
  }

  // Override parent method
  greet() {
    return `${super.greet()} and I am a Mage`;
  }
}

const mage = new Mage("Zara", 8, 45);
mage.greet();        // "Hi, I'm Zara, level 8 and I am a Mage"
mage.takeDamage(20); // inherited from Player
mage.castSpell(p1);  // uses spellPower
""") + """
<h2 class="lesson-section-title" id="getters-setters">Getters and Setters</h2>
""" + code("""class Temperature {
  #celsius;

  constructor(celsius) {
    this.#celsius = celsius;
  }

  get fahrenheit() {
    return this.#celsius * 9/5 + 32;
  }

  set fahrenheit(f) {
    this.#celsius = (f - 32) * 5/9;
  }

  get celsius() { return this.#celsius; }
  set celsius(c) { this.#celsius = c; }
}

const temp = new Temperature(100);
temp.fahrenheit;       // 212 — accessed like a property, not a method
temp.fahrenheit = 98.6;
temp.celsius;          // 37
"""),
    kc=[("What does super() do in a subclass constructor?","inheritance"),
        ("What is the difference between an instance method and a static method?","class-syntax"),
        ("How do private class fields differ from regular properties?","class-syntax")],
    assignments=[
        "Refactor your Library project to use ES6 Classes for Book.",
        "Build an Animal class hierarchy: Animal base class with name and sound properties, then Dog and Cat subclasses that each override a speak() method.",
    ],
    resources=[
        ("MDN — Classes","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes"),
        ("javascript.info — Classes","https://javascript.info/classes"),
        ("YouTube — JavaScript Classes (Fireship)","https://www.youtube.com/watch?v=2ZphE5HcQPQ"),
    ])

    write("es6-modules","ES6 Modules",
    intro="ES6 Modules let you split your JavaScript into separate files, each with its own private scope. They are the standard way to organise modern JavaScript applications.",
    overview=[
        "Export values from a module using named and default exports.",
        "Import values into another module.",
        "Understand module scope.",
        "Use modules in the browser with type='module'.",
    ],
    body="""
<h2 class="lesson-section-title" id="exports">Exports</h2>
""" + code("""// math.js

// Named exports — can export multiple things
export function add(a, b)      { return a + b; }
export function subtract(a, b) { return a - b; }
export const PI = 3.14159;

// Or export at the bottom
function multiply(a, b) { return a * b; }
const E = 2.71828;
export { multiply, E };

// Default export — one per file
// Typically the main thing the module provides
export default class Calculator {
  add(a, b)      { return a + b; }
  subtract(a, b) { return a - b; }
}
""") + """
<h2 class="lesson-section-title" id="imports">Imports</h2>
""" + code("""// main.js

// Named imports — must match the exported name
import { add, subtract, PI } from './math.js';
console.log(add(2, 3));  // 5
console.log(PI);          // 3.14159

// Rename on import
import { multiply as times } from './math.js';
times(3, 4);  // 12

// Import everything as a namespace
import * as Math from './math.js';
Math.add(1, 2);
Math.PI;

// Default import — any name you choose
import Calculator from './math.js';
const calc = new Calculator();
""") + """
<h2 class="lesson-section-title" id="browser-usage">Using Modules in the Browser</h2>
""" + code("""<!-- Add type="module" to your script tag -->
<script type="module" src="main.js"></script>

<!-- Modules are:
  - Deferred by default (run after HTML is parsed)
  - Strict mode always enabled
  - Each file has its own scope
  - Only loaded once even if imported multiple times
-->
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Modules require a server to work — they do not work with file:// URLs due to CORS restrictions. Use VS Code's Live Server extension while developing.</p>
</div>""",
    kc=[("What is the difference between a named export and a default export?","exports"),
        ("How do you import only specific named exports?","imports"),
        ("Why do ES6 modules require a server to work in the browser?","browser-usage")],
    assignments=[
        "Split your Library project into multiple modules: Book.js, library.js, and display.js. Import them into main.js.",
        "Read MDN's JavaScript modules guide — linked below.",
    ],
    resources=[
        ("MDN — JavaScript Modules","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules"),
        ("javascript.info — Modules","https://javascript.info/modules-intro"),
        ("YouTube — ES6 Modules (Fireship)","https://www.youtube.com/watch?v=cRHQNNcYf6s"),
    ])

    write("webpack","Webpack",
    intro="Webpack is a module bundler. It takes your JavaScript modules (and CSS, images, and other assets) and bundles them into optimised files for production. It is the backbone of almost every modern JavaScript build system.",
    overview=[
        "Understand what a module bundler does and why it is needed.",
        "Set up a basic Webpack configuration.",
        "Use npm scripts to run Webpack.",
        "Understand loaders and plugins.",
    ],
    body="""
<h2 class="lesson-section-title" id="why-webpack">Why Bundle?</h2>
<p>Without bundling, a large application might make dozens or hundreds of separate HTTP requests for individual module files. Bundling solves this by combining everything into one (or a few) optimised files. It also enables:</p>
<ul>
  <li>Using npm packages in the browser</li>
  <li>Transpiling modern JavaScript (via Babel) for older browsers</li>
  <li>Processing CSS, images, and other assets through the same pipeline</li>
  <li>Tree shaking — removing unused code from the bundle</li>
  <li>Hot Module Replacement (HMR) — instant updates during development without a full reload</li>
</ul>

<h2 class="lesson-section-title" id="setup">Basic Webpack Setup</h2>
""" + code("""# Create project and install webpack
mkdir my-project && cd my-project
npm init -y
npm install --save-dev webpack webpack-cli webpack-dev-server

# Project structure
my-project/
├── src/
│   ├── index.js       ← entry point
│   ├── math.js
│   └── styles.css
├── dist/              ← output (generated by webpack)
├── webpack.config.js
└── package.json
""") + code("""// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'development',              // 'production' for optimised output
  entry: './src/index.js',          // where webpack starts
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
    clean: true,                    // clean dist/ before each build
  },
  devServer: {
    static: './dist',
    hot: true,                      // hot module replacement
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html', // auto-injects the bundle script tag
    }),
  ],
};
""") + code("""// package.json scripts
{
  "scripts": {
    "build": "webpack",
    "dev":   "webpack serve --open"
  }
}

// Run development server
npm run dev

// Build for production
npm run build
"""),
    kc=[("What problem does a module bundler solve?","why-webpack"),
        ("What is the entry point in a Webpack config?","setup"),
        ("What does webpack-dev-server provide?","setup")],
    assignments=[
        "Set up a new project with Webpack following the steps above. Confirm the dev server runs.",
        "Add the HtmlWebpackPlugin so HTML is automatically generated and the bundle is injected.",
        "Port your Library project to use Webpack.",
    ],
    resources=[
        ("Webpack Official Docs — Getting Started","https://webpack.js.org/guides/getting-started/"),
        ("YouTube — Webpack Crash Course (Traversy Media)","https://www.youtube.com/watch?v=IZGNcSuwBZs"),
        ("MDN — JavaScript build tools","https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Package_management"),
    ])

    write("project-restaurant-page","Project: Restaurant Page",
    intro="Build a tabbed restaurant website where all content is rendered by JavaScript — not hard-coded in HTML. This project practises DOM manipulation, ES6 modules, and Webpack together.",
    overview=[
        "Use Webpack to bundle the project.",
        "Render all page content dynamically with JavaScript.",
        "Implement a tab navigation system.",
        "Organise code into ES6 modules.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>The HTML file contains only a <code>&lt;div id="content"&gt;</code> — all HTML is generated by JavaScript</li>
  <li>At least three tabs: Home, Menu, Contact</li>
  <li>Clicking a tab clears the content div and renders that tab's content</li>
  <li>Each tab's content is in its own module file</li>
  <li>Webpack bundles everything</li>
  <li>Published on GitHub Pages from the <code>dist/</code> folder</li>
</ul>

<h2 class="lesson-section-title" id="structure">Module Structure</h2>
""" + code("""src/
├── index.js          ← entry: sets up tabs, loads home by default
├── home.js           ← exports a function that renders home content
├── menu.js           ← exports a function that renders menu content
├── contact.js        ← exports a function that renders contact content
└── nav.js            ← exports a function that renders the tab navigation
""") + code("""// home.js
export default function renderHome() {
  const content = document.querySelector("#content");
  content.innerHTML = "";

  const hero = document.createElement("section");
  hero.classList.add("hero");
  hero.innerHTML = `
    <h1>Welcome to The Rustic Fork</h1>
    <p>Farm-to-table dining since 1995</p>
    <a href="#" class="btn-primary">View Menu</a>
  `;
  content.appendChild(hero);
}
""") + code("""// index.js
import renderHome    from './home.js';
import renderMenu    from './menu.js';
import renderContact from './contact.js';
import renderNav     from './nav.js';

renderNav();
renderHome();  // load home by default

document.addEventListener("click", (e) => {
  if (e.target.dataset.tab === "home")    renderHome();
  if (e.target.dataset.tab === "menu")    renderMenu();
  if (e.target.dataset.tab === "contact") renderContact();
});
""") + """
<h2 class="lesson-section-title" id="github-pages-dist">Deploying dist/ to GitHub Pages</h2>
""" + code("""# After running npm run build, deploy the dist/ folder
# Option: use gh-pages package
npm install --save-dev gh-pages

# Add to package.json scripts:
"deploy": "gh-pages -d dist"

# Then:
npm run build
npm run deploy
"""),
    kc=[("Why should the HTML file only contain a div#content?","requirements"),
        ("How do you make a tab switch render different content?","structure")],
    assignments=["Complete the Restaurant Page meeting all requirements.","Deploy to GitHub Pages."],
    resources=[
        ("Webpack — Getting Started","https://webpack.js.org/guides/getting-started/"),
        ("MDN — DOM Manipulation","https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model"),
        ("YouTube — Dynamic JS Restaurant Page (Kevin Powell)","https://www.youtube.com/watch?v=806nde1XSRY"),
    ])

    write("oop-principles","OOP Principles",
    intro="Object-oriented programming has four core principles. Understanding them helps you write code that is easier to maintain, extend, and reason about.",
    overview=[
        "Understand the four pillars of OOP: encapsulation, abstraction, inheritance, polymorphism.",
        "Apply SOLID principles to JavaScript code.",
        "Recognise common OOP anti-patterns.",
    ],
    body="""
<h2 class="lesson-section-title" id="four-pillars">The Four Pillars</h2>
<ul>
  <li><strong>Encapsulation</strong> — Bundling data and the methods that operate on that data together, hiding internal details. Already seen with private class fields and factory functions.</li>
  <li><strong>Abstraction</strong> — Exposing only what is necessary. A <code>Car</code> class has a <code>start()</code> method — the caller does not need to know about fuel injection, ignition timing, and valve timing.</li>
  <li><strong>Inheritance</strong> — A subclass inherits the properties and methods of its parent class, extending or overriding them. Done with <code>extends</code> in JavaScript.</li>
  <li><strong>Polymorphism</strong> — Different classes can be treated the same way if they implement the same interface. A function that calls <code>speak()</code> works whether it receives a Dog, Cat, or Parrot.</li>
</ul>
""" + code("""// Polymorphism example
class Animal {
  constructor(name) { this.name = name; }
  speak() { return `${this.name} makes a sound.`; }
}

class Dog extends Animal {
  speak() { return `${this.name} barks.`; }
}

class Cat extends Animal {
  speak() { return `${this.name} meows.`; }
}

// This function works with ANY Animal subclass
function makeNoise(animal) {
  console.log(animal.speak());
}

makeNoise(new Dog("Rex"));   // "Rex barks."
makeNoise(new Cat("Luna"));  // "Luna meows."
// The function doesn't care which subclass it receives
""") + """
<h2 class="lesson-section-title" id="solid">SOLID Principles</h2>
<ul>
  <li><strong>S — Single Responsibility</strong> — A class should have only one reason to change. If it handles both data storage AND email sending, split it.</li>
  <li><strong>O — Open/Closed</strong> — Open for extension, closed for modification. Add new behaviour by adding code, not modifying existing code.</li>
  <li><strong>L — Liskov Substitution</strong> — Subclasses should be usable wherever the parent class is used without breaking anything.</li>
  <li><strong>I — Interface Segregation</strong> — Do not force classes to implement methods they do not use.</li>
  <li><strong>D — Dependency Inversion</strong> — Depend on abstractions, not concretions.</li>
</ul>
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>You do not need to memorise SOLID for a quiz. Use them as diagnostic tools: when your code feels hard to change, one of these principles is probably being violated.</p>
</div>""",
    kc=[("What are the four pillars of OOP?","four-pillars"),
        ("What is polymorphism and why is it useful?","four-pillars"),
        ("What does the Single Responsibility Principle say?","solid")],
    assignments=[
        "Identify which OOP pillar is demonstrated in your Library and Restaurant projects.",
        "Read the SOLID principles article linked below and identify one violation in your existing code.",
    ],
    resources=[
        ("MDN — Object-Oriented Programming","https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_programming"),
        ("javascript.info — Classes","https://javascript.info/classes"),
        ("YouTube — SOLID Principles (Fireship)","https://www.youtube.com/watch?v=XzdhzyAukMM"),
    ])

    write("project-todo-list","Project: Todo List",
    intro="The Todo List is a classic project for a reason — it forces you to implement full CRUD (Create, Read, Update, Delete) logic, manage state, and keep the UI in sync. This version uses ES6 Modules and Webpack.",
    overview=[
        "Structure a complex app with ES6 Modules and Webpack.",
        "Implement full CRUD operations for todos and projects.",
        "Separate application logic from DOM manipulation.",
        "Persist data using localStorage.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Create, view, edit, and delete todo items</li>
  <li>Each todo has: title, description, due date, priority (high/medium/low), and completion status</li>
  <li>Todos belong to Projects (like work, personal, shopping)</li>
  <li>Create, view, and delete projects</li>
  <li>The active project's todos are displayed in the main panel</li>
  <li>Data persists in localStorage — survives page refresh</li>
  <li>Built with Webpack and ES6 Modules</li>
</ul>

<h2 class="lesson-section-title" id="architecture">Recommended Architecture</h2>
""" + code("""src/
├── index.js          ← entry point
├── Todo.js           ← Todo class
├── Project.js        ← Project class
├── Storage.js        ← localStorage read/write
├── UI.js             ← DOM manipulation
└── index.html
""") + code("""// Todo.js
export class Todo {
  constructor(title, description, dueDate, priority) {
    this.id          = Date.now().toString();
    this.title       = title;
    this.description = description;
    this.dueDate     = dueDate;
    this.priority    = priority;  // 'high' | 'medium' | 'low'
    this.complete    = false;
  }

  toggle() { this.complete = !this.complete; }
}

// Storage.js
export const Storage = {
  saveProjects(projects) {
    localStorage.setItem('projects', JSON.stringify(projects));
  },
  loadProjects() {
    const data = localStorage.getItem('projects');
    return data ? JSON.parse(data) : [];
  },
};
"""),
    kc=[("What does CRUD stand for?","requirements"),
        ("Why separate the UI module from the logic modules?","architecture")],
    assignments=["Complete the Todo List project meeting all requirements.","Ensure data persists after page refresh using localStorage.","Push to GitHub Pages."],
    resources=[
        ("MDN — localStorage","https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage"),
        ("javascript.info — LocalStorage","https://javascript.info/localstorage"),
        ("YouTube — Todo List App (Web Dev Simplified)","https://www.youtube.com/watch?v=W7FaYfuwu70"),
    ])

    write("linting","Linting",
    intro="A linter is a tool that statically analyses your code for errors, stylistic issues, and potential bugs — without running it. ESLint is the standard JavaScript linter used in virtually every professional project.",
    overview=[
        "Understand what linting is and why it matters.",
        "Set up ESLint in a project.",
        "Configure ESLint rules.",
        "Integrate ESLint with VS Code for real-time feedback.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-is-linting">What Linting Does</h2>
<p>A linter catches problems before they become bugs:</p>
<ul>
  <li>Undefined variables and functions</li>
  <li>Unreachable code</li>
  <li>Accidentally using <code>==</code> instead of <code>===</code></li>
  <li>Unused variables</li>
  <li>Inconsistent formatting (tabs vs spaces, semicolons, quote style)</li>
</ul>

<h2 class="lesson-section-title" id="setup">Setting Up ESLint</h2>
""" + code("""# Install ESLint
npm install --save-dev eslint

# Create a config file interactively
npx eslint --init

# Or create .eslintrc.json manually
""") + code("""// .eslintrc.json
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": "eslint:recommended",
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "rules": {
    "no-unused-vars": "warn",
    "no-console":     "off",
    "eqeqeq":         "error",
    "semi":           ["error", "always"],
    "quotes":         ["error", "single"],
    "indent":         ["error", 2]
  }
}
""") + code("""# Run ESLint on your files
npx eslint src/

# Fix auto-fixable issues automatically
npx eslint src/ --fix

# Add to package.json scripts
"lint":       "eslint src/",
"lint:fix":   "eslint src/ --fix"
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Install the ESLint extension for VS Code. It highlights problems inline as you type — no need to run the command manually. This is far more effective than linting after the fact.</p>
</div>""",
    kc=[("What kinds of problems does a linter catch?","what-is-linting"),
        ("What does eslint:recommended extend?","setup"),
        ("What does the --fix flag do?","setup")],
    assignments=[
        "Add ESLint to your Todo List project. Run it and fix every issue it flags.",
        "Install the ESLint VS Code extension. Confirm it shows errors inline.",
    ],
    resources=[
        ("ESLint — Getting Started","https://eslint.org/docs/latest/use/getting-started"),
        ("YouTube — ESLint Setup (Traversy Media)","https://www.youtube.com/watch?v=SydnKbGc7W8"),
        ("MDN — JavaScript best practices","https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Build_your_own_function"),
    ])

    write("dynamic-user-interface-interactions","Dynamic User Interface Interactions",
    intro="Modern web apps feel smooth and responsive. This lesson covers the patterns behind dropdowns, modals, image sliders, and other dynamic UI components — without relying on jQuery or UI frameworks.",
    overview=[
        "Build dropdown menus that open and close.",
        "Implement a modal dialog.",
        "Build an image carousel.",
        "Use CSS transitions combined with JavaScript for smooth animations.",
    ],
    body="""
<h2 class="lesson-section-title" id="dropdowns">Dropdown Menus</h2>
""" + code("""// HTML structure
<div class="dropdown">
  <button class="dropdown-toggle" aria-expanded="false">
    Options ▾
  </button>
  <ul class="dropdown-menu" hidden>
    <li><a href="#">Edit</a></li>
    <li><a href="#">Duplicate</a></li>
    <li><button class="danger">Delete</button></li>
  </ul>
</div>
""") + code("""// JavaScript
document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
  toggle.addEventListener('click', (e) => {
    e.stopPropagation();  // prevent document click from closing immediately
    const menu = toggle.nextElementSibling;
    const isOpen = !menu.hidden;

    // Close all other open dropdowns first
    document.querySelectorAll('.dropdown-menu').forEach(m => {
      m.hidden = true;
      m.previousElementSibling.setAttribute('aria-expanded', 'false');
    });

    // Toggle this dropdown
    if (!isOpen) {
      menu.hidden = false;
      toggle.setAttribute('aria-expanded', 'true');
    }
  });
});

// Close when clicking outside
document.addEventListener('click', () => {
  document.querySelectorAll('.dropdown-menu').forEach(m => {
    m.hidden = true;
  });
});
""") + """
<h2 class="lesson-section-title" id="modals">Modal Dialogs</h2>
""" + code("""// Modern HTML: use the native <dialog> element
<dialog id="confirm-modal">
  <h2>Are you sure?</h2>
  <p>This action cannot be undone.</p>
  <div class="modal-actions">
    <button id="cancel-btn">Cancel</button>
    <button id="confirm-btn" class="danger">Delete</button>
  </div>
</dialog>

<button id="open-modal">Delete Item</button>
""") + code("""const modal     = document.querySelector('#confirm-modal');
const openBtn   = document.querySelector('#open-modal');
const cancelBtn = document.querySelector('#cancel-btn');
const confirmBtn= document.querySelector('#confirm-btn');

openBtn.addEventListener('click', () => modal.showModal());
cancelBtn.addEventListener('click', () => modal.close());
confirmBtn.addEventListener('click', () => {
  // perform the action
  modal.close();
});

// Close on backdrop click
modal.addEventListener('click', (e) => {
  if (e.target === modal) modal.close();
});
"""),
    kc=[("How do you prevent a document click handler from immediately closing a dropdown?","dropdowns"),
        ("What HTML element provides a native accessible modal dialog?","modals"),
        ("What does aria-expanded communicate to screen readers?","dropdowns")],
    assignments=[
        "Build a dropdown navigation menu that is fully keyboard-accessible.",
        "Implement a confirmation modal using the native <dialog> element.",
    ],
    resources=[
        ("MDN — dialog element","https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog"),
        ("javascript.info — Browser Events","https://javascript.info/introduction-browser-events"),
        ("YouTube — Build a Modal (Web Dev Simplified)","https://www.youtube.com/watch?v=MBaw_6cPmAw"),
    ])

    write("form-validation-with-javascript","Form Validation with JavaScript",
    intro="HTML5 validation handles the basics. For custom error messages, complex cross-field validation, and async checks (like 'is this username taken?'), you need JavaScript.",
    overview=[
        "Use the Constraint Validation API.",
        "Write custom validation logic.",
        "Display error messages accessibly.",
        "Handle async validation (e.g. checking if a username exists).",
    ],
    body="""
<h2 class="lesson-section-title" id="constraint-api">Constraint Validation API</h2>
""" + code("""const form  = document.querySelector('#signup-form');
const email = document.querySelector('#email');

// Check validity programmatically
email.validity.valid;         // true/false
email.validity.valueMissing;  // true if required and empty
email.validity.typeMismatch;  // true if wrong type (e.g. not a valid email)
email.validity.tooShort;      // true if below minlength
email.validity.patternMismatch;// true if pattern fails
email.validationMessage;      // browser's built-in error message

// Override the browser's validation message
email.setCustomValidity("Please use your company email address.");
email.setCustomValidity(""); // empty string = valid — always reset first!
""") + """
<h2 class="lesson-section-title" id="custom-validation">Custom Validation with Accessible Errors</h2>
""" + code("""// Validation logic
function validatePassword(input) {
  const value = input.value;
  const errors = [];

  if (value.length < 8)           errors.push("At least 8 characters");
  if (!/[A-Z]/.test(value))       errors.push("At least one uppercase letter");
  if (!/[0-9]/.test(value))       errors.push("At least one number");

  return errors;
}

// Display errors accessibly
function showErrors(input, errors) {
  const errorEl = document.querySelector(`#${input.id}-error`);
  if (errors.length > 0) {
    input.setAttribute('aria-invalid', 'true');
    errorEl.textContent = errors.join(". ");
    errorEl.hidden = false;
  } else {
    input.setAttribute('aria-invalid', 'false');
    errorEl.hidden = true;
  }
}

// HTML structure for accessible errors
// <input id="password" aria-describedby="password-error">
// <p id="password-error" hidden role="alert"></p>
""") + """
<h2 class="lesson-section-title" id="async-validation">Async Validation</h2>
""" + code("""const usernameInput = document.querySelector('#username');

// Debounce — wait until user stops typing before checking
let debounceTimer;
usernameInput.addEventListener('input', () => {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(checkUsername, 500); // wait 500ms
});

async function checkUsername() {
  const username = usernameInput.value;
  if (username.length < 3) return;

  const response = await fetch(`/api/check-username?user=${username}`);
  const { available } = await response.json();

  if (!available) {
    usernameInput.setCustomValidity("Username already taken.");
    showErrors(usernameInput, ["Username already taken."]);
  } else {
    usernameInput.setCustomValidity("");
    showErrors(usernameInput, []);
  }
}
"""),
    kc=[("What does setCustomValidity('') do?","constraint-api"),
        ("What does debouncing prevent?","async-validation"),
        ("What ARIA attribute indicates an invalid field to screen readers?","custom-validation")],
    assignments=[
        "Add custom JavaScript validation to your Sign-Up Form project with inline error messages.",
        "Add password strength validation that checks length, uppercase, and numbers.",
    ],
    resources=[
        ("MDN — Constraint Validation","https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation"),
        ("MDN — Client-Side Form Validation","https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation"),
        ("YouTube — Custom Form Validation (Web Dev Simplified)","https://www.youtube.com/watch?v=In0nB0ABaUk"),
    ])

    write("what-is-es6","What is ES6?",
    intro="ES6 (ECMAScript 2015) was the largest update to JavaScript in its history. This lesson covers the features introduced then and in subsequent annual releases that you will use constantly.",
    overview=[
        "Use destructuring for arrays and objects.",
        "Use the spread and rest operators.",
        "Use template literals.",
        "Use optional chaining and nullish coalescing.",
    ],
    body="""
<h2 class="lesson-section-title" id="destructuring">Destructuring</h2>
""" + code("""// Object destructuring
const user = { name: "Alice", age: 28, city: "Addis Ababa" };
const { name, age } = user;
const { name: userName, city = "Unknown" } = user;  // rename + default

// Array destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
// first=1, second=2, rest=[3,4,5]

// In function parameters
function displayUser({ name, age, role = "user" }) {
  console.log(`${name} (${age}) — ${role}`);
}
displayUser(user);

// Swap variables
let a = 1, b = 2;
[a, b] = [b, a];  // a=2, b=1
""") + """
<h2 class="lesson-section-title" id="spread-rest">Spread and Rest</h2>
""" + code("""// Spread — expand an array or object
const nums    = [1, 2, 3];
const moreNums = [...nums, 4, 5, 6];   // [1,2,3,4,5,6]
const combined = [...arr1, ...arr2];    // merge arrays

// Copy an object
const original = { a: 1, b: 2 };
const copy      = { ...original, c: 3 };  // {a:1, b:2, c:3}

// Pass array elements as arguments
Math.max(...nums);  // same as Math.max(1, 2, 3)

// Rest — collect remaining arguments
function sum(...numbers) {
  return numbers.reduce((total, n) => total + n, 0);
}
sum(1, 2, 3, 4, 5);  // 15

function first(a, b, ...others) {
  console.log(a, b, others);
}
first(1, 2, 3, 4, 5);  // 1  2  [3,4,5]
""") + """
<h2 class="lesson-section-title" id="optional-chaining">Optional Chaining and Nullish Coalescing</h2>
""" + code("""const user = {
  profile: {
    address: {
      city: "Addis Ababa"
    }
  }
};

// Without optional chaining — crashes if profile is null
const city = user.profile.address.city; // fine here, but fragile

// With optional chaining — returns undefined instead of throwing
const city2 = user?.profile?.address?.city;     // "Addis Ababa"
const zip   = user?.profile?.address?.zip;      // undefined (not a crash)
const len   = user?.profile?.getFullName?.();   // undefined if no function

// Nullish coalescing — use right side only if left is null or undefined
const displayName = user.name ?? "Anonymous";   // "Anonymous" if name is null/undefined
const port        = config.port ?? 3000;         // 3000 if port not set

// Vs. OR operator — be careful: OR treats 0 and "" as falsy
const count = data.count || 10;  // wrong if count is legitimately 0
const count2 = data.count ?? 10; // correct — only falls back if null/undefined
"""),
    kc=[("What is the difference between spread and rest?","spread-rest"),
        ("What does optional chaining return if a property does not exist?","optional-chaining"),
        ("What is the difference between ?? and || ?","optional-chaining")],
    assignments=[
        "Refactor one of your projects to use destructuring in function parameters wherever an object is passed.",
        "Find all places where you write fallback values with || and check if ?? would be more correct.",
    ],
    resources=[
        ("javascript.info — Destructuring","https://javascript.info/destructuring-assignment"),
        ("MDN — Optional chaining","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining"),
        ("YouTube — ES6 Features (Fireship)","https://www.youtube.com/watch?v=nZ1DMMsyVyI"),
    ])

    write("json","JSON",
    intro="JSON (JavaScript Object Notation) is the universal format for sending and receiving data across the web. Every API you will ever work with uses JSON. This lesson covers everything you need to know.",
    overview=[
        "Understand JSON syntax and how it differs from JavaScript object literals.",
        "Parse JSON strings into JavaScript objects with JSON.parse().",
        "Convert JavaScript objects to JSON strings with JSON.stringify().",
        "Handle JSON in real API responses.",
    ],
    body="""
<h2 class="lesson-section-title" id="json-syntax">JSON Syntax</h2>
<p>JSON looks almost identical to JavaScript object literals but has stricter rules:</p>
""" + code("""{
  "name": "Alice",
  "age": 28,
  "isAdmin": false,
  "scores": [95, 87, 92],
  "address": {
    "city": "Addis Ababa",
    "country": "Ethiopia"
  },
  "nickname": null
}

// JSON rules:
// - Keys MUST be double-quoted strings
// - Strings MUST use double quotes (no single quotes)
// - No trailing commas
// - No comments
// - No undefined, functions, or Symbols (not valid JSON values)
// - Valid values: string, number, boolean, null, array, object
""") + """
<h2 class="lesson-section-title" id="parse-stringify">JSON.parse() and JSON.stringify()</h2>
""" + code("""// JSON string → JavaScript object
const jsonString = '{"name":"Alice","age":28}';
const user = JSON.parse(jsonString);
user.name; // "Alice"

// JavaScript object → JSON string
const data = { name: "Bob", scores: [90, 85, 92] };
const json = JSON.stringify(data);
// '{"name":"Bob","scores":[90,85,92]}'

// Pretty-print with indentation (useful for logging)
const pretty = JSON.stringify(data, null, 2);
// {
//   "name": "Bob",
//   "scores": [90, 85, 92]
// }

// Replacer function — filter what gets included
const filtered = JSON.stringify(user, ["name", "age"]);
// only includes name and age properties
""") + """
<h2 class="lesson-section-title" id="localStorage">JSON and localStorage</h2>
""" + code("""// localStorage only stores strings — JSON bridges the gap

// Save complex data
const todos = [{ id: 1, text: "Learn JavaScript", done: false }];
localStorage.setItem("todos", JSON.stringify(todos));

// Load it back
const stored = localStorage.getItem("todos");
const loaded = stored ? JSON.parse(stored) : [];

// CAUTION: JSON.parse throws if the string is invalid
try {
  const data = JSON.parse(localStorage.getItem("todos") ?? "[]");
} catch (e) {
  console.error("Invalid JSON in localStorage:", e);
  localStorage.removeItem("todos");
}
"""),
    kc=[("What are the key syntax differences between JSON and a JS object literal?","json-syntax"),
        ("What does JSON.parse() do?","parse-stringify"),
        ("Why must you use JSON with localStorage?","localStorage")],
    assignments=[
        "Update your Todo List project to save and load data from localStorage using JSON.stringify and JSON.parse.",
        "Fetch a public JSON API (like JSONPlaceholder) and log the parsed data.",
    ],
    resources=[
        ("MDN — JSON","https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON"),
        ("javascript.info — JSON","https://javascript.info/json"),
        ("JSONPlaceholder — Free fake API for testing","https://jsonplaceholder.typicode.com/"),
    ])

    write("asynchronous-code","Asynchronous Code",
    intro="JavaScript is single-threaded — it can only do one thing at a time. Asynchronous programming is how it handles operations that take time (network requests, file reads, timers) without freezing the page.",
    overview=[
        "Understand what asynchronous code means and why it is needed.",
        "Understand the event loop and the call stack.",
        "Use callbacks and understand callback hell.",
        "Understand Promises as a better alternative.",
    ],
    body="""
<h2 class="lesson-section-title" id="why-async">Why Asynchronous Code?</h2>
<p>Imagine fetching data from a server. That request might take 500ms. If JavaScript waited synchronously, the entire page would freeze for that half-second. Asynchronous code lets JavaScript <em>start</em> the operation and then continue executing other code while waiting for the result.</p>

<h2 class="lesson-section-title" id="event-loop">The Event Loop</h2>
<p>JavaScript uses a <strong>call stack</strong> to track what is currently executing. When an async operation completes, its callback is placed in the <strong>task queue</strong>. The <strong>event loop</strong> continuously checks: "Is the call stack empty? If yes, move the next task from the queue onto the stack."</p>
""" + code("""console.log("1 — synchronous, runs first");

setTimeout(() => {
  console.log("3 — runs after call stack is empty");
}, 0);  // 0ms delay — but still async!

console.log("2 — synchronous, runs second");

// Output:
// 1 — synchronous, runs first
// 2 — synchronous, runs second
// 3 — runs after call stack is empty
""") + """
<h2 class="lesson-section-title" id="callbacks">Callbacks and Callback Hell</h2>
""" + code("""// Simple callback
function fetchUser(id, callback) {
  setTimeout(() => {
    callback({ id, name: "Alice" });  // simulate async response
  }, 100);
}

fetchUser(1, (user) => {
  console.log(user.name);  // "Alice"
});

// Callback hell — deeply nested, hard to read and maintain
getUser(userId, (user) => {
  getProfile(user.id, (profile) => {
    getPosts(profile.id, (posts) => {
      getComments(posts[0].id, (comments) => {
        // now we can finally do something
        // this is called "callback hell" or "the pyramid of doom"
      });
    });
  });
});
""") + """
<h2 class="lesson-section-title" id="promises">Promises — The Solution</h2>
<p>A <strong>Promise</strong> is an object representing the eventual result of an async operation. It is either pending, fulfilled (success), or rejected (failure).</p>
""" + code("""// Creating a Promise
function fetchUser(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id > 0) {
        resolve({ id, name: "Alice" }); // success
      } else {
        reject(new Error("Invalid user ID")); // failure
      }
    }, 100);
  });
}

// Consuming a Promise with .then() and .catch()
fetchUser(1)
  .then(user => {
    console.log(user.name);
    return getProfile(user.id);  // return another promise
  })
  .then(profile => {
    console.log(profile);
  })
  .catch(error => {
    console.error("Something went wrong:", error);
  })
  .finally(() => {
    console.log("Done — runs whether success or failure");
  });
"""),
    kc=[("What is the event loop and what does it do?","event-loop"),
        ("What is callback hell?","callbacks"),
        ("What are the three states a Promise can be in?","promises")],
    assignments=[
        "Read javascript.info's 'Introduction: callbacks' and 'Promises' chapters — linked below.",
        "Create a function that returns a Promise. Handle both its resolved and rejected states with .then() and .catch().",
    ],
    resources=[
        ("javascript.info — Callbacks","https://javascript.info/callbacks"),
        ("javascript.info — Promises","https://javascript.info/promise-basics"),
        ("YouTube — JavaScript Event Loop (Fireship)","https://www.youtube.com/watch?v=eiC58R16hb8"),
    ])

    write("working-with-apis","Working with APIs",
    intro="APIs (Application Programming Interfaces) let your JavaScript talk to external services — weather data, news feeds, maps, authentication. The browser's fetch() function is the standard way to make these requests.",
    overview=[
        "Use fetch() to make HTTP requests.",
        "Handle JSON responses.",
        "Use query parameters and request headers.",
        "Handle errors in API calls gracefully.",
    ],
    body="""
<h2 class="lesson-section-title" id="fetch-basics">fetch() Basics</h2>
""" + code("""// fetch() returns a Promise
fetch('https://api.example.com/users')
  .then(response => {
    // response.ok is true for 200-299 status codes
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    return response.json(); // parse JSON — also returns a Promise
  })
  .then(data => {
    console.log(data); // the actual data
  })
  .catch(error => {
    console.error('Fetch failed:', error);
  });
""") + """
<h2 class="lesson-section-title" id="query-params">Query Parameters and Headers</h2>
""" + code("""// Query parameters
const params = new URLSearchParams({
  city:  'London',
  units: 'metric',
  appid: 'YOUR_API_KEY',
});

fetch(`https://api.openweathermap.org/data/2.5/weather?${params}`)
  .then(r => r.json())
  .then(data => console.log(data));

// Request headers (for authenticated APIs)
fetch('https://api.example.com/protected', {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
});

// POST request with a body
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'Alice', email: 'alice@example.com' }),
});
""") + """
<h2 class="lesson-section-title" id="error-handling">Error Handling</h2>
""" + code("""// Important: fetch() only rejects on network failure
// A 404 or 500 response still RESOLVES — you must check response.ok

async function getUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);

    if (response.status === 404) {
      throw new Error('User not found');
    }
    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const user = await response.json();
    return user;

  } catch (error) {
    if (error.name === 'TypeError') {
      // Network error — no internet connection etc.
      console.error('Network error:', error);
    } else {
      console.error('API error:', error.message);
    }
    throw error;  // re-throw so the caller can handle it too
  }
}
"""),
    kc=[("What does fetch() return?","fetch-basics"),
        ("Why must you check response.ok even if fetch did not throw?","error-handling"),
        ("How do you add authentication headers to a fetch request?","query-params")],
    assignments=[
        "Fetch data from the JSONPlaceholder API and render a list of posts on a page.",
        "Add a loading spinner that appears while the fetch is in progress and disappears when data loads.",
    ],
    resources=[
        ("MDN — Using Fetch","https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch"),
        ("javascript.info — Fetch","https://javascript.info/fetch"),
        ("YouTube — Fetch API (Traversy Media)","https://www.youtube.com/watch?v=Oive66jrwBs"),
    ])

    write("async-and-await","Async and Await",
    intro="Async/await is syntactic sugar over Promises that makes asynchronous code look and read like synchronous code. It is the modern standard for writing async JavaScript.",
    overview=[
        "Mark a function as async with the async keyword.",
        "Use await to pause execution until a Promise resolves.",
        "Handle errors with try/catch in async functions.",
        "Run multiple async operations in parallel with Promise.all().",
    ],
    body="""
<h2 class="lesson-section-title" id="async-await-syntax">async/await Syntax</h2>
""" + code("""// The async keyword makes a function return a Promise automatically
async function fetchUser(id) {
  // await pauses THIS function until the Promise resolves
  // Other code keeps running in the background
  const response = await fetch(`/api/users/${id}`);

  if (!response.ok) throw new Error('User not found');

  const user = await response.json();
  return user;  // this becomes the resolved value of the returned Promise
}

// Calling an async function
fetchUser(1).then(user => console.log(user));

// Or await it inside another async function
async function showUser() {
  const user = await fetchUser(1);
  console.log(user.name);
}
""") + """
<h2 class="lesson-section-title" id="try-catch">Error Handling with try/catch</h2>
""" + code("""async function loadData() {
  try {
    const response = await fetch('/api/data');
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    renderData(data);
  } catch (error) {
    showErrorMessage(error.message);
  } finally {
    hideLoadingSpinner();  // always runs, success or failure
  }
}
""") + """
<h2 class="lesson-section-title" id="parallel">Running in Parallel with Promise.all()</h2>
""" + code("""// Sequential — slow: waits for each before starting the next
async function sequential() {
  const user    = await fetchUser(1);      // waits ~200ms
  const posts   = await fetchPosts(1);     // then waits ~200ms
  const comments= await fetchComments(1);  // then waits ~200ms
  // total: ~600ms
}

// Parallel — fast: all three start simultaneously
async function parallel() {
  const [user, posts, comments] = await Promise.all([
    fetchUser(1),
    fetchPosts(1),
    fetchComments(1),
  ]);
  // total: ~200ms (limited by the slowest)
}

// Promise.allSettled — runs all, reports results even if some fail
const results = await Promise.allSettled([fetchA(), fetchB(), fetchC()]);
results.forEach(result => {
  if (result.status === 'fulfilled') console.log(result.value);
  else console.error(result.reason);
});
"""),
    kc=[("What does the async keyword do to a function's return value?","async-await-syntax"),
        ("What does await do to the surrounding function?","async-await-syntax"),
        ("When should you use Promise.all() instead of awaiting sequentially?","parallel")],
    assignments=[
        "Refactor your API fetch calls from .then()/.catch() chains to async/await with try/catch.",
        "Build a page that fetches data from two different endpoints simultaneously using Promise.all().",
    ],
    resources=[
        ("javascript.info — Async/Await","https://javascript.info/async-await"),
        ("MDN — async function","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function"),
        ("YouTube — Async Await (Fireship)","https://www.youtube.com/watch?v=vn3tm0quoqE"),
    ])

    write("project-weather-app","Project: Weather App",
    intro="The Weather App is the async/API capstone project. You will fetch live weather data from a real API and display it in a polished, responsive UI.",
    overview=[
        "Use the OpenWeatherMap API to fetch real weather data.",
        "Use async/await for all API calls.",
        "Handle loading states and errors gracefully.",
        "Toggle between Celsius and Fahrenheit.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>A search form where the user enters a city name</li>
  <li>Fetches current weather from OpenWeatherMap API (free tier)</li>
  <li>Displays: city name, country, temperature, weather description, humidity, wind speed, and an appropriate weather icon</li>
  <li>Toggle between Celsius and Fahrenheit (convert client-side, do not re-fetch)</li>
  <li>Loading indicator while the request is in progress</li>
  <li>Friendly error message for invalid cities or network failures</li>
  <li>Responsive layout that works on mobile</li>
</ul>

<h2 class="lesson-section-title" id="api-setup">API Setup</h2>
""" + code("""// 1. Sign up at openweathermap.org (free)
// 2. Get your API key from the API keys dashboard
// 3. The Current Weather endpoint:

const API_KEY = 'your_api_key_here';

async function getWeather(city) {
  const url = `https://api.openweathermap.org/data/2.5/weather`
    + `?q=${encodeURIComponent(city)}`
    + `&appid=${API_KEY}`
    + `&units=metric`;  // Celsius

  const response = await fetch(url);

  if (response.status === 404) {
    throw new Error(`City "${city}" not found`);
  }
  if (!response.ok) {
    throw new Error(`Weather service error: ${response.status}`);
  }

  return response.json();
}

// Example response structure
{
  "name": "London",
  "sys": { "country": "GB" },
  "main": { "temp": 15.2, "humidity": 76 },
  "weather": [{ "description": "light rain", "icon": "10d" }],
  "wind": { "speed": 4.1 }
}

// Weather icon URL
const iconUrl = `https://openweathermap.org/img/wn/${iconCode}@2x.png`;
""") + code("""mkdir ~/devpath-projects/weather-app
cd ~/devpath-projects/weather-app
git init
touch index.html styles.css index.js
code .
"""),
    kc=[("How do you handle a 404 from the weather API differently from other errors?","api-setup"),
        ("Why convert temperature client-side instead of making a new API request?","requirements")],
    assignments=["Complete the Weather App meeting all requirements.","Push to GitHub Pages."],
    resources=[
        ("OpenWeatherMap API Docs","https://openweathermap.org/current"),
        ("MDN — Fetch API","https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API"),
        ("YouTube — Weather App with API (Traversy Media)","https://www.youtube.com/watch?v=wPElVpR1rwA"),
    ])

    write("testing-basics","Testing Basics",
    intro="Testing is the practice of writing code that verifies your other code works correctly. This lesson introduces unit testing with Jest — the most popular JavaScript testing framework.",
    overview=[
        "Understand the purpose and types of software testing.",
        "Install and configure Jest.",
        "Write basic unit tests with describe, it, and expect.",
        "Use common Jest matchers.",
    ],
    body="""
<h2 class="lesson-section-title" id="why-test">Why Write Tests?</h2>
<ul>
  <li><strong>Confidence</strong> — tests prove your code does what you think it does</li>
  <li><strong>Regression prevention</strong> — tests catch when a change breaks existing functionality</li>
  <li><strong>Documentation</strong> — tests describe how your code should behave</li>
  <li><strong>Better design</strong> — code that is hard to test is usually badly structured</li>
</ul>

<h2 class="lesson-section-title" id="jest-setup">Jest Setup</h2>
""" + code("""npm install --save-dev jest

# Add to package.json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch"
  }
}

# Run tests
npm test

# Jest automatically finds files named:
# *.test.js
# *.spec.js
# files in __tests__/ folders
""") + """
<h2 class="lesson-section-title" id="writing-tests">Writing Tests</h2>
""" + code("""// calculator.js — the code under test
export function add(a, b)      { return a + b; }
export function divide(a, b) {
  if (b === 0) throw new Error('Cannot divide by zero');
  return a / b;
}
""") + code("""// calculator.test.js — the tests
import { add, divide } from './calculator.js';

describe('add()', () => {
  it('adds two positive numbers', () => {
    expect(add(2, 3)).toBe(5);
  });

  it('adds negative numbers', () => {
    expect(add(-1, -1)).toBe(-2);
  });

  it('returns a number', () => {
    expect(typeof add(1, 2)).toBe('number');
  });
});

describe('divide()', () => {
  it('divides two numbers', () => {
    expect(divide(10, 2)).toBe(5);
  });

  it('throws when dividing by zero', () => {
    expect(() => divide(10, 0)).toThrow('Cannot divide by zero');
  });
});
""") + """
<h2 class="lesson-section-title" id="matchers">Common Matchers</h2>
""" + code("""expect(value).toBe(5);              // strict equality (===)
expect(value).toEqual({ a: 1 });    // deep equality for objects/arrays
expect(value).toBeTruthy();         // any truthy value
expect(value).toBeFalsy();          // any falsy value
expect(value).toBeNull();
expect(value).toBeUndefined();
expect(value).toBeGreaterThan(3);
expect(value).toContain('hello');   // array or string contains
expect(value).toHaveLength(3);
expect(fn).toThrow('error message');
expect(fn).not.toThrow();           // .not inverts any matcher
"""),
    kc=[("What are four benefits of writing tests?","why-test"),
        ("What is the difference between toBe() and toEqual()?","matchers"),
        ("What does the describe() block do?","writing-tests")],
    assignments=[
        "Write unit tests for the Calculator project — test every function including edge cases.",
        "Achieve 100% passing tests before writing any new code this week.",
    ],
    resources=[
        ("Jest — Getting Started","https://jestjs.io/docs/getting-started"),
        ("javascript.info — Testing with Mocha","https://javascript.info/testing-mocha"),
        ("YouTube — Jest Crash Course (Traversy Media)","https://www.youtube.com/watch?v=7r4xVDI2vho"),
    ])

    write("more-testing","More Testing",
    intro="Beyond basic unit tests, real applications need mocking, spying, and testing asynchronous code. This lesson covers the advanced Jest techniques used in production projects.",
    overview=[
        "Mock modules and functions with jest.fn() and jest.mock().",
        "Test asynchronous code with async/await in tests.",
        "Use beforeEach and afterEach for test setup and teardown.",
        "Understand test-driven development (TDD).",
    ],
    body="""
<h2 class="lesson-section-title" id="mocking">Mocking Functions</h2>
<p>Mocking replaces a real implementation with a controlled fake. This isolates the unit you are testing from its dependencies.</p>
""" + code("""// jest.fn() creates a mock function
const mockCallback = jest.fn();

mockCallback(1);
mockCallback(2);

expect(mockCallback).toHaveBeenCalledTimes(2);
expect(mockCallback).toHaveBeenCalledWith(1);
expect(mockCallback).toHaveBeenLastCalledWith(2);

// Mock return values
const mockFetch = jest.fn()
  .mockResolvedValueOnce({ ok: true, json: () => ({ name: "Alice" }) })
  .mockRejectedValueOnce(new Error("Network error"));
""") + code("""// jest.mock() — replace an entire module
jest.mock('./api.js');
import { getUser } from './api.js';

getUser.mockResolvedValue({ id: 1, name: "Alice" });

test('renders user name', async () => {
  const user = await getUser(1);
  expect(user.name).toBe("Alice");
});
""") + """
<h2 class="lesson-section-title" id="async-tests">Testing Async Code</h2>
""" + code("""// Test async functions with async/await
it('fetches user successfully', async () => {
  const user = await fetchUser(1);
  expect(user.name).toBe("Alice");
});

// Test that a Promise rejects
it('throws on invalid ID', async () => {
  await expect(fetchUser(-1)).rejects.toThrow('Invalid user ID');
});
""") + """
<h2 class="lesson-section-title" id="setup-teardown">Setup and Teardown</h2>
""" + code("""describe('UserService', () => {
  let db;

  beforeAll(() => {
    db = createTestDatabase();    // once before ALL tests
  });

  afterAll(() => {
    db.close();                   // once after ALL tests
  });

  beforeEach(() => {
    db.clear();                   // before EACH test — clean state
    db.seed([{ id: 1, name: "Alice" }]);
  });

  afterEach(() => {
    jest.clearAllMocks();          // clear mock state between tests
  });

  it('finds a user by id', () => {
    const user = db.findById(1);
    expect(user.name).toBe("Alice");
  });
});
""") + """
<h2 class="lesson-section-title" id="tdd">Test-Driven Development (TDD)</h2>
<p>TDD is a workflow: <strong>Red → Green → Refactor</strong></p>
<ol>
  <li><strong>Red</strong> — Write a failing test for the functionality you want to add</li>
  <li><strong>Green</strong> — Write the minimum code to make the test pass</li>
  <li><strong>Refactor</strong> — Clean up the code without breaking the tests</li>
</ol>
<p>TDD forces you to think about what your code should do before you write it — which leads to better-designed, more testable code.</p>""",
    kc=[("What is the purpose of mocking in tests?","mocking"),
        ("What is the difference between beforeEach and beforeAll?","setup-teardown"),
        ("What are the three steps of TDD?","tdd")],
    assignments=[
        "Use TDD to build a simple string utility library: functions for capitalize, truncate, and slugify.",
        "Add mocking to your Weather App tests to avoid real API calls during testing.",
    ],
    resources=[
        ("Jest — Mock Functions","https://jestjs.io/docs/mock-functions"),
        ("Jest — Async Testing","https://jestjs.io/docs/asynchronous"),
        ("YouTube — TDD in JavaScript (Fireship)","https://www.youtube.com/watch?v=Jv2uxzhPFl4"),
    ])

    write("project-battleship","Project: Battleship",
    intro="Battleship is the most complex project in this course. It tests your ability to apply OOP, modules, DOM manipulation, and testing all together in one well-structured application.",
    overview=[
        "Design game logic completely separate from UI code.",
        "Use TDD to build the game logic layer.",
        "Implement drag-and-drop ship placement.",
        "Write comprehensive unit tests for all game logic.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Two 10x10 boards — one for the player, one for the computer</li>
  <li>Ships: Carrier(5), Battleship(4), Destroyer(3), Submarine(3), Patrol Boat(2)</li>
  <li>Player can place ships on their board (drag-and-drop or click-to-place)</li>
  <li>Computer places ships randomly</li>
  <li>Players alternate turns attacking the opponent's board</li>
  <li>Computer attacks randomly (stretch: smarter targeting)</li>
  <li>Game ends when all of one player's ships are sunk</li>
  <li>Comprehensive unit tests for all game logic using Jest</li>
</ul>

<h2 class="lesson-section-title" id="architecture">Architecture</h2>
""" + code("""src/
├── Ship.js          ← Ship class: length, hit(), isSunk()
├── Gameboard.js     ← Gameboard class: placeShip(), receiveAttack(), etc.
├── Player.js        ← Player class: human and computer
├── Game.js          ← Game controller: manages turns and win condition
├── UI.js            ← All DOM manipulation
└── index.js         ← Entry point, wires everything together

__tests__/
├── Ship.test.js
├── Gameboard.test.js
└── Player.test.js
""") + code("""// Ship.js — write tests FIRST (TDD)
export class Ship {
  constructor(length) {
    this.length = length;
    this.hits   = 0;
  }

  hit()    { this.hits++; }
  isSunk() { return this.hits >= this.length; }
}

// Ship.test.js
describe('Ship', () => {
  it('creates a ship with correct length', () => {
    const ship = new Ship(3);
    expect(ship.length).toBe(3);
  });

  it('records hits', () => {
    const ship = new Ship(3);
    ship.hit();
    ship.hit();
    expect(ship.hits).toBe(2);
  });

  it('is not sunk after partial hits', () => {
    const ship = new Ship(3);
    ship.hit(); ship.hit();
    expect(ship.isSunk()).toBe(false);
  });

  it('is sunk when all positions hit', () => {
    const ship = new Ship(2);
    ship.hit(); ship.hit();
    expect(ship.isSunk()).toBe(true);
  });
});
"""),
    kc=[("Why should game logic be completely separate from UI code?","architecture"),
        ("What does it mean to use TDD for this project?","architecture")],
    assignments=["Complete Battleship meeting all requirements.","Ensure all game logic has unit tests that pass.","Push to GitHub Pages."],
    resources=[
        ("Jest — Getting Started","https://jestjs.io/docs/getting-started"),
        ("MDN — Drag and Drop API","https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API"),
        ("YouTube — Battleship Game JavaScript","https://www.youtube.com/watch?v=4VkC4QoGTBc"),
    ])

    write("a-deeper-look-at-git","A Deeper Look at Git",
    intro="You know Git basics. This lesson covers the features that distinguish a junior developer's Git usage from a professional's: branching strategies, rebasing, and fixing mistakes.",
    overview=[
        "Create, switch, merge, and delete branches.",
        "Understand and use rebasing.",
        "Undo mistakes with git reset, git revert, and git restore.",
        "Use git stash to save work in progress.",
    ],
    body="""
<h2 class="lesson-section-title" id="branching">Branching</h2>
""" + code("""# Create and switch to a new branch
git checkout -b feature/user-auth
# Modern syntax
git switch -c feature/user-auth

# List branches
git branch         # local branches
git branch -a      # all branches (including remote)

# Switch branches
git switch main
git checkout main  # older syntax

# Merge a branch into current branch
git switch main
git merge feature/user-auth

# Delete branch after merging
git branch -d feature/user-auth       # safe delete
git branch -D feature/user-auth       # force delete
""") + """
<h2 class="lesson-section-title" id="rebase">Rebasing</h2>
<p>Merging creates a new merge commit. Rebasing <em>replays</em> your commits on top of another branch, creating a linear history.</p>
""" + code("""# Rebase your feature branch onto main
git switch feature/my-feature
git rebase main

# If conflicts arise:
# 1. Fix the conflicts
git add .
git rebase --continue
# or abandon:
git rebase --abort

# Interactive rebase — rewrite commit history
git rebase -i HEAD~3  # rewrite the last 3 commits
# In the editor: pick/squash/reword/drop each commit
""") + """
<h2 class="lesson-section-title" id="undoing">Undoing Mistakes</h2>
""" + code("""# Unstage a file (keep changes in working directory)
git restore --staged index.html

# Discard changes in working directory (IRREVERSIBLE)
git restore index.html

# Undo the last commit (keep changes staged)
git reset --soft HEAD~1

# Undo the last commit (keep changes unstaged)
git reset HEAD~1

# DANGEROUS: undo commit AND discard changes
git reset --hard HEAD~1

# Safely undo a commit by creating a new "undo" commit
# Use this for commits already pushed to GitHub
git revert abc1234

# Save work temporarily without committing
git stash
git stash list
git stash pop      # restore and remove stash
git stash apply    # restore but keep stash
"""),
    kc=[("What is the difference between merging and rebasing?","rebase"),
        ("What does git reset --soft HEAD~1 do?","undoing"),
        ("When should you use git revert instead of git reset?","undoing")],
    assignments=[
        "Create a practice repo and practise creating branches, merging, and rebasing.",
        "Practice interactive rebasing: squash three commits into one.",
    ],
    resources=[
        ("Atlassian — Git Branching","https://www.atlassian.com/git/tutorials/using-branches"),
        ("Atlassian — Git Rebase","https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase"),
        ("YouTube — Git Branches and Rebase (Fireship)","https://www.youtube.com/watch?v=0chZFIZLR_0"),
    ])

    write("working-with-remotes","Working with Remotes",
    intro="When collaborating with others, you need to manage multiple remote repositories, handle diverged histories, and work with pull requests. This lesson covers the collaborative Git workflow.",
    overview=[
        "Add, view, and manage remote repositories.",
        "Fetch, pull, and push to remotes.",
        "Understand the difference between fetch and pull.",
        "Resolve merge conflicts.",
    ],
    body="""
<h2 class="lesson-section-title" id="remotes">Managing Remotes</h2>
""" + code("""# View configured remotes
git remote -v

# Add a remote
git remote add origin git@github.com:user/repo.git
git remote add upstream git@github.com:original/repo.git  # for forks

# Change a remote URL
git remote set-url origin git@github.com:user/new-repo.git

# Remove a remote
git remote remove upstream
""") + """
<h2 class="lesson-section-title" id="fetch-pull">Fetch vs. Pull</h2>
""" + code("""# fetch — downloads changes but does NOT merge them
# Safe to run any time — does not affect your working code
git fetch origin

# View what came in
git log origin/main --oneline

# Merge fetched changes manually
git merge origin/main

# pull = fetch + merge in one command
git pull origin main

# pull with rebase instead of merge
git pull --rebase origin main
""") + """
<h2 class="lesson-section-title" id="conflicts">Resolving Merge Conflicts</h2>
""" + code("""# A conflict marker looks like this in your file:
<<<<<<< HEAD
const greeting = "Hello";    // your version
=======
const greeting = "Hi there"; // incoming version
>>>>>>> feature/new-greeting

# Resolution:
# 1. Edit the file — keep one version, the other, or a mix
# 2. Remove the conflict markers entirely
# 3. Stage and commit the resolved file

const greeting = "Hi there"; // resolved

git add greeting.js
git commit  # creates a merge commit
"""),
    kc=[("What is the difference between git fetch and git pull?","fetch-pull"),
        ("What do the conflict markers <<<<<<< and >>>>>>> mean?","conflicts"),
        ("What is an upstream remote used for?","remotes")],
    assignments=[
        "Fork a repository on GitHub. Add both origin (your fork) and upstream (original) as remotes. Fetch from upstream and merge the latest changes.",
        "Deliberately create a merge conflict in a test repo and resolve it.",
    ],
    resources=[
        ("Atlassian — Git Remote","https://www.atlassian.com/git/tutorials/syncing"),
        ("MDN — Git collaboration workflow","https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/GitHub"),
        ("YouTube — Resolving Merge Conflicts (Traversy Media)","https://www.youtube.com/watch?v=xNVM5UxlFSA"),
    ])

    write("using-git-in-the-real-world","Using Git in the Real World",
    intro="Professional teams use structured Git workflows. This lesson covers the conventions and processes used at real software companies — pull requests, code review, and branch naming.",
    overview=[
        "Understand the GitHub Flow branching strategy.",
        "Create pull requests and understand the code review process.",
        "Write good pull request descriptions.",
        "Use conventional commit messages.",
    ],
    body="""
<h2 class="lesson-section-title" id="github-flow">GitHub Flow</h2>
<p>GitHub Flow is a lightweight workflow used by thousands of teams:</p>
<ol>
  <li>Create a branch from <code>main</code> with a descriptive name</li>
  <li>Make commits on the branch</li>
  <li>Open a Pull Request when ready for review</li>
  <li>Discuss and review the changes</li>
  <li>Merge into <code>main</code></li>
  <li>Deploy from <code>main</code></li>
</ol>
""" + code("""# Typical workflow
git switch main
git pull origin main              # start from latest main

git switch -c feature/add-search  # descriptive branch name

# ... make commits ...
git push origin feature/add-search

# Open a Pull Request on GitHub
# After review and approval:
git switch main
git merge feature/add-search
git push origin main
git branch -d feature/add-search
""") + """
<h2 class="lesson-section-title" id="pull-requests">Good Pull Requests</h2>
<p>A good PR description answers: <strong>what</strong> changed, <strong>why</strong>, and <strong>how to test it</strong>.</p>
""" + code("""# PR Title: short, imperative, like a commit message
# "Add search functionality to the header"

# PR Description template:
## What
Added a search bar to the site header that filters articles in real time.

## Why
Users reported difficulty finding older articles. The search addresses this.

## How to test
1. Navigate to the home page
2. Type in the search box
3. Verify articles filter as you type
4. Verify clearing the search restores all articles

## Screenshots
[before.png] [after.png]

## Checklist
- [x] Tests added
- [x] No console.log statements
- [x] Responsive on mobile
"""),
    kc=[("What are the six steps of GitHub Flow?","github-flow"),
        ("What three questions should a PR description answer?","pull-requests")],
    assignments=[
        "Use GitHub Flow for all new work from this point forward: always branch, always PR.",
        "Contribute to an open-source project on GitHub: fork, create a branch, make a small fix, and open a PR.",
    ],
    resources=[
        ("GitHub Flow Documentation","https://docs.github.com/en/get-started/quickstart/github-flow"),
        ("Conventional Commits","https://www.conventionalcommits.org/"),
        ("YouTube — GitHub Pull Requests (Traversy Media)","https://www.youtube.com/watch?v=For9VtrQx58"),
    ])

    write("project-javascript-final","Project: JavaScript Final Project",
    intro="This is your capstone project for the JavaScript course. You have full creative freedom — choose something that interests you. The requirements are about quality and process, not a specific product.",
    overview=[
        "Plan and build a JavaScript application of your own design.",
        "Apply all course concepts: modules, classes, async, testing, and Git workflow.",
        "Write clean, well-organised, tested code.",
        "Deploy the finished application publicly.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<ul>
  <li>Built with Webpack and ES6 Modules</li>
  <li>Uses at least one external API</li>
  <li>Uses async/await for all asynchronous operations</li>
  <li>Has at least 10 passing unit tests</li>
  <li>Linted with ESLint (zero errors)</li>
  <li>Responsive — works on mobile and desktop</li>
  <li>Deployed on GitHub Pages</li>
  <li>README with description, screenshots, and instructions</li>
</ul>

<h2 class="lesson-section-title" id="ideas">Project Ideas</h2>
<ul>
  <li>Recipe finder using a recipe API</li>
  <li>Movie/TV show browser using TMDB API</li>
  <li>GitHub user profile viewer</li>
  <li>Pokedex using the PokéAPI</li>
  <li>Currency converter using an exchange rate API</li>
  <li>Quote of the day generator</li>
  <li>News aggregator</li>
  <li>Or anything else that genuinely interests you</li>
</ul>

<h2 class="lesson-section-title" id="process">Recommended Process</h2>
""" + code("""# 1. Plan first — write out the user stories
#    "As a user, I can search for movies by title"
#    "As a user, I can see a movie's rating and description"
#    "As a user, I can save movies to a watchlist"

# 2. Set up the project structure
mkdir ~/devpath-projects/final-project
cd ~/devpath-projects/final-project
npm init -y
npm install --save-dev webpack webpack-cli jest eslint

# 3. Build in small increments — commit after each feature

# 4. Write tests before or alongside the logic

# 5. Deploy early — keep GitHub Pages up to date throughout
""") + """
<div class="callout callout-tip">
  <span class="callout-icon">💡</span>
  <p>Scope matters. A simple app done well is worth far more than a complex app done poorly. Start with the minimum viable product, then add features if time allows.</p>
</div>""",
    kc=[("What is the minimum number of passing unit tests required?","requirements"),
        ("What should a project README include?","requirements")],
    assignments=["Complete the Final JavaScript Project meeting all requirements.","Add the live URL and repository to your GitHub profile README."],
    resources=[
        ("Public APIs — List of free APIs","https://github.com/public-apis/public-apis"),
        ("MDN — JavaScript Guide","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"),
        ("YouTube — How to Build a Portfolio Project (Kevin Powell)","https://www.youtube.com/watch?v=0RyhO2K5hbE"),
    ])

    write("recursion","Recursion",
    intro="Recursion is when a function calls itself to solve a smaller version of the same problem. It is an elegant technique for problems that have a naturally recursive structure — trees, nested data, divide-and-conquer algorithms.",
    overview=[
        "Understand what recursion is and how it works.",
        "Identify the base case and recursive case.",
        "Trace the call stack of a recursive function.",
        "Know when recursion is preferable to iteration.",
    ],
    body="""
<h2 class="lesson-section-title" id="how-recursion-works">How Recursion Works</h2>
<p>Every recursive function has two parts:</p>
<ul>
  <li><strong>Base case</strong> — the condition that stops the recursion</li>
  <li><strong>Recursive case</strong> — the call to itself with a smaller/simpler version of the problem</li>
</ul>
""" + code("""// Classic example: factorial
// n! = n × (n-1) × (n-2) × ... × 1
// 5! = 5 × 4! = 5 × 4 × 3! = 5 × 4 × 3 × 2! = 5 × 4 × 3 × 2 × 1

function factorial(n) {
  if (n <= 1) return 1;          // BASE CASE — stop here
  return n * factorial(n - 1);   // RECURSIVE CASE — call with smaller n
}

factorial(5);
// = 5 * factorial(4)
// = 5 * 4 * factorial(3)
// = 5 * 4 * 3 * factorial(2)
// = 5 * 4 * 3 * 2 * factorial(1)
// = 5 * 4 * 3 * 2 * 1
// = 120
""") + """
<h2 class="lesson-section-title" id="examples">More Recursive Examples</h2>
""" + code("""// Sum of an array
function sum(arr) {
  if (arr.length === 0) return 0;             // base case
  return arr[0] + sum(arr.slice(1));          // recursive case
}
sum([1, 2, 3, 4, 5]); // 15

// Flatten a nested array
function flatten(arr) {
  return arr.reduce((flat, item) => {
    return flat.concat(Array.isArray(item) ? flatten(item) : item);
  }, []);
}
flatten([1, [2, [3, [4]], 5]]); // [1, 2, 3, 4, 5]

// Count nodes in a tree
function countNodes(node) {
  if (!node) return 0;           // base case: null node
  return 1 + countNodes(node.left) + countNodes(node.right);
}
""") + """
<h2 class="lesson-section-title" id="call-stack">The Call Stack and Stack Overflow</h2>
""" + code("""// Every recursive call adds a frame to the call stack
// Too many calls → stack overflow
function badRecursion(n) {
  return n + badRecursion(n - 1); // no base case!
  // RangeError: Maximum call stack size exceeded
}

// Tail-call optimisation (where supported)
// The recursive call is the LAST thing the function does
// Some engines can optimise this to avoid stack overflow
function factorial(n, acc = 1) {
  if (n <= 1) return acc;
  return factorial(n - 1, n * acc);  // tail call
}
"""),
    kc=[("What are the two required parts of every recursive function?","how-recursion-works"),
        ("What causes a stack overflow in a recursive function?","call-stack"),
        ("When is recursion more natural than iteration?","examples")],
    assignments=[
        "Implement a recursive function that counts how many times a letter appears in a nested array of strings.",
        "Implement a recursive deepEqual function that compares two objects with any level of nesting.",
    ],
    resources=[
        ("javascript.info — Recursion","https://javascript.info/recursion"),
        ("MDN — Recursion","https://developer.mozilla.org/en-US/docs/Glossary/Recursion"),
        ("YouTube — Recursion in JavaScript (Fireship)","https://www.youtube.com/watch?v=mHYrFs4_Mvk"),
    ])

    write("project-fibonacci","Project: Fibonacci",
    intro="The Fibonacci sequence is the classic recursion exercise. This project also introduces memoization — an optimisation technique that prevents redundant computation.",
    overview=[
        "Implement Fibonacci recursively.",
        "Understand why naive recursion is slow for Fibonacci.",
        "Implement memoization to optimise it.",
        "Implement an iterative version and compare performance.",
    ],
    body="""
<h2 class="lesson-section-title" id="fibonacci">The Fibonacci Sequence</h2>
<p>Each number is the sum of the two before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...</p>
""" + code("""// Naive recursive — correct but VERY slow
function fib(n) {
  if (n <= 1) return n;
  return fib(n - 1) + fib(n - 2);
}

// fib(50) takes minutes — recalculates the same values billions of times
// fib(5) calls fib(3) twice, fib(2) three times, fib(1) five times...
""") + """
<h2 class="lesson-section-title" id="memoization">Memoization</h2>
<p><strong>Memoization</strong> stores the result of expensive function calls and returns the cached result when the same input occurs again.</p>
""" + code("""// Memoized — O(n) instead of O(2^n)
function fibMemo(n, memo = {}) {
  if (n in memo) return memo[n];    // return cached result
  if (n <= 1) return n;

  memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
  return memo[n];
}

fibMemo(50);  // instant!

// General memoize utility
function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

const fastFib = memoize(function fib(n) {
  if (n <= 1) return n;
  return fastFib(n - 1) + fastFib(n - 2);
});
""") + """
<h2 class="lesson-section-title" id="iterative">Iterative Fibonacci</h2>
""" + code("""// O(n) time, O(1) space — most efficient
function fibIterative(n) {
  if (n <= 1) return n;
  let prev = 0, curr = 1;
  for (let i = 2; i <= n; i++) {
    [prev, curr] = [curr, prev + curr];
  }
  return curr;
}
"""),
    kc=[("Why is naive recursive Fibonacci exponentially slow?","fibonacci"),
        ("What is memoization?","memoization"),
        ("What are the time and space complexities of the iterative solution?","iterative")],
    assignments=[
        "Implement all three versions and measure their performance with console.time() for fib(40).",
        "Write unit tests that verify all three versions produce the same results.",
    ],
    resources=[
        ("javascript.info — Memoization","https://javascript.info/task/memoize"),
        ("MDN — Map","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map"),
        ("YouTube — Memoization Explained (Fireship)","https://www.youtube.com/watch?v=lWGLW_OzvZs"),
    ])

    write("time-complexity","Time Complexity",
    intro="Time complexity describes how an algorithm's runtime grows as the input size grows. Understanding Big O notation helps you write code that scales — and recognise when it will not.",
    overview=[
        "Understand Big O notation.",
        "Identify the time complexity of common patterns.",
        "Compare O(1), O(log n), O(n), O(n log n), O(n²), and O(2ⁿ).",
        "Analyse the complexity of your own code.",
    ],
    body="""
<h2 class="lesson-section-title" id="big-o">Big O Notation</h2>
<p>Big O describes the <em>worst-case</em> growth rate of an algorithm's runtime as the input size <em>n</em> approaches infinity. Constant factors are dropped — we care about the shape of growth, not the exact numbers.</p>

<h2 class="lesson-section-title" id="complexity-classes">Common Complexity Classes</h2>
""" + code("""// O(1) — Constant: does not grow with input size
function getFirst(arr) {
  return arr[0];  // same speed regardless of array length
}
// object property access, array indexing, Map.get(), Set.has()

// O(log n) — Logarithmic: each step halves the problem
function binarySearch(arr, target) {
  let lo = 0, hi = arr.length - 1;
  while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
  }
  return -1;
}
// 1 billion items → ~30 steps

// O(n) — Linear: grows directly with input
function findMax(arr) {
  let max = arr[0];
  for (const n of arr) {    // one pass through array
    if (n > max) max = n;
  }
  return max;
}

// O(n log n) — Linearithmic: efficient sorting algorithms
// Array.sort() in most engines, merge sort, quicksort

// O(n²) — Quadratic: nested loops over the input
function hasDuplicate(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] === arr[j]) return true;
    }
  }
  return false;
}
// Can be O(n) by using a Set instead

// O(2ⁿ) — Exponential: doubles with each addition to input
// Naive recursive Fibonacci
""") + """
<h2 class="lesson-section-title" id="rules">Rules for Analysis</h2>
<ul>
  <li>Drop constants: O(3n) → O(n)</li>
  <li>Drop lower-order terms: O(n² + n) → O(n²)</li>
  <li>Different inputs are different variables: O(n + m) not O(2n)</li>
  <li>Nested loops over the same input: multiply — O(n × n) = O(n²)</li>
  <li>Sequential operations: add — O(n + m)</li>
</ul>""",
    kc=[("What does Big O notation measure?","big-o"),
        ("What is the time complexity of accessing an array by index?","complexity-classes"),
        ("Why is O(n²) often a red flag?","complexity-classes")],
    assignments=[
        "Analyse the time complexity of every function in your Calculator and Library projects.",
        "Rewrite the hasDuplicate() example to be O(n) using a Set.",
    ],
    resources=[
        ("Big O Cheat Sheet","https://www.bigocheatsheet.com/"),
        ("javascript.info — Time Complexity","https://javascript.info/task/array-unique"),
        ("YouTube — Big O Notation (Fireship)","https://www.youtube.com/watch?v=g2o22C3CRfU"),
    ])

    write("space-complexity","Space Complexity",
    intro="Time complexity measures how long an algorithm takes. Space complexity measures how much memory it uses. Both matter, and sometimes you trade one for the other.",
    overview=[
        "Understand what space complexity measures.",
        "Identify O(1), O(n), and O(n²) space usage.",
        "Understand the space/time trade-off.",
        "Analyse the space usage of recursive functions.",
    ],
    body="""
<h2 class="lesson-section-title" id="what-is-space">What Space Complexity Measures</h2>
<p>Space complexity counts the <em>additional</em> memory an algorithm allocates — not the input itself (that is called <em>auxiliary space</em>). We are interested in how memory usage grows with input size.</p>

<h2 class="lesson-section-title" id="examples-space">Space Complexity Examples</h2>
""" + code("""// O(1) — Constant space: uses same amount of memory regardless of input
function sum(arr) {
  let total = 0;     // one variable — O(1)
  for (const n of arr) total += n;
  return total;
}

// O(n) — Linear space: creates data structure proportional to input
function doubleAll(arr) {
  const result = [];                // grows with arr.length
  for (const n of arr) result.push(n * 2);
  return result;
}

// O(n) — Recursive call stack also uses space
function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
  // Each call adds a frame to the call stack
  // n calls deep → O(n) space
}

// O(n²) — Quadratic space
function buildMatrix(n) {
  return Array.from({ length: n }, () => new Array(n).fill(0));
  // n × n matrix → O(n²) space
}
""") + """
<h2 class="lesson-section-title" id="tradeoff">The Space/Time Trade-Off</h2>
<p>Memoization is the classic example: trading space for time. By storing results (O(n) space), we avoid recomputing them (reducing time from O(2ⁿ) to O(n)).</p>
""" + code("""// Time O(n), Space O(1) — iterative
function fibFast(n) {
  let a = 0, b = 1;
  for (let i = 0; i < n; i++) [a, b] = [b, a + b];
  return a;
}

// Time O(n), Space O(n) — memoized
const memo = {};
function fibMemo(n) {
  if (n in memo) return memo[n];
  if (n <= 1) return n;
  return (memo[n] = fibMemo(n-1) + fibMemo(n-2));
}

// The iterative version is strictly better — same time, less space
"""),
    kc=[("What does space complexity measure?","what-is-space"),
        ("What space complexity does a recursive function typically add?","examples-space"),
        ("What is the classic example of a space/time trade-off?","tradeoff")],
    assignments=[
        "For every function you wrote in the Time Complexity lesson, also note its space complexity.",
        "Rewrite a recursive function from earlier to be iterative and note the space savings.",
    ],
    resources=[
        ("Big O Cheat Sheet — Space Complexity","https://www.bigocheatsheet.com/"),
        ("youtube — Space Complexity (CS Dojo)","https://www.youtube.com/watch?v=yOb0BL-84h8"),
    ])

    write("common-data-structures","Common Data Structures and Algorithms",
    intro="Data structures are ways of organising data in memory. Choosing the right structure dramatically affects performance. This lesson surveys the structures you will build in the following lessons.",
    overview=[
        "Understand why data structure choice matters.",
        "Compare arrays, stacks, queues, linked lists, hash maps, and trees.",
        "Know the Big O characteristics of each structure's core operations.",
    ],
    body="""
<h2 class="lesson-section-title" id="why-data-structures">Why Data Structures Matter</h2>
<p>The same problem can have dramatically different performance depending on the data structure used:</p>
""" + code("""// Checking if a value exists:

// Array — O(n) — must check each element
const arr = [1, 2, 3, 4, 5];
arr.includes(5);  // checks 1, then 2, then 3... up to 5

// Set — O(1) — hash lookup
const set = new Set([1, 2, 3, 4, 5]);
set.has(5);  // instant — no matter how large the set

// For 1 million items:
// Array.includes() → potentially 1,000,000 checks
// Set.has() → always ~1 check
""") + """
<h2 class="lesson-section-title" id="overview">Data Structure Overview</h2>
<ul>
  <li><strong>Array</strong> — Ordered list. O(1) access by index, O(n) search, O(n) insert/delete in middle.</li>
  <li><strong>Stack</strong> — LIFO (Last In First Out). O(1) push and pop. Used for: call stack, undo history, depth-first search.</li>
  <li><strong>Queue</strong> — FIFO (First In First Out). O(1) enqueue and dequeue. Used for: task queues, breadth-first search.</li>
  <li><strong>Linked List</strong> — Chain of nodes, each pointing to the next. O(1) insert/delete at known position, O(n) access by index.</li>
  <li><strong>Hash Map</strong> — Key-value store. O(1) average for get, set, has. The most universally useful data structure.</li>
  <li><strong>Binary Search Tree</strong> — Sorted tree structure. O(log n) average search, insert, delete. Used for: databases, file systems, sorted sets.</li>
</ul>
""" + code("""// JavaScript's built-in data structures
const arr  = [];           // Array
const map  = new Map();    // HashMap (ordered key-value pairs)
const set  = new Set();    // HashSet (unique values)

// Stack (use array)
const stack = [];
stack.push(1);    // push to top
stack.pop();      // remove from top

// Queue (use array or linked list)
const queue = [];
queue.push(1);    // enqueue
queue.shift();    // dequeue — O(n)! use a proper queue for performance
"""),
    kc=[("What is the time complexity for checking membership in a Set?","why-data-structures"),
        ("What is the difference between a stack and a queue?","overview"),
        ("When would you use a linked list instead of an array?","overview")],
    assignments=[
        "Read the MDN documentation for Map and Set. List 5 practical use cases for each.",
        "Implement a Stack and Queue class using arrays, with push/pop and enqueue/dequeue methods.",
    ],
    resources=[
        ("MDN — Map","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map"),
        ("javascript.info — Map and Set","https://javascript.info/map-set"),
        ("YouTube — Data Structures Explained (Fireship)","https://www.youtube.com/watch?v=ZBdE8DElQQU"),
    ])

    write("linked-lists","Linked Lists",
    intro="A linked list is a data structure where each element (node) stores its value and a pointer to the next node. Unlike arrays, linked lists do not store elements contiguously in memory — but they offer O(1) insertion and deletion at known positions.",
    overview=[
        "Understand the structure of a singly linked list.",
        "Implement a LinkedList class with append, prepend, and remove.",
        "Traverse a linked list.",
        "Understand the trade-offs versus arrays.",
    ],
    body="""
<h2 class="lesson-section-title" id="structure">Linked List Structure</h2>
""" + code("""// A node holds a value and a reference to the next node
class Node {
  constructor(value) {
    this.value = value;
    this.next  = null;   // points to the next node
  }
}

// A linked list tracks the head (and optionally tail) node
// head → [1] → [2] → [3] → null
""") + """
<h2 class="lesson-section-title" id="implementation">Implementation</h2>
""" + code("""class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  // Add to end — O(n) without tail pointer
  append(value) {
    const node = new Node(value);
    if (!this.head) {
      this.head = node;
    } else {
      let current = this.head;
      while (current.next) current = current.next;
      current.next = node;
    }
    this.size++;
  }

  // Add to front — O(1)
  prepend(value) {
    const node = new Node(value);
    node.next  = this.head;
    this.head  = node;
    this.size++;
  }

  // Remove by value — O(n)
  remove(value) {
    if (!this.head) return;
    if (this.head.value === value) {
      this.head = this.head.next;
      this.size--;
      return;
    }
    let current = this.head;
    while (current.next) {
      if (current.next.value === value) {
        current.next = current.next.next;
        this.size--;
        return;
      }
      current = current.next;
    }
  }

  // Get node at index — O(n)
  at(index) {
    let current = this.head;
    for (let i = 0; i < index; i++) {
      if (!current) return null;
      current = current.next;
    }
    return current;
  }

  // Convert to string for display
  toString() {
    const values = [];
    let current = this.head;
    while (current) {
      values.push(current.value);
      current = current.next;
    }
    return values.join(' → ') + ' → null';
  }
}
"""),
    kc=[("What is the time complexity of inserting at the front of a linked list?","implementation"),
        ("What is the time complexity of accessing the nth element of a linked list?","implementation"),
        ("What advantage does a linked list have over an array for insertions?","structure")],
    assignments=[
        "Implement the LinkedList class above. Add methods: contains(value), pop() (remove last), insertAt(index, value).",
        "Write unit tests for every method.",
    ],
    resources=[
        ("javascript.info — Linked List","https://javascript.info/task/reverse-linked-list"),
        ("YouTube — Linked Lists (Fireship)","https://www.youtube.com/watch?v=WwfhLC16bis"),
        ("MDN — Classes","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes"),
    ])

    write("project-linked-lists","Project: Linked Lists",
    intro="Build a complete, tested LinkedList implementation. This project solidifies your understanding of linked list operations and pointer manipulation.",
    overview=[
        "Implement a fully-featured LinkedList class.",
        "Handle edge cases: empty list, single node, out-of-bounds index.",
        "Write comprehensive unit tests.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<p>Your LinkedList class must have these methods:</p>
<ul>
  <li><code>append(value)</code> — add to end</li>
  <li><code>prepend(value)</code> — add to start</li>
  <li><code>size</code> — return total number of nodes</li>
  <li><code>head</code> — return first node</li>
  <li><code>tail</code> — return last node</li>
  <li><code>at(index)</code> — return node at given index</li>
  <li><code>pop()</code> — remove last element</li>
  <li><code>contains(value)</code> — return true/false</li>
  <li><code>find(value)</code> — return index of node with value, or null</li>
  <li><code>toString()</code> — format: <code>(value) -> (value) -> null</code></li>
  <li><code>insertAt(value, index)</code> — insert at given index</li>
  <li><code>removeAt(index)</code> — remove node at given index</li>
</ul>

<h2 class="lesson-section-title" id="testing">Testing Strategy</h2>
""" + code("""// Test each method, including edge cases
describe('LinkedList', () => {
  describe('append()', () => {
    it('adds a node to an empty list', () => {
      const list = new LinkedList();
      list.append(1);
      expect(list.head.value).toBe(1);
      expect(list.size).toBe(1);
    });

    it('adds multiple nodes in order', () => {
      const list = new LinkedList();
      list.append(1); list.append(2); list.append(3);
      expect(list.toString()).toBe('(1) -> (2) -> (3) -> null');
    });
  });

  describe('at()', () => {
    it('returns null for out-of-bounds index', () => {
      const list = new LinkedList();
      expect(list.at(5)).toBeNull();
    });
  });
});
"""),
    kc=[("What does the tail() method return?","requirements"),
        ("What should at() return for an out-of-bounds index?","testing")],
    assignments=["Complete the Linked Lists project meeting all requirements.","Achieve 100% test coverage for your implementation."],
    resources=[
        ("jest — Getting Started","https://jestjs.io/docs/getting-started"),
        ("javascript.info — Linked List exercises","https://javascript.info/task/reverse-linked-list"),
    ])

    write("hash-map","Hash Map",
    intro="A hash map (also called a hash table or dictionary) stores key-value pairs and provides O(1) average-case access. It is the single most useful data structure in everyday programming.",
    overview=[
        "Understand how a hash map works internally.",
        "Understand hash functions and collision handling.",
        "Know the time complexities of hash map operations.",
        "Implement a basic hash map.",
    ],
    body="""
<h2 class="lesson-section-title" id="how-it-works">How a Hash Map Works</h2>
<ol>
  <li>A hash map stores data in an internal array of <strong>buckets</strong></li>
  <li>To store a key-value pair, a <strong>hash function</strong> converts the key into an array index</li>
  <li>The value is stored at that index</li>
  <li>To retrieve a value, the same hash function finds the index again</li>
</ol>

<h2 class="lesson-section-title" id="hash-function">Hash Functions and Collisions</h2>
""" + code("""// Simple hash function for string keys
function hash(key, size) {
  let hashCode = 0;
  const prime = 31;  // prime numbers reduce collisions
  for (let i = 0; i < key.length; i++) {
    hashCode = (prime * hashCode + key.charCodeAt(i)) % size;
  }
  return hashCode;
}

hash("name", 16);    // → some index 0-15
hash("age",  16);    // → some index 0-15

// Collision: two different keys hash to the same index
// Solution 1: Separate chaining — store a linked list at each bucket
// Solution 2: Open addressing — find the next empty bucket
""") + """
<h2 class="lesson-section-title" id="implementation">Implementation</h2>
""" + code("""class HashMap {
  constructor(size = 16) {
    this.buckets = new Array(size).fill(null).map(() => []);
    this.size = 0;
  }

  hash(key) {
    let code = 0;
    for (let i = 0; i < key.length; i++) {
      code = (31 * code + key.charCodeAt(i)) % this.buckets.length;
    }
    return code;
  }

  set(key, value) {
    const index  = this.hash(key);
    const bucket = this.buckets[index];
    const existing = bucket.find(pair => pair[0] === key);

    if (existing) {
      existing[1] = value;    // update existing key
    } else {
      bucket.push([key, value]); // add new entry
      this.size++;
    }
  }

  get(key) {
    const bucket = this.buckets[this.hash(key)];
    const pair   = bucket.find(p => p[0] === key);
    return pair ? pair[1] : null;
  }

  has(key) {
    return this.get(key) !== null;
  }

  remove(key) {
    const index  = this.hash(key);
    const bucket = this.buckets[index];
    const i      = bucket.findIndex(p => p[0] === key);
    if (i === -1) return false;
    bucket.splice(i, 1);
    this.size--;
    return true;
  }
}
"""),
    kc=[("What does a hash function do?","hash-function"),
        ("What is a collision in a hash map and how is it handled?","hash-function"),
        ("What is the average time complexity of get() and set()?","how-it-works")],
    assignments=[
        "Read the implementation above carefully. Draw a diagram of the bucket array with a few stored entries.",
        "Implement a keys() method that returns an array of all keys.",
    ],
    resources=[
        ("javascript.info — Map and Set","https://javascript.info/map-set"),
        ("YouTube — Hash Tables (Fireship)","https://www.youtube.com/watch?v=shs0KM3wKv8"),
        ("YouTube — Hash Map Data Structure (CS Dojo)","https://www.youtube.com/watch?v=sfWyugl4JWA"),
    ])

    write("project-hashmap","Project: HashMap",
    intro="Implement a complete HashMap from scratch. This project deepens your understanding of how fundamental data structures work at the implementation level.",
    overview=[
        "Implement a full HashMap class with all standard operations.",
        "Handle hash collisions with separate chaining.",
        "Handle load factor and rehashing.",
        "Write comprehensive unit tests.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<p>Your HashMap must implement:</p>
<ul>
  <li><code>set(key, value)</code> — store or update a key-value pair</li>
  <li><code>get(key)</code> — retrieve value by key, null if not found</li>
  <li><code>has(key)</code> — return true/false</li>
  <li><code>remove(key)</code> — delete a key, return true/false</li>
  <li><code>length()</code> — return number of stored keys</li>
  <li><code>clear()</code> — remove all entries</li>
  <li><code>keys()</code> — return array of all keys</li>
  <li><code>values()</code> — return array of all values</li>
  <li><code>entries()</code> — return array of [key, value] pairs</li>
</ul>

<h2 class="lesson-section-title" id="load-factor">Load Factor and Rehashing</h2>
""" + code("""// Load factor = number of entries / number of buckets
// When load factor exceeds 0.75, rehash (double the bucket array)
// This keeps O(1) average performance as the map grows

set(key, value) {
  // ... existing set logic ...

  // After inserting, check load factor
  if (this.size / this.buckets.length > 0.75) {
    this.resize();
  }
}

resize() {
  const oldBuckets = this.buckets;
  this.buckets = new Array(oldBuckets.length * 2).fill(null).map(() => []);
  this.size = 0;

  // Re-insert all existing entries into the larger array
  for (const bucket of oldBuckets) {
    for (const [key, value] of bucket) {
      this.set(key, value);
    }
  }
}
"""),
    kc=[("What is load factor and why does it matter?","load-factor"),
        ("What happens when the load factor exceeds 0.75?","load-factor")],
    assignments=["Complete the HashMap project meeting all requirements.","Write tests that verify rehashing occurs correctly."],
    resources=[
        ("YouTube — Hash Table Implementation (CS Dojo)","https://www.youtube.com/watch?v=sfWyugl4JWA"),
        ("javascript.info — Object references","https://javascript.info/object-copy"),
    ])

    write("binary-search-trees","Binary Search Trees",
    intro="A binary search tree (BST) is a tree where each node has at most two children, and all left descendants are smaller than the node while all right descendants are larger. This ordering enables O(log n) search, insert, and delete.",
    overview=[
        "Understand the structure and ordering property of a BST.",
        "Implement insert, find, and traversal methods.",
        "Understand balanced vs unbalanced trees.",
        "Implement tree traversals: inorder, preorder, postorder, level-order.",
    ],
    body="""
<h2 class="lesson-section-title" id="bst-structure">BST Structure</h2>
""" + code("""class Node {
  constructor(value) {
    this.value = value;
    this.left  = null;
    this.right = null;
  }
}

//        8
//       / \\
//      4   12
//     / \\   \\
//    2   6   14
//
// All left descendants < parent
// All right descendants > parent
// Searching for 6: 8 → left → 4 → right → 6 ✓ (3 steps vs 5 in unsorted)
""") + """
<h2 class="lesson-section-title" id="implementation">Core Operations</h2>
""" + code("""class BST {
  constructor() { this.root = null; }

  insert(value) {
    const node = new Node(value);
    if (!this.root) { this.root = node; return; }

    let current = this.root;
    while (true) {
      if (value === current.value) return; // no duplicates
      if (value < current.value) {
        if (!current.left) { current.left = node; return; }
        current = current.left;
      } else {
        if (!current.right) { current.right = node; return; }
        current = current.right;
      }
    }
  }

  find(value) {
    let current = this.root;
    while (current) {
      if (value === current.value) return current;
      current = value < current.value ? current.left : current.right;
    }
    return null;
  }

  // Inorder traversal — visits nodes in sorted order
  inorder(node = this.root, result = []) {
    if (!node) return result;
    this.inorder(node.left, result);
    result.push(node.value);
    this.inorder(node.right, result);
    return result;
  }

  // Level-order (BFS) — visits nodes level by level
  levelOrder() {
    if (!this.root) return [];
    const result = [], queue = [this.root];
    while (queue.length) {
      const node = queue.shift();
      result.push(node.value);
      if (node.left)  queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    return result;
  }
}
"""),
    kc=[("What is the BST ordering property?","bst-structure"),
        ("What is the average time complexity of finding a value in a BST?","bst-structure"),
        ("What order does inorder traversal visit nodes?","implementation")],
    assignments=[
        "Implement the BST class above. Add methods: height(), isBalanced(), and delete(value).",
        "Write tests verifying that inorder traversal returns values in sorted order.",
    ],
    resources=[
        ("javascript.info — Binary Search Trees","https://javascript.info/task/tree-sum-parent"),
        ("YouTube — Binary Search Trees (Fireship)","https://www.youtube.com/watch?v=cWSn-djJVQk"),
        ("Visualgo — BST Visualization","https://visualgo.net/en/bst"),
    ])

    write("project-binary-search-trees","Project: Binary Search Trees",
    intro="Build a complete, tested, balanced BST implementation. This is one of the most technically challenging projects in the curriculum and a common topic in technical interviews.",
    overview=[
        "Build a BST with full CRUD operations.",
        "Implement tree balancing.",
        "Implement all four traversal methods.",
        "Write comprehensive unit tests.",
    ],
    body="""
<h2 class="lesson-section-title" id="requirements">Requirements</h2>
<p>Your Tree class must implement:</p>
<ul>
  <li><code>buildTree(array)</code> — build a balanced BST from a sorted array</li>
  <li><code>insert(value)</code></li>
  <li><code>delete(value)</code></li>
  <li><code>find(value)</code></li>
  <li><code>levelOrder(fn)</code> — BFS traversal, calls fn on each node</li>
  <li><code>inorder(fn)</code>, <code>preorder(fn)</code>, <code>postorder(fn)</code> — DFS traversals</li>
  <li><code>height(node)</code> — returns height of subtree</li>
  <li><code>depth(node)</code> — returns depth from root</li>
  <li><code>isBalanced()</code> — true if all subtrees differ in height by at most 1</li>
  <li><code>rebalance()</code> — rebalances an unbalanced tree</li>
</ul>

<h2 class="lesson-section-title" id="build-balanced">Building a Balanced Tree</h2>
""" + code("""// Build balanced BST from sorted array
// Strategy: take the middle element as root, recurse on left and right halves

function buildTree(arr) {
  if (arr.length === 0) return null;

  const mid  = Math.floor(arr.length / 2);
  const node = new Node(arr[mid]);

  node.left  = buildTree(arr.slice(0, mid));
  node.right = buildTree(arr.slice(mid + 1));

  return node;
}

// Usage: sort and deduplicate array first
const arr = [...new Set([3, 1, 4, 1, 5, 9, 2, 6])].sort((a,b) => a-b);
// [1, 2, 3, 4, 5, 6, 9]
const tree = new Tree();
tree.root = buildTree(arr);
"""),
    kc=[("How do you build a balanced BST from a sorted array?","build-balanced"),
        ("What does isBalanced() check?","requirements")],
    assignments=["Complete the BST project meeting all requirements.","Write a driver script that: builds a tree, verifies balance, unbalances it, rebalances it, and prints all traversals."],
    resources=[
        ("Visualgo — BST Visualization","https://visualgo.net/en/bst"),
        ("youtube — Balanced BST (CS Dojo)","https://www.youtube.com/watch?v=qYEZguBTG7w"),
    ])

    write("knights-travails","Project: Knights Travails",
    intro="Given a chess knight at any position on the board, find the shortest path to any other position. This project applies graph theory, BFS, and your data structures knowledge in a concrete problem.",
    overview=[
        "Model the chessboard as a graph.",
        "Use BFS to find the shortest path.",
        "Reconstruct and display the path.",
    ],
    body="""
<h2 class="lesson-section-title" id="problem">The Problem</h2>
<p>A chess knight moves in an L-shape: two squares in one direction and one square perpendicular. Your function <code>knightMoves([0,0], [3,3])</code> should output the shortest sequence of moves.</p>
""" + code("""// Expected output:
knightMoves([0,0], [3,3])
// You made it in 2 moves!
// Here's your path:
// [0,0]
// [2,1]
// [3,3]

knightMoves([0,0], [1,2])
// You made it in 1 move!
// Here's your path:
// [0,0]
// [1,2]
""") + """
<h2 class="lesson-section-title" id="approach">BFS Approach</h2>
""" + code("""function knightMoves(start, end) {
  // All possible knight moves (8 total)
  const moves = [
    [2,1],[2,-1],[-2,1],[-2,-1],
    [1,2],[1,-2],[-1,2],[-1,-2]
  ];

  // BFS — shortest path guaranteed
  const queue = [[start, [start]]]; // [position, path]
  const visited = new Set();
  visited.add(start.toString());

  while (queue.length > 0) {
    const [pos, path] = queue.shift();
    const [x, y] = pos;

    if (x === end[0] && y === end[1]) {
      console.log(`You made it in ${path.length - 1} moves!`);
      console.log("Here's your path:");
      path.forEach(p => console.log(p));
      return path;
    }

    for (const [dx, dy] of moves) {
      const next = [x + dx, y + dy];
      const key  = next.toString();

      // Only visit positions on the board (0-7) and not yet visited
      if (next[0] >= 0 && next[0] <= 7 &&
          next[1] >= 0 && next[1] <= 7 &&
          !visited.has(key)) {
        visited.add(key);
        queue.push([next, [...path, next]]);
      }
    }
  }
}
"""),
    kc=[("Why does BFS guarantee the shortest path?","approach"),
        ("Why do you need to track visited positions?","approach")],
    assignments=[
        "Implement knightMoves() meeting all requirements above.",
        "Test it for several start/end combinations. Verify the path length matches what a chess expert would expect.",
    ],
    resources=[
        ("MDN — Set","https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set"),
        ("javascript.info — BFS","https://javascript.info/task/shortest-path"),
        ("YouTube — Knight's Tour Algorithm","https://www.youtube.com/watch?v=ab_dY3dZFHM"),
    ])

    print("\nAll 40 JavaScript lessons seeded.")
    os.chdir(BASE)
    subprocess.run(["git","add","-A"], check=True)
    subprocess.run(["git","commit","-m","Seed: JavaScript course — all 40 lessons fully written"], check=True)
    subprocess.run(["git","push"], check=True)
    print("Pushed to GitHub.")

if __name__ == "__main__":
    seed()
