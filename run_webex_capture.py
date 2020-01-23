### Make Sentimentor take a screen cap and analyse it (hit the sentimentor api)

import json
import requests


def run_webex_capture():
    # Get Stream ID
    response = requests.get("http://127.0.0.1:33600/streams")
    if response.status_code == 200:
        print(response.content)
        print(response.status_code)
        data = json.loads(response.content)
        print(data)
        print("TODO - manage streams")
        sessionID = ""  # TODO
        # Post stream ID to sentimentor for capture
        response = requests.post(
            "https://127.0.0.1:4443/cme/api/v1/sentimentor/" + sessionID + "capture",
            verify=False,
        )
        print(response)

    else:
        print("Can not connect to Sentimentor API")
        print(response.status_code)
    return


run_webex_capture()
