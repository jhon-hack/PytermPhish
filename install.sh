#!/bin/bash
set -u
echo -e "\e[1;33mInstalando Requisitos..."
sleep 1
echo -e "\e[1;32mInstalando php..."
apt install php -y > /dev/null 2>&1
echo -e "\e[1;33mInstalando python..."
apt install python -y > /dev/null 2>&1
echo -e "\e[1;32mInstalando play-audio..."
apt install play-audio -y > /dev/null 2>&1
echo -e "\e[1;33mInstalando curl..."
apt install curl -y > /dev/null 2>&1
echo -e "\e[1;32mActualizando pip..."
pip install --upgrade pip
echo -e "\e[1;33mInstalando zip y unzip..."
apt install zip -y > /dev/null 2>&1
apt install unzip -y > /dev/null 2>&1
echo -e "\e[1;32mInstalando librería gTTS"
pip install gTTS
echo -e "\e[1;33mDescomprimiendo archivos necesarios..."
sleep 3
unzip sitios.zip

if [ -x $PREFIX/bin/ngrok ]; then
	echo "Ngrok Instalado en el sistema"
	sleep 3
	clear
	echo -e "\e[1;33mTodos los requisitos Instalados :)"
	sleep 3
	exit
fi
sleep 2
echo -e "\e[1;36mInstalando ngrok..."
echo "Descargando  ngrok en termux..."
case `dpkg --print-architecture` in
	aarch64)
    	arquitectura="arm64" ;;
	arm)
    	arquitectura="arm" ;;
	armhf)
    	arquitectura="armhf" ;;
	amd64)
    	arquitectura="amd64" ;;
	i*86)
    	arquitectura="i386" ;;
	x86_64)
    	arquitectura="amd64" ;;
	*)
    	echo "Arquitectura desconocida"
    	;;
esac
wget "https://github.com/tchelospy/NgrokTest/blob/master/ngrok-stable-linux-${arquitectura}.zip?raw=true" -O ngrok.zip > /dev/null 2>&1
unzip ngrok.zip
cat ngrok > /data/data/com.termux/files/usr/bin/ngrok
chmod 700 /data/data/com.termux/files/usr/bin/ngrok
rm ngrok ngrok.zip
clear
echo -e "\e[1;32mTodos los requisitos instalados :3"
sleep 3
exit
