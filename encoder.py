#Hex + Base64 Encoder/Decoder by MN (GitHub: Mespeon)

import codecs as cdc
import base64 as b64
import sys
import os

def main():
    print("""\nHow may I help?
[1] Encode
[2] Decode
[0] Exit
""", sep='', flush=False)
    task = input(': ')

    if task == '0':
        sys.exit()
    else:
        source_string = input("\nEnter string: ")
        if task == '1':
            print('\nOriginal: ', source_string, 'Encoded: ', encode(source_string), sep='\n', flush=False)
        else:
            decode(source_string)

def encode(src):
    encoded_string = ''
    try:
        encToUtf = cdc.encode(src, 'utf-8')
        encToHex = cdc.encode(encToUtf, 'hex')
    except Exception as e:
        print(e)
        main()
        
    #Prompt if hex > base64 should be applied
    convb64 = input('Encode to base64? [Y/N] ')
    if convb64 == 'Y' or convb64 == 'y':
        try:
            encToB64 = b64.b64encode(encToHex)
            dec64ToString = cdc.decode(encToB64, 'utf-8')
            encoded_string = dec64ToString
        except Exception as e:
            print(e)
            main()
    else:
        try:
            decHexToString = cdc.decode(encToHex, 'utf-8')
            encoded_string = decHexToString
        except Exception as e:
            print(e)
            main()

    return encoded_string
        
def decode(src):
    decoded_string = ''
    #Prompt if string is in hex or base64.
    print("""What do you think is the format of the source?
[1] Hex
[2] Base64
""")
    srcFormat = input(': ')
    if srcFormat == '1':
        print('\nSource: ', src, 'Decoded: ', decodeHex(src), sep='\n', flush=False)
    else:
        print('\nSource: ', src, 'Decoded: ', decodeBase64(src), sep='\n', flush=False)
        
def decodeHex(src):
    try:
        decHexToAscii = cdc.decode(src, 'hex')
        decAsciiToString = cdc.decode(decHexToAscii, 'utf-8')
    except Exception as e:
        print(e)
        main()
    
    return decAsciiToString

def decodeBase64(src):
    print("\nIf the Base64 string came from this program, decode the value using the Hex decode mode.")
    try:
        b64decoded = b64.b64decode(src)
        decB64ToString = cdc.decode(b64decoded, 'utf-8')
    except Exception as e:
        print(e)
        main()

    return decB64ToString

#Run program
while True:
    main()
