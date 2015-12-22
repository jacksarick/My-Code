void setup() {
  Serial.begin(9600);
  pinMode(11, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // print out the value you read:
  Serial.println(sensorValue);
  analogWrite(11,sensorValue*10);
  delay(1);        // delay in between reads for stability
}
