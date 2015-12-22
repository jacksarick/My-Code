#include <IRLib.h>

//Make all the buttons
#define HELD 4294967295
#define CENTER 2011275488
#define LEFT 2011271392
#define RIGHT 2011259104
#define UP 2011255008
#define DOWN 2011246816

int recent = 0;

//Create a receiver object to listen on pin 11
IRrecv My_Receiver(11);

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
    
//    Check if button held
    if(My_Decoder.value == HELD){
      recent;
    }

    else{
      recent = My_Decoder.value;
    }
    
    switch(recent){
      case CENTER: Serial.println("CENTER Button"); break;
      case UP: Serial.println("UP Button"); break;
      case DOWN: Serial.println("DOWN Button"); break;
      case LEFT: Serial.println("LEFT Button"); break;
      case RIGHT: Serial.println("RIGHT Button"); break;
      default: Serial.println(My_Decoder.value); break;
    }
    My_Receiver.resume();     //Restart the receiver
  }
}
