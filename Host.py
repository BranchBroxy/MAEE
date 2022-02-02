import serial
import time
from servo import Servo_class
from datetime import datetime
from xyz import move_class

move_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
move_list_hour = ["12", "16"]
move_list_min = ["00"]
# move_list_min = list(range(00, 60))
# move_list_min = ''.join(str(e) for e in move_list_min)
move_list_sec = ["00"]
move_list_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# move_list_day = ["Monday", "Wednesday", "Friday", "Sunday"]

def serial_handler(ser, servo_motor, head):
    # servo()
    now = datetime.now()
    current_day = now.strftime("%A")
    current_time = now.strftime("%H:%M:%S")
    current_hour = now.strftime("%H")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")

    if current_min in move_list_min and current_sec in move_list_sec and current_day in move_list_day and current_hour in move_list_hour:
        print("Minute:" + current_min)
        print("Sekunde:" + current_sec)
        print("Servo move")
        #servo_motor.move_duty_cycle(1)
        #time.sleep(1)

        # Empty first MEA
        head.move_head(ser, x=100, y=100, z=25, f=1000) # x=85, y=85, z=25, f=3000
        servo_motor.first_push()
        time.sleep(5)
        head.move_head(ser, x=100, y=100, z=7, f=1000)
        time.sleep(5)
        servo_motor.zero_pos()
        time.sleep(2)
        head.move_head(ser, x=100, y=100, z=25, f=1000)
        time.sleep(5)

        # Medium Dump
        head.move_head(ser, x=180, y=180, z=25, f=1000)
        time.sleep(4)
        head.move_head(ser, x=180, y=180, z=15, f=1000)
        time.sleep(10)
        servo_motor.first_push()
        time.sleep(2)
        servo_motor.second_push()
        time.sleep(2)
        head.move_head(ser, x=180, y=180, z=25, f=1000)
        time.sleep(10)
        servo_motor.zero_pos()
        time.sleep(2)

        # Medium Load
        head.move_head(ser, x=40, y=40, z=25, f=1000)
        time.sleep(8)
        servo_motor.first_push()
        time.sleep(4)
        head.move_head(ser, x=40, y=40, z=7, f=1000)
        time.sleep(10)
        servo_motor.zero_pos()
        time.sleep(2)
        head.move_head(ser, x=40, y=40, z=25, f=1000)
        time.sleep(10)

        # First MEA
        head.move_head(ser, x=100, y=100, z=25, f=1000)
        time.sleep(8)
        head.move_head(ser, x=100, y=100, z=7, f=1000)
        time.sleep(10)
        servo_motor.push_routine()
        time.sleep(4)
        head.move_head(ser, x=100, y=100, z=25, f=1000)
        time.sleep(10)
        servo_motor.zero_pos()
        time.sleep(4)



        ########### Second MEA #################
        # Empty second MEA
        head.move_head(ser, x=150, y=100, z=25, f=1000) # x=135, y=85, z=25, f=3000
        servo_motor.first_push()
        time.sleep(4)
        head.move_head(ser, x=150, y=100, z=7, f=1000)
        time.sleep(10)
        servo_motor.zero_pos()
        time.sleep(4)
        head.move_head(ser, x=150, y=100, z=25, f=1000)
        time.sleep(10)

        # Medium Dump
        head.move_head(ser, x=180, y=180, z=25, f=1000)
        head.move_head(ser, x=180, y=180, z=15, f=1000)
        time.sleep(10)
        servo_motor.first_push()
        time.sleep(2)
        servo_motor.second_push()
        time.sleep(2)
        head.move_head(ser, x=180, y=180, z=25, f=1000)
        time.sleep(10)
        servo_motor.zero_pos()
        time.sleep(2)

        # Medium Load
        head.move_head(ser, x=40, y=40, z=25, f=1000)
        time.sleep(8)
        servo_motor.first_push()
        time.sleep(4)
        head.move_head(ser, x=40, y=40, z=7, f=1000)
        time.sleep(10)
        servo_motor.zero_pos()
        time.sleep(2)
        head.move_head(ser, x=40, y=40, z=25, f=1000)
        time.sleep(10)

        # Second MEA
        head.move_head(ser, x=150, y=100, z=25, f=1000)
        time.sleep(8)
        head.move_head(ser, x=150, y=100, z=7, f=1000)
        time.sleep(10)
        servo_motor.push_routine()
        time.sleep(4)
        head.move_head(ser, x=150, y=100, z=25, f=1000)
        time.sleep(10)
        servo_motor.zero_pos()
        time.sleep(4)

        # Zero Pos
        head.move_head(ser, x=50, y=50, z=25, f=1000)
        servo_motor.zero_pos()


    else:
        time_message = "M117 " + current_time + "\r\n"
        ser.write(time_message.encode())
        # print("Current Time =", current_time)
        time.sleep(1)

try:
    ser = serial.Serial('/dev/ttyUSB0', 250000)  # open serial port
    servo_motor = Servo_class(servoPIN=17)
    head = move_class()
    head.init_head(serial=ser)
    print(ser.name)  # check which port was really used
    print(move_list_min)
    time.sleep(30)      # sleep 10 sec
    message = "M117 MAEE ready\r\n"
    ser.write(message.encode())
    # ser.write(b"M117 Helloy\r\n")
    time.sleep(2)  # sleep 2 sec
    while True:
        serial_handler(ser, servo_motor, head)
        # comment

except KeyboardInterrupt:
    servo_motor.servo_interrupt()
    ser.close()