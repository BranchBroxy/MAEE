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
    self.pwm.start(5) # Initialisierung
    self.pwm.ChangeDutyCycle(0)
    time.sleep(1)
    self.pwm.ChangeDutyCycle(5)
    time.sleep(1)
    self.pwm.ChangeDutyCycle(10)
    time.sleep(1)
    self.pwm.ChangeDutyCycle(5)
    time.sleep(1)
    self.pwm.stop()
    GPIO.cleanup()

  def move_duty_cycle(self, angle):
    self.pwm.start(0)  # Initialisierung
    time.sleep(0.2)
    self.pwm.ChangeDutyCycle(angle)
    time.sleep(0.5)
    self.pwm.stop()
    GPIO.cleanup()

  def servo_interrupt(self):
    self.pwm.stop()
    GPIO.cleanup()

# comment

