# Python Logging Simplifier
It will automatically create log folder, create log file, and insert and add all data.
Basically it will handles the heavy work, while leaves the blazing fast performance.
Works really fast, takes almost no memory and is very simple yet advanced and scalable.
The actual script itself consists of less than 90 lines - very **simple** 
and **robust**, making it **very efficient**.

"ifprint" variable is not required, as by default it is set to **True**, meaning all messages
sent through logging command will end up printed on end-user's screen. It can be toggled to 
**False** to be logged in the file quietly with no output. *(e.g. for back-end logging)*

**THERE IS ALSO STRIPPED VERSION AVAILABLE** Removed Comments, Polished Code, Shortened Lines - **ALL UNDER 50 LINES OF CODE** - AMAZING IF YOU ASK ME :))

**TO INSTALL:**
- Download 'logger.py' file (or logger_stripped.py)
- Put in the same folder as your other .py files

**TO USE:**

	# PUT AT YOUR TOP OF THE SCRIPT
	from Logger import *
	(or)
	from Logger_Stripped import * # If Using Stripped Version    
	
	Logger = Logging() # Initialize Logger Script

	# PUT EVERYWHERE IN YOUR CODE WHERE YOU WANT TO LOG
	
	Logging.log(Logger,0,"Hello") 
	
	# logger - Use Before initialized logger,
	# then enter Error Code (e.g. 0)
	# and finally enter the message to log (e.g. "Hello")

**Default Code Numbers:**
*( You can change and create your own anytime )*

    Error_Codes = [
                "INFO",    # ID 0
                "WARNING", # ID 1
                "ERROR",   # ID 2
                "CRITICAL" # ID 3
                # Continue etc...
                ]

**EXAMPLE USAGE:**

    from Logger.py import *
    Logger = Logging() # Initialize Logger Script
    Logging.log(Logger,0,"Starting Script...") 
    # < Code Below > 
    # blah blah..
    # < More Code Below >
    Logging.log(Logger,3,"Exiting Script...") 
    exit()

**Will Produce:**

      [xx:xx:xx]> [INFO] Starting Script...
      < ... >
      [xx:xx:xx]> [CRITICAL] Exiting Script...
      
      
All Other Customisable Settings Will be in the **Logging.py** File.
Around Line ~28 There should be - **class Logging:** 
Under it, you can customise it to your liking.


**DEFAULT SETTINGS:**

    # SELECT Timestamp_Setting:    "LOCALTIME" (LOCALTIME OF PC)  [DEFAULT PRINT: HH:MM:SS]
    # OR SELECT Timestamp_Setting: "RUNTIME" (RUNTIME of the app) [DEFAULT PRINT: [0.0s]  ]
    Timestamp_Setting = "LOCALTIME"
    Timestamp = "" # ONLY DECLARATION OF VALUE - DO NOT EDIT - DYNAMIC CACHE VARIABLE
    Todays_Date = datetime.today().strftime('%d-%m-%Y')
    Log_Folder = "Logs/"
    Log_File   = Log_Folder + Todays_Date + '.ini' # - Log file will be DD-MM-YYYY.ini Files 
    Verbose_Output = True # True/False - Whether show output from Logging Module
    
