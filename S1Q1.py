import binascii
import base64

hex_str = "49276d206b696c6c696e6720796f7572206c696665206120706f726e6f6772617068792e"
byte_str = binascii.unhexlify(hex_str)

b64_string = base64.b64encode(byte_str).decode('utf-8')
print(b64_string)
