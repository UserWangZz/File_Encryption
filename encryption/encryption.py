from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
# from decryption import decrypt_key
import os
import base64


def encrypt_file(input_path, output_path, key):
    # 获取原始文件名并编码为字节
    original_file_name = os.path.basename(input_path).encode('utf-8')
    file_name_length = len(original_file_name)  # 文件名长度

    # 使用 AES 加密文件
    iv = os.urandom(16)  # 初始化向量
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()

    with open(input_path, "rb") as infile, open(output_path, "wb") as outfile:
        # 写入文件名长度和文件名
        outfile.write(file_name_length.to_bytes(2, 'big'))  # 使用 2 字节存储文件名长度
        outfile.write(original_file_name)  # 写入文件名
        outfile.write(iv)  # 保存 IV
        while chunk := infile.read(4096):
            outfile.write(encryptor.update(chunk))
        outfile.write(encryptor.finalize())


if __name__ == '__main__':
    from decryption import decrypt_key

    aes_key = decrypt_key('key/key.enc', 'key/private_key.pem')
    encrypt_file("data/JPG.zip", "data/JPG.enc", aes_key)
    # encrypt_key(aes_key, "key/public_key.pem", "key/key.enc")
