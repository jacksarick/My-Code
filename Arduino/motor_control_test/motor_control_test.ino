#include <AFMotor.h>

AF_DCMotor motor(1, MOTOR12_64KHZ);
AF_DCMotor motor2(2, MOTOR12_64KHZ);
int inbyte = 0;

void setup() {
  Serial.begin(9600);
   motor.setSpeed(255);
   motor2.setSpeed(255);
}

void loop() {
  if (Serial.available() > 0) {
    inbyte = Serial.read();
    
    if (inbyte == 'f'){
      motor.run(BACKWARD);
      delay(1000);
      motor.run(RELEASE);
    }

    else if (inbyte == 'b'){
      motor.run(FORWARD);
      delay(1000);
      motor.run(RELEASE);
    }

    else if (inbyte == 'l'){
      motor2.run(FORWARD);
      delay(1000);
      motor2.run(RELEASE);
    }

    else if (inbyte == 'r'){
      motor2.run(FORWARD);
      delay(1000);
      motor2.run(RELEASE);
    }

    else{
      Serial.println("Not a command");
    }
  }
}
