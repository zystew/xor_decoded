import base64
import binascii

message = b"NwMXGRwQB0wcB1MHBw0PHFMVGhkLUxAAAUwcCxYXFgUaFlNEVSkXBRwcEBZZBRwRBwlZMCVFBhkLUx0KAR4cUxIBBwkKABZFGA0QH1MBEEEaGxIXDA4dFl4AG0EKEAoJGQ05EAoHEB4OEgcGHUIfAV9FFA8aHB4VFAsXsNpFERlZEBwBEEwIBhZFAwMMAFMEAwkDUwYRHAAQALDMVRwWBgFFGg4NFh0MB0waFlMIEB8KEhQAW0w3HAYWVRoWBgBFBwkaHB0RFA8NFgEKGx9ZFxILBkwVFgBFBQAMAFMHBwkfAFMBtsUVEhoWVQ0PFhBFAAIcUwMXGhwWABoRHAMXUxcAVR4cHRcAD0EPHAYWWw=="
#message = b'MzAwZDA5MTYxODQ1MGYwOTQ1MGUwMzBiMDcwOQ=='


wordlist = open("rockyou.txt", "r", encoding="utf8", errors='ignore')

message_encode  = base64.b64decode(message)
print(message_encode)


for k in wordlist.readlines():
    cle     = k.rstrip().encode()
    z = cle
    if len(z) > 0:
        taille = len(message_encode)
        for i in range(int(taille/len(z))):
            cle += z


        test = bytes(a ^ b for a, b in zip(cle, message_encode))

        
        try:
            decode = bytes(test).decode()
            if "cyberwatch" in str(decode):
                print(str(decode))
                print(z)

        except:
            continue

       

