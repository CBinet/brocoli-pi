# WebPI

# Installation

### If you don't have git :
sudo apt-get install git --y

### Clone the repository :
Navigate where you want to create the folder and clone the repository <br>
git clone https://github.com/WebPI.git

### Pull the last version
Navigate where your git local repository is located <br>
git pull origin master

### Launch WebPi normally
python server.py 

# Using WebPi

### GPIOControls

Classes :
- Output : Single output pin
- Group : Group of output pins

Routes :
- GET/ outputs : Returns informations of current binded outputs
- GET/ outputs/:id : Returns information of the output at 'id' location
- GET/ outputs/:id/toggle : Toggle the voltage of the output at 'id' location
- GET/ groups : Returns informations of current binded groups
- GET/ groups/:id : Returns information of the group 'id'
- GET/ groups/:id/toggle : Toggle the voltage of the output of group 'id'

### Weather

Working on it :)



