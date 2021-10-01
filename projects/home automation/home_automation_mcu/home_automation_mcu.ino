//code edited by rahul guglani


#include <ESP8266WiFi.h>

WiFiClient client;
WiFiServer server(80);

#define light1 16          //D0
#define tubeLight 5       //D1
#define nightLight 4      //D2
#define fan 2            //D4

#define light1Switch 14   //D5
#define tubeLightSwitch 12  //D6
#define nightLightSwitch 13 //D7
#define fanSwitch 15       //D8


#define tdel 500           //500ms button change is checked

const char* ssid = "NodeMcu";         // Enter SSID here
const char* password = "password";   //Enter Password here

unsigned long prevMili =0;
bool light1BtnStateP,tubeLightBtnStateP,nightLightBtnStateP,fanBtnStateP;
bool light1BtnStateC,tubeLightBtnStateC,nightLightBtnStateC,fanBtnStateC;
bool light1State, tubeLightState , nightLightState, fanState;


void setup() 
{
  // put your setup code here, to run once:
  Serial.begin(9600);
 
  Serial.println("NodeMCU Started!");
  WiFi.softAP(ssid, password);
  delay(100);
  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);
  server.begin();
  delay(1000);
  
  pinMode(light1, OUTPUT);
  pinMode(tubeLight, OUTPUT);
  pinMode(nightLight, OUTPUT);
  pinMode(fan, OUTPUT);
  
  pinMode(light1Switch, INPUT);
  pinMode(tubeLightSwitch, INPUT);
  pinMode(nightLightSwitch, INPUT);
  pinMode(fanSwitch, INPUT);
  
  light1BtnStateP = digitalRead(light1Switch);
  tubeLightBtnStateP = digitalRead(tubeLightSwitch);
  tubeLightBtnStateP = digitalRead(tubeLightSwitch);
  fanBtnStateP = digitalRead(fanSwitch);
  
  light1State = light1BtnStateP;
  tubeLightState = tubeLightBtnStateP;
  nightLightState = nightLightBtnStateP;
  fanState = fanBtnStateP;

  digitalWrite(light1,light1State);
  digitalWrite(tubeLight,tubeLightState);
  digitalWrite(nightLight,nightLightState);
  digitalWrite(fan,fanState);
  
  
}



void chkBtnChange()
{
  light1BtnStateC = digitalRead(light1Switch);
  tubeLightBtnStateC = digitalRead(tubeLightSwitch);
  nightLightBtnStateC = digitalRead(nightLightSwitch);
  fanBtnStateC = digitalRead(fanSwitch);
  
  if(light1BtnStateC!=light1BtnStateP)
  {
    light1State = !light1State;   
  }
  if(tubeLightBtnStateC!=tubeLightBtnStateP)
  {
    tubeLightState = !tubeLightState;   
  }
  if(nightLightBtnStateC!=nightLightBtnStateP)
  {
    nightLightState = !nightLightState;   
  }
  if(fanBtnStateC!=fanBtnStateP)
  {
    fanState = !fanState;   
  }
    
    light1BtnStateP=light1BtnStateC;
    tubeLightBtnStateP=tubeLightBtnStateC;
    nightLightBtnStateP=nightLightBtnStateC;
    fanBtnStateP=fanBtnStateC;

}




void loop() 
{
  unsigned long currMili = millis();
  
  if(currMili - prevMili >= tdel )
  {
    chkBtnChange();
    prevMili = millis();
  }
  
  digitalWrite(light1,light1State);
  digitalWrite(tubeLight,tubeLightState);
  digitalWrite(nightLight,nightLightState);
  digitalWrite(fan,fanState);

    
  client = server.available();  //Gets a client that is connected to the server and has data available for reading.    
  if (client == 1)
  {  
    String request =  client.readStringUntil('\n');
    Serial.println(request);
     
    request.trim();
    
    
    if(request == "GET /led1on HTTP/1.1")
    {
      light1State = HIGH;
    }
    else if(request == "GET /led1off HTTP/1.1")
    {
      light1State = LOW;
    }
    else if(request == "GET /tubeLighton HTTP/1.1")
    {
      tubeLightState = HIGH;
    }
    else if(request == "GET /tubeLightoff HTTP/1.1")
    {
      tubeLightState= LOW;
    }
    else if(request == "GET /nightLighton HTTP/1.1")
    {
      nightLightState= HIGH;
    }
    else if(request == "GET /nightLightoff HTTP/1.1")
    {
      nightLightState= LOW;
    }
    else if(request == "GET /fanon HTTP/1.1")
    {
      fanState = HIGH;
    }
    else if(request == "GET /fanoff HTTP/1.1")
    {
      fanState = LOW;
    }
    
  }
}
