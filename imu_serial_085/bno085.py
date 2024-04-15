from serial import Serial
import time
import numpy as np

class BNO085(Serial):
    def __init__(self, Port):
        self.imu_serial = super().__init__(Port, baudrate=115200, timeout=1)
        
        self.quat_i=0.0
        self.quat_j = 0.0
        self.quat_k = 0.0
        self.quat_r = 0.0

        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.velocity_z = 0.0

        self.accel_x = 0.0
        self.accel_y = 0.0
        self.accel_z = 0.0

        self.angle_x = 0.0
        self.angle_y = 0.0
        self.angle_z = 0.0

        self.magnetic_x = 0.0
        self.magnetic_y = 0.0
        self.magnetic_z = 0.0
        


    def _readData(self):
        try:
            super(BNO085, self).flushInput()
            noUse = super(BNO085, self).readline()
            imu_msg = super(BNO085, self).readline().strip().decode('utf-8')
            imu_data = imu_msg.split(",")
            self.quat_i = float(imu_data[0])
            self.quat_j = float(imu_data[1])
            self.quat_k = float(imu_data[2])
            self.quat_r = 0.0

            self.velocity_x = float(imu_data[4])
            self.velocity_y = float(imu_data[5])
            self.velocity_z = float(imu_data[6])

            self.accel_x = float(imu_data[8])
            self.accel_y = float(imu_data[9])
            self.accel_z = float(imu_data[10])

            self.angle_x = 0.0
            self.angle_y = 0.0
            self.angle_z = 0.0

            self.magnetic_x = float(imu_data[12])
            self.magnetic_y = float(imu_data[13])
            self.magnetic_z = float(imu_data[14])
        
            
        except KeyboardInterrupt:
            super(BNO085, self).close()
    
    def getData(self):
        self._readData()
        return (self.quat_i, self.quat_k, self.quat_k, self.quat_r), \
               (self.velocity_x, self.velocity_y, self.velocity_z), \
               (self.accel_x, self.accel_y, self.accel_z), \
               (self.angle_x, self.angle_y, self.angle_z), \
               (self.magnetic_x, self.magnetic_y, self.magnetic_z)        

if __name__ =="__main__":
    sensor = BNO085("/dev/ttyACM0")
    while True:
        time.sleep(0.1)
        print(sensor.getData())