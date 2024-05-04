import threading
import socket
import random

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen()
        print("Servidor iniciado em 'localhost' na porta 7777")
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept()
        key = key_generator()
        print(f"Cliente {addr} conectado com a chave {key}")
        send_cripto_key(key, client)
        new_client = [client, key]
        clients.append(new_client)

        thread = threading.Thread(target=messagesTreatment, args=[new_client])
        thread.start()

def key_generator() -> int:
    return random.randint(0, 9999)

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

def messagesTreatment(client):
    client_socket, key = client
    while True:
        try:
            msg = client_socket.recv(2048).decode()
            if msg:
                print(f"Mensagem criptografada recebida: {msg}")
                msg = decripto(key, msg)
                print(f"Mensagem decriptografada: {msg}")
                broadcast(msg, client)
        except:
            print(f"Erro com o cliente {client_socket}")
            deleteClient(client)
            break

def broadcast(msg, sender):
    for client, key in clients:
        if client != sender[0]:
            try:
                encrypted_msg = cripto(key, msg)
                client.send(encrypted_msg.encode())
            except:
                print(f"Erro ao enviar para o cliente {client}")
                deleteClient([client, key])

def send_cripto_key(key, client):
    try:
        client.send(str(key).encode())
    except:
        print("Erro ao enviar chave para o cliente")
        deleteClient([client, key])

def deleteClient(client):
    if client in clients:
        clients.remove(client)
        client[0].close()

main()
