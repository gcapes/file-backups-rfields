import re
import os


def getmetadata(inputFile, keywordList):
    '''Extract key info from (.idf and .ids) log files'''
    metadata = []
    with open(inputFile, 'r', encoding='ascii', errors='ignore') as f:
        for keyword in keywordList:
            regex = keyword + '=(\w{2,})'
            for line in f:
                match = re.search(regex, line, re.IGNORECASE)
                if match:
                    metadata.append(keyword + ' = ' + match.group(1))
                    break  # Not expecting more than one keyword per line
    return metadata


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


# Testing
CCDfile = 'Ivium Datafile - CCCD Example.idf'
CVfile = 'Ivium Datafile - CV Example.ids'
EISfile = 'Ivium Datafile - EIS Example.idf'
keywords = ['Serialnumber', 'Software', 'Firmware', 'Technique']

CCDlist = getmetadata(CCDfile, keywords)
CVlist = getmetadata(CVfile, keywords)
EISlist = getmetadata(EISfile, keywords)

CCDReadmeFile = os.path.join('output', 'CCD', 'README.txt')
CVReadmeFile = os.path.join('output', 'CV', 'README.txt')
EISReadmeFile = os.path.join('output', 'EIS', 'README.txt')
writelisttofile(CCDlist, CCDReadmeFile)
writelisttofile(CVlist, CVReadmeFile)
writelisttofile(EISlist, EISReadmeFile)
