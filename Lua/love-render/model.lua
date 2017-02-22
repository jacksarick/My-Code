function string:split( inSplitPattern, outResults )
	if not outResults then
		outResults = { }
	end
	local theStart = 1
	local theSplitStart, theSplitEnd = string.find( self, inSplitPattern, theStart )
	while theSplitStart do
		table.insert( outResults, string.sub( self, theStart, theSplitStart-1 ) )
		theStart = theSplitEnd + 1
		theSplitStart, theSplitEnd = string.find( self, inSplitPattern, theStart )
	end
	table.insert( outResults, string.sub( self, theStart ) )
	return outResults
end

function read_lines(filename)
	lines = {}

	for line in io.lines(file) do 
		lines[#lines + 1] = line
	end

	return lines
end

function load_model(filename)
	model = {v = {}, vt = {}, vn = {}, f = {}}
	for _, line in read_lines(filename) do
		arr = line:split(" ")
		_, model[arr[1]]
	end
end