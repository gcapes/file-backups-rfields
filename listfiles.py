import os
import shutil


def getSrcFiles(path, allFiles):
    for fileOrDir in os.listdir(path):
        if not fileOrDir.startswith('.'):
            fullPath = os.path.join(path, fileOrDir)
            if os.path.isdir(fullPath):
                getSrcFiles(os.path.join(path, fileOrDir), allFiles)
            else:
                allFiles.append(os.path.join(path, fileOrDir))
    return allFiles


def backupDir(src, dest):
    assert (os.path.isdir(src))
    srcDir = os.path.abspath(src)
    srcFiles = os.listdir(srcDir)

    if not os.path.exists(dest):
        os.makedirs(dest)
    assert (os.path.isdir(dest))

    for file in srcFiles:
        # Don't copy hidden files
        if not file.startswith('.'):
            # Don't overwrite destination files
            destFile = os.path.abspath(file)
            if not os.path.exists(destFile):
                shutil.copy(file, dest)


def backupFiles(srcFiles, destFiles):
    # srcFiles is a list of source files
    # destFiles is a corresponding list of destination files
    assert (len(srcFiles) == len(destFiles))

    for src, dest in zip(srcFiles, destFiles):
        # Check that src exists
        assert (os.path.exists(src)), "Source file doesn't exist: %r" % src

        # If dest dir doesn't exist, create it
        destDir = os.path.dirname(os.path.abspath(dest))
        if not os.path.exists(destDir):
            os.makedirs(destDir)
        # Confirm destination directory exists before copying
        assert (os.path.exists(destDir))

        # Check that destination file doesn't already exist
        if not os.path.exists(dest):
            shutil.copyfile(src, dest)
        else:
            print('Destination file already exists: %r. File not copied.' % dest)
        # Confirm file has copied
        assert (os.path.exists(dest)), "File failed to copy. Src: %r, Dest: %r" % (src, dest)


for x in getSrcFiles('../', []):
    print(x)
backupDir('.', '/home/mbexegc2/Downloads/pytest/')
backupFiles(['listfiles.py', 'README.md'],
            ['/home/mbexegc2/Downloads/pytest/pythonfile.py', '/home/mbexegc2/Downloads/pytest/dir/markdown.md'])
