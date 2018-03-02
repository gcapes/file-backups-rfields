# Data backup for NGI Energy Lab

## The task
- Files are manually backed up to a shared drive
	- This should be automated instead
- Metadata is recorded by the instruments in log files
	- Extract key information and make it more accessible
- Key information is recorded on a paper log sheet
	- This needs to be associated with the backed up data
	- Organise the files in a directory structure which reflects this

## Requirements and questions
- Confirm files have been copied
- Delete files from original location
- Is there just one directory (with subdirectories) for each PC?
	- Yes
- Preserve time stamps of files. Permissions not important.
- Will all files be complete, or will any need appending to?
	- Complete.

## Update
- 5 pieces of information on a paper log sheet, which should
go into the file/directory name (read from file / manual prompt)
	- creator
	- date
	- investigation ID
	- experiment ID
	- general ID
- Suggested directory structure
	- Creator
		- Experiment ID
			- Date
				- General ID
- Technique should also form part of the filename
	- extract from data file
- Create a README file containing
	- serial number
	- software number
	- firmware version
	- technique

## Questions
- There may be multiple outputs per file -- I have just taken the first complete set of information.
    - Do I need to check that every output within a file contains the same information?
- Do the filenames actually need to change?
    - Or am I including all the information in the directory structure,
    and then just copying all the files?
- Should I get the date from a logfile rather than user input from the logsheet?