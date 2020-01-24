### Make Sentimentor take a screen cap and analyse it (hit the sentimentor api)

import json
import requests


def run_webex_capture():
    # Get Stream ID
    response = requests.get("http://127.0.0.1:33600/streams")
    if response.status_code == 200:
        data = json.loads(response.content)
        streamID = data.get("streams")[0]

        # Post stream ID to sentimentor for capture
        response = requests.post(
            "https://127.0.0.1:4443/cme/api/v1/sentimentor/" + streamID + "/capture",
            verify=False,
        )
    else:
        print("ERROR: Can not connect to Sentimentor API")
        print(response.status_code)
    return
