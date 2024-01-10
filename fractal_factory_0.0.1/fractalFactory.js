// this is where the back end fractal calculations and image creation happen

function drawFractal(x, y, len, angle, colors, shape, depth = 0) {
  
  if (depth === 0) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }
    // Base case: if the branch length is too short, return
  if(len < 1) {
    return;
  }

  // Calculate the endpoint of the branch
  let x1 = x - len * Math.cos(angle);
  let y1 = y - len * Math.sin(angle);

  // Calculate the color index and interpolation factor
  let index = Math.floor(depth) % colors.length;
  let color1 = colors[index];
  let color2 = colors[(index + 1) % colors.length];

  // Create a linear gradient from color1 to color2
  let gradient = ctx.createLinearGradient(x, y, x1, y1);
  gradient.addColorStop(0, 'rgb(' + color1.join(',') + ')');
  gradient.addColorStop(1, 'rgb(' + color2.join(',') + ')');

  // Set the stroke style to the gradient
  ctx.strokeStyle = gradient;

  // Draw the branch
  ctx.beginPath();
  ctx.moveTo(x, y);
  ctx.lineTo(x1, y1);
  ctx.stroke();

  // Calculate the new angle for the branches


  // Recursive calls for the two new branches
  drawFractal(x1, y1, len * 0.67, angle + Math.PI / 6, colors, shape, depth + 1);
  drawFractal(x1, y1, len * 0.67, angle - Math.PI / 6, colors, shape, depth + 1);
}





//interpolates from color1 to color2 

// function interpolateColor(color1, color2, factor) {
//   let result = [];
//   for(let i = 0; i < 3; i++) {
//     result[i] = Math.round(color1[i] + factor * (color2[i] - color1[i]));
//   }
//   return result;
// }

// // Changes a hex color to rgb
// function hexToRgb(hex) {
//   let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
//   return result ? [
//     parseInt(result[1], 16),
//     parseInt(result[2], 16),
//     parseInt(result[3], 16)
//   ] : null;
// }