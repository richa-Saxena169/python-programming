import configparser
import datetime

import requests
import json


config = configparser.ConfigParser()
config.read('config.txt')


class DatapipeLine:
    tableName = 'User'
    Column = 'FirstName'
    pageSize = 2
    datakeys = ['name', 'url', 'topics']
    dataapi = {}
    APIData = []

    def __init__(self, env, username):
        self.env = env
        self.apiURL = config[env]['apiUrL'].format(username)
        self.outputpath = config[env]['outputpath']
        self.username = username

    def apiGetData(self):
        data = requests.get(self.apiURL)
        print(data)

        if data.status_code == 200:
            fdata = json.loads(data.text)

            filename = self.outputpath + datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p") +'.txt'
            with open(filename, "w") as f:
                f.write(json.dumps(fdata))



