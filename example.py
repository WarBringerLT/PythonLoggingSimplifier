from Logger import * # Import Logger Module To Your Script

Logger = Logging() # Initialize Logger Script # REQUIRED

Logger.log("Starting Script, importing other modules...") # Log as soon as the script starts, easier debugging later.
# < Code Below > 
# blah blah..
# < More Code Below >
# __ END OF SCRIPT__ 
Logger.log(f"Script Finished! Exiting",2)
exit(input())

# After running this code, have a look in the script folder, 
# a new 'Logs' folder should appear with everything you logged.
