#ifndef HW6_H
#define HW6_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const int bytecount = 1024;

int readfile (FILE* openfile, int dataformat, int num);
int read_flags(int argc, char *argv[], int &dataformat, int &numlines);
void helpflag (void); // function prototype for -h flag


#endif
