# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:01:34 2020

@author: ajpla
"""

import simulator 
import argparse
from functools import partial



class Ping:
    trip = 0

    def ping(self,trip):
        self.trip += 1/3
        return
    


sim_time = 100
fixed = False
lat_limit = 10
process = 3
parser = argparse.ArgumentParser()
parser.add_argument('-s', action="store", dest="sim_time", default=sim_time)
parser.add_argument('-f', action="store_true", dest="fixed",default=fixed)
parser.add_argument('-k', action="store", dest="lat_limit",default=lat_limit)
args = parser.parse_args()

s = simulator.Simulator(sim_time,fixed,lat_limit)
p = Ping()
i = 0;
list = [[0 for i in range(process)] for j in range(sim_time + 1)] 
#list = [sim_time + 1]
while i < sim_time:
    if s.num_in_system <= 1:
        for x in range(process):
            list = [x][sim_time+1]
        #list[0] = i
            list[x].insert(1, p.ping)
            list[x].insert(2, p.trip)
        s.enqueue(i, list) 
       

        #print(i)
    i = s.advance_time()   
    
print("the total trips done between ping and pong is: ")
print(p.trip)