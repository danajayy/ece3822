#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int ece_3822_add_sin( float x, float y);

int main() {

  float xx = 30;
  float yy = 30;
  float a;
  
  printf("Hello World\n");
  
  a = ece_3822_add_sin(xx, yy);
  printf("Sum of the sines is: %.2f\n", a);

}
  
