#!/usr/bin/env python3

import json
import os

SCRIPT_DIR = os.path.dirname(__file__)
INIT_FILE = os.path.join(SCRIPT_DIR, 'init.txt')

def get_problem_name(polygon_shortname):
    filename = 'polygon-contest/problems/%s/statements/russian/problem-properties.json' % polygon_shortname
    with open(os.path.join(SCRIPT_DIR, filename), encoding='utf-8') as f:
        content = f.read()
    parsed = json.loads(content)
    return parsed['name']

with open(INIT_FILE, 'r', encoding='utf-8') as init:
    for line in init:
        line = line.strip().split()
        row, column, ejudge_name, polygon_shortname, award, penalty, open_time = line[:8]
        row = int(row)
        column = int(column)

        parameters = 'row=%d, column=%d, ejudge_short_name="%s", name="%s", statement_file_name="%s.pdf", automatic_open_time=%d' % \
            (int(row), int(column), ejudge_name, get_problem_name(polygon_shortname), polygon_shortname, int(open_time))

        parameters += ', solved_award=%d, wrong_penalty=%d' % (int(award), int(penalty))

        print('        Problem(%s).save()' % parameters)
