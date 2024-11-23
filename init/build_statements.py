#!/usr/bin/env python3

import codecs
import os
import os.path
import shutil
import subprocess
import logging
import glob
import json

SCRIPT_DIR = os.path.dirname(__file__)
CONTEST_DIR = os.path.join(SCRIPT_DIR, 'polygon-contest')
BUILD_DIR = os.path.join(SCRIPT_DIR, 'build')
LANGUAGE = 'russian'
FILES_DIR = os.path.join(SCRIPT_DIR, 'files-' + LANGUAGE)


def time_limit_from_int(tl):
    tl //= 1000
    return str(tl) + ' секунд' + ('a' if tl == 1 else 'ы')

def memory_limit_from_int(ml):
    return str(ml // (1024 ** 2)) + ' мегабайт'

def build_with_text(text, replace_data, result, section='', problem_name=''):
    text = text.replace('%TEXT%', section + '\n' + replace_data)

    with codecs.open(os.path.join(BUILD_DIR, 'data.tex'), 'w', 'utf-8') as data_file:
        data_file.write(text)

    cwd = os.getcwd()
    os.chdir(BUILD_DIR)
    logging.info('Compile problem %s' % problem_name)
    for _ in range(2):
        subprocess.check_output(['pdflatex', '--shell-escape', 'compile.tex'])
    os.chdir(cwd)

    shutil.copy(os.path.join(BUILD_DIR, 'compile.pdf'), os.path.join(FILES_DIR, result))


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
    if not os.path.exists(FILES_DIR):
        logging.info('Create folder for output files: %s' % FILES_DIR)
        os.mkdir(FILES_DIR)
    if not os.path.exists(BUILD_DIR):
        logging.info('Create folder for build files: %s' % BUILD_DIR)
        os.mkdir(BUILD_DIR)

    problems_dir = os.path.join(CONTEST_DIR, 'problems')
    for problem_counter, problem_dir in enumerate(glob.glob(os.path.join(problems_dir, '*')), start=1):
        statement_dir = os.path.join(problem_dir, 'statements', LANGUAGE)
        properties_file_name = os.path.join(statement_dir, 'problem-properties.json')
        logging.info('Read problem properties file %s' % properties_file_name)

        with codecs.open(properties_file_name, 'r', 'utf-8') as properties_file:
            properties = json.load(properties_file)

            name = properties['name']
            legend = properties['legend']
            notes = properties['notes']
            input_file = properties['inputFile']
            output_file = properties['outputFile']
            time_limit = time_limit_from_int(properties['timeLimit'])
            memory_limit = memory_limit_from_int(properties['memoryLimit'])
            input_format = properties['input']
            output_format = properties['output']
            samples = properties['sampleTests']

            # shutil.copytree(statement_dir, BUILD_DIR, dirs_exist_ok=True)
            sample_tex_str = '\\begin{example}'
            for sample in samples:
                sampleInputFile, sampleOutputFile = sample['inputFile'], sample['outputFile']
                sample_tex_str += "\\exmpfile{%s}{%s}" % (sampleInputFile, sampleOutputFile)
                shutil.copy(os.path.join(statement_dir, sampleInputFile), os.path.join(BUILD_DIR, sampleInputFile))
                shutil.copy(os.path.join(statement_dir, sampleOutputFile), os.path.join(BUILD_DIR, sampleOutputFile))
            sample_tex_str += '\\end{example}'

            shutil.copy(os.path.join(SCRIPT_DIR, 'template.tex'), os.path.join(BUILD_DIR, 'compile.tex'))
            shutil.copy(os.path.join(SCRIPT_DIR, 'olymp.sty'), os.path.join(BUILD_DIR, 'olymp.sty'))
            with codecs.open(os.path.join(SCRIPT_DIR, 'data.tex'), 'r', 'utf-8') as data_file:
                data = data_file.read()


            data = data.replace('%NAME%', name).replace('%INPUT_FILE%', input_file).\
                        replace('%OUTPUT_FILE%', output_file).\
                        replace('%TIME_LIMIT%', time_limit).replace('%MEMORY_LIMIT%', memory_limit).\
                        replace('%PROBLEM_COUNTER%', str(problem_counter)).\
                        replace('%STATEMENT_DIR%', os.path.join('..', statement_dir).replace('\\', '/') + '/').\
                        replace('%EXAMPLES%', sample_tex_str)

            problem_name = os.path.basename(problem_dir)

            text = legend + '\n\\InputFile\n' + input_format + '\n\\OutputFile\n' + output_format
            if notes:
                text += '\n\\Notes\n' + notes

            build_with_text(data, text, problem_name + '.pdf', problem_name=problem_name)
            # build_with_text(data, input_format, problem_name + '-input-format.pdf', problem_name=problem_name, section=r'\InputFile')
            # build_with_text(data, output_format, problem_name + '-output-format.pdf', problem_name=problem_name, section=r'\OutputFile')


if __name__ == '__main__':
    main()
