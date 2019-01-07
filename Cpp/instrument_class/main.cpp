#include "Instrument.h"

int main() {
  //create an Instrument object
  Instrument myInstrument;

  //set the sound field
  myInstrument.sound = "Biem";

  //call the makeSound method 'make a sound into the console'
  myInstrument.makeSound();

  //exit the programm
  return 0;
}
