/**
 * Created by Chalenged on 4/15/2015.
 */

exports.preferences = {
    chatPersistence: "[Number] How long a user message allows for a user to be kept in userlist, in milliseconds. (Default: 300000, only used when tc is not 1)"
};

exports.setup = function(main) {
    userData = loadObject("./misc/userData.json"); //load syncronously
    for (var x in userData) {
        userData[x].userlist = []; //reset userlists
    }
    var self = this;
    //if (options.options.tc != 1) {
    //    console.log("Twitch Client is not client 1. For accurate joins/parts, set your twitch client version to 1. (options.options.tc)");
    //}
    bot.addListener('PRIVMSG', function(channel, user, msg, message) {
        var username = user.username;
        //console.log(channel + ": " + username);
        if (!userData.hasOwnProperty(channel)) {
            userData[channel] = {};
            userData[channel].userlist = [];
        }
        if (!userData[channel].hasOwnProperty(username)) {
            userData[channel][username] = {};
            userData[channel][username].joinDate = new Date();
        }
        if (userData[channel].userlist.indexOf(username) === -1) {
            userData[channel].userlist.push(username);
        }
        //console.log(JSON.stringify(main.userData));
        //if (options.options.tc != 1) { //if there will not be joins/parts
        //    setTimeout(function(channel, username, main) { //after the preset timeout, remove the user from the userlist
        //
        //        //console.log(JSON.stringify(main.userData));
        //        //console.log(main.userData[channel].userlist.indexOf(username));
        //        if (main.userData[channel].userlist.indexOf(username) > -1) //if user still exists
        //            main.userData[channel].userlist.splice(main.userData[channel].userlist.indexOf(username), 1); //remove from userlist
        //    }, Number(getPreference('chatPersistence', channel, 300000)), channel, user.username, main);
        //}
    });
    bot.addListener('JOIN', function (username, channel, message) {
        //console.log(username + " just joined channel " + channel);
        if (!userData.hasOwnProperty(channel)) {
            userData[channel] = {};
            userData[channel].userlist = [];
        }
        if (!userData[channel].hasOwnProperty(username)) {
            userData[channel][username] = {};
            userData[channel][username].joinDate = new Date();
            userData[channel].userlist.push(username);
        }

    });
    bot.addListener('PART', function (username, channel, message) {
        //console.log(username + " just left channel " + channel);
        if (main.userData[channel].userlist.indexOf(username) > -1) //if user still exists
            main.userData[channel].userlist.splice(main.userData[channel].userlist.indexOf(username), 1); //remove from userlist
    });
};

exports.onMessage = function(user, message, channel) {
    //if (userData.hasOwnProperty(channel))
    //    console.log("Userlist for " + channel + ": " + userData[channel].userlist);
};

exports.requirements = ['utils'];