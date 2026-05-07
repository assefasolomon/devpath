(function () {
  "use strict";

  // ── Active nav link ──────────────────────────────────────
  function setActiveNav() {
    var path = window.location.pathname;
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      var href = a.getAttribute("href");
      if (!href) return;
      try {
        var abs = new URL(href, window.location.href).pathname;
        if (path === abs || (abs !== "/" && path.startsWith(abs.replace(/index\.html$/, "")))) {
          a.classList.add("active");
        }
      } catch(e) {}
    });
  }

  // ── Active sidebar link ──────────────────────────────────
  function setActiveSidebar() {
    var path = window.location.pathname;
    document.querySelectorAll(".sidebar-link").forEach(function (a) {
      var href = a.getAttribute("href");
      if (!href) return;
      try {
        var abs = new URL(href, window.location.href).pathname;
        if (path === abs) {
          a.classList.add("active");
          a.scrollIntoView({ block: "nearest" });
        }
      } catch(e) {}
    });
  }

  // ── Knowledge check scroll ───────────────────────────────
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

  // ── Mark completed toggle ────────────────────────────────
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

  // ── Syntax highlighting ──────────────────────────────────
  function highlight(text) {
    var isHTML = text.indexOf("&lt;") !== -1;
    var isCSS  = !isHTML && text.indexOf("{") !== -1 && text.indexOf(":") !== -1;

    if (isHTML) {
      return text
        .replace(/(&lt;!--[\s\S]*?--&gt;)/g,
          '<span class="token-comment">$1</span>')
        .replace(/(&lt;\/?)([\w-]+)/g,
          '<span class="token-punct">$1</span><span class="token-tag">$2</span>')
        .replace(/\b([\w-]+)(=&quot;)/g,
          '<span class="token-attr">$1</span><span class="token-punct">=</span><span class="token-string">&quot;')
        .replace(/&quot;([^&]*)&quot;/g,
          '&quot;<span class="token-value">$1</span>&quot;');
    }

    if (isCSS) {
      return text
        .replace(/(\/\*[\s\S]*?\*\/)/g,
          '<span class="token-comment">$1</span>')
        .replace(/^([.#:\w][\w\s,.()\[\]:>+~-]*)(\{)/gm,
          '<span class="token-selector">$1</span><span class="token-punct">{</span>')
        .replace(/^\s{2}([\w-]+)(\s*:)/gm,
          '  <span class="token-property">$1</span><span class="token-punct">:</span>')
        .replace(/:\s*([^;{}\n]+)(;)/g,
          ': <span class="token-value">$1</span><span class="token-punct">;</span>');
    }

    // JavaScript / Shell / Generic
    return text
      .replace(/(\/\/[^\n]*|#[^\n]*)/g,
        '<span class="token-comment">$1</span>')
      .replace(/(\/\*[\s\S]*?\*\/)/g,
        '<span class="token-comment">$1</span>')
      .replace(/(&#39;[^&#]*&#39;|&quot;[^&]*&quot;|`[^`]*`)/g,
        '<span class="token-string">$1</span>')
      .replace(/\b(const|let|var|function|return|if|else|for|while|do|switch|case|break|continue|class|extends|import|export|default|new|this|typeof|instanceof|async|await|try|catch|finally|throw|null|undefined|true|false)\b/g,
        '<span class="token-keyword">$1</span>')
      .replace(/\b([a-zA-Z_$][\w$]*)\s*\(/g,
        '<span class="token-function">$1</span>(')
      .replace(/\b(\d+\.?\d*)\b/g,
        '<span class="token-number">$1</span>');
  }

  function initHighlighting() {
    document.querySelectorAll(".code-block code").forEach(function (el) {
      el.innerHTML = highlight(el.innerHTML);
    });
  }

  // ── Copy buttons ─────────────────────────────────────────
  function initCopyButtons() {
    document.querySelectorAll(".code-block").forEach(function (block) {
      if (block.querySelector(".copy-btn")) return;

      var btn = document.createElement("button");
      btn.className = "copy-btn";
      btn.textContent = "Copy";
      btn.setAttribute("aria-label", "Copy code to clipboard");
      block.style.position = "relative";
      block.appendChild(btn);

      btn.addEventListener("click", function () {
        var code = block.querySelector("code");
        if (!code) return;
        var raw = code.innerText || code.textContent;

        navigator.clipboard.writeText(raw).then(function () {
          btn.textContent = "Copied!";
          btn.classList.add("copied");
          setTimeout(function () {
            btn.textContent = "Copy";
            btn.classList.remove("copied");
          }, 2000);
        }).catch(function () {
          // Fallback for older browsers
          var ta = document.createElement("textarea");
          ta.value = raw;
          ta.style.position = "fixed";
          ta.style.opacity = "0";
          document.body.appendChild(ta);
          ta.select();
          document.execCommand("copy");
          document.body.removeChild(ta);
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

  // ── Init (order matters: highlight first, then copy buttons) ──
  document.addEventListener("DOMContentLoaded", function () {
    setActiveNav();
    setActiveSidebar();
    initKnowledgeChecks();
    initMarkCompleted();
    initHighlighting();
    initCopyButtons();  // must run AFTER highlight so buttons aren't wiped
  });

})();
