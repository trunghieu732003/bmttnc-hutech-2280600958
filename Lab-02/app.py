from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher 
from cipher.transposition import TranspositionCipher


app = Flask(__name__)

playfair_cipher = PlayFairCipher()
railfence_cipher = RailFenceCipher()
transposition_cipher = TranspositionCipher()


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    try:
        # Lấy dữ liệu từ form
        text = request.form.get('plain_text')
        key = request.form.get('key')  # Không chuyển đổi thành int()

        # Kiểm tra dữ liệu đầu vào
        if not text or not key:
            return "Error: Missing plain text or key", 400

        # Mã hóa văn bản
        vigenere = VigenereCipher()
        encrypted_text = vigenere.vigenere_encrypt(text, key)
        
        # Trả về kết quả dạng HTML giống như Caesar cipher
        return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
    except Exception as e:
        return f"Error: {str(e)}", 500


@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    try:
        # Lấy dữ liệu từ form
        text = request.form.get('cipher_text')
        key = request.form.get('key')  # Không chuyển đổi thành int()

        # Kiểm tra dữ liệu đầu vào
        if not text or not key:
            return "Error: Missing cipher text or key", 400

        # Giải mã văn bản
        vigenere = VigenereCipher()
        decrypted_text = vigenere.vigenere_decrypt(text, key)
        
        # Trả về kết quả dạng HTML giống như Caesar cipher
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
    except Exception as e:
        return f"Error: {str(e)}", 500


# Route cho Playfair Cipher
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

# API để tạo ma trận Playfair
@app.route('/api/playfair/creatematrix', methods=['POST'])
def create_playfair_matrix():
    try:
        key = request.form.get('key')
        if not key:
            return "Error: Key is required", 400

        matrix = playfair_cipher.create_playfair_matrix(key)
        return f"Key: {key}<br/>Matrix: {matrix}"
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    try:
        plain_text = request.form.get('plain_text')
        key = request.form.get('key')

        if not plain_text or not key:
            return "Error: Plain text and key are required", 400

        matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
        return f"Plain Text: {plain_text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}"
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    try:
        cipher_text = request.form.get('cipher_text')
        key = request.form.get('key')

        if not cipher_text or not key:
            return "Error: Cipher text and key are required", 400

        matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
        return f"Cipher Text: {cipher_text}<br/>Key: {key}<br/>Decrypted Text: {decrypted_text}"
    except Exception as e:
        return f"Error: {str(e)}", 500

# Route cho Rail Fence Cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

# Route để mã hóa Rail Fence Cipher
@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    try:
        plain_text = request.form.get('plain_text')
        num_rails = int(request.form.get('num_rails'))

        if not plain_text or not num_rails:
            return "Error: Plain text and number of rails are required", 400

        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, num_rails)
        return f"Plain Text: {plain_text}<br/>Number of Rails: {num_rails}<br/>Encrypted Text: {encrypted_text}"
    except Exception as e:
        return f"Error: {str(e)}", 500

# Route để giải mã Rail Fence Cipher
@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    try:
        cipher_text = request.form.get('cipher_text')
        num_rails = int(request.form.get('num_rails'))

        if not cipher_text or not num_rails:
            return "Error: Cipher text and number of rails are required", 400

        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, num_rails)
        return f"Cipher Text: {cipher_text}<br/>Number of Rails: {num_rails}<br/>Decrypted Text: {decrypted_text}"
    except Exception as e:
        return f"Error: {str(e)}", 500

# Route cho Transposition Cipher
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

# Route để mã hóa Transposition Cipher
@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    try:
        plain_text = request.form.get('plain_text')
        key = int(request.form.get('key'))

        if not plain_text or not key:
            return "Error: Plain text and key are required", 400

        encrypted_text = transposition_cipher.encrypt(plain_text, key)
        return f"Plain Text: {plain_text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}"
    except Exception as e:
        return f"Error: {str(e)}", 500

# Route để giải mã Transposition Cipher
@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    try:
        cipher_text = request.form.get('cipher_text')
        key = int(request.form.get('key'))

        if not cipher_text or not key:
            return "Error: Cipher text and key are required", 400

        decrypted_text = transposition_cipher.decrypt(cipher_text, key)
        return f"Cipher Text: {cipher_text}<br/>Key: {key}<br/>Decrypted Text: {decrypted_text}"
    except Exception as e:
        return f"Error: {str(e)}", 500

####################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)