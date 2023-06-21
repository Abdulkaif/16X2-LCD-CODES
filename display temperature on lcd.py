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


# TEMPERATURE PART:


temp_sensor = ADC(4) # Defauclt connection of on board temperature sensor

while True:
    #get raw sensor data
    raw_sensor_data = temp_sensor.read_u16()
    
    # convert raw value to equivalent voltage
    sensor_voltage = (raw_sensor_data / 65535)*3.3
    
    # convert voltage to temperature (celcius)
    temperature = 27 - (sensor_voltage - 0.706)/0.001721

    lcd.putstr(f": Temperature : {round(temperature,2)}° celcius")
    print(f"Temperature : {round(temperature,2)}° celcius")
    utime.sleep(1)
    lcd.clear()
    
    