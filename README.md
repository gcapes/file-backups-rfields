# Data backup for NGI Energy Lab

## The task
- Files are manually backed up to a shared drive
	- This should be automated instead
- Metadata is recorded by the instruments in a log file
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
- There may be multiple outputs per file
    - How should I deal with this? Will they always contain the same info?
    Just take the first complete set of information?
