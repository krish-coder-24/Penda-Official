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
w="\e[1;37m"

###############################give Permissons,if not root user exit

[[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo -e ${m} "You must be root to run the script${n}"; echo ; exit 1; }

if [ -d /data/data/com.termux/files/usr/share/pendal_pl ];then
   echo -e ${m} "Already Installed !!"
   exit 0

elif [ -d /data/data/com.termux/files ];then
   echo -e ${k}"Installing For Termux..."
   mv ~/penda_pl ~/../usr/share/
   mv ~/../usr/share/penda_pl/penda ~/../usr/bin/
   echo -e ${h} "Succesfully Installed !!"

elif [ -d /usr/share/pendal_pl ];then
   echo -e ${m} "Already Installed !!"
   exit 0

elif [ -d /usr/share/ ];then
   echo -e ${k} "Installing For kali ..."
   cp -r  /home/kali/penda_pl /root/
   mv ~/penda_pl /usr/share/
   mv /usr/share/penda_pl/penda /usr/bin/
   echo -e ${h} "Succesfully Installed !!"
fi
