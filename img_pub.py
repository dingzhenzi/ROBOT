#!/usr/bin/python
import rospy
import cv2
from cv_bridge import CvBridge,CvBridgeError
from sensor_msgs.msg import Image
def publisher():
	bridge=CvBridge()
	rospy.init_node('publisher',anonymous=True)
	pub=rospy.Publisher('picture/cmd_vel',Image,queue_size=10)
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		cap=cv2.VideoCapture(0)
		cap.set(3, 256)
		cap.set(4, 256)
		cap.set(5, 60)
		while True:
        		flag,frame=cap.read()
        		if not flag:
        			break
        		msg=bridge.cv2_to_imgmsg(frame,"bgr8")
        		pub.publish(msg)
        		rospy.loginfo("finish")
        		rate.sleep()
if __name__=='__main__':
	publisher()