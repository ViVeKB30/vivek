def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if mode == 'encrypt':
                if char.islower():
                    result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif mode == 'decrypt':
                if char.islower():
                    result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += char
    return result

def main():
    while True:
        print("Caesar Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift, 'encrypt')
            print("Encrypted message:", encrypted_message)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, shift, 'decrypt')
            print("Decrypted message:", decrypted_message)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
