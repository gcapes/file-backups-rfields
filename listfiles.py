import os
import shutil

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

def backupDir(src,dest):
    assert(os.path.isdir(src))
    srcDir = os.path.abspath(src)
    srcFiles = os.listdir(srcDir)

    if not os.path.exists(dest):
        os.makedirs(dest)
    assert(os.path.isdir(dest))

    for file in srcFiles:
        # Don't copy hidden files
        if not file.startswith('.'):
            # Don't overwrite destination files
            destFile = os.path.abspath(file)
            if not os.path.exists(destFile):
                shutil.copy(file,dest)

backupDir('.','/home/mbexegc2/Downloads/pytest/')
