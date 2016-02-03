// imports
var express = require('express');
var config = require('read')

//Start server app
var app = express();

app.get('/', function(req, res){
	res.send("hello");
});

app.listen(3000);