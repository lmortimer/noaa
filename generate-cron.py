#!/usr/bin/python3

import json
import os


ABSOLUTE_PATH = os.path.dirname(os.path.realpath(__file__))
JOB_STR = '{absolute_path}/get.py {url} > {absolute_path}/{directory}$(date -d "today" +"%Y-%m-%d-%H%M%S").txt'
CRON_STR = '{cron} {absolute_path}/scripts/{id}.sh'

os.makedirs('scripts', exist_ok=True)
configuration = json.loads(open("sources.json", "r").read())

for item in configuration:

    output_directory = 'output/' + item['dir'] + '/'

    os.makedirs(output_directory, exist_ok=True)

    with open('scripts/{}.sh'.format(item['id']), 'w') as fh:
        fh.write('#!/bin/bash\n')
        fh.write(JOB_STR.format(absolute_path=ABSOLUTE_PATH,
                                url=item['url'],
                                directory=output_directory))

    os.chmod('scripts/{}.sh'.format(item['id']), 0o755)

    print(CRON_STR.format(cron=item['cron'],
                          absolute_path=ABSOLUTE_PATH,
                          id=item['id']))