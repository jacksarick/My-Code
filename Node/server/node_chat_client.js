// Client
var sock = require('net').Socket();
sock.connect(8080);

sock.on('data', function (data) {
	console.log(data.toString());
	sock.write(data.toString());
});
sock.end();