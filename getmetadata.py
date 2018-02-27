import re

def getmetadata(inputFile,keywordList):
    metadata = []
    with open(inputFile,'r', encoding='ascii',errors='ignore') as f:
        for line in f:
            for keyword in keywordList:
                regex = keyword + '=\w+'
                match = re.search(regex,line)
                if match:
                    metadata.append(match.group(0))
                    break # Not expecting more than one keyword per line
    return metadata

CCDfile = 'Ivium Datafile - CCCD Example.idf'
CVfile = 'Ivium Datafile - CV Example.ids'
EISfile = 'Ivium Datafile - EIS Example.idf'
keywords = ['Method','serialnumber']
print(getmetadata(CCDfile,keywords))
print(getmetadata(CVfile,keywords))
print(getmetadata(EISfile,keywords))