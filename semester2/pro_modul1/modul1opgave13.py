import pickle
from pathlib import Path

def create_data():
    a_file = Path("data.pkl")
    if a_file.exists():
        pass
    else:
        a_file.touch(exist_ok=True)
        a_file = open("data.pkl", "wb")
        pickle.dump([], a_file)
        a_file.close()

def save_data(data_to_file):
    a_file = open("data.pkl", "wb")
    pickle.dump(data_to_file, a_file)
    a_file.close()

def load_data():
    a_file = open("data.pkl", "rb")
    output = pickle.load(a_file)
    #print(output)
    a_file.close()
    return output

def show_library(li_of_dict):
    number = len(li_of_dict)
    start = 0
    while number > start:
        print(start,": ",li_of_dict[start])
        start += 1

def create_book(li_of_dict):
    titel = input("Enter titel of book: ")
    author = input("Enter author of book: ")
    book = {
    "titel": titel,
    "author": author
    }
    li_of_dict.append(book)
    save_data(li_of_dict)

def delete_book(li_of_dict):
    show_library(li_of_dict)
    x = checkint("Enter the number of the book to delete: ")
    li_of_dict.pop(x)
    save_data(li_of_dict)

def checkint(s):
    run = True
    while run:
        tal = input(s)
        try:
            inttal = int(tal)
            run = False
        except ValueError:
            print("Please enter a valid option")
    return inttal


def menu(li_of_dict):
    while True:
        print("\nPress 1 to add new book.\nPress 2 to delete book.\nPress 3 to view all books.\nPress 4 to exit.\n")
        x = checkint("Select: ")
        if x == 1:
            print("adding new book\n")
            create_book(li_of_dict)
        elif x == 2:
            print("deleteing book\n")
            delete_book(li_of_dict)
        elif x == 3:
            print("All your books:\n")
            show_library(li_of_dict)

        elif x == 4:
            break
        else:
            print("wrong input")

def main():
    create_data()
    data = load_data()
    menu(data)
    save_data(data)

if __name__ == '__main__':
    main()
