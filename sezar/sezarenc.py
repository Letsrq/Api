from flask import Flask, request, jsonify

app = Flask(__name__)

kriptler = []
dekriptler = []

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            shifted = shifted if shifted < ord("z") else ord("a") + ((shifted - ord("a")) % 26)
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift  # Subtract shift to move backwards
            shifted = shifted if shifted >= ord("a") else ord("z") - ((ord("a") - shifted - 1) % 26)
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

@app.route('/')
def index():
    return "Sezaringo"

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form.get('text')
    shift = int(request.form.get('shift', 1)) 
    if not text:
        return "You didn't enter anything", 400
    encrypted_text = caesar_cipher(text, shift)
    kriptler.append({'Kripto': encrypted_text, 'metin': text})
    return encrypted_text

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form.get('text')
    shift = int(request.form.get('shift', 1)) 
    if not text:
        return "You didn't enter anything", 400
    decrypted_text = caesar_decipher(text, shift)
    dekriptler.append({'Kriptolu': text, 'Çözülmüş hali': decrypted_text})
    return decrypted_text

@app.route('/kriptler', methods=['GET'])
def get_kriptler():
    return jsonify(kriptler)

@app.route('/dekriptler', methods=['GET'])
def get_dekriptler():
    return jsonify(dekriptler)

@app.route('/hafiza', methods=['GET'])
def get_hafiza():
    hafiza = {'kriptler': kriptler, 'dekriptler': dekriptler}
    return jsonify(hafiza)

if __name__ == '__main__':
    app.run(debug=True)
