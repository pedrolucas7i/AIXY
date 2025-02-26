# Import the Motor class from the gpiozero library
from gpiozero import Motor
from time import sleep
import env

# Define the tankMotor class to control the motors of a tank-like robot
class Motor:
    
    def __init__(self):
        """Initialize the tankMotor class with GPIO pins for the left and right motors."""
        self.left_motor = Motor(23, 24)  # Initialize the left motor with GPIO pins 23 and 24
        self.right_motor = Motor(6, 5)   # Initialize the right motor with GPIO pins 6 and 5

    def duty_range(self, duty1, duty2):
        """Ensure the duty cycle values are within the valid range (-4095 to 4095)."""
        if duty1 > 4095:
            duty1 = 4095     # Cap the value at 4095 if it exceeds the maximum
        elif duty1 < -4095:
            duty1 = -4095    # Cap the value at -4095 if it falls below the minimum
        
        if duty2 > 4095:
            duty2 = 4095     # Cap the value at 4095 if it exceeds the maximum
        elif duty2 < -4095:
            duty2 = -4095    # Cap the value at -4095 if it falls below the minimum
        
        return duty1, duty2  # Return the clamped duty cycle values

    def left_Wheel(self, duty):
        """Control the left wheel based on the duty cycle value."""
        if duty > 0:
            self.left_motor.forward(duty / 4096)    # Move the left motor forward
        elif duty < 0:
            self.left_motor.backward(-duty / 4096)  # Move the left motor backward
        else:
            self.left_motor.stop()                  # Stop the left motor

    def right_Wheel(self, duty):
        """Control the right wheel based on the duty cycle value."""
        if duty > 0:
            self.right_motor.forward(duty / 4096)    # Move the right motor forward
        elif duty < 0:
            self.right_motor.backward(-duty / 4096)  # Move the right motor backward
        else:
            self.right_motor.stop()                  # Stop the right motor

    def setMotorModel(self, duty1, duty2):
        """Set the duty cycle for both motors and ensure they are within the valid range."""
        duty1, duty2 = self.duty_range(duty1, duty2)  # Clamp the duty cycle values
        self.left_Wheel(duty1)   # Control the left wheel
        self.right_Wheel(duty2)  # Control the right wheel
        
    def driveForward(self, speedLevel=1):
        """Drive Forward with diferent speed levels"""
        pwm_value = 1200
        
        if speedLevel == 2:
            pwm_value = 2640
        elif speedLevel == 3:
            pwm_value = 4000
        
        self.setMotorModel(pwm_value + env.LEFT_MOTOR_CORRECTION_PWM_VALUE, pwm_value + env.RIGHT_MOTOR_CORRECTION_PWM_VALUE)
        
    def driveLeft(self, turnLevel=1):
        """Drive Left with diferent turn levels"""
        left_pwm = 2640
        right_pwm = 4000
        
        if turnLevel == 2:
            left_pwm = 1200
            right_pwm = 4000
        elif turnLevel == 3:
            left_pwm = 0
            right_pwm = 2640
        elif turnLevel == 4:
            left_pwm = -1200
            right_pwm = 1200
        
        self.setMotorModel(left_pwm + env.LEFT_MOTOR_CORRECTION_PWM_VALUE, right_pwm + env.RIGHT_MOTOR_CORRECTION_PWM_VALUE)
        
    def driveRight(self, turnLevel=1):
        """Drive Right with diferent turn levels"""
        left_pwm = 4000
        right_pwm = 2640
        
        if turnLevel == 2:
            left_pwm = 4000
            right_pwm = 1200
        elif turnLevel == 3:
            left_pwm = 2640
            right_pwm = 0
        elif turnLevel == 4:
            left_pwm = 1200
            right_pwm = -1200
        
        self.setMotorModel(left_pwm + env.LEFT_MOTOR_CORRECTION_PWM_VALUE, right_pwm + env.RIGHT_MOTOR_CORRECTION_PWM_VALUE)
        
    def driveBackward(self, speedLevel=1):
        """Drive Backward with diferent speed levels"""
        pwm_value = -1200
        
        if speedLevel == 2:
            pwm_value = -2640
        elif speedLevel == 3:
            pwm_value = -4000
        
        self.setMotorModel(pwm_value - env.LEFT_MOTOR_CORRECTION_PWM_VALUE, pwm_value - env.RIGHT_MOTOR_CORRECTION_PWM_VALUE)
    
    def close(self):
        """Close the motors to release resources."""
        self.left_motor.close()   # Close the left motor
        self.right_motor.close()  # Close the right motor

# Main program logic follows:
if __name__ == '__main__':
    print('MOTOR TESTING STARTED ... \n')  # Print a start message
    motor = Motor()                        # Create an instance of the tankMotor class

    try:
        motor.driveLeft(4)
        sleep(0.35)
        motor.driveRight(4)
        sleep(0.35)
        motor.driveForward(1)
        sleep(0.2)
        motor.driveBackward(1)
        sleep(0.2)
    except KeyboardInterrupt:              # Handle a keyboard interrupt (Ctrl+C)
        motor.setMotorModel(0, 0)          # Stop both motors
        motor.close()                      # Close the motors to release resources