// server
require('net').createServer(function (socket) {
	console.log("connected");

	socket.on('data', function (data) {
		console.log(data.toString());
		s.write(data.toString());
	});
}).listen(8080);