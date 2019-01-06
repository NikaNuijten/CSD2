#include "square.h"
#include <cmath>

// Constructor and destructor
Square::Square(double samplerate, double frequency) :
  Oscillator(samplerate, frequency){
}

Square::~Square(){
}


void Square::calculate()
{
  // calculate sample
  if (phase < 0.5) sample = -1;
  if (phase >= 0.5) sample = 1;

}
