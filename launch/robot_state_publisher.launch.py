from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('my_first_bot')) # Get the path to the package
    xacro_file = os.path.join(pkg_path, 'description', 'robot.urdf.xacro') # Get the path to the xacro file
    robot_description = Command(['xacro ', xacro_file]) # Process the xacro file to get the robot description as a string


    # Launch a robot_state_publisher node with the processed URDF
    return LaunchDescription([
        # Publish the joint states of the robot to determine the current position of robot's moving joints
        Node(
            package="joint_state_publisher",
            executable="joint_state_publisher",
            name="joint_state_publisher",
        ),
        # Publish the robot's state to the rest of the ROS system, including the transforms between the robot's links
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        )
    ])
