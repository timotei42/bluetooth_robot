from time import sleep
from machine import PWM,Pin,UART,Pin

uart = UART(0,9600)
buzzer = PWM(Pin(15))
pwm_frq=50 #defining pwm frequency

signal_sv1 = PWM(Pin(5))
signal_sv1.freq(pwm_frq)

signal_sv2 = PWM(Pin(4))
signal_sv2.freq(pwm_frq)

#defining starting positions
pos_sv_1=1000
pos_sv_2=1000

#defining the value of the step(how much the servo will move at each iteration)
STEP=500

def move_servo (position,signal):
    signal.duty_u16(position)
    sleep(0.01)
    
def buzz():
    buzzer.duty_u16(1000)
    buzzer.freq(1000)
    buzzer.duty_u16(0)
    
def pos_init():
    move_servo(pos_sv_1,signal_sv1)
    move_servo(pos_sv_2,signal_sv2)

pos_init()
#to be commented out unless you want it to snap at a set position
#every time you plug it in 
while True:
    if uart.any():
        command = uart.readline()
        print(command)
        if command== b'1':
            buzz()
            for pos in range(pos_sv_1,pos_sv_1+STEP,50):
                move_servo(pos,signal_sv1)
            pos_sv_1=pos_sv_1+STEP
        elif command== b'2' :
            buzz()
            for pos in range(pos_sv_1,pos_sv_1-STEP,-50):
                move_servo(pos,signal_sv1)
            pos_sv_1=pos_sv_1-STEP
        elif command == b'3' :
            buzz()
            for pos in range(pos_sv_2,pos_sv_2-STEP,-50):
                move_servo(pos,signal_sv2)
            pos_sv_2=pos_sv_2-STEP
        elif command == b'4' :
            buzz()
            for pos in range(pos_sv_2,pos_sv_2+STEP,50):
                move_servo(pos,signal_sv2)
            pos_sv_2=pos_sv_2+STEP
