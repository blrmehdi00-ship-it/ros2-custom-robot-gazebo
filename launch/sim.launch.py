from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():

    return LaunchDescription([

        ExecuteProcess(
            cmd=['gazebo', '--verbose'],
            output='screen'
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'my_robot', '-file',
                       os.path.join(os.getcwd(), 'src/my_robot_project/urdf/robot.urdf')]
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
