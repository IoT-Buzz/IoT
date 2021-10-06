#include <Keypad.h>
#include <Adafruit_NeoPixel.h>

#define passwordLength 4
#define pin_piezo 4
#define pin_pir 3
#define pin_NeoPixel 13

// Alarm related variables
volatile bool alarmCounterTriggered = false;
const int timeWindow = 10;
volatile static int alarmTimer = 0;

//counter and compare values Timer1 = 16bit
const uint16_t t1_load = 0;
const uint16_t t1_comp = 62500;

//Keypad related variables
char inputPassword[passwordLength + 1]; //Password_Length+1 due to terminating zero \0
char masterPasswort[passwordLength + 1] = "123A";
byte dataCount = 0, masterCount = 0;

const byte ROWS = 4;
const byte COLS = 4;

char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {12, 11, 10, 9};
byte colPins[COLS] = {8, 7, 6, 5};

//Initialization of objects
Keypad myKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);
Adafruit_NeoPixel pixel = Adafruit_NeoPixel(1, pin_NeoPixel, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  DDRD |= (1 << pin_piezo);

  //setup PIR pin
  DDRD &= ~(1 << pin_pir); //Pinmode Input
  PORTD &= ~(1 << pin_pir); //Pull-Down

  /* ------------------------------
      Setup Externe Interrupt
     ------------------------------*/
  //setup extern Interrupt interrupt: Rising edge of INT1 gennerates Interrupt
  EICRA |= (1 << ISC11);
  EICRA |= (1 << ISC10);
  EIMSK = 0; //Reset Register
  EIMSK |= (1 << INT1); //Enable Interrupts for INT1

  /* -------------------------------
     Setup Software Interrupt
     -------------------------------*/
  //Reset Timer1 Control Reg A
  TCCR1A = 0;

  //Set CTC mode (automatic reload of timer
  TCCR1B &= ~(1 << WGM13); // ensure that cleared
  TCCR1B |= (1 << WGM12);

  //Set Prescaler of 256
  TCCR1B |= (1 << CS12);
  TCCR1B &= ~(1 << CS11);
  TCCR1B &= ~(1 << CS10);

  // Reset Timer and Compare Value
  TCNT1 = t1_load;
  OCR1A = t1_comp;

  pixel.begin();
  SetPixel(0, 255, 0); // green
}

void loop()
{
  char keyInput = myKeypad.getKey();
  if (keyInput != NO_KEY)  {
    Serial.println(keyInput);
    inputPassword[dataCount] = keyInput;
    dataCount++;
  }

  if (dataCount == passwordLength) {
    if (!strcmp(inputPassword, masterPasswort)) {
      Serial.println("Correct password!");
      DeactivateAlarm();
    }
    else
      Serial.println("Incorrect password!");

    ClearData();
  }
}

//external Interrupt Service Routine
ISR(INT1_vect) {
  SetPixel(255, 255, 0); // yellow

  Serial.println("Alarm timer (re)started!");

  if (!alarmCounterTriggered)  {
    //activate Timer
    TIMSK1 |= (1 << OCIE1A);
    alarmCounterTriggered = true;
  }

  alarmTimer = timeWindow;
  Serial.print("Alarm timer: ");
  Serial.println(alarmTimer);
}

//Timer Interrupt Service Routine
ISR(TIMER1_COMPA_vect) {
  alarmTimer--;
  Serial.print("Alarm timer: ");
  Serial.println(alarmTimer);

  //activate Alarm
  if (alarmTimer <= 0)
    ActivateAlarm();
}

void SetPixel(int redValue, int greenValue, int blueValue) {
  pixel.setPixelColor(0, pixel.Color(redValue, greenValue, blueValue));
  pixel.show();
}

void ActivateAlarm() {
  TIMSK1 &= ~(1 << OCIE1A); //deactivate Timer
  SetPixel(255, 0, 0); // LED Red
  tone(pin_piezo, 1000);
  Serial.println("Alarm activated!");
}

void DeactivateAlarm() {
  TIMSK1 &= ~(1 << OCIE1A); //deactivate Timer
  SetPixel(0, 255, 0); // green
  noTone(pin_piezo);
  alarmCounterTriggered = false;
  Serial.println("Alarm deactivated!");
}

void ClearData() {
  while (dataCount != 0) {
    inputPassword[dataCount--] = 0;
  }
  return;
}
