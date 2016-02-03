/**
 * Created by Chalenged on 6/5/2015.
 */

exports.setup = function() {
    commands.status = {
        command: function(user, message, channel) {
            var reqRank = getPreference("statusRank", channel, 4); //default to broadcaster rank
            if (reqRank <= getRank(user, channel) && message.indexOf(" ") > -1) { //user has enough rank to change status, and has a status to set
                var statusToSet = message.split(" ").slice(1).join(" "); //remove the command trigger
                //var game;
                //request("https://api.twitch.tv/kraken/channels/" + channel.substr(1), function (error, response, body) {
                //    var game = JSON.parse(body).game;
                //});
                var opts = {
                    "channel": {
                        "status": statusToSet
                    }
                };
                if (!options.hasOwnProperty("channelTokens") || !options.channelTokens.hasOwnProperty(channel.substr(1))) {
                    bot.say(channel, "No access token found.");
                }
                var oauth = "OAuth " + options.channelTokens[channel.substr(1)];
                request.put({url:"https://api.twitch.tv/kraken/channels/" + channel.substr(1), form: opts, headers: {"Client-Id": CLIENTID, "Accept": 'application/vnd.twitchtv.v2+json', "Authorization": oauth}}, function (error, response, body) {
                    body = JSON.parse(body);
                    if (body.hasOwnProperty("error")) {
                        bot.say(channel, "Error updating status: " + body.message)
                    }
                    var status = body.status;
                    bot.say(channel, "Current status: " + status);
                });
            } else {
                request("https://api.twitch.tv/kraken/channels/" + channel.substr(1), function (error, response, body) {
                    //console.log(JSON.parse(body));
                    var status = JSON.parse(body).status;
                    bot.say(channel, "Current status: " + status);
                });
            }
        },
        rank: 0
    };
    commands.title = commands.status; //alias

    commands.game = {
        command: function(user, message, channel) {
            var reqRank = getPreference("statusRank", channel, 4); //default to broadcaster rank
            if (reqRank <= getRank(user, channel) && message.indexOf(" ") > -1) { //user has enough rank to change status, and has a status to set
                var gameToSet = message.split(" ").slice(1).join(" "); //remove the command trigger
                //var game;
                //request("https://api.twitch.tv/kraken/channels/" + channel.substr(1), function (error, response, body) {
                //    var game = JSON.parse(body).game;
                //});
                var opts = {
                    "channel": {
                        "game": gameToSet
                    }
                };
                if (!options.hasOwnProperty("channelTokens") || !options.channelTokens.hasOwnProperty(channel.substr(1))) {
                    bot.say(channel, "No access token found.");
                }
                var oauth = "OAuth " + options.channelTokens[channel.substr(1)];
                request.put({url:"https://api.twitch.tv/kraken/channels/" + channel.substr(1), form: opts, headers: {"Client-Id": CLIENTID, "Accept": 'application/vnd.twitchtv.v2+json', "Authorization": oauth}}, function (error, response, body) {
                    body = JSON.parse(body);
                    if (body.hasOwnProperty("error")) {
                        bot.say(channel, "Error updating status: " + body.message)
                    }
                    var game = body.game;
                    bot.say(channel, "Current status: " + game);
                });
            } else {
                request("https://api.twitch.tv/kraken/channels/" + channel.substr(1), function (error, response, body) {
                    //console.log(JSON.parse(body));
                    var game = JSON.parse(body).game;
                    bot.say(channel, "Current game: " + game);
                });
            }
        },
        rank: 0
    }
};

exports.requirements = ["commands"];