def command_exec(m):
cid = m.chat.id
puerto = 4444
ip1 = "127.0.0.1"
ip2 = "192.168.0.191"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if cid == "CID": # Cambiar por numero cid
rpi = m.text.split()[1]
cmd = m.text[10:]
bot.send_message(cid, "Ejecutando: " + cmd)
bot.send_chat_action(cid, 'typing')

if rpi == "rpi1":
s.connect((ip1, puerto))
s.send(cmd)
elif rpi == "rpi2":
s.connect((ip2, puerto))
s.send(cmd)
s.close()
else:
bot.send_message(cid, " ¡¡PERMISO DENEGADO!!")
print(" ¡¡PERMISO DENEGADO!! ")