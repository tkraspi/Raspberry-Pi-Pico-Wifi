# Raspberry Pi Pico Wifi
Raspberry Pi Pico Project

This is the modification from source code from Blog [Raspberry Pi Pico/MicroPython + HC-08 BLE 4.0 UART Module](https://helloraspberrypi.blogspot.com/2021/02/raspberry-pi-picomicropython-hc-08-ble.html)
I used uart communication between The Raspberry Pi Pico and ESP 8266. The AT command to communication with access point to ESP8266.
We can used any AT Command for ESP8266 like reset, reconnect and more.

Wire : 
RPi-Pico   ||   ESP8266

GP0 (TX) <----> GPIO1 (RX)

GP1 (RX) <----> GPIO0 (TX)

3V3(out) <----> VCC

3V3(out) <----> CH_EN

GND      <----> GND
 
