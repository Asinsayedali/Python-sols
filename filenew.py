char_count ={}
with open("code1.txt","r") as file:
    for line in file:
        for char in line:
            if char in char_count:
                char_count[char] +=1
            else:
                char_count[char] =1

            