# =============================version 1=============================
import os
os.system("ssh root@185.43.7.52")
uname = os.system("pwd")
os.system("exit")
print(uname)
# os.system("")


# # =============================version 2=============================
# import paramiko
# # Создаем объект ssh для подключения к удаленному серверу
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # Подключаемся к удаленному серверу по имени хоста и порту
# ssh.connect('myserver.example.com', port=22)
# # Получаем сессию для работы с удаленным сервером
# session = ssh.open_session()
# # Выполняем команду "ls"
# command = 'ls'
# session.exec_command(command)
# # Получаем вывод команды и выводим его в консоль
# output = session.get_channel().makefile('rb')
# print(output.read().decode('utf-8'))
# # Закрываем сессию и соединение с сервером
# output.close()
# session.close()
# ssh.close()


# =============================version 3=============================
# asdfsadf
# asdf
# asdf
# asdf