import re

def getmetadata(inputFile,keywordList):
    '''Extract key info from (.idf and .ids) log files'''
    metadata = []
    with open(inputFile,'r', encoding='ascii',errors='ignore') as f:
        for line in f:
            for keyword in keywordList:
                regex = keyword + '=(\w+)'
                match = re.search(regex,line,re.IGNORECASE)
                if match:
                    metadata.append(keyword + ' = ' + match.group(1))
                    break # Not expecting more than one keyword per line
    return metadata

CCDfile = 'Ivium Datafile - CCCD Example.idf'
CVfile = 'Ivium Datafile - CV Example.ids'
EISfile = 'Ivium Datafile - EIS Example.idf'
keywords = ['Serialnumber','Software','Firmware','Technique']

print(getmetadata(CCDfile,keywords))
print(getmetadata(CVfile,keywords))
print(getmetadata(EISfile,keywords))