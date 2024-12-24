from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
import os
import base64


def decrypt_file(input_path, output_path, key):
    # 使用 AES 解密文件
    with open(input_path, "rb") as infile:
        # 读取文件名长度
        file_name_length = int.from_bytes(infile.read(2), 'big')
        # 读取原始文件名
        original_file_name = infile.read(file_name_length).decode('utf-8')

        iv = infile.read(16)  # 读取 IV
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
        decryptor = cipher.decryptor()

        # 构造解密后的文件路径
        output_path = os.path.join(output_path, original_file_name)

        with open(output_path, "wb") as outfile:
            while chunk := infile.read(4096):
                outfile.write(decryptor.update(chunk))
            outfile.write(decryptor.finalize())


def decrypt_key(encrypted_key_path, private_key_path):
    # 使用 RSA 私钥解密对称密钥
    with open(private_key_path, "rb") as key_file:
        private_key = load_pem_private_key(key_file.read(), password=None)
    with open(encrypted_key_path, "rb") as infile:
        encrypted_key = infile.read()

    return private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


# 示例：解密文件
if __name__ == '__main__':
    aes_key = decrypt_key("key/key.enc", "key/private_key.pem")
    decrypt_file("data/JPG.enc", "data/", aes_key)
