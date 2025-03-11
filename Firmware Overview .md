Firmware Overview & MicroPython Code
The firmware reads sensor data, processes flight dynamics, and controls servos for **TVC stabilization**. Key functions include:
- **Sensor Fusion Algorithm**: Madgwick/Kalman for accurate orientation
- **PID Controller**: Adjusts servos for stability
- **Telemetry & Logging**: Sends real-time data via LoRa
- **Failsafe Handling**: Emergency cut-off for anomalies