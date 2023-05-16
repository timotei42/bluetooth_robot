CC = gcc
CFLAGS = -Wall
LIBS = -lwiringPi 

TARGET = main
SRCS = main.c

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRCS) $(LIBS)

install-deps:
	sudo apt-get update
	sudo apt-get install wiringpi libwiringpi-dev


clean:
	rm -f $(TARGET)
