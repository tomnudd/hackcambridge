// Change seaRiseAmt to a number between 0 and 100 to set base sea level!
// public domain

var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

seaRiseAmt = 50

var date = Date.now();
function draw(delta) {
  requestAnimationFrame(draw);

  canvas.width = canvas.width;

  rise = (seaRiseAmt/100) * canvas.height

  ctx.save()

  ctx.fillStyle = "#87ceeb";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

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

  ctx.restore()

  ctx.translate(0, canvas.height);
ctx.scale(1, -1);

  ctx.beginPath();
  ctx.lineTo(canvas.width,600);
  ctx.arc(0.4*canvas.width, 0, 400, 0.5*Math.PI, 1*Math.PI);
  ctx.lineTo(canvas.width,0);
  ctx.fillStyle = "#c2b280";
  ctx.fill();

}
requestAnimationFrame(draw);
