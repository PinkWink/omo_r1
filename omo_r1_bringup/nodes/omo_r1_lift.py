#!/usr/bin/env python

import sys
import rospy
import serial
from time import sleep
from std_msgs.msg import Int32

port_name = rospy.get_param('~port', '/dev/ttyUSB1')
baud_rate = rospy.get_param('~baud', 115200)

ser = serial.Serial(port_name, baud_rate)

def move_lift_pos():
    rospy.init_node('move_lift', anonymous=False)
    
    rospy.Subscriber("/lift_pose", Int32, callback)
    rospy.spin()

def callback(data):
    rospy.loginfo("lift_pose X : %s", data)
    cmd = "$LTMOV,"+str(data)
    ser.write(cmd+"\r\n")

if __name__ == '__main__':
	move_lift_pos()
