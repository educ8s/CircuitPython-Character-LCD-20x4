# This script supports the Raspberry Pi Pico board
# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# 20x4 I2C DISPLAY: http://educ8s.tv/part/20x4LCD

import board, busio, microcontroller
from lcd.lcd import LCD #Get this module here: https://github.com/dhalbert/CircuitPython_LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface #Get this module here: https://github.com/dhalbert/CircuitPython_LCD
from time import sleep

sda, scl = board.GP0, board.GP1
i2c = busio.I2C(scl, sda)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=4, num_cols=20)


# Create you own custom characters here: http://educ8s.tv/tools/lcd-character-creator/

LT = (0b01111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111)
UB = (0b11111, 0b11111, 0b11111, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000)
RT = (0b11110, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111)
LL = (0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b01111)
LB = (0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b11111, 0b11111, 0b11111)
LR = (0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11110)
UMB = (0b11111, 0b11111, 0b11111, 0b00000, 0b00000, 0b00000, 0b11111, 0b11111)
LMB = (0b11111, 0b00000, 0b00000, 0b00000, 0b00000, 0b11111, 0b11111, 0b11111)

def c_to_f(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def create_custom_characters():
    lcd.create_char(0,LT)
    lcd.create_char(1,UB)
    lcd.create_char(2,RT)
    lcd.create_char(3,LL)
    lcd.create_char(4,LB)
    lcd.create_char(5,LR)
    lcd.create_char(6,UMB)
    lcd.create_char(7,LMB)

def digit_0(position):
    lcd.set_cursor_pos(1, position) 
    lcd.write(0)
    lcd.write(1)
    lcd.write(2)
    lcd.set_cursor_pos(2, position)
    lcd.write(3)
    lcd.write(4)
    lcd.write(5)
    
def digit_1(position):
    lcd.set_cursor_pos(1,position)
    lcd.write(1);
    lcd.write(2)
    lcd.set_cursor_pos(2,position + 1)
    lcd.write(5)

def digit_2(position):
    lcd.set_cursor_pos(1, position)
    lcd.write(6)
    lcd.write(6)
    lcd.write(2)
    lcd.set_cursor_pos(2, position)
    lcd.write(3)
    lcd.write(7)
    lcd.write(7)

def digit_3(position):
    lcd.set_cursor_pos(1,position)
    lcd.write(6)
    lcd.write(6)
    lcd.write(2)
    lcd.set_cursor_pos(2,position)
    lcd.write(7)
    lcd.write(7)
    lcd.write(5)

def digit_4(position):
    lcd.set_cursor_pos(1,position)
    lcd.write(3)
    lcd.write(4)
    lcd.write(2)
    lcd.set_cursor_pos(2, position + 2)
    lcd.write(5)
    
def digit_5(position):
    lcd.set_cursor_pos(1, position)
    lcd.write(0)
    lcd.write(6)
    lcd.write(6)
    lcd.set_cursor_pos(2, position)
    lcd.write(7)
    lcd.write(7)
    lcd.write(5)

def digit_6(position):
    lcd.set_cursor_pos(1, position)
    lcd.write(0)
    lcd.write(6)
    lcd.write(6)
    lcd.set_cursor_pos(2, position)
    lcd.write(3)
    lcd.write(7)
    lcd.write(5)
    
def digit_7(position):
    lcd.set_cursor_pos(1, position)
    lcd.write(1)
    lcd.write(1)
    lcd.write(2)
    lcd.set_cursor_pos(2, position + 1)
    lcd.write(0)

def digit_8(position):
    lcd.set_cursor_pos(1, position)
    lcd.write(0)
    lcd.write(6)
    lcd.write(2)
    lcd.set_cursor_pos(2, position)
    lcd.write(3)
    lcd.write(7)
    lcd.write(5)
    
def digit_9(position):
    lcd.set_cursor_pos(1, position)
    lcd.write(0)
    lcd.write(6)
    lcd.write(2)
    lcd.set_cursor_pos(2, position + 2)
    lcd.write(5)

def digit_dot(position):
    lcd.set_cursor_pos(2, position)
    lcd.write(0)
    
def digit_f(position):
    lcd.set_cursor_pos(1, position)
    lcd.write(0)
    lcd.write(1)
    lcd.set_cursor_pos(2, position)
    lcd.write(3)
    lcd.write(1)

def digit_c(position):
    lcd.set_cursor_pos(1, position)
    lcd.write(0)
    lcd.write(1)
    lcd.set_cursor_pos(2, position)
    lcd.write(3)
    lcd.write(4)

def print_digit(digit, position):
    if digit == "0":
        digit_0(position)
    if digit == "1":
        digit_1(position)
    if digit == "2":
        digit_2(position)
    if digit == "3":
        digit_3(position)
    if digit == "4":
        digit_4(position)
    if digit == "5":
        digit_5(position)
    if digit == "6":
        digit_6(position)
    if digit == "7":
        digit_7(position)
    if digit == "8":
        digit_8(position)
    if digit == "9":
        digit_9(position)
        
def print_temperature(temperature):
    if len(temperature) == 3:
        print_digit(temperature[2],13)
        digit_dot(11)
        print_digit(temperature[0],7)
    
    if len(temperature) == 4:
        print_digit(temperature[3],13)
        digit_dot(11)
        print_digit(temperature[1],7)
        print_digit(temperature[0],3)
        
    if len(temperature) == 5:
        print_digit(temperature[4],13)
        digit_dot(11)
        print_digit(temperature[2],7)
        print_digit(temperature[1],3)
        print_digit(temperature[0],0)

metric = True  #Change to False for degrees Fahrenheit

create_custom_characters()

previous_temperature = ""
temperature = ""

while True:
    previous_temperature = temperature
    
    if metric:
        temperature = str(round(microcontroller.cpu.temperature,1))
    else:
        temperature = str(round(c_to_f(microcontroller.cpu.temperature),1))
        
    if temperature != previous_temperature:
        lcd.clear()
        print_temperature(temperature)
        lcd.set_cursor_pos(1,17)
        lcd.print("o")
        if metric:
            digit_c(18)
        else:
            digit_f(18)

    sleep(5)