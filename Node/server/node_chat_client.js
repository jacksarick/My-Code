// Client
var sock = require('net').Socket();
sock.connect(8080);

sock.on('data', function (data) {
	console.log(data.toString());
});

process.stdin.on('data', function (text) {
	if (text === 'quit\n') {
		console.log("bye!");
		process.exit();
	}
	sock.write(util.inspect(text));
});

sock.end();