/**
 * Created by Chalenged on 4/22/2015.
 */

exports.setup = function(main) {
    this.quotes = loadObject("./misc/quotes.json"); //load quotes
    var self = this;
    //this.record = {
    //    game: {},
    //    date: {}
    //};
    this.record = loadObject("./misc/quotesettings.json");
    if (!this.record.hasOwnProperty("game")) {
    }
    commands.quote = {
        command: function(user, message, channel) {
            if (!self.quotes.hasOwnProperty(channel)) self.quotes[channel] = [];
            if (self.quotes[channel].length === 0) { //no quotes
                bot.say(channel, "This room doesn't have any quotes yet! Use !addquote to add some!");
                return;
            }
            args = message.split(" ");
            if (args.length === 1) { //no args, just command
                bot.say(channel, self.quotes[channel][Math.floor(Math.random() * self.quotes[channel].length)]); //say a random quote
                return;
            } else {
                if (args.length === 2) {//1 arg
                    if (!isNaN(args[1])) { //is a number
                        var index = Number(args[1]) - 1; //arrays start at 0
                        if (index < 0) { //negative quote number
                            return;
                        }
                        if (index-1 >= self.quotes[channel].length) { //too high
                            bot.say(channel, "There are only " + self.quotes[channel].length + " quotes!");
                            return;
                        }
                        bot.say(channel, self.quotes[channel][index]); //say quote
                        return;
                    }
                }
                var search = message.substr(message.indexOf(" ") + 1); //after command
                var found = [];
                var foundIndexes = [];
                for (var i = 0; i < self.quotes[channel].length; i++) {
                    if (self.quotes[channel][i].toLowerCase().indexOf(search.toLowerCase()) > -1) { //found
                        found.push(self.quotes[channel][i]);
                        foundIndexes.push(i + 1);
                    }
                }
                if (found.length === 0 ) {
                    bot.say(channel, "No quotes found.");
                    return;
                } else if (found.length === 1) {
                    bot.say(channel, "Quote #" + foundIndexes.pop() + ": " + found.pop());
                    return;
                } else {
                    bot.say(channel, "Matching quotes found at: " + foundIndexes.join(", "));
                    return;
                }

            }
        },
        rank: 0
    };

    commands.quotegame = {
        syntax: "quotegame <on/off>",
        command: function(user, message, channel) {
            if (!self.record.hasOwnProperty(channel)) {
                self.record[channel] = {
                    game: true,
                    date: true
                }
            }
            var state = message.split(" ", 2)[1];
            if (!state) state = "";
            if (state.toLowerCase() == "on") {
                self.record[channel].game = true;
                bot.say(channel, "Quotes will now automatically include the current game.");
            } else if (state.toLowerCase() == "off") {
                self.record[channel].game = false;
                bot.say(channel, "Quotes will no longer automatically include the current game.");
            } else {
                bot.say(channel, "Adding games to quotes is currently " + self.record[channel].game)
            }
        },
        rank: 3
    };
    commands.quotedate = {
        syntax: "quotedate <on/off>",
        command: function(user, message, channel) {
            if (!self.record.hasOwnProperty(channel)) {
                self.record[channel] = {
                    game: true,
                    date: true
                }
            }
            var state = message.split(" ", 2)[1];
            if (!state) state = "";
            if (state.toLowerCase() == "on") {
                self.record[channel].date = true;
                bot.say(channel, "Quotes will now automatically include the date.");
            } else if (state.toLowerCase() == "off") {
                self.record[channel].date = false;
                bot.say(channel, "Quotes will no longer automatically include the date.");
            } else {
                bot.say(channel, "Adding dates to quotes is currently " + self.record[channel].date)
            }
        },
        rank: 3
    };

    commands.addquote = {
        command: function(user, message, channel) {
            if (!self.quotes.hasOwnProperty(channel)) self.quotes[channel] = [];
            if (!self.record.hasOwnProperty(channel))
                self.record[channel] = {
                    game: true,
                    date: true
                };
            var quote = message.substr(message.indexOf(" ") + 1);
            if (self.record[channel].date) {
                quote += " [" + new Date().toUTCString() + "] ";
            }
            if (self.record[channel].game) {
                request("https://api.twitch.tv/kraken/channels/" + channel.substr(1), function (error, response, body) {
                    //console.log(JSON.parse(body));
                    var game = JSON.parse(body).game;
                    quote += " [" + game + "] ";
                    self.quotes[channel].push(quote);
                    saveObject("./misc/quotes.json", self.quotes);
                    bot.say(channel, "Quote #" + self.quotes[channel].length + " added!");
                    return;
                });
                return;
            }
            self.quotes[channel].push(quote);
            saveObject("./misc/quotes.json", self.quotes);
            bot.say(channel, "Quote #" + self.quotes[channel].length + " added!");
            return;
        },
        rank: 2
    };
    commands.delquote = {
        command: function(user, message, channel) {
            if (!self.quotes.hasOwnProperty(channel)) self.quotes[channel] = [];
            if (message.split(" ").length -1 !== 1) return;
            var index = message.split(" ")[1];
            self.quotes[channel].splice(index - 1, 1);
            saveObject("./misc/quotes.json", self.quotes);
            bot.say(channel, "Quote #" + index + " removed!");
            return;
        },
        rank: 2
    };
    commands.quotes = commands.quote; //alias(?) unsure if this works
};