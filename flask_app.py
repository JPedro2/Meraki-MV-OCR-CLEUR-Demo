from flask import request, Flask
import Meraki_AWS_Script
import credentials
import get_face_data
import run_webex_capture
import emotion_graph
import aggregate_totals
import fatigue_graph
import brew_coffee


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
def run_webex_captures():
    run_webex_capture.run_webex_capture()
    return ("", 204)


@flask_app.route("/emotion-graph", methods=["GET"])
def emotions_graph():
    result = emotion_graph.emotion_graph()
    return result


@flask_app.route("/fatigue-graph", methods=["GET"])
def fatigues_graph():
    result = fatigue_graph.fatigue_graph()
    return result


@flask_app.route("/aggregate-totals", methods=["GET"])
def aggregete_total():
    result = aggregate_totals.aggregate_totals()
    return result

@flask_app.route("/brew-coffee", methods=["GET"])
def brew_coffee_demo():
    fatigue = brew_coffee.get_fatigue_result()
    coffee_strength = brew_coffee.strength_calc(fatigue)
    make_coffee = brew_coffee.IFTTT_make_coffee(coffee_strength)
    return make_coffee

if __name__ == "__main__":
    flask_app.run(
        host=credentials.FLASK["Flask_HOST"],
        port=credentials.FLASK["Flask_PORT"],
        debug=False,
    )

