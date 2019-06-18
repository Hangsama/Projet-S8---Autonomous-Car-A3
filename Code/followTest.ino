//int pinMC = 5;  //pin pour commander le moteur continue
int pinMS = 6;  //pin pour commander le servo moteur
int command = 0;  // initial command

void setup() {
  //pinMode(pinMC, OUTPUT);
  pinMode(pinMS, OUTPUT);  
  Serial.begin(115200);
  //Mode 5: for changing to approximately 16.4ms  e.g. 16.4ms/255*24 = 1.6ms  占空比
  //Reconfigurer le timer 0 (changer la fréquence sur les PWM en PIN5 , 6. Par contre il va changer le temps de delay() )
  //Every delay(60) is approximately 1s after the reconfiguration.
  TCCR0B = TCCR0B & 0xF8 |0x05; 
  reset();
}

void loop() {
     if(Serial.available() >= 0){
     command = Serial.read();
     //if(command == 'w'){forward();}
     if(command == 'a'){analogWrite(pinMS,25);} //left
     if(command == 'd'){analogWrite(pinMS,18);} //right
     if(command == 'm'){analogWrite(pinMS,21);} //mid
   }
}

//PWM pour démarrer les deux moteurs
void reset(){
  analogWrite(pinMS, 21);   //mid
  //analogWrite(pinMC, 24);   //16 pour 1ms, 32 pour 2ms, 24 pour 1.5ms & demarrer 
  //delay(300);
}

void forward(){
  //analogWrite(pinMC, 26);
  //analogWrite(pinMC, map(104, 0, 1021, 0, 255));
  //analogWrite(pinMC, map(260000, 0, 2550000, 0, 255));
  //analogWrite(pinMC, map(240000, 0, 2550000, 0, 255));
  
}

void stopp(){
  //analogWrite(pinMC,0); //arreter
}
