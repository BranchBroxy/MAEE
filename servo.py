import RPi.GPIO as GPIO
import time

class Servo_class:
  def __init__(self, servoPIN , frequency = 50):
    self.servoPIN = servoPIN
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.servoPIN, GPIO.OUT)
    self.pwm = GPIO.PWM(servoPIN, frequency)
    # self.GPIO = GPIO

  def move(self):
    # p =  # GPIO 17 als PWM mit 50Hz
    self.pwm.start(2.5) # Initialisierung
    self.pwm.ChangeDutyCycle(0)
    time.sleep(1)
    self.pwm.ChangeDutyCycle(5)
    time.sleep(1)
    self.pwm.ChangeDutyCycle(10)
    time.sleep(1)
    self.pwm.ChangeDutyCycle(5)
    time.sleep(1)
    self.pwm.stop()
    GPIO.cleanup() #not

  def move_duty_cycle(self, duty_cycle):
    self.pwm.start(2.5)  # Initialisierung
    print("Here")
    # time.sleep(0.2)
    self.pwm.ChangeDutyCycle(duty_cycle)
    # time.sleep(0.5)
    # self.pwm.stop()
    # GPIO.cleanup()

  def move_angle(self, angle):
    self.pwm.start(2.5)  # Initialisierung
    # print("Here")
    duty_cycle = 1/18 * angle + 2.5
    # time.sleep(0.2)
    self.pwm.ChangeDutyCycle(duty_cycle)
    # time.sleep(0.5)
    # self.pwm.stop()
    # GPIO.cleanup()

  def servo_interrupt(self):
    self.pwm.stop()
    GPIO.cleanup()

  def first_push(self):
    self.move_angle(117)

  def second_push(self):
    self.move_angle(137)

  def zero_pos(self):
    self.move_angle(0)

  def push_routine(self):
    self.zero_pos()
    time.sleep(2)
    self.first_push()
    time.sleep(2)
    self.second_push()
    time.sleep(2)
    # self.zero_pos()

  def pull_routine(self):
    self.first_push()
    time.sleep(2)


# comment

