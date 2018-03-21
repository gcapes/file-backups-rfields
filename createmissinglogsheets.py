"""Prompt user for information on all missing logfiles"""
import logsheet as ls
import os
import utils

datadir     = utils.loadpaths("paths.txt", 'data', 'backup')[0]
missinglogs = "missinglogsheets.txt"
missinglogs = os.path.join(datadir, missinglogs)

assert os.path.isfile(missinglogs), "File not found: %s" % missinglogs

with open(missinglogs, 'r') as f:
    for line in f:
        dir = line.strip('\n')
        ls.createlogsheet(dir)