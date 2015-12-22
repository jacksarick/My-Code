#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *drive_motor = AFMS.getMotor(1);

void setup() {
  AFMS.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  drive_motor->run(FORWARD);
  delay(1000);
  drive_motor->run(RELEASE);
  delay(3000);
}
