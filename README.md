# PythonLoggingSimplifier
It will automatically create log folder, create log file, and insert and add all data. 
TO USE IN YOUR OWN PYTHON SCRIPT (TO YOUR OTHER FILE ADD)
and it will handle the rest of work. Works really fast,
takes almost no memory and is very simple yet advanced and scalable.

    from Logger.py import *
    Logging.log(CODE_NUMBER~MUST BE INTEGER~, MESSAGE~STRING~) 

Default Code Numbers:
( You can change and create your own anytime )
                
    Error_Codes = [
                
                "INFO",     ID 0

                "WARNING", # ID 1
                
                "ERROR",   # ID 2
                
                "CRITICAL" # ID 3
                
                # Continue etc...
                
                ]


EXAMPLE USAGE:

      from Logger.py import *
      Logging.log(1, "Hey, How Ya Doing?") 
      

Will Produce:

      [xx:xx:xx]> [WARNING] - Hey, How Ya Doing?
      
All Other Customisable Settings Will be in the **Logging.py** File.
Around Line ~40 There should be - **LOOK FOR def __init__(self):** 
Under it, you can customise it to your liking.



DEFAULT SETTINGS:

    self.Timestamp = ""
    # SELECT MODE: LOCALTIME (LOCALTIME OF PC)
    # SELECT MODE: RUNTIME (RUNTIME of the app)
    self.Timestamp_Setting = "LOCALTIME"
    self.Todays_Date = datetime.today().strftime('%d-%m-%Y')
    self.Log_Folder = "Logs/"
    self.Log_File   = self.Log_Folder + self.Todays_Date + '.ini' # - Log file will be DD-MM-YYYY.ini Files 

    if self.Timestamp_Setting == "LOCALTIME":
        self.Timestamp = datetime.now().strftime('[%H:%M:%S]>')
    elif self.Timestamp_Setting == "RUNTIME":
        self.Timestamp = f"[{round(time()-script_init_time,3)}s]>"

    self.Verbose_Output = True # True/False - Whether show output from Logging Module
