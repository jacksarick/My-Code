'use strict';

function BinarySearchTree() {
	this.root = null;

	this.has = function(value, node) {
		if (node === undefined) node = this.root;

		if ((node.value > value && node.less == undefined) ||
			(node.value < value && node.greater == undefined)) return false;

		if (node.value == value) return true;
		if (node.value >  value) return this.has(value, node.less);
		if (node.value <  value) return this.has(value, node.greater);

	}

	this.add = function(value){

		let val = {
			"value": value
		};

		let node = this.root;

		if (!node){
			this.root = val;
			return;
		}

		while(true){
			if (node.value > value) {
				if (node.less === undefined){
					node.less = val;
					break;
				}

				node = node.less;
			}
			
			if (node.value < value) {
				if (node.greater === undefined){
					node.greater = val;
					break;
				}
				
				node = node.greater;
			}

			else {
				break;
			}
		}
	}

}

var bst = new BinarySearchTree();

var arr = [];
for (var i=0, t=40; i<t; i++) {
    arr.push(Math.round(Math.random() * t))
}

for (var i = arr.length - 1; i >= 0; i--) {
	bst.add(arr[i])
}

console.log(JSON.stringify(bst.root));
console.log(bst.has(21));
