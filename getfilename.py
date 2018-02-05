def getNewFileName(inputFile):
    newFileName = ''
    with open(inputFile,'r') as f:
        for i, line in enumerate(f):
            if i < 3:
                # Do some useful string manipulation here
                newFileName += line
    return newFileName

filename = 'README.md'            
print(getNewFileName(filename))