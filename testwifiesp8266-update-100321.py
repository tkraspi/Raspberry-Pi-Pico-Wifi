#tkraspilabs 2021

import os, sys
import utime
import machine

#print sys info
print(os.uname())

rx0=machine.Pin(1) #RPI PICO GPI1
tx0=machine.Pin(0) #RPI PICO GPI0 

#print uart info
uart = machine.UART(0, tx=tx0, rx=rx0, baudrate=115200,bits=8, parity=None, stop=1)
print(uart)

led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(0)     # onboard LED OFF for 0.5 sec
utime.sleep(0.5)
led_onboard.value(1)


def sendCMD_waitResp(cmd, uart=uart, timeout=2000):
    print("CMD: " + cmd)
    uart.write(cmd)
    waitResp(uart, timeout)
    print()
    
def waitResp(uart=uart, timeout=2000):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print("resp:")
    try:
        print(resp.decode())
    except UnicodeError:
        print(resp)           

            

waitResp()
sendCMD_waitResp("AT\r\n")
sendCMD_waitResp("AT+GMR\r\n")


utime.sleep(0.5)
sendCMD_waitResp("AT+RST\r\n") #RESET ESP8266

sendCMD_waitResp("AT\r\n")
sendCMD_waitResp("AT+CWJAP=\"SSDI NAME\",\"YOUR SSID PASSWORD\"r\n",  timeout=5000) #please check you ssid and password 
sendCMD_waitResp("AT+CIPSTATUS\r\n")
sendCMD_waitResp("AT+CIFSR\r\n")

print("connected........")
print("RPi-PICO with esp8266")
while True:
    if uart.any()>0:
      respon = uart.readline()
      print (respon)
      print ( "lose....." )
    

