

class move_class():

    def init_head(self, serial):
        homing_string = "G28" + "\r\n"
        serial.write(homing_string.encode()) # homing

    def move_head(self, serial, x, y, z):
        move_string = "G0" + "X" + x + "Y" + y + "Z" + z + "\r\n"
        serial.write(move_string.encode())
