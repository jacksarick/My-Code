var canvas = document.getElementById('canvas');
var crect = canvas.getBoundingClientRect();
canvas.addEventListener('mousemove', function(evt) {
var mousePos = {x: evt.clientX-crect.left, y: evt.clientY-crect.top};
