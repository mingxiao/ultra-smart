#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_TSL2561.h>

/*
  This is pretty much the sensorapi.pde except without
  all those print statements, because we just want to print
  the lux reading to our receiver (the python module)
*/

Adafruit_TSL2561 tsl = Adafruit_TSL2561(TSL2561_ADDR_FLOAT,12345);

void configureSensor(void){
  tsl.enableAutoGain(true);
  tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);
}

void setup(){
  Serial.begin(9600);
  if(!tsl.begin()){
    Serial.println("no tsl2561 sensor detected");
    while(1);
  }
  configureSensor();
}

void loop(){
  delay(300);
  sensors_event_t event;
  tsl.getEvent(&event);
  if(event.light){
    //Serial.flush();
    Serial.println(event.light);
    //Serial.flush();
  }
  else{
    Serial.println("Serial overload");
  }
}
