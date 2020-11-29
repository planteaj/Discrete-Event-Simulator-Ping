# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import simulator as s

sim = s.Simulator()
pingbool = True
class pingClass:
    
    def __init__(self):
        self.ping = True
        
    def ping(self, timestamp):
        sim.handleEvent(timestamp)
        sim.departEvent(timestamp)
        print("ping")        
        return False
        
    def pong(self, timestamp):
        sim.handleEvent(timestamp)
        sim.departEvent(timestamp)
        print("pong")
        return True
        

timestamp = 0
while timestamp != 100:
    p = pingClass()
    if pingbool == True:
        pingbool = p.ping(timestamp)
    else:
        pingbool = p.pong(timestamp)
    timestamp = timestamp + 1
a = sim.printNumOfEntries()
print(a)
    
