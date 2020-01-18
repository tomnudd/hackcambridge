// Change seaRiseAmt to a number between 0 and 100 to set base sea level!

var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

seaRiseAmt = 59

var date = Date.now();
function draw(delta) {
  requestAnimationFrame(draw);

  rise = (seaRiseAmt/100) * canvas.height

  canvas.width = canvas.width;

  // colour!
  ctx.fillStyle = "rgba(100, 150, 210, 0.63)";

  var randomLeft = Math.abs(Math.pow( Math.sin(delta/1000), 2 )) * 100;
  var randomRight = Math.abs(Math.pow( Math.sin((delta/1000) + 10), 2 )) * 100;
  var randomLeftConstraint = Math.abs(Math.pow( Math.sin((delta/1000)+2), 2 )) * 100;
  var randomRightConstraint = Math.abs(Math.pow( Math.sin((delta/1000)+1), 2)) * 100;

  ctx.beginPath();
  ctx.moveTo(0, randomLeft+canvas.height-rise);

  ctx.bezierCurveTo(canvas.width / 3, randomLeftConstraint-rise+canvas.height, canvas.width / 3 * 2, randomRightConstraint-rise+canvas.height, canvas.width, randomRight-rise+canvas.height);
  ctx.lineTo(canvas.width, canvas.height); // top left to bot right
  ctx.lineTo(0, canvas.height); // bot right to bot left
  ctx.lineTo(0, randomLeft-rise); // bot left to top right

  ctx.closePath();
  ctx.fill();
}
requestAnimationFrame(draw);
