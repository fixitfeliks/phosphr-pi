# FixitFeliks Phosphr PI Node Started March 16th 2019
import requests
import json

filename = "/proc/cpuinfo"
id = ""

#Can add functionality to verify serial num on every run?
try:
    with open(filename) as f:
        for line in f:
            str = line.split(":")
            if  str[0].find("Serial") > -1:
                id = id.join(c for c in str[1] if c.isalnum())
except FileNotFoundError:
    id = "NA001"
    print("Id not found, set deafult")

url = "https://fixitfeliks.com/phosphr"

light = """{
    "id": "%s",
    "type": "action.devices.types.LIGHT",
    "traits": [
      "action.devices.traits.OnOff",
      "action.devices.traits.Brightness",
      "action.devices.traits.ColorSpectrum"],
    "name":{
      "defaultNames": ["SmartLight"],
      "name":"Smart Light 0",
      "nicknames": ["Feliks Light"]},
      "willReportState": false,
      "roomHint": "",
      "deviceInfo": {
      "manufacturer": "Phosphr Cloud",
      "model":"fp1337",
      "swVersion": "0.0.1",
      "hwVersion": "0.1.0"}
}
"""

light = light % id
reqStr = json.loads(light)
print(reqStr)

def getId():
    return id

#r = requests.post(url, json=reqStr)
#print(r)
