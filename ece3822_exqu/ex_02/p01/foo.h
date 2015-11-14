#include <stdio.h>
#include <stdlib.h>

enum STATE {ON, OFF};

static float ac_power = 60.0;

// Lamp class
//
class lamp {

protected:
  long lamp_length;
  long height;
  long width;
  int watts;
  char* brand;
  STATE state;

public:
  // sets all the data in protected to -1
  //
  void setdata() {
    lamp_length = -1;
    height = -1;
    width = -1;
    watts = -1;
    brand = -1;
  };
  
  // clears everything...hopefully
  //
  void destructor() { delete(); };

  // brand name stored in arg
  //
  bool set_brand(char* arg) {
    arg = brand;
  };

  bool debug(FILE* fp) {
    printf(" length: %ld \n height: %ld \n width: %ld \n watts: %d \n brand: %s \n", lamp_length, height, width, watts, brand);
  };
  
};
