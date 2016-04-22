void setup() {
  // initialize digital pin 13 as an output.
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  digitalWrite(2, HIGH);
}

void loop() {
  digitalWrite(3, analogRead(A6));
  digitalWrite(4, analogRead(A7));
}
