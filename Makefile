SHELL = /bin/sh
CFLAGS := 

CC = gcc
CXX = g++
OBJS = kvdb.o io.o handler.o data_t.o

default:release

release: CFLAGS += -O2
release: $(OBJS)
	$(CXX) $(CFLAGS) -o kvdb $^
	strip -s kvdb

debug: CFLAGS += -g -O0 -D DEBUG
debug: $(OBJS)
	$(CXX) $(CFLAGS) -o kvdb $^

noopt: CFLAGS += -O0
noopt: $(OBJS)
	$(CXX) $(CFLAGS) -o kvdb $^

asan: CFLAGS += -g -fsanitize=address -fsanitize-recover=address -fno-omit-frame-pointer
asan: $(OBJS)
	$(CXX) $(CFLAGS) -o kvdb.asan $^
	
afl: CXX = afl-g++-fast
afl: $(OBJS)
	$(CXX) $(CFLAGS) -o kvdb $^

%.o: %.cpp
	$(CXX) $(CFLAGS) -c -o $@ $<
	

.PHONY:clean
clean:
	rm -f *.o *.core
