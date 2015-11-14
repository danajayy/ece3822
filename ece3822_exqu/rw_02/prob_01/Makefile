# file: GNUMakefile
#

# define a target for the application
#
all: foo # desired program that will be made

# define a target to link the application
#
foo: foo.o foo_00.o # needed object files for foo
	g++ foo.o foo_00.o -o foo # need to establish what object files are needed and will be linked to create foo

# define a target to compile the application
#
foo.o: foo.cc foo.h # need to compile foo.cc to get foo.o
	g++ -O2 -c foo.cc -o foo.o
foo_00.o: foo_00.cc foo.h # need to compile foo_00.cc to get foo_00.cc
	g++ -O2 -c foo_00.cc -o foo_00.o

# define a target to clean the directory
#
clean:
	rm -f foo.o foo_00.o
	rm -f foo

#
# end of file


