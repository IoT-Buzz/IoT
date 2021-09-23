void setup()
{
  pinMode(13, OUTPUT);
}

void loop()
{
  digitalWrite(13, HIGH);
  delay(10); // Wait for 1000 millisecond(s)
  digitalWrite(13, LOW);
}