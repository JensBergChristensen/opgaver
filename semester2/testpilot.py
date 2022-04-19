""" take user input, if it was a number higher than 10, open windows calculator """
input_number = input("Please enter a number: ")
input_number = int(input_number)
if input_number > 10:
    import os
    os.system("calc")
else:
    print("Your number is not higher than 10")