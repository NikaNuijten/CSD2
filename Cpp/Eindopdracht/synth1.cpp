#include "synth1.h"

Synth1::Synth1(Oscillator *oscillator){
  this->oscillator = oscillator;
}

Synth1::~Synth1(){
}

double Synth1::midiToFrequency(int midinote){
  return pow(2.0, ((midinote-69)/12.))*440.0;
}

void Synth1::noteOn(int midinote, double amplitude, double duration){
  oscillator->setFrequency(midiToFrequency(midinote));
  oscillator->setAmplitude(amplitude);
  this->duration = duration;
  noteOffThread = new std::thread( [=] { noteOffThreadCallable(); } );
}

void Synth1::noteOff(){
  oscillator->setAmplitude(0.0);
}

void Synth1::setOscillator(Oscillator *oscillator){
  this->oscillator = oscillator;
}

void Synth1::noteOffThreadCallable(){
  //std::cout << "noteOffThreadCallable" << std::endl;
  using namespace std::this_thread;     // sleep_for, sleep_until
  using namespace std::chrono_literals; // ns, us, ms, s, h, etc.
  using std::chrono::system_clock;

  sleep_for(duration*(1ms));
  noteOff();
}
