from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    urdf_path = os.path.join(
        get_package_share_directory('my_robot_project'),
        'urdf',
        'robot.urdf'
    )

    return LaunchDescription([

        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'my_robot', '-file', urdf_path]
        ),

        Node(
            package='my_robot_project',
            executable='publisher'
        ),

        Node(
            package='my_robot_project',
            executable='follower'
        ),
    ])
