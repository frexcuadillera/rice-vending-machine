#define credit1 2
#define credit2 3
#define credit3 4
#define credit4 5
#define inhibit 6

bool executed1 = false;
bool executed2 = false;
bool executed3 = false;

void setup() {
    Serial.begin(9600);
    pinMode(credit1, INPUT_PULLUP);
    pinMode(credit2, INPUT_PULLUP);
    pinMode(credit3, INPUT_PULLUP);
    pinMode(credit4, INPUT_PULLUP);
    pinMode(inhibit, OUTPUT);

    Serial.println(0);
}

void loop() {
         
  digitalWrite(inhibit, LOW); 

 if(digitalRead(credit1) == LOW && executed1 == false){
    Serial.println(20);
    executed1 = true;
 }
 
 if(digitalRead(credit1) == HIGH && executed1 == true){
    executed1 = false;
 }

 if(digitalRead(credit2) == LOW && executed2 == false){
    Serial.println(50);
    executed2 = true;
 }
  
 if(digitalRead(credit2) == HIGH && executed2 == true){
    executed2 = false;
 }

 if(digitalRead(credit3) == LOW && executed3 == false){
    Serial.println(100);
    executed3 = true;
  }
  
  if(digitalRead(credit3) == HIGH && executed3 == true){
    executed3 = false;
  }
  
}
