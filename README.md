# dobot_ros
This repository contains the Dobot Magician API code and ROS drivers,
repackaged in a more ROSified way.

# Requirement
* Ubuntu 20.04
* ROS noetic

# Installation
```bash
cd ~/catkin_ws/src
git clone https://github.com/shuto1441/dobot_ros.git
cd ../
catkin build
```

# Usage
### Launch the Server
DobotServer.cpp is required to run dobot's server.
Please rewrite the port name.
```
rosrun dobot_driver DobotServer Portname
```

### Launch the Sample Python Code 
```
rosrun dobot_py tk_controller.py
```

### Launch the Sample C++ Code 
```
rosrun dobot_bringup DobotClient_JOG
```

# Author
* [shuto1441](https://github.com/shuto1441)

# Reference
https://afrel.co.jp/dobot/




