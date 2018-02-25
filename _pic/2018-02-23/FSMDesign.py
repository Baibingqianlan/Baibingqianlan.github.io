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
        
#----------Transfer---------------
class Transfer:
    def __init__(self, e, s):
        self.event = e
        self.state = s
        
    def setTransfer(self,e,s):
        self.event = e
        self.state = s
    
    def getEvent(self):
        return self.event
        
    def getState(self):
        return self.state
            
#----------Event----------
class Event:
    def __init__(self, i):
        self.curE = i
    def setEvent(self,e):
        self.curE = e
    def getEvent(self):
        return self.curE
         
#----------FSM-------------
class FSM:
    def __init__(self):
        self.statesArray = []
        self.transferArray =[]
   
    def setInitState(self, s):
        self.statesArray.insert(0,s)
        
    def addState(self, s):
        self.statesArray.append(s)
        
    def addTransfer(self, tr):
        self.transferArray.append(tr)
        
    def acceptEvent(self, e):
        print "accept Event: " + str(e.getEvent())
        self.curEvent = e
        
    def setState(self, s):
        self.curState = s
        print "current Event is " + str(self.curEvent.getEvent())
        self.curState.doSomething()
        
    def run(self):
        self.setState(self.statesArray[0])
        for t in self.transferArray:
            jj = self.curEvent.getEvent()
            kk = t.getEvent().getEvent()
            if jj == kk:
                self.setState(t.getState())
        
 
#--------------test-----------------------
if __name__ == '__main__':
    
    play = StatePlay()
    eat = StateEat()
    sleep = StateSleep()
    
    fsm = FSM()
    fsm.setInitState(play)  
    fsm.addTransfer(Transfer(Event(7),eat)) #7:00 eating
    fsm.addTransfer(Transfer(Event(14),play)) #14:00 playing
    fsm.addTransfer(Transfer(Event(19),sleep)) #19:00 sleeping
    
    while 1:  
        r = random.sample([7,14,19],1)
        fsm.acceptEvent(Event(r[0]))
        fsm.run()
        time.sleep(2)
    
    
            

        