<a href="https://app.codiga.io/public/user/github/<username>">
   <img src="https://app.codiga.io/public/badge/user/github/<username>" alt="Codiga badge" />
</a>

# Python Logging Simplifier
It will automatically create log folder, create log file, and append all logs.
Basically it handles the heavy lifting, while leaving blazing fast performance.
Works really fast, takes almost no memory and is very simple yet advanced and scalable.
The actual script itself consists of less than 90 lines - very **simple** 
and **robust**, making it **very efficient**.
**THERE IS ALSO STRIPPED VERSION AVAILABLE** Removed Comments, Polished Code, Shortened Lines - **ALL UNDER 50 LINES OF CODE** - AMAZING IF YOU ASK ME :))


"ifprint" parameter is not required, as by default it is set to **True**, meaning all messages
sent through logging command will end up printed on end-user's screen. It can be toggled to 
**False** to be logged in the file quietly with no screen-output. *(e.g. for back-end logging)*


**TO INSTALL:**
- Download 'logger.py' file (or logger_stripped.py)
- Put in the same folder as your other .py files

**TO USE:**

PUT AT THE TOP OF YOUR SCRIPT TO INCLUDE THIS MODULE:

	from Logger import *
(or)

	from Logger_Stripped import * # If Using Stripped Version    

And Then:

	Logger = Logging() # Initialize Logger Script

	# PUT EVERYWHERE IN YOUR CODE WHERE YOU WANT TO LOG
	
	Logger.log(Logger,"Hello",0,False) 
	
	# (Required) "Logger" Param - Engine That Was Initialized in the beginning of the script;
	# (Required) Enter the message to log (e.g. "Hello")
	# (OPTIONAL) Enter Error Code (e.g. 0)
	# (OPTIONAL) Enter ifprint Value

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
    Logger.log(Logger,"Starting Script...") 
    # < Code Below > 
    # blah blah..
    # < More Code Below >
    Logger.log(Logger,"Exiting Script...",3)  #Critical Exit Code
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
    Todays_Date = datetime.today().strftime('%d-%m-%Y')
    Log_Folder  = "Logs/"
    Log_File    = Log_Folder + Todays_Date + '.ini' # - Log file will be DD-MM-YYYY.ini Files 
    Verbose_Output = True # True/False - Whether show output from Logging Module
    
