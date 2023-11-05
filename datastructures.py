# list
myList = ["Abdi", "Lameq", "Zaira", 'Abdul']
print(myList)
print(f"My name is {myList[0]}")
print("My name is " + myList[0])
# sorting the list for instance
myList = ["Abdi", "Lameq", "Zaira", 'Abdul']
myList.sort()
print(myList)

# let us ceck te list for numbers
myList2 = [19, 99, 11, 9, 29, 69, 49, -3]
myList2.sort()
print(f"My sorted list {myList2}")

# tuple- is immutable and ordered
my_tuple = ("Kenya", "Rwanda", "Burundi", "Ethiopia")
print(my_tuple)
print(f"my country is {my_tuple[0]}")

# set -unordered
fruits = {"Oranges", "Pineapples", "Apples", "Banana", "Apples"}
print(fruits)

# dictionaries
employees = {"Name": "Abdi", "Age": 30, "Gender": "Male", "Salary": 619000}

print("Employees name :%s" % employees["Name"])
print("Employees age :%s" % employees["Age"])
