/*
 * Module dependencies
 */
var express  = require('express')
	, url    = require('url');

var app = express();

app.use(express.logger('dev'));

// Index
app.get('/', function (req, res) {
	console.log(req);
	console.log(res);
})

// app.get("_", function (req, res) {
// 	console.log(req);
// 	console.log(res);
// })

// Turn server on
app.listen(8080);