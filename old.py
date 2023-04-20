from machine import Pin, PWM, UART
from time import sleep

uart = UART(0, 9600)

buzzer = PWM(Pin(15))

signal_sv1 = PWM(Pin(5))
signal_sv1.freq(50)

signal_sv2 = PWM(Pin(4))
signal_sv2.freq(50)

#definig the size of the step that the motor will take in the loop 
#it's equivalent to the speed at which the motor is moving
STEP= 50

def move_servo(position, signal):
    signal.duty_u16(position)

#function to activate the buzzer attached to the robot
def buzz():
    buzzer.duty_u16(1000)
    buzzer.freq(1000)
    sleep(0.5)
    buzzer.duty_u16(0)

# dictinary to map out the commands
COMMANDS = {
    b'1': (signal_sv1, range(1000, 6000, STEP),
    b'2': (signal_sv1, range(6000, 1000, -STEP)),
    b'3': (signal_sv2, range(6000, 1000, -STEP)),
    b'4': (signal_sv2, range(1000, 6000, STEP))
}

while True:
    if uart.any():
        command = uart.readline()
        print(command)
        if command in COMMANDS:
            buzz()
            signal, positions = COMMANDS[command]
            for pos in positions:
                move_servo(pos, signal)
