import socket, threading
import database_chat as dbc

FORMAT = 'utf-8'

def accept_client(): 
    while True: 
        cli_sock, cli_add = ser_sock.accept()
        CONNECTION_LIST.append(cli_sock)
        thread_client = threading.Thread(target = receive_data, args=[cli_sock, cli_add])
        thread_client.start()

def receive_data(cli_sock, cli_add):
    while True:
        data = cli_sock.recv(128)
        new = data.decode(FORMAT).split(">")
        print(new)
        if new[0] == 'sup':
            insert_user = dbc.signup_server_db(new[1],cli_add[0])
            if not insert_user:
                msg = '400'
                cli_sock.send(msg.encode(FORMAT))
            else:
                msg = '500'
                cli_sock.send(msg.encode(FORMAT))
        elif new[0] == 'sig':
            check_user = dbc.signin_server_db(new[1])
            if check_user:
                msg = '200'
                cli_sock.send(msg.encode(FORMAT))
            else:
                msg = '300'
                cli_sock.send(msg.encode(FORMAT))
        elif new[0] == 'msg':
            dbc.message_server_db(new[1])
            send_to_usr(cli_sock, new[1])

def send_to_usr(cli_sock, data):
    for client in CONNECTION_LIST:
        if client != cli_sock:
            client.send(data.encode(FORMAT))

if __name__ == "__main__":
    CONNECTION_LIST = []

    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    HOST = 'localhost'
    PORT = 5023
    ser_sock.bind((HOST, PORT))

    # listen    
    ser_sock.listen(3)
    print('Chat server started on port : ' + str(PORT))

    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()