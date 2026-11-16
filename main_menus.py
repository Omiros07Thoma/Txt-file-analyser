import os
import book_analysis as ba
import compare_books as compare


def create_list_of_books():
    list_of_books = []
    for i in os.listdir(r"C:\Users\othom\project"):
        if i.endswith('.txt'):
            list_of_books.append(i)
    return list_of_books


#this function gives us the menu for a single book.
def single_file_menu():
    list_of_books = create_list_of_books()
    for i in range(len(list_of_books)):
        print(f"{i + 1}. {list_of_books[i]}")
    print("0. Return to main menu")
    n = int(input("Enter the number of the book you want to analyze: "))
    if n == 0:
        main_menu()
    elif 1 <= n <= len(list_of_books):
        selected_book = list_of_books[n - 1]
        ba.open_single_book(selected_book)
        main_menu()
    else:
        print("Invalid selection. Please try again.")
        single_file_menu()

#this function gives us the menu for comparing books from a list of books.
def compare_books():
    list_of_books = create_list_of_books()
    for i in range(len(list_of_books)):
        print(f"{i + 1}. {list_of_books[i]}")
    print("0. Return to main menu")
    n1 = int(input("Enter the number of the first book you want to compare: "))
    n2 = int(input("Enter the number of the second book you want to compare: "))
    if n1  == 0 or n2 == 0:
        main_menu()
    elif 1 <= n1 <= len(list_of_books) and 1 <= n2 <= len(list_of_books):
        book1 = list_of_books[n1 - 1]
        book2 = list_of_books[n2 - 1]
        compare.open_compared_books(book1, book2)
        main_menu()
    else:
        print("Invalid selection. Please try again.")
        compare_books()
        
        

        

    
        
#this function gives us the main menu for the program.
def main_menu():
    main_menu_selection = int(input('''
    Choose an option:
    1. Single book
    2. Compare books
    3. Exit
    '''))
    if main_menu_selection == 1:
        single_file_menu()

    elif main_menu_selection == 2:
        compare_books()

    elif main_menu_selection == 3:
        print("Exiting the program.")
        exit()
    else:
        print("Invalid selection. Please try again.")
        main_menu()    


if __name__ == "__main__":
    main_menu()