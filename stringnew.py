name = "asin"
list_new = list(name)
print(list_new)
list_new[0] = "s"
print(list_new)
name = "".join(list_new)
print(name[-1])
print(name[:-4:-1])