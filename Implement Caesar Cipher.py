def caesar_cipher(text: str, shift: int, mode: str = 'encrypt') -> str:
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.
    
    :param text: The message to transform.
    :param shift: Number of positions to shift (positive integer).
    :param mode: 'encrypt' to shift forward, 'decrypt' to shift backward.
    :return: The resulting text.
    """
    if mode == 'decrypt':
        shift = -shift

    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            # Compute new character position with wrap‑around
            offset = (ord(ch) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            # Leave digits, punctuation, spaces, etc. unchanged
            result.append(ch)
    return ''.join(result)


def main():
    print("=== Caesar Cipher ===")
    # 1) Choose operation
    while True:
        choice = input("Encrypt or Decrypt? (E/D): ").strip().lower()
        if choice in ('e', 'encrypt'):
            mode = 'encrypt'
            break
        if choice in ('d', 'decrypt'):
            mode = 'decrypt'
            break
        print("Please enter 'E' for encrypt or 'D' for decrypt.")

    # 2) Get message and shift
    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter shift value (e.g. 3): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for shift.")

    # 3) Perform transformation and display
    result = caesar_cipher(message, shift, mode)
    label = "Encrypted" if mode == 'encrypt' else "Decrypted"
    print(f"{label} message: {result}")


if __name__ == "__main__":
    main()
