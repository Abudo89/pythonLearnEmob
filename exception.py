# name="Abudo"
#
# for i in name:
#     if i !=0:
#         print(i)

fruits = ["Apple", "Banana", "Citrus"]
try:
    for i in range(6):
        print(f"The index and element from the list is {i, fruits[i]}")
except:
    print("index out of range")