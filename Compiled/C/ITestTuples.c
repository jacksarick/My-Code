//C hello world example
#include <stdio.h>

typedef struct
{
	int x, y;
} coord;

int main()
{
	coord testcoord = {4, 9};
	printf("%d", testcoord.y);
	return 0;
}