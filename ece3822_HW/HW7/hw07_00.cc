#include "hw_07.h"


// constructor definition
//
NL::NL() {
  name = (char*)NULL; // making sure name is not initialized
  namefile = (char*)NULL;
}

NL::~NL() {
  delete [] namefile;
  delete [] name;
}

bool NL::readfile(FILE* fp_a) {
  //
}

bool NL::writefile(FILE* fp_a) {
  //
}

bool NL::debug() {
  printf("file name: %s\n", (char*)namefile);
  return true;
}
