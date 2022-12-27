import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class CounterNode(Node):

    def __init__(self):
        super().__init__('counter')

        self.counter = 0

        self.pub = self.create_publisher(
            Int32,
            '/count',
            10
        )

        self.create_timer(
            1.0, 
            self.execute     
        )
    
    def execute(self):
        self.counter += 1

        msg = Int32()
        msg.data = self.counter
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = CounterNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()