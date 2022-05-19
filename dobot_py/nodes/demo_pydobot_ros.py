#!/usr/bin/env python

from dobot_py.pydobot_ros import Dobot

if __name__ == "__main__":
    dobot = Dobot()
    dobot.home()
    dobot.speed(400, 400)
    dobot.move_to(200, 0, 0, 0)
    dobot.move_to(250, 0, 0, 0)
    dobot.wait(1000)
    dobot.move_to(200, 0, 0, 0)
    dobot.move_to(250, 0, 0, 0)
    dobot.wait(3000)
    print(dobot.pose())
