import os

def listFilesAndDirs(path,allFiles):
    for fileOrDir in os.listdir(path):
        if not fileOrDir.startswith('.'):
            fullPath = os.path.join(path,fileOrDir)
            if os.path.isdir(fullPath):
                listFilesAndDirs(os.path.join(path,fileOrDir),allFiles)
            else:
                allFiles.append(os.path.join(path,fileOrDir))
    return allFiles
            
for x in listFilesAndDirs('../',[]):
    print(x)