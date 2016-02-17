// Client
var stdin = process.openStdin();
var sock  = require('net').Socket();

sock.connect(8080);

sock.on('data', function (data) {
	console.log(data.toString());
});


stdin.addListener("data", function(text) {
	try {
		sock.write(text.toString().trim());
		sock.end();
	}

	catch (err) {
		console.log(err.message);
	}
});