// menu settings (mobile nav)
function menuToggle() {
    const nav = document.getElementById('menu-overlay');
    nav.classList.toggle('active');
    const nav = document.getElementById('toggleIcon');
    nav.classList.toggle('active');
}

// change to dark mode or light mode
const toggle = document.getElementById('toggle');

toggle.onclick = function() {
    toggle.classList.toggle('active');
}

// dark mode settings
const body = document.querySelector('body');
const navTags = document.querySelector('nav');
const card = document.getElementsByClassName('desc');

toggle.onclick = function() {
    body.classList.toggle('active');
    navTags.classList.toggle('active');
    card.classList.toggle('active');
}