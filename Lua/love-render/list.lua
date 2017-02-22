metalist = {}
function metalist.__concat(l1, l2)
	for k, v in pairs(l2) do l1[#l1 + 1] = v end
	return l1
end