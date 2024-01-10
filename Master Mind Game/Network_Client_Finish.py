#import module
from socket import *
import socket

#set client socket
HOST = socket.gethostname() 
PORT = 50000       
client_socket = socket.socket(AF_INET, SOCK_STREAM)

# เชื่อมต่อกับ Server
client_socket.connect((HOST, PORT))

#เริ่มเกม
while True:
    
    #รับข้อความจาก server
    message = client_socket.recv(1024).decode()
    print(message)

    #ตอบกลับ server
    if message.__contains__('Enter'): 
        number = input(': ')
        client_socket.send(number.encode())

    #เกมจบ
    elif message.__contains__('!!!Game Over!!!'):
        client_socket.close()
        break
    
    
    