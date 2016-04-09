#!/usr/bin/env python
# encoding utf-8

import sys
from workflow import Workflow
from subprocess import call, check_output
from os.path import basename

# References:
#  - http://alfredworkflow.readthedocs.org/en/latest/user-manual/setup.html
#  - http://stackoverflow.com/questions/89228/calling-an-external-command-in-python

log = None

def main(wf):
    args = wf.args
    results = check_output(["texdoc", '--list', '-M', args[0]])

    if len(results) != 0:
        lines = results.split('\n')
        for line in lines:
            item = parseLine(line)
            wf.add_item(basename(item['file']),
                        subtitle=item['description'],
                        valid=True,
                        arg=item['file'],
                        uid=item['file'],
                        icon=item['file'],
                        icontype='fileicon',
                        type='file',
                        copytext=item['file'],
                        largetext=line)

    wf.send_feedback()

def parseLine(line):
    # Line has format "<KEYWORD> <SCORE> <PATH> <DESCRIPTIONS>"
    parts = line.split('\t',3)
    result = {'keyword': '','score': '', 'file': '', 'description':''}
    if len(parts) >= 1: result['keyword'] = parts[0]
    if len(parts) >= 2: result['score'] = parts[1]
    if len(parts) >= 3: result['file'] = parts[2]
    if len(parts) >= 4: result['description'] = parts[3]
    return result

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
