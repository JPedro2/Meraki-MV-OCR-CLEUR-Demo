import psycopg2
import json
import credentials

# DB Table Ref:

#   Column  |            Type             | Collation | Nullable |                Default                | Storage  | Stats target | Description
# ----------+-----------------------------+-----------+----------+---------------------------------------+----------+--------------+-------------
#  id       | integer                     |           | not null | nextval('mood_data_id_seq'::regclass) | plain    |              |
#  streamid | character varying(50)       |           | not null |                                       | extended |              |
#  emotion  | character varying(50)       |           | not null |                                       | extended |              |
#  smile    | boolean                     |           | not null |                                       | plain    |              |
#  age      | integer                     |           | not null |                                       | plain    |              |
#  gender   | character varying(50)       |           | not null |                                       | extended |              |
#  fatigue  | integer                     |           | not null |                                       | plain    |              |
#  location | character varying(50)       |           | not null |                                       | extended |              |
#  time     | timestamp without time zone |           | not null |                                       | plain    |              |


def emotion_graph():
    con = psycopg2.connect(
        dbname=credentials.POSTGRES["DBname"],
        user=credentials.POSTGRES["USER"],
        password=credentials.POSTGRES["PASSWORD"],
        host=credentials.POSTGRES["HOST"],
        port=credentials.POSTGRES["PORT"],
    )

    cur = con.cursor()
    cur.execute("SELECT emotion FROM mood_data;")
    rows = cur.fetchall()
    # print(rows)

    # Get total Happy people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where emotion ='HAPPY';")
    rows = cur.fetchall()
    happyTotal = rows[0][0]
    # print("Total Happy: " + str(happyTotal))

    # Get total sad people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where emotion ='SAD';")
    rows = cur.fetchall()
    sadTotal = rows[0][0]
    # print("Total sad: " + str(sadTotal))

    # Get total ANGRY people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where emotion ='ANGRY';")
    rows = cur.fetchall()
    angryTotal = rows[0][0]
    # print("Total ANGRY: " + str(angryTotal))

    # Get total CONFUSED people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where emotion ='CONFUSED';")
    rows = cur.fetchall()
    confusedTotal = rows[0][0]
    # print("Total CONFUSED: " + str(confusedTotal))

    # Get total DISGUSTED people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where emotion ='DISGUSTED';")
    rows = cur.fetchall()
    disgustedTotal = rows[0][0]
    # print("Total DISGUSTED: " + str(disgustedTotal))

    # Get total SURPRISED people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where emotion ='SURPRISED';")
    rows = cur.fetchall()
    surprisedTotal = rows[0][0]
    # print("Total SURPRISED: " + str(surprisedTotal))

    # Get total calm people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where emotion ='CALM';")
    rows = cur.fetchall()
    calmTotal = rows[0][0]
    # print("Total calm: " + str(calmTotal))

    # Get total FEAR people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where emotion ='FEAR';")
    rows = cur.fetchall()
    fearTotal = rows[0][0]

    con.close()

    # print("Total FEAR: " + str(fearTotal))

    data = [
        {"emotion": "Happy", "total": happyTotal},
        {"emotion": "Sad", "total": sadTotal},
        {"emotion": "Angry", "total": angryTotal},
        {"emotion": "Confused", "total": confusedTotal},
        {"emotion": "Disgusted", "total": disgustedTotal},
        {"emotion": "Surprised", "total": surprisedTotal},
        {"emotion": "Calm", "total": calmTotal},
        {"emotion": "Fearful", "total": fearTotal},
    ]
    jsonResult = json.dumps(data)

    return jsonResult
