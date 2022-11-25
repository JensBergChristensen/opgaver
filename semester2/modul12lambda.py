"""
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

my_list = [1,2,3,4,5]
my_new_list = list(filter(lambda a: a % 2 == 0, my_list))

print(my_new_list)

"""

list_of_names = ["John", "Bob", "Mary", "Sue", "Joe", "Mike", "Sally", "longname", "shortname", "verylongname", "veryshortname", "veryverylongname", "veryveryshortname", "anna", "anorld"]
x = list(filter(lambda a: 10 > len(a) > 5, list_of_names))
print(x)

# use map to create a list with length of each name
z = list(map(lambda a: len(a), list_of_names))
print(z)

# make list upeprcase
y = list(map(lambda a: a.upper(), list_of_names))

