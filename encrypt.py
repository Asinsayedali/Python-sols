plaintext = input("enter the text")
distance = int(input("enter the distance\n"))
encrypted_text= ""
for char in plaintext:
    if ord('a') <= ord(char) <= ord('z'):
        orignal_pos = ord(char)-ord('a')
        new_pos = (orignal_pos+distance) % 26
        new_char = ord('a')+new_pos
        encrypted_text+=chr(new_char)
print(plaintext)
print(encrypted_text)