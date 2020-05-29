 # custom-functions/my_functions.py

# TODO: define temperature conversion function here

def celsius_to_fahrenheit(x):
    return ((x*9/5)+32)

# TODO: define gradebook function here

def numeric_to_letter_grade(n):
    if n < 60:
        return "F"
    if n < 70:
        return "D"
    if n < 80:
        return "C"
    if n < 90:
        return "B"
    else:
        return "A"


if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = 0
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

    print("--------------------")
    score = 87.5
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)