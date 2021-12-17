## Dobot Magician ROS stack

This repository contains the Dobot Magician API code and ROS drivers,
repackaged in a more ROSified way.

## Changes to original code

The controller node in the ros_driver package provides a crude velocity
controller.

### Start ROS

```
roscore
```

### Launch the Server
DobotServer.cpp is required to run dobot's server.
Please rewrite the port name.
```
rosrun dobot_driver DobotServer Portname
```
### Writing a Client
Functions for running dobot on client are organized in DobotClient.py.
Import DobotClient.py to create a client
```
from dobot_py import DobotClient as dc
```

## Demo
### Launch the Sample Python Code 
```
rosrun dobot_driver DobotServer Portname
rosrun dobot_py tk_controller.py
```

### Launch the Sample C++ Code 
```
rosrun dobot_driver DobotServer Portname
rosrun dobot_bringup DobotClient_JOG
```
```
rosrun dobot_driver DobotServer Portname
rosrun dobot_bringup DobotClient_PTP
```