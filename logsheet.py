'''
Prompt user for info on paper logsheet and write to file.
Also read logsheet.txt file in order to organise directories for backup.
'''
# Intended workflow:
	# Check for existence of logsheet.txt file.
	# If present, read the file and copy the directory.
		# Save successful copies to a log file.
	# Otherwise report directories where logfile.txt missing.
		# Prompt user to create missing logsheet.txt files

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

    assert os.path.exists(dir), "Directory doesn't exist: %s." % dir
    # Confirm that logsheet.info is indeed missing from dir
    logsheetfile = os.path.join(dir,'logsheet.txt')
    if os.path.exists(logsheetfile):
        overwrite = input('File already exists: ' + logsheetfile + '. Overwrite? (Y/N): ')
        if overwrite.lower() == 'n':
            return None
    creator = input('Creator: ')
    experimentid = input('Experiment ID: ')
    date = getdatefromdatafile(dir)
    assert date, 'Date not found in .idf or .ids file!'
    generalid = input('General ID: ')
    logsheetinfo = ['Creator: ' + creator, 'Experiment ID: ' + experimentid, 'Date: ' + date, 'General ID: ' + generalid]
    logsheetfile = os.path.join(dir,'logsheet.txt')
    utils.writelisttofile(logsheetinfo,logsheetfile)

def copydirusinglogsheet(logsheet, dest):
    """
    Use info in logsheet to create back up in subfolder of dest.
    :param logsheet: Path to file containing key experimental info
    :param dest: Path to directory to use for backups (subfolders created using info in logsheet)
    :return:
    """
    assert os.path.exists(logsheet), "File doesn't exist: %s" % logsheet

    src = os.path.dirname(os.path.abspath(logsheet))

    # Ensure back up is not within the source directory -- recursive back up would result.
    dest = os.path.abspath(dest)
    pathoverlap = os.path.commonpath([src,dest])
    if src == pathoverlap:
        raise ValueError('Back up directory is within source directory!\n'
                         'Back up: %s\n'
                         'Source: %s\n' % (dest, src))
    
    # Ensure back up directory exists, rather than creating a directory
    # from a path which could contain typos.
    assert os.path.exists(dest), "Destination directory doesn't exist: % s\n\
        Please create it first then try again." % dest

    # Read info from logsheet file
    regex = ':\s*(.+)'
    backupdir = dest
    with open(logsheet, 'r') as f:
        for line in f:
            match = re.search(regex, line)
            dirname = match.group(1)
            backupdir = os.path.join(backupdir, dirname)

    # Back up directory
    shutil.copytree(src, backupdir)

def findlogsheets(basedir, logfile):
    '''
    Scan a directory to identify (missing and present) logsheets.
    :param basedir: Directory to scan (string)
    :param logfile: Name of log file to search for
    :return: foundornot: List of lists [[dirs with logsheets],[dirs missing logsheets]]
    '''

    assert os.path.exists(basedir), "Directory doesn't exist: %s" % basedir

    # List directories recursively
    dirinfo = os.walk(basedir)

    found   = []
    missing = []

    # Identify which level should contain the logsheet.txt file (same as the *.idf, *.ids files)
    for root, subdirs, files in dirinfo:
        for file in files:
            if file.endswith(('.idf','.ids')):
                if logfile in files:
                    found.append(root)
                else:
                    missing.append(root)

    foundornot = [found, missing]

    return foundornot

def getdatefromdatafile(dir):
    """
    Scan .idf or .ids file for date, to be used in logsheet.txt

    :param dir: Directory to search
    :return: date
    """

    assert os.path.exists(dir), "Directory doesn't exist: %s" % dir

    dirlisting = os.listdir(dir)
    for file in dirlisting:
        if file.endswith(('.idf','.ids')):
            break
    else:
        raise Error('File not found. Looking for a .idf or .ids file in %s.' % dir)

    regex = 'starttime=([0-9]{1,2})/([0-9]{1,2})/([0-9]{4})'
    with open(file, 'r', encoding='ascii', errors='ignore') as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                year  = match.group(3)
                month = match.group(2)
                day   = match.group(1)
                date = year + month + day
                return date
        else:
            raise ValueError('Date not found in .idf or .ids file')