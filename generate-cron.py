#!/usr/bin/python3

import json
import os


ABSOLUTE_PATH = os.path.dirname(os.path.realpath(__file__))
JOB_STR = '{cron} {absolute_path}/get.py {url} > {absolute_path}/{directory}$(date -d "today" +"%Y-%m-%d-%H%M%S").txt'

configuration = json.loads(open("sources.json", "r").read())

for item in configuration:

    output_directory = 'output/' + item['dir'] + '/'

    os.makedirs(output_directory, exist_ok=True)

    print(JOB_STR.format(absolute_path=ABSOLUTE_PATH,
                         cron=item['cron'],
                         url=item['url'],
                         directory=output_directory))
