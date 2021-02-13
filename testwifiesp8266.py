import os, sys
import utime
import machine

#print sys info
print(os.uname())

#indicate program started visually
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(0)     # onboard LED OFF for 0.5 sec
utime.sleep(0.5)
led_onboard.value(1)


#2 sec timeout is arbitrarily chosen
def sendCMD_waitResp(cmd, timeout=2000):
    print("CMD: " + cmd)
    uart.write(cmd.encode('utf-8'))
    waitResp(timeout)
    print()
    
def waitResp(timeout=2000):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print(resp)

def sendCMD_waitRespLine(cmd, timeout=2000):
    print("CMD: " + cmd)
    uart.write(cmd.encode('utf-8'))
    waitRespLine(timeout)
    print()
    
def waitRespLine(timeout=2000):
    prvMills = utime.ticks_ms()
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            print(uart.readline())
            

            
#print uart info
uart = machine.UART(0, baudrate=115200,bits=8, parity=None, stop=1)

print(uart)



waitResp()
sendCMD_waitResp("AT\r\n")
sendCMD_waitResp("AT+GMR\r\n")




utime.sleep(0.5)
sendCMD_waitResp("AT+RST\r\n") #reset the esp8266

sendCMD_waitResp("AT\r\n")

sendCMD_waitResp("AT+CIPSTATUS\r\n") #check status

sendCMD_waitResp("AT+CIFSR\r\n")
# check IP address of esp8266



print("connected........")
print("RPi-PICO with esp8266")
while True:
    if uart.any()>0:
      respon = uart.readline()
      print (respon)
      print ( "lose....." )
    
