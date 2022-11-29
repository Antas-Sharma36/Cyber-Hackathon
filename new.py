import sys
import fileinput
import random

orig_commands = ["dmitry","ike-scan","dmesg","legion","netdiscover","nmap","recon-ng","spiderfoot","burpsuite","skipfish","commix","sqlmap","wpscan","cewl","crunch","hashcat","john","medusa","ncrack","ophcrack","wordlists","aircrack-ng","fern-wifi-cracker","kismet","pixiewps","reaver","wifite","clang","clang++","NASM shell","radare2","crackmapexec","metasploit framework","msf payload creator","searchsploit","social engineering","dnschef","netsniff-ng","rebind","sslsplit"]
replace_commands= ["echo Hello world", "ping google.com","ifconfig","ls -a","echo $0","env","echo $USER","ls -alR","nano","vi","ls /etc/shadow","ls /mnt","sudo useradd new_user","sudo userdel new_user","chmod +x test.sh","top","dmesg","ps","ps aux","ls /proc"]
print(len(replace_commands))
i= 0
for line in fileinput.input("hist.txt", inplace=True):
    
    for i in orig_commands:
        line = line.replace(i,random.choice(replace_commands))
    
    sys.stdout.write(line)

   