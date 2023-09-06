

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



if [ -d /data/data/com.termux/files/usr/share ];then
   echo -e ${k} "Installing For Termux ..."
   cd ~/../usr/share/
   git clone https://github.com/krish-coder-24/Penda-Official.git penda_pl
   cd penda_pl
   mv penda-install_termux penda-install 
   bash penda-install
   rm penda-install_kali
   rm install.sh

elif [ -d /usr/share ];then
   if [ -d /usr/share/penda_pl ];then
      echo -e ${m} "Already Installed !!"
      exit 0

   else
      [[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo -e ${m} "You must be root to run the script${n}"; echo ; exit 1; }
      echo -e ${k} "Installing For kali ..."
      cd /usr/share/
      git clone https://github.com/krish-coder-24/Penda-Official.git penda_pl
      cd penda_pl 
      mv penda-install_kali penda-install 
      bash penda-install 
      rm penda-install_termux 
      rm install.sh
   fi
fi
