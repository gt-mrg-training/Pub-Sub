import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class ListenerNode(Node):

    def __init__(self):
        super().__init__('listener')

        self.sub = self.create_subscription(
            Int32,
            '/count',
            self.callback,
            10
        )
    
    def callback(self, msg:Int32):
        count = msg.data
        self.get_logger().info(
            f'I heard: {count}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = ListenerNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()