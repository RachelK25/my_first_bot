# Simple Caster Wheel Robot

This package provides a minimal setup for a caster wheel robot, intended as a starting point for further development and customization.

---

## Compatibility

**Operating System:** Ubuntu 24.04 Noble \
**ROS2 version:** Jazzy \
**SDFormat:** 1.10 \
**Gazebo Version:** Harmonic

---

## Launch files

In case of performing Gazebo simulations, start Gazebo first:

```bash
ros2 launch ros_gz_sim gz_sim.launch.py
```

Then launch the robot:

```bash
ros2 launch my_first_bot robot_state_publisher.launch.py
```

or:

```bash
ros2 launch my_first_bot robot_state_publisher.launch.xml
```

Both launch files perform the same actions but are written in different formats (Python and XML).

The robot model will then be available in Gazebo and can also be visualized in RViz2.

---

## Robot Description

The basic robot structure is defined in:

```text
description/robot_base.urdf.xacro
```

This file specifies all robot components such as:

- the chassis
- drive wheels
- caster wheel

Each robot link contains three important elements:

- **Visual** — defines how the robot appears in visualization tools.
- **Collision** — defines the physical geometry used for collision detection during simulation.
- **Inertial** — defines the mass and inertia properties required for realistic physics simulation.

The inertia calculations are implemented in:

```text
description/macros_inertia.xacro
```

These macros provide predefined inertia formulas for common geometric shapes.

---

## Nodes

The robot launch file starts three ROS 2 nodes:

- **robot_state_publisher** — publishes the robot transforms (`tf`) based on the URDF model.
- **joint_state_publisher** — publishes joint states so movable joints can be visualized correctly.
- **ros_gz_sim/create** — reads the robot description and spawns the robot into Gazebo.

These nodes are automatically started when launching the robot.