int brightness = 0;
int led;

void setup()
{
    pinMode(13, OUTPUT);
    pinMode(12, OUTPUT);
    pinMode(11, OUTPUT);
    pinMode(10, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(8, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(5, OUTPUT);
}

void loop()
{
    for (led = 5; led <= 13; led++)
    {
        for (brightness = 0; brightness <= 255; brightness++)
        {
            analogWrite(led, brightness);
            delay(2);
        }
    }
    for (led = 13; led >= 5; led--)
    {
        for (brightness = 255; brightness >= 0; brightness--)
        {
            analogWrite(led, brightness);
            delay(2);
        }
    }
}