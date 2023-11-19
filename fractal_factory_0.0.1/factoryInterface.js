// Get inputs
let colorInputs = document.querySelectorAll('.color');
let originSelector = document.getElementById('origin-selector');
let selectedorigin = originSelector.value;
let shapeSelector = document.getElementById('shape-selector');
let shape = shapeSelector.value;

// Get 'Create' button
let createButton = document.querySelector('#create-button');

// Add event listener to 'Create' button
createButton.addEventListener('click', function() {
  //clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // Get selected origin and colors when the button is clicked
  let selectedOrigin = originSelector.value;
  let colors = Array.from(colorInputs).map(input => hexToRgb(input.value));
  let shape = shapeSelector.value;
// Set the initial origin based on the selected origin
  let x, y;
  switch(selectedOrigin) {
    case 'top-left':
      x = y = len * .025; //len*.025 gives us a margin of 2.5% the canvas size
      break;
    case 'top-center':
      x = canvas.width / 2;
      y = len * .025; 
      break;
    case 'top-right':
      x = canvas.width - len * .025; 
      y = len * .025; 
      break;
    case 'center-left':
      x = len * .025; 
      y = canvas.height / 2;
      break;
    case 'center':
      x = canvas.width / 2;
      y = canvas.height / 2;
      break;
    case 'center-right':
      x = canvas.width - len * .025; 
      y = canvas.height / 2;
      break;
    case 'bottom-left':
      x = len * .025; 
      y = canvas.height - len * .025; 
      break;
    case 'bottom-center':
      x = canvas.width / 2;
      y = canvas.height - len * .025; 
      break;
    case 'bottom-right':
      x = canvas.width - len * .025; 
      y = canvas.height - len * .025; 
      break;
  }
  // Call your function to draw the fractal
  drawFractal(x, y, len, angle, colors, shape, 0);
});

// Get the canvas and context
let canvas = document.getElementById('fractal-window');
let ctx = canvas.getContext('2d');

// Set the initial position, length and angle
let x = canvas.width / 2;
let y = canvas.height;
let len = 100;
let angle = -Math.PI / 2;

// Clear the canvas and set the stroke color
ctx.clearRect(0, 0, canvas.width, canvas.height);
ctx.strokeStyle = '#ffffff';

window.onload = function() {
  // Get selected position and colors
  let selectedOrigin = originSelector.value;
  let colors = Array.from(colorInputs).map(input => hexToRgb(input.value));
  let shape = shapeSelector.value;
  // Set the initial position based on the selected position
  // Your existing code...

  // Call your function to draw the fractal
  drawFractal(x, y, len, angle, colors, shape, 0);
};


