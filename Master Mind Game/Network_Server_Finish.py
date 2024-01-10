#import module
from socket import *
import socket
import random as rd

#set server socket
HOST = socket.gethostname()
IP = socket.gethostbyname(HOST)
PORT = 50000 
server = socket.socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(IP,' ',HOST)

#random number
def Create_number():
    n = [0,1,2,3,4,5,6,7,8,9]
    sn = rd.sample(n, k=6)
    return sn
number = Create_number()
number_string = [str(i) for i in number]
number_show = ''.join(number_string)
number_show_end = ' '.join(number_string)

#check ans
def check(data):
    ans = [int(i) for i in data]
    n_ans = ' '.join(data)
    count1 = 0
    count2 = 0
    if number == ans:
        return 'win'
    else:
        for i in range(0,6):
            if number[i] == ans[i]:
                count1 += 1
            else :
                for j in range(0,6):
                    if number[i] == ans[j]:
                        count2 += 1
        return f'ใส่ค่า [ {n_ans} ] เครื่องแม่ข่ายตอบ {count1} {count2} [ {n_ans} ]'
    
# set game
players = []
rounds = 0
current = 0
names = []

#show ans
print("The answer is:",number_show)

#Enter number player
nroom = int(input('Enter the number in room: '))


while True:    
    print('Waiting for connection')	
    
    #เชื่อมต่อกับ client
    client_socket, address = server.accept()
    
    #เก็บ socket ของ client ใน players
    players.append(client_socket)
    
    #รับชื่อผู้เล่นแล้วเก็บ
    client_socket.send('Enter your name '.encode())
    name = client_socket.recv(1024).decode()
    names.append(name)
    
    #ประกาศให้รอผู้เล่นอื่นเชื่อมต่อ
    if nroom != 1:
        client_socket.send('Wait a minute....'.encode())
    
    #เริ่มเกมเมื่อคนครบ
    if len(players) >= nroom:
        
        #ประกาศบอกผู้เล่นทุกคนว่าเกมเริ่ม
        for player in players:
            player.send('***Game Start*** \n'.encode())

        while True:
            
            #ลำดับของผู้เล่น
            current = rounds%nroom
            
            #ประกาศบอกผู้เล่นทุกคนว่าถึงรอบใคร
            for player in players:
                player.send(f'รอบเล่นของผู้เล่น: {names[current]}\n'.encode())
            
            #รับคำตอบจากผู้เล่นในรอบนั้น
            players[current].send('Enter 6 number '.encode())
            data = players[current].recv(1024).decode().strip()
            
            #ตรวจสอบคำตอบที่ได้
            while len(data) != 6 or len(set(data)) != 6 or not data.isdigit():
                players[current].send('Enter 6 number again '.encode())
                data = players[current].recv(1024).decode().strip()

            #แสดงรอบเล่น
            print(f'รอบที่ {rounds+1} ผู้เล่น {names[current]} ตอบ {data}')
            
            #แสดงผลจากการเช็ค
            response = check(data)
            
            #ถ้าคำตอบถูกให้จบเกมและประกาศบอกผู้เล่นทุกคน
            if response == 'win':
                for player in players:
                    player.send(f'!!!Game Over!!! The winner is Player {names[current]} and The correct number : [ {number_show_end} ]'.encode())
                break
            
            #ถ้าไม่ถูกให้ประกาศบอกผู้เล่นทุกคน
            else:    
                for player in players:
                    player.send(f'รอบที่ {rounds+1} ผู้เล่น {names[current]} {response}'.encode())
            
            #นับรอบ
            rounds += 1

            #เช็ครอบเล่น
            if rounds == 12:
                break
            
        #ประกาศเมื่อหมดเวลา
        for player in players:
            player.send(f'!!!Game Over!!! and The correct number : [ {number_show_end} ]'.encode())
        break

print('End Game')
#ยกเลิกการเชื่อมต่อ
client_socket.close()