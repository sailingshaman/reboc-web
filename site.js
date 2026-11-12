/* Day and night display switch.
   The site is the light "Admiralty" scheme for everyone. The switch in the masthead
   turns on "Night watch". The choice is remembered in this browser only, so it holds
   from page to page; nothing is sent anywhere. */
(function () {
    var root = document.documentElement, KEY = 'reboc-display';

    function apply(night) {
        if (night) { root.setAttribute('data-theme', 'night'); } else { root.removeAttribute('data-theme'); }
        var meta = document.querySelector('meta[name="theme-color"]');
        if (meta) { meta.setAttribute('content', night ? '#090505' : '#d9ebf4'); }
        var button = document.querySelector('.watch');
        if (button) { button.setAttribute('aria-checked', night ? 'true' : 'false'); }
    }

    var saved = null;
    try { saved = localStorage.getItem(KEY); } catch (e) {}
    apply(saved === 'night');

    document.addEventListener('DOMContentLoaded', function () {
        var button = document.querySelector('.watch');
        if (!button) { return; }
        button.hidden = false;
        apply(root.getAttribute('data-theme') === 'night');
        button.addEventListener('click', function () {
            var night = root.getAttribute('data-theme') !== 'night';
            apply(night);
            try { localStorage.setItem(KEY, night ? 'night' : 'day'); } catch (e) {}
        });
    });
})();

/* Contact form.
   The message is sent in the background, so the visitor stays on the page, sees a
   confirmation and gets an empty form back. If that is refused (Formspree does so
   while its robot check is switched on for the form) or fails, the form is handed
   over the ordinary way and Formspree shows its own page. Coming back from that
   page, the form is emptied. */
(function () {
    document.addEventListener('DOMContentLoaded', function () {
        var form = document.querySelector('form.form');
        if (!form) { return; }
        var button = form.querySelector('.send'), status = form.querySelector('.form-status');

        window.addEventListener('pageshow', function (event) {
            var nav = window.performance && performance.getEntriesByType ? performance.getEntriesByType('navigation')[0] : null;
            if (event.persisted || (nav && nav.type === 'back_forward')) {
                form.reset();
                button.disabled = false;
                status.textContent = '';
            }
        });

        if (!window.fetch || !window.FormData) { return; }
        form.addEventListener('submit', function (event) {
            event.preventDefault();
            if (button.disabled) { return; }
            button.disabled = true;
            status.textContent = 'Sending\u2026';
            fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
                .then(function (response) {
                    if (!response.ok) { throw new Error('refused'); }
                    form.reset();
                    button.disabled = false;
                    status.textContent = 'Thank you. Your message has been sent.';
                })
                .catch(function () {
                    status.textContent = '';
                    form.submit();
                });
        });
    });
})();
