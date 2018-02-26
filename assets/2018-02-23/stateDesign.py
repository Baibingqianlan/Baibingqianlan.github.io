# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:59:50 2018

@author: bbql
"""
import random
import time

#----------State-----------
# interface for state
class State:
    '''base interface '''
    def doSomething(self):
        print "nothing..."

class StateEat(State):
    def doSomething(self):
        print "Eating..." 

class StateSleep(State):
    def doSomething(self):
        print "Sleeping..." 
        
class StatePlay(State):
    def doSomething(self):
        print "Playing..." 
  
#----------Context-------------
class Context:
    def __init__(self):
        self.eatState = StateEat()
        self.sleepState = StateSleep()
        self.playState = StatePlay()
        
    def setState(self, s):
        self.curState = s
        self.curState.doSomething()
        
    def setRadom(self, r):
        if r<50:
            self.setState(self.eatState)
        elif r<20:
            self.setState(self.sleepState)
        else:
            self.setState(self.playState)

#--------------test-----------------------
if __name__ == '__main__':
    
    ct = Context()
    while 1:  
        r = random.randint(0,100)
        ct.setRadom(r)
        time.sleep(2)
    
    
            

        