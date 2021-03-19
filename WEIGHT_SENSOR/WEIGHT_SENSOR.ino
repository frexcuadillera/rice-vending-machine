//int val[13];
//
//void setup() {
//  // put your setup code here, to run once:
// 
//  for(int i = 0; i < 13; i++){
//    val[i] = 0;
//    pinMode(i, INPUT);
//  }
//
//  Serial.begin(9600);
//
//
//}
//
//void loop() {
//  // put your main code here, to run repeatedly:
//  for(int i = 0; i < 13; i++){
//    val[i] = digitalRead(i);
//  }
//
//  for(int i = 0; i < 13; i++){
//    Serial.print(val[i]);
//  }
//
//  Serial.println();
//
//}


int val[13];

void setup(){
  Serial.begin(1000000);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
  pinMode(A6, INPUT);
  pinMode(A7, INPUT);
  pinMode(A8, INPUT);
  pinMode(A9, INPUT);
  pinMode(A10, INPUT);
  pinMode(A11, INPUT);
  pinMode(A12, INPUT);
  
  for(int i = 0; i < 13; i++){
    val[i] = 0;
  }
}

void loop(){

  for(int i = 0; i < 13; i++){
    val[i] = analogRead(i);
    Serial.print(val[i]); 
    Serial.print(" ");  
  }
  Serial.println();

  
}
