import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class Follower(Node):

    def __init__(self):
        super().__init__('follower')
        self.sub = self.create_subscription(Float32, '/target', self.callback, 10)
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def callback(self, msg):
        cmd = Twist()
        cmd.linear.x = float(msg.data)
        cmd.angular.z = 0.0
        self.pub.publish(cmd)

def main():
    rclpy.init()
    node = Follower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
