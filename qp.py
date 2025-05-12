plaintext = input("Enter the string ")
distance = int(input("Enter the distance "))
Encrypted_text = ""
for char in plaintext :
    if ord('a') <= ord(char) <= ord('z'):
        orginal_pos =  ord(char) - ord('a')
        new_pos = (distance+orginal_pos)%26
        newchar = ord('a')+new_pos
        Encrypted_text +=chr(newchar)
print(Encrypted_text)
        