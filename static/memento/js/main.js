// change to dark mode or light mode
// const aTags = document.querySelector('a');
const navTags = document.querySelector('nav');
const body = document.querySelector('body');
const toggle = document.getElementById('toggle');
const card = document.getElementsByClassName('desc');

toggle.onclick = function() {
    toggle.classList.toggle('active');
    body.classList.toggle('active');
    navTags.classList.toggle('active');
    card.classList.toggle('active');
}
// menu settings
function menuToggle() {
    const nav = document.getElementById('menu-overlay');
    nav.classList.toggle('active');
}