import RPi.GPIO as GPIO
import time

class Servo_class:
  def __init__(self, servoPIN , frequency = 50):
    self.servoPIN = servoPIN
    self.pwm = GPIO.PWM(servoPIN, frequency)
    self.GPIO = GPIO
  def move(self):

    self.GPIO.setmode(GPIO.BCM)
    self.GPIO.setup(self.servoPIN, GPIO.OUT)
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
    self.GPIO.cleanup()

  def servo_interrupt(self):
    self.pwm.stop()
    self.GPIO.cleanup()

# comment

