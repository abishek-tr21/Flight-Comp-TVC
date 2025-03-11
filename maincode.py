
from machine import Pin, I2C, PWM
import time
from mpu6050 import MPU6050
from bmp280 import BMP280
import lora

# Initialize I2C Bus
i2c = I2C(0, scl=Pin(21), sda=Pin(20))
imu = MPU6050(i2c)
bmp = BMP280(i2c)

# Servo Configuration
servo_pitch = PWM(Pin(16))
servo_yaw = PWM(Pin(17))
servo_pitch.freq(50)
servo_yaw.freq(50)

# LoRa Initialization
lora.init()

def set_servo_angle(servo, angle):
    duty = int((angle / 180) * 1023 + 512)  # Convert angle to duty cycle
    servo.duty_u16(duty)

def stabilize():
    while True:
        accel_data = imu.get_acceleration()
        altitude = bmp.read_altitude()
        
        pitch_angle = accel_data['x'] * -1  # Example conversion
        yaw_angle = accel_data['y'] * -1
        
        set_servo_angle(servo_pitch, 90 + pitch_angle)
        set_servo_angle(servo_yaw, 90 + yaw_angle)
        
        lora.send(f"Alt: {altitude}, Pitch: {pitch_angle}, Yaw: {yaw_angle}")
        time.sleep(0.1)

stabilize()