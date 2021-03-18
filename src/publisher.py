#!/usr/bin/env python3

#import anypackages you need
import rospy

#import any ROS messages you need
from std_msgs.msg import String

#create a function where all the action happens
def messenger():
    #set up and publisers you want along with creating the ROS node
    pub = rospy.Publisher('mymessage', String, queue_size=10)
    rospy.init_node('messenger', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    #this standard ROS construct allows us to loop only when ROS is still active
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

#This allows the node to exit gracefully if ROS is shut down
if __name__ == '__main__':
    try:
        messenger()
    except rospy.ROSInterruptException:
        pass