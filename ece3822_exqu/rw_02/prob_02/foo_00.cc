#include "foo.h"

// constructor definition with argument float speed_a
//
Car::Car(float speed_a) {
  speed = speed_a; // speed_a = 60.0 = speed
  model = (char*)NULL; // make sure that model is not initialized
  brand = (char*)NULL;
}

// destructor definition
//
Car::~Car() {
  delete [] model; // clearing model name
  delete [] brand; // clearing brand name
}

bool Car::set_model(char* model_a) {

  if (model == (char*)NULL) {
      // if model is NULL, then memory never been allocated/initialized
      //
      model = new char[strlen(model_a)+1]; // have to allocate memory to model
      strcpy(model, model_a); // copy model_a into object model
    }
  else if (model != (char*)NULL) {
      // if model is not NULL, must delete the memory for model and
      // un-initialize it by NULL
      //
      delete [] model;
      model = (char*)NULL;
    }
  return true;
}

bool Car::debug() {
  printf("hello world: %s\n", model);
  return true;
}

// implement a function
//
bool Car::fun(Car** car_a, char* str) {

  // need this object to exist for debug method to run
  //
  car_a[1] = new Car; // had to change from index 0 to index 1
  car_a[1]->set_model(str); // had to change from index 0 to index 1
  return true;
}
