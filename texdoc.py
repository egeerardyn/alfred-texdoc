#!/usr/bin/env python3
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
    results = str(results, 'utf-8')

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
    values = line.split('\t',3)
    fields = ('keyword','score','file','description')
    # Build dictionary with values
    result = dict((field,'') for field in fields)
    for (field,value) in zip(fields, values):
        result[field] = value
    return result

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
