#include "saw.h"
#include <cmath>

// Constructor and destructor
Saw::Saw(double samplerate, double frequency) :
  Oscillator(samplerate, frequency)
{
  //std::cout << "\nInside Saw::oscillator (double frequency, double phase)"
  //  << "\nfrequency: " << frequency
  //  << "\nphase: " << phase;
}

Saw::~Saw()
{
  //std::cout << "\nInside Saw::~Saw";
}


void Saw::calculate()
{
  // calculate sample
  sample = 2*phase - 1;
}
