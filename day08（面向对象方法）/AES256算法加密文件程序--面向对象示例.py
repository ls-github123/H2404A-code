from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

class AES256Encryptor:
    def __init__(self, key: bytes):
        """初始化AES256Encryptor对象。
        
        参数:
        key (bytes): 32字节的密钥，用于AES-256加密。
        """
        if len(key) != 32:
            raise ValueError("Key must be 32 bytes long for AES-256.")
        self.key = key

    def encrypt_file(self, file_path: str, output_path: str):
        """加密文件。
        
        参数:
        file_path (str): 要加密的文件路径。
        output_path (str): 加密后文件的输出路径。
        """
        # 生成16字节的随机IV
        iv = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CFB, iv=iv)
        
        with open(file_path, 'rb') as f:
            plaintext = f.read()
        
        ciphertext = cipher.encrypt(plaintext)
        
        with open(output_path, 'wb') as f:
            f.write(iv + ciphertext)
        
        print(f"File '{file_path}' has been encrypted and saved as '{output_path}'.")

    def decrypt_file(self, file_path: str, output_path: str):
        """解密文件。
        
        参数:
        file_path (str): 要解密的文件路径。
        output_path (str): 解密后文件的输出路径。
        """
        with open(file_path, 'rb') as f:
            iv = f.read(16)  # 读取前16字节的IV
            ciphertext = f.read()
        
        cipher = AES.new(self.key, AES.MODE_CFB, iv=iv)
        plaintext = cipher.decrypt(ciphertext)
        
        with open(output_path, 'wb') as f:
            f.write(plaintext)
        
        print(f"File '{file_path}' has been decrypted and saved as '{output_path}'.")

# 示例用法
if __name__ == "__main__":
    key = get_random_bytes(32)  # 生成32字节的随机密钥
    encryptor = AES256Encryptor(key)

    # 文件路径
    original_file = 'example.txt'
    encrypted_file = 'example_encrypted.aes'
    decrypted_file = 'example_decrypted.txt'

    # 加密文件
    encryptor.encrypt_file(original_file, encrypted_file)

    # 解密文件
    encryptor.decrypt_file(encrypted_file, decrypted_file)
