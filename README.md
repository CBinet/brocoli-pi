# Brocoli pi
Brocoli pi is a Flask REST API that can control your house, 
tell you what's the weather outside or simply act as a private server
for whatever reason you would need a private server. <br> 
It comes with a module to control the GPIO pins of the Rasberry 
pi it is running on, the **GPIOControls** module. It also comes with a
weather module, the **Weather** module, which gives you 
the temperature of any city using a Web API.

# Installation

## Install with git

### Clone the repository :
```sh
git clone https://github.com/CBinet/Brocoli-pi.git
```

### Launch WebPi
Launch the server :
```sh
python server.py
```
Your server will then be running locally at address http://0.0.0.0:5000. <br>
From other devices, the address will be something like http://192.168.x.xx:5000.

## Install with npm

### Install the package
```sh
npm install brocoli-pi
```
### Launch WebPi
Launch the server :
```sh
npm start
```

## **Extras** - Setup autorun on bootup
If you want to start the server automatically when
you boot up your raspberry, you can modify the **.profile** file
with the following command :
```sh
sudo nano ~/.profile
```

This will open your terminal file editor. <br> 
Add the following line at the end of the file :
```sh
python <where-your-server.py-is-located>/server.py
```
Then press **CTRL+X**, **Y** to save and quit the file editor. <br>

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
You could also run any python script by adding :
```sh
python <where-your-script.py-is-located>/<script.py>
```

# Using Brocoli-pi
To run the server
```sh
python server.py
```

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
## Weather

Working on it :) This is what is available at the moment.

### **Routes** :
- GET/ weather/current?city='city' : *Returns current's weather of 'city'*
- GET/ weather/forecast?city='city' : *Returns today's forecast of 'city'*

### **Example responses** :
*GET/ weather/current?city=Quebec* :
```json
{
  "precip_mm": 1.7,
  "last_updated": "2017-04-12 03:15",
  "wind_degree": 50,
  "wind_kph": 15.1,
  "is_day": 0,
  "temp_f": 36.3,
  "vis_miles": 5,
  "temp_c": 2.4,
  "humidity": 98,
  "last_updated_epoch": 1491981306,
  "cloud": 0,
  "feelslike_c": -1.5,
  "wind_mph": 9.4,
  "feelslike_f": 29.3,
  "wind_dir": "NE",
  "pressure_mb": 1021,
  "vis_km": 9.3,
  "precip_in": 0.07,
  "pressure_in": 30.6,
  "condition": {
    "text": "Clear",
    "code": 1000,
    "icon": "//cdn.apixu.com/weather/64x64/night/113.png"
  }
}
```

*GET/ weather/forecast?city=Quebec* :
```json
{
  "forecastday": [
    {
      "date": "2017-04-12",
      "astro": {
        "moonrise": "08:58 PM",
        "moonset": "07:03 AM",
        "sunset": "07:30 PM",
        "sunrise": "06:03 AM"
      },
      "date_epoch": 1491955200,
      "day": {
        "avgvis_miles": 6,
        "avghumidity": 84,
        "totalprecip_mm": 3.6,
        "avgtemp_c": 3.1,
        "avgtemp_f": 37.5,
        "maxwind_mph": 5.8,
        "mintemp_f": 36,
        "maxtemp_c": 3.2,
        "mintemp_c": 2.2,
        "maxtemp_f": 37.8,
        "totalprecip_in": 0.14,
        "maxwind_kph": 9.4,
        "avgvis_km": 10.4,
        "condition": {
          "text": "Light drizzle",
          "code": 1153,
          "icon": "//cdn.apixu.com/weather/64x64/day/266.png"
        }
      },
      "hour": [
        {
          "heatindex_c": 1.1,
          "heatindex_f": 34,
          "will_it_rain": 1,
          "will_it_snow": 0,
          "windchill_c": -1.2,
          "windchill_f": 29.8,
          "pressure_in": 30.6,
          "cloud": 100,
          "precip_mm": 1.7,
          "is_day": 0,
          "feelslike_c": -1.2,
          "condition": {
            "text": "Light drizzle",
            "code": 1153,
            "icon": "//cdn.apixu.com/weather/64x64/night/266.png"
          },
          "feelslike_f": 29.8,
          "wind_mph": 5.8,
          "dewpoint_c": 2.3,
          "vis_km": 9.3,
          "temp_f": 31.1,
          "temp_c": -0.5,
          "pressure_mb": 1021,
          "time_epoch": 1491969600,
          "precip_in": 0.07,
          "wind_dir": "ENE",
          "wind_kph": 9.4,
          "vis_miles": 5,
          "humidity": 80,
          "dewpoint_f": 36.1,
          "time": "2017-04-12 00:00",
          "wind_degree": 59
        },
        ...
      ]
    }
  ]
}
```