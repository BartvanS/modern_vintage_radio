import pySerial
import os
import time
serial = None

try:
    serial = pySerial.PySerial('COM3')
    connected = True
except:
    print("could not connect serial")


def parse_msg(volume):
    if len(volume) == 0:
        return
    command = 'sudo amixer cset numid=1 ' + str(volume) + '%'
    print(command)
    # os.system(command)


if __name__ == '__main__':
    while True:
        if serial.ser.inWaiting():
            line = serial.read_line()
            parse_msg(line)
        # print("sending test")

