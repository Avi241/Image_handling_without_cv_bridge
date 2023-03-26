#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageSubscriber:

    def __init__(self):
        # self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/image_raw', Image, self.callback)

    def callback(self, data):
        print(data.data)
        # try:
        #     cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        # except Exception as e:
        #     print(e)
        #     return
        # cv2.imshow("Image window", cv_image)
        # cv2.waitKey(3)

if __name__ == '__main__':
    rospy.init_node('image_subscriber', anonymous=True)
    image_subscriber = ImageSubscriber()
    rospy.spin()
