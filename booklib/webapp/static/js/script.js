window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");

var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

const openPopupBtn = document.getElementById('openPopupBtn');
const closePopupBtn = document.getElementById('closePopupBtn');
const popupContainer = document.getElementById('popupContainer');

openPopupBtn.addEventListener('click', () => {
    popupContainer.style.display = 'flex';
});

closePopupBtn.addEventListener('click', () => {
    popupContainer.style.display = 'none';
});

