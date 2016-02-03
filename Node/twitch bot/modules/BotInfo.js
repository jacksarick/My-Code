exports.setup = function() {
	commands.commands = {
		rank: 0,
		command: function(user, message, channel) {
			bot.say(channel, "Info on how to use this bots commands can be found at: https://github.com/chalenged/bearded-meme/wiki/Commands");
		}
	}
	commands.about = {
		rank: 0,
		command: function(user, message, channel) {
			bot.say(channel, "Bearded-Meme is an open source bot created by Chalenged, and can be found here: https://github.com/chalenged/bearded-meme");
		}
	}
	commands.ticket = {
		rank: 0,
		command: function(user, message, channel) {
			bot.say(channel, "Issues can be posted to https://github.com/chalenged/bearded-meme/issues . If you find any bugs/oversights etc with the bot, report it there.");
		}
	}
	commands.issues = commands.ticket;
};

exports.requirements = ["commands"];