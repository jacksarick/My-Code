void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.write("Start 5 Minutes");
  delay(300000);
  Serial.write("End 5 Minutes");
  delay(1000);
}
