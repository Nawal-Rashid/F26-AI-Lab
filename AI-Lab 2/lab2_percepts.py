class ClassroomAgent:
    def act(self,temp,occupied):
        if not occupied:
            return "eco"
        if temp>26:
            return "cool"
        if temp<20:
            return "warm"
        return "idle"
agent = ClassroomAgent()
percept = [(29,True),(29,True),(20,True),(26,True),(19,True),(29,True)]
for step, percept, in enumerate(percept, 1):
    print(step, percept, "target mode", agent.act(*percept))