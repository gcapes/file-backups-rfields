# Prompt user for information on all missing logfiles
import logsheet as ls
import os

missinglogs = "/home/mbexegc2/Downloads/missinglogsheets.txt"

assert os.path.isfile(missinglogs), "File not found: %s" % missinglogs

with open(missinglogs, 'r') as f:
    for line in f:
        dir = line.strip('\n')
        ls.createlogsheet(dir)