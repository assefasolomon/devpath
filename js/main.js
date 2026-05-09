(function () {
  "use strict";

  /* ── Active nav link ─────────────────────────────────── */
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
      } catch (e) {}
    });
  }

  /* ── Active sidebar link ─────────────────────────────── */
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
      } catch (e) {}
    });
  }

  /* ── Knowledge check scroll ──────────────────────────── */
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

  /* ── Mark completed ──────────────────────────────────── */
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

  /* ── Syntax highlighting ─────────────────────────────── */
  function highlight(html) {
    var isHTML = html.indexOf("&lt;") !== -1;
    var isCSS  = !isHTML
      && html.indexOf("{") !== -1
      && html.indexOf(":") !== -1
      && !/\bconsole\b|\bconst\b|\blet\b|\bfunction\b/.test(html);

    if (isHTML) {
      return html
        .replace(/(&lt;!--)([\s\S]*?)(--&gt;)/g,
          '<span class="token-comment">$1$2$3</span>')
        .replace(/(&lt;\/)([\w][\w-]*)/g,
          '<span class="token-punct">$1</span><span class="token-tag">$2</span>')
        .replace(/(&lt;)([\w][\w-]*)/g,
          '<span class="token-punct">$1</span><span class="token-tag">$2</span>')
        .replace(/\s([\w-]+)(=)((?:&quot;|&#39;)[^&]*(?:&quot;|&#39;))/g,
          ' <span class="token-attr">$1</span><span class="token-punct">$2</span><span class="token-string">$3</span>');
    }

    if (isCSS) {
      return html
        .replace(/(\/\*[\s\S]*?\*\/)/g,
          '<span class="token-comment">$1</span>')
        .replace(/^([.#\w:[\]()>,\s~+*-][^{]*?)(\{)/gm,
          '<span class="token-selector">$1</span><span class="token-punct">{</span>')
        .replace(/^(\s{2,})([\w-]+)(\s*:)/gm,
          '$1<span class="token-property">$2</span><span class="token-punct">$3</span>')
        .replace(/:\s*([^;{}\/\n]+)(;)/g,
          ': <span class="token-value">$1</span><span class="token-punct">;</span>');
    }

    /* JavaScript / Shell / Generic */
    return html
      .replace(/((?:^|\n)([ \t]*))(#[^\n]*)/g,
        '$1<span class="token-comment">$3</span>')
      .replace(/(\/\/[^\n]*)/g,
        '<span class="token-comment">$1</span>')
      .replace(/(\/\*[\s\S]*?\*\/)/g,
        '<span class="token-comment">$1</span>')
      .replace(/(&quot;[^&\n]*&quot;|&#39;[^&\n]*&#39;|`[^`\n]*`)/g,
        '<span class="token-string">$1</span>')
      .replace(/\b(const|let|var|function|return|if|else|for|while|do|switch|case|break|continue|class|extends|import|export|default|new|this|typeof|instanceof|async|await|try|catch|finally|throw|null|undefined|true|false)\b/g,
        '<span class="token-keyword">$1</span>')
      .replace(/\b([A-Za-z_$][\w$]*)\s*(?=\()/g,
        '<span class="token-function">$1</span>')
      .replace(/\b(\d+\.?\d*)\b/g,
        '<span class="token-number">$1</span>');
  }

  function initHighlighting() {
    document.querySelectorAll(".code-block code").forEach(function (el) {
      el.dataset.raw = el.innerText || el.textContent;
      el.innerHTML = highlight(el.innerHTML);
    });
  }

  /* ── Copy buttons ─────────────────────────────────────── */
  function initCopyButtons() {
    document.querySelectorAll(".code-block").forEach(function (block) {
      if (block.querySelector(".copy-btn")) return;
      var btn = document.createElement("button");
      btn.className = "copy-btn";
      btn.textContent = "Copy";
      btn.setAttribute("aria-label", "Copy code");
      block.style.position = "relative";
      block.appendChild(btn);

      btn.addEventListener("click", function () {
        var code = block.querySelector("code");
        if (!code) return;
        var raw = code.dataset.raw || code.innerText || code.textContent;
        var done = function () {
          btn.textContent = "Copied!";
          btn.classList.add("copied");
          setTimeout(function () {
            btn.textContent = "Copy";
            btn.classList.remove("copied");
          }, 2000);
        };
        if (navigator.clipboard) {
          navigator.clipboard.writeText(raw).then(done).catch(function () {
            fallbackCopy(raw); done();
          });
        } else {
          fallbackCopy(raw); done();
        }
      });
    });
  }

  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.cssText = "position:fixed;top:0;left:0;opacity:0;";
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand("copy"); } catch (e) {}
    document.body.removeChild(ta);
  }

  /* ── Init ────────────────────────────────────────────── */
  document.addEventListener("DOMContentLoaded", function () {
    setActiveNav();
    setActiveSidebar();
    initKnowledgeChecks();
    initMarkCompleted();
    initHighlighting();
    initCopyButtons();
  });

})();
