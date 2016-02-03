var canvas;
var ctx;
var WIDTH = 400;
var HEIGHT = 600;


// Emulation functions
function countNeighbours(x, y) {
	var amount = 0;

	if (isFilled(x-1, y-1)) amount++;
	if (isFilled(x,   y-1)) amount++;
	if (isFilled(x+1, y-1)) amount++;
	if (isFilled(x-1, y  )) amount++;
	if (isFilled(x+1, y  )) amount++;
	if (isFilled(x-1, y+1)) amount++;
	if (isFilled(x,   y+1)) amount++;
	if (isFilled(x+1, y+1)) amount++;

	return amount;
}

function isFilled(x, y) {
	return board[x] && board[x][y];
}

// Drawing functions
function init() {
	canvas = document.getElementById("canvas");
	ctx = canvas.getContext("2d");
	return setInterval(draw, 100);
}

function clear() {
	ctx.clearRect(0, 0, WIDTH, HEIGHT);
}

function rect(x,y,) {
	ctx.beginPath();
	ctx.rect(x, y, 5, 5);
	ctx.closePath();
	ctx.fill();
	ctx.stroke();
}

function draw() {
	clear();

	var count = [0,0];

	for (cell in board){
		if (board[cell]){
			rect(count[0], count[1]);
		}

		count[0] += (count[0] == WIDTH)? -WIDTH : 5;
		count[1] += (count[1] == HEIGHT)? -HEIGHT : 5;
	}
}