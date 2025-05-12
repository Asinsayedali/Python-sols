count = 0
with open('code.txt','r') as file:
    text_Value = file.read()
    list_Values = text_Value.split()
    for words in list_Values:
        if len(words)==4:
            print(words)
            count+=1
print(f"the number of words with four count : {count}")