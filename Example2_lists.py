list = []

newIem = "x"

while (newIem != ""):
     newIem = input("Enter new item:")

     if (newIem != ""):
         list.append(newIem)

print(list)
print("Total items: ", list.count())
