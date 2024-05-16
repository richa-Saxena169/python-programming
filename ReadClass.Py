import configparser
import requests
import json
import os

config = configparser.ConfigParser()
config.read('config.txt')


class EnvironmentSelect:
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

            for i in fdata:
                print(i)
                dataapi = {}
                dataapi['name'] = i['name']
                dataapi['url'] = i['url']
                dataapi['topics'] = i['topics']

                self.APIData.append(dataapi)

            filename = self.outputpath

            with open(filename, "w") as f:
                f.write(json.dumps(self.APIData))
