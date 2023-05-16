#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <unistd.h>
#include <wiringPi.h>
#include <softPwm.h>
#include <wiringSerial.h>

#define BUZZER_PIN 15
#define SERVO_1_PIN 5
#define SERVO_2_PIN 4
#define UART_DEVICE "/dev/ttyS0"
#define BAUD_RATE 9600
#define PWM_FREQUENCY 50
#define STEP 500

uint16_t pos_sv_1 = 1000;
uint16_t pos_sv_2 = 1000;

void moveServo(uint16_t position, int signal) {
    pwmWrite(signal, position);
    usleep(10000);
}

void buzz() {
    pwmWrite(BUZZER_PIN, 1000);
    delay(1);
    pwmWrite(BUZZER_PIN, 0);
}

void posInit() {
    moveServo(pos_sv_1, SERVO_1_PIN);
    moveServo(pos_sv_2, SERVO_2_PIN);
}

int main() {
    wiringPiSetup();
    serialOpen(UART_DEVICE, BAUD_RATE);
    softPwmCreate(BUZZER_PIN, 0, 2000);
    softPwmCreate(SERVO_1_PIN, 0, 20000);
    softPwmCreate(SERVO_2_PIN, 0, 20000);

    posInit();

    while (1) {
        if (serialDataAvail(0)) {
            char command = serialGetchar(0);
            printf("%c\n", command);
            
            if (command == '1') {
                buzz();
                for (uint16_t pos = pos_sv_1; pos <= pos_sv_1 + STEP; pos += 50) {
                    moveServo(pos, SERVO_1_PIN);
                }
                pos_sv_1 += STEP;
            } else if (command == '2') {
                buzz();
                for (uint16_t pos = pos_sv_1; pos >= pos_sv_1 - STEP; pos -= 50) {
                    moveServo(pos, SERVO_1_PIN);
                }
                pos_sv_1 -= STEP;
            } else if (command == '3') {
                buzz();
                for (uint16_t pos = pos_sv_2; pos >= pos_sv_2 - STEP; pos -= 50) {
                    moveServo(pos, SERVO_2_PIN);
                }
                pos_sv_2 -= STEP;
            } else if (command == '4') {
                buzz();
                for (uint16_t pos = pos_sv_2; pos <= pos_sv_2 + STEP; pos += 50) {
                    moveServo(pos, SERVO_2_PIN);
                }
                pos_sv_2 += STEP;
            }
        }
    }
    
    return 0;
}
