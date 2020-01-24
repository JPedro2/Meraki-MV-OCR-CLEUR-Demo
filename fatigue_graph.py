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


def fatigue_graph():
    con = psycopg2.connect(
        dbname=credentials.POSTGRES["DBname"],
        user=credentials.POSTGRES["USER"],
        password=credentials.POSTGRES["PASSWORD"],
        host=credentials.POSTGRES["HOST"],
        port=credentials.POSTGRES["PORT"],
    )

    cur = con.cursor()
    cur.execute("SELECT fatigue FROM mood_data;")
    rows = cur.fetchall()
    con.close()

    total40 = 0
    total45 = 0
    total50 = 0
    total55 = 0
    total60 = 0
    total65 = 0
    total70 = 0
    total75 = 0
    total80 = 0
    total85 = 0

    for row in rows:
        number = row[0]
        if 40 <= number < 45:
            total40 += 1
        elif 45 <= number < 50:
            total45 += 1
        elif 50 <= number < 55:
            total50 += 1
        elif 55 <= number < 60:
            total55 += 1
        elif 60 <= number < 65:
            total60 += 1
        elif 65 <= number < 70:
            total65 += 1
        elif 70 <= number < 75:
            total70 += 1
        elif 75 <= number < 80:
            total75 += 1
        elif 80 <= number < 85:
            total80 += 1
        elif 85 <= number < 90:
            total85 += 1

    data = [
        {"name": "40-45%", "total": total40},
        {"name": "45-50%", "total": total45},
        {"name": "50-55%", "total": total50},
        {"name": "55-60%", "total": total55},
        {"name": "60-65%", "total": total60},
        {"name": "65-70%", "total": total65},
        {"name": "70-75%", "total": total70},
        {"name": "75-80%", "total": total75},
        {"name": "80-85%", "total": total80},
        {"name": "85-90%", "total": total85},
    ]
    jsonResult = json.dumps(data)

    return jsonResult

