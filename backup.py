"""Back up files from Ivium machines"""
import logsheet as ls
import utils
import os
import datetime
import getmetadata as gm

# Define variables
pathfile     = os.path.abspath("paths.txt")
datadir, backupdir = utils.loadpaths(pathfile, 'data', 'backup')
logsheetname = 'logsheet.txt'
ignorefile   = '.backupignore'
missinglog   = os.path.join(datadir,'missinglogsheets.txt')
ignorelog   = os.path.join(datadir,'ignoreddirs.txt')
backuplog    = os.path.join(datadir, 'backuplog.txt')
keywords     = ['Serialnumber', 'Software', 'Firmware', 'Technique']
ext          = ('.ids','.idf')

logsheetreport = ls.findlogsheets(datadir, logsheetname, ignorefile)

dirswithlogsheet    = logsheetreport[0]
dirsmissinglogsheet = logsheetreport[1]
dirsignored         = logsheetreport[2]

utils.writelisttofile(dirsmissinglogsheet, missinglog)
utils.writelisttofile(dirsignored, ignorelog)

# Confirm directories haven't already been backed up
needbackup = dirswithlogsheet
if os.path.exists(backuplog):
    with open(backuplog, 'r') as f:
        for i, line in enumerate(f):
            if i > 0: # skip header row
                srcdir = line.split("\t")[1]
                if srcdir in dirswithlogsheet:
                    needbackup.remove(srcdir)

if needbackup:
    if not os.path.exists(backuplog):
        with open(backuplog, 'w') as f:
            f.write("Time\tSource directory\tBack up directory\n")

    with open(backuplog, 'a') as f:
        for dir in needbackup:
            # Create README files from .idf and .ids data files
            gm.writereadme(dir, ext, keywords)

            # Write log file to report src and dest directories and time copied
            logsheet = os.path.join(dir, logsheetname)
            src, dest = ls.copydirusinglogsheet(logsheet, backupdir)
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(now + '\t' + src + '\t' + dest + '\n')
            print("Directory copied: %s" % dir)
    print("Back up complete. See log file for directories copied: %s" % backuplog)
else:
    print("No directories were backed up.")
    print("See log file for directories already backed up: %s" % backuplog)

if dirsmissinglogsheet:
    print("See log file for directories missing log sheets: %s" % missinglog)

if dirsignored:
    print("The following directories have been ignored:")
    for dir in dirsignored:
        print(dir)
