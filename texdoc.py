#!/usr/bin/env python
# encoding utf-8

import sys
from workflow import Workflow
from subprocess import call, check_output

# References:
#  - http://alfredworkflow.readthedocs.org/en/latest/user-manual/setup.html
#  - http://stackoverflow.com/questions/89228/calling-an-external-command-in-python

log = None

def main(wf):
    args = wf.args
    call(["texdoc", args[0]])

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
