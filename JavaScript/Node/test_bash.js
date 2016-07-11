var exec = require('child_process').exec;

var ls = exec("ls", function(error, stdout, stderr){
	return stdout;
});

console.log(ls);