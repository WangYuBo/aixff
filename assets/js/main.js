/* 2026 AI International Film Festival — aixff.org */
(function () {
  "use strict";

  var STORE_KEY = "aixff-lang";

  /* ---------- Language toggle ---------- */
  var zhEls = document.querySelectorAll(".zh");
  var enEls = document.querySelectorAll(".en");
  var toggle = document.getElementById("langToggle");

  function applyLang(lang) {
    var toEn = lang === "en";
    for (var i = 0; i < zhEls.length; i++) zhEls[i].hidden = toEn;
    for (var j = 0; j < enEls.length; j++) enEls[j].hidden = !toEn;
    document.documentElement.lang = toEn ? "en" : "zh-CN";
    if (toggle) toggle.textContent = toEn ? "中文" : "EN";
    /* 每页 body 上的 data-title-zh / data-title-en 声明各自双语标题；缺省回退首页标题 */
    var pageTitle = document.body.getAttribute(toEn ? "data-title-en" : "data-title-zh");
    document.title = pageTitle
      || (toEn
        ? "2026 AI International Film Festival"
        : "2026 AI国际影展 · AI International Film Festival");
    try { localStorage.setItem(STORE_KEY, lang); } catch (e) { /* private mode */ }
  }

  function langFromStorage() {
    try {
      var v = localStorage.getItem(STORE_KEY);
      return v === "en" || v === "zh" ? v : null;
    } catch (e) { return null; }
  }

  /* 首次访问且未存偏好时，按浏览器语言自动切换（服务“国际影展”定位） */
  function initialLang() {
    var stored = langFromStorage();
    if (stored) return stored;
    var nav = (navigator.language || navigator.userLanguage || "").toLowerCase();
    return nav.indexOf("en") === 0 ? "en" : "zh";
  }

  if (toggle) {
    toggle.addEventListener("click", function () {
      applyLang(document.documentElement.lang === "en" ? "zh" : "en");
    });
  }
  applyLang(initialLang());

  /* ---------- Mobile navigation ---------- */
  var burger = document.getElementById("navBurger");
  var links = document.getElementById("navLinks");

  function closeNav() {
    document.body.classList.remove("nav-open");
    if (burger) burger.setAttribute("aria-expanded", "false");
  }

  if (burger) {
    burger.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  if (links) {
    links.addEventListener("click", function (e) {
      if (e.target.closest("a")) closeNav();
    });
  }

  /* ---------- Scroll-spy nav highlight ---------- */
  var navAnchors = {};
  document.querySelectorAll(".nav-links a").forEach(function (a) {
    var id = a.getAttribute("href").slice(1);
    if (id) navAnchors[id] = a;
  });

  var sectionIds = Object.keys(navAnchors);
  if (sectionIds.length && "IntersectionObserver" in window) {
    var spy = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          sectionIds.forEach(function (id) {
            navAnchors[id].classList.toggle("active", id === entry.target.id);
          });
        });
      },
      { rootMargin: "-40% 0px -55% 0px" }
    );
    sectionIds.forEach(function (id) {
      var el = document.getElementById(id);
      if (el) spy.observe(el);
    });
  }
})();
