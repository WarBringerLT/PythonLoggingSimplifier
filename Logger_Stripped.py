###############################################################
#                                                             #
#               LOGGER MODULE by WarBringerLT                 #
#                       25 - 03 - 2022                        #
#                                                             #
###############################################################
from os import path, chdir, mkdir
from sys import argv
from time import ctime, time
from datetime import datetime
script_init_time = time()
chdir(path.dirname(argv[0]))
Error_Codes = [ "INFO",    # ID 0
				"WARNING", # ID 1
				"ERROR",   # ID 2
				"CRITICAL" # ID 3
				]
class Logging:
	Timestamp = ""
	Timestamp_Setting = "LOCALTIME"
	Todays_Date = datetime.today().strftime('%d-%m-%Y')
	Log_Folder = "Logs/"
	Log_File   = Log_Folder + Todays_Date + '.ini' # - Log file will be DD-MM-YYYY.ini Files 
	Verbose_Output = True # True/False - Whether show output from Logging Module
	def __init__(self):
		global Timestamp
		self.Timestamp_Setting = Logging.Timestamp_Setting
		if self.Timestamp_Setting == "LOCALTIME": Timestamp = datetime.now().strftime('[%H:%M:%S] ')
		elif self.Timestamp_Setting == "RUNTIME": Timestamp = f"[{round(time()-script_init_time,3)}s]>"
		if not path.isdir(self.Log_Folder):
			if self.Verbose_Output: print(f"{self.Timestamp} Logs Folder was not found - attempting to create one...")
			mkdir(self.Log_Folder)
		if not path.isfile(self.Log_File):
			if self.Verbose_Output: print(f"{self.Timestamp} Today's Log File was not found - attempting to create one...")
			logfile = open(self.Log_File,'w')
			logfile.write(f"#> Log File was first generated at {ctime()}.")
			logfile.close()
	def log(self, code, message, ifprint = True):
		FinalLog = f"{Timestamp} [{Error_Codes[int(code)]}]: {message}"
		f = open(Logging.Log_File,'a')
		f.write('\n'+FinalLog)
		f.close()
		if Logging.Verbose_Output or ifprint:
			try: Logging.print(self, code, message)
			except TypeError: Logging.print(code, message)
		return True
	def print(self, code, message):
		# Output of the Log After Storing
		if self.Timestamp_Setting == "LOCALTIME": Timestamp = datetime.now().strftime('[%H:%M:%S] ')
		elif self.Timestamp_Setting == "RUNTIME": Timestamp = f"[{round(time()-script_init_time,3)}s]>"
		FinalLog = f"{Timestamp} [{Error_Codes[int(code)]}]: {message}"
		print(FinalLog)
		return True
if __name__ == "__main__": # IF USED IN ANOTHER SCRIPT ALL LINES BELOW (INCLUDING THIS LINE) CAN BE DELETED TO USE EVEN LESS SPACE
	Logging = Logging() 
	Logging.log(0,f"Logging Started - Init Successful - Time Taken: {time()-script_init_time}s")
	print(f"Log File: {Logging.Log_File}")
	print(f"File Directory Created: {path.isfile(Logging.Log_File)}")
	print(f"Found Total: {len(Error_Codes)} Error_Codes Codes. Cycling Through All of them")
	for item in Error_Codes:
		Code_Number = int(Error_Codes.index(item))
		Logging.log(Code_Number,f"Testing Error Code: {item} (CODE: {Code_Number})")
