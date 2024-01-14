from cryptography.fernet import Fernet
import socket
import hashlib
import hmac
import os

def encrypt(key, message):
    return Fernet(key).encrypt(message.encode())

def decrypt(key, encrypted):
    return Fernet(key).decrypt(encrypted).decode()

def sha512_gen(data):
    return hashlib.sha512(data).digest()

def generate_hmac(key, data):
    return hmac.new(key, data, hashlib.sha512).digest()

def verify_hmac(key, data, received_hmac):
    computed_hmac = generate_hmac(key, data)
    return hmac.compare_digest(computed_hmac, received_hmac)

def start_server():
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind(('localhost', 12345))
    s_socket.listen(1)
    print("Server listening")
    connection, c_addr = s_socket.accept()
    print("User connected from", c_addr)

    shared_key = Fernet.generate_key()
    connection.sendall(shared_key)

    while True:
        encrypted = connection.recv(1024)
        if not encrypted:
            break
        received_message, received_hmac = encrypted[:-64], encrypted[-64:]

        if verify_hmac(shared_key, received_message, received_hmac):
            decrypted_message = decrypt(shared_key, received_message)
            print("Received:", decrypted_message)

            response = input("Enter response: ")
            encrypted_response = encrypt(shared_key, response)
            response_hmac = generate_hmac(shared_key, encrypted_response)
            response_with_hmac = encrypted_response + response_hmac
            connection.sendall(response_with_hmac)
        else:
            print("Integrity verification failed!")

    connection.close()
    s_socket.close()

start_server()
