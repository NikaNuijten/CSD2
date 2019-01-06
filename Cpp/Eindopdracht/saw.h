#ifndef _SAW_H_
#define _SAW_H_
#include <iostream>
#include "math.h"
#include "oscillator.h"

class Saw : public Oscillator
{
public:
  //Constructor and destructor
  Saw(double samplerate, double frequency);
  ~Saw();

  // ovverride calculate method
  void calculate();


};

#endif
