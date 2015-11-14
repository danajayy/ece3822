#include "foo.h" // import custom header file that contains the class lamp and its implementations

int main (int argc, char** argv) {

  lamp lamp[argc]; // create an array of lamps the length of amount of args

  // loop through all the arguments
  // and run them by with the class debug
  //
  for(int i = 1; i < argc; i++) {
  
    lamp[i].set_brand(argv[i]); // has to be 1-index of argv since 0-index of argv is the script name
  }

  // for every argument in arg, send it to debugger
  for (int i = 1; i < argc ; i++) {
    printf("Brand %d\n", i); // print out the value of i to indicate the number of brand
    lamp[i].debug(stdout); // for the i index of lamp, send to debugger to print the data
    printf("-----\n"); // a divider to make the output look pretty
  }
  
}
