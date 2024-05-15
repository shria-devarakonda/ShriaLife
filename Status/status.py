import random

class Status:
    instance = None
    def __init__(self):
        if Status.instance:
            raise Exception("use Status.create()")
        Status.instance = self
        self.happy = random.randint(0,10)
        self.sad = random.randint(0,10)
        self.confused = random.randint(0,10)
        self.angry = random.randint(0,10)
        self.scared = random.randint(0,10)
        self.calm = random.randint(0,10)
        self.smart = random.randint(0,10)
        self.manic = random.randint(0,10)
        # above metrics depend on the dream had before waking up or quality of sleep
        # or some other inexplicable thing
    
    def create(self):
        if Status.instance is None:
            Status.instance = Status()
        return Status.instance
        
        
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
    
    def update_calm(self,val=0):
        self.calm += val
        
    def show_status(self):
        return self.__dict__