import rospy
from std_msgs.msg import String


def main():
    
     # Node Name Initialization
    rospy.init_node('hello_world')
    
    # Publisher Declaration, Topic Name = say_hello_world
    pub = rospy.Publisher('say_hello_world', String, queue_size=10)
    rate = rospy.Rate(10) # 10 hz
    while not rospy.is_shutdown():
        pub.publish("hello world")
        rate.sleep() 


if __name__ == '__main__':
    main()
