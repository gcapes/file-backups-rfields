'''
Prompt user for info on paper logsheet and write to file.
Also read logsheet.info file in order to organise directories for backup.
'''

# Check for existence of logsheet.info file.
# If present, read the file and copy the directory.
# Otherwise report file missing.
# Prompt user for information where logsheet.txt is missing.

import utils
import os
import re
import shutil

def createlogsheet(dir):
    '''
    Write a file containing logsheet information from user input.
    :param dir: Where the file should be saved.
    :return:
    '''
    # assert that logsheet.info is indeed missing from dir
    logsheetfile = os.path.join(dir,'logsheet.txt')
    if os.path.exists(logsheetfile):
        overwrite = input('File already exists: ' + logsheetfile + '. Overwrite? (Y/N)\n')
        if overwrite.lower() == 'n':
            return None
    creator = input('Creator: ')
    experimentid = input('Experiment ID: ')
    date = input('Date: ') # Shouldn't I be able to read this from instrument log file?
    generalid = input('General ID: ')
    logsheetinfo = ['Creator: ' + creator, 'Experiment ID: ' + experimentid, 'Date: ' + date, 'General ID: ' + generalid]
    logsheetfile = os.path.join(dir,'logsheet.txt')
    utils.writelisttofile(logsheetinfo,logsheetfile)

