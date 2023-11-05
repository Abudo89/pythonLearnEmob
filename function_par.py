def students(fullname, age, gender, course, school):
    print(f"{fullname} is :{age} years of age pursuing "
          f"{course} in {school} and gender {gender}")


students("Abdi Abudo", 30,"male", "Bachelors Degree in IT", "JKUAT")


def square(num):
    return num**2
answer=square(9)
print(f"The square is {answer}")
