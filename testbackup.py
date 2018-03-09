# Test code during development.
import logsheet as ls
import utils
import os

# Define variables
datadir      = '/home/mbexegc2/Downloads'
backupdir    = '/home/mbexegc2/backup'
missinglog   = os.path.join(datadir,'missinglogsheets.txt')
logsheetname = 'logsheet.txt'
tobecopied   = os.path.join(datadir, 'dirstobecopied.txt')

# Create README files from .idf and .ids data files

logsheetreport = ls.findlogsheets('/home/mbexegc2/Downloads', logsheetname)

dirswithlogsheet    = logsheetreport[0]
dirsmissinglogsheet = logsheetreport[1]

utils.writelisttofile(dirsmissinglogsheet, missinglog)
utils.writelisttofile(dirswithlogsheet, tobecopied)

for dir in dirswithlogsheet:
    logsheet = os.path.join(dir, logsheetname)
    ls.copydirusinglogsheet(logsheet, backupdir)
    # Write log file to report src and dest directories and time copied
    
# Check that directories have been backed up
    # Check destination directories and files exist, and that the file sizes are the same.

# Read missinglogsheets.txt file in order to create new logsheets.