

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(2, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValueY = analogRead(A0);
  delay(100);
  int sensorValueX = analogRead(A1);
  int button = digitalRead(2);
  // print out the value you read:
  Serial.print("X: ");
  Serial.print(sensorValueX);
  Serial.print(" Y: ");
  Serial.print(sensorValueY);
  Serial.print(" B: ");
  Serial.print(button);
  Serial.println();
  delay(10);        // delay in between reads for stability
}
