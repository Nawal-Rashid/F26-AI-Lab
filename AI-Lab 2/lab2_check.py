from lab2_model import ClassroomAgent
agent = ClassroomAgent()
percepts = [
    (29,True),
    (29,True),
    (20,True),
    (26,True),
    (19,True),
    (29,False),
]
print("Classroom Agent Test")
print()
for step,percept in enumerate(percepts,1):
    old_mode=agent.previous_mode
    mode,command_needed=agent.act(*percept)
    if command_needed:
        status="send command"
    else:
        status="no command needed"
    print("step:",step)
    print("previous mode:",old_mode)
    print("percept:",percept)
    print("target mode:",mode)
    print("result:",status)