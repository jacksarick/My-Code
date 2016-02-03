/**
 * Created by Chalenged on 6/1/2015.
 */
exports.setup = function() {
    commands.eval = {
        rank: 5,
        command: function(user, message, channel) {
            if (preferences["#global"].hasOwnProperty("admins")) if (!preferences["#global"].admins.indexOf(" " + user.username + " ")) return; //only global admins can eval
            var text;
            try {
                text = eval(message.substr(message.indexOf(" ")));
            } catch (err) {
                console.log(err);
            }
            if (text != undefined) {
                bot.say(channel, text);
            }
        }
    }
};

exports.requirements = ["commands"];