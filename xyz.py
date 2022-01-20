import time

class move_class():

    def init_head(self, serial):
        homing_string = "G28" + "\r\n"
        print(homing_string)
        serial.write(homing_string.encode()) # homing

    def move_head(self, serial, x, y, z, f=1500):
        move_string = "G0" + "F" + str(f) + "X" + str(x) + "Y" + str(y) + "Z" + str(z) + "\r\n"
        print(move_string)
        serial.write(move_string.encode())
        time.sleep(5)
