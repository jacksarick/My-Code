// Server
var connections = [];
var stdin = process.openStdin();

require('net').createServer(function (sock) {
	console.log("connected");

	sock.on('start', function (data) {
		console.log("connected!");
		console.log(sock);
		connections.push(sock);
	});

	sock.on('data', function (data) {
		console.log(data.toString());
		// for (var connection in connections){
			sock.write(data.toString());
		// }
	});

	sock.on('end', function() {
        console.log('disconnected');
    });

    sock.on('error', console.log);
}).listen(8080);

stdin.addListener("data", function(text) {
	try {
		eval(text.toString().trim());
	}

	catch (err) {
		console.log(err.message);
	}
});