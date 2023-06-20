#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import rospy
import actionlib
from demo_paket.msg import YolTamamlamaAction, YolTamamlamaFeedback, YolTamamlamaResult


class ActionServer():

    def __init__(self):

        rospy.init_node("action_server_node")
        self.a_server = actionlib.SimpleActionServer("gorev_action", YolTamamlamaAction, auto_start = False, execute_cb = self.cevap)

        self.a_server.start()
        rospy.spin()




    def cevap(self, istek):

        geri_bildirim = YolTamamlamaFeedback()
        result = YolTamamlamaResult()

        rate = rospy.Rate(1)



        for i in range(1, istek.gidilecek_yol):

            durum = "% " + str(i*100/istek.gidilecek_yol)
            geri_bildirim.yol_durumu = durum

            self.a_server.publish_feedback(geri_bildirim)
            rate.sleep()




        
        result.kontrol = "gorev tamamlandi !"
        self.a_server.set_succeeded(result)


ActionServer()





