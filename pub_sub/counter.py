import rclpy
from rclpy.node import Node

class CounterNode(Node):

    def __init__(self):
        super().__init__('counter')

        self.counter = 0

        self.create_timer(
            1.0, 
            self.execute     
        )
    
    def execute(self):
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)

    node = CounterNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()