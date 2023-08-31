// in your js file
document.getElementById("navbar-html").textContent = `
<nav class="navbar"></nav>
`;
document.getElementById("navbar-css").textContent = `
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  padding: 16px;
  display: flex;
  background-color: var(--primary-green);
  color: var(--dark-text);
  box-shadow: 1px 3px 5px rgba(0,0,0,.12), 1px 3px 5px rgba(0,0,0,.24);
}
`;
document.getElementById("navbar-js").textContent =`
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  padding: 8px;
  display: flex;
  background-color: var(--primary-green);
  color: var(--dark-text);
  box-shadow: 1px 3px 5px rgba(0,0,0,.12), 1px 3px 5px rgba(0,0,0,.24);
}
\`;
document.getElementById("navbar-js").textContent = \`
const navbar = document.querySelector('.navbar');
  navbar.innerHTML =\`
    <button class="nav-button">
      <span class="material-symbols-outlined">menu</span>
    </button>\`;

  // Navigation Drawer
  const drawer = document.querySelector('.drawer');
  drawer.innerHTML =\`
  <a><span class="material-symbols-outlined">home</span>Home</a>
  <a><span class="material-symbols-outlined">school</span>Courses</a>
  <a><span class="material-symbols-outlined">person</span>Account</a>
  <a><span class="material-symbols-outlined">settings</span>Settings</a>\`;
  const navButton = document.querySelector(".nav-button");
  
  let isNavOpen = false;
  navButton.addEventListener("click", () => {
    isNavOpen = !isNavOpen;
    drawer.dataset.open = \`\${isNavOpen}\`;
  });
  navButton.addEventListener('mouseup', (event) => {
    event.target.style.backgroundColor = 'rgb(213,235,126)';
    event.target.style.boxShadow = \`5px 3px 1px rgba(10, 30, 0, .5), 3px 2px 1px rgba(10, 30, 0, 0.5)\`
    event.target.style.color = 'rgb(10,30,0)'
  });
  navButton.addEventListener('mousedown', (event) => {
    event.target.style.backgroundColor = 'rgb(136,179,29)';
    event.target.style.boxShadow = 'none';
    event.target.style.color = 'rgb(252,241,237)';
  });
`

document.getElementById("drawer-html").textContent = `
<div class="drawer"></div>
`;
document.getElementById("drawer-css").textContent = `

.nav-button {
  background-color: var(--secondary-green);
  border: none;
  outline: none;
  color: var(--dark-text);
  text-align: center;
  text-decoration: none;
  display: inline-block;
  padding: 4px 12px;
  border-top-left-radius: 20px;
  border-top-right-radius: 64px;
  border-bottom-left-radius: 20px;
  box-shadow: 4px 3px 1px rgba(10, 30, 0, .5), 3px 2px 1px rgba(10, 30, 0, 0.5);
  transition: all .15s ease;
}

.drawer {
  position: fixed;
  top: 61.76px;
  left: -320px;
  bottom: 0;
  width: 300px;
  background-color: transparent;
  box-shadow: transparent;
  transition: all .5s ease;
}

.drawer[data-open="true"] {
  left: 0px;
  background-color: var(--dark-green);
  box-shadow: 1px 3px 5px rgba(0,0,0,.3), 1px 3px 5px rgba(0,0,0,.5);
}

.drawer > a {
  display: flex;
  padding: 8px 16px;
  align-items: center;
  gap: 8px;
  color: var(--secondary-green);
}
`;
document.getElementById("drawer-js").textContent = `
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  padding: 8px;
  display: flex;
  background-color: var(--primary-green);
  color: var(--dark-text);
  box-shadow: 1px 3px 5px rgba(0,0,0,.12), 1px 3px 5px rgba(0,0,0,.24);
}
\`;
document.getElementById("navbar-js").textContent = \`
const navbar = document.querySelector('.navbar');
  navbar.innerHTML =\`
    <button class="nav-button">
      <span class="material-symbols-outlined">menu</span>
    </button>\`;

  // Navigation Drawer
  const drawer = document.querySelector('.drawer');
  drawer.innerHTML =\`
  <a><span class="material-symbols-outlined">home</span>Home</a>
  <a><span class="material-symbols-outlined">school</span>Courses</a>
  <a><span class="material-symbols-outlined">person</span>Account</a>
  <a><span class="material-symbols-outlined">settings</span>Settings</a>\`;
  const navButton = document.querySelector(".nav-button");
  
  let isNavOpen = false;
  navButton.addEventListener("click", () => {
    isNavOpen = !isNavOpen;
    drawer.dataset.open = \`\${isNavOpen}\`;
  });
  navButton.addEventListener('mouseup', (event) => {
    event.target.style.backgroundColor = 'rgb(213,235,126)';
    event.target.style.boxShadow = \`5px 3px 1px rgba(10, 30, 0, .5), 3px 2px 1px rgba(10, 30, 0, 0.5)\`
    event.target.style.color = 'rgb(10,30,0)'
  });
  navButton.addEventListener('mousedown', (event) => {
    event.target.style.backgroundColor = 'rgb(136,179,29)';
    event.target.style.boxShadow = 'none';
    event.target.style.color = 'rgb(252,241,237)';
  });
`;

document.getElementById("button-html").textContent = `
<div class="button">Click me!</div>
`;
document.getElementById("button-css").textContent = `
.button {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--secondary-green);
  border: none;
  color: var(--dark-text);
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-top-left-radius: 20px;
  border-top-right-radius: 64px;
  border-bottom-left-radius: 20px;
  box-shadow: 4px 3px 1px rgba(10, 30, 0, .5), 3px 2px 1px rgba(10, 30, 0, 0.5);
  transition: all .15s ease;
}
`;
document.getElementById("button-js").textContent = `
const button = document.querySelector('.button');
  button.addEventListener('mouseup', (event) => {
    event.target.style.backgroundColor = 'rgb(213,235,126)';
    event.target.style.boxShadow = \`5px 3px 1px rgba(10, 30, 0, .5), 3px 2px 1px rgba(10, 30, 0, 0.5)\`
    event.target.style.color = 'rgb(10,30,0)'
  });
  button.addEventListener('mousedown', (event) => {
    event.target.style.backgroundColor = 'rgb(136,179,29)';
    event.target.style.boxShadow = 'none';
    event.target.style.color = 'rgb(252,241,237)';
  });
`;

document.getElementById("fab-html").textContent = `
div class="fab"></div>
`;
document.getElementById("fab-css").textContent = `
.fab-button {
  position: fixed;
  align-items: center;
  background-color: var(--secondary-green);
  outline: none;
  border: none;
  right: 60px;
  bottom: 60px;
  color: var(--dark-text);
  padding: 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 64px;
  box-shadow: 4px 3px 1px rgba(10, 30, 0, .5), 3px 2px 1px rgba(10, 30, 0, 0.5);
  transition: all .15s ease;
}
`;
document.getElementById("fab-js").textContent = `
const fab = document.querySelector('.fab');
  fab.innerHTML = \`
  <button class="fab-button">
    <span class="material-symbols-outlined">add</span>
  </button>\`;
  const fabButton = document.querySelector(".fab-button");
  fabButton.addEventListener('mouseup', (event) => {
    event.target.style.backgroundColor = 'rgb(213,235,126)';
    event.target.style.boxShadow = \`5px 3px 1px rgba(10, 30, 0, .5), 3px 2px 1px rgba(10, 30, 0, 0.5)\`;
    event.target.style.color = 'rgb(10,30,0)';
  });
  fabButton.addEventListener('mousedown', (event) => {
    event.target.style.backgroundColor = 'rgb(136,179,29)';
    event.target.style.boxShadow = 'none';
    event.target.style.color = 'rgb(252,241,237)';
  });
`;

document.getElementById("image-carousel-html").textContent = `
        <div class="image-carousel">
          <img class="active" src="https://www.thewowstyle.com/wp-content/uploads/2015/01/nature-images..jpg">
          <img src="https://www.thewowstyle.com/wp-content/uploads/2015/01/nature-wallpaper-27.jpg">
          <img src="https://jooinn.com/images/nature-319.jpg">
        </div>
`;
document.getElementById("image-carousel-css").textContent = `
.image-carousel {
  position: relative;
  overflow: hidden;
}

.image-carousel img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  left: 100%;
  transition: left 1s ease;
}

.image-carousel img.active {
  left: 0;
}
`;
document.getElementById("image-carousel-js").textContent = `
const imageCarousel = document.querySelector('.image-carousel');
  let images = imageCarousel.querySelectorAll('img');
  let currentImage = 0;

  function nextImage() {
      images[currentImage].classList.remove('active');
      currentImage = (currentImage + 1) % images.length;
      images[currentImage].classList.add('active');
  }

setInterval(nextImage, 3000);
`;

document.getElementById("loading-spinners-html").textContent = `
<div class="loading-spinners-1"></div>
<div class="loading-spinners-2"></div>
<div class="loading-spinners-3"></div>

`;
document.getElementById("loading-spinners-css").textContent = `
.loading-spinners-1 {
  animation: spin 2s linear infinite;
  width: 32px;
  height: 32px;
  margin: 8px;
  background-color: var(--primary-green);
}

.loading-spinners-2 {
  width: 32px;
  height: 32px;
  animation: bounce 1s ease-in-out infinite;
  margin: 16px;
  background-color: var(--secondary-green);
}

.loading-spinners-3 {
  background-color: var(--dark-green);
  margin: 16px;
  width: 32px;
  height: 32px;
  animation: spin 2s linear infinite;
  transition: all .3s ease;
}

.loading-spinners-3:hover {
  background-color: red;
  width: 32px;
  height: 32px;
  margin: 16px;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
`;
document.getElementById("loading-spinners-js").textContent = `
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

`;
