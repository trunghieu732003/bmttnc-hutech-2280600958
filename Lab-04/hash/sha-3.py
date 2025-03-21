from Crypto.Hash import SHA3_256

def sha3 (message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhập chuỗi cần băm: ").encode('utf-8')
    hashed_value = sha3(text)
    
    print("Chuỗi văn bản đã nhâp: ", text.decode('utf-8'))
    print("SHA-3 Hash: ", hashed_value.hex())
    
if __name__ == "__main__":
    main()