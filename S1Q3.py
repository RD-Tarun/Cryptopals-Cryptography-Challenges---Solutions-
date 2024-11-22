def count_freq(s):  # return element with max frequency
    freq = {byte: s.count(byte) for byte in s}
    max_occuring_element = max(freq, key=freq.get)
    return max_occuring_element


def xor(s, key):  # xor function
    result = bytes(byte ^ key for byte in s)
    return result.decode('utf-8', errors='ignore')


input_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# Convert hex string to bytes
decoded_bytes = bytes.fromhex(input_str)
key = count_freq(decoded_bytes)
result = xor(decoded_bytes, key)

print("Decoded XOR'd string:", result)
