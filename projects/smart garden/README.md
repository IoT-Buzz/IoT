# Automated plant watering system
## About
It's a simple project which turns on the water pump if moisture level of the soil drops below a certain level.
## Components required
* Arduino/NodeMCU/Any other micro controller. 
* Analog soil moisture sensor.
* Water pump/Solenoid valve.
## Working
* The main loop takes in value of soil moisture and compares it with pre-defined threshold set.
* If the moisture value goess below this threshold, then it'll start the pump. 
* setup loop has serial port where the value is to be printed and also defines pin mode for both of the components.
* Initial moisture value has been initialized to 0.0
* A fail safe is added in case of sensor failure.