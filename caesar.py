def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''ciphernum > ord('z')
    """
    # PUT YOUR CODE HERE
    ciphertext = ''
    for ch in plaintext:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            ciphernum = ord(ch) + 3
            if сiphernum > ord('Z') and ciphernum < ord('a') or ciphernum > ord('z'):
                ciphernum -= 26
            ciphertext += chr(ciphernum)
        else:
            ciphertext += ch
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    plaintext = ''
    for ch in ciphertext:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            ciphernum = ord(ch) - 3
            if ciphernum > ord('z') or ciphernum > ord('Z') and ciphernum < ord('a'):
                ciphernum += 26
            ciphertext += chr(ciphernum)
        else:
            ciphertext += ch
    return ciphertext
    return plaintext
