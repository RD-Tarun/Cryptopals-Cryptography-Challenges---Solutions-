def detect_ecb_ciphertext(file):
    def count_repeated_blocks(ciphertext, block_size=16):
        blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
        return len(blocks) - len(set(blocks)) #set dosen't accept duplicates , so this will give number of repeated blocks

    with open(file,"r") as file:
        lines = file.readlines()

    repeated_list = []
    for index,line in enumerate(lines):
        ciphertext = bytes.fromhex(line.strip()) #removing whitespaces on both sides
        repeated_blocks = count_repeated_blocks(ciphertext)
        if repeated_blocks > 0:
            repeated_list.append((index, repeated_blocks, ciphertext))

    if repeated_list:
        repeated_list.sort(key=lambda x: -x[1])  #sorting by most repeated blocks(descending order)
        line_number,repetitions,ciphertext=repeated_list[0]
        print(f"Detected ECB mode ctext at line {line_number + 1} with {repetitions} repeated blocks")
        return ciphertext
    else:
        print("No repeated ciphertext detected")
        return None

file_path = r'C:\Users\R.D.Tarun\DSA\Cryptopals\q8.txt' 
ecb_ciphertext = detect_ecb_ciphertext(file_path)
print(f"Detected ECB ciphertext (hex): {ecb_ciphertext.hex()}")
