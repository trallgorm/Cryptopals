import base64
HEX_STRING = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
encoded = base64.b64encode(bytearray.fromhex(HEX_STRING).decode().encode())
print(str(encoded,'utf-8'))
