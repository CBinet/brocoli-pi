

class Output:

    def __init__(self, id):
        self.id = id
	self.state = False

    def toggle(self):
        self.state = not self.state
        GPIO.output(self.id,self.state)

    def getId(self):
        return self.id

    def getCurrentState(self):
	    return self.state
