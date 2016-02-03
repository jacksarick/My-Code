/**
  * Copyright (C) 2015 Chalenged
  * This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version.
  *
  * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
  *
  * You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

VERSION = "0.0.0.0";
CLIENTID = "46ltr2qjw2omg950rsp9bkpg9jintd3"; //used for twitch-api

net = require("net");
ircMsg = require("irc-message");
request = require("request");
//var options = require("./options.json");

options = require("./options.json");
//irc = require("irc");
//twitchirc = require("twitch-irc");
//net = require("net");
//ircMsg = require("irc-message");
fs = require("fs");

//bot = new twitchirc.client(options); //global so modules can access the bot, to make it say things, do actions, etc.
//
//
//bot.connect();



function User(username) {
    this.username = username;
    this.badges = {};
    this.isSubscriber = function() {
        return this.badges.subscriber == "1";
    };
    this.isMod = function() {
        return this.badges.mod == "1";
    };
    this.isTurbo = function() {
        return this.badges.turbo == "1";
    };
    this.isBroadcaster = function() {
        return this.badges.broadcaster == "1";
    };

}

bot = new (require('events').EventEmitter);
bot.setMaxListeners(0); //Unlimited listeners (Remember to delete a listener if you stop needing it!)
bot.say = function(channel, msg) {
    console.log("sending message to server");
    client.write("PRIVMSG " + channel + " :" + msg + "\r\n");
};

//net.connect(6667, 'irc.twitch.tv')
//    .pipe(ircMsg.createStream())
//    .on('data', function(message) {
//        console.log(message)
//    });

//client.addListener("data", function(chuck) {
//    console.log("Received: ", chunk);
//});

//
//
//var client = new net.Socket();

client = net.connect(6667, 'irc.twitch.tv', function () {
    console.log("Connected!");
    var channels = "";
    for (var i = 0; i < options.channels.length; i++) {
        channels += ":" + options.identity.username +"!" + options.identity.username + "@" + options.identity.username + ".tmi.twitch.tv JOIN #" + options.channels[i] + "\r\n";
    }

    client.write(
        "PASS " + options.identity.password + "\r\n" +
        "NICK " + options.identity.username + "\r\n" +
        "USER nodebot USING NODE IRC\r\n" +
        "CAP REQ :twitch.tv/tags\r\n" +
        "CAP REQ :twitch.tv/commands\r\n" +
        "CAP REQ :twitch.tv/membership\r\n" +
            //"TWITCHCLIENT 4\r\n" +
        channels
    );
    //client.write("PASS " + options.identity.password + "\r\n");
    //client.write("NICK " + options.identity.username + "\r\n");
    //client.write("JOIN #chalenged" + "\r\n");
});

client.pipe(ircMsg.createStream())
    .on('data', function(message) {
        console.log("RAW> " + message.raw);
        //console.log(message);
        /*this switch is for the different IRC commands that are sent to the bot client
         * EACH ONE should emit the command as the event, and the last parameter
         * should be the message, to allow modules to hook in and get access to
         * all prudent information
         * */
        switch (message.command) {
            case "JOIN":case "PART": //part and join are done is a very similar manner, so we do them in the same block
                var userregex = /(.*)!.*@.*\.tmi\.twitch\.tv/gi; //regex used to get user
                var data = userregex.exec(message.prefix);//get user from the prefix
                var room = message.params[0]; //the room
                var user = data[1];
                //console.log(data[1], "joined room", room, ".\r\n");
                bot.emit(message.command, user, room, message); //emits the message for modules to hook into (message is passed in incase it is useful)
            break;
            case "PRIVMSG":
                if (/^:jtv!jtv@jtv.tmi.twitch.tv/.test(message.raw)) { //info from the server has no username but still uses PRIVMSG, so treat it as if it was an INFO command
                    bot.emit("INFO", message);
                    return;
                }
                var user = new User(message.tags["display-name"]); //base object
                var room = message.params[0];
                user.badges.subscriber = message.tags.subscriber;
                user.badges.turbo = message.tags.turbo;
                if (message.tags["user-type"] == "mod") user.badges.mod = "1"; //if user has mod tag
                else user.badges.mod = "0";
                if (room.substr(1) == user.username) user.badges.broadcaster = "1"; //if user is the same as the room name they are the broadcaster
                else user.badges.broadcast = "0";
                var msg = message.params[1];
                bot.emit(message.command, user, room, msg, message);
                break;
            case "PING":
                client.write("PONG tmi.twitch.tv\r\n"); //fallthrough (modules can catch PING events, however useless that may be)
            default:
                bot.emit(message.command, message); //This way other events (such as MODE) can still be caught by modules
                break;
        }
    });

//
//client.setTimeout(0);
client.setEncoding("utf8");

String.prototype.getIndexes = function(arg) {//returns an array of indexes the arg appears
    var indexes = [];
    var text = this;
    var count = 0;
    var index = text.indexOf(arg);
    while (index > -1) {
        text = text.substr(index+1);
        count += index;
        indexes.push(count);
        count++;
        index = text.indexOf(arg);
    }
    return indexes;
};

String.prototype.clean = function() {//removes extra whitespace
    var text = this;
    text = text.replace(/\s+/g, " "); //removes multiple spaces, which is supported by IRC, but generally not shown
    text = text.trim(); //removes whitespace on the edges
    return text;
};

preferences = {};

assertFolder = function(folder) {
    fs.mkdir(folder, function(err) {
        if (!err) return;
        if (err.code != "EEXIST") //if the error was something other than the folder already existing
            console.log("Error while making " + folder + " folder: " + err);
    });
};

assertFolder("./modules"); //make sure modules exists
assertFolder("./misc");

var availableModules = fs.readdirSync("./modules/");//synchronous to ensure modules are loaded before bot starts

//console.log(availableModules);
function readPreferences() {
    var channel = "#global";
    preferences[channel] = {};
    var fail = false;
    try {
        var data = fs.readFileSync('./Preferences.txt', {encoding: 'utf8'}); //we want preferences loaded before things are set up, so load them synchronously
    } catch(err) {
        if (err.code === "ENOENT") fail = true; //no preferences file, none loaded
        else throw err; //some other readFile error
    }
    if (fail) {
        console.log("Preferences.txt file not found (no modules will be loaded!)");
        return; //can't read preferences if the file doesn't exist
    }
    data = data.replace(/\r/g, ""); //remove carriage returns
    var prefs = data.split("\n"); //splits for each line
    for (var i = 0; i < prefs.length; i++) { //operate on each line
        var line = prefs[i].clean(); //easy reference
        if (!line) continue;
        if (line.charAt(0) === '#') {
            channel = line;
            preferences[channel] = {};
            continue;
        }
        var index = line.indexOf(" "); //separator index
        if (index === -1) {
            var err = "Improperly formatted preferences file on line " + (Number(i) + 1) + ": No space";
            throw err;
        }
        var end = line.indexOf("//"); //finds comments
        if (end === -1) end = data.length; //end of line if no comments
        preferences[channel][line.substring(0, index)] = line.substring(index + 1, end); //adds to preferences object
    }
    console.log("Preferences successfully loaded");
}
readPreferences();

var modulesToLoad = [];
modules = {};
function loadModules() {
    if (preferences["#global"]["modules"]) { //finds requested modules
        var modulesToUse = preferences["#global"]["modules"].split(" ");
        for (var i = 0; i < modulesToUse.length; i++) {
            var mod = modulesToUse[i] + ".js";
            var found = false;
            for (var j = 0; j < availableModules.length; j++) {
                var avMod = availableModules[j];

                if (avMod.toLowerCase() === mod.toLowerCase()) {
                    found = true;
                    modulesToLoad.push(avMod);
                }
            }
            if (!found) throw "Error loading module " + mod + ": Module not found";
        }
    }
    if (modulesToLoad.length > 0) console.log("Loading modules: ", modulesToLoad.join(", ").replace( /.js/g, ""));

    for (var i = 0; i < modulesToLoad.length; i++) {
        var module = modulesToLoad[i];
        //console.log(this);
        modules[module.substring(0, module.length-3)] = require("./modules/" + module);
    }

}
loadModules();

function checkModuleRequirements() {
    for (var x in modules) {
        if (!modules[x].hasOwnProperty("requirements")) continue; //if no requirements, move to next module
        for (var i = 0; i < modules[x].requirements.length; i++) {
            var found = false;
            var moduleList = Object.keys(modules);
            for (var j = 0; j < moduleList.length; j++) {
                if (moduleList[j].toLowerCase() === modules[x].requirements[i].toLowerCase() || modules[x].requirements[i].charAt(0) === "!") found = true;
                if (modules[x].requirements[i].charAt(0) === "!") {
                    if (moduleList[j].toLowerCase() === modules[x].requirements[i].substr(1).toLowerCase()) {
                        var err = "Error loading module " + x + ": incompatable with " + modules[x].requirements[i].substr(1);
                        console.log(err);
                        throw err;
                    }
                }
            }
            if (!found) {
                    var err = "Error loading module " + x + ": Requires " + modules[x].requirements[i];
                    console.log(err);
                    throw err;
            }
        }
    }
}
checkModuleRequirements();

/*
bot = new irc.Client(settings.server, settings.nick, {
    channels: [settings.channels + " " + settings.password],
    debug: false,
    password: settings.password,
    username: settings.nick
});

bot.addListener("join", function (channel, who) {
    if(who === settings.nick){
        console.log("Bot successfully joined channel " + channel);
    }
    else {
        //console.log(who + " joined the chat!");
        //var mes = "Welcome to the channel, " + who + "!";
        //bot.say(settings.channels[0], mes);
    }
});
*/

getPreference = function(preference, channel, defaultValue) { //global function, modules need this function
    if (preferences.hasOwnProperty(channel) && preferences[channel].hasOwnProperty(preference)) return preferences[channel][preference];
    if (preferences["#global"].hasOwnProperty(preference)) return preferences["#global"][preference];
    else return defaultValue;
};


function setupModules() {
    var priorityList = modulePriorityList();
    if (priorityList.length === 0) return; //no reason to try loading modules that don't exist
    console.log("Setting up modules...");
    for (var i = 0; i < priorityList.length; i++) { //setup modules in order of priority
        if (modules[priorityList[i]].hasOwnProperty("setup")) modules[priorityList[i]].setup(this);
    }
}
setupModules();

function modulePriorityList() {
    return Object.keys(modules).sort(function(a, b) {   //sorts modules based on priority level
        if (!modules[b].hasOwnProperty("priority")) modules[b].priority = 0; //defaults to 0 priority
        if (!modules[a].hasOwnProperty("priority")) modules[a].priority = 0;
        return modules[b].priority - modules[a].priority ;          //higher priority objects get ran first
    });                                                             //same priority shouldn't matter the order. If it does, the priorities should be changed
}

runModules = function(func) {
    //console.log(priorityList);
    //this[func].apply(this, Array.prototype.slice.call(arguments, 1));
    var priorityList = modulePriorityList();
    for (var i = 0; i < priorityList.length; i++) {
        if (Number(getPreference("debugLevel", "#global", "0")) > 1) console.log("Running " + func + " on module" + priorityList[i]);
        if (modules[priorityList[i]].hasOwnProperty(func)) modules[priorityList[i]][func].apply(modules[priorityList[i]], Array.prototype.slice.call(arguments, 1));
    }
};
//runModules();
/*
for (var x in settings.channels) {
    var channel = settings.channels[x];
    try {
        bot.addListener("message" + channel, function (nick, to, text, message) {
            //bot.say("#chalenged", to);
            //console.log(text);
            var chan = text.args[0];
            //if (nick === "twitchnotify" && chan === "#cirno_tv") {
            //    //twitchnotify: potatohandle subscribed for 17 months in a row!
            //    //var months = to.indexOf("for") + 4;
            //    //console.log(months);
            //    console.log(to);
            //    var subber = to.split(" ")[0];
            //    if (to.indexOf("for") === -1) {
            //        bot.say(chan, "cirFairy cirMini Welcome to the Baka Brigade, " + subber + "! cirMini cirFairy");
            //    } else {
            //        var months = to.split("for ")[1].split(" months")[0];
            //        bot.say(chan, "cirFairy cirMini Welcome back to the Baka Brigade, " + subber + "! " + months + " months! cirMini cirFairy");
            //    }
            //    //bot.say(chan, "cirMini");
            //}

             //if (messages[chan][nick].length >= 2 && messages[chan][nick][0].split(messages[chan][nick][1]).length === 3) {
                //console.log(nick + " is trying to pyramid!");
             //}
             //if (messages[chan][nick].length >= 2 && messages[chan][nick][0].split(messages[chan][nick][2]).length === 4) {
                 //if (pyramidBlock && nick != "chalenged") bot.say(chan, "cirMini");
                 //console.log(nick + " is trying to pyramid even more!");
             //}
            runModules("onMessage", nick, to, chan, text);
        });
    } catch (err) {
        console.log("Error adding message listener: " + err);
    }
}

bot.addListener("raw", function(message) {
    console.log(message);
});
*/





bot.addListener('PRIVMSG', function (user, room, msg, message) {
    console.log(user, ": ", msg);
    runModules("onMessage", user, room, msg, message);
});
/*
process.stdin.setEncoding('utf8');

process.stdin.on('readable', function() {
    var chunk = process.stdin.read();
    if (chunk !== null) {
        console.log(eval(chunk));
    }
});
*/