import board, busio

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

custom_char = bytearray((
    0b00000,
    0b00100,
    0b01110,
    0b01110,
    0b00000,
    0b00000,
    0b00000,
    0b00000
))

sda, scl = board.GP0, board.GP1
i2c = busio.I2C(scl, sda)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=4, num_cols=20)

lcd.print("Hello world!")

lcd.set_cursor_pos(1,5)
lcd.print("A new text")

lcd.create_char(0,custom_char)
lcd.write(0)