#include "oscillator.h"


// Constructor and destructor
Oscillator::Oscillator(double samplerate, double frequency) :
  samplerate(samplerate), frequency(frequency), phase(0), sample(0){
}

Oscillator::~Oscillator(){
}

double Oscillator::getSample() { return sample*amplitude; }

void Oscillator::tick()
{
  // increase phase
  phase += frequency / samplerate;
  // wrap phase from 0 to 1
  if(phase >= 1) phase = phase - 1;

  // calculate new sample
  calculate();
}

void Oscillator::calculate()
{
  std::cout << ".";
}


void Oscillator::setFrequency(double frequency)
{
  if(frequency > 0 && frequency < 0.5 * samplerate)
  this->frequency = frequency;
}

double Oscillator::getFrequency()
{
  return frequency;
}

void Oscillator::setAmplitude(double amplitude)
{
  this->amplitude = amplitude;
}

double Oscillator::getAmplitude()
{
  return amplitude;
}
