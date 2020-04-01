def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    ciphertext = ''
    for index, ch in enumerate(plaintext):
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a')if 'a' <= ch <= 'z' else ord('A')
            cipher = ord(ch) + shift
            if 'a' <= ch <= 'z' and cipher > ord('z'):
                cipher -= 26
            elif 'A' <= ch <= 'Z' and cipher > ord('Z'):
                cipher -= 26
            ciphertext += chr(cipher)
        else:
            chiphertext += ch
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    plaintext = ''
    for index, ch in enumerate(ciphertext):
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= ch <= 'z' else ord('A')
            cipher = ord(ch) - shift
            if 'a' <= ch <= 'z' and cipher < ord('a'):
                cipher += 26
            elif 'A' <= ch <= 'Z' and cipher < ord('A'):
                cipher += 26
            plaintext += chr(cipher)
        else:
            plaintext += ch

    return plaintext