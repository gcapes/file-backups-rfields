# Test code during development.
import logsheet as ls
import utils
import os
import datetime

# Define variables
datadir      = '/home/mbexegc2/Downloads'
backupdir    = '/home/mbexegc2/backup'
missinglog   = os.path.join(datadir,'missinglogsheets.txt')
logsheetname = 'logsheet.txt'
backuplog    = os.path.join(datadir, 'backuplog.txt')

# Confirm paths exist
assert os.path.exists(datadir), "Source directory not found: %s" % datadir
assert os.path.exists(backupdir), "Back up directory not found: %s" % backupdir

# Create README files from .idf and .ids data files

logsheetreport = ls.findlogsheets('/home/gerard/Downloads', logsheetname)

dirswithlogsheet    = logsheetreport[0]
dirsmissinglogsheet = logsheetreport[1]

utils.writelisttofile(dirsmissinglogsheet, missinglog)

# Confirm directories haven't already been backed up
if os.path.exists(backuplog):
    needbackup = []
    with open(backuplog, 'r') as f:
        for i, line in enumerate(f):
            if i > 0: # skip header row
                srcdir = line.split("\t")[1]
                if not srcdir in dirswithlogsheet:
                    needbackup.append(srcdir)
else:
    needbackup = dirswithlogsheet

if needbackup:
    if not os.path.exists(backuplog):
        with open(backuplog, 'w') as f:
            f.write("Time\tSource directory\tBack up directory\n")

    with open(backuplog, 'a') as f:
        for dir in needbackup:
            logsheet = os.path.join(dir, logsheetname)
            src, dest = ls.copydirusinglogsheet(logsheet, backupdir)
            # Write log file to report src and dest directories and time copied
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(now + '\t' + src + '\t' + dest + '\n')
    
# Check that directories have been backed up
    # Check destination directories and files exist, and that the file sizes are the same.

# Read missinglogsheets.txt file in order to create new logsheets.