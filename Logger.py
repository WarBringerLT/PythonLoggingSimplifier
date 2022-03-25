###############################################################
#                                                             #
#               LOGGER MODULE by WarBringerLT                 #
#                       25 - 03 - 2022                        #
#                                                             #
###############################################################

### [All Other Dependent Modules]
from os import path, chdir, mkdir
from sys import argv
from time import ctime, time
from datetime import datetime
### [All Other Dependent Modules] END


### [SCRIPT INIT]

script_init_time = time() # Calculate how long it took for the module to load later

Todays_Date = datetime.today().strftime('%d-%m-%Y')
Log_Folder = "Logs/"
Log_File   = Log_Folder + Todays_Date + '.ini' # - Log file will be DD-MM-YYYY.ini Files 
Timestamp = datetime.now().strftime('[%S:%M:%H]>')

Verbose_Output = True # True/False - Whether show output from Logging Module

chdir(path.dirname(argv[0])) # CHANGE THE SCRIPT WORKING  DIRECTORY TO .py File Location

## [CODE LEVELS]
Error_Codes = [ "INFO",    # ID 0
				"WARNING", # ID 1
				"ERROR",   # ID 2
				"CRITICAL" # ID 3
						   # Continue etc...
				]

## [CODE LEVELS] END

# Code below will check whether LOGS FOLDER exists, if not, generate one

if not path.isdir(Log_Folder):
	if Verbose_Output:
		print(f"{Timestamp} Logs Folder was not found - attempting to create one...")
	mkdir(Log_Folder)

# Code below will check whether there's today's file generated already, if not, generate one.
if not path.isfile(Log_File):
	if Verbose_Output:
		print(f"{Timestamp} Today's Log File was not found - attempting to create one...")
	logfile = open(Log_File,'w')
	logfile.write(f"#> Log File was first generated at {ctime()}.")
	logfile.close()

### [SCRIPT INIT] END


## [MAIN PRINT AND SAVE MODULE]

class Logging:
	def log(code, message):
		FinalLog = f"{Timestamp} [{Error_Codes[int(code)]}] - {message}"
		f = open(Log_File,'a')
		f.write('\n'+FinalLog)
		f.close()
		Logging.print(code,message)
		return True

	def print(code, message):
		FinalLog = f"{Timestamp} [{Error_Codes[int(code)]}] - {message}"
		print(FinalLog)
		return True

## [MAIN PRINT AND SAVE MODULE] END

## %% ON START %% ##
Logging.log(0,f"Logging Started - Init Successful - Time Taken: {script_init_time-time()}s")



if __name__ == "__main__": # IF SCRIPT IS LAUNCHED DIRECTLY
	print(f"Log File: {Log_File}")
	print(f"File Directory Created: {path.isfile(Log_File)}")
	print(f"Found Total: {len(Error_Codes)} Error_Codes Codes. Cycling Through All of them")
	for item in Error_Codes:
		Code_Number = int(Error_Codes.index(item))
		Logging.log(Code_Number,f"Testing Error Code: {item} (CODE: {Code_Number})")

	

# TO USE IN YOUR OWN PYTHON SCRIPT (TO YOUR OTHER FILE ADD)
#
# from Logger.py import *
#
# Usage:
# Logging.log(CODE_NUMBER, MESSAGE) 
# 
# It will automatically create log folder, create log file, and insert and add all data. 