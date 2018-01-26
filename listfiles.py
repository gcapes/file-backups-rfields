import os

def getSrcFiles(path,allFiles):
    for fileOrDir in os.listdir(path):
        if not fileOrDir.startswith('.'):
            fullPath = os.path.join(path,fileOrDir)
            if os.path.isdir(fullPath):
                getSrcFiles(os.path.join(path,fileOrDir),allFiles)
            else:
                allFiles.append(os.path.join(path,fileOrDir))
    return allFiles
            
for x in getSrcFiles('../',[]):
    print(x)