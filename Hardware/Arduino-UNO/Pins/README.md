# Pin Details
There are several I/O digital and analog pins placed on the board which operates at 5V. These pins come with standard operating ratings ranging between 20mA to 40mA. Internal pull-up resistors are used in the board that limits the current exceeding the given operating conditions. However, too much increase in current makes these resisters useless and damages the device.

<img src="https://github.com/IoT-Buzz/IoT/blob/main/Hardware/pictures/arduino-uno-s1.png" width=700 height=600>

* LED = Arduino Uno comes with a built-in LED which is connected through pin 13. Providing HIGH value to the pin will turn it ON and LOW will turn it OFF.
* Vin= It is the input voltage provided to the Arduino Board. It is different than 5 V supplied through a USB port. This pin is used to supply voltage. If a voltage is provided through a power jack, it can be accessed through this pin.
* 5V= This board comes with the ability to provide voltage regulation. 5V pin is used to provide output regulated voltage. The board is powered up using three ways i.e. USB, Vin pin of the board or DC power jack.
* GND= These are ground pins. More than one ground pins are provided on the board which can be used as per requirement.
* Reset= This pin is incorporated on the board which resets the program running on the board. Instead of physical reset on the board, IDE comes with a feature of resetting the board through programming.
* IOREF= This pin is very useful for providing voltage reference to the board. A shield is used to read the voltage across this pin which then selects the proper power source.
* PWM=PWM is provided by 3,5,6,9,10, 11pins. These pins are configured to provided 8-bit output PWM.
* SPI=It is known as Serial Peripheral Interface. Four pins 10(SS), 11(MOSI), 12(MISO), 13(SCK) provide SPI communication with the help of the SPI library.
* AREF= It is called Analog Reference. This pin is used for providing a reference voltage to the analog inputs.
* TWI= It is called Two-wire Interface. TWI communication is accessed through Wire Library. A4 and A5 pins are used for this purpose.
* Serial Communication= Serial communication is carried out through two pins called Pin 0 (Rx) and Pin 1 (Tx).
* Rx pin= is used to receive data while Tx pin is used to transmit data.
* External Interrupts= Pin 2 and 3 are used for providing external interrupts. An interrupt is called by providing LOW or changing value.
