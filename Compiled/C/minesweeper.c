#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define red   "\033[0;31m"
#define blue  "\033[0;34m"
#define green "\033[0;32m"
#define grey  "\033[0;37m"
#define none  "\033[0m"

int printBoard(short bs, short pb[bs][bs], short gb[bs][bs]){
	//Weird self-referential voodoo ^ bullshit goin on here
	printf("\033[2J\033[1;1H");
	for (int i = 0; i < bs; ++i)
	{
		if ((bs - i) <= 9){ printf(" "); }
		printf(grey "%d ", (bs - i) );

		for (int j = 0; j < bs; ++j)
		{
			if (gb[i][j] == 1){
				if (pb[i][j] == 0)
				{
					printf(blue "%d ", pb[i][j]);
				}

				if (pb[i][j] == 9)
				{
					printf(red "%d ", pb[i][j]);
				}

				if ((pb[i][j] > 0) && (pb[i][j] < 9))
				{
					printf(green "%d ", pb[i][j]);
				}
			}
			else
			{
				printf(none "# ");
			}
		}
		printf(none "\n");
	}

	printf("%s   1 2 3 4 5 6 7 8 9 0 Ⅱ ½ ⅓ 4 ⅕\n", grey);

	return 0;
}

int main()
{
	//initial variable stuff
	srand(time(NULL)); //for random numbers
	static short boardsize = 15;
	short playboard[boardsize][boardsize];
	short guessboard[boardsize][boardsize];

	//sets mines
	for (int i = 0; i < boardsize; ++i)
	{
		short r1 = rand() % boardsize;
		short r2 = rand() % boardsize;

		playboard[r1][r2] = 9;
	}

	//sets flags
	short flagcounter = 0;
	for (int k = 0; k < boardsize; ++k)
	{
		for (int p = 0; p < boardsize; ++p)
		{
			if (playboard[k][p] != 9){
				//Logic to see if adjacent to bomb
				if ((playboard[k][p+1] == 9) && (p < boardsize)){ flagcounter++; }//r
				if ((playboard[k][p-1] == 9) && (p != 0)){ flagcounter++;  }//l
				if ((playboard[k+1][p] == 9) && (k <= boardsize)){ flagcounter++; }//b
				if ((playboard[k-1][p] == 9) && (k > 0)){ flagcounter++;  }//t
				if ((playboard[k+1][p+1] == 9) && (p < boardsize) && (k <= boardsize)){ flagcounter++; }//br
				if ((playboard[k+1][p-1] == 9) && (p != 0) && (k <= boardsize)){ flagcounter++;  }//bl
				if ((playboard[k-1][p+1] == 9) && (p < boardsize) && (k > 0)){ flagcounter++;  }//tr
				if ((playboard[k-1][p-1] == 9) && (p != 0) && (k > 0)){ flagcounter++;   }//tl
				
				playboard[k][p] = flagcounter;
			}
			flagcounter = 0;
		}
	}

	printBoard(boardsize, playboard, guessboard);
	for (int i = 0; i < (boardsize*boardsize); ++i)
	{
		short ui1;
		short ui2;
		printf("%sX coordinate:", none);
		scanf("%hd", &ui1);
		printf("%sY coordinate:", none);
		scanf("%hd", &ui2);
		guessboard[boardsize - ui2][ui1 - 1] = 1;
		printBoard(boardsize, playboard, guessboard);
	}
	return 0;
}