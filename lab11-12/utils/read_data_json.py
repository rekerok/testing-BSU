import json
import os


def read_data_json(enviroment):
    PATH_RESOURCES = "./resources/" + enviroment + ".json"
    with open(PATH_RESOURCES, "r") as env:
        data = json.load(env)
    return data
