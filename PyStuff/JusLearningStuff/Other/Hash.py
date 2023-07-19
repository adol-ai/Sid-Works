print("\t size of the HashTable is 10")
Hash_Table=[]
for i in range(0,10):
    Hash_Table.append(["NULL"])

print("\n\n")
x=eval(input("Enter the Key values to be feeded (List form): "))

for k in x:

    Hash_Function = ((2*k)+3)%len(Hash_Table)
    
    if Hash_Table[Hash_Function]==["NULL"]:
        Hash_Table[Hash_Function] = [k]
        
    else:
        Hash_Table[Hash_Function].append(k)

print("\n")
print("\t Hash_Function = ((2*k)+3)%len(Hash_Table)")
print("\n")
print("\t\t *Hash Table*")
print("\n")

for y in range(0,10):
    print("\t",y,"  --->  ",Hash_Table[y])

    
