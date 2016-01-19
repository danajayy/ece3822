#include "hw6.h"

int readfile (FILE* openfile, int dataformat, int num) {

  long fsize;
  int result;
  int i;
  
  // getting size of openfile to create buffer
  //
  fseek(openfile, 0, SEEK_END);
  fsize = ftell(openfile);
  rewind(openfile);

  if (dataformat==1) { // if 1, read as float
    float* buffer;
    //allocate memory to contain whole file
    //
    buffer = (float*) malloc (sizeof(float)*fsize);
    if (buffer == NULL) {
      fprintf(stdout, "Unable to allocate memory for read data.\n");
    }

    // read file into buffer
    //
    result = fread(buffer, bytecount, fsize, openfile);

  }
   
  if ((dataformat==2)||(dataformat==0)){
    long* buffer;

    // allocate memory for buffer
    //
    buffer = (long*) malloc(sizeof(long)*fsize);
    if (buffer == NULL) {
      fprintf(stdout, "Unable to allocate memory for read data\n");
    } // end of if statement to check if buffer is NULL
    result = fread(buffer, bytecount, fsize, openfile);

    printf("Successfully read the file. result = %d\n", result);
    
    for (i = 0; i < sizeof(buffer); i++) {
      if (num == 1) {
	fprintf(stdout, "%06d : %ld\n", i, buffer[i]);
      }
      else {
	fprintf(stdout, "%ld\n", buffer[i]);
      }
    }
    
  } // end of if statement to read file as 16-byte int

  printf("I ran through the readfile function.\n");
  
} // end of readfile function


int read_flags (int argc, char *argv[], int &data_format, int &numflag) {

  int i; // counter to loop through command line arguments
  
  for (i=1; i < argc; i++) {
    if (strcmp(argv[i], "-h") == 0 ) {
      helpflag();
    }
  
    if (strcmp(argv[i], "-numbers") == 0 ) {
      numflag = 1;
    }

    if (strcmp(argv[i], "-f") == 0 ) {
      data_format = 1;
    }

    if (strcmp(argv[i], "-i") == 0 ) {
      data_format = 2;
    }
  }

  return 0;

}

void helpflag (void) {
  fprintf(stdout, "\nThis program opens a .raw data file(s) and reads the data based on what the user specifies.\nBy default, the program reads the data as 16-bit integers if user does not specify data format.\nLine numbers can be displayed next to each read data if specified by user, they are not by default.");
  fprintf(stdout, "\n\n\tflag\t\tfunction\n\t-------------------------------------------\n");
  fprintf(stdout, "\t-h\t\tDisplays this help message\n\n\t-numbers\tdisplays line numbers for each data read from file(s)\n\n\t-f\t\treads data as floats\n\n\t-i\t\treads data as 16-bit integers\n\n");

}

