/**
 * Created by Chalenged on 3/30/2015.
 */

/*
 * Commands structure is as follows:
 * commands.commandName = {"command": function(user, message, channel) {
 *   return "message to say";
 * },
 * "rank": <rank>;//rank is a numeric from 0-3. 0=regular, 1=subscriber, 2=moderator, 3=broadcaster
 * };
 * using the "this" keyword in a command represents the command object
 * */


exports.setup = function() {
    commands = {}; //global object for commands
    loadObject("./misc/voices.json", function(obj) {
        voices = obj;
    });
    commands.voice = {
        syntax: "!voice <add|del|list> [user]",
        command: function(user, message, channel) {
            if (!voices.hasOwnProperty(channel)) voices[channel] = [];
            var args = message.split(" ");
            if (args.length < 2) {
                bot.say(channel, "Correct syntax is: " + this.syntax);
                return;
            }
            if (/add/i.test(args[1])) {
                if (args.length != 3) {
                    bot.say(channel, "Correct syntax is: " + this.syntax);
                    return;
                }
                args[2] = args[2].clean().toLowerCase();
                if (voices[channel].indexOf(args[2]) > -1) {
                    bot.say(channel, "That user is already voiced!");
                    return;
                } else {
                    voices[channel].push(args[2]);
                    bot.say(channel, args[2] + " is now voiced.");
                    saveObject("./misc/voices.json", voices);
                }
            } else if (/del|delete|remove/i.test(args[1])) {
                if (args.length != 3) {
                    bot.say(channel, "Correct syntax is: " + this.syntax);
                    return;
                }
                args[2] = args[2].clean().toLowerCase();
                if (voices[channel].indexOf(args[2]) > -1) {
                    voices[channel].splice(voices[channel].indexOf(args[2]), 1);
                    bot.say(channel, args[2] + " is no longer voiced.");
                    saveObject("./misc/voices.json", voices);
                } else {
                    bot.say(channel, "That user isn't voiced yet!");
                    return;
                }

            } else if (/list/i.test(args[1])) {
                bot.say(channel, "Voices: " + voices[channel].join(", "));
            }
        },
        rank: 2
    };

    commands.voices = commands.voice;//alias

    getRank = function(user, channel) { //allows commands to easily get ranks
        if (getPreference("admins", channel, "").indexOf(" " + user.username + " ") > -1 || (preferences["#global"].hasOwnProperty("admins") && preferences["#global"].admins.indexOf(user.username) > -1)) return 5; //admins have highest rank
        if (user.isBroadcaster()) return 4;
        if (user.isMod()) return 3;
        if (voices.hasOwnProperty(channel) && voices[channel].indexOf(user.username.clean().toLowerCase()) > -1) return 2;
        if (user.isSubscriber()) return 1;
        else return 0;
    };

    readRank = function(rank) {
        rank = String(rank);
        rank = rank.trim();
        if ("012345".indexOf(rank) > -1) rank = "rsvmba"["012345".indexOf(rank)];
        var text = "";
        switch (rank) {
            case "r": text = "r (regular)"; break;
            case "s": text = "s (subscriber)"; break;
            case "v": text = "v (voice)"; break;
            case "m": text = "m (mod)"; break;
            case "b": text = "b (broadcaster)"; break;
            case "a": text = "a (admin)"; break;
            default: console.log("Error determining rank from \"" + rank + "\""); text = "undetermined"; break;
        }
        return text;
    }
};

exports.onMessage = function(user, channel, msg, message) {
    //console.log(user);
    var commandCharacters = getPreference("commandCharacters", channel, "!");
    var found = false;
    msg = msg.clean();
    //console.log(user.username, "has rank of", getRank(user, channel));
    //console.log("command characters: "  + commandCharacters);
    if (commandCharacters.indexOf(msg.charAt(0)) > -1) {
        var index = msg.indexOf(" ");
        if (index === -1) index = msg.length + 1;
        var command = msg.substring(1, index);
        if (commands.hasOwnProperty(command)) {
            if (!commands[command].hasOwnProperty("rank")) {
                commands[command].rank = 0;
                console.log("Command " + command + " had no rank set, defaulting to 0 (regular)");
            }
            if (commands[command].rank <= getRank(user, channel)) {
                if (!commands[command].hasOwnProperty("command")) {
                    console.log("Command object " + command + " found, but has no command function.");
                } else {
                    commands[command].command(user, msg, channel);
                    found = true;
                }
            }
        }
    }
    if (!found) runModules("customCommand", user, msg, channel); //won't fail if customCommands isn't loaded, but shouldn't affect other modules regardless
};

exports.priority = 10; //since any module that adds commands needs to run after commands is loaded, commands gets a high priority