#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2
import numpy as np

def main():
    rospy.init_node('opencv_to_ros_image_publisher')
    image_pub = rospy.Publisher('image_raw', Image, queue_size=10)

    # Load the image using OpenCV
    cv_image = cv2.imread('ros.png')

    # Convert the OpenCV image to a ROS Image message
    ros_image = Image()
    ros_image.header.stamp = rospy.Time.now()
    ros_image.height = cv_image.shape[0]
    ros_image.width = cv_image.shape[1]
    ros_image.encoding = 'bgr8'
    ros_image.is_bigendian = False
    ros_image.step = 3 * ros_image.width
    ros_image.data = np.array(cv_image).tostring()

    # Publish the ROS Image message on the 'image_raw' topic
    while not rospy.is_shutdown():
        image_pub.publish(ros_image)
        rospy.sleep(1.0)

if __name__ == '__main__':
    main()
