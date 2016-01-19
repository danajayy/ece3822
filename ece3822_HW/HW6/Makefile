# file: GNUMakefile
#

# define a target for the application
#
all: hw6

# define a target to link the application
#
hw6: hw6.o hw6_00.o
	g++ hw6.o hw6_00.o -o hw6

# define a target to compile the application
#
hw6.o: hw6.cc hw6.h
	g++ -O2 -c hw6.cc -o hw6.o
hw6_00.o: hw6_00.cc hw6.h
	g++ -O2 -c hw6_00.cc -o hw6_00.o

# define a target to clean the directory
#
clean:
	rm -f hw6.o hw6_00.o
	rm -f hw6

#
# end of file


