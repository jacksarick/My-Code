int inbyte = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    inbyte = Serial.parseInt();
    
    if (inbyte == 1){
      Serial.println("Led On");
    }

    else if (inbyte == 0){
      Serial.println("Led Off");
    }

    else{
      Serial.println("Not a command");
    }
  }
}

