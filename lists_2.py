list_1 = ["Apples", "Bananas", "Cherry", "Pears"]
list_2 = list_1

print(list_1)
print(list_2)

list_2.remove("Bananas")
print(list_1)
print(list_2)

list_1.insert(1,"Bananas")

list_2 = list_1.copy()
list_2.remove("Bananas")
print(list_1)
print(list_2)