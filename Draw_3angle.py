#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__=='__main__':
    rospy.init_node("Draw_triangle")
    rospy.loginfo("Node has been started.")

    pub= rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    
    rate=rospy.Rate(2)
    msg=Twist()

    if not rospy.is_shutdown():

        msg.linear.x=2.0
        rate.sleep()

        pub.publish(msg)

        """ msg.linear.x=0
        msg.linear.y=0
        rate.sleep()

        pub.publish() """

        
        msg.linear.x=-2.0
        msg.linear.y=2.0
        rate.sleep()
        

        pub.publish(msg)
        """ msg.linear.x=0
        msg.linear.y=0
        rate.sleep()

        pub.publish()
 """

        msg.linear.x=-2.0
        msg.linear.y=-2.0


        rate.sleep()
        pub.publish(msg)
        """
        msg.linear.x=0
        msg.linear.y=0
        rate.sleep()

        pub.publish() 
        """
        msg.linear.x=2.0
        msg.linear.y=0
        rate.sleep()

        pub.publish(msg)


