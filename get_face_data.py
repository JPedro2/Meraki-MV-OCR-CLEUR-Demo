### Import Json file produced by sentimentor bot and provide through flask API

import json


def face_data():
    # read file
    with open(
        "/home/peolivei/Cisco-SAD-DEMO-UI/src/media/sentimentor_capture/data.json", "r"
    ) as myfile:
        data = myfile.read()
    # parse file
    obj = json.loads(data)

    # Get Fatigue Sentence
    fatigue = obj.get("fatigue")
    emotion = obj.get("emotion").lower()

    sentence1 = ""
    sentence2 = ""
    # Set main title sentence based on fatigue level
    if fatigue < 50:
        sentence1 = "You're a Machine! 🤨🤘🏽"
    elif fatigue < 60:
        sentence1 = "You're Looking Fresh! 😊👊🏽"
    elif fatigue < 70:
        sentence1 = "You're Looking Ok! 😕👌🏽"
    elif fatigue >= 70:
        sentence1 = "You are Exhausted! 😴👎🏽"

    # Set subtitle based on fatigue level and emotion
    if fatigue < 50:
        if emotion == "happy":
            sentence2 = (
                "and happy, energized and totally ready to hit some more sessions!"
            )
        elif emotion == "sad":
            sentence2 = "but sad. Why the long face?"
        elif emotion == "angry":
            sentence2 = "yet Angry! What’s annoying you?"
        elif emotion == "confused":
            sentence2 = "but confused and little dazed. Is it all a little too much?"
        elif emotion == "disgusted":
            sentence2 = "but disgusted! At the wrong conference maybe?"
        elif emotion == "surprised":
            sentence2 = "but surprised!? I know. This is Awesome technology right!!"
        elif emotion == "calm":
            sentence2 = "and calm. Totally zen my friend."
        elif emotion == "fear":
            sentence2 = "but scared?? Relax. We’re all friends here."

    elif fatigue < 60:
        if emotion == "happy":
            sentence2 = (
                "and happy. Obviously enjoying the event! Hit some more sessions."
            )
        elif emotion == "sad":
            sentence2 = "but please cheer up... Do you need a hug?"
        elif emotion == "angry":
            sentence2 = "but so angry!! Try and take it easy."
        elif emotion == "confused":
            sentence2 = "but you have no idea what’s going on!"
        elif emotion == "disgusted":
            sentence2 = "but you obviously hate all things technical!"
        elif emotion == "surprised":
            sentence2 = "and surprised. Yes… you are beautiful!!"
        elif emotion == "calm":
            sentence2 = "and taking everything in your stride. Possibly the perfect Cisco live attendee!"
        elif emotion == "fear":
            sentence2 = "but don’t be scared though. You are quite safe."

    elif fatigue < 70:
        if emotion == "happy":
            sentence2 = (
                "and happy! Maybe slow down a bit though. Don’t push it too hard."
            )
        elif emotion == "sad":
            sentence2 = "but cheer up. Maybe take a moment. You are at Cisco Live!!"
        elif emotion == "angry":
            sentence2 = "but angry! Have we offended you?"
        elif emotion == "confused":
            sentence2 = "but confused. Maybe slow down a bit. Your brain is full."
        elif emotion == "disgusted":
            sentence2 = "But disgusted!!? What have we done..?"
        elif emotion == "surprised":
            sentence2 = "but surprised? this is an amazing demo I know!"
        elif emotion == "calm":
            sentence2 = "and calm, Seems like you are in a good place."
        elif emotion == "fear":
            sentence2 = "but don’t be scared though. You are quite safe."

    elif fatigue < 80:
        if emotion == "happy":
            sentence2 = "but happy. This conference is great, but you need to slow down. Grab some sugar and caffeine!"
        elif emotion == "sad":
            sentence2 = "and sad. Maybe pushing this conference too hard my friend. Grab a coffee!"
        elif emotion == "angry":
            sentence2 = "and Angry. Someone not getting enough sleep!?"
        elif emotion == "confused":
            sentence2 = "and confused. Partying too hard! Am I right?"
        elif emotion == "disgusted":
            sentence2 = "and disgusted? Your picture was not that bad. We can only work with what we are given!"
        elif emotion == "surprised":
            sentence2 = "but surprised? What exactly were you expecting..?"
        elif emotion == "calm":
            sentence2 = "but calm. Pushing it but chilled."
        elif emotion == "fear":
            sentence2 = "but fearful? Maybe have a lie down."

    obj["sentence1"] = sentence1
    obj["sentence2"] = sentence2

    return obj
    