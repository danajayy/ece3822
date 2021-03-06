#include <stdio.h>
#include <stdlib.h>
#include <string.h> // library is called string, not strings

class Car {

  // protected 
  //
protected:
  float speed;
  char* model;
  char* brand;

  // public
  //
public:
  Car(float arg = 60.0); // constructor declaration with parameter
  ~Car(); // destructor declaration

  bool set_model(char* model_a);
  bool fun(Car** car, char* str);
  bool debug();

  // private
  //
private:

};
