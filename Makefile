SHELL = /bin/sh
CFLAGS = -O1
CC = gcc
CXX = g++
OBJS = kvdb.o io.o handler.o data_t.o

default:kvdb

kvdb: $(OBJS)
	$(CXX) $(CFLAGS) -o kvdb $^

debug: $(OBJS)
	$(CXX) $(CFLAGS) -D DEBUG -o kvdb $^

%.o: %.c
	$(CXX) $(CFLAGS) -c -o $@ $<

.PHONY:clean
clean:
	rm -f *.o *.core