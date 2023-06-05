from pprint import pprint
import requests
import json
import time
from datetime import datetime
from config import username, password, deviceGuid

def main():

    url = "https://www.talent-monitoring.com/"
    url_login = url + "prod-api/login"
    urlcap = url + "prod-api/captchaImage"
    urlInverterinfo = url + "/prod-api/tools/device/selectDeviceInverterInfo?deviceGuid=" + deviceGuid + "&timezone=%2B02%3A00"

    LastTime = ""

    while True:
        #do some serial sending here
        with requests.session() as session:
            response = session.get(urlcap)
            if response.status_code != 200 :
                print ("Problem")
                time.sleep(60)
                continue
            response_dict = json.loads(response.text)
            uuid = response_dict["uuid"]
            data = {"username": username, "password": password, "uuid": uuid}
            response = session.post(url_login, json=data)
            if response.status_code != 200 :
                print ("Problem")
                time.sleep(60)
                continue
    #        pprint(response.text)
            token = json.loads(response.text)["token"]
    
            response = session.get(urlInverterinfo, headers={'Authorization': token})
            if response.status_code != 200 :
                print ("Problem")
                time.sleep(60)
                continue
    #        pprint(response.text)
            response_dict = json.loads(response.text)
            model = response_dict["data"]["model"]
            inverterTemp = response_dict["data"]["inverterTemp"]
            totalActivePower = response_dict["data"]["totalActivePower"]
            status = response_dict["data"]["status"]
            clientTime = response_dict["data"]["clientTime"]
            lastDataUpdateTime = response_dict["data"]["lastDataUpdateTime"]
            energyToday = response_dict["data"]["energyToday"]   # in Wh
            energyTotal = response_dict["data"]["energyTotal"]   
            phaseAActivePower = response_dict["data"]["phaseAActivePower"]
            phaseACurrent = response_dict["data"]["phaseACurrent"]
            phaseAVoltage = response_dict["data"]["phaseAVoltage"]
            PV1_current = response_dict["data"]["pv"][0]["current"]
            PV1_voltage = response_dict["data"]["pv"][0]["voltage"]
            PV1_power = response_dict["data"]["pv"][0]["power"]
            PV2_current = response_dict["data"]["pv"][1]["current"]
            PV2_voltage = response_dict["data"]["pv"][1]["voltage"]
            PV2_power = response_dict["data"]["pv"][1]["power"]

        if LastTime != lastDataUpdateTime :
            print(str(datetime.now()) + " Status: "+ status + " LastUpdate: " + lastDataUpdateTime + " " + str(inverterTemp) + "°C Power: " + str(totalActivePower) + " W Input: " + str(PV1_power+PV2_power) + " W" )
            LastTime = lastDataUpdateTime

        time.sleep(2.5*60)      # talent webside is updated every ~300 seconds, but not really reliable

if __name__ =='__main__':

    main()
