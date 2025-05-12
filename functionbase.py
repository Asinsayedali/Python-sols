def print_value(name: str, age: int)-> None:
    print("""shefin is a funda mwon this is true from his young age because he isa  myren 
    \"from\" the childhood itself """) #this is true for the shefin thayoli
GRADIENT = 0.76
values = ["apple", "grape","orange","asin"]
i =0
while i < len(values):
    value = values[i]
    if 'g' in value:
        print(value)
    elif value == "apple":
        values[i] = "cherry"
        print(values[i])
    else:
        values.append("shefin")
    i += 1
print(values)
