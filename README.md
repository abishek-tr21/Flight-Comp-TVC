🚀 Flight Computer with Thrust Vector Control (TVC)
📝 Project Overview
This is a Raspberry Pi Pico-based flight computer designed for model rockets with Thrust Vector Control (TVC). It stabilizes the rocket by dynamically adjusting the nozzle position using SG90 servo motors based on real-time IMU (MPU6050) data. The system also includes a BMP280 altimeter for altitude tracking and a LoRa module for wireless telemetry transmission.

📌 Features
Thrust Vector Control (TVC) using SG90 servos
Real-time orientation detection via MPU6050 IMU
Altitude & Barometric Pressure monitoring using BMP280
Wireless telemetry transmission using LoRa
Custom 3D-printed TVC mount & PCB integration
MicroPython-based firmware with PID stabilization
🔧 Components List
Microcontroller: Raspberry Pi Pico
IMU Sensor: MPU6050
Servo Motors: 2x SG90 (for TVC)
Power Source: LiPo battery (3S 11.1V)
Voltage Regulator: Step-down 5V
Altimeter & Barometer: BMP280
Communication: LoRa Module (SPI)
PCB: Custom-designed for component integration
🔄 Working Principle
IMU detects angular deviations of the rocket.
Flight computer processes data & calculates corrections.
Servo motors adjust nozzle angle to maintain stability.
BMP280 measures altitude and pressure changes.
LoRa transmits real-time telemetry to a ground station.
🛠 Circuit Diagram & Connections
✅ Schematic & PCB Gerber files are included!

🔌 Wiring
MPU6050 (I2C: GP20, GP21)
BMP280 (I2C: GP22, GP23)
SG90 Servos (PWM: GP16, GP17)
LoRa Module (SPI: GP10-GP14)
LiPo Battery with Step-Down Regulator (5V & 11.1V)
🖥 Firmware
Implemented in MicroPython
Uses PID control for stability
Supports real-time telemetry over LoRa
Efficient low-power operation
📜 Code is included in the repository!

🔍 Future Improvements
✅ GPS Tracking for better positioning
✅ Higher power servos for increased control
✅ Advanced AI-based flight optimization

⚡ This project is designed for hobbyists, students, and space enthusiasts who want to explore TVC in model rocketry!