def sort_list(numbers,n):
    for i in range(n):
        for j in range(n-1):
            if numbers[j]>numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1]=numbers[j]
                numbers[j]=temp
    return numbers
n = int(input("enter the limit of the list\n"))
numbers=[]
for _ in range(n):
    number = int(input("enter the number"))
    numbers.append(number)
print("unsorted list:", numbers)
sorted_list = sort_list(numbers,n)
print("sortedlist:",sorted_list)