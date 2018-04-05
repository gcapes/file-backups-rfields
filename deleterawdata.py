"""
Delete source data files.
Confirm that back up was successful before deleting.
"""

import os
import csv
import utils
import datetime

pathfile = os.path.abspath("paths.txt")
srcdir, backupdir = utils.loadpaths(pathfile, 'data', 'backup')

backuplog = os.path.join(srcdir, "backuplog.txt")
assert os.path.isfile(backuplog), "File not found: % s" % backuplog

# Load back up log
with open(backuplog, 'r') as tsv:
    tsv = csv.reader(tsv, delimiter='\t')
    data = list(tsv)

# Delete header row
del data[0]

deletedlog = os.path.join(srcdir, "deleteddirslog.txt")
errorlog = os.path.join(srcdir, "deleteerrorlog.txt")

# Create log file if it doesn't already exist
if not os.path.isfile(deletedlog):
    header = "Time\tSource directory (deleted)\tBack up directory\n"
    with open(deletedlog, 'w') as logfile:
        logfile.write(header)

# Delete directories and write log file
with open(deletedlog, 'a') as logfile, open(errorlog, 'w') as errorfile:
    header = "Time\tSource directory (not deleted)\tBack up directory\tReason\n"
    errorfile.write(header)
    for row in data:
        srcdir = row[1]
        backupdir = row[2]
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = "{0}\t{1}\t{2}\n".format(now, srcdir, backupdir)
        
        # If srcdir doesn't exist, it can't be deleted
        # If back up doesn't exist, something has gone wrong,
        # and srcdir needs backing up again
        if os.path.isdir(srcdir) and os.path.isdir(backupdir):
            if utils.deletebackedupdir(srcdir, backupdir):
                logfile.write(log)
            else:
                log = log.strip() + "\tSource and back up are different\n"
                errorfile.write(log)
        else:
            if not os.path.isdir(srcdir):
                log = log.strip() + "\tSource dir not found\n"
            if not os.path.isdir(backupdir):
                log = log.strip() + "\tBack up dir not found\n"
            errorfile.write(log)
print("Delete complete.")
print("See log and error files for further details:\n%s\n%s" % (deletedlog, errorlog))
