
document.addEventListener("DOMContentLoaded", () => {

  // My Navbar
  const navbar = document.querySelector('.navbar');
  navbar.innerHTML =`
    <button class="nav-button">
      <span class="material-symbols-outlined">menu</span>
    </button>`;

  // Navigation Drawer
  const drawer = document.querySelector('.drawer');
  drawer.innerHTML =`
  <a><span class="material-symbols-outlined">home</span>Home</a>
  <a><span class="material-symbols-outlined">school</span>Courses</a>
  <a><span class="material-symbols-outlined">person</span>Account</a>
  <a><span class="material-symbols-outlined">settings</span>Settings</a>`;
  const navButton = document.querySelector(".nav-button");
  
  let isNavOpen = false;
  navButton.addEventListener("click", () => {
    isNavOpen = !isNavOpen;
    drawer.dataset.open = `${isNavOpen}`;
  });
  navButton.addEventListener('mouseup', (event) => {
    event.target.style.backgroundColor = 'rgb(213,235,126)';
    event.target.style.boxShadow = `5px 3px 1px rgba(10, 30, 0, .5), 3px 2px 1px rgba(10, 30, 0, 0.5)`
    event.target.style.color = 'rgb(10,30,0)'
  });
  navButton.addEventListener('mousedown', (event) => {
    event.target.style.backgroundColor = 'rgb(136,179,29)';
    event.target.style.boxShadow = 'none';
    event.target.style.color = 'rgb(252,241,237)';
  });

  // Button
  const button = document.querySelector('.button');
  button.addEventListener('mouseup', (event) => {
    event.target.style.backgroundColor = 'rgb(213,235,126)';
    event.target.style.boxShadow = `5px 3px 1px rgba(10, 30, 0, .5), 3px 2px 1px rgba(10, 30, 0, 0.5)`
    event.target.style.color = 'rgb(10,30,0)'
  });
  button.addEventListener('mousedown', (event) => {
    event.target.style.backgroundColor = 'rgb(136,179,29)';
    event.target.style.boxShadow = 'none';
    event.target.style.color = 'rgb(252,241,237)';
  });

  // Floating Action Button
  const fab = document.querySelector('.fab');
  fab.innerHTML = `
  <button class="fab-button">
    <span class="material-symbols-outlined">add</span>
  </button>`;
  const fabButton = document.querySelector(".fab-button");
  fabButton.addEventListener('mouseup', (event) => {
    event.target.style.backgroundColor = 'rgb(213,235,126)';
    event.target.style.boxShadow = `5px 3px 1px rgba(10, 30, 0, .5), 3px 2px 1px rgba(10, 30, 0, 0.5)`;
    event.target.style.color = 'rgb(10,30,0)';
  });
  fabButton.addEventListener('mousedown', (event) => {
    event.target.style.backgroundColor = 'rgb(136,179,29)';
    event.target.style.boxShadow = 'none';
    event.target.style.color = 'rgb(252,241,237)';
  });

  // Image Carousel
  const imageCarousel = document.querySelector('.image-carousel');
  let images = imageCarousel.querySelectorAll('img');
  let currentImage = 0;

  function nextImage() {
      images[currentImage].classList.remove('active');
      currentImage = (currentImage + 1) % images.length;
      images[currentImage].classList.add('active');
  }

setInterval(nextImage, 3000);

  // Loading Spinners
  const loadingSpinners3 = document.querySelector('.loading-spinners-3');
  let isSpinning = true;
loadingSpinners3.addEventListener('click', () => {
  isSpinning = !isSpinning;
  if (isSpinning) {
    loadingSpinners3.style.animation = 'spin 2s linear infinite';
  } else {

    loadingSpinners3.style.animation = 'spin 4s linear infinite';
  }
});

});
