#usr/bin/env python3
import rospy
from  geometry_msgs.msg import Twist

from turtlesim.msg import Pose




    

if __name__=='__main__':

    rospy.init_node("Draw_square")
    rospy.loginfo("Node has been started")

    pub=rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    #sub=rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    rate=rospy.Rate(2)
    msg=Twist()
    if not rospy.is_shutdown():

        
        msg.linear.x=3.5
        msg.linear.y=0.0

        rate.sleep()
        pub.publish(msg)

        msg.linear.x=0
        msg.linear.y=3.5
        
        rate.sleep()
        pub.publish(msg)

        msg.linear.x=-3.5
        msg.linear.y=0.0

        rate.sleep()
        pub.publish(msg)

        msg.linear.x=0.0
        msg.linear.y=-3.5

        rate.sleep()
        pub.publish(msg)

        msg.linear.x=0
        msg.linear.y=0
        rate.sleep()

        pub.publish(msg)

        rate.sleep()




    