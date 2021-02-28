import socket, threading
from time import sleep

FORMAT = 'utf-8'

def send_sig_sup(action):
    cli_sock.send(action.encode(FORMAT))

def send_msg():
    message = input()
    action = f"msg>{username}: {message}"
    cli_sock.send(action.encode(FORMAT))

def receive():
    while True:
        sleep(1)
        data = cli_sock.recv(128)
        data = data.decode("utf-8")
        if data == '300':
            print("This username doesn't exist")
            break
        elif data == '400':
            print('This username already exists')
            break
        elif data == '500':
            print('Welcome')
        else:
            print(data)
            send_msg()

if __name__ == "__main__":   

    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = 'localhost'
    PORT = 5023
    cli_sock.connect((HOST, PORT))     
    print('Connected to remote host...')
    
    option = input('Enter what you want to do : Signup (sup) / Signin (sig) : ')
    username = input('Enter your username : ')
    action = f"{option}>{username}"

    thread_receive = threading.Thread(target = receive)
    thread_receive.start()

    if option == 'sup':
        sup_send = threading.Thread(target=send_sig_sup, args = [action])
        sup_send.start()
    elif option == 'sig':
        sup_send = threading.Thread(target=send_sig_sup, args = [action])
        sup_send.start()