var lineReader = require('readline').createInterface({
	input: require('fs').createReadStream('file.md')
});

// We count header tags to make life easier
var header_num = 0;

// Generic count variable
var count;

// Most of our markdown patters
// var simple_md_patterns = /^#+.+|(`{1,3})[^`]+\1|(\*{1,3})[^\*]+\2|^\>.+/g;

var file_out = [];

lineReader.on('line', function (line) {

	// Header tag
	if (/^#+.+/.test(line)) {
		// Header count
		count = line.match(/^#+/)[0].length;

		// Strip header
		line = line.replace(/#/g, "");

		// Assemble tags
		var head = "<h" + count + " id=toc_" + header_num + ">";
		var tail = "</h" + count + ">";

		// Increment amount of header tags
		header_num++;

		// Return built line
		line = head + line + tail;
	}
	
	// Quote
	if (/^\>.+/.test(line)) {
		// Strip >
		line = line.replace(/^\>/, "");

		// Return built line
		line = "<blockquote>" + line + "</blockquote>"
	}

	// If it ain't a header or block-quote, wrap it in a paragraph
	else {
		line = "<p>" + line + "</p>";
	}

	// Codeblock
	if (/(`{1,3})[^`]+\1/.test(line)) {
		// Strip backticks
		line = line.replace(/`/g, "");

		// Return built line
		line = "<code>" + line + "</code>";
	}

	// Italics/Bold
	if (/(\*{1,3})[^\*]+\1/.test(line)) {
		// Weird thing happens: While it can find stuff to replace, it does

		// Both
		while (/(\*{3})[^\*]+\1/.test(line)) {
			// replace first *** with open <b><i>
			line = line.replace(/\*{3}/, "<b><i>");

			// Close above
			line = line.replace(/\*{3}/, "</i></b>");
		}

		// Bold
		while (/(\*{2})[^\*]+\1/.test(line)) {
			// replace first ** with open <b>
			line = line.replace(/\*{2}/, "<b>");

			// Close above
			line = line.replace(/\*{2}/, "</b>");
		}

		// Italics
		while (/\*[^\*]+\*/.test(line)) {
			// replace first * with open <i>
			line = line.replace(/\*/, "<i>");

			// Close above
			line = line.replace(/\*/, "</i>");
		}

		// Return built line
		line = line;
	}

	console.log(line);
	file_out.push(line);
});

console.log(file_out);