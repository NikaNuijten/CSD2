#include "sine.h"
#include <cmath>

// Constructor and destructor
Sine::Sine(double samplerate, double frequency) :
  Oscillator(samplerate, frequency){
}

Sine::~Sine(){
}


void Sine::calculate()
{
  // calculate sample
  sample = sin(phase * PI_2);
}
