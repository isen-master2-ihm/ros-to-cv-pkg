from setuptools import setup

package_name = 'ros_bridge_cv'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mael',
    maintainer_email='mael.lemaire@student.junia.com',
    description='using opencv inside ROS environment',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'converter = ros_bridge_cv.link:main',
        ],
    },
)
