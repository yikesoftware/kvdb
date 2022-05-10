SHELL = /bin/sh
CFLAGS := 

CC = afl-gcc-fast
CXX = afl-g++-fast
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

%.o: %.cpp
	$(CXX) $(CFLAGS) -c -o $@ $<
	

.PHONY:clean
clean:
	rm -f *.o *.core
