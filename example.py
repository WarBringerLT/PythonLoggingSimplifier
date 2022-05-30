from Logger_Stripped import * # Import Logger Module To Your Script

Logger = Logging() # Initialize Logger Script

Logger.log("Starting Script, importing other modules")
import os #random modules, example.
import sys  #random modules, example.

Username = os.environ.get('USERNAME')
Logger.log(f"Logged in User: {Username}")









Logger.log(f"Script Finished! Exiting",2)
exit(input())
