import serial


class PySerial:
    def __init__(self, port='/dev/serial0', timeout=1):
        self.port = port
        self.ser = serial.Serial(self.port, 9600, timeout=timeout)
        print("serial connected")

    def read_line(self):
        line = self.ser.readline().decode('utf-8').replace("\r\n", "")
        linesplit = line.split("|")
        return linesplit

    def write(self, message):
        self.ser.write(message.encode('utf-8'))

    def close_conn(self):
        self.ser.close()
