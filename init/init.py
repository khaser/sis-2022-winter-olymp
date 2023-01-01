#!/usr/bin/python

import json

INIT_FILE = 'init.txt'

def get_problem_name(polygon_shortname):
    filename = 'polygon-contest/problems/%s/statements/russian/problem-properties.json' % polygon_shortname
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    parsed = json.loads(content) 
    return parsed['name']

with open('init_script.py', 'w', encoding='utf-8') as output_file:
    # print('from map.models import *', file=output_file)
    print('def __init__():', file=output_file)
    print('    AbstractTile.objects.all().delete()', file=output_file)
    
    with open(INIT_FILE, 'r', encoding='utf-8') as init:
        for line in init:
            line = line.strip().split()
            column, row, ejudge_name, terrain, polygon_shortname, award, penalty, open_time = line[:8]
            terrain = 1 if (terrain == "Ground") else 0
            row = int(row)
            column = int(column)
    
            parameters = 'row=%d, column=%d, terrain=%d, ejudge_short_name="%s", name="%s", statement_file_name="%s.pdf", automatic_open_time=%d' % \
                (int(row), int(column), terrain, ejudge_name, get_problem_name(polygon_shortname), polygon_shortname, int(open_time)) 
    
            parameters += ', solved_award=%d, wrong_penalty=%d' % (int(award), int(penalty))
    
            print('    Problem(%s).save()' % parameters, file=output_file)
