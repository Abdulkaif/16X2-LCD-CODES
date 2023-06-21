import utime
from machine import Pin,PWM,ADC
from gpio_lcd import GpioLcd
import utime

# LCD PART:

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

led = Pin(04, Pin.OUT)

ir_sensor = Pin(28, Pin.IN)

while True:
    lcd.clear()
    if (ir_sensor.value() == 0):
        lcd.putstr("Detected")
    else:
        lcd.putstr("Not detected")
        
    utime.sleep(0.2)
    
    
        