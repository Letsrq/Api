from flask import Flask, request

app = Flask(__name__)

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.kucukharf():
                if shifted > ord('z'):
                    shifted -= 29
                elif shifted < ord('a'):
                    shifted += 29
            elif char.buyukharf():
                if shifted > ord('Z'):
                    shifted -= 29
                elif shifted < ord('A'):
                    shifted += 29
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

@app.route('/')
def index():
    return "Sezaringo"

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form.get('text')
    shift = int(request.form.get('shift', 1)) 
    if not text:
        return "No text provided for encryption", 400
    encrypted_text = caesar_cipher(text, shift)
    return encrypted_text

if __name__ == '__main__':
    app.run(debug=True)
