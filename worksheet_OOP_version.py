class Thermostat: 

    def __init__(self,name):
        self.name = name
        self.rooms = {"Golden Gate":70, "Great Hall":55, "Times Square":40, "Stonehenge":19}

    def cool_down(self,room):
    if room in self.rooms.keys():
        #subtract 5 from it
        self.rooms[room] = self.rooms[room] - 5
    else:
        return "Error"

    
    def head_up(room):
    if room in rooms.keys():
        #subtract 5 from it
        rooms[room] = rooms[room] + 5
    else:
        return "Error"


thermostat = Thermostat("Steve")

print(steve.rooms)
steve.cool_down("Golden Gate")
print(steve.rooms)

class Nest(Thermostat):
    def __init__(self, cool_extra):
        super().__init__(name)
        self.cool_extra = cool_extra
