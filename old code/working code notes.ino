#include <Adafruit_NeoPixel.h>

/*
HC-SR04 Ping distance sensor]
VCC to arduino 5v GND to arduino GND
Echo to Arduino pin 13 Trig to Arduino pin 12
Red POS to Arduino pin 11
Green POS to Arduino pin 10
560 ohm resistor to both LED NEG and GRD power rail
More info at: http://goo.gl/kJ8Gl
Original code improvements to the Ping sketch sourced from Trollmaker.com
Some code and wiring inspired by http://en.wikiversity.org/wiki/User:Dstaub/robotcar
*/
#define PIN 6
#define trigPin 10
#define echoPin 12
#define led 8
#define led2 9
int count , bright[15];
byte data[80];
long duration, currentdistance , lastdistantce , distchange;
boolean dataread = 0;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(15, PIN, NEO_GRB + NEO_KHZ800);


void setup() {
  Serial.begin (9600);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  count = 0;
}

void loop() {
 for(int i =0 ;i<15;i++){
  strip.setPixelColor(i, 0, 0, 0) ;
}

   count=0;
 
  while (Serial.available() > 0) { 
      data[count] = Serial.read();
     Serial.println (data[count] ,HEX); 
      count++;
  }    
  
int j = 0;   
   for(int i = 0;i < 45 ;i=i+3){
     strip.setPixelColor(j, data[i] , data[i+1]  , data[i+2]);
   j++;
    //Serial.println(j,DEC); 
  // Serial.println(i,DEC);
   }
   strip.show();
   delay(10);
   //Serial.println("l"); 
  // Serial.print(i,dec);
 
   
   // bright [(i*3)+1]=data[i]; 
    //strip.setPixelColor((i*3)+1, strip.Color((bright)/4, 0, (255-bright)/4)); 
   // }
  /* bright [0] = bright [1];
   bright [14] = bright [14]; 
   
   bright [2] = (bright [1]+bright [4])/2;
   bright [3]=bright [2];
   bright [5] = (bright [4]+bright [7])/2;
   bright [6]=bright [5];
    bright [8] = (bright [7]+bright [10])/2;
   bright [9]=bright [8];
    bright [11] = (bright [10]+bright [13])/2;
   bright [12]=bright [11];
     for(int i = 0;i < 15;i++){
    
    strip.setPixelColor(i, bright[i] , 0  , (255-bright[i])); 
    }
  
  
   //2 5 8 11 14
   //strip.setPixelColor( 1, data[0], 0, 0);
   //strip.setPixelColor( 4, data[1], 0, 0);
   //strip.setPixelColor( 7, data[2], 0, 0);
   //strip.setPixelColor( 10, data[3], 0, 0);
  // strip.setPixelColor( 13, data[4], 0, 0);
   
  // count++;
 // count = count & 0x0F;
  // strip.setPixelColor(count+1, 0, 0, 255);
   
   */
   
   
   
//strip.show();
   
  // delay(10);





 //   strip.show(); 

  
 //   for(uint16_t i=0; i<15; i++) {
 //     strip.setPixelColor(i, c);
  //    strip.show();
  //    delay(wait);
 // }
  
  

  
    //else{
    // Serial.read(); 
    //}
  //dataread = 1;
  //}
   //if(dataread){
   
   
  
 // strip.setPixelColor(1, strip.Color(1, 1, 1));
  
  //2
  // strip.setPixelColor(2, 0, 10, 0);
   //strip.setPixelColor(2, strip.Color( Serial.read(), 0));
   
   /*
   strip.setPixelColor(3, strip.Color(1, 1, 1));
   strip.setPixelColor(4, strip.Color(1, 1, 1));
   //5
   
    strip.setPixelColor(5, strip.Color(0, Serial.read(), 0));


   strip.setPixelColor(6, strip.Color(1, 1, 1));
   strip.setPixelColor(7, strip.Color(1, 1, 1));
   //8
    
    strip.setPixelColor(8, strip.Color(0, Serial.read(),0));
   
   
   strip.setPixelColor(9, strip.Color(1, 1, 1));
   strip.setPixelColor(10, strip.Color(1, 1, 1));
   //11
  
    strip.setPixelColor(11, strip.Color(0, Serial.read(), 0));
 
   
   strip.setPixelColor(12, strip.Color(1, 1, 1));
   strip.setPixelColor(13, strip.Color(1, 1, 1));
     //14
    
    strip.setPixelColor(14, strip.Color(0, Serial.read(), 0));
   
   
   strip.setPixelColor(15, strip.Color(1, 1, 1)); 
     */
  //strip.show();
  
  
  
  //delay(50); 
  //dataread = 0;
  

//}
  

    
 
    
    
 /*
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2); 
  digitalWrite(trigPin, HIGH);

  delayMicroseconds(10); // Added this line
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  currentdistance = (duration/2) / 29.1;
    distchange =  currentdistance - lastdistantce;
    
    if (distchange > 5){
     // Serial.print('u');
    }
    
    else if (distchange < -5){
      //Serial.print('d');
     }
     else {
    // Serial.print('n');
     }
lastdistantce = currentdistance;
  delay(5);
  
  */
}


//void colorWipe(uint32_t c, uint8_t wait) {
  //for(uint16_t i=0; i<strip.numPixels(); i++) {
  //    strip.setPixelColor(i, c);
  //    strip.show();
   //   delay(wait);
 // }
//}
