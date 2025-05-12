Encrypted_text = input("Enter the string")
distance = int(input("Enter the dis"))
decrypted = ""
for char in Encrypted_text:
    if ord('a') <= ord(char) <= ord('z'):
        orginalpos =ord(char) -ord('a')
        newpos = (orginalpos - distance)%26
        newchar = ord('a') + newpos
        decrypted +=chr(newchar)
print(decrypted)