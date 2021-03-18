#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

class Adder:
    def __init__(self):
        self.number1 = None
        self.number2 = None

    def number1_callback(self, msg):
        # "Store" message received.
        self.number1 = msg.data

    def number2_callback(self, msg):
        # "Store" the message received.
        self.number2 = msg.data

    def add_numbers(self):
        if self.number1 is not None and self.number2 is not None:
            sum = self.number1 + self.number2
            pub.publish(sum)

if __name__ == '__main__':
    rospy.init_node('adding_machine')

    pub = rospy.Publisher('sum', Int16, queue_size=10)

    adder = Adder()

    rospy.Subscriber('/number1', Int16 , adder.number1_callback)
    rospy.Subscriber('/number2', Int16, adder.number2_callback)

    rate = rospy.Rate(1) # 1hz

    #this standard ROS construct allows us to loop only when ROS is still active
    while not rospy.is_shutdown():
        adder.add_numbers()
        rate.sleep()