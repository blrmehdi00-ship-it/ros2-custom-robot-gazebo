import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class Follower(Node):

    def __init__(self):
        super().__init__('follower')
        self.sub = self.create_subscription(Float32, '/target_position', self.callback, 10)
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def callback(self, msg):
        cmd = Twist()

        if msg.data > 0.2:
            cmd.angular.z = -0.5
        elif msg.data < -0.2:
            cmd.angular.z = 0.5
        else:
            cmd.linear.x = 0.4

        self.pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = Follower()
    rclpy.spin(node)
    rclpy.shutdown()
