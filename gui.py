import tkinter as tk
# For some reason, the above doesn't import messagebox, so have to import separately.
import tkinter.messagebox as tkmb
import tkinter.filedialog as fd
import utils
import os

import backup as b
import logsheet as log


# Create main window
root = tk.Tk()
root.title("ElectroDaB: File back up utility")


# Initialise variables
pathfile = os.path.abspath("paths.txt")
try:
    data_dir, backup_dir = utils.loadpaths(pathfile, 'data', 'backup')
except AssertionError as load_path_fail:
    tkmb.showerror(title="Path file missing!", message=load_path_fail)

# Make a frame to group back up functions
backup_frame = tk.LabelFrame(master=root, text="Back up")
backup_frame.grid(row=5, column=2) # Sets maximum number of rows and cols
        
# Button to set data directory
def browse_data_dir():
    global data_dir
    data_dir = fd.askdirectory(parent=backup_frame, initialdir=data_dir)
    data_dir_display.config(text=data_dir)
    try:
        utils.savepaths(pathfile, data_dir, backup_dir)
    except AssertionError as assert_fail:
        tkmb.showerror(title="Path file error", message=assert_fail)
    except NameError as name_fail:
        tkmb.showerror(title="Invalid paths", message=name_fail)
    
data_dir_button = tk.Button(backup_frame, text="Select data directory", command=browse_data_dir)
data_dir_button.grid(row=0, column=0)

# Display data directory
data_dir_display = tk.Label(backup_frame, text=data_dir)
data_dir_display.grid(row=0, column=1)


# Button to set back up directory
def browse_backup_dir():
    global backup_dir
    backup_dir = fd.askdirectory(parent=backup_frame, initialdir=backup_dir)
    backup_dir_display.config(text=backup_dir)
    try:
        utils.savepaths(pathfile, data_dir, backup_dir)
    except AssertionError as assert_fail:
        tkmb.showerror(title="Path file error", message=assert_fail)
    except NameError as name_fail:
        tkmb.showerror(title="Invalid paths", message=name_fail)

backup_dir_button = tk.Button(backup_frame, text="Select back up directory", command=browse_backup_dir)
backup_dir_button.grid(row=1, column=0)

# Display backup directory
backup_dir_display = tk.Label(backup_frame, text=backup_dir)
backup_dir_display.grid(row=1, column=1)


# Find missing log sheets
log_sheet_name = "logsheet.txt"

def find_missing_logsheets():
    try:
        ignore_file = ".backupignore"
        logsheetreport = log.findlogsheets(data_dir, log_sheet_name, ignore_file)
        log.writelogsheetreport(data_dir, logsheetreport)
    except AssertionError as fail:
        tkmb.showerror(title="User error", message=fail)

find_button = tk.Button(backup_frame, text="Find missing logsheets", command=find_missing_logsheets)
find_button.grid(row=3, column=0)


# Display GUI
root.mainloop()
