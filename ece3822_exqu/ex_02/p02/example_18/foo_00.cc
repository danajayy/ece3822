#include "foo.h"

// constructor definition with argument float speed_a
//
Car::Car(float speed_a) {
  speed = speed_a; // speed_a argument will be speed
  model = (char*)NULL;
  brand = (char*)NULL;
}

// destructor definition
//
Car::~Car() {
  delete [] model; // clearing model name
  delete [] brand; // clearing brand name
}

bool Car::set_model(char* model_a) {
  model = model_a;
  return true;
}

bool Car::debug() {
  printf("hello world: %s\n", model);
  return true;
}

// implement a function
//
bool Car::fun(Car** car_a, char* str) {
  car_a[0] = new Car;
  car_a[0]->set_model(str);
  return true;
}