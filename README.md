# Cyber-Hackathon
## Terminal History Spoofer  - 5th Semester Ethical hacking project 

Created by - 

1. Antas Sharma (E20CSE243)
2. Oruganti Sampath Srikar (E20CSE255)
3. Sarthak Sharma (E20CSE164)

### Description - 

This is a simple tool that can be used to spoof your terminal history for some commands.

In this project we are only considering 40 commands such as password brute forcing commands, information gathering commands, etc. 

These 40 Commands are those that can be used for attacking other systems.

### Working - 

The project consists of three files - a python script, a shell script and a text file.

The shell script does a few things - first it pauses the history and gives the python file execution rights 

Then it copies the history file into the hist.txt

Then it runs the python file.

The python script simply reads the history that is copied into the hist.txt file and replaces all commands that are in the list of the 40 commands that can be used to attack 
other devices, with any random command from a list of 20 other commands. 

In this project, we have only taken 20 commands, but more can be taken.

These changes are reflected in the hist.txt file.

Then, it resumes the history and overwrites the .bash_history(or .zsh_history in our case) with the hist.txt file.

So, when we invoke the history in the terminal, we will get the modified history.

### Installation and Usage -

1. Go into the directory where your .bash_history ( .zsh_history in our case) file is stored.
2. Clone this repository and copy the contents of this repo to one directory up so (in the directoy where the history file is stored).
3. Give the shell script execution rights using ```chmod +x driver.sh```.
4. Run the shell script(in the background if you want to keep it running)
5. Check using the history file - ```cat .zsh_history```
