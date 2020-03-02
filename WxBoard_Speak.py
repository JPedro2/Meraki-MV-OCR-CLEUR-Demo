import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import xmltodict
import credentials

#Disable SSL Warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

WxBoard_IPaddress = credentials.Webex_Board["ip_address"]
WxBoard_username = credentials.Webex_Board["user"]
WxBoard_password = credentials.Webex_Board["password"]

def makeWxBoardSpeak(Sentence):
    url = "https://" + WxBoard_IPaddress + "/putxml"
    payload = "<XmlDoc><Command><Experimental><VoiceControl><Speak><Text>" + Sentence + "</Text></Speak></VoiceControl></Experimental></Command></XmlDoc>"
    header = {'Content-Type': "text/xml"}

    try:
        getResponse = requests.request("POST", url, data=payload, headers=header, verify=False, auth=(WxBoard_username, WxBoard_password))
        getResponse = xmltodict.parse(getResponse.content)
        return print("Request Successful, listen to the WxBoard carefully!")
    except:
        return print("Failed")

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

if __name__ == "__main__":
    makeWxBoardSpeak("1, 2, 1, 2, Sound Check")