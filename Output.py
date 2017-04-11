class Output:

    def __init__(self, id):
        self.id = id
	self.state = False

    def getId(self):
        return str(self.id)

    def getCurrentState(self):
        if self.state:
	    return "On"
	else:
	    return "Off"
