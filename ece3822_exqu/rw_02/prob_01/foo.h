// This is a rework for exam 2 problem 1

#ifndef FOO_H
#define FOO_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

enum STATE { ON, OFF }; // declaring the state of the lamp

static const float ac_power = 60.0; // static const ac_power

class lamp{ // creating the class lamp

  // protected data
 protected:
  long length; // length of lamp
  long height; // height of lamp
  long width; // width of lamp
  long watts; // watts of lamp
  char* brand; // brand of lamp
  STATE state; // on/off state of lamp

 public:
  bool set_brand(char* arg); // gets the brand names of lamp
  bool debug(FILE* fp); // debugger declared, where the
  //data of lamp is being outputted
  lamp(); // constuctor declared
  ~lamp (); // destructor declared
  
};

#endif
