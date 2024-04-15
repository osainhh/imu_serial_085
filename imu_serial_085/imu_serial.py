import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu, MagneticField
from geometry_msgs.msg import Vector3
import subprocess

from .bno085 import BNO085

class Imu085(Node):
    def __init__(self, time_interval=1.0):
        super().__init__('imu_serial')
        self.pub_imu = self.create_publisher(Imu, '/sensor/bno085/Imu', 10)
        self.pub_mag = self.create_publisher(MagneticField, '/sensor/bno085/MagF', 10)
        self.pub_ang = self.create_publisher(Vector3, '/sensor/bno085/Angle', 10)
        self.tmr = self.create_timer(time_interval, self.callback)
        subprocess.call("sudo chmod 777 /dev/ttyACM0", shell=True)
        self.imu_sensor = BNO085("/dev/ttyACM0")
    
    def callback(self):
        msg_imu = Imu()
        msg_mag = MagneticField()
        msg_ang = Vector3()

        # BNO085 getData

        msg_imu.orientation.x = quat[0]
        msg_imu.orientation.y = quat[1]
        msg_imu.orientation.z = quat[2]
        msg_imu.orientation.w = quat[3]
        msg_imu.angular_velocity.x = velocity[0]
        msg_imu.angular_velocity.y = velocity[1]
        msg_imu.angular_velocity.z = velocity[2]
        msg_imu.linear_acceleration.x = accel[0]
        msg_imu.linear_acceleration.y = accel[1]
        msg_imu.linear_acceleration.z = accel[2]
        self.pub_imu.publish(msg_imu)

        msg_mag.magnetic_field.x = float(magnetic[0])
        msg_mag.magnetic_field.y = float(magnetic[1])
        msg_mag.magnetic_field.z = float(magnetic[2])
        self.pub_mag.publish(msg_mag)

        msg_ang.x = angle[0]
        msg_ang.y = angle[1]
        msg_ang.z = angle[2]
        self.pub_ang.publish(msg_ang)


def main(args=None):
    print('BNO085 Node test')
    
    rclpy.init(args=args)
    node_imu_serial_085 = Imu085(time_interval=0.01)
    rclpy.spin(node_imu_serial_085)

    node_imu_serial_085.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
