class AiRobo:
    
    def __init__(self,name,battery=100):
        self.name=name
        self.battery=battery
        
    def charge(self):
        self.battery=100
        return self
    
    def say_name(self):
        if self.battery>0:
            self.battery-=1
            return f"i am a {self.name.upper()}"
        return "please charge"
    
    def learn(self,new_skill,cost_to_learn):
        if self.battery>=cost_to_learn:
            self.battery-=cost_to_learn
            self.skills.append(new_skill)
            
            return f"{new_skill.upper()}"
        return "insufficient battery. please charge and try again"