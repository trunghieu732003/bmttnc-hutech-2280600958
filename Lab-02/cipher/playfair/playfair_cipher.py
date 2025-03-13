class PlayFairCipher:
    def __init__(self):
        pass
    
    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")
        key = key.upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key)
        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix
    
    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
    
    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            if len(pair) == 1:
                pair += "X"
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
            elif col1 == col2:
                encrypted_text += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text
    
    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                decrypted_text += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
            elif col1 == col2:
                decrypted_text += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        # Remove any padding 'X' characters that were added during encryption
        decrypted_text = decrypted_text.replace("X", "")
        
        return decrypted_text