class triathlon:
    
    def __init__(self, first_name, last_name, location, swimtime, cycletime, runtime):
        self.f=first_name
        self.la=last_name
        self.lo=location
        self.st=swimtime
        self.ct=cycletime
        self.rt=runtime
        totaltime= swimtime+cycletime+runtime
        self.tt=totaltime
    def print_details(self):
        print(self.f+' '+self.la+' triathlon in '+self.lo+'. Swim time: '+str(self.st)+' Cycle time: '+str(self.ct)+' Run time: '+str(self.rt)+' Total time'+str(self.tt))

athlete1 = triathlon("Hugo", "Samano", "Haining", 500, 200, 100)
athlete1.print_details()
