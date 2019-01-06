#ifndef _MELODYGENERATOR_H_
#define _MELODYGENERATOR_H_

#include <random>
#include <cmath>
#include <iostream>
#include <time.h>

class MelodyGenerator{
public:
  MelodyGenerator();
  int rand_between(int min, int max);
};

#endif
