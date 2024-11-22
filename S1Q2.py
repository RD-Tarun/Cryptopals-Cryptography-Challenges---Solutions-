def fixed_xor(s1,s2):
    b1 = bytes.fromhex(s1)
    b2 = bytes.fromhex(s2)

    xor_result=bytes(a^b for a,b in zip(b1,b2))
    return(xor_result.hex())

s1="1c0111001f010100061a024b53535009181c"
s2="686974207468652062756c6c277320657965"

result=fixed_xor(s1,s2)
print(result)

