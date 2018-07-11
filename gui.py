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

#######################
## Back up functions ##
#######################

# Initialise variables
pathfile = os.path.abspath("paths.txt")
data_dir = ""
backup_dir = ""
missing_logsheets_log = tk.StringVar()
missing_logsheets_log.set('missinglogsheets.txt')


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
    # Prompt user to locate correct path file
    data_dir = fd.askdirectory(title="Select data directory")
    backup_dir = fd.askdirectory(title="Select back up directory")
    save_paths(pathfile, data_dir, backup_dir)


# Group back up functions in a frame
backup_frame = tk.LabelFrame(master=root, text="Back up")
backup_frame.grid(row=0, column=0) # Sets row and col position of widget


# Button to set data directory
def browse_data_dir():
    global data_dir
    data_dir = fd.askdirectory(parent=backup_frame, initialdir=data_dir,
                               title="Select data directory")
    save_paths(pathfile, data_dir, backup_dir)

data_dir_button = tk.Button(backup_frame, text="Select data directory", width=25, command=browse_data_dir)
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

backup_dir_button = tk.Button(backup_frame, text="Select back up directory", width=25, command=browse_backup_dir)
backup_dir_button.grid(row=1, column=0)

# Display backup directory
backup_dir_display = tk.Label(backup_frame, text=backup_dir)
backup_dir_display.grid(row=1, column=1)

# Back up progress bar
p = ttk.Progressbar(backup_frame, orient='horizontal', length=200, mode='indeterminate')
p.grid(row=4, column=1)

# Back up data
def back_up_data():
    keywords = ['Serialnumber', 'Software', 'Firmware', 'Technique']
    ext      = ('.ids','.idf')
    p.start()
    infostring = b.makebackup(data_dir, backup_dir, keywords, ext)
    p.stop()
    tkmb.showinfo(title="Back up summary", message=infostring)

backup_button = tk.Button(backup_frame, text="Back up data", command=back_up_data, width=25)
backup_button.grid(row=4, column=0)

########################
## Logsheet functions ##
########################

# Make a frame to group logsheet functions
logsheet_frame = tk.LabelFrame(master=root, text="Log sheets")
logsheet_frame.grid(row=1, column=0, pady=10) # Sets row and col position of widget

# Find missing log sheets
def find_missing_logsheets():
    global missing_logsheets_log
    log_sheet_name = "logsheet.txt"
    ignore_file = ".backupignore"
    try:
        logsheetreport = log.findlogsheets(data_dir, log_sheet_name, ignore_file)
        log.writelogsheetreport(data_dir, logsheetreport)
        missing_logsheet_file = os.path.join(data_dir, missing_logsheets_log.get())
        tkmb.showinfo(message="Missing log sheets logged in %s" % missing_logsheet_file)
        missing_logsheets_log.set(missing_logsheet_file)
        missing_logsheet_label = tk.Label(logsheet_frame, text=missing_logsheets_log.get())
        missing_logsheet_label.grid(row=1, column=0)

    except AssertionError as fail:
        tkmb.showerror(title="User error", message=fail)

find_button = tk.Button(logsheet_frame, text="Find missing logsheets", command=find_missing_logsheets)
find_button.grid(row=0, column=0)

# Group widgets used to create missing logsheets
create_logsheet_frame = tk.LabelFrame(master=logsheet_frame, text="Create logsheets")
create_logsheet_frame.grid(row=2)

# Declare variables
exp_num = tk.IntVar()
exp_path = tk.StringVar()

def load_experiment_path(data_dir):
    '''
    Read missinglogsheets.txt file to get path to experiment directory specified
    by exp_number.
    data_dir: directory containing the data,
              with separate directories for each experiment.
    '''
    global missing_logsheets_log
    global exp_path
    try:
        missinglogs = os.path.join(data_dir, missing_logsheets_log.get())
        with open(missinglogs, 'r') as f:
            for line_num, line in enumerate(f):
                if line_num == exp_num.get():
                    exp_path.set(line.strip('\n'))
                    current_experiment_display.configure(text=exp_path.get())
                    break
            if exp_num.get() > line_num:
                    tkmb.showinfo(title="Complete", message="No more logsheets to process.")

    except FileNotFoundError as not_found:
        tkmb.showerror(title="Can't find missing logsheets file", message=not_found)


def get_first_experiment_path():
    '''
    Reset experiment number to zero, i.e. start at the beginning of the
    missinglogsheets.txt file, and load path to experiment.
    '''
    global exp_num
    exp_num.set(0)
    # load first experiment
    load_experiment_path(data_dir)
    load_experiment_date()


# Button to load first missing logsheet
first_logsheet_button = tk.Button(create_logsheet_frame, text="Start", command=get_first_experiment_path)
first_logsheet_button.grid(row=1, column=0)

def get_next_experiment_path():
    '''
    Advance to next experiment in missinglogsheets.txt, and load
    path to experiment.
    '''
    counter = exp_num.get()
    counter +=1
    exp_num.set(counter)
    # load this experiment
    load_experiment_path(data_dir)
    load_experiment_date()

# Load next experiment with missing logsheet
next_logsheet_button = tk.Button(create_logsheet_frame, text="Get next", command=get_next_experiment_path)
next_logsheet_button.grid(row=1, column=1)

# Label widget to diplay current experiment
current_experiment_display = tk.Label(create_logsheet_frame)
current_experiment_display.grid(row=2, column=1)

current_exp_label = tk.Label(create_logsheet_frame, text="Current experiment:")
current_exp_label.grid(row=2, column=0, sticky="e")

# Entry widgets to get user input
creator = tk.StringVar()
exp_ID = tk.StringVar()
gen_ID = tk. StringVar()
exp_date = tk.StringVar()

creator_label = tk.Label(create_logsheet_frame, text="Creator:")
creator_label.grid(row=3, column=0, sticky="e")
creator_display = tk.Entry(create_logsheet_frame, textvariable=creator)
creator_display.grid(row=3, column=1)

#experiment id
exp_id_label = tk.Label(create_logsheet_frame, text="Experiment ID:")
exp_id_label.grid(row=4, column=0, sticky="e")
exp_id_display = tk.Entry(create_logsheet_frame, textvariable=exp_ID)
exp_id_display.grid(row=4, column=1)

#general id
gen_id_label = tk.Label(create_logsheet_frame, text="General ID:")
gen_id_label.grid(row=5, column=0, sticky="e")
gen_id_display = tk.Entry(create_logsheet_frame, textvariable=gen_ID)
gen_id_display.grid(row=5, column=1)

#display date
date_label = tk.Label(create_logsheet_frame, text="Date (YYYYMMDD):")
date_label.grid(row=6, column=0, sticky="e")
date_display = tk.Label(create_logsheet_frame)
date_display.grid(row=6, column=1)

def load_experiment_date():
    global exp_date
    global exp_path
    try:
        exp_date.set(log.getdatefromdatafile(exp_path.get()))
        date_display.config(text=exp_date.get())
    except NameError as filenameerror:
        tkmb.showerror(title="Data file not found", message=filenameerror)
    except ValueError as datenotfound:
        tkmb.showerror(title="Date not found", message=datenotfound)
    except AssertionError as invalidpath:
        tkmb.showerror(title="File not found", message=invalidpath)


# Button to write log sheet
def write_logsheet():
    global exp_path
    global exp_ID
    global gen_ID
    global creator
    global exp_date

    try:
        logsheet = os.path.join(exp_path.get(), 'logsheet.txt')
        logsheetinfo = ['Creator: ' + creator.get(), 'Experiment ID: ' + exp_ID.get(),
                        'Date: ' + exp_date.get(), 'General ID: ' + gen_ID.get()]

        if os.path.exists(logsheet):
            # A logsheet might already exist if user hasn't re-run `find missing logsheets`
            response = tkmb.askyesno(title='File already exists', message='Overwrite existing logsheet?')
            if not response:
                return

        utils.writelisttofile(logsheetinfo,logsheet)
    except NameError as dirnotfound:
        tkmb.showerror(title="Directory not found", message=dirnotfound)


write_logsheet_button = tk.Button(create_logsheet_frame, text="Create", command=write_logsheet)
write_logsheet_button.grid(row=7, column=0)

# Display GUI
root.mainloop()
