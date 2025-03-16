from machine import I2C
from MPU6050 import MPU6050
from time import sleep

mpu = MPU6050(I2C(0))

while True:
    # Accelerometer Data
    # accel = mpu.read_accel_data() # read the accelerometer [ms^-2]
    # aX = accel["x"]
    # aY = accel["y"]
    # aZ = accel["z"]
    # print("x: " + str(aX) + " y: " + str(aY) + " z: " + str(aZ))


    # Angle Data
    angle = mpu.read_angle()
    print(f"x:{str(angle['x'])} y:{str(angle['y'])}")

    # Gyroscope Data
    # gyro = mpu.read_gyro_data()   # read the gyro [deg/s]
    # gX = gyro["x"]
    # gY = gyro["y"]
    # gZ = gyro["z"]
    # print("x:" + str(gX) + " y:" + str(gY) + " z:" + str(gZ))

    # Rough Temperature
    temp = mpu.read_temperature()   # read the device temperature [degC]
    print("Temperature: " + str(temp) + "°C")

    # G-Force
    # gforce = mpu.read_accel_abs(g=True) # read the absolute acceleration magnitude
    # print("G-Force: " + str(gforce))
    
    sleep(0.5)
 
