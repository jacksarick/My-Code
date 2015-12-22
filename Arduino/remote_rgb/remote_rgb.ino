#include <IRLib.h>

//Make all the buttons
#define HELD 4294967295
#define CENTER 2011275488
#define LEFT 2011271392
#define RIGHT 2011259104
#define UP 2011255008
#define DOWN 2011246816
#define MENU 2011283680

//Our nice little RGBness
#define G_PIN 11
#define R_PIN 10
#define B_PIN 9

int recent = 0;

int colours[] = {0, 0, 0};
int selected_led = 0;


//Create a receiver object to listen on pin 11
IRrecv My_Receiver(6);

//Create a decoder object
IRdecode My_Decoder;

void setup()
{
	Serial.begin(9600);
	My_Receiver.enableIRIn(); // Start the receiver
}

void loop() {
	//Continuously look for results. When you have them pass them to the decoder
	if (My_Receiver.GetResults(&My_Decoder)) {
		My_Decoder.decode();
		
		// Check if button held
		if(My_Decoder.value == HELD){
			recent;
		}

		else{
			recent = My_Decoder.value;
		}
		
		// Write out the values
		switch(My_Decoder.value){
			case CENTER:
				colours[selected_led] = (colours[selected_led] == 255)? 0 :255;
				break;

			case MENU:
				colours[0] = 255;
				colours[1] = 255;
				colours[2] = 255;
				break;
			
			case UP:
				colours[selected_led] += (colours[selected_led] < 255)? 1 : 0;
				break;
			
			case DOWN:
				colours[selected_led] -= (colours[selected_led] > 0)? 1 : 0;
				break;
			
			case LEFT:
				selected_led -= 1;
				selected_led %= 3;
				break;
			
			case RIGHT:
				selected_led += 1;
				selected_led %= 3;
				break;
		}


		// write to the pins
		Serial.println(colours[0]);
		Serial.println(colours[1]);
		Serial.println(colours[2]);
		analogWrite(R_PIN, colours[0]);
		analogWrite(G_PIN, colours[1]);
		analogWrite(B_PIN, colours[2]);
		My_Receiver.resume();     //Restart the receiver
	}
}
