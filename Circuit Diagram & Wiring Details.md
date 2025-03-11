 Circuit Diagram & Wiring Details
 **Connections to Raspberry Pi Pico:**
- **MPU6050 (I2C):**
  - VCC → 3.3V (Pico)
  - GND → GND (Pico)
  - SDA → GP20
  - SCL → GP21

- **BMP280 (I2C):**
  - VCC → 3.3V (Pico)
  - GND → GND (Pico)
  - SDA → GP22
  - SCL → GP23

- **SG90 Servo Motors (PWM Control for TVC):**
  - Servo 1 (Pitch) → GP16 (PWM)
  - Servo 2 (Yaw) → GP17 (PWM)
  - Servo VCC → External 5V (Regulated)
  - Servo GND → GND (Pico)

- **LoRa Module (SPI/UART):**
  - VCC → 3.3V (Pico)
  - GND → GND (Pico)
  - MOSI → GP10
  - MISO → GP11
  - SCK → GP12
  - CS → GP13
  - RST → GP14

- **LiPo Battery:**
  - Connected through **Step-down Regulator** (11.1V to 5V)
  - 5V Output → Powers Pico & sensors
  - 11.1V Direct → Powers servos
