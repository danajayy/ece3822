#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int ece_3822_add_sin(float x, float y);

int ece_3822_add_sin(float x, float y){

  float pi = 3.14159265;
  float z;
  float a = sin((x*pi)/180);
  float b = sin((x*pi)/180);
  
  printf("a = %.2f\n", a);
  printf("b= %.2f\n", b);
  
  z = a + b;

  return(z);
  
}
