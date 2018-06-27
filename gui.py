import tkinter as tk
# For some reason, the above doesn't import messagebox, so have to import separately.
import tkinter.messagebox as tkmb
import tkinter.filedialog as fd
import tkinter.ttk as ttk
import utils
import os

import backup as b
import logsheet as log


# Create main window
root = tk.Tk()
root.title("ElectroDaB: File back up utility")

# Initialise variables
pathfile = os.path.abspath("paths.txt")
data_dir = ""
backup_dir = ""


def save_paths(pathfile, data_dir, backup_dir):
    try:
        utils.savepaths(pathfile, data_dir, backup_dir)
    except FileNotFoundError as not_found_fail:
        tkmb.showerror(title="Path file error", message=not_found_fail)
    except NameError as name_fail:
        tkmb.showerror(title="Invalid paths", message=name_fail)

# Load paths from file
try:
    data_dir, backup_dir = utils.loadpaths(pathfile, 'data', 'backup')
except AssertionError as load_path_fail:
    tkmb.showerror(title="Problem with path file", message=load_path_fail)
    data_dir = fd.askdirectory(title="Select data directory")
    backup_dir = fd.askdirectory(title="Select back up directory")
    save_paths(pathfile, data_dir, backup_dir)


# Make a frame to group back up functions
backup_frame = tk.LabelFrame(master=root, text="Back up")
backup_frame.grid(row=0, column=0) # Sets row and col position of widget
        

# Button to set data directory
def browse_data_dir():
    global data_dir
    data_dir = fd.askdirectory(parent=backup_frame, initialdir=data_dir,
                               title="Select data directory")
    save_paths(pathfile, data_dir, backup_dir)
    
data_dir_button = tk.Button(backup_frame, text="Select data directory", command=browse_data_dir)
data_dir_button.grid(row=0, column=0)

# Display data directory
data_dir_display = tk.Label(backup_frame, text=data_dir)
data_dir_display.grid(row=0, column=1)


# Button to set back up directory
def browse_backup_dir():
    global backup_dir
    backup_dir = fd.askdirectory(parent=backup_frame, initialdir=backup_dir,
                                 title="Select back up directory")
    backup_dir_display.config(text=backup_dir)
    save_paths(pathfile, data_dir, backup_dir)

backup_dir_button = tk.Button(backup_frame, text="Select back up directory", command=browse_backup_dir)
backup_dir_button.grid(row=1, column=0)

# Display backup directory
backup_dir_display = tk.Label(backup_frame, text=backup_dir)
backup_dir_display.grid(row=1, column=1)

# Back up data
p = ttk.Progressbar(backup_frame, orient='horizontal', length=200, mode='indeterminate')
p.grid(row=4, column=1)


def back_up_data():
    keywords = ['Serialnumber', 'Software', 'Firmware', 'Technique']
    ext      = ('.ids','.idf')
    p.start()
    infostring = b.makebackup(data_dir, backup_dir, keywords, ext)
    p.stop()
    tkmb.showinfo(title="Back up summary", message=infostring)
    
backup_button = tk.Button(backup_frame, text="Back up data", command=back_up_data)
backup_button.grid(row=4, column=0)

# Make a frame to group logsheet functions
logsheet_frame = tk.LabelFrame(master=root, text="Log sheets")
logsheet_frame.grid(row=1, column=0) # Sets row and col position of widget

# Find missing log sheets
def find_missing_logsheets():
    log_sheet_name = "logsheet.txt"
    ignore_file = ".backupignore"
    try:
        logsheetreport = log.findlogsheets(data_dir, log_sheet_name, ignore_file)
        log.writelogsheetreport(data_dir, logsheetreport)
        tkmb.showinfo(message="Missing log sheets logged in %s" % os.path.join(data_dir, "missinglogsheets.txt"))
    except AssertionError as fail:
        tkmb.showerror(title="User error", message=fail)

find_button = tk.Button(logsheet_frame, text="Find missing logsheets", command=find_missing_logsheets)
find_button.grid(row=0, column=0)

# Display GUI
root.mainloop()
