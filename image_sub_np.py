#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import cv2
import numpy as np

class ImageSubscriber:
    def __init__(self):
        self.image_sub = rospy.Subscriber('/image_raw', Image, self.callback)

    def callback(self, msg):
        try:
            # Convert the image message to a NumPy array
            img_np = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1)
            img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        except Exception as e:
            rospy.logerr(e)
            return

        # Display the image using OpenCV
        cv2.imshow('Image', img_np)
        cv2.waitKey(3)

if __name__ == '__main__':
    rospy.init_node('image_subscriber', anonymous=True)
    image_subscriber = ImageSubscriber()
    rospy.spin()
