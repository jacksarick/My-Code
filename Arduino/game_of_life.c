#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define WIDTH 128
#define HEIGHT 64

int matrix[WIDTH][HEIGHT];

void setup() {
	Serial.begin(9600);

	// by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
	display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3D (for the 128x64)
	// init done
	
	// Show image buffer on the display hardware.
	// Since the buffer is intialized with an Adafruit splashscreen
	// internally, this will display the splashscreen.
	display.display();
	delay(2000);

	// Clear the buffer.
	display.clearDisplay();

	// draw a single pixel
	display.drawPixel(10, 10, WHITE);
	// Show the display buffer on the hardware.
	// NOTE: You _must_ call display after making any drawing commands
	// to make them visible on the display hardware!
	display.display();
	delay(2000);
	display.clearDisplay();
}

	
bool isFilled(bool x, bool y) {
	return matrix[x] && matrix[x][y];
}

bool countNeighbours(bool x, bool y) {
	int amount = 0;
	
	if (isFilled(x-1, y-1)) amount++;
	if (isFilled(x,   y-1)) amount++;
	if (isFilled(x+1, y-1)) amount++;
	if (isFilled(x-1, y  )) amount++;
	if (isFilled(x+1, y  )) amount++;
	if (isFilled(x-1, y+1)) amount++;
	if (isFilled(x,   y+1)) amount++;
	if (isFilled(x+1, y+1)) amount++;
	
	return amount;
}

void draw_matrix(){
	//JARVIS, run the "clean slate" protocol
	display.clearDisplay();

	//For each row
	for (int k = 0; k < WIDTH; k++) {
		//For each column
		for (int p = 0; p < HEIGHT; p++) {
			//Shits there?
			if (isFilled(k,p)){
				// Draw Shit!
				display.drawPixel(k,p);
			}
		}
	}

	//Show our work
	display.display();
}


void loop() {
	//For each row..
	for (int i = 0; i < WIDTH; i++) {
		//For each column
		for (int j = 0; j < HEIGHT; j++) {
			//Tally up the neighbors
			int state = countNeighbours(i,j);

			//If it's alive
			if (isFilled(i,j)){
				//If it has less than 2 neighbors, it dies from under-population
				if (state < 2){
					matrix[i][j] = false;
				}

				//If it has more than 3 neighbors, it dies from over-population
				if (state > 3){
					matrix[i][j] = false;
				}

				//Else... do nothing cuz you're alive
			}

			//If it's dead, but it has three neighbors, it gets born. Genetics are weird
			if (!isFilled(i,j) && state == 3){
				matrix[i][j] = true;
			}
		}
	}

	draw_matrix();
	Serial.println(matrix);

	delay(500);
}