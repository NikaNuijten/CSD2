#include "square.h"
#include <cmath>

// Constructor and destructor
Square::Square(double samplerate, double frequency) :
  Oscillator(samplerate, frequency)
{
  //std::cout << "\nInside Square::oscillator (double frequency, double phase)"
  //  << "\nfrequency: " << frequency
  //  << "\nphase: " << phase;
}

Square::~Square()
{
  //std::cout << "\nInside Square::~Square";
}


void Square::calculate()
{
  // calculate sample
  if (phase < 0.5) sample = -1;
  if (phase >= 0.5) sample = 1;

}
