#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rospy
from demo_paket.srv import KonumSure

def zamanHesaplama(data):

    hiz = 10.0
    sure = data.yol / hiz

    return sure


def response():

    rospy.init_node("server_node")
    rospy.Service("zaman", KonumSure, zamanHesaplama)

    rospy.spin()


if __name__ == "__main__":
    response()