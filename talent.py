from pprint import pprint
import requests
import json
from config import username, password, deviceGuid

def main():
    
    url = "https://www.talent-monitoring.com/"
    url_login = url + "prod-api/login"
    urlcap = url + "prod-api/captchaImage"
    urlInverterinfo = url + "/prod-api/tools/device/selectDeviceInverterInfo?deviceGuid=" + deviceGuid + "&timezone=%2B02%3A00"


    with requests.session() as session:
        response = session.get(urlcap)
        response_dict = json.loads(response.text)
        uuid = response_dict["uuid"]
        data = {"username": username, "password": password, "uuid": uuid}
        response = session.post(url_login, json=data)
#        pprint(response.text)
        token = json.loads(response.text)["token"]

        response = session.get(urlInverterinfo, headers={'Authorization': token})
#        pprint(response.text)
        response_dict = json.loads(response.text)
#        pprint(response_dict["data"])

        model = response_dict["data"]["model"]
        print("model: %s" % model)

        inverterTemp = response_dict["data"]["inverterTemp"]
        print("inverterTemp: %s" % inverterTemp)

        totalActivePower = response_dict["data"]["totalActivePower"]
        print("totalActivePower: %s" % totalActivePower)

        status = response_dict["data"]["status"]
        print("status: %s" % status)

        clientTime = response_dict["data"]["clientTime"]
        print("clientTime: %s" % clientTime)

        lastDataUpdateTime = response_dict["data"]["lastDataUpdateTime"]
        print("lastDataUpdateTime: %s" % lastDataUpdateTime)

        energyToday = response_dict["data"]["energyToday"]   # in Wh
        print("energyToday: %s" % energyToday)

        energyTotal = response_dict["data"]["energyTotal"]   
        print("energyTotal: %s" % energyTotal)

        phaseAActivePower = response_dict["data"]["phaseAActivePower"]
        print("phaseAActivePower: %s" % phaseAActivePower)

        phaseACurrent = response_dict["data"]["phaseACurrent"]
        print("phaseACurrent: %s" % phaseACurrent)

        phaseAVoltage = response_dict["data"]["phaseAVoltage"]
        print("phaseAVoltage: %s" % phaseAVoltage)

        PV1_current = response_dict["data"]["pv"][0]["current"]
        print("PV1_current: %s" % PV1_current)

        PV1_voltage = response_dict["data"]["pv"][0]["voltage"]
        print("PV1_voltage: %s" % PV1_voltage)

        PV1_power = response_dict["data"]["pv"][0]["power"]
        print("PV1_power: %s" % PV1_power)

        PV2_current = response_dict["data"]["pv"][1]["current"]
        print("PV2_current: %s" % PV2_current)

        PV2_voltage = response_dict["data"]["pv"][1]["voltage"]
        print("PV2_voltage: %s" % PV2_voltage)

        PV2_power = response_dict["data"]["pv"][1]["power"]
        print("PV2_power: %s" % PV2_power)


if __name__ =='__main__':

    main()
