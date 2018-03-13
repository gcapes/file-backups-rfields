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
tobecopied   = os.path.join(datadir, 'dirstobecopied.txt')
backuplog    = os.path.join(datadir, 'backuplog.txt')

# Create README files from .idf and .ids data files

logsheetreport = ls.findlogsheets('/home/mbexegc2/Downloads', logsheetname)

dirswithlogsheet    = logsheetreport[0]
dirsmissinglogsheet = logsheetreport[1]

utils.writelisttofile(dirsmissinglogsheet, missinglog)
utils.writelisttofile(dirswithlogsheet, tobecopied)


with open(backuplog, 'w') as f:
    f.write("Time\tSource directory\tBack up directory\n")
    for dir in dirswithlogsheet:
        logsheet = os.path.join(dir, logsheetname)
        src, dest = ls.copydirusinglogsheet(logsheet, backupdir)
        # Write log file to report src and dest directories and time copied
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(now + '\t' + src + '\t' + dest + '\n')
    
# Check that directories have been backed up
    # Check destination directories and files exist, and that the file sizes are the same.

# Read missinglogsheets.txt file in order to create new logsheets.