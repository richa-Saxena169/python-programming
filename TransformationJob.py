import configparser
import csv
from datetime import datetime

import pandas as pd
import json

config = configparser.ConfigParser()
config.read('config.txt')


class TransformationJob:

    def __init__(self, env):
        self.env = env
        self.filename = config[env]['readFile']
        self.tranformfilepath = config[env]['tranformfilepath']

    def transformer(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)

        df = pd.json_normalize(data)
        df['topicnew'] = [','.join(map(str, l)) for l in df['topics']]

        df = df[['id', 'name', 'description', 'url', 'topicnew']]

        outputfile = self.tranformfilepath + 'flatdata' + datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p") + '.csv'
        df.to_csv(outputfile, index=False, quoting=csv.QUOTE_ALL)
