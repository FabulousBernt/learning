# Error Handling 1

while True:
    try:
        age = int(input("what is your age? "))
        print(age)
        10/age
    except ValueError:
        print("Age must be a number.")
        continue
    except ZeroDivisionError:
        print("Age must be higher than 0.")
        continue
    else:
        print("Great age")
        break
    finally:
        print("Ok, I'm finally done.")

# # Error Handling 2
# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(f"Please enter numbers only. {err}")
#
# print(sum('1', 2))