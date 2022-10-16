# Voice_control_Car

Presenting before you 'The R Car' : A voice control car.

## Brief description :

It is made with the help of Arduino UNO, L298N Motor driver and HC05 Bluetooth module, Two BO motor, Two 9V battery, Two wheels, One 360 degree rotation wheel, and some basis material like jumper wires etc.

## Components required

### Arduino UNO
### L298N Motor driver
### HC05 Bluetooth module
### Two BO motor
### Two 9V battery
### Two wheels
### One 360 degree rotation wheel
### Jumper wires

## Circuit Diagram
![circuit diagram_2 wheels](https://user-images.githubusercontent.com/78155393/194743301-94d248c1-c02f-446e-b47a-734953dcc086.jpg)


## Working
We connect the Bluetooth module with the mobile app. Once done, the commands which we give through the mobile get sent to the Arduino via the module. We accept character by character from the serial buffer sent by the app and combine them to form a string.

We then compare it to the command. If it matches, the command is carried out. For example, when the string we receive is "Right", the bot turns right.

## Demonstration Video details :

👉🏻Car Demonstration Video 1 - Working with 'Right', 'Left', 'Forward', 'Backward' command.

👉🏻Car Demonstration Video 2 - Working with a special and unique 'Garba Dance' command.
![image](https://user-images.githubusercontent.com/78155393/194743005-a08810d3-9684-4ff2-a257-b0faf57495f9.png)
![Car Picture 1](https://user-images.githubusercontent.com/78155393/149631528-34348ad0-fccc-46ad-8102-651ba5070fb4.jpg)
![Car Picture 2](https://user-images.githubusercontent.com/78155393/149631977-ceb2704e-de2d-40d6-82d9-fc3c6f23e3d6.jpg)


