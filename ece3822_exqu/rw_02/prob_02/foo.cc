#include "foo.h"

int main (int argc, char** argv) {

  // declare some variables
  //
  
  Car tcar; // create new object tcar

  // new Car*[10] is an array of pointers with length 10
  // these are not objects yet, they are just pointers
  //
  Car** cars = new Car*[10];

  // create temp variable to hold argv value
  char* tstr = new char[100];

  // call the function
  //
  strcpy(tstr, argv[1]); // copy the first command line argument into tstr
  tcar.fun(cars, (char*)tstr); // passing in cars and tstr (pointer to argv[1])
  delete tstr; // clears tstr

  // display debug information
  //
  cars[1]->debug();
}

