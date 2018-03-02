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

def copydirusinglogsheet(logsheet,dest):
    """
    Use info in logsheet to create back up in subfolder of dest.
    :param logsheet: File containing key experimental info
    :param dest: Directory to make backups in (subfolders created using logsheet info)
    :return:
    """
    src = os.path.dirname(os.path.abspath(logsheet))

    # Ensure back up is not within the source directory -- recursive back up would result.
    dest = os.path.abspath(dest)
    pathoverlap = os.path.commonpath([src,dest])
    if src == pathoverlap:
        raise ValueError('Back up directory is within source directory!\n'
                         'Back up: %s\n'
                         'Source: %s\n' % (dest, src))

    # Read info from logsheet file
    regex = ':\s*(\w+)'
    backupdir = dest
    with open(logsheet, 'r') as f:
        for line in f:
            match = re.search(regex, line)
            dirname = match.group(1)
            backupdir = os.path.join(backupdir, dirname)

    # Create backup directory
    # Create backup directory
    utils.createdirfromfilepath(backupdir)

    # Back up directory
    shutil.copytree(src, backupdir)