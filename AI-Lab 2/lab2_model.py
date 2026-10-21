class ClassroomAgent:
    def __init__(self):
        self.previous_mode=None
    def act(self,temp,occupied):
        if not occupied:
            mode="eco"
        elif temp>26:
            mode="cool"
        elif temp<20:
            mode="warm"
        else:
            mode="idle"
        if mode==self.previous_mode:
            command_needed=False
        else:
            command_needed=True
        self.previous_mode=mode
        return mode, command_needed 