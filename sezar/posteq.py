import requests
from time import sleep

url_encrypt = 'http://127.0.0.1:5000/encrypt'
url_decrypt = 'http://127.0.0.1:5000/decrypt'
url_hafiza = 'http://127.0.0.1:5000/hafiza'

while True:
    secimyap = input("""
        1 = metni encryptler
        2 = metni decryptler
        3 = encrypt ve decrypt edilmiş metinleri gösterir 
""")
    if secimyap == "1":
        text_to_encrypt = input("Metin gir:") 
        if text_to_encrypt.lower() == '31':
            break
        if text_to_encrypt.lower() == 'mal':
            print(":D \n" * 5)
            sleep(3)
            print(">:(")
            break
        response = requests.post(url_encrypt, data={'text': text_to_encrypt})
        if response.status_code == 200:
            encrypted_text = response.text
            print("Gizli metin:", encrypted_text)
        else:
            print("Hata:", response.text)

    if secimyap == "2":
        text_to_decrypt = input("Metin gir: ") 
        if text_to_decrypt.lower() == '31':
            break
        if text_to_decrypt.lower() == 'mal':
            print(":D \n" * 5)
            sleep(3)
            print(">:(")
            break
        response = requests.post(url_decrypt, data={'text': text_to_decrypt})
        if response.status_code == 200:
            decrypted_text = response.text
            print("Orj metin:", decrypted_text)
        else:
            print("Hata:", response.text)

    if secimyap == "3":
        response = requests.get(url_hafiza)
        if response.status_code == 200:
            hafiza = response.json()
            print("Kriptolanmış metinler:", hafiza['kriptler'])
            print("Çözülmüş metinler:", hafiza['dekriptler'])
        else:
            print("Hata:", response.text)
