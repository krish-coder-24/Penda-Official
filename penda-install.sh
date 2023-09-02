

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

clear
[[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo -e ${m} "You must be root to run the script${n}"; echo ; exit 1; }

if [ -d /data/data/com.termux/files/usr/share ];then
   if [ -d /data/data/com.termux/files/usr/share/penda_pl ];then
      echo -e ${m} "Already Installed !!"
      exit 0
   else
      echo -e ${k}"Installing For Termux..."
      cd ~/../usr/share/
      git clone https://github.com/krish-coder-24/Penda-Official.git penda_pl
      mv ~/../usr/share/penda_pl/penda ~/../usr/bin/
      chmod +x ../bin/penda
      mkdir ~/.penda
      mv ~/../usr/share/penda_pl/penda-install.sh ~/.penda/ 
      cd
      echo -e ${h} "Succesfully Installed !!"
   fi

elif [ -d /usr/share ];then
   if [ -d /usr/share/penda_pl ];then
      echo -e ${m} "Already Installed !!"
      exit 0

   else
      echo -e ${k} "Installing For kali ..."
      cd /usr/share/
      git clone https://github.com/krish-coder-24/Penda-Official.git penda_pl
      mv /usr/share/penda_pl/penda /usr/bin/
      chmod +x ../bin/penda
      mkdir /home/kali/.penda
      mv /usr/share/penda_pl/penda-install.sh /home/kali/.penda/
      cd
      echo -e ${h} "Succesfully Installed !!"
   fi
fi
