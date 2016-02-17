// Server
var users = [];
require('net').createServer(function (sock) {
	console.log("connected");

	sock.on('data', function (data) {
		console.log(data.toString());
		sock.write(data.toString());
	});

	sock.on('end', function() {
        console.log('disconnected');
    });

    sock.on('error', console.log);
}).listen(8080);