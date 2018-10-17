# Brocoli pi
**Brocoli pi - Flask REST API for Raspberry pi**

# Installation

## Install with git

### Clone the repository :
```sh
git clone https://github.com/CBinet/Brocoli-pi.git
```

### Launch Brocoli pi
Launch the server :
```sh
python server.py
```
Your server will then be running locally at address http://0.0.0.0:5000. <br>
From other devices, the address will be your pi address. **Example** : http://192.168.2.51:5000. <br> 
*You can get your raspberry pi IP address with the following command :*
```sh
hostname -I
```

## Install with npm

### Install the package
```sh
npm install brocoli-pi
```
Navigate inside the brocoli-pi folder then :
### Launch Brocoli pi
```sh
npm start
```

## **Extras** - Setup autorun on bootup
If you want to start the server automatically when
you boot up your raspberry, you can modify your **.profile** file
located in your raspberry pi home folder :
```sh
sudo nano ~/.profile
```

Add the following line at the end of the file :
```sh
python <where-your-server.py-is-located>/server.py
```
Then press **CTRL+X**, **Y** to save and quit the file editor. <br> <br>

**Example** : Let's say your git repository is located in 
your home folder. If you want to add a greeting message, 
pull the latest version of *Brocoli-pi* and also start the server
you would do something like this :
```sh
echo Greetings, human.
cd ~/
git pull origin master
python server.py
```

# Using Brocoli-pi
To run the server :
```sh
python server.py
```
Once the server is started, you can test it by navigating to http://0.0.0.0:5000/outputs. <br> 
You should see a list of your outputs.

# Modules

## GPIOControls

### **Classes** :
- **Output** : *Single output pin*
- **Group** : *Group of output pins*

### **Usage** : 
```py
# Instanciate an output at location '17'
# with label "Red Light".
output = Output(17, "Red Light")

# Toggles the voltage of 'output'
output.toggle()

# ...

# Instanciate a group controlling 'outputs' with
# the label "LED group"
group = Group(0, outputs, "LED group")

# This will toggle the voltage of the outputs
# of the group.
group.toggle()
```


### **Routes** :
- GET/ outputs : *Returns informations of current binded outputs*
- GET/ outputs/:id : *Returns information of the output at 'id' location*
- GET/ outputs/:id/toggle : *Toggle the voltage of the output at 'id' location*
- GET/ groups : *Returns informations of current binded groups*
- GET/ groups/:id : *Returns information of the group 'id'*
- GET/ groups/:id/toggle : *Toggle the voltage of the output of group 'id'*

### **Example responses** :

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

*GET/ outputs/17/toggle* :
```json
    {
        "id": 17,
        "info": "Red Light",
        "state": true
    }
```

*GET/ groups/0* :
```json
{
    "id": 0,
    "info": "Basic 3 LED group",
    "outputs": [
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
    ],
    "state": false
}
```
