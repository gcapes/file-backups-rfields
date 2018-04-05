import os
import shutil
import filecmp
import re

'''
General utility functions used in other modules
'''

def writelisttofile(data, filename):
    '''
    Write contents of <data> into <filename>
    :param data: List containing data to write
    :param filename: String containing a filename
    :return:
    '''

    # Check parent directory of file exists
    createdirfromfilepath(filename)

    file = open(filename, 'w')
    for i, value in enumerate(data):
        file.write('%s\n' % value)


def createdirfromfilepath(dest):
    '''
    If dest dir doesn't exist, create it.
    :param dest: Directory path (string).
    :return:
    '''
    destDir = os.path.dirname(os.path.abspath(dest))
    if not os.path.exists(destDir):
        os.makedirs(destDir)
    # Confirm destination directory exists before copying
    assert (os.path.exists(destDir))
    
def deletebackedupdir(srcdir, backupdir):
    """
    Check that back up has completed successfully,
    before deleting source directory.

    :param: srcdir: data directory being backed up
    :param: backupdir: directory containing back up of srcdir
    :return: True if directory was deleted,
        otherwise False if directory wasn't deleted
    """
    assert os.path.isdir(backupdir), "Directory not found: %s" % backupdir
    assert os.path.isdir(srcdir),  "Directory not found: %s" % srcdir
    
    safetodelete = equaldirs(backupdir, srcdir)
    if safetodelete:
        print("Deleting directory: %s" % srcdir)
        shutil.rmtree(srcdir)
        assert not os.path.exists(srcdir), "Directory removal failed: %s" % srcdir
        return True
    else:
        print("Directory not deleted: %s" % srcdir)
        print("Source and backup are different: %s, %s" % (srcdir, backupdir))
        return False
    
def equaldirs(dir1, dir2):
    """
    Test recursively if two directories are equal.
    
    :param: dir1: First directory to compare
    :param: dir2: Secondary directory to compare
    :return: True if the directory trees are the same and 
        there were no errors while accessing the directories or files, 
        False otherwise.
    """
    assert os.path.isdir(dir1), "Directory not found: %s" % dir1
    assert os.path.isdir(dir2), "Directory not found: %s" % dir2
    assert dir1 is not dir2, "Only given one directory to compare! %s" % dir1
    
    dirresult = filecmp.dircmp(dir1, dir2)
    if dirresult.left_only or dirresult.right_only or dirresult.funny_files:
        return False
    
    (_, mismatch, errors) =  filecmp.cmpfiles(
            dir1, dir2, dirresult.common_files, shallow=False)
    if mismatch or errors:
        return False
    
    for commondir in dirresult.common_dirs:
        newdir1 = os.path.join(dir1, commondir)
        newdir2 = os.path.join(dir2, commondir)
        if not equaldirs(newdir1, newdir2):
            return False
    return True

def loadpaths(pathfile, src, dest):
    """
    Load a text file containing data directory
    and back up directory paths.
    
    :param: pathfile: File containing the paths.
                This should contain two lines:
                    data: path/to/data
                    backup: path/to/backup
    :param: src: Key word in the path file labelling the source path
    :param: dest: Key word in the path file labelling the back up path
    :return: (datadir, backupdir) The data and back up directory paths.
    """
    
    assert os.path.isfile(pathfile), "File not found: %s" % pathfile
    
    regex = "(\w+):\s*(.+)"
    pathdict = {}
    with open(pathfile, 'r') as f:
        for i, line in enumerate(f):
            # File should contain only two lines. Ignore accidental extra lines.
            if i < 2:
                match = re.match(regex,line)
                assert match, "Search pattern not found in %s" % pathfile
                pathtype = match[1].strip()
                path = match[2].strip()
                pathdict[pathtype] = path

    datadir   = pathdict.get(src)
    backupdir = pathdict.get(dest)
    
    # Confirm paths exist
    assert len(datadir), "Source directory not set.\nEdit path file: %s" % pathfile
    assert len(backupdir), "Back up directory not set.\nEdit path file: %s" % pathfile
    assert os.path.exists(datadir), "Source directory not found: %s" % datadir
    assert os.path.exists(backupdir), "Back up directory not found: %s" % backupdir
    
    # Confirm paths are different
    assert datadir!=backupdir, "Source and back up directories must be different!\n"\
                               "Please edit paths file: %s " % pathfile
    
    
    return (datadir, backupdir)
