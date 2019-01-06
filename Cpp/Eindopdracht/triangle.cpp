#include "triangle.h"
#include <cmath>

// Constructor and destructor
Triangle::Triangle(double samplerate, double frequency) :
  Oscillator(samplerate, frequency)
{
  // TODO - use setFrequency and phase instead, to prevent outrange values
  std::cout << "\nInside Triangle::oscillator (double frequency, double phase)"
    << "\nfrequency: " << frequency
    << "\nphase: " << phase;
}

Triangle::~Triangle()
{
  std::cout << "\nInside Triangle::~Triangle";
}


void Triangle::calculate()
{
  // calculate sample
  // NOTE: sin() method is not the most efficient way to calculate the sine value
  // TODO: Bedenken hoe een triangle werkt
 sample = 2*phase - 1;

}
