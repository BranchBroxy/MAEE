import serial
import time
from servo import Servo_class
from datetime import datetime


def serial_handler_1(ser):
    print(ser.name)  # check which port was really used
    time.sleep(10)      # sleep 10 sec
    message = "M117 MAEE ready\r\n"
    ser.write(message.encode())
    # ser.write(b"M117 Helloy\r\n")
    time.sleep(2) # sleep 2 sec
    #servo()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    time.sleep(1)
    ser.close()

move_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
move_list_min = ["50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]
move_list_sec = ["00"]

def serial_handler(ser, servo_motor):
    # servo()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_hour = now.strftime("%H")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")

    if current_min in move_list_min and current_sec in move_list_sec:
        print("Minute:" + current_min)
        print("Sekunde:" + current_sec)
        print("Servo move")
        servo_motor.move_angle(10)
        time.sleep(1)
        servo_motor.move_angle(0)
    else:
        time_message = "M117 " + current_time + "\r\n"
        ser.write(time_message.encode())
        print("Current Time =", current_time)
        time.sleep(1)

try:
    ser = serial.Serial('/dev/ttyUSB0', 250000)  # open serial port
    servo_motor = Servo_class(17)
    print(ser.name)  # check which port was really used
    time.sleep(10)      # sleep 10 sec
    message = "M117 MAEE ready\r\n"
    ser.write(message.encode())
    # ser.write(b"M117 Helloy\r\n")
    time.sleep(2)  # sleep 2 sec
    while True:
        serial_handler(ser, servo_motor)
        # comment

except KeyboardInterrupt:
    servo_motor.servo_interrupt()
    ser.close()