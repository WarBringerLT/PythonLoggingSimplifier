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
chdir(path.dirname(argv[0])) # CHANGE THE SCRIPT WORKING  DIRECTORY TO .py File Location

## [CODE LEVELS]
Error_Codes = [ "INFO",    # ID 0
		"WARNING", # ID 1
		"ERROR",   # ID 2
		"CRITICAL" # ID 3
				   # Continue etc...
		]

## [CODE LEVELS] END
### [SCRIPT INIT] END

## [MAIN PRINT AND SAVE MODULE]
class Logging:
	def __init__(self):
		self.Timestamp = ""
		self.Todays_Date = datetime.today().strftime('%d-%m-%Y')
		self.Log_Folder = "Logs/"
		self.Log_File   = self.Log_Folder + self.Todays_Date + '.ini' # - Log file will be DD-MM-YYYY.ini Files 
		self.Verbose_Output = True # True/False - Whether show output from Logging Module
		
		# SELECT Timestamp_Setting:    "LOCALTIME" (LOCALTIME OF PC)  [DEFAULT PRINT: HH:MM:SS]
		# OR SELECT Timestamp_Setting: "RUNTIME" (RUNTIME of the app) [DEFAULT PRINT: [0.0s] ]
		self.Timestamp_Setting = "LOCALTIME"
		
		if self.Timestamp_Setting == "LOCALTIME": self.Timestamp = datetime.now().strftime('[%H:%M:%S]>')
		elif self.Timestamp_Setting == "RUNTIME": self.Timestamp = f"[{round(time()-script_init_time,3)}s]>"
			
		# Code below will check whether LOGS FOLDER exists, if not, generate one
		if not path.isdir(self.Log_Folder):
			if Logging.Verbose_Output:
				print(f"{self.Timestamp} Logs Folder was not found - attempting to create one...")
			mkdir(Log_Folder)

		# Code below will check whether there's today's file generated already, if not, generate one.
		if not path.isfile(self.Log_File):
			if self.Verbose_Output:
				print(f"{self.Timestamp} Today's Log File was not found - attempting to create one...")
			logfile = open(self.Log_File,'w')
			logfile.write(f"#> Log File was first generated at {ctime()}.")
			logfile.close()

	def log(self,code, message, ifprint = True):
		# self    = self.
		# code    = Error Code 
		# Message = Contents of Log Message
		# ifprint = if True (default) will print the message to app
		#however, messages can be suppresed (to log only) with no output/silent
		#if specified with False parameter

		FinalLog = f"{self.Timestamp} [{Error_Codes[int(code)]}] - {message}"
		f = open(self.Log_File,'a')
		f.write('\n'+FinalLog)
		f.close()
		if self.Verbose_Output or ifprint:
			Logging.print(code,message)
		return True

	def print(self,code, message):
		# Output of the Log After Storing
		FinalLog = f"{self.Timestamp} [{Error_Codes[int(code)]}] - {message}"
		print(FinalLog)
		return True

## [MAIN PRINT AND SAVE MODULE] END

## %% ON START %% ##
Logging = Logging() # INITIALIZE Logging System
# Print Succesfull Start
Logging.log(0,f"Logging Started - Init Successful - Time Taken: {time()-script_init_time}s")

if __name__ == "__main__": # IF SCRIPT IS LAUNCHED DIRECTLY
	print(f"Log File: {Logging.Log_File}")
	print(f"File Directory Created: {path.isfile(Logging.Log_File)}")
	print(f"Found Total: {len(Error_Codes)} Error_Codes Codes. Cycling Through All of them")
	for item in Error_Codes:
		Code_Number = int(Error_Codes.index(item))
		Logging.log(Code_Number,f"Testing Error Code: {item} (CODE: {Code_Number})")


##### README:
#
# TO USE IN YOUR OWN PYTHON SCRIPT (TO YOUR OTHER FILE ADD)
#
# from Logger.py import *
#
# Usage:
# Logging.log(CODE_NUMBER, MESSAGE) 
# 
# It will automatically create log folder, create log file, and insert all messages
# that were "announced" in the app
