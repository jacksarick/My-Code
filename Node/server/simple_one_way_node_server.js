// server
require('net').createServer(function (socket) {
	console.log("connected");

	socket.on('data', function (data) {
		console.log(data.toString());
	});
}).listen(8080);

// client
var s = require('net').Socket();
s.connect(8080);
s.write('Hello');
s.end();