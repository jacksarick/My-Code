#define R_PIN 11
#define G_PIN 12
#define B_PIN 13

int sensorValue = 0;

void setup() {
  Serial.begin(9600);
  pinMode(R_PIN, OUTPUT);
  pinMode(G_PIN, OUTPUT);
  pinMode(B_PIN, OUTPUT);
}

void loop() {
//  Take R value
  //Turn on the red LED
  digitalWrite(R_PIN, HIGH);
  //Take a reading and convert the sensor value to a number between 0 and 255
  sensorValue = map(analogRead(A0), 0, 1023, 0, 256);
  //Turn red LED off
  digitalWrite(R_PIN, LOW);
  //Display values
  Serial.print("R: ");
  Serial.print(sensorValue);
  Serial.println();
  //1/100th of a second pause
  delay(10);
  
//  Take G value
  digitalWrite(G_PIN, HIGH);
  sensorValue = map(analogRead(A0), 0, 1023, 0, 256);
  digitalWrite(G_PIN, LOW);
  Serial.print("G: ");
  Serial.print(sensorValue);
  Serial.println();
  delay(10);

//  Take B value
  digitalWrite(B_PIN, HIGH);
  sensorValue = map(analogRead(A0), 0, 1023, 0, 256);
  digitalWrite(B_PIN, LOW);
  Serial.print("B: ");
  Serial.print(sensorValue);
  Serial.println();

  //This should be the number of seconds between readings divided by 1,000
  delay(100);
}
