/**
 * Created by Chalenged on 4/12/2015.
 */
exports.setup = function() {
    saveObject = function (filename, object, sync) {
        //console.log("test");
        try {
            if (sync) return fs.writeFileSync(filename, JSON.stringify(object));
        } catch (err) {
            console.log("Error saving object synchronously.");
            throw err;
        }
        fs.writeFile(filename, JSON.stringify(object), function (err) {
            if (err) {
                console.log("Error saving object.");
                throw err;
            }
        })
    };

    loadObject = function (filename, callback) {
        if (!callback) {
            var obj = {};
            try {
                obj = JSON.parse(fs.readFileSync(filename));
            } catch (err) {
                if (err.code != "ENOENT") {
                    console.log("Error loading object synchronously.");
                    throw err;
                }
            }
            return obj;
        }
        fs.readFile(filename, function (err, data) {
            if (err && err.code != "ENOENT") {
                console.log("Error loading object.");
                throw err;
            } else {
                if (err && err.code == "ENOENT") {
                    callback({});
                } else {
                    callback(JSON.parse(data));
                }
            }

        });
    };


};

exports.priority = 11; //high priority since it's used by lots of modules