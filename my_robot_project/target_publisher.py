import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TargetPublisher(Node):

    def __init__(self):
        super().__init__('target_publisher')
        self.pub = self.create_publisher(Float32, '/target_position', 10)
        self.timer = self.create_timer(1.0, self.publish_target)

    def publish_target(self):
        msg = Float32()
        msg.data = random.uniform(-1.0, 1.0)
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TargetPublisher()
    rclpy.spin(node)
    rclpy.shutdown()
