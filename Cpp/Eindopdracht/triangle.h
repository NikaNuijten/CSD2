#ifndef _TRIANGLE_H_
#define _TRIANGLE_H_
#include <iostream>
#include "math.h"
#include "oscillator.h"

class Triangle : public Oscillator
{
public:
  //Constructor and destructor
  Triangle(double samplerate, double frequency);
  ~Triangle();

  // ovverride calculate method
  void calculate();


};

#endif
