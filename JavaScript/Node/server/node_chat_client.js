// Client
var stdin = process.openStdin();
var sock  = require('net').Socket();
var uid = "" + Math.floor(Math.random() * 10000);
console.log("You are user " + uid);

sock.connect(8080, function() {
	console.log('Connection Opened');
});

sock.on('data', function (data) {
	data = JSON.parse(data.toString());
	console.log(data);
	if (data.usr != uid) {
		console.log(data.usr + ": " + data.msg);
	}
});

sock.on('close', function() {
    console.log('Connection Closed');
});

sock.on('error', console.log);

stdin.addListener("data", function(text) {
	try {
		var packet = {};
		packet.usr = uid;
		packet.msg = text.toString().trim();
		sock.write(JSON.stringify(packet));
		// sock.end();
	}

	catch (err) {
		console.log(err.message);
	}
});