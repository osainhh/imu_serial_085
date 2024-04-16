from setuptools import find_packages, setup

package_name = 'imu_serial_085'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nishi',
    maintainer_email='nishicrycat@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'imu_serial = imu_serial_085.imu_serial:main'
        ],
    },
    py_modules=["imu_serial_085.bno085"]
)
