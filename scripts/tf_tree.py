#!/usr/bin/env python3

import rospy
import tf
from tf.transformations import quaternion_from_euler as qe

if __name__ == "__main__":
    rospy.init_node("tf_tree", anonymous=False)
    br = tf.TransformBroadcaster()

    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():

        br.sendTransform((0.1235,0.03,0),qe(0,0,0), rospy.Time.now(), "camera_link", "base_link")
        br.sendTransform((-0.0965,-0.06,0),qe(0,0,0), rospy.Time.now(), "imu_link", "base_link")

        rate.sleep()