# What is a MICROCONTROLLER ?
<h5>
  <img src="https://github.com/IoT-Buzz/IoT/blob/main/Hardware/pictures/microcontroller%20.png">

  
* A microcontroller is an integrated circuits ( IC ) that can be programmed to
perform a set of functions to control a collection of electronic devices.
* A self-contained system in which a processor, support, memory and
input/output ( I/O ) are all contained in a single package.

* The most important thing is that it is programmable . So one can program it
according to the requirement and produce desired outputs
</h5>

## There are 2 microcontrollers in Arduino-UNO (an Atmega328p and a ATmega16U2).
Atmega328P is a microcontroller which is the heart :heart: of Arduino Uno, where the Atmega16U2 is the USB to serial convertor for arduino communicated with computer.

## Atmega16U2
The Atmega16U2 acts as a USB to serial converter. The Arduino bootloader in the Atmega328P allows the chip to be programmer via UART(serial port). Older computer systems had serial ports which could have been connected directly to the Atmega328P. But USB is ubiquitous these days and a USB to serial converter is needed to mimic the serial port over USB. Usually FTDI chips are used, but the arduino guys decided to go with Atmega16U2 for some reason. The best part is that you can also program and create your own applications on the Atmega16U2 if you have an In-circuit Serial Programmer.

## Atmega328P
ATmega328P is a high performance yet low power consumption 8-bit AVR microcontroller

### Features and Parametrics
#### Features:

* In system self-programmable flash program memory
* Programming Lock for software security
### Peripheral features
* Two 8-bit Timer/Counter with separate prescaler, compare mode.
* One 16-bit Timer/Counter with separate prescaler, compare mode, and capture mode
* Temperature measurement
* Programmable serial USART and watchdog timer with separate on-chip oscillator


  
