// server
require('net').createServer(function (socket) {
	console.log("connected");

	socket.on('data', function (data) {
		console.log(data.toString());
	});
}).listen(8080);

// client
var sock = require('net').Socket();
sock.connect(8080);
sock.write('Hello');
sock.end();