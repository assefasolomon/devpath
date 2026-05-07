#!/usr/bin/env python3
import os

BASE = os.path.expanduser("~/devpath")

FOUNDATIONS_SECTIONS = [
    ("Introduction", [
        ("how-this-course-will-work",      "How This Course Will Work",        "lesson"),
        ("introduction-to-web-dev",        "Introduction to Web Development",  "lesson"),
        ("motivation-and-mindset",         "Motivation and Mindset",           "lesson"),
        ("asking-for-help",                "Asking For Help",                  "lesson"),
        ("join-the-community",             "Join the Odin Community",          "lesson"),
    ]),
    ("Prerequisites", [
        ("computer-basics",                "Computer Basics",                  "lesson"),
        ("how-does-the-web-work",          "How Does the Web Work?",           "lesson"),
        ("installation-overview",          "Installation Overview",            "lesson"),
        ("installations",                  "Installations",                    "lesson"),
        ("text-editors",                   "Text Editors",                     "lesson"),
        ("command-line-basics",            "Command Line Basics",              "lesson"),
        ("setting-up-git",                 "Setting Up Git",                   "lesson"),
    ]),
    ("Git Basics", [
        ("introduction-to-git",            "Introduction to Git",              "lesson"),
        ("git-basics",                     "Git Basics",                       "lesson"),
    ]),
    ("HTML Foundations", [
        ("introduction-to-html-css",       "Introduction to HTML and CSS",     "lesson"),
        ("elements-and-tags",              "Elements and Tags",                "lesson"),
        ("html-boilerplate",               "HTML Boilerplate",                 "lesson"),
        ("working-with-text",              "Working with Text",                "lesson"),
        ("lists",                          "Lists",                            "lesson"),
        ("links-and-images",               "Links and Images",                 "lesson"),
        ("commit-messages",                "Commit Messages",                  "lesson"),
        ("project-recipes",                "Project: Recipes",                 "project"),
    ]),
    ("CSS Foundations", [
        ("intro-to-css",                   "Intro to CSS",                     "lesson"),
        ("the-cascade",                    "The Cascade",                      "lesson"),
        ("inspecting-html-and-css",        "Inspecting HTML and CSS",          "lesson"),
        ("the-box-model",                  "The Box Model",                    "lesson"),
        ("block-and-inline",               "Block and Inline",                 "lesson"),
    ]),
    ("Flexbox", [
        ("introduction-to-flexbox",        "Introduction to Flexbox",          "lesson"),
        ("growing-and-shrinking",          "Growing and Shrinking",            "lesson"),
        ("axes",                           "Axes",                             "lesson"),
        ("alignment",                      "Alignment",                        "lesson"),
        ("project-landing-page",           "Project: Landing Page",            "project"),
    ]),
    ("JavaScript Basics", [
        ("variables-and-operators",        "Variables and Operators",          "lesson"),
        ("data-types-and-conditionals",    "Data Types and Conditionals",      "lesson"),
        ("javascript-developer-tools",     "JavaScript Developer Tools",       "lesson"),
        ("function-basics",                "Function Basics",                  "lesson"),
        ("problem-solving",                "Problem Solving",                  "lesson"),
        ("understanding-errors",           "Understanding Errors",             "lesson"),
        ("project-rock-paper-scissors",    "Project: Rock Paper Scissors",     "project"),
        ("clean-code",                     "Clean Code",                       "lesson"),
        ("installing-nodejs",              "Installing Node.js",               "lesson"),
        ("arrays-and-loops",               "Arrays and Loops",                 "lesson"),
        ("dom-manipulation-and-events",    "DOM Manipulation and Events",      "lesson"),
        ("revisiting-rock-paper-scissors", "Revisiting Rock Paper Scissors",   "lesson"),
        ("project-etch-a-sketch",          "Project: Etch-a-Sketch",           "project"),
        ("object-basics",                  "Object Basics",                    "lesson"),
        ("project-calculator",             "Project: Calculator",              "project"),
    ]),
    ("Conclusion", [
        ("choose-your-path",               "Choose Your Path Forward",         "lesson"),
    ]),
]

JS_PATH_COURSES = [
    {
        "slug": "intermediate-html-css",
        "title": "Intermediate HTML and CSS",
        "desc": "Go deeper with HTML forms, tables, SVG, and accessibility. Master advanced CSS selectors, custom properties, CSS Grid, animations, and responsive design.",
        "tags": ["HTML", "CSS", "Grid", "Responsive"],
        "sections": [
            ("Introduction", [
                ("int-html-css-intro",                  "Introduction",                                  "lesson"),
            ]),
            ("Intermediate HTML Concepts", [
                ("emmet",                               "Emmet",                                         "lesson"),
                ("svg",                                 "SVG",                                           "lesson"),
                ("html-tables",                         "Tables",                                        "lesson"),
            ]),
            ("Intermediate CSS Concepts", [
                ("default-styles",                      "Default Styles",                                "lesson"),
                ("css-units",                           "CSS Units",                                     "lesson"),
                ("more-text-styles",                    "More Text Styles",                              "lesson"),
                ("more-css-properties",                 "More CSS Properties",                           "lesson"),
                ("advanced-selectors",                  "Advanced Selectors",                            "lesson"),
                ("positioning",                         "Positioning",                                   "lesson"),
                ("css-functions",                       "CSS Functions",                                 "lesson"),
                ("custom-properties",                   "Custom Properties",                             "lesson"),
                ("browser-compatibility",               "Browser Compatibility",                         "lesson"),
            ]),
            ("Forms", [
                ("form-basics",                         "Form Basics",                                   "lesson"),
                ("form-validation",                     "Form Validation",                               "lesson"),
                ("project-sign-up-form",                "Project: Sign-Up Form",                         "project"),
            ]),
            ("Grid", [
                ("introduction-to-grid",                "Introduction to Grid",                          "lesson"),
                ("creating-a-grid",                     "Creating a Grid",                               "lesson"),
                ("positioning-grid-elements",           "Positioning Grid Elements",                     "lesson"),
                ("advanced-grid-properties",            "Advanced Grid Properties",                      "lesson"),
                ("using-flexbox-and-grid",              "Using Flexbox and Grid",                        "lesson"),
                ("project-admin-dashboard",             "Project: Admin Dashboard",                      "project"),
            ]),
            ("Accessibility", [
                ("introduction-to-web-accessibility",   "Introduction to Web Accessibility",             "lesson"),
                ("wcag",                                "The Web Content Accessibility Guidelines",      "lesson"),
                ("accessible-colors",                   "Accessible Colors",                             "lesson"),
                ("keyboard-navigation",                 "Keyboard Navigation",                           "lesson"),
                ("meaningful-text",                     "Meaningful Text",                               "lesson"),
                ("wai-aria",                            "WAI-ARIA",                                      "lesson"),
            ]),
            ("Responsive Design", [
                ("introduction-to-responsive-design",   "Introduction to Responsive Design",             "lesson"),
                ("natural-responsiveness",              "Natural Responsiveness",                        "lesson"),
                ("responsive-images",                   "Responsive Images",                             "lesson"),
                ("media-queries",                       "Media Queries",                                 "lesson"),
                ("project-homepage",                    "Project: Homepage",                             "project"),
            ]),
        ],
    },
    {
        "slug": "javascript",
        "title": "JavaScript",
        "desc": "Master JavaScript deeply: organizing code, object-oriented programming, async patterns, testing, and complex data structures through hands-on projects.",
        "tags": ["JavaScript", "OOP", "Async", "Testing", "Data Structures"],
        "sections": [
            ("Introduction", [
                ("javascript-intro",                        "Introduction",                                  "lesson"),
                ("a-quick-review",                          "A Quick Review",                                "lesson"),
            ]),
            ("Organizing Your JavaScript Code", [
                ("organizing-js-intro",                     "Organizing Your JavaScript Code Introduction",  "lesson"),
                ("objects-and-constructors",                "Objects and Object Constructors",               "lesson"),
                ("project-library",                         "Project: Library",                              "project"),
                ("factory-functions-and-the-module-pattern","Factory Functions and the Module Pattern",      "lesson"),
                ("classes",                                 "Classes",                                       "lesson"),
                ("es6-modules",                             "ES6 Modules",                                   "lesson"),
                ("webpack",                                 "Webpack",                                       "lesson"),
                ("project-restaurant-page",                 "Project: Restaurant Page",                      "project"),
                ("oop-principles",                          "OOP Principles",                                "lesson"),
                ("project-todo-list",                       "Project: Todo List",                            "project"),
            ]),
            ("JavaScript in the Real World", [
                ("linting",                                 "Linting",                                       "lesson"),
                ("dynamic-user-interface-interactions",     "Dynamic User Interface Interactions",           "lesson"),
                ("form-validation-with-javascript",         "Form Validation with JavaScript",               "lesson"),
                ("what-is-es6",                             "What is ES6?",                                  "lesson"),
            ]),
            ("Asynchronous JavaScript and APIs", [
                ("json",                                    "JSON",                                          "lesson"),
                ("asynchronous-code",                       "Asynchronous Code",                             "lesson"),
                ("working-with-apis",                       "Working with APIs",                             "lesson"),
                ("async-and-await",                         "Async and Await",                               "lesson"),
                ("project-weather-app",                     "Project: Weather App",                          "project"),
            ]),
            ("Testing JavaScript", [
                ("testing-basics",                          "Testing Basics",                                "lesson"),
                ("more-testing",                            "More Testing",                                  "lesson"),
                ("project-battleship",                      "Project: Battleship",                           "project"),
            ]),
            ("Intermediate Git", [
                ("a-deeper-look-at-git",                    "A Deeper Look at Git",                          "lesson"),
                ("working-with-remotes",                    "Working with Remotes",                          "lesson"),
                ("using-git-in-the-real-world",             "Using Git in the Real World",                   "lesson"),
            ]),
            ("Finishing Up with JavaScript", [
                ("project-javascript-final",                "Project: JavaScript Final Project",             "project"),
            ]),
            ("Computer Science", [
                ("recursion",                               "Recursion",                                     "lesson"),
                ("project-fibonacci",                       "Project: Fibonacci",                            "project"),
                ("time-complexity",                         "Time Complexity",                               "lesson"),
                ("space-complexity",                        "Space Complexity",                              "lesson"),
                ("common-data-structures",                  "Common Data Structures and Algorithms",         "lesson"),
                ("linked-lists",                            "Linked Lists",                                  "lesson"),
                ("project-linked-lists",                    "Project: Linked Lists",                         "project"),
                ("hash-map",                                "Hash Map",                                      "lesson"),
                ("project-hashmap",                         "Project: HashMap",                              "project"),
                ("binary-search-trees",                     "Binary Search Trees",                           "lesson"),
                ("project-binary-search-trees",             "Project: Binary Search Trees",                  "project"),
                ("knights-travails",                        "Project: Knights Travails",                     "project"),
            ]),
        ],
    },
    {
        "slug": "advanced-html-css",
        "title": "Advanced HTML and CSS",
        "desc": "Master performance, animation, and the fine details that separate good sites from great ones.",
        "tags": ["CSS Animations", "Performance", "Accessibility"],
        "sections": [
            ("Animation", [
                ("transforms",                          "Transforms",                                    "lesson"),
                ("transitions",                         "Transitions",                                   "lesson"),
                ("keyframes",                           "Keyframes",                                     "lesson"),
            ]),
            ("Accessibility", [
                ("accessibility-intro",                 "Introduction to Accessibility",                 "lesson"),
                ("wcag-adv",                            "The Web Content Accessibility Guidelines",      "lesson"),
                ("accessible-colors-adv",               "Accessible Colors",                             "lesson"),
                ("keyboard-navigation-adv",             "Keyboard Navigation",                           "lesson"),
                ("meaningful-text-adv",                 "Meaningful Text",                               "lesson"),
                ("wai-aria-adv",                        "WAI-ARIA",                                      "lesson"),
            ]),
            ("Responsive Design", [
                ("natural-responsiveness-adv",          "Natural Responsiveness",                        "lesson"),
                ("responsive-images-adv",               "Responsive Images",                             "lesson"),
                ("media-queries-adv",                   "Media Queries",                                 "lesson"),
                ("project-homepage-adv",                "Project: Homepage",                             "project"),
            ]),
        ],
    },
    {
        "slug": "react",
        "title": "React",
        "desc": "Build dynamic user interfaces with the most popular JavaScript UI library. Hooks, routing, testing, and real-world applications.",
        "tags": ["React", "Hooks", "React Router", "Testing"],
        "sections": [
            ("Introduction to React", [
                ("react-intro",                             "Introduction to React",                         "lesson"),
                ("getting-started-with-react",              "Getting Started with React",                    "lesson"),
                ("state-and-props",                         "State and Props",                               "lesson"),
                ("rendering-techniques",                    "Rendering Techniques",                          "lesson"),
                ("handling-inputs-and-rendering-lists",     "Handling Inputs and Rendering Lists",           "lesson"),
                ("project-cv-application",                  "Project: CV Application",                       "project"),
                ("passing-data-between-components",         "Passing Data Between Components",               "lesson"),
                ("project-memory-card",                     "Project: Memory Card",                          "project"),
            ]),
            ("Getting Deeper into React", [
                ("more-on-state",                           "More on State",                                 "lesson"),
                ("refs-and-memoization",                    "Refs and Memoization",                          "lesson"),
                ("project-shopping-cart",                   "Project: Shopping Cart",                        "project"),
            ]),
            ("Hooks", [
                ("introduction-to-react-hooks",             "Introduction to React Hooks",                   "lesson"),
                ("useeffect",                               "useEffect",                                     "lesson"),
                ("custom-hooks",                            "Custom Hooks",                                  "lesson"),
            ]),
            ("Class Components", [
                ("class-components",                        "Class Components",                              "lesson"),
            ]),
            ("React Ecosystem", [
                ("react-router",                            "React Router",                                  "lesson"),
                ("fetching-data-in-react",                  "Fetching Data in React",                        "lesson"),
                ("introduction-to-state-management",        "Introduction to State Management",              "lesson"),
                ("managing-state-with-the-context-api",     "Managing State with the Context API",           "lesson"),
                ("project-where-in-the-world",              "Project: Where in the World?",                  "project"),
            ]),
            ("Testing React", [
                ("introduction-to-react-testing",           "Introduction to React Testing",                 "lesson"),
                ("mocking-callbacks-and-components",        "Mocking Callbacks and Components",              "lesson"),
                ("project-battleship-react",                "Project: Battleship (React)",                   "project"),
            ]),
        ],
    },
    {
        "slug": "nodejs",
        "title": "NodeJS",
        "desc": "Take your JavaScript to the server side. Build REST APIs, work with databases, implement authentication, and deploy full-stack apps.",
        "tags": ["Node.js", "Express", "PostgreSQL", "REST APIs"],
        "sections": [
            ("Introduction to NodeJS", [
                ("introduction-to-nodejs",              "Introduction to NodeJS",                        "lesson"),
                ("getting-started",                     "Getting Started",                               "lesson"),
                ("debugging-node",                      "Debugging Node",                                "lesson"),
            ]),
            ("Express and Mongoose", [
                ("introduction-to-express",             "Introduction to Express",                       "lesson"),
                ("express-routes-and-controllers",      "Express Routes and Controllers",                "lesson"),
                ("express-views",                       "Express Views",                                 "lesson"),
                ("project-mini-message-board",          "Project: Mini Message Board",                   "project"),
                ("introduction-to-mongodb",             "Introduction to MongoDB",                       "lesson"),
                ("mongoose-primer",                     "Mongoose Primer",                               "lesson"),
                ("project-inventory-application",       "Project: Inventory Application",                "project"),
            ]),
            ("Authentication", [
                ("authentication-basics",               "Authentication Basics",                         "lesson"),
                ("security-configuration",              "Security Configuration",                        "lesson"),
                ("project-members-only",                "Project: Members Only",                         "project"),
            ]),
            ("APIs", [
                ("apis",                                "APIs",                                          "lesson"),
                ("api-security-and-authentication",     "API Security and Authentication",               "lesson"),
                ("project-blog-api",                    "Project: Blog API",                             "project"),
            ]),
            ("Testing Express", [
                ("testing-express",                     "Testing Express",                               "lesson"),
            ]),
            ("SQL and PostgreSQL", [
                ("sql-basics",                          "SQL Basics",                                    "lesson"),
                ("databases-and-sql",                   "Databases and SQL",                             "lesson"),
                ("knex-js",                             "Knex.js",                                       "lesson"),
                ("project-file-uploader",               "Project: File Uploader",                        "project"),
            ]),
            ("Finishing the Full Stack", [
                ("project-odinbook",                    "Project: Odin-Book",                            "project"),
            ]),
        ],
    },
    {
        "slug": "getting-hired",
        "title": "Getting Hired",
        "desc": "Turn your skills into your first developer job. Portfolio, resume, networking, technical interviews, and negotiating your offer.",
        "tags": ["Portfolio", "Interviews", "Job Search", "Career"],
        "sections": [
            ("Preparing to Get Hired", [
                ("introduction-to-getting-hired",       "Introduction to Getting Hired",                 "lesson"),
                ("how-to-get-hired",                    "How to Get Hired as a Web Developer",           "lesson"),
                ("strategy",                            "Strategy",                                      "lesson"),
                ("it-starts-with-you",                  "It Starts with You",                            "lesson"),
                ("what-companies-want",                 "What Do Companies Want?",                       "lesson"),
                ("what-you-can-do",                     "What Can You Do to Prepare?",                   "lesson"),
                ("building-your-portfolio",             "Building Your Portfolio",                       "lesson"),
            ]),
            ("Applying and Interviewing", [
                ("collecting-leads",                    "Collecting Leads",                              "lesson"),
                ("qualifying-leads",                    "Qualifying Leads",                              "lesson"),
                ("reaching-out",                        "Reaching Out",                                  "lesson"),
                ("preparing-for-interviews",            "Preparing for Interviews",                      "lesson"),
                ("the-first-interview",                 "The First Interview",                           "lesson"),
                ("the-technical-interview",             "The Technical Interview",                       "lesson"),
                ("after-the-interview",                 "After the Interview",                           "lesson"),
                ("handling-offers-and-negotiations",    "Handling Offers and Negotiations",              "lesson"),
            ]),
        ],
    },
]

RAILS_PATH_COURSES = [
    {
        "slug": "ruby",
        "title": "Ruby",
        "desc": "Learn Ruby from scratch. Cover the fundamentals, OOP, testing, and classic computer science topics.",
        "tags": ["Ruby", "OOP", "RSpec", "Algorithms"],
        "sections": [
            ("Introduction", [
                ("ruby-intro",                          "Introduction",                                  "lesson"),
            ]),
            ("Basic Ruby", [
                ("basic-ruby",                          "Basic Ruby",                                    "lesson"),
                ("project-caesar-cipher",               "Project: Caesar Cipher",                        "project"),
                ("sub-strings",                         "Project: Sub Strings",                          "project"),
                ("stock-picker",                        "Project: Stock Picker",                         "project"),
                ("bubble-sort",                         "Project: Bubble Sort",                          "project"),
            ]),
            ("Basic Ruby Objects", [
                ("object-oriented-programming",         "Object Oriented Programming",                   "lesson"),
                ("project-tic-tac-toe",                 "Project: Tic Tac Toe",                          "project"),
                ("project-mastermind",                  "Project: Mastermind",                           "project"),
            ]),
            ("Files and Serialization", [
                ("files-and-serialization",             "Files and Serialization",                       "lesson"),
                ("project-event-manager",               "Project: Event Manager",                        "project"),
                ("project-hangman",                     "Project: Hangman",                              "project"),
            ]),
            ("Advanced Ruby", [
                ("pattern-matching",                    "Pattern Matching",                              "lesson"),
                ("blocks",                              "Blocks",                                        "lesson"),
            ]),
            ("A Bit of Computer Science", [
                ("a-bit-of-computer-science",           "A Bit of Computer Science",                     "lesson"),
                ("project-recursion",                   "Project: Recursion",                            "project"),
                ("linked-lists",                        "Linked Lists",                                  "lesson"),
                ("project-linked-lists",                "Project: Linked Lists",                         "project"),
                ("hash-map",                            "Hash Map",                                      "lesson"),
                ("project-hashmap",                     "Project: HashMap",                              "project"),
                ("binary-search-trees",                 "Binary Search Trees",                           "lesson"),
                ("project-binary-search-trees",         "Project: Binary Search Trees",                  "project"),
                ("knights-travails",                    "Project: Knights Travails",                     "project"),
            ]),
            ("Testing Ruby with RSpec", [
                ("introduction-to-rspec",               "Introduction to RSpec",                         "lesson"),
                ("project-connect-four",                "Project: Connect Four",                         "project"),
            ]),
            ("Conclusion", [
                ("project-custom-enumerables",          "Project: Custom Enumerables",                   "project"),
            ]),
        ],
    },
    {
        "slug": "intermediate-html-css",
        "title": "Intermediate HTML and CSS",
        "desc": "Strengthen your front-end skills with advanced selectors, forms, accessibility, CSS Grid, and responsive design.",
        "tags": ["HTML", "CSS", "Grid", "Responsive"],
        "sections": [
            ("Introduction", [
                ("int-html-css-rails-intro",            "Introduction",                                  "lesson"),
            ]),
            ("Intermediate HTML Concepts", [
                ("emmet-rails",                         "Emmet",                                         "lesson"),
                ("svg-rails",                           "SVG",                                           "lesson"),
                ("html-tables-rails",                   "Tables",                                        "lesson"),
            ]),
            ("Intermediate CSS Concepts", [
                ("default-styles-rails",                "Default Styles",                                "lesson"),
                ("css-units-rails",                     "CSS Units",                                     "lesson"),
                ("more-text-styles-rails",              "More Text Styles",                              "lesson"),
                ("more-css-properties-rails",           "More CSS Properties",                           "lesson"),
                ("advanced-selectors-rails",            "Advanced Selectors",                            "lesson"),
                ("positioning-rails",                   "Positioning",                                   "lesson"),
                ("css-functions-rails",                 "CSS Functions",                                 "lesson"),
                ("custom-properties-rails",             "Custom Properties",                             "lesson"),
                ("browser-compatibility-rails",         "Browser Compatibility",                         "lesson"),
            ]),
            ("Forms", [
                ("form-basics-rails",                   "Form Basics",                                   "lesson"),
                ("form-validation-rails",               "Form Validation",                               "lesson"),
                ("project-sign-up-form-rails",          "Project: Sign-Up Form",                         "project"),
            ]),
            ("Grid", [
                ("introduction-to-grid-rails",          "Introduction to Grid",                          "lesson"),
                ("creating-a-grid-rails",               "Creating a Grid",                               "lesson"),
                ("positioning-grid-elements-rails",     "Positioning Grid Elements",                     "lesson"),
                ("advanced-grid-properties-rails",      "Advanced Grid Properties",                      "lesson"),
                ("project-admin-dashboard-rails",       "Project: Admin Dashboard",                      "project"),
            ]),
            ("Accessibility", [
                ("intro-to-accessibility-rails",        "Introduction to Web Accessibility",             "lesson"),
                ("wcag-rails",                          "The Web Content Accessibility Guidelines",      "lesson"),
                ("accessible-colors-rails",             "Accessible Colors",                             "lesson"),
                ("keyboard-navigation-rails",           "Keyboard Navigation",                           "lesson"),
                ("meaningful-text-rails",               "Meaningful Text",                               "lesson"),
                ("wai-aria-rails",                      "WAI-ARIA",                                      "lesson"),
            ]),
            ("Responsive Design", [
                ("natural-responsiveness-rails",        "Natural Responsiveness",                        "lesson"),
                ("responsive-images-rails",             "Responsive Images",                             "lesson"),
                ("media-queries-rails",                 "Media Queries",                                 "lesson"),
                ("project-homepage-rails",              "Project: Homepage",                             "project"),
            ]),
        ],
    },
    {
        "slug": "databases",
        "title": "Databases",
        "desc": "Understand relational databases and SQL — the language used to store, query, and manage structured data.",
        "tags": ["SQL", "PostgreSQL", "Databases"],
        "sections": [
            ("Databases", [
                ("databases-intro",                     "Databases",                                     "lesson"),
                ("databases-and-sql",                   "Databases and SQL",                             "lesson"),
                ("project-sql-exercises",               "Project: SQL Exercises",                        "project"),
            ]),
        ],
    },
    {
        "slug": "ruby-on-rails",
        "title": "Ruby on Rails",
        "desc": "Build full web applications quickly using Rails and the MVC pattern. Active Record, forms, authentication, and deployment.",
        "tags": ["Rails", "MVC", "Active Record", "PostgreSQL"],
        "sections": [
            ("Introduction to Rails", [
                ("rails-intro",                         "Introduction to Rails",                         "lesson"),
                ("getting-your-feet-wet",               "Getting Your Feet Wet",                         "project"),
            ]),
            ("Routes, Views, Controllers, and Assets", [
                ("routing",                             "Routing",                                       "lesson"),
                ("controllers",                         "Controllers",                                   "lesson"),
                ("views",                               "Views",                                         "lesson"),
                ("the-asset-pipeline",                  "The Asset Pipeline",                            "lesson"),
                ("project-blog-app",                    "Project: Blog App",                             "project"),
            ]),
            ("Active Record", [
                ("active-record-basics",                "Active Record Basics",                          "lesson"),
                ("active-record-queries",               "Active Record Queries",                         "lesson"),
                ("active-record-associations",          "Active Record Associations",                    "lesson"),
                ("project-micro-reddit",                "Project: Micro-Reddit",                         "project"),
            ]),
            ("Forms and Authentication", [
                ("forms-and-rails",                     "Forms and Rails",                               "lesson"),
                ("project-private-events",              "Project: Private Events",                       "project"),
                ("advanced-forms-and-active-record",    "Advanced Forms and Active Record",              "lesson"),
                ("project-flight-booker",               "Project: Flight Booker",                        "project"),
                ("authentication",                      "Authentication",                                "lesson"),
                ("project-members-only",                "Project: Members Only",                         "project"),
            ]),
            ("Advanced Topics", [
                ("installing-postgresql",               "Installing PostgreSQL",                         "lesson"),
                ("sessions-cookies-and-flashes",        "Sessions, Cookies, and Flashes",                "lesson"),
                ("action-mailer",                       "Sending Emails with Action Mailer",             "lesson"),
                ("advanced-topics",                     "Advanced Topics",                               "lesson"),
                ("api-basics",                          "APIs and Building Your Own",                    "lesson"),
                ("css-bundling",                        "CSS Bundling",                                  "lesson"),
                ("project-odinbook",                    "Project: Odin-Book",                            "project"),
            ]),
        ],
    },
    {
        "slug": "advanced-html-css",
        "title": "Advanced HTML and CSS",
        "desc": "Animations, advanced accessibility, and responsive design patterns to polish your Rails front-ends.",
        "tags": ["CSS Animations", "Performance", "Accessibility"],
        "sections": [
            ("Animation", [
                ("transforms-rails",                    "Transforms",                                    "lesson"),
                ("transitions-rails",                   "Transitions",                                   "lesson"),
                ("keyframes-rails",                     "Keyframes",                                     "lesson"),
            ]),
            ("Accessibility", [
                ("accessibility-intro-rails",           "Introduction to Accessibility",                 "lesson"),
                ("wcag-adv-rails",                      "The Web Content Accessibility Guidelines",      "lesson"),
                ("accessible-colors-adv-rails",         "Accessible Colors",                             "lesson"),
                ("keyboard-navigation-adv-rails",       "Keyboard Navigation",                           "lesson"),
                ("meaningful-text-adv-rails",           "Meaningful Text",                               "lesson"),
                ("wai-aria-adv-rails",                  "WAI-ARIA",                                      "lesson"),
            ]),
            ("Responsive Design", [
                ("natural-responsiveness-adv-rails",    "Natural Responsiveness",                        "lesson"),
                ("responsive-images-adv-rails",         "Responsive Images",                             "lesson"),
                ("media-queries-adv-rails",             "Media Queries",                                 "lesson"),
                ("project-homepage-adv-rails",          "Project: Homepage",                             "project"),
            ]),
        ],
    },
    {
        "slug": "getting-hired",
        "title": "Getting Hired",
        "desc": "Turn your Rails skills into a developer career. Portfolio, resume, interview prep, and landing your offer.",
        "tags": ["Portfolio", "Interviews", "Job Search", "Career"],
        "sections": [
            ("Preparing to Get Hired", [
                ("intro-getting-hired-rails",           "Introduction to Getting Hired",                 "lesson"),
                ("how-to-get-hired-rails",              "How to Get Hired as a Web Developer",           "lesson"),
                ("strategy-rails",                      "Strategy",                                      "lesson"),
                ("it-starts-with-you-rails",            "It Starts with You",                            "lesson"),
                ("what-companies-want-rails",           "What Do Companies Want?",                       "lesson"),
                ("what-you-can-do-rails",               "What Can You Do to Prepare?",                   "lesson"),
                ("building-your-portfolio-rails",       "Building Your Portfolio",                       "lesson"),
            ]),
            ("Applying and Interviewing", [
                ("collecting-leads-rails",              "Collecting Leads",                              "lesson"),
                ("qualifying-leads-rails",              "Qualifying Leads",                              "lesson"),
                ("reaching-out-rails",                  "Reaching Out",                                  "lesson"),
                ("preparing-for-interviews-rails",      "Preparing for Interviews",                      "lesson"),
                ("the-first-interview-rails",           "The First Interview",                           "lesson"),
                ("the-technical-interview-rails",       "The Technical Interview",                       "lesson"),
                ("after-the-interview-rails",           "After the Interview",                           "lesson"),
                ("handling-offers-rails",               "Handling Offers and Negotiations",              "lesson"),
            ]),
        ],
    },
]

LOGO_SVG = '<svg viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="14" cy="14" r="13" stroke="currentColor" stroke-width="1.8"/><path d="M8 14 L14 7 L20 14 L14 21 Z" fill="currentColor"/></svg>'

def depth_root(depth):
    return "../" * depth

def nav(root):
    return f"""<nav class="site-nav">
  <a href="{root}index.html" class="nav-logo">{LOGO_SVG} DevPath</a>
  <ul class="nav-links">
    <li><a href="{root}index.html">Home</a></li>
    <li><a href="{root}foundations/index.html">Foundations</a></li>
    <li><a href="{root}paths/full-stack-javascript/index.html">Full Stack JS</a></li>
    <li><a href="{root}paths/full-stack-ruby-on-rails/index.html">Full Stack Rails</a></li>
  </ul>
</nav>"""

def footer():
    return '<footer class="site-footer"><p>DevPath — inspired by <a href="https://www.theodinproject.com" target="_blank">The Odin Project</a>. Architecture ready for content seeding.</p></footer>'

def shell(title, root, body, depth):
    r = depth_root(depth)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | DevPath</title>
  <link rel="stylesheet" href="{r}css/styles.css">
</head>
<body>
{nav(r)}
{body}
{footer()}
<script src="{r}js/main.js"></script>
</body>
</html>"""

def breadcrumb(*crumbs):
    parts = []
    for i, (label, href) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            parts.append(f'<span class="breadcrumb-current">{label}</span>')
        else:
            parts.append(f'<a href="{href}">{label}</a>')
            parts.append('<span class="breadcrumb-sep">/</span>')
    return '<nav class="breadcrumb">' + " ".join(parts) + "</nav>"

def seed(title):
    return f'<div class="seed-notice"><strong>🌱 Content not yet seeded</strong>Replace this block with real content for <em>{title}</em>.</div>'

def sidebar(course_title, sections):
    html = f'<div class="sidebar-course-title">{course_title}</div>\n'
    for section_name, lessons in sections:
        html += f'<div class="sidebar-section"><div class="sidebar-section-label">{section_name}</div>\n'
        for slug, title, ltype in lessons:
            cls = "sidebar-link is-project" if ltype == "project" else "sidebar-link"
            html += f'<a href="{slug}.html" class="{cls}">{title}</a>\n'
        html += "</div>\n"
    return f'<aside class="sidebar">{html}</aside>'

def lesson_page(title, bc, sb, prev, nxt):
    prev_html = f'<a href="{prev[1]}" class="pagination-link prev"><span class="pagination-label">← Previous</span><span class="pagination-title">{prev[0]}</span></a>' if prev else "<span></span>"
    next_html = f'<a href="{nxt[1]}"  class="pagination-link next"><span class="pagination-label">Next →</span><span class="pagination-title">{nxt[0]}</span></a>'  if nxt  else "<span></span>"
    return f"""<div class="page-header"><div class="page-header-inner">{bc}<h1>{title}</h1></div></div>
<div class="lesson-layout">
  {sb}
  <main>
    <div class="lesson-body">
      <div class="block-intro">{seed(title)}</div>
      <div class="block-overview">
        <div class="block-overview-label">Lesson Overview</div>
        <ul>
          <li><!-- seed overview point 1 --></li>
          <li><!-- seed overview point 2 --></li>
          <li><!-- seed overview point 3 --></li>
        </ul>
      </div>
      <!-- seed: add <h2 id="..."> content sections here -->
      <div class="block-kc">
        <div class="block-kc-label">Knowledge Check</div>
        <p class="kc-note">Click a question to jump to the section that answers it.</p>
        <ol>
          <li><a href="#" data-target=""><!-- seed kc question 1 --></a></li>
          <li><a href="#" data-target=""><!-- seed kc question 2 --></a></li>
          <li><a href="#" data-target=""><!-- seed kc question 3 --></a></li>
        </ol>
      </div>
      <div class="block-assignments">
        <div class="block-assignments-label">Assignments</div>
        <ol>
          <li><!-- seed assignment 1 --></li>
          <li><!-- seed assignment 2 --></li>
        </ol>
      </div>
      <div class="block-resources">
        <div class="block-resources-label">Additional Resources</div>
        <ul>
          <li><a href="https://www.theodinproject.com" target="_blank">The Odin Project — original reference</a></li>
          <li><!-- seed resource 1 --></li>
          <li><!-- seed resource 2 --></li>
        </ul>
      </div>
    </div>
    <div class="lesson-pagination">{prev_html}{next_html}</div>
  </main>
</div>"""

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def gen_foundations():
    all_lessons = []
    for _, lessons in FOUNDATIONS_SECTIONS:
        all_lessons.extend(lessons)

    rows = ""
    for i, (slug, title, ltype) in enumerate(all_lessons):
        bc = "badge-project" if ltype == "project" else "badge-lesson"
        bt = "Project"       if ltype == "project" else "Lesson"
        rows += f'<li class="lesson-item"><span class="lesson-item-num">{i+1:02d}</span><a href="lessons/{slug}.html">{title}</a><span class="badge {bc}">{bt}</span></li>\n'

    bc = breadcrumb(("Home", "../index.html"), ("Foundations", "#"))
    body = f'<div class="page-header"><div class="page-header-inner">{bc}<h1>🧱 Foundations</h1><p class="subtitle">The starting point for every path. HTML, CSS, JavaScript, Git, and the command line — built through real projects.</p></div></div><div class="content-wrapper"><ul class="lesson-list">{rows}</ul></div>'
    write(f"{BASE}/foundations/index.html", shell("Foundations", "../", body, depth=1))

    sb = sidebar("Foundations", FOUNDATIONS_SECTIONS)
    for i, (slug, title, ltype) in enumerate(all_lessons):
        prev = (all_lessons[i-1][1], f"{all_lessons[i-1][0]}.html") if i > 0 else None
        nxt  = (all_lessons[i+1][1], f"{all_lessons[i+1][0]}.html") if i < len(all_lessons) - 1 else None
        bc   = breadcrumb(("Home","../../index.html"), ("Foundations","../index.html"), (title,"#"))
        body = lesson_page(title, bc, sb, prev, nxt)
        write(f"{BASE}/foundations/lessons/{slug}.html", shell(title, "../../", body, depth=2))

    print(f"  Foundations: {len(all_lessons)} lesson shells")

def gen_path(path_slug, path_title, path_icon, path_desc, courses):
    path_dir = f"{BASE}/paths/{path_slug}"

    cards = ""
    for i, c in enumerate(courses):
        tags = "".join(f'<span class="tag">{t}</span>' for t in c["tags"])
        cards += f'<a href="courses/{c["slug"]}/index.html" class="course-card"><h3><span class="course-num">{i+1:02d} —</span> {c["title"]}</h3><p>{c["desc"]}</p><div class="course-card-meta">{tags}</div></a>\n'

    bc   = breadcrumb(("Home","../../index.html"), (path_title,"#"))
    body = f'<div class="page-header"><div class="page-header-inner">{bc}<h1>{path_icon} {path_title}</h1><p class="subtitle">{path_desc}</p></div></div><div class="content-wrapper"><div class="course-grid">{cards}</div></div>'
    write(f"{path_dir}/index.html", shell(path_title, "../../", body, depth=2))

    total = 0
    for course in courses:
        cs   = course["slug"]
        ct   = course["title"]
        cdir = f"{path_dir}/courses/{cs}"

        all_lessons = []
        for _, lessons in course["sections"]:
            all_lessons.extend(lessons)
        total += len(all_lessons)

        rows = ""
        for i, (slug, title, ltype) in enumerate(all_lessons):
            bc2 = "badge-project" if ltype == "project" else "badge-lesson"
            bt  = "Project"       if ltype == "project" else "Lesson"
            rows += f'<li class="lesson-item"><span class="lesson-item-num">{i+1:02d}</span><a href="lessons/{slug}.html">{title}</a><span class="badge {bc2}">{bt}</span></li>\n'

        tags = "".join(f'<span class="tag">{t}</span>' for t in course["tags"])
        bc   = breadcrumb(("Home","../../../../index.html"), (path_title,"../../index.html"), (ct,"#"))
        body = f'<div class="page-header"><div class="page-header-inner">{bc}<h1>{ct}</h1><p class="subtitle">{course["desc"]}</p><div style="margin-top:.85rem;">{tags}</div></div></div><div class="content-wrapper"><ul class="lesson-list">{rows}</ul></div>'
        write(f"{cdir}/index.html", shell(ct, "../../../../", body, depth=4))

        sb = sidebar(ct, course["sections"])
        for i, (slug, title, ltype) in enumerate(all_lessons):
            prev = (all_lessons[i-1][1], f"{all_lessons[i-1][0]}.html") if i > 0 else None
            nxt  = (all_lessons[i+1][1], f"{all_lessons[i+1][0]}.html") if i < len(all_lessons) - 1 else None
            bc   = breadcrumb(("Home","../../../../../../index.html"), (path_title,"../../../../index.html"), (ct,"../../index.html"), (title,"#"))
            body = lesson_page(title, bc, sb, prev, nxt)
            write(f"{cdir}/lessons/{slug}.html", shell(title, "../../../../../../", body, depth=5))

    print(f"  {path_title}: {len(courses)} courses, {total} lesson shells")

def gen_homepage():
    body = """<section class="hero">
  <span class="hero-label">Free · Open · Project-Based</span>
  <h1>Your path to becoming a<br><em>full-stack developer</em></h1>
  <p>A structured, hands-on curriculum that takes you from zero to job-ready. No fees. No fluff.</p>
  <div class="hero-actions">
    <a href="foundations/index.html" class="btn btn-primary">Start with Foundations →</a>
    <a href="paths/full-stack-javascript/index.html" class="btn btn-outline">Browse Paths</a>
  </div>
</section>
<section class="section">
  <div class="section-header"><h2>Choose Your Learning Path</h2><p>All paths start with Foundations. After that, pick the track that fits your goals.</p></div>
  <div class="path-grid">
    <a href="foundations/index.html" class="path-card" data-path="foundations">
      <div class="path-card-icon">🧱</div>
      <h3>Foundations</h3>
      <p>Start here — no exceptions. HTML, CSS, JavaScript, Git, and the command line through real projects.</p>
      <div class="path-tags"><span class="tag">HTML &amp; CSS</span><span class="tag">JavaScript</span><span class="tag">Git</span><span class="tag">5 projects</span></div>
    </a>
    <a href="paths/full-stack-javascript/index.html" class="path-card" data-path="js">
      <div class="path-card-icon">⚡</div>
      <h3>Full Stack JavaScript</h3>
      <p>Go deep with JavaScript. React on the front-end, Node.js and Express on the back-end, PostgreSQL for data.</p>
      <div class="path-tags"><span class="tag">JavaScript</span><span class="tag">React</span><span class="tag">Node.js</span><span class="tag">PostgreSQL</span></div>
    </a>
    <a href="paths/full-stack-ruby-on-rails/index.html" class="path-card" data-path="rails">
      <div class="path-card-icon">💎</div>
      <h3>Full Stack Ruby on Rails</h3>
      <p>Learn Ruby, then harness Rails to build polished web applications from back to front.</p>
      <div class="path-tags"><span class="tag">Ruby</span><span class="tag">Rails</span><span class="tag">SQL</span><span class="tag">MVC</span></div>
    </a>
  </div>
</section>"""
    write(f"{BASE}/index.html", shell("Learn Full-Stack Web Development", "", body, depth=0))
    print("  Homepage generated")

if __name__ == "__main__":
    print("Building DevPath architecture...")
    gen_homepage()
    gen_foundations()
    gen_path("full-stack-javascript",    "Full Stack JavaScript",    "⚡", "The complete JavaScript curriculum — Intermediate HTML/CSS, JavaScript, React, Node.js, and Getting Hired. Take courses in order.", JS_PATH_COURSES)
    gen_path("full-stack-ruby-on-rails", "Full Stack Ruby on Rails", "💎", "The complete Ruby on Rails curriculum — Ruby, Databases, Rails, Advanced CSS, and Getting Hired. Take courses in order.",    RAILS_PATH_COURSES)
    import subprocess
    n = len(subprocess.run(["find", BASE, "-name","*.html"], capture_output=True, text=True).stdout.strip().split("\n"))
    print(f"\nDone — {n} HTML files in ~/devpath/")
