def sublist(mylist, sublist_value):
    for i in range(len(mylist)):
        if mylist[i] == sublist_value[0]:
            if mylist[i: i+len(sublist_value)] == sublist_value:
                return True
    return False

print(sublist([3,4,5,2,7,8],[5,2]))


