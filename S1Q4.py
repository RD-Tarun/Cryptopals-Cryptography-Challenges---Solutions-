#The dictionary given above
ENGLISH_FREQUENCIES ={
        'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442,
        'f': 0.0197881, 'g': 0.0158610,'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033,
        'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,'o': 0.0596302,
        'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563,'s': 0.0515760, 't': 0.0729357,
        'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984,
        'z': 0.0007836, ' ': 0.1918182
        }

#Rating a plaintext based on English frequencies
def rate_text(text):
    return sum(ENGLISH_FREQUENCIES.get(chr(byte).lower(), 0) for byte in text)

#Breaking single-byte XOR
def break_single_byte_xor(ciphertext):
    best_score = 0
    best_key = None
    best_plaintext = None
    for key in range(256):
        plaintext = bytes([byte ^ key for byte in ciphertext])
        score = rate_text(plaintext)
        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = plaintext
    return best_key, best_plaintext

#Detecting single-character XOR in a list of strings
def detect_single_character_xor(lines):
    best_score = 0
    best_result = None
    for line in lines:
        ciphertext = bytes.fromhex(line.strip())
        key, plaintext = break_single_byte_xor(ciphertext)
        score = rate_text(plaintext)
        if score > best_score:
            best_score = score
            best_result = (key, plaintext)
    return best_result

with open(r"C:\Users\R.D.Tarun\DSA\Cryptopals\S1Q4.txt", "r") as file:
    lines = file.readlines()
key, plaintext = detect_single_character_xor(lines)
print(f"Key: {key}, Plaintext: {plaintext.decode('utf-8', 'ignore')}")

