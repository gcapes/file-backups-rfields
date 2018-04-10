"""Prompt user for information on all missing logfiles"""
import logsheet as ls
import os
import utils
import backup

datadir     = utils.loadpaths("paths.txt", 'data', 'backup')[0]
missinglogs = "missinglogsheets.txt"
missinglogs = os.path.join(datadir, missinglogs)

assert os.path.isfile(missinglogs), "File not found: %s" % missinglogs

with open(missinglogs, 'r') as f:
    for line in f:
        dir = line.strip('\n')
        if ls.createlogsheet(dir, datadir) == "q":
            break
        print("-----------------------------------")
print("Finished creating missing logsheets!")
print("-----------------------------------")

runbackup = input("Run back up now? (Y/N): ").lower().strip()
if runbackup == "y":
    print("Making back up ...")
    backup.makebackup()
else:
    print("Back up not made.")
print("-----------------------------------")