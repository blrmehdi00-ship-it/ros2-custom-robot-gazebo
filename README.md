 🤖 ROS2 Custom Robot with Gazebo

📌 Project Overview

This project is a simple robotics simulation using ROS 2 and Gazebo.

A mobile robot is created using a custom URDF model.  
The robot moves inside Gazebo and follows a randomly generated target.

The system is based on ROS 2 nodes:
- A publisher node generates a target position
- A follower node controls the robot movement
- A launch file starts everything in Gazebo



⚙️ System Architecture

The project contains 3 main parts:

 1. 🧠 Target Publisher
- Generates random target values
- Publishes them on `/target_position`

 2. 🤖 Robot Controller (Follower)
- Reads target values
- Sends movement commands to `/cmd_vel`
- Controls robot direction and speed

 3. 🚀 Gazebo Simulation
- Loads the robot URDF model
- Simulates movement in a virtual environment

- ---

 How to Run

```bash
git clone https://github.com/USERNAME/ros2-custom-robot-gazebo
cd ros2_ws
colcon build
source install/setup.bash
ros2 launch my_robot_project sim.launch.py


