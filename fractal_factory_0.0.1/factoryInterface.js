// define colors
const colors = {
  'red': [255, 0, 0],
  'orange': [255, 128, 0],
  'yellow': [255, 255, 0],
  'green': [0, 255, 0],
  'blue': [0, 0, 255],
  'indigo': [75, 0, 130],
  'violet': [238, 130, 238],
  'UV': [255, 255, 255],
  'UV-red': [255, 128, 128],
  'UV-orange': [255, 191, 128],
  'UV-yellow': [255, 255, 128],
  'UV-green': [128, 255, 128],
  'UV-indigo': [165, 128, 192],
  'UV-violet': [246, 192, 246]
};

// Define your color gradients
const colorGradients = {
  'human-button': [colors['red'], colors['orange'], colors['yellow'], colors['green'], colors['blue'], colors['indigo'], colors['violet']], // Human R,G,B
  'cat-button': [colors['yellow'], colors['blue']], // Cat B,Y
  'humming-button': [colors['red'], colors['UV'], colors['orange'], colors['UV'], colors['yellow'], colors['UV'], colors['green'],  colors['UV'], colors['blue'], colors['UV'], colors['indigo'], colors['UV'], colors['violet'], colors['UV']], // Humming Bird R,G,B,UV
  'golden-button': [[0, 0, 0],[0,0,0]], // Golden Mole ...
  'starfish-button': [[255, 255, 255],[255,255,255]], // Starfish SL
  'bee-button': [colors['yellow'], colors['UV'], colors['blue'], colors['UV'], colors['UV']], // Bee B,Y,UV
  'rabbit-button': [colors['green'], colors['blue']], // Rabbit B,G
  'rat-button': [colors['green'], colors['UV'], colors['blue'], colors['UV'], colors['UV']] // Rat B,G,UV
};

// Define your audio files
const audioFiles = {
  'human-button': new Audio('audio/scribble.mp3'),
  'humming-button': new Audio('audio/br_hummers1.mp3'),
  'cat-button': new Audio('audio/cat-meow.mp3'),
  'golden-button': new Audio('audio/sandfall.mp3'),
  'starfish-button': new Audio('audio/underwater-waves.mp3'),
  'bee-button': new Audio('audio/bumblebee.mp3'),
  'rabbit-button': new Audio('audio/boing-spring-mouth-harp.mp3'),
  'rat-button': new Audio('audio/double-squeak.mp3')
};

Object.keys(audioFiles).forEach(function(buttonId) {
  if (!colorGradients.hasOwnProperty(buttonId)) {
      console.log('Missing color gradient for: ' + buttonId);
  }
});

// Get the element where you want to display the color gradient
let gradientElement = document.getElementById('gradient-slider');
let canvas = document.getElementById('fractal-window');
let ctx = canvas.getContext('2d');
let len = 200
let shape = 'shape-line';
let angle = Math.PI/2
let x = canvas.width / 2;
let y = canvas.height - len * .025; 
let overlay = document.getElementById('fade-overlay');
let currentButton = null;

// Add event listeners to the buttons
Object.keys(audioFiles).forEach(function(buttonId) {
  document.getElementById(buttonId).addEventListener('click', function() {
    // If the same button is clicked, hide the slider and return
    if (currentButton === buttonId) {
      gradientElement.style.transform = 'translateX(-100%)';
      currentButton = null;
      return;
    }

    // Stop all audio
    Object.values(audioFiles).forEach(function(audio) {
      audio.pause();
      audio.currentTime = 0;
    });

    // Play the audio for this button
    audioFiles[buttonId].play();

    // Hide the gradient slider/fractal
    gradientElement.style.transform = 'translateX(-100%)';
    overlay.style.opacity = 0;

    // Use setTimeout to wait for the transition to finish
    setTimeout(function() {
      // Update the current button
      currentButton = buttonId;

      // Display the color gradient for this button
      gradientElement.style.background = 'linear-gradient(to right, ' + colorGradients[currentButton].map(rgb => 'rgb(' + rgb.join(',') + ')').join(',') + ')';

      // Show the gradient slider/fractal
      gradientElement.style.transform = 'translateX(0)';
      overlay.style.opacity = 1;

      // Call your function to draw the fractal with the new gradient
      drawFractal(x, y, len, angle, colorGradients[currentButton], shape, 0);
    }, 500); // Adjust this value to match the transition duration
  });
});

window.onload = function() {
  let gradientElement = document.getElementById('gradient-slider');
  let buttonId = 'human-button';
  let canvas = document.getElementById('fractal-window');
  let len = 200
  let shape = 'shape-line';
  let angle = Math.PI/2
  const x = canvas.width / 2;
  const y = canvas.height - len * .025; 
  // Call your function to draw the fractal
  drawFractal(x, y, len, angle, colorGradients[buttonId], shape, 0);
  
  // Set the current button to 'human-button'
  currentButton = 'human-button';

  // Display the color gradient for the 'human-button'
  gradientElement.style.background = 'linear-gradient(to right, ' + colorGradients[currentButton].map(rgb => 'rgb(' + rgb.join(',') + ')').join(',') + ')';

  // Show the gradient slider
  gradientElement.style.transform = 'translateY(0)';

  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Call your function to draw the fractal with the new gradient
  drawFractal(x, y, len, angle, colorGradients[currentButton], shape, 0);


};


