/**
 * Les <nr> · <titel> (<context>, <klas>) — script.js
 * Uit _sjablonen/lespakket (basis: les 06 ORLO, 08-10-2026).
 * Opbouw naar het voorbeeld van PedalPro: links de route, midden één stap,
 * rechts een checklist met concrete taken.
 *
 * - één stap tegelijk tonen; de laatst geopende stap wordt onthouden
 * - checklist: voortgang, afgewerkte stappen krijgen een vinkje in de route
 * - op een smal scherm toont de checklist alleen de taken van de huidige stap
 * - in de laatste stap (data-laatste-stap op body) staat de hele checklist open
 * - handelingen met stapjes: bij de start dicht (Kort); de leerling opent ze met Toon stapjes
 * - zelftest met directe feedback (wordt niet bewaard)
 * - screenshot-plaatsen: tonen de afbeelding alleen als het bestand bestaat
 * - melding als alles afgevinkt is
 *
 * localStorage bewaart alleen vinkjes en de stap. Geen persoonsgegevens.
 * Geen externe bibliotheken.
 */
(function () {
  'use strict';

  var body = document.body;
  body.classList.add('js');
  var PREFIX = body.getAttribute('data-storage') || 'lespakket_v1_';
  var LAATSTE = body.getAttribute('data-laatste-stap') || '6';
  var teacherMode = new URLSearchParams(window.location.search).has('leraar');
  if (teacherMode) body.classList.add('teacher');

  /* ---------- Opslag (werkt ook als localStorage geblokkeerd is) ---------- */
  function store(key, value) {
    try { localStorage.setItem(PREFIX + key, JSON.stringify(value)); } catch (e) { /* geen opslag */ }
  }
  function load(key, fallback) {
    try {
      var raw = localStorage.getItem(PREFIX + key);
      return raw === null ? fallback : JSON.parse(raw);
    } catch (e) { return fallback; }
  }

  function all(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  /* ---------- 1. Checklist ---------- */
  var checklist = document.getElementById('checklist');
  var checks = all('.cl-item input[type="checkbox"]');
  var groups = all('.cl-group');
  var fill = document.getElementById('clFill');
  var count = document.getElementById('clCount');
  var klaar = document.getElementById('klaar');
  var navButtons = all('.nav-btn[data-step]');

  var saved = load('vinkjes', []);
  checks.forEach(function (cb) { cb.checked = saved.indexOf(cb.id) !== -1; });

  function updateProgress(fromUser) {
    var done = checks.filter(function (c) { return c.checked; }).length;
    var pct = checks.length ? Math.round(done / checks.length * 100) : 0;
    fill.style.width = pct + '%';
    fill.parentElement.setAttribute('aria-valuenow', String(pct));
    count.textContent = done + ' van ' + checks.length + ' klaar';

    groups.forEach(function (g) {
      var boxes = all('input[type="checkbox"]', g);
      var groupDone = boxes.length > 0 && boxes.every(function (b) { return b.checked; });
      g.classList.toggle('done', groupDone);
      var btn = document.querySelector('.nav-btn[data-step="' + g.getAttribute('data-step') + '"]');
      if (btn) btn.classList.toggle('done', groupDone);
    });

    // Melding alleen op het moment dat het laatste vinkje gezet wordt
    if (fromUser && done === checks.length && checks.length > 0) openKlaar();
  }

  checks.forEach(function (cb) {
    cb.addEventListener('change', function () {
      store('vinkjes', checks.filter(function (c) { return c.checked; }).map(function (c) { return c.id; }));
      updateProgress(true);
    });
  });

  // Smal scherm: alleen de huidige stap, met een knop om alles te tonen
  var toggle = document.getElementById('clToggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = checklist.classList.toggle('alles');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.textContent = open ? 'Toon minder' : 'Toon alles';
    });
  }

  function markCurrentGroup(step) {
    var any = false;
    groups.forEach(function (g) {
      // In de laatste stap loop je de hele lijst na: dan zijn alle groepen "huidig"
      var cur = step === LAATSTE || g.getAttribute('data-step') === step;
      g.classList.toggle('current', cur);
      if (cur) any = true;
    });
    checklist.classList.toggle('leeg', !any);
  }

  /* ---------- 2. Stappen ---------- */
  var panes = all('.pane');
  var order = panes.map(function (p) { return p.id.replace('pane-', ''); });

  function showStep(key, focus) {
    if (order.indexOf(key) === -1) key = order[0];
    panes.forEach(function (p) { p.classList.toggle('active', p.id === 'pane-' + key); });
    navButtons.forEach(function (b) {
      if (b.getAttribute('data-step') === key) b.setAttribute('aria-current', 'step');
      else b.removeAttribute('aria-current');
    });
    markCurrentGroup(key);
    store('stap', key);
    if (history.replaceState) history.replaceState(null, '', '#' + key);
    window.scrollTo(0, 0);
    if (focus) {
      var h = document.querySelector('#pane-' + key + ' h1, #pane-' + key + ' h2');
      if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
    }
  }

  navButtons.forEach(function (b) {
    b.addEventListener('click', function () { showStep(b.getAttribute('data-step'), true); });
  });
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-goto]');
    if (!t) return;
    e.preventDefault();
    showStep(t.getAttribute('data-goto'), true);
  });

  /* ---------- 3b. Stap voor stap of Kort (11-10-2026) ----------
   * Stap voor stap: elke handeling staat open, met haar kleine stapjes en een beeld.
   * Kort: alleen de handelingen; een leerling klapt zelf open wat ze niet weet.
   * Een handeling met data-dicht (alleen voor wie ze nodig heeft) blijft dicht tot de leerling ze opent.
   * De beginstand komt uit data-modus-start op body (standaard kort, Jonas 18-10-2026). Sinds 18-10-2026
   * staat de knop niet meer op de pagina (Jonas: "Doe maar voor iedereen"): de leerling opent per handeling
   * Toon stapjes. Zonder knop telt alleen data-modus-start; met een knop wordt de keuze per les onthouden. */
  var modusBtns = all('.modus-btn');
  var stapjes = all('details.stapjes');
  function zetModus(m, bewaar) {
    if (m !== 'stap') m = 'kort';
    body.classList.toggle('modus-kort', m === 'kort');
    stapjes.forEach(function (d) { d.open = (m === 'stap') && !d.hasAttribute('data-dicht'); });
    modusBtns.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-modus') === m ? 'true' : 'false'); });
    if (bewaar) store('modus', m);
  }
  modusBtns.forEach(function (b) {
    b.addEventListener('click', function () { zetModus(b.getAttribute('data-modus'), true); });
  });
  var modusStart = body.getAttribute('data-modus-start') || 'kort';
  zetModus(modusBtns.length ? load('modus', modusStart) : modusStart, false);

  /* ---------- 4. Vinkjes wissen ---------- */
  var reset = document.getElementById('btnReset');
  if (reset) {
    reset.addEventListener('click', function () {
      if (!window.confirm('Wil je alle vinkjes op deze pagina wissen? Je werkdocument en je mappen veranderen niet.')) return;
      checks.forEach(function (c) { c.checked = false; });
      store('vinkjes', []);
      updateProgress(false);
    });
  }

  /* ---------- 5. Klaar! ---------- */
  var lastFocus = null;
  function openKlaar() {
    if (!klaar) return;
    lastFocus = document.activeElement;
    klaar.hidden = false;
    var btn = document.getElementById('klaarSluit');
    if (btn) btn.focus();
  }
  function closeKlaar() {
    if (!klaar || klaar.hidden) return;
    klaar.hidden = true;
    if (lastFocus) lastFocus.focus();
  }
  if (klaar) {
    document.getElementById('klaarSluit').addEventListener('click', closeKlaar);
    klaar.addEventListener('click', function (e) { if (e.target === klaar) closeKlaar(); });
  }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeKlaar(); });

  /* ---------- 6. Zelftest ---------- */
  all('.quiz-q').forEach(function (q) {
    var fb = q.querySelector('.feedback');
    all('button', q).forEach(function (btn) {
      btn.addEventListener('click', function () {
        all('button', q).forEach(function (b) { b.classList.remove('right', 'wrong'); });
        var ok = btn.hasAttribute('data-right');
        btn.classList.add(ok ? 'right' : 'wrong');
        if (fb) fb.textContent = ok ? (q.getAttribute('data-ok') || 'Juist!') : (q.getAttribute('data-nok') || 'Nog niet. Probeer opnieuw.');
      });
    });
  });

  /* ---------- 6b. Inleveren pas na de zelftest (15-10-2026) ----------
   * Een todo-box met data-na-zelftest="<id van een vinkje>" blijft dicht tot alle vragen van de zelftest in
   * dezelfde stap juist zijn (Jonas: anders slaan ze de zelftest over en leveren ze meteen in). Opnieuw
   * proberen mag. Eenmaal open blijft hij open, ook na herladen, en het vinkje gaat aan. Zonder JavaScript
   * en met ?leraar staat alles open. Heeft de slotregel data-codewoord, dan toont ze dat woord als alles
   * juist is: de leerling typt het in het werkdocument (staat niet in de tekst, dus niet in ai-bron.txt). */
  all('[data-na-zelftest]').forEach(function (box) {
    var pane = box.closest('.pane');
    var vragen = all('.quiz-q', pane);
    var slot = pane.querySelector('.slot');
    var tekst = slot && slot.querySelector('.slot-tekst');
    var sleutel = 'open_' + pane.id;
    var vink = document.getElementById(box.getAttribute('data-na-zelftest'));
    function juist() { return vragen.filter(function (q) { return q.querySelector('button.right'); }).length; }
    function toon(open) {
      box.hidden = !open;
      if (!slot) return;
      slot.classList.toggle('open', open);
      var n = vragen.length - juist();
      var code = slot.getAttribute('data-codewoord');   // het bewijs in het werkdocument (sinds 15-10-2026)
      if (!tekst) return;
      if (open && code) {
        tekst.textContent = 'Alles juist. Jouw codewoord is ';
        var b = document.createElement('strong');
        b.className = 'codewoord';
        b.textContent = code;
        tekst.appendChild(b);
        tekst.appendChild(document.createTextNode('. Typ het in je werkdocument. Zo lever je in:'));
      } else {
        tekst.textContent = open ? 'Alles juist. Zo lever je in:' :
          'Nog ' + n + (n === 1 ? ' vraag' : ' vragen') + ' juist te beantwoorden. Dan zie je hier hoe je inlevert.';
      }
    }
    function maakOpen() {
      store(sleutel, true);
      toon(true);
      if (vink && !vink.checked) { vink.checked = true; vink.dispatchEvent(new Event('change')); }
      setTimeout(function () {             // de regel net onder de vaste balk bovenaan, de stappen eronder
        if (!slot) return;
        var balk = document.querySelector('.topbar');
        var marge = (balk && getComputedStyle(balk).position !== 'static' ? balk.offsetHeight : 0) + 16;
        window.scrollTo({ top: slot.getBoundingClientRect().top + window.scrollY - marge, behavior: 'smooth' });
      }, 700);
    }
    var open = teacherMode || load(sleutel, false) || !vragen.length;
    toon(open);
    if (open) return;
    vragen.forEach(function (q) {
      all('button', q).forEach(function (btn) {
        btn.addEventListener('click', function () {
          if (!box.hidden) return;
          if (juist() === vragen.length) maakOpen(); else toon(false);
        });
      });
    });
  });

  /* ---------- 7. Screenshot-plaatsen ---------- */
  all('figure.shot').forEach(function (fig) {
    var file = fig.getAttribute('data-shot');
    var caption = fig.getAttribute('data-caption') || '';
    if (!file) return;
    var img = new Image();
    img.alt = fig.getAttribute('data-alt') || caption;
    img.onload = function () {
      fig.innerHTML = '';
      fig.appendChild(img);
      if (caption) { var c = document.createElement('figcaption'); c.textContent = caption; fig.appendChild(c); }
      fig.classList.add('loaded');
    };
    img.onerror = function () {
      if (teacherMode) fig.innerHTML = '📷 <strong>Screenshot-plaats</strong>: bewaar als <code>assets/screenshots/' + file + '</code><br>' + (fig.getAttribute('data-alt') || '');
    };
    img.src = 'assets/screenshots/' + file;
  });

  /* ---------- 8. Kijk na: toont het geanonimiseerde voorbeeldverslag ---------- */
  all('.kijkna').forEach(function (k) {
    var knop = k.querySelector('button');
    var inhoud = k.querySelector('.kijkna-inhoud');
    if (!knop || !inhoud) return;
    knop.addEventListener('click', function () {
      var open = inhoud.hidden;
      inhoud.hidden = !open;
      knop.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  /* ---------- Start ---------- */
  updateProgress(false);
  var start = window.location.hash ? window.location.hash.slice(1) : load('stap', 'start');
  showStep(start, false);
})();
