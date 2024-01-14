from cryptography.fernet import Fernet
import socket
import hashlib
import hmac

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

def start_client():
    c_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # client socket
    c_s.connect(('localhost', 12345))
    print("Connected to server!")

    shared_key = c_s.recv(1024)

    while True:
        message = input("Enter message: ")
        encrypted = encrypt(shared_key, message)
        message_hmac = generate_hmac(shared_key, encrypted)
        message_with_hmac = encrypted + message_hmac

        c_s.sendall(message_with_hmac)
        encrypted_response_with_hmac = c_s.recv(1024)
        received_message, received_hmac = (
            encrypted_response_with_hmac[:-64], encrypted_response_with_hmac[-64:]
        )

        if verify_hmac(shared_key, received_message, received_hmac):
            print("Server response:", decrypt(shared_key, received_message))
        else:
            print("Integrity verification failed!")
    c_s.close()

start_client()
