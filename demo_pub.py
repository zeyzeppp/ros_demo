#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rospy
from demo_paket.msg import BataryaDurumu

def mesaj_publish():

    rospy.init_node("publisher_node", anonymous = True)
    pub = rospy.Publisher("batarya_topic", BataryaDurumu, queue_size = 10)

    rate = rospy.Rate(1)

    while(not rospy.is_shutdown()):
        
        durum = 15
        
        rospy.loginfo(durum)
        
        pub.publish(durum)
        
        rate.sleep()
        
mesaj_publish()




