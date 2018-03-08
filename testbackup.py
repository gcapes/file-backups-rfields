# Test code during development.
import logsheet as ls

ls.createlogsheet('/home/gerard/Downloads/temp')
ls.copydirusinglogsheet('/home/gerard/Downloads/temp/logsheet.txt','/home/gerard/backup')
logsheetlog = ls.findlogsheets('/home/gerard/Downloads', 'logsheet.txt')
print('With logsheet: ',logsheetlog[0])
print('Without logsheet: ',logsheetlog[1])
