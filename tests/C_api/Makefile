CFLAGS = -O0 -g
INCLUDES = -I../../S4 
LIBS = -L../../build -lS4 -lopenblas -lfftw3 -lm

all:
	g++ -g $(CFLAGS) $(INCLUDES) test_api.c -o test_api.out $(LIBS)
