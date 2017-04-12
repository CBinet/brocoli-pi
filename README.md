# WebPI

# Installation

### If you don't have git :
```sh
sudo apt-get install git --y
```


### Clone the repository :
Navigate where you want to create the folder and clone the repository <br>
```sh
git clone https://github.com/WebPI.git
```

### Pull the last version
Navigate where your git local repository is located <br>
```sh
git pull origin master
```

### Launch WebPi normally
```sh
python server.py
```

# Using WebPi

### GPIOControls

Classes :
- **Output** : *Single output pin*
- **Group** : *Group of output pins*

Usage : 
```py
# This instanciates an Output object.
# The first argument is the pin location
# on your raspberry pi. The second is simply
# a label to keep track of things.
output = Output(17, "Red Light")
# This will toggle the voltage of the output.
output.toggle()
```
```py
# This instanciates an Group object.
# The first argument is the id of the group
# The second are the outputs to assign to
# the group. The third argument is
# a label to keep track of things.
group = Group(0, outputs, "Basic 3 LED group")
# This will toggle the voltage of the outputs
# of the group.
group.toggle()
```


Routes :
- GET/ outputs : *Returns informations of current binded outputs*
- GET/ outputs/:id : *Returns information of the output at 'id' location*
- GET/ outputs/:id/toggle : *Toggle the voltage of the output at 'id' location*
- GET/ groups : *Returns informations of current binded groups*
- GET/ groups/:id : *Returns information of the group 'id'*
- GET/ groups/:id/toggle : *Toggle the voltage of the output of group 'id'*

### Weather

Working on it :)



