# Returns the total number of people analysed, smiling and male/female from DB

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


def aggregate_totals():
    con = psycopg2.connect(
        dbname=credentials.POSTGRES["DBname"],
        user=credentials.POSTGRES["USER"],
        password=credentials.POSTGRES["PASSWORD"],
        host=credentials.POSTGRES["HOST"],
        port=credentials.POSTGRES["PORT"],
    )

    # # Get total  people
    # cur = con.cursor()
    # cur.execute("SELECT gender FROM mood_data;")
    # rows = cur.fetchall()
    # # peopleTotal = rows[0][0]
    # print(rows)

    # Get total  people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data;")
    rows = cur.fetchall()
    peopleTotal = rows[0][0]
    # print("Total People: " + str(peopleTotal))

    # Get total Smily people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where smile = True;")
    rows = cur.fetchall()
    smileTotal = rows[0][0]
    # print("Total Smiling: " + str(smileTotal))

    # Get total male people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where gender = 'Male';")
    rows = cur.fetchall()
    maleTotal = rows[0][0]
    # print("Total male: " + str(maleTotal))

    # Get total male people
    cur = con.cursor()
    cur.execute("SELECT count(*) FROM mood_data Where gender = 'Female';")
    rows = cur.fetchall()
    femaleTotal = rows[0][0]
    # print("Total female: " + str(femaleTotal))

    con.close()
    result = {}
    result["totalPeople"] = peopleTotal
    result["totalMale"] = maleTotal
    result["totalFemale"] = femaleTotal
    result["totalSmile"] = smileTotal

    # print(result)
    return result

