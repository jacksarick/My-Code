# Bearded-Meme
This is a twitch bot. The name was suggested by GitHub, and I thought it was pretty dank so I kept it. :sunglasses:

#### Info
If you notice something wrong with the code, or just want to add things, feel free to make a pull request.

If you have any questions, concerns, or suggestions, contact me at any of the following: 

-	Email: <chalenged@users.noreply.github.com>
-	Twitch: [my twitch][mytwitch]
-	Twitter: http://twitter.com/_chalenged

#### Installation
First, install [node.js][node]. It is required for the bot to work. After installing node, you can either clone the git repository into a folder on your computer, fork the git so you can change things yourself, or simply downloading and extracting the zip file. If you just get the zip, you will have to make the changes yourself if you want any updates. After getting the folder ready, you will need to install the node modules from the command line in the folder you installed the bot to. On windows, you can simply use windows search for "cmd", which will open up the command prompt. Navigate to the folder through the console. You can copy the file directory from windows explorer and right click in command prompt to paste it in. do 
    >cd <directory>
To navigate to the directory. Encase the directory in double quotes if there is any whitespace in the directory. Once in the directory, assuming node.js was installed correctly, run
    >npm install
This should create a folder called "node\_modules" in the folder. These modules are used by the bot. Now that you have all of that installed, you will need to setup the "options.json" file. Make an options.json file (you can just make a text file and change the name to have the extention) in a [json][json] format following the rules of the [twitch-irc configuration](https://github.com/twitch-irc/documentation/blob/master/02_Configuration.md "configuration documentation"). An example options.json file is on the git. Note: twitch bots require a special oauth token to connect, instead of a standard password. You can get your oauth token [here][oauth]. Once you have that set up, the bot is ready to run at a _very_ basic level. Most of the functunality is encapsulated in modules, to allow for lots of customizability. 

If you feel you have followed these instructions properly (and at least attempted to setup your options), feel free to contact me (my info is above). I am willing to help with installation, but I will not do the work for you. 

#### Preferences 
The Preferences.txt file is very important to the bot's functionality, as it allows you to tell how you want the bot to behave, including which modules to load. The syntax of the preferences file is as follows:

-   All preferences stated before a channel has been stated will go to the "global" channel, which serves as a default. Preferences stated in specific channels have priority.
-   The modules preference is to be followed by which modules to load. The module should correspond to a js file in the modules folder.
-   Channels are to be denoted on a line starting with a '#'.
-   Example: 


        modules messagelogger example-module commands
        debugLevel 1

        #testchannel1
        commandCharacters !~
        lengthLimit 500
        capsTolerance 0.5
        log true

        #testchannel
        commandCharacters ~!
        lengthLimit -1
        capsTolerance 0.5
        log false

#### Modules
Modules are js files put into the modules folder, and are used to extend the functionality of the bot without requiring editing the main bot's code. Modules can have any of the following attributes using exports:

-   module.setup: function() - Called during setup, after bot is created. (bot is not likely to have successfully connected to twitch irc by this stage)
-   module.onMessage: function(user, message, channel) - a function called every time a user chats. (bot does not trigger itself through this)
-   module.priority: Number - Determines when to call setup and most other functions of the module, including onMessage. The higher thr priority number, the earlier it will be called. Default is 0 if not defined.
-   module.requirements: Array of strings - A list of modules this module requires. You can start a module name with a ! to indicate that the module has an incompatibility with a module.

Modules have access to the following attributes (as well as other implicitly declared attributes created by other modules): 

    fs //the file system require, used for file i/o
    twitchirc //the twitch-irc module require, used for many things
    bot //twitch-irc client bot
    preferences //an object that stores the preferences. Not recommended to use, use getPreferences method instead
    assertFolder(path) //ensures that a folder exists. Will create it if it doesn't i.e. assertFolder(./modules)
    modules //an object that stores the different modules
    getPreferences(preferenceName, channel, default) //gets the preference (In a string!) for the desired channel, defaulting to the global if none exists for that channel, and defaulting to the specified default if neither is specified
    runModules(functionName, ...)//runs a function on all modules that have that function, passing the elements from this function into the module function
    anything else provided by modules.

You can create "global" attributes such as these by simply implicitly declaring them, such as

    exports.setup = function() {
        commands = {};
    }

This way, all modules will have access to the attribute. Each module can use the "this" keyword within itself to easily keep track of variables that only that module needs, such as 

    exports.setup = function() {
        this.count = 0;
    }
    
    exports.onMessage = function() {
        this.count++;
        console.log("onMessage called " + this.count + " times.");
    }
    
Do note that if creating a function inside one of these functions (such as creating a command), you may need to set a variable to "this", because of the way "this" works. Look at the existing modules for more reference. Example-Module might be useful.

#### Channel Authorization
To allow the bot to do things such as change stream status and game, you need to setup an OAuth token, different than the one used to let the bot log in. To do so, simply go to https://api.twitch.tv/kraken/oauth2/authorize?response_type=token&client_id=46ltr2qjw2omg950rsp9bkpg9jintd3&redirect_uri=http://localhost&scope=channel_editor and change the scope as needed. Authorize bearded-meme to access your account. You will then be at what seems like and empty page, do **not** refresh. In the address bar will be an access token; copy the token and put it into the options JSON file under "channelTokens" and under <channelname> (check the example options for reference) Then the bot will be able to change your status and game through the related module. Remember that this token can be used to change status, game, and some other sensitive things, so be sure to keep the token private.

Feel free to make your own twitch app and configure the bot to work with that, using your own CLIENTID and access tokens. However, that's probably more trouble than it's worth.

[node]: https://nodejs.org/ "Node home site"
[json]: http://json.org "JSON home site"
[mytwitch]: http://twitch.tv/chalenged "My Twitch"
[oauth]: http://twitchapps.com/tmi/ "oauth twitch app"
