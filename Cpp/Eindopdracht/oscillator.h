#ifndef _OSCILLATOR_H_
#define _OSCILLATOR_H_
#include <iostream>
#include "math.h"

#define PI_2 6.28318530717959

class Oscillator
{
public:
  //Constructor and destructor
  Oscillator(double samplerate, double frequency);
  Oscillator();
  ~Oscillator();

  //return the current sample
  double getSample();
  // go to next sample
  void tick();
  //getters and setters
  void setFrequency(double frequency);
  double getFrequency();

  void setAmplitude(double amplitude);
  double getAmplitude();

protected:
  virtual void calculate();
  double samplerate;
  double frequency;
  double phase;
  double sample;
  double amplitude;
};

#endif
