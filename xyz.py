

class move_class():

    def init_head(self, serial):
        serial.write("G28") # homing

    def move_head(self, serial, x, y, z):
        move_string = "G0" + "X" + x + "Y" + y + "Z" + z
        serial.write(move_string)
