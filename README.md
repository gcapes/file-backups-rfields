# Data backup for NGI Energy Lab

## Background
- Files are currently backed up manually to a shared drive
	- This should be automated instead
- Metadata is recorded by the instruments in log files
	- Extract key information and make it more accessible
- Key information is recorded on a paper log sheet
	- This needs to be associated with the backed up data
	- Organise the files in a directory structure which reflects this

## Behaviour
- The source (data) directory is assumed to be just that: raw data only.
Once it has been backed up, it will not be backed up again even if files are modified or added.
    - Analysis etc should be added to the backup directory.
- It is assumed that there is only one data directory containing all the experiments
- There may be multiple outputs per file -- I have just taken the first complete set of information.
- Complete directories (and subdirectories) are copied, using their original filenames.
The back up directory has subdirectory names based on the information in the logsheets.
- The date for the experiment is extracted from the datafile (`.ids` or `.idf`)
- It is assumed that `logfile.txt` will be at the same level as an `.idf` or `.ids` data file,
and that only data file will be present for all experiments.
If a directory doesn't contain an `.idf` or `.ids` file, it is either a sub-directory or
otherwise not an experimental directory.

## Usage
### Set 'data' and 'backup' directories
- Edit the file `paths.txt` in the root of this repository
- All the processing scripts (`backup.py`, `createmissinglogsheets.py`, and `deleterawdata.py`)
will read paths from this file
- The 'data' directory doesn't have to be the root directory --
it could be a user's subdirectory if they only want to back up their own data

### Back up directory using `backup.py`
- This function will scan recursively for `logsheet.txt` and where present, back up that directory
    - first it checks that it hasn't already been backed up
    - information is extracted from data files, and saved in `README.txt`:
        - Serial number
        - Software
        - Firmware
        - Technique
- logfile reporting missing logfiles: `missinglogfiles.txt`
- logfile reporting successful copies: `backuplog.txt`

### Create missing logsheets using `createmissinglogsheets.py`
- This prompts the user for information required for missing logsheets
- `logsheet.txt` will contain the following information:
    - creator
	- date
	- investigation ID
	- experiment ID
	- general ID

### Delete backed up directories using `deleterawdata.py`
- This double checks that files have been copied before deleting from source directory
- Successful deletions reported at the prompt and in `deleteddirslog.txt`
- Problems deleting directories are reported at the prompt and in `deleteerrorlog.txt`

### Log files
- All log files are created in the 'data' directory -- not the backup directory