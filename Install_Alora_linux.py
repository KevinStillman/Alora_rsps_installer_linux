import subprocess
import time
import shutil
import os
from pathlib import Path

print("ALORA RSPS Linux Installer by Kevin (RGH/Dumbfuck/UIM Dick)")
time.sleep(2)

print("Downloading Alora...")
#grab that shit
download_process = subprocess.Popen("wget https://alora.io/downloads/Alora.jar", shell=True)
download_process.wait()

#move that shit to like... documents!...?
print("Moving Alora.jar to Documents folder for cleanly desktop")
time.sleep(2)
downloaded_file = "./Alora.jar"
documents_folder_file = Path.home() / "Documents/Alora.jar"
shutil.copyfile(downloaded_file, documents_folder_file)
time.sleep(.5)

#delete the downloaded file (since just moving didn't work)
os.remove(downloaded_file)


#build the shell script so users don't need to run the command everytime
print("Creating Alora launcher on desktop...")
time.sleep(2)
shell_script_location = Path.home() / "Desktop/Alora.sh"
shell_script_contents = f'#!/bin/bash\ncd {Path.home() / "Documents"}\njava -jar Alora.jar'
with open(shell_script_location, "x") as shell_script_file:
	shell_script_file.write(shell_script_contents)
time.sleep(.5)


print("All done, enjoy!")
print("NOTE:")
print("If you aren't able to double click 'Alora.sh' to run the game, you may need to open a folder window and go to properties and enable 'Allow executing file as program'")
