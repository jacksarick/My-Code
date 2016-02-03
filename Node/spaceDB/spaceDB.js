function readUserData(srcPath, callback) { 
	fs.readFile(srcPath, 'utf8', function (err, data) {
			if (err) throw err;
			callback(data);
		}
	);
}

function copyFileContent(savPath, data) { 
	fs.writeFile (savPath, data, function(err) {
		if (err) throw err;
		console.log('complete');
	});
}
