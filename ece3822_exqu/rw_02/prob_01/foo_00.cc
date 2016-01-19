// This is the rework for exam 2 problem 1

#include "foo.h" // need to include foo.h because contains all the class method declarations

// defining constructor to initialize all data to be -1
//
lamp::lamp() {
  length = -1; // initializing length to be -1
  height = -1; // initializing height to be -1
  width = -1; // initializing width to be -1
  watts = -1; // initializing watts to be -1
  state = OFF; // starting with the lamp off
  brand = (char*)NULL; // make sure that brand is not initialized
}

// defining destructor
//
lamp::~lamp() {

  // if brand already has been initialized, clear it!
  //
  if (brand != (char*)NULL) {
    delete [] brand; //clears 100 bytes of memory for brand
    brand = (char*)NULL; // makes sure to un-initialize brand
  }
}

// defining set_brand method
//
bool lamp::set_brand(char* arg) {

  // if brand is not initialized, allocate memory for it
  // if not, delete/clear the memory for brand and
  // uninitialize it for the next lamp brand
  //
  if (brand == (char*)NULL) {
    brand = new char[100]; // allocates 100 bytes of memory for brand
    strcpy(brand, arg); // copies argument into brand
  } else if (brand != (char*)NULL) {
    delete [] brand; // clear memory of brand
    brand = (char*)NULL; // uninitialize brand
  }
  
  return true;
}

//defining debug method
//
bool lamp::debug(FILE* fp) {
  fprintf(fp, "brand: %s\n", brand); // print the lamp brand
  fprintf(fp, "length: %ld\n", length); // print length of lamp
  fprintf(fp, "width: %ld\n", width); // print width of lamp
  fprintf(fp, "height: %ld\n", height); // print height of lamp
  fprintf(fp, "watts: %ld\n", watts); // print watts of lamp

  // switch case used to print out the state of the lamp
  //
  switch(state) {
  case ON : fprintf(fp, "State: ON\n"); break; // case for when lamp is ON
  case OFF : fprintf(fp, "State: OFF\n"); break; // case for when the lamp is OFF (this is the default case too)
  }
}
