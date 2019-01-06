#include "synth1.h"

// constructor
Synth1::Synth1(Oscillator *oscillator, Oscillator *oscillator2){
  this->oscillator = oscillator;
  this->oscillator2 = oscillator2;
}

// destructor
Synth1::~Synth1(){
}

double Synth1::midiToFrequency(int midinote){
  return pow(2.0, ((midinote-69)/12.))*440.0;
}

// noteOn
void Synth1::noteOn(int midinote, double amplitude, double duration){
  oscillator->setFrequency(midiToFrequency(midinote));
  oscillator->setAmplitude(amplitude);
  oscillator2->setFrequency(midiToFrequency(midinote));
  oscillator2->setAmplitude(amplitude);
  this->duration = duration;
  noteOffThread = new std::thread( [=] { noteOffThreadCallable(); } );
}
//noteOff
void Synth1::noteOff(){
  oscillator->setAmplitude(0.0);
  oscillator2->setAmplitude(0.0);
}

void Synth1::setOscillator(Oscillator *oscillator, Oscillator *oscillator2){
  this->oscillator = oscillator;
  this->oscillator2 = oscillator2;
}

void Synth1::noteOffThreadCallable(){
  using namespace std::this_thread;     // sleep_for, sleep_until
  using namespace std::chrono_literals; // ns, us, ms, s, h, etc.
  using std::chrono::system_clock;

  sleep_for(duration*(1ms));
  noteOff();
}
