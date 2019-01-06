#include "melodyGenerator.h"

MelodyGenerator::MelodyGenerator(){
  std::srand(std::time(nullptr));
}

int MelodyGenerator::rand_between(int min, int max){
  int size = max - min;
  //std::cout << min+std::rand()%size << "\n";
  return min+std::rand()%size;
}
