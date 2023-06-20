#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import rospy
import actionlib
from demo_paket.msg import YolTamamlamaAction, YolTamamlamaGoal


def gorevDurumu(info):

    print("gorev tamamlanma orani: ", info.yol_durumu)



def request():

    rospy.init_node("action_client_node")
    client = actionlib.SimpleActionClient("gorev_action", YolTamamlamaAction)

    client.wait_for_server()
    
    istek = YolTamamlamaGoal()

    istek.gidilecek_yol = 10
    
    client.send_goal(istek, feedback_cb = gorevDurumu)

    client.wait_for_result()

    x = client.get_result().kontrol
    
    return x


cikti = request()
print("gorevin son durumu: ", cikti)
