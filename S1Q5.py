def repeating_key_xor(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % key_length]
        
        # XOR operation on the ASCII values of the characters
        xor_result = ord(char) ^ ord(key_char)
        
        # Convert result to a hex string, remove the '0x' prefix
        hex_result = hex(xor_result)[2:]
        
        # Ensure the hex result is 2 characters long
        if len(hex_result) == 1:
            hex_result = "0" + hex_result
        
        ciphertext += hex_result
    
    return ciphertext

# Plaintext and key
plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

# Encrypt the plaintext
encrypted_text = repeating_key_xor(plaintext, key)
print(encrypted_text)
