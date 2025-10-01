def atbash(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
                pos = ord(char) - base
                new_pos = 25 - pos
                result += chr(new_pos + base)
            else:
                base = ord('a')
                pos = ord(char) - base
                new_pos = 25 - pos
                result += chr(new_pos + base)
        else:
            result += char
    return result



plaintext = input("Enter your message: ")
encrypted = atbash(plaintext)
print("Encrypted message:", encrypted)

decrypted = atbash(encrypted)
print("Decrypted message:", decrypted)
