#ifndef _SQUARE_H_
#define _SQUARE_H_
#include <iostream>
#include "math.h"
#include "oscillator.h"

class Square : public Oscillator
{
public:
  //Constructor and destructor
  Square(double samplerate, double frequency);
  ~Square();

  // ovverride calculate method
  void calculate();


};

#endif
