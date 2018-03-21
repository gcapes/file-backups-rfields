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
    - Analysis etc should be added to the backed up directory.
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
### Back up directory using `backup.py`
- scan recursively for `logsheet.txt` and where present, back up that directory
    - first check that it hasn't already been backed up
    - extract information from data files, and save in `README.txt`:
        - Serial number
        - Software
        - Firmware
        - Technique
- write logfile reporting missing logfiles: `missinglogfiles.txt`
- write logfile reporting successful copies: `backuplog.txt`

### Create missing logsheets `createmissinglogsheets.py`
- after back up (or manually) prompt user for information required for missing logsheets
- `logsheet.txt` should contain the following information:
    - creator
	- date
	- investigation ID
	- experiment ID
	- general ID

### Delete backed up directories using `deleterawdata.py`
- Double checks that files have been copied before deleting from source directory
- Successful deletions reported at the prompt and in `deleteddirslog.txt`
- Problems deleting directories are reported at the prompt and in `deleteerrorlog.txt`
- Both log files are created in the data source directory

### Setting 'data' and 'backup' directories
- Edit the file `paths.txt` in the root of this repository
- `backup.py` and `createmissinglogsheets.py` will read paths from this file