# This script supports the Raspberry Pi Pico board
# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# 20x4 I2C DISPLAY: http://educ8s.tv/part/20x4LCD

import board, busio, time

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# Create you own custom characters here: http://educ8s.tv/tools/lcd-character-creator/
phone = (0x04,0x1F,0x11,0x11,0x1F,0x1F,0x1F,0x1F)
heart = (0x00,0x0A,0x15,0x11,0x0A,0x04,0x00,0x00)
speaker = (0x01,0x03,0x07,0x1F,0x1F,0x07,0x03,0x01)
smile = (0x00,0x0A,0x00,0x11,0x0E,0x00,0x00,0x00)

sda, scl = board.GP0, board.GP1
i2c = busio.I2C(scl, sda)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=4, num_cols=20) #If address 0x27 does not work try 0x3F

lcd.set_cursor_pos(0,3)
lcd.print("Hello YouTube!")
lcd.set_cursor_pos(1,8)
lcd.print("****")
lcd.set_cursor_pos(2,0)
lcd.print("This is a demo text.")
lcd.set_cursor_pos(3,8)
lcd.print("****")

time.sleep(2)
lcd.clear()

lcd.create_char(0,phone)
lcd.create_char(1,heart)
lcd.create_char(2,speaker)
lcd.create_char(3,smile)

lcd.set_cursor_pos(0,0)
lcd.print("Custom Characters")
lcd.set_cursor_pos(2,0)
lcd.write(0)
lcd.set_cursor_pos(2,2)
lcd.write(1)
lcd.set_cursor_pos(2,4)
lcd.write(2)
lcd.set_cursor_pos(2,6)
lcd.write(3)

time.sleep(3)
lcd.set_backlight(False)
time.sleep(1)
lcd.set_backlight(True)