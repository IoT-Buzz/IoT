#include <SPI.h>
#include <Wire.h>
#include <ESP8266WiFi.h>
#define sensor_pin A0    //soil moisture sensor data pin
#define valve_pin 5     //valve data pin
#include "ThingSpeak.h"
//#define OLED_RESET -1       // Reset pin # (or -1 if sharing Arduino reset pin)

unsigned long myChannelNumber = <your_own_channel_id>; //plant1 channel id. Replace it with your own channel id. 
                                                      //It will be a 7 digit integer.

const char *apiKey = <your_own_API_key>; // 17 digit string API key for plant1. Replace this with your own api key


const char *ssid = "your_own_wifi_ssid";     // replace with your wifi ssid and wpa2 key 
const char *pass = "your_own_wifi_password";
const char* server = "api.thingspeak.com";
 
WiFiClient client;
 
 
void setup() {
  Serial.begin(115200);
  delay(10);
  pinMode(sensor_pin, INPUT);
  pinMode(valve_pin, OUTPUT); 

  WiFi.mode(WIFI_STA);

  ThingSpeak.begin(client);
 
}
void loop() {

  //int moisture_percentage;
  float moisture;


  moisture = analogRead(sensor_pin);       //getting soil moisture
  moisture = (moisture/1023)*100; 
  //moisture_percentage = ( 100.00 - ( (analogRead(sensor_pin)/1023.00) * 100.00 ) );

    Serial.print("Soil Moisture(in Percentage) = ");
    Serial.print(moisture);
    Serial.println("%");

   if(moisture <= 40)            //condition for motor to start
  {
    digitalWrite(valve_pin, HIGH);     //condition for motor to start
    Serial.println("Valve open");
  }
  else
  {
    digitalWrite(valve_pin, LOW);      //condition for motor to stop
    Serial.println("Valve closed");
  }
  

    if (WiFi.status() != WL_CONNECTED) {
        Serial.print("Attempting to connect to SSID: ");
        Serial.println(ssid);
        while (WiFi.status() != WL_CONNECTED) {
          WiFi.begin(ssid, pass); // Connect to WPA/WPA2 network. Change this line if using open or WEP network
          Serial.print(".");
          delay(2000);
        }
        Serial.println("\nConnected.");
      } 

          // Write value to Field 1 of a ThingSpeak Channel
      int httpCode = ThingSpeak.writeField(myChannelNumber, 1, moisture, apiKey);
      //int httpCode1 = ThingSpeak.writeField(myChannelNumber, 2, valve_status, apiKey);
      
      if (httpCode == 200) {
        Serial.println("Channel write successful.");
      }
      else {
        Serial.println("Problem writing to channel. HTTP error code " + String(httpCode));
      }
    
      // Wait 20 seconds to update the channel again
      delay(20000);
    

}