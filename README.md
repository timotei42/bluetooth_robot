# Raspberry Pi Robot

This repository is dedicated to documenting the robot I made using microPython and Raspberry Pi. 

[You can see it in action here.](https://youtu.be/KlTeV0myg9c)

Here I will go over:
 - the components I use
 - some values I set in the code
 - the code's general structure
 - how I communicate with it
 
 ## The Components
 The noteworthy components I use are:
  - a Raspberry Pi Pico H
  - HC-05 Bluetooth module
  - a simple piezo-buzzer 
  - 2 SG 90 servos ([microservos, as not to bother with powering them up](http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf))
 
 ## Set Values in the Code
 They are as follows
 - The PWM frequency for the microservos is 50 Hz.
 - The Baud Rate for the Bluetooth chip is set to 9600, as per [standard.](http://www.ece.northwestern.edu/local-apps/matlabhelp/techdoc/matlab_external/baudrate.html).Despite the commands being really basic, I didn't bother setting it any lower. 9600 is on the lower end of UART transmission anyway.
 - The Buzzer frequency for when it's active is set to 1000 Hz.
 - The 2 positions that the servos move between in the old.py script (1000 and 6000 respectively) are chosen at random. I could potentially set a wider angle so the arm has a larger range of mobility.
  - The STEP variable is to determine how fast the servo schanges position. The higher it is the faster the servo will move. I set it to 50 for smooth movement. It also runs a lower risk of the robot losing balance, with the base being 0.5 kg.
## The structure of the code

### main.py

After initializing the starting position for each servo I snap both servos to it. After this, based on the command read, I either decrement or increment one of the positions.I attached a piezo buzzer so I have an indicator for when the command has been received succesfully.The bluetooth module may lose connection at random.

### old.py

The first itteration of the script but instead of allowing for "precise" movement between 2 points for each servo, it moves the arm to one of four positions.The commands are simple so I ended up mapping them to a dictionary. 

## Communication

I send the robot commands via the Bluetooth module, thus I need a bluetooth-compadible device. For this project I used a phone with the "Serial Bluetooth Terminal" app. It also allowed me to set the commands for the servos as macros. Highly recommend it.
 
## Implementaton in C

I adeed the implementation in C of this script along with a makefile to install the dependencies needed. Simply run 
```make install-deps```
and 
```make``` 
in the src directory. The program is to be compiled with ```gcc main.c -lwiringPi -o main```.
