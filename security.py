from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os


APP_PEPPER = os.getenv('APP_PEPPER')

def criptografarsenha(senha_texto_plano):
    senha_com_pepper = senha_texto_plano + APP_PEPPER
    return generate_password_hash(senha_com_pepper, method='pbkdf2:sha256')

def verificarsenha(hash_salvo_no_banco, senha_fornecida_no_login):
    senha_com_pepper = senha_fornecida_no_login + APP_PEPPER
    return check_password_hash(hash_salvo_no_banco, senha_com_pepper)

def generate_encryption_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode() + APP_PEPPER.encode()))
    return key

def encrypt_data(data: str, key: bytes) -> str:
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data.decode()

def decrypt_data(encrypted_data: str, key: bytes) -> str:
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data.encode())
    return decrypted_data.decode()