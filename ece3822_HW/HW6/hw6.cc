#include "hw6.h"

int main (int argc, char *argv[]) {

  int format = 0; // to determine how to read data
  int numlines = 0; // to determine if number lines
  int i; // counter for for loop
  int j;
  long fsize;
  FILE* fp; // will contain data of open file

  int result;

  read_flags(argc, argv, format, numlines);

  for (i = 0; i < argc; i++ ) {
    if (strstr(argv[i], ".raw") != NULL ) {
      fp = fopen(argv[i], "r");
      if (fp == NULL ) {
	fprintf(stdout, "Unable to open ifile %s because either does not exist or no read permission.\n", argv[i]);
      }
      else {
	fprintf(stdout,"File %s successfully opened.\n", argv[i]);
	fseek(fp, 0, SEEK_END);
	fsize = ftell(fp);
	rewind(fp);

	long *buffer;
	buffer = (long*) malloc(sizeof(long)*fsize);
	if (buffer == NULL) {
	  printf("unable to allocate memory\n");
	}
	
	result = fread(buffer, bytecount, fsize, fp);

	for (j = 0; i <sizeof(buffer); j++) {
	  fprintf(stdout, "%06d : %ld\n", j, buffer[j]);
	}
	//	readfile(fp, format, numlines);
	//	fclose(fp);
      }
    }
  }
}
