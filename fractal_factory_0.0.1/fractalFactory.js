// this is where the back end fractal calculations and image creation happen

function drawFractal(x, y, len, angle, colors, shape, depth = 0) {
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

  // Draw the shape
  switch(shape) {

    case 'shape-line':
      // Draw each pixel along the line
      if (depth > 0){
      for(let i = 0; i < len; i++) {
        // Calculate the position of the pixel
        let px = x + i * Math.cos(angle);
        let py = y + i * Math.sin(angle);

        // Interpolate between the current color and the next color
        let color1 = colors[index % colors.length];
        let color2 = colors[(index + 1) % colors.length];
        let color = interpolateColor(color1, color2, i / len);

        // Set the fill color
        ctx.fillStyle = 'rgb(' + color.join(',') + ')';

        // Draw the pixel
        ctx.fillRect(px, py, 1, 1);
      }
       // Recursive calls for the two new branches
    drawFractal(x1, y1, len * 0.75, angle + Math.PI / 6, colors, shape, depth + 1);
    drawFractal(x1, y1, len * 0.75, angle - Math.PI / 6, colors, shape, depth + 1);
      };
      break;
    case 'shape-triangle':

      if(depth > 0) {
        // Draw smaller triangles at each corner
        drawFractal(x, y, len / 2, angle, colors, shape, depth - 1);
        drawFractal(x + len / 2 * Math.cos(angle), y + len / 2 * Math.sin(angle), len / 2, angle, colors, shape, depth - 1);
        drawFractal(x + len / 2 * Math.cos(angle - Math.PI / 3), y + len / 2 * Math.sin(angle - Math.PI / 3), len / 2, angle, colors, shape, depth - 1);
      } else {
        // Base case: draw a single triangle
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + len * Math.cos(angle), y + len * Math.sin(angle));
        ctx.lineTo(x + len * Math.cos(angle - Math.PI / 3), y + len * Math.sin(angle - Math.PI / 3));
        ctx.closePath();
        ctx.stroke();
      }
      break;
    case 'shape-square':

      if(depth > 0) {
        // Draw smaller squares at each corner
        drawFractal(x, y, len / 2, angle, colors, shape, depth - 1);
        drawFractal(x + len / 2 * Math.cos(angle), y + len / 2 * Math.sin(angle), len / 2, angle, colors, shape, depth - 1);
        drawFractal(x + len / 2 * Math.cos(angle + Math.PI / 2), y + len / 2 * Math.sin(angle + Math.PI / 2), len / 2, angle, colors, shape, depth - 1);
        drawFractal(x + len / 2 * Math.cos(angle - Math.PI / 2), y + len / 2 * Math.sin(angle - Math.PI / 2), len / 2, angle, colors, shape, depth - 1);
      } else {
        // Base case: draw a single square pixel by pixel
        for(let i = 0; i < len; i++) {
          for(let j = 0; j < len; j++) {
            // Interpolate between the current color and the next color
            let color1 = colors[index % colors.length];
            let color2 = colors[(index + 1) % colors.length];
            let color = interpolateColor(color1, color2, (i * len + j) / (len * len));
    
            // Set the fill color
            ctx.fillStyle = 'rgb(' + color.join(',') + ')';
    
            // Draw the pixel
            ctx.fillRect(x + i, y + j, 1, 1);
          }
        }
      }
      break;
    case 'shape-circle':

      if(depth >= 0) {
        // Draw smaller circles around the current circle
        drawFractal(x + len / 2 * Math.cos(angle), y + len / 2 * Math.sin(angle), len / 2, angle, colors, shape, depth - 1);
        drawFractal(x + len / 2 * Math.cos(angle + Math.PI / 2), y + len / 2 * Math.sin(angle + Math.PI / 2), len / 2, angle, colors, shape, depth - 1);
        drawFractal(x + len / 2 * Math.cos(angle + Math.PI), y + len / 2 * Math.sin(angle + Math.PI), len / 2, angle, colors, shape, depth - 1);
        drawFractal(x + len / 2 * Math.cos(angle - Math.PI / 2), y + len / 2 * Math.sin(angle - Math.PI / 2), len / 2, angle, colors, shape, depth - 1);
      } else {
        // Base case: draw a single circle
        ctx.beginPath();
        ctx.arc(x, y, len / 2, 0, 2 * Math.PI);
        ctx.stroke();
      }
      break;
  }
  };

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
