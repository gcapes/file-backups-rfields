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
    assert os.path.exists(inputFile), "File not found: %s" % inputFile
    
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

def getdatafile(dir,extensions):
    """
    Get name of data file, given directory name.
    :param: dir: Directory to search
    :param: extensions: Data file file extensions (string or tuple)
    :return: file
    """
    
    assert os.path.exists(dir), "Directory doesn't exist: %s" % dir
    
    dirlisting = os.listdir(dir)
    for file in dirlisting:
        if file.endswith(extensions):
            break
    else:
        raise NameError('File not found. Looking for a file ending in %s in %s.' % (extensions, dir))
    
    return file

def writereadme(dir, ext, keywords):
    """
    Write README file including key information from data file.
    param: dir: Source directory containing the data file.
    param: ext: File extensions to search for.
    param: keywords: Information to extract from data file.
    """
    assert os.path.exists(dir), "Directory doesn't exist: %s" % dir
    
    file = getdatafile(dir, ext)
    data = getmetadata(file, keywords)
    readme = os.path.join(dir, 'README.txt')
    utils.writelisttofile(data, readme)