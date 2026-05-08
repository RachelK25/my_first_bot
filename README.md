# Simple Caster Wheel Robot

This package provides a minimal setup for a caster wheel robot, intended as a starting point for further development and customization.

## Compatibility

**Operating System:** Noble \
**ROS2 version:** Jazzy \
**SDFormat:** 1.10

## Launch files

The robot state publisher can be launched by executing 'ros2 launch my_first_bot robot_state_publisher.launch.xml' (C++ version) or 'ros2 launch my_first_bot robot_state_publisher.launch.py (Python version). Note that both codes do the exact same, just written in another language.

The robot model will then be available for visualization in RViz2.

## Robot Description

The basic robot structure is defined in: *description/robot_base.urdf.xacro*

This file specifies all robot components such as the chassis, drive wheels, and caster wheel.
Each link of the robot contains three important elements:

- **Visual** – defines how the robot looks in visualization tools.
- **Collision** – defines the physical shape used for collision detection during simulation.
- **Inertial** – defines the mass and inertia properties required for realistic physics simulation.

The inertia calculations are implemented in a separate xacro file located in: *description/macros_inertia.xacro*

These macros provide predefined inertia formulas for common geometric shapes.

## Nodes

This package uses two nodes:

- **robot_state_publisher** - Publishes the robot transforms (tf) based on the URDF model.
- **joint_state_publisher** - Publishes joint states for the robot and allows movable joints to be visualized correctly.

## Gazebo

This version does not spawn the robot into Gazebo automatically. The robot is therefore not visible upon opening Gazebo.