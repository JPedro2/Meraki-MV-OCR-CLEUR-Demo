import json
import credentials
import requests


def get_fatigue_result():
    # read file
    with open(
        "/home/peolivei/Cisco-SAD-DEMO-UI/src/media/sentimentor_capture/data.json", "r"
    ) as sentimentor_data:
        face_data = json.load(sentimentor_data)

    # Get Fatigue level
    fatigue = face_data["fatigue"]

    return fatigue


def IFTTT_make_coffee(strength):

    ifttt_headers = {
      'Content-Type': 'application/json'
    }

    payload = {}

    url = 'https://maker.ifttt.com/trigger/brew_coffee_{0}/with/key/{1}'.format(strength, credentials.IFTTT["API_Key"])

    r = requests.post(url, data=payload, headers=ifttt_headers)
    print("IFTTT URL: %s" % url)
    return r.text


def strength_calc(fatigue_lvl):

    if fatigue_lvl <= 55:
        strength = 'weak'
    elif fatigue_lvl <= 75:
        strength = 'medium'
    else:
        strength = 'strong'

    print("The fatigue level is " + str(fatigue_lvl) + " and the coffee strength is " + strength)

    return strength

if __name__ == "__main__":
    fatigue = get_fatigue_result()
    coffee_strength = strength_calc(fatigue)
    brew_coffee = IFTTT_make_coffee(coffee_strength)
    print(brew_coffee)
 
