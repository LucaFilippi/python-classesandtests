family = ["Luca", "Matteo", "Maria"]
#           0      1         2
print (family[0])
print (family[1])
print (family[2])

print (family[1:])

print (family[0:2])

family[2] = "Maria Fernanda"
print (family)

family.extend(["Claudia", "Peterson"])
print(family)

family.append("Bella")
print(family)

family.insert(3,"Snow")
print(family)

family.pop()
family.pop()
family.pop()

family.remove("Snow")
print(family)

## family.clear()
## print(family)

family_age = [19, 16, 11]
print(family_age)

family_age.sort()
print(family_age)

family.sort()
print(family)
