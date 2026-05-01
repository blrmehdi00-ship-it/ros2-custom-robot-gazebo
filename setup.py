from setuptools import setup

package_name = 'my_robot_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'publisher = my_robot_project.target_publisher:main',
            'follower = my_robot_project.follower_node:main',
        ],
    },
)
