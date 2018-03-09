# Test code during development.
import logsheet as ls

ls.createlogsheet('/home/mbexegc2/Downloads/test/subinclude')
# Make an error with logsheet path here to test assertion
ls.copydirusinglogsheet('/home/mbexegc2/Downloads/test/subinclude/logsheet.txt','/home/mbexegc2/backup')
logsheetlog = ls.findlogsheets('/home/mbexegc2/Downloads', 'logsheet.txt')
print('With logsheet: ',logsheetlog[0])
print('Missing logsheet: ',logsheetlog[1])
# Check that directories have been backed up
# Read logsheets
# Check destination directories and files exist, and that the file sizes are the same.