import os

'''
General utility functions used in other modules
'''

def writelisttofile(data, filename):
    '''Write contents of <data> into <filename>'''
    # Check parent directory of file exists
    createdirfromfilepath(filename)

    file = open(filename, 'w')
    for i, value in enumerate(data):
        file.write('%s\n' % value)


def createdirfromfilepath(dest):
    '''If dest dir doesn't exist, create it'''
    destDir = os.path.dirname(os.path.abspath(dest))
    if not os.path.exists(destDir):
        os.makedirs(destDir)
    # Confirm destination directory exists before copying
    assert (os.path.exists(destDir))