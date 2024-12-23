# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
import os
import base64

def encrypt_key(key, public_key_path, output_path):
    # 使用 RSA 公钥加密对称密钥
    with open(public_key_path, "rb") as key_file:
        public_key = load_pem_public_key(key_file.read())
    encrypted_key = public_key.encrypt(
        key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    with open(output_path, "wb") as outfile:
        outfile.write(encrypted_key)


# 示例：对文件加密并存储加密密钥
if __name__ == '__main__':
    aes_key = os.urandom(32)  # 随机生成 AES 密钥
    encrypt_key(aes_key, "key/public_key.pem", "key/key.enc")