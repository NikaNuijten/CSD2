#include "saw.h"
#include <cmath>

// Constructor and destructor
Saw::Saw(double samplerate, double frequency) :
  Oscillator(samplerate, frequency){
}

Saw::~Saw(){
}


void Saw::calculate()
{
  // calculate sample
  sample = 2*phase - 1;
}
