// this is where the front end style of the web page will go that needs to interact with the .css file


// Get a reference to the canvas element
const canvas = document.getElementById("myCanvas");

// Get the 2D drawing context
const ctx = canvas.getContext("2d");

// Create a new image object
const img = new Image();

// Set the source of the image
img.src = 'https://wallpaperaccess.com/full/1260789.jpg'; // Replace with your image path

// Draw the image onto the canvas once it's loaded
img.onload = function() {
    ctx.drawImage(img, 10, 10);
}
