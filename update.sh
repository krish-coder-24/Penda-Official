

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


if [ -d /data/data/com.termux/files ];then
   echo -e ${k}"Updating For Termux..."
   cd ~/../usr/share/penda_pl
   git pull
   cd
   rm -rf ~/../usr/share/penda_pl/ && rm -rf ~/../usr/share/penda_pl
   cd
   rm -rf ../usr/share/penda_pl
   bash penda-install
   echo -e ${h} "Succesfully Updated !!"

elif [ -d /usr/share/ ];then
   echo -e ${k} "Updating For kali ..."
   cd /usr/share/penda_pl
   git pull
   cd
   rm -rf /usr/share/penda_pl/  && rm -r /usr/share/penda_pl/
   sudo bash penda-install
   echo -e ${h} "Succesfully Updated !!"
fi
