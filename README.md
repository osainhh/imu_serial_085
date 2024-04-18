# IMU_SERIAL_085 ROS2 package
BNO085+ESP32C3で構成されたIMUモジュールをROS2 Humbleで利用するためのパッケージです．
IMUを接続後，Nodeを起動してください．

## Install
### ros2ワークスペース/src に配置後，colconでビルド
$ colcon build --packages-select imu_serial_085

### USBシリアル権限の自動付与
/lib/udev/rules.d/50-udev-default.rules

該当箇所を以下に変更\
KERNEL=="tty[A-Z]*[0-9]|pppox[0-9]*|ircomm[0-9]*|noz[0-9]*|rfcomm[0-9]*", GROUP="dialout", MODE="0666"

## Usage
IMUを接続後，ノードを立ち上げ

$ ros2 run imu_serial_085 imu_serial

成功すればtopicにIMUデータが流れてきます．

$ ros2 topic echo /sensor/bno085/Imu

$ ros2 topic echo /sensor/bno085/MagF

$ ros2 topic echo /sensor/bno085/Angle
- Roll，Pitch，Yaw (degrees)

### topic種別
- Rotation，Gyro, Accel: sensor_msgs.msg Imu  /sensor/bno085/Imu
- MagneticField: sensor_msgs.msg MagneticField  /sendor/bno085/MagF
- Angle: geometry_msgs.msg Vector3  /sensor/bno085/Angle

### Angle角度
水平状態において，Yaw=0°の時ケース矢印が北を指します．