import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TargetPublisher(Node):

    def __init__(self):
        super().__init__('target_publisher')
        self.pub = self.create_publisher(Float32, '/target', 10)
        self.timer = self.create_timer(1.0, self.send_target)

    def send_target(self):
        msg = Float32()
        msg.data = random.uniform(-1.0, 1.0)
        self.pub.publish(msg)
        self.get_logger().info(f"Target: {msg.data}")

def main():
    rclpy.init()
    node = TargetPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
