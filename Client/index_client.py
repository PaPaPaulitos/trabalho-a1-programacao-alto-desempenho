import threading
import socket
import sys

def cripto(key: int, word: str) -> str:
    cripto_word = ''
    for i in word:
        if i.isalpha():
            base = ord('A') if i.isupper() else ord('a')
            shift = (ord(i) - base + key) % 26
            cripto_word += chr(shift + base)
        else:
            cripto_word += i
    return cripto_word

def decripto(key: int, word: str) -> str:
    decripto_word = ''
    for i in word:
        if i.isalpha():
            base = ord('A') if i.isupper() else ord('a')
            shift = (ord(i) - base - key) % 26
            decripto_word += chr(shift + base)
        else:
            decripto_word += i
    return decripto_word

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possível se conectar ao servidor!\n')

    key = int(client.recv(1024).decode())
    
    if len(sys.argv) > 1:
        username =sys.argv[1]
    else:
        username = input('Usuário> ')
    
    print('\nConectado ao servidor com a chave:', key)

    thread1 = threading.Thread(target=receiveMessages, args=[client, key])
    thread2 = threading.Thread(target=sendMessages, args=[client, username, key])

    thread1.start()
    thread2.start()

def receiveMessages(client, key):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            decrypted_msg = decripto(key, msg)
            print(decrypted_msg + '\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break

def sendMessages(client, username, key):
    while True:
        try:
            msg = input('\n')
            encrypted_msg = cripto(key, f'<{username}> {msg}')
            client.send(encrypted_msg.encode('utf-8'))
        except:
            print("Erro ao enviar mensagem.")
            break

main()
