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
    initHighlighting();
  });
})();
// Syntax highlighting for code blocks
  function highlight(text) {
    return text
      // HTML comments
      .replace(/(&lt;!--[\s\S]*?--&gt;)/g, '<span class="token-comment">$1</span>')
      // HTML tags
      .replace(/(&lt;\/?)([\w-]+)/g, '<span class="token-punct">$1</span><span class="token-tag">$2</span>')
      // HTML attributes
      .replace(/\s([\w-]+)(=)/g, ' <span class="token-attr">$1</span><span class="token-punct">$2</span>')
      // Strings (quoted values)
      .replace(/(&#34;|&quot;|")(.*?)\1/g, '<span class="token-string">"$2"</span>')
      // CSS selectors (lines ending with {)
      .replace(/^([.#\w][\w\s,.-]*)(\s*\{)/gm, '<span class="token-selector">$1</span>$2')
      // CSS properties
      .replace(/^\s{2,}([\w-]+)(\s*:)/gm, '  <span class="token-property">$1</span>$2')
      // JS keywords
      .replace(/\b(const|let|var|function|return|if|else|for|while|class|import|export|default|new|this|typeof|async|await)\b/g,
        '<span class="token-keyword">$1</span>')
      // JS functions/methods
      .replace(/\b([\w]+)(\()/g, '<span class="token-function">$1</span><span class="token-punct">$2</span>')
      // Numbers
      .replace(/\b(\d+\.?\d*)\b/g, '<span class="token-number">$1</span>')
      // Shell comments
      .replace(/(#.+)$/gm, '<span class="token-comment">$1</span>');
  }

  function initHighlighting() {
    document.querySelectorAll(".code-block code").forEach(function (el) {
      el.innerHTML = highlight(el.innerHTML);
    });
  }
