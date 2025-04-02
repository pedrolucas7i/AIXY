from gpiozero import Motor as Motors, DistanceSensor, PWMSoftwareFallback

if __name__ == '__main__':
    servo = Servo()
    servo.setServoAngle('1', 90)
    servo.setServoAngle('0', 150)