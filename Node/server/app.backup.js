/*
 * Module dependencies
 */
var express  = require('express')
	, stylus = require('stylus')
	, nib    = require('nib')
	, url    = require('url')
	, mysql  = require('mysql')

// Jade compiler
var app = express();

function compile(str, path) {
	return stylus(str)
		.set('filename', path)
		.use(nib());
}

app.set('views', __dirname + '/views');
app.set('view engine', 'jade');
app.use(express.logger('dev'));
app.use(stylus.middleware(
	{ src: __dirname + '/resources'
	, compile: compile
	}
));
app.use(express.static(__dirname + '/resources'));

// console.log(get_table("article"));

article = {title : "Look at me, I'm an article", date:"10/4/15", author:"Jack Sarick", body : "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."}

// Index
app.get('/', function (req, res) {
	console.log("received!")
	res.render('index',
		{
			"arg": "value"
		}
	)
})

// Turn server on
console.log("Started!")
app.listen(8080);
