// Client
var stdin = process.openStdin();
var sock  = require('net').Socket();

sock.connect(8080, function() {
	console.log('Connection Opened');
});

sock.on('data', function (data) {
	console.log(data.toString());
});

sock.on('close', function() {
    console.log('Connection Closed');
});

sock.on('error', console.log);


stdin.addListener("data", function(text) {
	try {
		sock.write(text.toString().trim());
		sock.end();
	}

	catch (err) {
		console.log(err.message);
	}
});