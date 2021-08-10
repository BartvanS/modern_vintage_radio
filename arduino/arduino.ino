int ledPin = 13;   // select the pin for the LED
int potPin = 2;
int value = 0;
void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);  // declare the ledPin as an OUTPUT
}
int handleSerial() {
  if (Serial.available() > 0) {
    String message = Serial.readString();
    if (message == "1\n") {
      digitalWrite(ledPin, HIGH);
    }
    else if (message == "0\n") {
      digitalWrite(ledPin, LOW);
    }
  }
  return 0;
}
int previousValue = 0;
void handleVolume() {
  value = analogRead(potPin);
  int mappedValue = map(value, 0, 1023, 0, 100);
  if (previousValue == mappedValue || mappedValue == 100) {
    return;
  }
  previousValue = mappedValue;
  Serial.println(mappedValue);
}

void loop() {
  handleSerial();
  handleVolume();
}
