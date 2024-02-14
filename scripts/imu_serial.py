import serial
import time

esp = serial.Serial(port='/dev/ttyUSB0',baudrate=115200, timeout=0.1)

def write_read(x):
    esp.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = esp.readline()
    return data

while True:
    num = input("Enter a number: ")
    value = write_read(num)
    print(value)