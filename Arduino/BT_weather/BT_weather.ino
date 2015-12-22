#include <SoftwareSerial.h>
#include <dht.h>

SoftwareSerial BT(10, 11); 
dht DHT;
#define DHT11_PIN 12

// creates a "virtual" serial port/UART
// connect BT module TX to D10
// connect BT module RX to D11
// connect BT Vcc to 5V, GND to GND
// connect DHT S to 12, GND to GND, and PWR to 3.3

void setup()  
{
  // set digital pin to control as an output
  pinMode(13, OUTPUT);
  // set the data rate for the SoftwareSerial port
  BT.begin(9600);
  // Send test message to other device
  BT.println("Hello from Arduino");
}

void loop() 
{
  if (BT.available())
  // if text arrived in from BT serial...
  {
    // READ DATA
    BT.print("DHT11, \t");
    int chk = DHT.read11(DHT11_PIN);
    switch (chk)
    {
      case DHTLIB_OK:  
                  BT.print("OK,\t"); 
                  break;
      case DHTLIB_ERROR_CHECKSUM: 
                  BT.print("Checksum error,\t"); 
                  break;
      case DHTLIB_ERROR_TIMEOUT: 
                  BT.print("Time out error,\t"); 
                  break;
      case DHTLIB_ERROR_CONNECT:
          BT.print("Connect error,\t");
          break;
      case DHTLIB_ERROR_ACK_L:
          BT.print("Ack Low error,\t");
          break;
      case DHTLIB_ERROR_ACK_H:
          BT.print("Ack High error,\t");
          break;
      default: 
                  BT.print("Unknown error,\t"); 
                  break;
    }
    // DISPLAY DATA
    BT.print(DHT.humidity, 1);
    BT.print(",\t");
    BT.println(DHT.temperature, 1);
  
    delay(5000);
  }
}
