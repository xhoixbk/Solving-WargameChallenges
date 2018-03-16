import base64, binascii

hexStr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
base64Str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

def hextob64(hexStr):
    # convert hex string to raw bytes
    byteStr = binascii.unhexlify(hexStr.lower())
    # convert raw bytes to base64, then return
    return base64.b64encode(byteStr)

if __name__ == '__main__':
    print("Convert hex '%s' to base64:\n" % hexStr + str(hextob64(hexStr))[1:])

