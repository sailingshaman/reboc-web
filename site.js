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
