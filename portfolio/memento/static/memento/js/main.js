// menu settings (mobile nav)
function menuToggle() {
    const nav = document.getElementById('menu-overlay');
    nav.classList.toggle('active');
}
// closes the menu after clicking link
const menu = document.getElementById('menu-overlay');

function closeMenu() {
    menu.classList.remove('active');
}
// --------------------------------

//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// --------------------------------

// change to dark mode or light mode
const toggle = document.getElementById('toggle');

toggle.onclick = function() {
    toggle.classList.toggle('active');
}

// dark mode settings ++
const body = document.querySelector('body');
const navTags = document.querySelector('nav');
const card = document.getElementsByClassName('desc');

toggle.onclick = function() {
    body.classList.toggle('active');
    navTags.classList.toggle('active');
    card.classList.toggle('active');
}