//Define IR Sensors
int IRSensor1 = 7;
int IRSensor2 = 9;
int total = 5;


void setup() 
{
  Serial.begin(9600);
  Serial.println("-------Smart Car Parking System-------");
  pinMode (IRSensor1, INPUT); // sensor pin INPUT
  pinMode (IRSensor2, INPUT); // sensor pin INPUT
}

void loop()
{
  int statusSensor1 = digitalRead (IRSensor1);
  int statusSensor2 = digitalRead (IRSensor2);
  
  if (statusSensor1 == 0){
    if(total ==0){
      Serial.println("No more Car spaces Available");
      Serial.println("Please Do not enter");
      Serial.println("-------------------------------------");
      delay(5000);
      }
    else{
      total = total - 1;
    Serial.println("Car Entering");
    Serial.println("Please Enter within 5 second");
    Serial.println("Total Car Spaces left");
    Serial.println(total);
    Serial.println("-------------------------------------");
    delay(5000);
      }
  }

  if (statusSensor2 == 0){
    if(total < 5){
      total = total + 1;      
      }
    Serial.println("Car Exiting");
    Serial.println("Please Exit within 5 second");
    Serial.println("Total Car Spaces left");
    Serial.println(total);
    Serial.println("-------------------------------------");
    delay(5000);
  }
}
