import RPi.GPIO as GPIO
import time
def servo():

  servoPIN = 17
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPIN, GPIO.OUT)

  p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
  p.start(5) # Initialisierung
  try:
    p.ChangeDutyCycle(0)
    time.sleep(1)
    p.ChangeDutyCycle(5)
    time.sleep(1)
    p.ChangeDutyCycle(10)
    time.sleep(1)
    p.ChangeDutyCycle(5)
    time.sleep(1)
    p.stop()
    GPIO.cleanup()

  except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

# comment