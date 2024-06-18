from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    # Encrypting image pixels
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Example encryption: XOR with a key
            r ^= key
            g ^= key
            b ^= key
            pixels[x, y] = (r, g, b)

    encrypted_image_path = 'pixel_encrypted.png'  # Save as pixel_encrypted.png
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")

def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    width, height = img.size
    pixels = img.load()

    # Decrypting image pixels
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Example decryption: XOR with the same key
            r ^= key
            g ^= key
            b ^= key
            pixels[x, y] = (r, g, b)

    decrypted_image_path = 'pixel_decrypted.png'  # Save as pixel_decrypted.png
    img.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")

def main():
    image_path = input("Enter the path to the image file (.png): ")
    key = int(input("Enter the encryption/decryption key (an integer): "))

    # Encrypt the image
    encrypt_image(image_path, key)

    # Decrypt the encrypted image
    encrypted_image_path = 'pixel_encrypted.png'  # Update path if different
    decrypt_image(encrypted_image_path, key)

if __name__ == "__main__":
    main()
