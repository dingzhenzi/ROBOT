#!/usr/bin/python
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge,CvBridgeError
from sensor_msgs.msg import Image
def callback(msg):
	pub=rospy.Publisher('picture',Image,queue_size=10)
	rate=rospy.Rate(10)
	rospy.loginfo("finish")
	bridge=CvBridge()
	img=bridge.imgmsg_to_cv2(msg,"bgr8")
	cur_img=img.copy()
	gray=cv2.cvtColor(cur_img,cv2.COLOR_BGR2HSV)
	low=np.array([100,50,70])
	high=np.array([250,150,170])
	thresh=cv2.inRange(gray,low,high)
	kernel=np.ones([5,5],dtype=np.uint8)
	thresh=cv2.erode(thresh,kernel,iterations=2)
	thresh=cv2.dilate(thresh,kernel,iterations=4)
	contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	cnt=contours[0]
	x,y,w,h=cv2.boundingRect(cnt)
	text="%d,%d" % (x, y)
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
	cv2.putText(img,text, (143,121 ), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
	msg=bridge.cv2_to_imgmsg(img,"bgr8")
	pub.publish(msg)
def subscriber():
	rospy.init_node('subscriber',anonymous=True)
	rospy.Subscriber('picture/cmd_vel',Image,callback)
	rospy.loginfo("Success")
	rospy.spin()
if __name__=='__main__':
	try:
		subscriber()
	except rospy.ROSInterruptException:
		pass