# dobot_ros
This repository contains the Dobot Magician API code and ROS drivers,
repackaged in a more ROSified way.

# Requirement
* Ubuntu 20.04
* ROS noetic

# Installation
```bash
sudo apt install libqt5serialport5 libqt5serialport5-dev
cd ~/catkin_ws/src
git clone https://github.com/shuto1441/dobot_ros.git
cd ../
catkin build
```

# Usage
### Launch the Server
DobotServer.cpp is required to run dobot's server.
Please rewrite the port name.
```bash
rosrun dobot_driver DobotServer Portname
```

### Launch the Sample Python Code 
```bash
rosrun dobot_py tk_controller.py
```
```bash
rosrun dobot_py demo_pydobot_ros.py
```
# Examples
```bash
dobot = Dobot() # Dobot class call Dobot(namespace). If you use multiple dobots, you need to set namespace.
dobot.home() # return to home position
dobot.speed(400, 400) # setting dobot speed (Velocity, Acceration)
dobot.move_to(200, 0, 0, 0) # setting dobot move to position (x, y, z, r)
dobot.wait(1000) # dobot wait(ms)
dobot.suck(1) # Sucker attachment 1: on 0: off
dobot.grip(1) # Gripper attachment 1: on 0: off
print(dobot.pose()) # return dobot current position
```

# Author
* [shuto1441](https://github.com/shuto1441)

# Reference
https://afrel.co.jp/dobot/




