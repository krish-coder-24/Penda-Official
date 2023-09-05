import os
from colorama import Fore, Back, Style
##############################color
m="\e[0;31m"      # merah           # red
k="\e[0;33m"      # kuning          # yellow
h="\e[0;32m"      # hijau           # green
b="\e[0;34m"      # biru            # blue
lm="\e[1;31m"     # merah terang    # pink
lk="\e[1;33m"     # kuning terang   # bright yellow
lh="\e[1;32m"     # hijau terang    # light green
lb="\e[1;34m"     # langit biru     # blue sky
n="\e[0m"         # netral          # neutral

def Uninstaller(type):
   if os.path.isfile("/data/data/com.termux/files/usr/share/penda_pl/penda_file.py"):
      if type == "Safe":
         print (Fore.RED + "Unistalling For Termux...")
         os.system("""
                  cd
                  rm -rf ../usr/share/penda_pl
                  rm ../usr/bin/penda
                  """)
         print (Fore.GREEN + "Succesfully Uninstalled !!")
      elif type == "Full":
         print (Fore.RED + "Unistalling For Termux...")
         os.system("""
                  cd
                  rm -rf ../usr/share/penda_pl && rm ../usr/bin/penda
                  rm -rf ~/.penda && rm ../usr/bin/penda-install
                  """)
         print (Fore.GREEN + "Succesfully Uninstalled !!")

   elif os.path.isfile("/usr/share/penda_pl/penda_file.py"):
      if type == "Safe":
         print (Fore.RED + "Unistalling Penda For Linux...")
         os.system("""
                  sudo rm -rf /usr/share/penda_pl && rm /usr/bin/penda
                  """)
         print (Fore.GREEN + "Succesfully Uninstalled !!")
      elif type == "Full":
         print (Fore.RED + "Unistalling Penda For Linux...")
         os.system("""
                  sudo rm -rf /usr/share/penda_pl && rm /usr/bin/penda
                  rm -r /root/.penda && rm /usr/bin/penda-install
                  """)
         print (Fore.GREEN + "Succesfully Uninstalled !!")


# if [ -d /data/data/com.termux/files/usr/share/penda_pl ];then
#    echo -e ${lm}"Do you want Uninstall it Completely (y/N)?  "
#    read choice
#    if [ $choice == "N" || $choice == "n"];then
#       echo -e ${k}"Unistalling For Termux..."
#       rm -r ~/../usr/share/penda_pl && rm ~/../usr/bin/penda
#       echo -e ${h} "Succesfully Uninstalled !!"
#    elif [ $choice == "Y" || $choice == "y"];then
#       echo -e ${k}"Unistalling For Termux..."
#       rm -r ~/../usr/share/penda_pl && rm ~/../usr/bin/penda
#       rm -r ~/.penda && rm ~/../usr/bin/penda-install
#       echo -e ${h} "Succesfully Uninstalled !!"

# elif [ -d /usr/share/penda_pl ];then
#    echo "Do you want Uninstall it Completely (y/N)?  "
#    read choice
#    if [ $choice == "N" || $choice == "n"];then
#       echo -e ${k}"Unistalling Penda For Linux..."
#       rm -r /usr/share/penda_pl && rm /usr/bin/penda
#       echo -e ${h} "Succesfully Uninstalled !!"
#    elif [ $choice == "Y" || $choice == "y"];then
#       echo -e ${k}"Unistalling Penda For Linux..."
#       rm -r /usr/share/penda_pl && rm /usr/bin/penda
#       rm -r /root/.penda && rm /usr/bin/penda-install
#       echo -e ${h} "Succesfully Uninstalled !!"
# fi
