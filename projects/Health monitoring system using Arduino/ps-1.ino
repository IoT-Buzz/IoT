/*LIBRARIES*/
#define USE_ARDUINO_INTERRUPTS false              
#include <PulseSensorPlayground.h>                //Pulse Sensor library
#include <TinyGPS++.h>                            //GPS library
#include <SoftwareSerial.h>                       //create a sw serial communication
#include "MAX30100_PulseOximeter.h"

/*VARIABLES*/
char buf[70];

/*SpO2 Sensor */
PulseOximeter PulOx;
float spo2;

/*LM35_Temperature_sensor*/
const int LM35_sensor_output = A0;                
float temp;                                       
float vout;                                       
int contor_apelare = 0;

/*Pulse_sensor_Variables*/
int Beat_per_mins = 0;                         
const int OUTPUT_TYPE = SERIAL_PLOTTER;           //the format of our pulse sensor output, chosen by us to being a serial monitor output0

const int Pulse_sensor_output = A1;              
const int treshhold = 550;                        //the threshold used to helping us reading the pulse waves (heart beat moments)

byte samplesUntilReport;                          //the number of samples remaining to read until we want to report a sample over the serial connection.
const byte SAMPLES_PER_SERIAL_SAMPLE = 10;        //after 10 samples measurment we will calculate the Pulse

/*GPS_Variables*/

double lat = 0;                             
double lon = 0;                             
int yrs,mon,days;                          
int hrs,mins,sec;                        
static const uint32_t GPSBaud = 9600;             
static const int RXPin = 4, TXPin = 3;            
SoftwareSerial gps_bus(RXPin, TXPin);     
        
/*HC-12_Variables*/
SoftwareSerial HC12(6, 7);         // HC-12 TX Pin, HC-12 RX Pin

/*FUNCTION OBJECT FOR DEDICATED LIBRARY*/

PulseSensorPlayground pulseSensor;                
TinyGPSPlus GPS;                                  

/*COMMUNICATION SETUP AND OTHERS SETUP*/
void setup()
{
 pinMode(LM35_sensor_output,INPUT);              
 Serial.begin(9600);                             //sets the data rate in bps (baud) for serial monitor communication
 HC12.begin(9600);                               // Serial port to HC12        
 gps_bus.begin(GPSBaud);                         //sets the data rate in bps (baud) for sw serial communication with GPS  
 
 // Configure the PulseSensor manager.
 pulseSensor.analogInput(Pulse_sensor_output);   
 pulseSensor.setSerial(Serial);                  
 pulseSensor.setOutputType(OUTPUT_TYPE);         
 pulseSensor.setThreshold(treshhold);            


 samplesUntilReport = SAMPLES_PER_SERIAL_SAMPLE; // Skip the first SAMPLES_PER_SERIAL_SAMPLE in the loop().

 
 if (!pulseSensor.begin())                       
 {
   Serial.print("Pulse sensor start reading the pulse");
 }
}

/*MAIN FUNCTION*/
void loop()
{
 
 if(contor_apelare == 25)
 {
   vout = analogRead(LM35_sensor_output);
   vout = analogRead(LM35_sensor_output);
   vout = vout * 5 / 1023;
   temp = vout / 0.01;
   
   PulOx.update();
   /* We store the Spo2 value obatined form the MAX30100 in the spo2 variable */    
   spo2 = PulOx.getSpO2();
   contor_apelare = 0;
 }


 if (pulseSensor.sawNewSample())
 {
   contor_apelare++;
   if (--samplesUntilReport == (byte) 0)
   {
     
     samplesUntilReport = SAMPLES_PER_SERIAL_SAMPLE;

     if (pulseSensor.sawStartOfBeat())
     {
       
       Beat_per_mins = pulseSensor.getBeatsPerMinute();
       Beat_per_mins = pulseSensor.getBeatsPerMinute();
     }
     
   }

    if (gps_bus.available() > 0)               // Check for gps data on the serial communication
     {
       GPS.encode(gps_bus.read());                 
       if (GPS.location.isUpdated())
       {
        
/*LOCATION*/
         // Latitude in degrees (double)
         lat = GPS.location.lat();
         char str_lat[10];
         dtostrf(lat,4,6,str_lat);
         sprintf(buf, "Latitude = %s \r", str_lat);
         HC12.write(buf);
         /*Serial.print("Latitude = ");
         Serial.print(lat, 6);*/
             
         // lon in degrees (double)
         lon = GPS.location.lng();
         char str_lon[10];
         dtostrf(lon,4,6,str_lon);
         sprintf(buf, " lon = %s\r\n", str_lon);
         HC12.write(buf);
         /*Serial.print(" lon = ");
         Serial.println(lon, 6);*/
         
 /*DATE*/
         // Year (2000+) 
         yrs = GPS.date.year();
         char str_year[10];
         dtostrf(yrs,4,0,str_year);
         sprintf(buf, "Year:%s", str_year);
         HC12.write(buf);
         /*Serial.print("Year = ");
         Serial.print(yrs);*/
         
         // Month (1-12)
        mon = GPS.date.month();
         char str_month[10];
         dtostrf(mon,4,0,str_month);
         sprintf(buf, " Month:%s\r", str_month);
         HC12.write(buf);
         /*Serial.print("  Month = ");
         Serial.print(mounth);*/
         
         // Day (1-31)
         days = GPS.date.day();
         char str_day[10];
         dtostrf(days,4,0,str_day);
         sprintf(buf, " Day:%s\r\n", str_day);
         HC12.write(buf);
         /*Serial.print("  Day = ");
         Serial.println(days);*/
         
 /*TIME/*/
         // Hour (0-23) 
         hrs = GPS.time.hour();
         hrs = hrs + 5;
         char str_hour[10];
         dtostrf(hrs,4,0,str_hour);
         sprintf(buf, "Hour:%s", str_hour);
         HC12.write(buf);
         //Serial.print("Hour = ");
         //Serial.print(hrs);
         
         // Minute (0-59) 
         mins = GPS.time.minute();
         char str_min[10];
         dtostrf(mins,4,0,str_min);
         sprintf(buf, " mins:%s", str_min);
         HC12.write(buf);
         //Serial.print("  Minute = ");
         //Serial.print(mins);
         
         // Second (0-59) 
         sec = GPS.time.second();
         char str_sec[10];
         dtostrf(sec,4,0,str_sec);
         sprintf(buf, " sec:%s\r\n", str_sec);
         HC12.write(buf);
         //Serial.print("  Second = ");
         //Serial.println(sec);

/*Pulse*/
         char str_bpm[10];
         dtostrf(Beat_per_mins,4,2,str_bpm);
         sprintf(buf, "BPM: %s \r\n", str_bpm);
         HC12.write(buf);
         /*Serial.print("BPM: ");
         Serial.println(Beat_per_mins);*/

/*Temperature*/
         char str_temp[10];
         dtostrf(temp,4,2,str_temp);
         sprintf(buf, "Temperature = %s °C\r\n\n", str_temp);
         HC12.write(buf);
         /*Serial.print("Temperature = ");
         Serial.print(temp);
         Serial.println(" °C");
         Serial.println(" ");*/

         

/*Spo2*/
         char str_spo2[10];
         dtostrf(spo2,4,2,str_spo2);
         sprintf(buf, "Spo2 = %s %\r\n\n", str_spo2);
         HC12.write(buf);
         /*Serial.print("SPO2 = ");
         Serial.print(spo2);
         Serial.println(" %");
         Serial.println(" ");*/
         
         Serial.println("Sent Soldier's Data.");

              
     }
     
    }

 }    
 
}
