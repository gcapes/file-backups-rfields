# Structure of the problem
- List files (recursively) in data directory
- Extract any metadata
- Copy to destination, using directory structure for metadata
- Confirm files have been copied
- Delete files from original location

# Questions
- Is there just one directory (with subdirectories) for each PC?
- Do the time stamp and permissions have to be preserved?
	- Time stamps yes, permissions no.
- Will all files be complete, or will any need appending to?
	- Complete.

# Update
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
