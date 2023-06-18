#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rospy
from demo_paket.msg import BataryaDurumu


def batarya(veri):
    rospy.loginfo("Batarya: yuzde %d", veri.batarya_durumu)

def mesaj_subscribe():

    rospy.init_node("subscriber_node", anonymous = True)
    rospy.Subscriber("batarya_topic", BataryaDurumu, batarya)
    rospy.spin()
    

mesaj_subscribe()




