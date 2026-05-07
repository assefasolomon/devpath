(function () {
  "use strict";

  // Active nav
  function setActiveNav() {
    var path = window.location.pathname;
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      var href = a.getAttribute("href");
      if (!href) return;
      var abs = new URL(href, window.location.href).pathname;
      if (path === abs || (abs !== "/" && path.startsWith(abs.replace(/index\.html$/, "")))) {
        a.classList.add("active");
      }
    });
  }

  // Active sidebar link
  function setActiveSidebar() {
    var path = window.location.pathname;
    document.querySelectorAll(".sidebar-link").forEach(function (a) {
      var href = a.getAttribute("href");
      if (!href) return;
      var abs = new URL(href, window.location.href).pathname;
      if (path === abs) {
        a.classList.add("active");
        a.scrollIntoView({ block: "nearest" });
      }
    });
  }

  // Knowledge check scroll
  function initKnowledgeChecks() {
    document.querySelectorAll(".block-kc li a[data-target]").forEach(function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var target = document.getElementById(this.dataset.target);
        if (!target) return;
        target.scrollIntoView({ behavior: "smooth", block: "start" });
        target.style.outline = "2px solid #2563eb";
        target.style.borderRadius = "4px";
        setTimeout(function () { target.style.outline = ""; }, 2200);
      });
    });
  }

  // Copy buttons on code blocks
  function initCopyButtons() {
    document.querySelectorAll(".code-block").forEach(function (block) {
      var btn = document.createElement("button");
      btn.className = "copy-btn";
      btn.textContent = "Copy";
      block.appendChild(btn);
      btn.addEventListener("click", function () {
        var code = block.querySelector("code");
        if (!code) return;
        navigator.clipboard.writeText(code.innerText).then(function () {
          btn.textContent = "Copied!";
          btn.classList.add("copied");
          setTimeout(function () {
            btn.textContent = "Copy";
            btn.classList.remove("copied");
          }, 2000);
        });
      });
    });
  }

  // Mark completed toggle
  function initMarkCompleted() {
    document.querySelectorAll(".mark-complete-btn").forEach(function (btn) {
      var key = "completed_" + window.location.pathname;
      if (localStorage.getItem(key)) {
        btn.textContent = "✓ Completed";
        btn.style.background = "#059669";
      }
      btn.addEventListener("click", function () {
        if (localStorage.getItem(key)) {
          localStorage.removeItem(key);
          btn.textContent = "Mark Completed";
          btn.style.background = "";
        } else {
          localStorage.setItem(key, "1");
          btn.textContent = "✓ Completed";
          btn.style.background = "#059669";
        }
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    setActiveNav();
    setActiveSidebar();
    initKnowledgeChecks();
    initCopyButtons();
    initMarkCompleted();
  });
})();
