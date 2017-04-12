# WebPI

# Installation

### 0 - You should already have git installed. If not :
```sh
sudo apt-get install git --y
```

### 1 - Clone the repository :
Navigate where you want to create the folder and clone the repository <br>
```sh
git clone https://github.com/WebPI.git
```

### 2 - Launch WebPi
```sh
python server.py
```

### Extras - Setup autorun on bootup
1 - If you want to start the server automatically when
you boot up your raspberry pi, you can modify the .profile file
like this :
```sh
sudo nano ~/.profile
```
2 - This will open terminal text editor. Add the following line 
at the end of the file : 
```sh
python <where-your-server.py-is-located>/server.py
```
Extras - For example, your git repository is located in your
home folder. If you want the latest version of WebPi,
then start the server and also add a greeting message, 
you would do something like this :
```sh
echo Greetings, human.
cd ~/
git pull origin master
python server.py
```

# Using WebPi
To run the server

```sh
python server.py
```


# Modules

### GPIOControls

**Classes** :
- **Output** : *Single output pin*
- **Group** : *Group of output pins*

**Usage** : 
```py

# ...

# This instanciates an Output object.
# The first argument is the pin location
# on your raspberry pi. The second is simply
# a label to keep track of things.
output = Output(17, "Red Light")

# This will toggle the voltage of the output.
output.toggle()

#...

# This instanciates an Group object.
# The first argument is the id of the group
# The second are the outputs to assign to
# the group. The third argument is
# a label to keep track of things.
group = Group(0, outputs, "Basic 3 LED group")

# This will toggle the voltage of the outputs
# of the group.
group.toggle()

# ...

```


**Routes** :
- GET/ outputs : *Returns informations of current binded outputs*
- GET/ outputs/:id : *Returns information of the output at 'id' location*
- GET/ outputs/:id/toggle : *Toggle the voltage of the output at 'id' location*
- GET/ groups : *Returns informations of current binded groups*
- GET/ groups/:id : *Returns information of the group 'id'*
- GET/ groups/:id/toggle : *Toggle the voltage of the output of group 'id'*

**Example response** :

*GET/ outputs* :
```json
{
  "results": [
    {
      "id": 17,
      "info": "Red Light",
      "state": false
    },
    {
      "id": 18,
      "info": "Green Light",
      "state": false
    },
    {
      "id": 19,
      "info": "Yellow Light",
      "state": false
    }
  ]
}
```

### Weather

Working on it :)



