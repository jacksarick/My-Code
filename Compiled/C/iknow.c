#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int fibonnaci(int x){
	if (x < 2){
		return 1;
	}
	else{
		return (fibonnaci(x - 1) + fibonnaci(x - 2));
	}
}

int main(){
	long unsigned answer = 0;
	for (int i = 0; i < 50; ++i){
		long unsigned answer = fibonnaci(i);
		printf("%lu\n", answer);
	}

	return 0;
}