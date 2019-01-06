#ifndef _SYNTH1_H_
#define _SYNTH1_H_
#include "oscillator.h"

#include <iostream>
#include <cmath>
#include <chrono>
#include <thread>

class Synth1 {
public:
  Synth1(Oscillator *oscillator);
  ~Synth1();
  double midiToFrequency(int midinote);
  void noteOn(int midinote, double amplitude, double duration);
  void noteOff();
  void setOscillator(Oscillator *oscillator);
private:
  Oscillator *oscillator;
  double duration;
  std::thread *noteOffThread;
  void noteOffThreadCallable();
};


#endif
