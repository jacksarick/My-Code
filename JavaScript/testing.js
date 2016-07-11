function make_list() {
	var list = [];
	for (var i = 0; i <= 100; i++) {
		list.push([i, i]);
	}

	return list;
}

function setup(){
	var my_list = make_list();
}

function loop(){
	for (var i = my_list.length - 1; i >= 0; i--) {
		draw(my_list[i]);
	}
}

console.log(list);