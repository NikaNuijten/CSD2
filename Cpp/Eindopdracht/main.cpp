#include <iostream>
#include <thread>
#include "jack_module.h"
#include "sine.h"
#include "saw.h"
#include "square.h"
#include "melody.h"
#include "synth1.h"
#include "melodyGenerator.h"

#define PI_2 6.28318530717959

int main(int argc,char **argv)
{
  // create melody instance
  Melody melody2;
  MelodyGenerator melodyGenerator;
  // generate and add some notes to melody
  while (melody2.isWritable()) {
    // write random melody
    int value = melodyGenerator.rand_between(60,73);
    melody2.addNote(value);
    std::cout << value << "\n";
  }

  //std::cout << melody2.getNote() << "\n";

  // create a JackModule instance
  JackModule jack;

  // init the jack, use program name as JACK client name
  jack.init(argv[0]);
  double samplerate = jack.getSamplerate();
  //int frequencies = myMelody.frequencies;

  // create waves
  Sine sine(samplerate, 262);
  Saw saw(samplerate, 262);
  Square square(samplerate, 262);

  Sine sine2(samplerate, 262);
  Saw saw2(samplerate, 262);
  Square square2(samplerate, 262);

  Oscillator* oscillator = &sine;
  Oscillator* oscillator2 = &sine;

  oscillator->setAmplitude(0.00);
  oscillator2->setAmplitude(0.00);
  Synth1 synth1(oscillator, oscillator2);

  //assign a function to the JackModule::onProces
  jack.onProcess = [&oscillator, &oscillator2](jack_default_audio_sample_t *inBuf,
     jack_default_audio_sample_t *outBuf, jack_nframes_t nframes) {

    for(unsigned int i = 0; i < nframes; i++) {
      // write oscillator output * amplitude --> to output buffer
      outBuf[i] = oscillator->getSample() + oscillator2->getSample();
      // calculate next sample
      oscillator->tick();
      oscillator2->tick();
    }

    return 0;
  };

  jack.autoConnect();

  //keep the program running and listen for user input, q = quit
  std::cout << "\n\nPress 'q' when you want to quit the program.\nPress '1' for sine, '2' for saw, '3' for square.\n";
  bool running = true;
  while (running)
  {
    switch (std::cin.get())
    {
      case 'q':
        running = false;
        jack.end();
        //delete oscillator;
        //oscillator = nullptr;
        break;

      case '1':
        //point oscillator to sine
        oscillator = &sine;
        oscillator2 = &saw2;
        synth1.setOscillator(oscillator, oscillator2);
        break;

      case '2':
        //point oscillator to saw
        oscillator = &saw;
        oscillator2 = &square2;
        synth1.setOscillator(oscillator, oscillator2);
        break;

      case '3':
        //point oscillator to square
        oscillator = &square;
        oscillator2 = &sine2;
        synth1.setOscillator(oscillator, oscillator2);
        break;

      case 'a':
        synth1.noteOn(60, 0.05, 500.); // play note c
        break;

      case 'w':
        synth1.noteOn(61, 0.05, 500.); // play note c#
        break;

      case 's':
        synth1.noteOn(62, 0.05, 500.); // play note d
        break;

      case 'e':
        synth1.noteOn(63, 0.05, 500.); // play note d#
        break;

      case 'd':
        synth1.noteOn(64, 0.05, 500.); // play note e
        break;

      case 'f':
        synth1.noteOn(65, 0.05, 500.); // play note f
        break;

      case 't':
        synth1.noteOn(66, 0.05, 500.); // play note f#
        break;

      case 'g':
        synth1.noteOn(67, 0.05, 500.); // play note g
        break;

      case 'y':
        synth1.noteOn(68, 0.05, 500.); // play note g#
        break;

      case 'h':
        synth1.noteOn(69, 0.05, 500.); // play note a
        break;

      case 'u':
        synth1.noteOn(70, 0.05, 500.); // play note a#
        break;

      case 'j':
        synth1.noteOn(71, 0.05, 500.); // play note b
        break;

      case 'k':
        synth1.noteOn(72, 0.05, 500.); // play note c'
        break;

      case 'z':
        synth1.noteOff();
        break;

      case 'p':
        // play melody2
        int note = melody2.getNote();
        std::cout << note << "\n";
        synth1.noteOn(note, 0.05, 500.);
        break;
    }
  }

  //end the program
  return 0;
} // main()
