from flask import request, Flask
import Meraki_AWS_Script
import env
import get_face_data
import run_webex_capture
import emotion_graph

flask_app = Flask(__name__)

merakiDetectedText = "Loading..."


@flask_app.route("/detect-text-retrieve", methods=["GET"])
def detect_text_retrieve():
    global merakiDetectedText
    return merakiDetectedText


@flask_app.route("/detect-text-analyze", methods=["GET"])
def detect_text_analyze():
    Meraki_AWS_Script.snapshot_meraki_camera()
    global merakiDetectedText
    merakiDetectedText = Meraki_AWS_Script.detect_text()
    return ("", 204)


@flask_app.route("/face-data", methods=["GET"])
def face_data():
    face_data = get_face_data.face_data()
    return face_data


@flask_app.route("/run-webex-capture", methods=["GET"])
def run_webex_capture():
    result = run_webex_capture.run_webex_capture()
    return ("", 204)


@flask_app.route("/emotion-graph", methods=["GET"])
def emotions_graph():
    result = emotion_graph.emotion_graph()
    return result


if __name__ == "__main__":
    flask_app.run(
        host=env.FLASK["Flask_HOST"], port=env.FLASK["Flask_PORT"], debug=False
    )

