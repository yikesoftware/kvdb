SHELL = /bin/sh
CFLAGS_RELEASE = -O2
CFLAGS_DEBUG = -g -D DEBUG
CFLAGS_NOOPT = -O0
CC = gcc
CXX = g++
OBJS = kvdb.o io.o handler.o data_t.o

default:kvdb

kvdb: $(OBJS)
	$(CXX) $(CFLAGS_RELEASE) -o kvdb $^

debug: $(OBJS)
	$(CXX) $(CFLAGS_DEBUG) -o kvdb $^

noopt: $(OBJS)
	$(CXX) $(CFLAGS_NOOPT) -o kvdb $^

%.o: %.c
	$(CXX) $(CFLAGS) -c -o $@ $<

.PHONY:clean
clean:
	rm -f *.o *.core