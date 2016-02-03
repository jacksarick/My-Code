/**
 * Created by Chalenged on 3/30/2015.
 */

exports.setup = function() {
    messages = {};
    assertFolder("./misc/logs");
    logMessage = function (user, message, channel) {
        //console.log((getPreference("log", "#cirno_tv", true) === "0"));
        //if (!messages[channel]) messages[channel] = {};
        //if (!messages[channel][user.username]) messages[channel][user.username] = [];
        //if (messages[channel][user.username].length > 10) messages[channel][user.username].pop();
        //messages[channel][user.username].unshift(message);
        if (getPreference("log", channel, "true") === "false") return;
        fs.appendFile("./misc/logs/" + channel.substr(1) + ".txt", user.username + ": " + message + "\r\n", function (err) {
            if (err) throw err;
        });
    };
};

exports.onMessage = function(user, channel, msg, message) {
    logMessage(user, msg, channel);
};