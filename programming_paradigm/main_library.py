# main_book_library.py

from library_management import Book, Library

def main():
    # Create a library
    library = Library()
    
    # Add some books to the library
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("The Catcher in the Rye", "J.D. Salinger"))

    print("Available books after setup:")
    library.list_available_books()

    # Check out a book
    title_to_checkout = "1984"
    success = library.check_out_book(title_to_checkout)
    if success:
        print(f"\nChecked out '{title_to_checkout}' successfully.")
    else:
        print(f"\nCould not check out '{title_to_checkout}'. Maybe it's already checked out or not available.")

    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Try returning the book
    title_to_return = "1984"
    success = library.return_book(title_to_return)
    if success:
        print(f"\nReturned '{title_to_return}' successfully.")
    else:
        print(f"\nCould not return '{title_to_return}'. Maybe it was not checked out.")

    print("\nAvailable books after returning '1984':")
    library.list_available_books()


if __name__ == "__main__":
    main()
