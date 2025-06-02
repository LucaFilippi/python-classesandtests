name = input("What is your name? ")

age = input("What is your age? ")

test1_str = input("Please enter the grade for the first test: ")
test1 = float(test1_str)

test2_str = input("Please enter the grade for the second test: ")
test2 = float(test2_str)

final_average = (test1 + test2) / 2

print("\n--- Student Summary ---")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"First Test Grade: {test1:.2f}")
print(f"Second Test Grade: {test2:.2f}")
print(f"Final Average: {final_average:.2f}")