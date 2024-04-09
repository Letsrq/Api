
import requests
from time import sleep

url = 'http://127.0.0.1:5000/encrypt'

while True:
    text_to_encrypt = input("Metin gir (cıkmak icin 31 yaz) -> ")
    
    if text_to_encrypt.lower() == '31':
        break
    if text_to_encrypt.lower() == 'mal':
        print(":D \n" *5)
        sleep(3)
        print(">:(")
        break
    response = requests.post(url, data={'text': text_to_encrypt})

    if response.status_code == 200:
        encrypted_text = response.text
        print("Gizli metin:", encrypted_text)
    else:
        print("Hata:", response.text)
# xd
=======
import requests
from time import sleep

url = 'http://127.0.0.1:5000/encrypt'

while True:
    text_to_encrypt = input("Metin gir (cıkmak icin 31 yaz) -> ")
    
    if text_to_encrypt.lower() == '31':
        break
    if text_to_encrypt.lower() == 'mal':
        print(":D \n" *5)
        sleep(3)
        print(">:(")
        break
    response = requests.post(url, data={'text': text_to_encrypt})

    if response.status_code == 200:
        encrypted_text = response.text
        print("Gizli metin:", encrypted_text)
    else:
        print("Hata:", response.text)

