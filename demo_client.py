#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rospy
from demo_paket.srv import KonumSure


def request(konum):

    rospy.wait_for_service("zaman")

    try: 
        
        servis = rospy.ServiceProxy("zaman", KonumSure)
        cevap = servis(konum)

        return cevap.gecen_sure
    
    except rospy.ServiceException:

        rospy.loginfo("Servis Hatasi !")



hedef = float(input("hedef konumu yaziniz: "))

print("yol boyunca gecen sure: ", request(hedef))

    