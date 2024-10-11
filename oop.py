#Lab 5
#Qno1:


# class Item:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def display_info(self):
#         print(f'Title: {self.title}')
#         print(f'Author: {self.author}')

# if __name__ == "__main__":
#     item = Item("To Kill a Mockingbird", "Harper Lee")
#     item.display_info()

#Qno2:

class Item:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')


class Book(Item):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def additional_info(self):
        print(f'Pages: {self.pages}')


class Magazine(Item):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def additional_info(self):
        print(f'Issue Number: {self.issue_number}')

if __name__ == "__main__":
    book = Book("harry potter", "j.k rowling", 224)
    magazine = Magazine("jane austen", "huge", 202)

    print("Book Information:")
    book.display_info()
    book.additional_info()

    print("\nMagazine Information:")
    magazine.display_info()
    magazine.additional_info()

