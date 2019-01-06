#include "sine.h"
#include <cmath>

// Constructor and destructor
Sine::Sine(double samplerate, double frequency) :
  Oscillator(samplerate, frequency)
{
  //std::cout << "\nInside Sine::oscillator (double frequency, double phase)"
  //  << "\nfrequency: " << frequency
  //  << "\nphase: " << phase;
}

Sine::~Sine()
{
  //std::cout << "\nInside Sine::~Sine";
}


void Sine::calculate()
{
  // calculate sample
  sample = sin(phase * PI_2);
}
