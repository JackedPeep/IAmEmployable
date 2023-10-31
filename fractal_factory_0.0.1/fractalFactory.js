// this is where the back end fractal calculations and image creation happen

function drawFractal(x, y, len, angle, colors, depth = 0) {
  // Base case: if the branch length is too short, return
  if(len < 2) {
    return;
  }

  // Calculate the endpoint of the branch
  let x1 = x + len * Math.cos(angle);
  let y1 = y + len * Math.sin(angle);

  // Calculate the color index and interpolation factor
  let index = Math.floor(depth / len);
  let factor = (depth % len) / len;

  // Interpolate between the current color and the next color
  let color1 = colors[index % colors.length];
  let color2 = colors[(index + 1) % colors.length];
  let color = interpolateColor(color1, color2, factor);

  // Set the stroke color
  ctx.strokeStyle = 'rgb(' + color.join(',') + ')';

  // Draw the branch
  ctx.beginPath();
  ctx.moveTo(x, y);
  ctx.lineTo(x1, y1);
  ctx.stroke();

  // Recursive calls for the two new branches
  drawFractal(x1, y1, len * 0.75, angle + Math.PI / 6, colors, depth + len);
  drawFractal(x1, y1, len * 0.75, angle - Math.PI / 6, colors, depth + len);
}

// Changes a hex color to rgb
function hexToRgb(hex) {
  let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? [
    parseInt(result[1], 16),
    parseInt(result[2], 16),
    parseInt(result[3], 16)
  ] : null;
}

//interpolates from color1 to color2 

function interpolateColor(color1, color2, factor) {
  let result = [];
  for(let i = 0; i < 3; i++) {
    result[i] = Math.round(color1[i] + factor * (color2[i] - color1[i]));
  }
  return result;
}
