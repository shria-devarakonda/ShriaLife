import random

class Status:
    instance = None
    def __init__(self):
        if Status.instance:
            raise Exception("use Status.create()")
        Status.instance = self
        self.happy = 0
        self.sad = 0
        self.confused = 0
        self.angry = 0
        self.scared = 0 
        # above metrics depend on the dream had before waking up or quality of sleep
        # or some other inexplicable thing, so little 
        # control on these, as it is mostly governed by the subconscious. might
        # have to think of a more sophisticated way of initializing these
        # also self commentary probs, figure out to have more control on 
        # my own emotions LOL
        self.init_emotion()
    
    def create(self):
        if Status.instance is None:
            Status.instance = Status()
        return Status.instance
        
    def init_emotion(self, emos={}):
        self.happy = emos.get("happy",random.randint(0,10))
        self.sad = emos.get("sad",random.randint(0,10))
        self.confused = emos.get("confused",random.randint(0,10))
        self.angry = emos.get("angry",random.randint(0,10))
        self.scared = emos.get("scared",random.randint(0,10))
        
    def update_happy(self,val=0):
        self.happy += val
    
    def update_sad(self,val=0):
        self.sad += val
        
    def update_confused(self,val=0):
        self.confused += val
    
    def update_angry(self,val=0):
        self.angry += val
    
    def update_scared(self,val=0):
        self.scared += val
        
    def show_status(self):
        return self.__dict__