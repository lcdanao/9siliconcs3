class Publication: # Create the parent class Publication
    def __init__(self, title, author):
        # ATTRIBUTES
        self.__title = title
        self.__author = author
    # METHODS
    # Getter Methods
    def get_title(self):
        return self.__title
    def get_author(self):
    # Setter Methods
        return self.__author
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    # Display Information 
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")

class Book(Publication): # Create the child class Book (that inherits from Publication)
    def __init__(self, title, author, number_of_pages):
        # ATTRIBUTES
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages
    # METHODS
    def get_number_of_pages(self):
        return self.__number_of_pages
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0: # Ensures that the number of pages is positive
            self.__number_of_pages = number_of_pages 
        else:
            print("Number of pages must be positive.")

class Magazine(Publication): # Create the child class Magazine (that inherits from Publication)
    def __init__(self, title, author, issue_number):
            # ATTRIBUTES
            super().__init__(title, author)
            self.__issue_number = issue_number
    # METHODS
    def get_issue_number(self):
        return self.__issue_number
    def set_issue_number(self, issue_number):
        if issue_number > 0: # Ensures that the issue number is positive
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive.")


# Creating Objects
pub1 = Publication("The Diary of a Young Girl", "Anne Frank")
book1 = Book("The Lightning Thief", "Rick Riordan", 377)
mag1 = Magazine("Vogue", "Various Authors", 217)

pub2 = Publication("The Origin of Species", "Charles Darwin")
book2 = Book("The Hunger Games", "Suzanne Collins", 374)
mag2 = Magazine("W Korea", "Various Authors", 404)

# Printing the Information (Set 1)
print("PUBLICATIONS Set 1")
# Publication Information
print("\nPublication Information:")
pub1.display_info()

# Book Information
print("\nBook Information:")
book1.set_number_of_pages(-377) # Triggers the validation message
book1.display_info()
print(f"Number of pages: {book1.get_number_of_pages()}")

# Magazine Information
print("\nMagazine Information:")
mag1.display_info()
print(f"Issue number: {mag1.get_issue_number()}")

# Printing the Information (Set 2)
print()
print("\nPUBLICATIONS Set 2")
# Publication Information
print("\nPublication Information:")
pub2.display_info()

# Book Information
print("\nBook Information:")
book2.display_info()
print(f"Number of pages: {book2.get_number_of_pages()}")

# Magazine Information
print("\nMagazine Information:")
mag2.set_issue_number(-404) # Triggers the validation message
mag2.display_info()
print(f"Issue number: {mag2.get_issue_number()}")