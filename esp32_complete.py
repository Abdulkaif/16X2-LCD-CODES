import usocket as socket
import time
import network
from machine import Pin,PWM
from gpio_lcd import GpioLcd

pwm = PWM(Pin(23))
pwm.freq(50)
pwm.duty_ns(1500000)

# Create the LCD object
lcd = GpioLcd(rs_pin=Pin(22),
              enable_pin=Pin(1),
              d4_pin=Pin(15),
              d5_pin=Pin(8),
              d6_pin=Pin(7),
              d7_pin=Pin(6),
              num_lines=2, num_columns=16)


lcd.putstr("Starting...")

timeout = 0 # WiFi Connection Timeout variable 

wifi = network.WLAN(network.STA_IF)

# Restarting WiFi
wifi.active(False)
time.sleep(0.5)
wifi.active(True)

wifi.connect('WIFI_786','WIFI_786786')

if not wifi.isconnected():
    print('connecting..')
    while (not wifi.isconnected() and timeout < 5):
        print(5 - timeout)
        timeout = timeout + 1
        time.sleep(1)
        
if(wifi.isconnected()):
    print('Connected...')
    print('network config:', wifi.ifconfig())
    lcd.putstr(str(wifi.ifconfig()))
    
# HTML Document

html='''<!DOCTYPE html>
<html>
<center><h2>ESP32 Webserver </h2></center>
<form>
#<center>
<h3> LED_BEDROOM </h3>
<button name="LED" value='ON' type='submit'>  ON </button>
<button name="LED" value='OFF' type='submit'> OFF </button>
<h3> LED_KITCHEN </h3>
<button name="LED" value='ON' type='submit'>  ON </button>
<button name="LED" value='OFF' type='submit'> OFF </button>
<h3> LED_HALL </h3>
<button name="LED" value='ON' type='submit'>  ON </button>
<button name="LED" value='OFF' type='submit'> OFF </button>
<h3> BUZZER </h3>
<button name="LED" value='ON' type='submit'>  ON </button>
<button name="LED" value='OFF' type='submit'> OFF </button>
#</center>
'''

# Output Pin Declaration 
LED = Pin(2,Pin.OUT)
LED_BEDROOM = Pin(0, Pin.OUT)
LED_KITCHEN = Pin(4, Pin.OUT)
LED_HALL = Pin(16, Pin.OUT)
BUZZER = Pin(17, Pin.OUT)
LED.value(0)
LED_BEDROOM.value(0)
LED_KITCHEN.value(0)
LED_HALL.value(0)
BUZZER.value(0)

# Initialising Socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET - Internet Socket, SOCK_STREAM - TCP protocol

Host = '' # Empty means, it will allow all IP address to connect
Port = 80 # HTTP port
s.bind((Host,Port)) # Host,Port

s.listen(5) # It will handle maximum 5 clients at a time

# main loop
while True:
  connection_socket,address=s.accept() # Storing Conn_socket & address of new client connected
  print("Got a connection from ", address)
  request=connection_socket.recv(1024) # Storing Response coming from client
  print("Content ", request) # Printing Response 
  request=str(request) # Coverting Bytes to String
  # Comparing & Finding Postion of word in String 
  LED_ON =request.find('/?LED=ON')
  LED_OFF =request.find('/?LED=OFF')
  LED_BEDROOM_ON = request.find('/?LED_BEDROOM=ON')
  LED_BEDROOM_OFF = request.find('/?LED_BEDROOM=OFF')
  LED_KITCHEN_ON = request.find('/?LED_KITCHEN=ON')
  LED_KITCHEN_OFF = request.find('/?LED_KITCHEN=OFF')
  LED_HALL_ON = request.find('/?LED_HALL =ON')
  LED_HALL_OFF = request.find('/?LED_HALL =OFF')
  BUZZER_ON = request.find('/?LED_HALL =ON')
  BUZZER_OFF = request.find('/?LED_HALL =OFF')
  
  if(LED_ON ==6):
    LED.value(1)  
    
  if(LED_OFF ==6):
    LED.value(0)
    
  if(LED_BEDROOM_ON ==6):
    LED.value(1)  
    
  if(LED_BREDROOM_OFF ==6):
    LED.value(0)
    
  if(LED_HALL_ON ==6):
    LED.value(1) 
    
  if(LED_HALL_OFF ==6):
    LED.value(0)
    
  if(LED_KITCHEN_ON ==6):
    LED.value(1)  
    
  if(LED_KITCHEN_OFF ==6):
    LED.value(0)
    
  if(BUZZER_ON ==6):
    LED.value(1) 
    
  if(BUZZER_OFF ==6):
    LED.value(0)
    
  
    
  # Sending HTML document in response everytime to all connected clients  
  response=html 
  connection_socket.send(response)
  
  #Closing the socket
  connection_socket.close() 