// For two colour LED in 12 and 13
void setup() {
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(12, HIGH);
//  digitalWrite(13, LOW);
  delay(1000);
  digitalWrite(12, LOW);
//  digitalWrite(13, HIGH);
  delay(1000);
}
