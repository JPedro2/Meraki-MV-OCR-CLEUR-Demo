import ssl
import os
import requests
import json
import aws_utils
import log_utils
from PIL import Image
import io
import time
import credentials


def meraki_snapshot_link():

    base_URL = credentials.MERAKI["baseURL"]
    api_Key = credentials.MERAKI["API-Key"]
    network_ID = credentials.MERAKI["NetworkID"]
    camera_SERIAL = credentials.MERAKI["Camera-Serial"]

    url = (
        base_URL + "/networks/" + network_ID + "/cameras/" + camera_SERIAL + "/snapshot"
    )
    payload = ""
    headers = {"X-Cisco-Meraki-API-Key": api_Key, "Content-Type": "application/json"}

    response = requests.request("POST", url, data=payload, headers=headers)
    picture_url = json.loads(response.text)
    picture_url = picture_url["url"]
    print("The Meraki Snapshot API Status code is: " + str(response.status_code))
    print("The picture URL is: " + picture_url)
    return picture_url


def snapshot_meraki_camera():

    url = meraki_snapshot_link()

    # bypass SSL Cert validation
    if not os.environ.get("PYTHONHTTPSVERIFY", "") and getattr(
        ssl, "_create_unverified_context", None
    ):
        ssl._create_default_https_context = ssl._create_unverified_context

    if os.path.exists("/home/peolivei/Cisco-SAD-DEMO-UI/src/media/meraki_capture/meraki_snapshot.jpeg"):
        os.remove("/home/peolivei/Cisco-SAD-DEMO-UI/src/media/meraki_capture/meraki_snapshot.jpeg")

    time.sleep(5)
    r = requests.get(url)
    n = 0

    # Make sure that the snapshot link is accessible before downloading the picture
    while r.status_code != 200 | n<10:
        print("Image not found and the response status code is: "+str(r.status_code)+". Trying again in 2 seconds.")
        time.sleep(2)
        n+=1

    if r.status_code == 200:
        with open('/home/peolivei/Cisco-SAD-DEMO-UI/src/media/meraki_capture/meraki_snapshot.jpeg', 'wb') as f:
            f.write(r.content)
    else:
        print("Image not found and the response status code is:", r.status_code)

def convert_jpeg_binary():
    image_path = "/home/peolivei/Cisco-SAD-DEMO-UI/src/media/meraki_capture/meraki_snapshot.jpeg"
    #image_path = "/home/peolivei/Cisco-SAD-DEMO-UI/src/media/meraki_capture/test1.jpeg"
    image = Image.open(image_path)

    stream = io.BytesIO()
    image.save(stream, format="JPEG")
    image_binary = stream.getvalue()

    return image_binary


def detect_text():

    client = aws_utils.init_aws_Session()

    response = client.detect_text(Image={"Bytes": convert_jpeg_binary()})

    textDetections = response["TextDetections"]

    # Write to rekognition_logs log file
    log_utils.write_to_reko_log_file(textDetections)

    print("Detected text\n----------")
    for text in textDetections:
        if text["Confidence"] >= 90 and text["Type"] == "LINE":
            print("Detected text:" + text["DetectedText"])
            print("Confidence: " + "{:.2f}".format(text["Confidence"]) + "%")
            print("Id: {}".format(text["Id"]))
            print("Type:" + text["Type"])
            detected_text = text["DetectedText"]
        print()

    if "detected_text" not in locals():
        detected_text = "No text detected with high enough confidence"

    return detected_text


def main():
    snapshot_meraki_camera()
    text = detect_text()
    print("Text detected: " + str(text))


if __name__ == "__main__":
    main()
