###############################################################
#                                                             #
#               LOGGER MODULE by WarBringerLT                 #
#                       25 - 03 - 2022                        #
#                                                             #
###############################################################

### [All Dependent Modules]
from os import path, chdir, mkdir
from sys import argv
from time import ctime, time
from datetime import datetime
#################################

### [SCRIPT INIT]
script_init_time = time() # Calculate how long it took for the module to load later
chdir(path.dirname(argv[0])) # CHANGE THE SCRIPT WORKING  DIRECTORY TO .py File Location

## [ERROR CODE LEVELS]
Error_Codes = [ "INFO",    # ID 0
				"WARNING", # ID 1
				"ERROR",   # ID 2
				"CRITICAL" # ID 3
				] # Continue etc...

## [MAIN PRINT AND SAVE MODULE]
class Logging:
	Timestamp = "" # ONLY DECLARATION OF VALUE - DO NOT EDIT - DYNAMIC CACHE VARIABLE
	Todays_Date = datetime.today().strftime('%d-%m-%Y')
	Log_Folder = "Logs/"
	Log_File   = Log_Folder + Todays_Date + '.ini' # - Log file will be DD-MM-YYYY.ini Files 
	Verbose_Output = True # True/False - Whether show output from Logging Module
	
	def __init__(self):
		global Timestamp,Todays_Date,Log_Folder,Log_File,Verbose_Output
		
		# SELECT Timestamp_Setting:    "LOCALTIME" (LOCALTIME OF PC)  [DEFAULT PRINT: HH:MM:SS]
		# OR SELECT Timestamp_Setting: "RUNTIME" (RUNTIME of the app) [DEFAULT PRINT: [0.0s] ]
		self.Timestamp_Setting = "LOCALTIME"
		
		if self.Timestamp_Setting == "LOCALTIME": self.Timestamp = datetime.now().strftime('[%H:%M:%S]>')
		elif self.Timestamp_Setting == "RUNTIME": self.Timestamp = f"[{round(time()-script_init_time,3)}s]>"
			
		# Code below will check whether LOGS FOLDER exists, if not, generate one
		if not path.isdir(self.Log_Folder):
			if self.Verbose_Output:
				print(f"{self.Timestamp} Logs Folder was not found - attempting to create one...")
			mkdir(self.Log_Folder)

		# Code below will check whether there's today's file generated already, if not, generate one.
		if not path.isfile(self.Log_File):
			if self.Verbose_Output:
				print(f"{self.Timestamp} Today's Log File was not found - attempting to create one...")
			logfile = open(self.Log_File,'w')
			logfile.write(f"#> Log File was first generated at {ctime()}.")
			logfile.close()

	def log(self, code, message, ifprint = True):
		# self    = self.
		# code    = Error Code 
		# Message = Contents of Log Message
		# ifprint = if True (default) will print the message to app
		#however, messages can be suppresed (to log only) with no output/silent
		#if specified with False parameter

		FinalLog = f"{Logging.Timestamp} [{Error_Codes[int(code)]}] - {message}"
		f = open(Logging.Log_File,'a')
		f.write('\n'+FinalLog)
		f.close()
		if Logging.Verbose_Output or ifprint:
			try:
				Logging.print(self, code, message)
			except TypeError:
				Logging.print(code, message)
		return True

	def print(self, code, message):
		# Output of the Log After Storing
		FinalLog = f"{Logging.Timestamp} [{Error_Codes[int(code)]}] - {message}"
		print(FinalLog)
		return True

## %% ON START %% ##


if __name__ == "__main__": # IF SCRIPT IS LAUNCHED DIRECTLY
	Logging = Logging() # INITIALIZE Logging System
	# Print Succesfull Start
	Logging.log(0,f"Logging Started - Init Successful - Time Taken: {time()-script_init_time}s")
	print(f"Log File: {Logging.Log_File}")
	print(f"File Directory Created: {path.isfile(Logging.Log_File)}")
	print(f"Found Total: {len(Error_Codes)} Error_Codes Codes. Cycling Through All of them")
	for item in Error_Codes:
		Code_Number = int(Error_Codes.index(item))
		Logging.log(Code_Number,f"Testing Error Code: {item} (CODE: {Code_Number})")
