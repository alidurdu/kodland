import random
import string

def generate_strong_password(length, uppercase=True, digits=True, symbols=True):
    characters = string.ascii_letters if uppercase else string.ascii_lowercase
    characters += string.digits if digits else ''
    characters += string.punctuation if symbols else ''

    if not characters:
        print("Lütfen en az bir karakter türünü seçin.")
        return None

    strong_password = ''.join(random.choice(characters) for _ in range(length))
    return strong_password

def main():
    print("Güçlü Şifre Üreteci")
    length = int(input("Şifre uzunluğunu girin: "))
    uppercase = input("Büyük harfler içersin mi? (Evet/Hayır): ").lower() == 'evet'
    digits = input("Rakamlar içersin mi? (Evet/Hayır): ").lower() == 'evet'
    symbols = input("Semboller içersin mi? (Evet/Hayır): ").lower() == 'evet'

    strong_password = generate_strong_password(length, uppercase, digits, symbols)

    if strong_password:
        print("Oluşturulan Güçlü Şifre:", strong_password)

if __name__ == "__main__":
    main()
