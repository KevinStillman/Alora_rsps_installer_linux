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


#build the desktop launcher file so users can double-click to run
print("Creating Alora launcher on desktop...")
time.sleep(.5)
desktop_file_location = Path.home() / "Desktop/Alora.desktop"
desktop_file_contents = f'''[Desktop Entry]
Version=1.0
Type=Application
Name=Alora RSPS
Comment=Launch Alora RSPS Game
Exec=java -jar {Path.home() / "Documents/Alora.jar"}
Path={Path.home() / "Documents"}
Terminal=false
Icon=applications-games
Categories=Game;
'''
with open(desktop_file_location, "w") as desktop_file:
	desktop_file.write(desktop_file_contents)

# Make the desktop file executable
os.chmod(desktop_file_location, 0o755)

# Mark the desktop file as trusted (for GNOME and similar desktop environments)
try:
	subprocess.run(f'gio set "{desktop_file_location}" metadata::trusted true', shell=True, check=False)
except:
	pass  # If gio isn't available, the chmod should be enough for most systems

time.sleep(.5)


print("All done, enjoy!")
print("You can now double-click 'Alora.desktop' on your desktop to launch the game!")
