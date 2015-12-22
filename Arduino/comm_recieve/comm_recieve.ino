int inbyte = 0;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    inbyte = Serial.parseInt();
    
    if (inbyte == 1){
      digitalWrite(13, HIGH);
    }

    else if (inbyte == 0){
      digitalWrite(13, LOW);
    }

    else{
      Serial.println("Not a command");
    }
  }
}
