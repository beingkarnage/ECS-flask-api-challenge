"""Routines associated with the application data.
"""
import json

courses = {}
last_id = 0


def load_data():
    """Load the data from the json file.
    """
    data = []
    try :
        with open('./json/course.json') as json_data :
            data = json.loads(json_data.read())
    except Exception as e:
        print(e)
        print("error opening course.json file")
        return

    global courses
    global last_id
    courses = { d['id'] : d for d in data }
    last_id = max(courses.keys()) 

