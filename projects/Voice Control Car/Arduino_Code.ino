#include <SoftwareSerial.h>
SoftwareSerial BT(10, 11); //TX, RX 
String readvoice;
int RMF = 3; // IN1
int RMB = 4; //  IN2
int LMF = 5; // IN3
int LMB = 6; // IN4
void setup() {
 BT.begin(9600);
 Serial.begin(9600);
   pinMode (RMF, OUTPUT); 
  pinMode (RMB, OUTPUT);
  pinMode (LMF, OUTPUT);
  pinMode (LMB, OUTPUT);
}void loop() {
  while (BT.available()){ 
  delay(10); 
  char c = BT.read(); 
  readvoice += c; 
  } 
  if (readvoice.length() > 0) {
    
    Serial.println(readvoice);

  if(readvoice == "forward")
  {
    digitalWrite(RMF, HIGH);
    digitalWrite (LMF, HIGH);
    digitalWrite(RMB,LOW);
    digitalWrite(LMB,LOW);
    delay(100); }
else if(readvoice == "back")
  { digitalWrite(RMF, LOW);
    digitalWrite(LMF, LOW);
    digitalWrite(RMB, HIGH);
    digitalWrite(LMB,HIGH);
    delay(100); }
 else if (readvoice == "left")
  { digitalWrite (RMF,HIGH);
    digitalWrite (LMF,LOW);
    digitalWrite (RMB,LOW);
    digitalWrite (LMB,LOW);
   delay (100);}
 else if ( readvoice == "right")
 {digitalWrite (RMF, LOW);
   digitalWrite (LMF, HIGH);
   digitalWrite (RMB, LOW);
   digitalWrite (LMB, LOW);
   delay (100);}
 else if (readvoice == "stop")
 {digitalWrite (RMF, LOW);
   digitalWrite (LMF, LOW);
   digitalWrite (RMB, LOW);
   digitalWrite (LMB, LOW);
   delay (100);}
   else if (readvoice == "off"){ digitalWrite (RMF, LOW);
   digitalWrite (LMF, LOW);
   digitalWrite (RMB, LOW);
   digitalWrite (LMB, LOW);
   delay (100);}
else if (readvoice == "garba dance"){
 digitalWrite (RMF, LOW);digitalWrite (RMB, HIGH);
digitalWrite (LMF, LOW);digitalWrite (LMB, LOW);delay (400);
    digitalWrite(RMF, HIGH);
    digitalWrite (RMB, LOW);
    digitalWrite(LMF,HIGH);
    digitalWrite(LMB,LOW);
    delay(600);
    digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, HIGH);
   digitalWrite (LMB, LOW);
   delay (500);
   digitalWrite (RMF, HIGH);
   digitalWrite (RMB, LOW);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, HIGH);
   delay (500);

digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, LOW);
   delay (400);
      digitalWrite(RMF, HIGH);
    digitalWrite (RMB, LOW);
    digitalWrite(LMF,HIGH);
    digitalWrite(LMB,LOW);
    delay(600);
    digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, HIGH);
   digitalWrite (LMB, LOW);
   delay (500);
   digitalWrite (RMF, HIGH);
   digitalWrite (RMB, LOW);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, HIGH);
   delay (500);
   digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, LOW);
   delay (400);
      digitalWrite(RMF, HIGH);
    digitalWrite (RMB, LOW);
    digitalWrite(LMF,HIGH);
    digitalWrite(LMB,LOW);
    delay(600);
    digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, HIGH);
   digitalWrite (LMB, LOW);
   delay (500);
   digitalWrite (RMF, HIGH);
   digitalWrite (RMB, LOW);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, HIGH);
   delay (500);
   digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, LOW);
   delay (400);
      digitalWrite(RMF, HIGH);
    digitalWrite (RMB, LOW);
    digitalWrite(LMF,HIGH);
    digitalWrite(LMB,LOW);
    delay(600);
    digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, HIGH);
   digitalWrite (LMB, LOW);
   delay (500);
   digitalWrite (RMF, HIGH);
   digitalWrite (RMB, LOW);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, HIGH);
   delay (500);
   digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, LOW);
   delay (400);
      digitalWrite(RMF, HIGH);
    digitalWrite (RMB, LOW);
    digitalWrite(LMF,HIGH);
    digitalWrite(LMB,LOW);
    delay(600);
    digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, HIGH);
   digitalWrite (LMB, LOW);
   delay (500);
   digitalWrite (RMF, HIGH);
   digitalWrite (RMB, LOW);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, HIGH);
   delay (500);
   digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, LOW);
   delay (400);
      digitalWrite(RMF, HIGH);
    digitalWrite (RMB, LOW);
    digitalWrite(LMF,HIGH);
    digitalWrite(LMB,LOW);
    delay(600);
    digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, HIGH);
   digitalWrite (LMB, LOW);
   delay (500);
   digitalWrite (RMF, HIGH);
   digitalWrite (RMB, LOW);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, HIGH);
   delay (500);
   digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, LOW);
   delay (400);
      digitalWrite(RMF, HIGH);
    digitalWrite (RMB, LOW);
    digitalWrite(LMF,HIGH);
    digitalWrite(LMB,LOW);
    delay(600);
    digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, HIGH);
   digitalWrite (LMB, LOW);
   delay (500);
   digitalWrite (RMF, HIGH);
   digitalWrite (RMB, LOW);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, HIGH);
   delay (500);
   digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, LOW);
   delay (400);
      digitalWrite(RMF, HIGH);
    digitalWrite (RMB, LOW);
    digitalWrite(LMF,HIGH);
    digitalWrite(LMB,LOW);
    delay(600);
    digitalWrite (RMF, LOW);
   digitalWrite (RMB, HIGH);
   digitalWrite (LMF, HIGH);
   digitalWrite (LMB, LOW);
   delay (500);
   digitalWrite (RMF, HIGH);
   digitalWrite (RMB, LOW);
   digitalWrite (LMF, LOW);
   digitalWrite (LMB, HIGH);
   delay (500);
 }
readvoice="";}}
