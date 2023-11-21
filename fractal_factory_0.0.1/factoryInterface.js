// define colors
const colors = {
  'red': [255, 0, 0],
  'orange': [255, 127, 0],
  'yellow': [255, 255, 0],
  'green': [0, 255, 0],
  'blue': [0, 0, 255],
  'violet': [238, 130, 238],
  'UV': [255, 255, 255]
};

// Define your color gradients
const colorGradients = {
  'human-button': [colors['red'], colors['orange'], colors['yellow'], colors['green'], colors['blue'], colors['violet']], // Human R,G,B
  'cat-button': [colors['yellow'], colors['blue']], // Cat B,Y
  'humming-button': [colors['red'], colors['orange'], colors['yellow'], colors['green'], colors['blue'], colors['violet'], colors['UV']], // Humming Bird R,G,B,UV
  'golden-button': [[0, 0, 0]], // Golden Mole ...
  'starfish-button': [[255, 255, 255]], // Starfish SL
  'bee-button': [colors['yellow'], colors['blue'], colors['UV']], // Bee B,Y,UV
  'rabbit-button': [colors['green'], colors['blue']], // Rabbit B,G
  'rat-button': [colors['green'], colors['blue'], colors['UV']] // Rat B,G,UV
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



// Get the element where you want to display the color gradient
let gradientElement = document.getElementById('gradient');
let canvas = document.getElementById('fractal-window');
let ctx = canvas.getContext('2d');
let len = 200
let shape = 'shape-line';
let angle = Math.PI/2
const x = canvas.width / 2;
const y = canvas.height - len * .025; 

// Add event listeners to the buttons
Object.keys(audioFiles).forEach(function(buttonId) {
    document.getElementById(buttonId).addEventListener('click', function() {
        // Stop all audio
        Object.values(audioFiles).forEach(function(audio) {
            audio.pause();
            audio.currentTime = 0;
        });

        // Play the audio for this button
        audioFiles[buttonId].play();

        // Display the color gradient for this button
        gradientElement.style.background = colorGradients[buttonId];

        // Call your function to draw the fractal with the new gradient
        drawFractal(x, y, len, angle, colorGradients[buttonId], shape, 0);
    });
});

window.onload = function() {
  // Get selected position and colors
  let colors = Array.from(colorGradients["human-button"]);

  // Call your function to draw the fractal
  drawFractal(x, y, len, angle, colors, shape, 0);
};


