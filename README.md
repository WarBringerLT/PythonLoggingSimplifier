# PythonLoggingSimplifier
It will automatically create log folder, create log file, and insert and add all data. 
TO USE IN YOUR OWN PYTHON SCRIPT (TO YOUR OTHER FILE ADD)
and it will handle the rest of work. Works really fast,
takes almost no memory and is very simple yet advanced and scalable.

    from Logger.py import *
    Logging.log(CODE_NUMBER, MESSAGE) 

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
