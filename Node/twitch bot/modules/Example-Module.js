/**
 * Created by Chalenged on 3/30/2015.
 */

exports.setup = function() {
    this.count = {};
    var self = this;
    commands.example = {
        "command": function(user, message, channel) {
        bot.say(channel, "Hello, " + user.username + "! This is an example command!");
    },
        "rank": 0
    };
    commands.count = {};
    commands.count.command = function(user, message, channel) {
        if (!this.count) this.count = {};
        if (!this.count[channel]) this.count[channel] = 0;
        this.count[channel]++;
        bot.say(channel, "This command has been used " + this.count[channel] + " times!");
    };
    commands.count.rank = 0;
};

exports.requirements = ["commands", "!incompatablemodule"];