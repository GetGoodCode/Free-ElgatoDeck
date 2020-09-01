# Free-ElgatoDeck
The deal behind this repo is to provide users with a script to behave the same way an Elgato streaming deck can without actually purchasing one. This will be constantly modified and altered to suite music demands, UI customization including actual buttons and eventually issuing command/programs, etc.
1.	Installation process: 

For beginners, I recommend either utilizing the original Python IDLE which is free or PyCharm which is another tool more robust and ideal than the typical IDLE.

Required modules if utilizing the IDLE are integrated on either Windows via the command line or on Linux via the terminal. Execute this command “pip3 install pynput” to install the pynput library and integrate it on system variables on a windows system by heading to MY PC > Right Click > Properties > Environment Variables > under system variables add a path depends on where the script is going to be located.

PyCharm users can repeat the same process as IDLE. This tool can install the required module by selecting the bulb icon in front of line numbers and select “install pynput  package”.

Anyone utilizing Visual Studio can head to tools > Python Environments and top right side a new menu opens. Change from “Overview” mode to “Package (PyPI)” and search the required modules to install.

Modules required to install: pynput, pygame and keyboard.

Commands for IDLE and PhCharm:
Pynput: “pip3 install pynput”
Pygame: “pip3 install pygame”
Keyboard: “pip3 install keyboard”

2.	V1 of the stream deck project is capable of playing 8 music tracks from a static directory at the same time with just a click of a button. Keep in mind of the comments to determine which parts should be modified.

GUI integration is in the process…await further updates. 
