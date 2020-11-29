# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:42:43 2020

@author: ajpla
"""
import random
import heapq
from queue import PriorityQueue


class Simulator:
    def __init__(self, sim,fix, lat):
        self.num_in_system = 0
        self.clock = 0
        #self.eventtime = []
        self.eventlist = []
        if fix == True:
            self.latency = 1
        else:
            self.latency = lat
        self.temp = []
        self.process = 0
        self.maxTime = sim
        import ping
        
    def enqueue(self, time, event):
       heapq.heappush(self.eventlist,(self.clock+self.interarrival_time(),event))
       self.num_in_system += 1
        
    def dequeue(self):
        while len(self.eventlist) > 0:
            r = heapq.heappop(self.eventlist)
            self.event_dispatch(r[1][1], r[1][2])
            self.num_in_system -=1
           
            return r[0]
            
    def event_dispatch(self, func, param):
        func(param)
        self.process +=1
     

    def advance_time(self):
        if self.num_in_system > 0:
            self.clock = self.dequeue()
            #print(self.clock)
            return self.clock
        else:
            return self.maxTime
        
    def interarrival_time(self):
        return random.randint(1, self.latency)
        


    