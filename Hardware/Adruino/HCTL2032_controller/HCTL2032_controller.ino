#include <ArduinoJson.h>
/**
 * Unless otherwise specified in individual files, all code is
 * Copyright (C) 2016 The Trustees of Columbia University in the City of New
 * York. This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by the
 * Free Software Foundation; either version 2 of the License, or (at your
 * option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
 * details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program. If not, see <http://www.gnu.org/licenses/>.
 **/

//D13: read select 1 (S1)
unsigned char readSel1H = 0B00100000;
unsigned char readSel1L = 0B11011111;

//D12 read reset (RR)
unsigned char readResetH = 0B00010000;
unsigned char readResetL = 0B11101111;

//D11 reset EC2 (R2)
unsigned char resetEC2H = 0B00001000;
unsigned char resetEC2L = 0B11110111;

//D10 reset EC1 (R1)
unsigned char resetEC1H = 0B00000100;
unsigned char resetEC1L = 0B11111011;

//D9 read select 2 (S2)
unsigned char readSel2H = 0B00000010;
unsigned char readSel2L = 0B11111101;

//D8 EC read select (CS)
unsigned char selECReadH = 0B00000001;
unsigned char selECReadL = 0B11111110;

//D2 and D3 lap reset pin read
unsigned char lapPins=0B00001100;
bool lapLow=false;

long prevPos;
long curPos;
long diffPos;
long diffT;
unsigned char *pos8BitArr = (unsigned char *)(&curPos);

unsigned long tMillis;
unsigned long pMillis;

StaticJsonDocument<200> jsonBuffer;
JsonObject message = jsonBuffer.to<JsonObject>();
JsonObject value = message.createNestedObject("position");

StaticJsonDocument<200> lapResetBuffer;
JsonObject lapResetMessage = lapResetBuffer.to<JsonObject>();
JsonObject lapRstVals = lapResetMessage.createNestedObject("lapReset");

void setup()
{
  Serial.begin(115200);
  pMillis = millis();
  value["dy"] = 0;
  value["dt"] = pMillis;
  message["millis"] = 0;
  lapRstVals["type"] = "IR 2 pin";
  lapResetMessage["millis"] = 0;

  //A0-A5 as digital input pins, for reading the data from
  //HCTL2032 bit 0-5 (D0-D5)
  DDRC = 0;  pos8BitArr[3] = B00111111 & PINC;
  
  //D6-D7 as digital input pins for reading bit 6-7 (D6, D7)
  //D2-D3 as digital input pints for reading lap reset
  DDRD = DDRD & B00110011;

  //control pins
  DDRB = DDRB | B00111111;

  //reset EC1
  PORTB = PORTB & resetEC1L;
  delayMicroseconds(10);
  PORTB = PORTB | resetEC1H;

  //reset EC2
  PORTB = PORTB & resetEC2L;
  delayMicroseconds(10);
  PORTB = PORTB | resetEC2H;

  //disable read latch
  PORTB = PORTB | readResetH;

  //select read channel, low for EC1, high for EC2
  PORTB = PORTB & selECReadL;
  //  PORTB=PORTB | selECReadH;
}

void loop()
{
  for (unsigned int i=0; i<60000; i++)
  {
    if((lapPins & PIND)==0)
    {
      if(!lapLow)
      {
        lapResetMessage["millis"] = millis();
        serializeJson(lapResetMessage, Serial);
        Serial.println();
        lapLow=true;
      }
      break;
    }
    lapLow=false;
  }

  
  //read MSB
  PORTB = PORTB & readResetL;
  PORTB = PORTB & readSel1L;
  PORTB = PORTB | readSel2H;
  tMillis = millis();
  delayMicroseconds(2);
  pos8BitArr[3] = B11000000 & PIND;
  pos8BitArr[3] = pos8BitArr[3] | B00111111 & PINC;

  //next byte
  PORTB = PORTB | readSel1H;
  delayMicroseconds(2);
  pos8BitArr[2] = B11000000 & PIND;
  pos8BitArr[2] = pos8BitArr[2] | B00111111 & PINC;
  
  //next byte
  PORTB = PORTB & readSel1L;
  PORTB = PORTB & readSel2L;
  delayMicroseconds(2);
  pos8BitArr[1] = B11000000 & PIND;
  pos8BitArr[1] = pos8BitArr[1] | B00111111 & PINC;

  //read LSB
  PORTB = PORTB | readSel1H;
  delayMicroseconds(2);
  pos8BitArr[0] = B11000000 & PIND;
  pos8BitArr[0] = pos8BitArr[0] | B00111111 & PINC;
  
  PORTB = PORTB | readResetH;
  delayMicroseconds(2);

  diffPos = curPos-prevPos;
  diffT = tMillis-pMillis;
  pMillis = tMillis;
  if(diffPos==0)
  {
    return;
  }

  value["dy"] = diffPos;
  value["dt"] = diffT;
  message["millis"] = tMillis;
  serializeJson(message, Serial);
  Serial.println();

  prevPos = curPos;
  pMillis = millis();
}
