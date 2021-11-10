import rospy
from std_msgs.msg import String


pub = rospy.Publisher('say_hello_world', String, queue_size=10)
rospy.init_node('hello_world_node')
rate = rospy.Rate(10) # 10 hz
while not rospy.is_shutdown():
    pub.publish('hello world!')
    rate.sleep()