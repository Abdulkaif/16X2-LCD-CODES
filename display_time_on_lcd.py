import DS1302
from machine import Pin,PWM
from time import sleep
from gpio_lcd import GpioLcd

# Creating PWM, PWM represents the contrast of the words written on the 16X2 display.
pwm = PWM(Pin(7))
pwm.freq(50)
pwm.duty_ns(1500000)

# Create the LCD object
lcd = GpioLcd(rs_pin=Pin(8),
              enable_pin=Pin(9),
              d4_pin=Pin(10),
              d5_pin=Pin(11),
              d6_pin=Pin(12),
              d7_pin=Pin(13),
              num_lines=2, num_columns=16)

# Initializing Pins for Clk,Dat,Rst
ds = DS1302.DS1302(clk=Pin(0), dio=Pin(1), cs=Pin(2))

# this returns the already running date time
ds.date_time()

""" this is used to set the date time but no need to run it every time because once you have save the datetime
then it can last upto 30days in the cmos battery so just use ds.date_time() to get back previous time which is 
running till now"""
#ds.date_time([2022,11,12,02,20,30])

# this start the clock
ds.start()

print(type(ds.month()))
while True:
    # Printing time on the LCD
    lcd.clear()
    lcd.move_to(0,0)
    print(f"Time: {str(ds.hour())}:{str(ds.minute())}:{str(ds.second())}")
    lcd.putstr(f"Time: {str(ds.hour())}:{str(ds.minute())}:{str(ds.second())}")
    lcd.move_to(0,1)
    print(f"Date: {str(ds.day())}/{str(ds.month())}/{str(ds.year())}")
    lcd.putstr(f"Date: {str(ds.day())}/{str(ds.month())}/{str(ds.year())}")
    sleep(1)