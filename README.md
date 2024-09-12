# Pub-Sub

A basic ROS2 package containing 2 nodes. One node publishes a message and the other node prints the message to the console.
 
# Commands

Pull the repo:
`git clone https://github.com/gt-mrg-training/Pub-Sub.git && cd Pub-Sub && git checkout training`

Demo Commands:

Source ROS2:

`source /opt/ros/humble/setup.bash`

Counter Node:

`colcon build`

`source install/setup.bash`


`ros2 run pub_sub counter`

`ros2 node list`


`ros2 topic list`

`ros2 topic info /count`

`ros2 topic echo /count`

Listener Node:

`ros2 run pub_sub listener`

`rqt_graph`

Turtle Sim:

`ros2 run turtlesim turtlesim_node`

`ros2 run turtlesim turtle_teleop_key`

`ros2 bag record -o turtle_data /turtle1/cmd_vel`

`ros2 bag play turtle_data`

`ros2 topic echo /turtle1/cmd_vel`

Launch Files

`ros2 launch pub_sub main.launch.py`

