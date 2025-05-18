import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('localhost', 12345))

server_socket.listen(1)

print('Сервер очікує підключення')

connection, address = server_socket.accept()

print(f'Підключився клієнт: {address}')

data = connection.recv(1024).decode()

print(f'Отримано повідомлення від клієнта: {data}')

connection.send('Привіт від сервера!'.encode())

connection.close()

server_socket.close()