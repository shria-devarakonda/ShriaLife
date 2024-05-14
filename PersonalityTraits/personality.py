import random

class Personality:
    instance = None
    def __init__(self):
        if Personality.instance:
            raise Exception("use Personality.create()")
        Personality.instance = self
        self.confident = 0
        self.intelligent = 0
        self.generous = 0 
        self.trusting = 0
        self.brave = 0
        self.greedy = 0
        self.selfish = 0
        self.evil = 0 
        self.kind = 0
        self.init_personality()
    
    def create(self):
        if Personality.instance is None:
            Personality.instance = Personality()
        return Personality.instance
        
    def init_personality(self):
        # these are personal points, on a range to 10
        self.confident = 3
        self.intelligent = 5
        self.generous = 7
        self.trusting = 7
        self.brave = 3
        self.greedy = 6
        self.selfish = 6
        self.evil = 6 
        self.kind = 6
        
    def update_confidence(self,val=0):
        self.confident += val
    
    def update_intelligence(self,val=0):
        self.intelligent += val
        
    def update_generosity(self,val=0):
        self.generous += val
    
    def update_trustingness(self,val=0):
        self.trusting += val
    
    def update_bravery(self,val=0):
        self.brave += val
        
    def update_greediness(self,val=0):
        self.greedy += val
        
    def update_selfishness(self,val=0):
        self.selfish += val
        
    def update_evilness(self,val=0):
        self.evil += val
        
    def update_kindness(self,val=0):
        self.kind += val
    
    def show_personality(self):
        return self.__dict__