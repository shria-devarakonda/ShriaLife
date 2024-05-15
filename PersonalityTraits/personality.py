import random

class Personality:
    instance = None
    def __init__(self):
        if Personality.instance:
            raise Exception("use Personality.create()")
        Personality.instance = self
        self.confident = 3
        self.intelligent = 4
        self.generous = 7 
        self.trusting = 6
        self.brave = 4
        self.greedy = 5
        self.selfish = 6
        self.evil = 5 
        self.kind = 6
    
    def create(self):
        if Personality.instance is None:
            Personality.instance = Personality()
        return Personality.instance
        
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