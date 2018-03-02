import re
import os
import utils

def getmetadata(inputFile, keywordList):
    '''
    Extract key info from (.idf and .ids) log files.
    :param inputFile: Log file to extract metadata from
    :param keywordList: List of keywords to search for
    :return:
    '''
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
utils.writelisttofile(CCDlist, CCDReadmeFile)
utils.writelisttofile(CVlist, CVReadmeFile)
utils.writelisttofile(EISlist, EISReadmeFile)
