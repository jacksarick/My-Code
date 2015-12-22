#define R_PIN 11
#define G_PIN 12
#define B_PIN 13

#define G_LED 9
#define R_LED 6
#define B_LED 5

void setup() {
  Serial.begin(9600);
  pinMode(R_PIN, OUTPUT);
  pinMode(G_PIN, OUTPUT);
  pinMode(B_PIN, OUTPUT);
}

void loop() {
//  Take R value
  //Display values
  Serial.print("R: ");
  Serial.print(colour(R_PIN));
  Serial.println();
  //1/100th of a second pause
  delay(100);
  
//  Take G value
  Serial.print("G: ");
  Serial.print(colour(G_PIN));
  Serial.println();
  delay(100);

//  Take B value
  Serial.print("B: ");
  Serial.print(colour(B_PIN));
  Serial.println();

  //This should be the number of seconds between readings divided by 1,000
  delay(200);
}

int colour(int N_PIN, int N_LED){
  //Turn on the N LED
  digitalWrite(N_PIN, HIGH);
  //Take a reading and convert the sensor value to a number between 0 and 255
  int sensorValue = map(analogRead(A0), 0, 1023, 0, 256);
  //Turn N LED off
  digitalWrite(N_PIN, LOW);

  //Write sensorValue to corresponding LED
//  analogWrite(N_LED, analogRead(A0)/100);
  return sensorValue;
}
